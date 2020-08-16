// Source: https://github.com/OneLoneCoder/videos/blob/master/OneLoneCoder_Tetris.cpp

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <iostream>
#include <Windows.h>
// main function - 
// where the execution of program begins 
using namespace std;

wstring tetromino[7];
int nFieldWidth = 12;
int nFieldHeight = 18;
unsigned char *pField = nullptr;

int nScreenWidth = 80;
int nScreenHeight = 30;

int rotate(int x, int y, int r) {
    switch (r % 4)
    {
    case 0: return y * 4 + x;       // 0 degrees
    case 1: return 12 + y - 4 * x;  // 90 degrees
    case 2: return 15 - 4 * y - x;  // 180 degrees
    case 3: return 3 + y + 4 * x;   // 270 degrees
    }
    return 0;
}

int main()
{
    // prints hello world 
    printf("Hello Tetris");

    // Create assets
    tetromino[0].append(L"..X.");
    tetromino[0].append(L"..X.");
    tetromino[0].append(L"..X.");
    tetromino[0].append(L"..X.");

    tetromino[1].append(L"..X.");
    tetromino[1].append(L".XX.");
    tetromino[1].append(L".X..");
    tetromino[1].append(L"....");

    tetromino[2].append(L".X.");
    tetromino[2].append(L".XX.");
    tetromino[2].append(L"..X.");
    tetromino[2].append(L"....");

    tetromino[3].append(L"....");
    tetromino[3].append(L".XX.");
    tetromino[3].append(L".XX.");
    tetromino[3].append(L"....");

    tetromino[4].append(L"..X.");
    tetromino[4].append(L".XX.");
    tetromino[4].append(L"..X.");
    tetromino[4].append(L"....");

    tetromino[5].append(L"....");
    tetromino[5].append(L".XX.");
    tetromino[5].append(L"..X.");
    tetromino[5].append(L"..X.");

    tetromino[6].append(L"....");
    tetromino[6].append(L".XX.");
    tetromino[6].append(L".X..");
    tetromino[6].append(L".X..");

    pField = new unsigned char[nFieldHeight * nFieldWidth]; //Create new playing field
    for (int i = 0; i < nFieldWidth; i++)
    {
        for (int j = 0; i < nFieldHeight; j++)
        {
            pField[j * nFieldWidth + i] = (i == 0 || i == nFieldWidth - 1 || j == nFieldHeight - 1) ? 9 : 0;
        }
    }

    wchar_t *screen = new wchar_t[nScreenWidth * nScreenHeight];
    
    for (int i = 0; i < nScreenWidth * nScreenHeight; i++)
    {
        screen[i] = L' ';
    }

    HANDLE hConsole = CreateConsoleScreenBuffer(GENERIC_READ | GENERIC_WRITE, 0, NULL, CONSOLE_TEXTMODE_BUFFER, NULL);
    SetConsoleActiveScreenBuffer(hConsole);
    DWORD dwBytesWritten = 0;
    
    bool isGameOver = false;

    while (!isGameOver) {

        // Draw Field
        for (int i = 0; i < nFieldWidth; i++)
        {
            for (int j = 0; j < nFieldHeight; j++)
            {
                screen[(j + 2) * nScreenWidth + (i + 2)] = L" ABCDEFG=#"[pField[j * nFieldWidth + i]];
            }
        }

        // Display Frame
        WriteConsoleOutputCharacter(hConsole, screen, nScreenWidth * nScreenHeight, { 0,0 }, &dwBytesWritten);
    }


    return 0;
}