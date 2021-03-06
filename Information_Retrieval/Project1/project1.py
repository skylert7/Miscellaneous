import requests
from bs4 import BeautifulSoup
import time
import sys
import operator

tags = ["a", "abbr", "acronym", "address", "area", "b", "base", "bdo", "big", "blockquote", "body", "br", "button",
        "caption", "cite", "code", "col", "colgroup", "dd", "del", "dfn", "div", "dl", "DOCTYPE", "dt", "em",
        "fieldset", "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "html", "hr", "i", "img", "input", "ins", "kbd",
        "label", "legend", "li", "link", "map", "meta", "noscript", "object", "ol", "optgroup", "option", "p", "param",
        "pre", "q", "samp", "script", "select", "small", "span", "strong", "style", "sub", "sup", "table", "tbody",
        "td", "textarea", "tfoot", "th", "thead", "title", "tr", "tt", "ul", "var"]

text_file_extension = ['.txt', '.php', '.htm', '.html']

class WebCrawl():
    def __init__(self, domain, N):
        self.N = N # limit on the number of pages to retrieve
        self.domain = domain
        self.url = ""
        self.raw_content = ""
        self.content_dict = dict()
        self.disallow = list()
        self.allow = list()
        self.broken_links = list()
        self.non_text_urls = list()
        self.titles = dict()
        self.num_of_documents_indexed = 0
        self.document_matrix = dict()
        self.totalWordsInDocument = dict()

    def isNoIndexPage(self):
        soup = BeautifulSoup(self.raw_content, 'html.parser')
        meta_tag_content = soup.find_all(attrs={'content': 'noindex'})
        if len(meta_tag_content) > 0:
            return True
        return False

    def create_site_map(self):
        robots_content = []

        if self.isLocalRobotsTxt():
            robots_txt_file = open("robots.txt", "r")
            for line in robots_txt_file:
                robots_content.append(line)

        else:
            prefix = "https://"
            # Get a list of crawl-able site using robots.txt
            robot_url = prefix + self.domain + "/robots.txt"
            r = requests.get(robot_url)
            robots_content = r.content.decode('utf-8').split('\n')

        self.allow.append(prefix + self.domain)

        for i in robots_content:
            try:
                if i[0] == "#":
                    continue
            except:
                continue
            if i.split(": ")[0] == "Disallow":
                url = prefix + self.domain + i.split(": ")[1]
                self.disallow.append(url)

                #Check for non-text url
                if any(ext in url for ext in text_file_extension): # if any text ext found in the url
                    print('', end='')
                else: # if not found, append the url to non_text_urls
                    if url not in self.non_text_urls:
                        self.non_text_urls.append(url)

            if i.split(": ")[0] == "Allow":
                url = prefix + self.domain + i.split(": ")[1]
                self.allow.append(url)

                #Check for non-text url
                if any(ext in url for ext in text_file_extension): # if any text ext found in the url
                    print('', end='')
                else: # if not found, append the url to non_text_urls
                    if url not in self.non_text_urls:
                        self.non_text_urls.append(url)

    def parse_html_and_make_word_vector(self):
        soup = BeautifulSoup(self.raw_content, 'html.parser')
        content_list_of_each_tag = list()

        # put each tag into a list
        for tag in tags:
            content_of_tag = soup.find_all(tag)
            for content in content_of_tag:
                if content.string != None:
                    content_list_of_each_tag.append(content.string)


        # making document_matrix
        # {word: [(word count, url1), (word count, url2)]
        for i in range(len(content_list_of_each_tag)):
            for word in content_list_of_each_tag[i].split():
                if word not in self.document_matrix.keys():
                    self.document_matrix[word] = [(1, self.url)]
                else:
                    for i in range(len(self.document_matrix[word])):
                        if self.document_matrix[word][i][1] == self.url:
                            self.document_matrix[word][i] = (self.document_matrix[word][i][0] + 1, self.url)
                            break
                        else:
                            if i == len(self.document_matrix[word]) - 1:
                                self.document_matrix[word].append((1, self.url))

    def getTitle(self):
        for url in self.disallow:
            self.getRawContentFromTextFile(url)
            if self.raw_content == "":
                continue

            soup = BeautifulSoup(self.raw_content, 'html.parser')
            title_tag = soup.find_all('title')

            # Check for existing url in self.titles
            if url not in self.titles.keys():
                self.titles[url] = title_tag[0].string

            time.sleep(3)

        for url in self.allow:
            self.getRawContentFromTextFile(url)
            if self.raw_content == "":
                continue

            self.getRawContentFromTextFile(url)

            soup = BeautifulSoup(self.raw_content, 'html.parser')
            title_tag = soup.find_all('title')

            # Check for existing url in self.titles
            if url not in self.titles.keys():
                self.titles[url] = title_tag[0].string

            time.sleep(3)

    def isLocalRobotsTxt(self):
        try:
            file_object = open("robots.txt", "r")
        except:
            return False
        return True

    def getRawContentFromTextFile(self, url):
        try:
            r = requests.get(url)
            status_code = r.status_code
        except:
            self.raw_content = ""
            self.url = ""
            return

        if status_code != 200:
            print("Error encountered in {} with status code {}".format(url, status_code))
            self.broken_links.append(url)
            self.raw_content = ""
            self.url = ""
            return

        self.url = url #Keep track of what url is being processed
        self.raw_content = r.content.decode('utf-8')

    def getTotalWordsIndexed(self):
        return

    def crawl(self):
        self.create_site_map()

        self.getTitle()

        for i in range(len(self.allow)):
            url = self.allow[i]
            if url in self.non_text_urls:
                continue

            if i <= self.N:
                self.getRawContentFromTextFile(url=url)
                if self.isNoIndexPage(): # has meta tag of noindex, move on
                    continue

                #Check for duplicate
                if self.raw_content not in self.content_dict.values():
                    self.content_dict[url] = self.raw_content
                else: #if raw content exists in indexed pages, move on
                    continue

                self.parse_html_and_make_word_vector()
                self.num_of_documents_indexed = self.num_of_documents_indexed + 1
                time.sleep(4) # wait 4 second after crawling a single webpage

if __name__ == '__main__':
    N = 100 # limit on the number of pages to retrieve
    domain = "s2.smu.edu/~fmoore"
    # domain = "google.com"

    if len(sys.argv) >= 2:
        my_crawler = WebCrawl(sys.argv[1], sys.argv[2])
    else:
        my_crawler = WebCrawl(domain, N)

    my_crawler.crawl() # Run crawler

    print(my_crawler.titles)

    #Number of document indexed
    print("Number of document indexed")
    print(my_crawler.num_of_documents_indexed)

    #Term - Document Matrix
    print("Term - Document Matrix")
    print(my_crawler.document_matrix)

    #Top 20 common words
    print("20 common words")

    word_count = dict()

    for word in my_crawler.document_matrix.keys():
        total_word_count = 0
        for index in range(len(my_crawler.document_matrix[word])):
            total_word_count = total_word_count + my_crawler.document_matrix[word][index][0]
        word_count[word] = total_word_count

    sorted_word_count = dict(sorted(word_count.items(), key=operator.itemgetter(1), reverse=True))

    for i in range(20):
        print(list(sorted_word_count)[i])