#include "raylib.h"
#include <stdio.h>  // Include this for sprintf

#define ROWS 6
#define COLUMNS 7
#define CELL_SIZE 64

typedef enum { EMPTY, PLAYER1, PLAYER2 } Cell;

Cell board[ROWS][COLUMNS] = { { EMPTY } };

int currentPlayer = PLAYER1;
bool gameWon = false;  // Declare gameWon
char winMessage[64] = "";  // Declare winMessage

// Function prototypes
void DrawBoard();
bool CheckWin(int player);

int main(void) {
    InitWindow(COLUMNS * CELL_SIZE, ROWS * CELL_SIZE + 50, "Connect 4");

    while (!WindowShouldClose()) {
        // Input
        if (!gameWon && IsMouseButtonPressed(MOUSE_BUTTON_LEFT)) {
            int column = GetMouseX() / CELL_SIZE;
            for (int row = ROWS - 1; row >= 0; row--) {
                if (board[row][column] == EMPTY) {
                    board[row][column] = currentPlayer;
                    if (CheckWin(currentPlayer)) {
                        gameWon = true;
                        sprintf(winMessage, "Player %d Wins!", currentPlayer);
                    }
                    currentPlayer = (currentPlayer == PLAYER1) ? PLAYER2 : PLAYER1;
                    break;
                }
            }
        }

        // Drawing
        BeginDrawing();
        ClearBackground(RAYWHITE);

        DrawBoard();

        if (gameWon) {
            DrawText(winMessage, 10, ROWS * CELL_SIZE + 10, 20, BLACK);
        }

        EndDrawing();
    }

    CloseWindow();
    return 0;
}

void DrawBoard() {
    for (int row = 0; row < ROWS; row++) {
        for (int col = 0; col < COLUMNS; col++) {
            Color color;
            if (board[row][col] == PLAYER1) color = RED;
            else if (board[row][col] == PLAYER2) color = YELLOW;
            else color = LIGHTGRAY;

            DrawCircle(col * CELL_SIZE + CELL_SIZE / 2, row * CELL_SIZE + CELL_SIZE / 2, CELL_SIZE / 2 - 5, color);
        }
    }
}

bool CheckWin(int player) {
    // Check horizontal
    for (int row = 0; row < ROWS; row++) {
        for (int col = 0; col < COLUMNS - 3; col++) {
            if (board[row][col] == player &&
                board[row][col + 1] == player &&
                board[row][col + 2] == player &&
                board[row][col + 3] == player) {
                return true;
            }
        }
    }

    // Check vertical
    for (int row = 0; row < ROWS - 3; row++) {
        for (int col = 0; col < COLUMNS; col++) {
            if (board[row][col] == player &&
                board[row + 1][col] == player &&
                board[row + 2][col] == player &&
                board[row + 3][col] == player) {
                return true;
            }
        }
    }

    // Check diagonal (bottom-left to top-right)
    for (int row = 0; row < ROWS - 3; row++) {
        for (int col = 0; col < COLUMNS - 3; col++) {
            if (board[row][col] == player &&
                board[row + 1][col + 1] == player &&
                board[row + 2][col + 2] == player &&
                board[row + 3][col + 3] == player) {
                return true;
            }
        }
    }

    // Check diagonal (top-left to bottom-right)
    for (int row = 3; row < ROWS; row++) {
        for (int col = 0; col < COLUMNS - 3; col++) {
            if (board[row][col] == player &&
                board[row - 1][col + 1] == player &&
                board[row - 2][col + 2] == player &&
                board[row - 3][col + 3] == player) {
                return true;
            }
        }
    }

    return false;
}
