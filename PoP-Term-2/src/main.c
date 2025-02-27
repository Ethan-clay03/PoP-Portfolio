#include "raylib.h"
#include <stdio.h>

#define ROWS 6
#define COLUMNS 7
#define CELL_SIZE 64

enum Cell {
    EMPTY,    // 0 = Empty cell
    PLAYER1,  // 1 = Player 1
    PLAYER2   // 2 = Player 2
};

enum Cell board[ROWS][COLUMNS] = { { EMPTY } };  // Set all cells to empty

enum Cell current_player = PLAYER1;  // Start with Player 1
bool game_won = false;               // Has game been won?
char win_message[64] = "";           // Win message

void draw_board();
bool check_win(enum Cell player);

int main(void) {
    InitWindow(COLUMNS * CELL_SIZE, ROWS * CELL_SIZE + 50, "Connect 4");

    while (!WindowShouldClose()) {
        if (!game_won && IsMouseButtonPressed(MOUSE_BUTTON_LEFT)) {
            int column = GetMouseX() / CELL_SIZE;  // Get the column based on X co-ordinate
            // Check bottom to top to find next available free space
            for (int row = ROWS - 1; row >= 0; row--) {
                if (board[row][column] == EMPTY) {
                    // Place the piece for the current player when free space found
                    board[row][column] = current_player;

                    // Check if move wins the game
                    if (check_win(current_player)) {
                        game_won = true; 
                        sprintf(win_message, "Player %d Wins!", current_player);  // Winner message
                    }

                    // Switching player
                    current_player = (current_player == PLAYER1) ? PLAYER2 : PLAYER1;
                    break;  
                }
            }
        }

        BeginDrawing();
        ClearBackground(RAYWHITE); 

        draw_board();  // Re-draw board
        if (game_won) {
            DrawText(win_message, 10, ROWS * CELL_SIZE + 10, 20, BLACK);  //Winner message
        }

        EndDrawing();
    }

    CloseWindow();
    return 0;
}


void draw_board() {
    // Go through entire board drawing circles
    for (int row = 0; row < ROWS; row++) {
        for (int col = 0; col < COLUMNS; col++) {
            Color cell_color;

            // Draw 
            if (board[row][col] == PLAYER1) {
                cell_color = RED;
            }
            else if (board[row][col] == PLAYER2) {
                cell_color = YELLOW;
            }
            else {
                cell_color = LIGHTGRAY;
            }

            // Draw circle (raylib method)
            DrawCircle(col * CELL_SIZE + CELL_SIZE / 2, row * CELL_SIZE + CELL_SIZE / 2, CELL_SIZE / 2 - 5, cell_color);
        }
    }
}

bool check_win(enum Cell player) {
    // Horizontal
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

    // Vertical
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

    // Top Left bottom right
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

    // Top-right to bottom left
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
