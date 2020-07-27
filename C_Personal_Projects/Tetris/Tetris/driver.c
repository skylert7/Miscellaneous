#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define ROWS 20
#define COLS 11
#define TRUE 1
#define FALSE 0
// main function - 
// where the execution of program begins 

typedef struct {
    char** array;
    int width, row, col;
} Shape;
Shape current;

void DeleteShape(Shape shape) {
    int i;
    for (i = 0; i < shape.width; i++) {
        free(shape.array[i]);
    }
    free(shape.array);
}

int main()
{

    // prints hello world 
    printf("Hello Tetris");

    return 0;
}