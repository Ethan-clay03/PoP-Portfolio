#include "raylib.h"

#define ROWS 6
#define COLUMNS 7
#define CELL_SIZE 100

enum Cell {
    EMPTY,
    PLAYER1,
    PLAYER2
};

enum Cell board[ROWS][COLUMNS] = { { EMPTY } };
enum Cell current_player = PLAYER1;
bool game_won = false;
char win_message[64] = "";

//Access player names from main.c
extern char player1Name[64];
extern char player2Name[64];

//Falling disc animation struct
typedef struct {
    bool active;
    int col;
    float y;
    Color color;
} FallingDisc;

FallingDisc fallingDisc = { false, 0, 0.0f, LIGHTGRAY };


void draw_board() {
    for (int row = 0; row < ROWS; row++) {
        for (int col = 0; col < COLUMNS; col++) {
            Color cell_color;
            if (board[row][col] == PLAYER1) {
                cell_color = RED;
            } else if (board[row][col] == PLAYER2) {
                cell_color = YELLOW;
            } else {
                cell_color = LIGHTGRAY;
            }
            DrawCircle(col * CELL_SIZE + CELL_SIZE / 2, row * CELL_SIZE + CELL_SIZE / 2, CELL_SIZE / 2 - 5, cell_color);
        }
    }
}


bool check_win(enum Cell player) {
    // Horizontal
    for (int row = 0; row < ROWS; row++) {
        for (int col = 0; col < COLUMNS - 3; col++) {
            if (board[row][col] == player && board[row][col + 1] == player && board[row][col + 2] == player && board[row][col + 3] == player) {
                return true;
            }
        }
    }
    // Vertical
    for (int row = 0; row < ROWS - 3; row++) {
        for (int col = 0; col < COLUMNS; col++) {
            if (board[row][col] == player && board[row + 1][col] == player && board[row + 2][col] == player && board[row + 3][col] == player) {
                return true;
            }
        }
    }
    // Top Left to Bottom Right
    for (int row = 0; row < ROWS - 3; row++) {
        for (int col = 0; col < COLUMNS - 3; col++) {
            if (board[row][col] == player && board[row + 1][col + 1] == player && board[row + 2][col + 2] == player && board[row + 3][col + 3] == player) {
                return true;
            }
        }
    }
    // Top Right to Bottom Left
    for (int row = 3; row < ROWS; row++) {
        for (int col = 0; col < COLUMNS - 3; col++) {
            if (board[row][col] == player && board[row - 1][col + 1] == player && board[row - 2][col + 2] == player && board[row - 3][col + 3] == player) {
                return true;
            }
        }
    }
    return false;
}


void AnimateFallingDisc(int animated_row, int animated_col, float *animated_y) {
    *animated_y += 10.0f;
    if (*animated_y >= animated_row * CELL_SIZE + CELL_SIZE / 2) {
        board[animated_row][animated_col] = current_player;
        if (check_win(current_player)) {
            game_won = true;
            sprintf(win_message, "%s Wins!", current_player == PLAYER1 ? player1Name : player2Name);
        }
        current_player = (current_player == PLAYER1) ? PLAYER2 : PLAYER1;
        *animated_y = -1.0f;  // Reset animation
    } else {
        DrawCircle(animated_col * CELL_SIZE + CELL_SIZE / 2, *animated_y, CELL_SIZE / 2 - 5, (current_player == PLAYER1) ? RED : YELLOW);
    }
}


void gameStart() {
    static int animated_row = -1;
    static int animated_col = -1;
    static float animated_y = 0.0f;

    if (animated_row >= 0) {
        AnimateFallingDisc(animated_row, animated_col, &animated_y);
        if (animated_y == -1.0f) {
            animated_row = -1;
        }
    } else if (!game_won && IsMouseButtonPressed(MOUSE_BUTTON_LEFT)) {
        int column = GetMouseX() / CELL_SIZE;
        for (int row = ROWS - 1; row >= 0; row--) {
            if (board[row][column] == EMPTY) {
                animated_row = row;
                animated_col = column;
                animated_y = 0.0f;
                break;
            }
        }
    }

    draw_board();
    if (game_won) {
        DrawText(win_message, 10, ROWS * CELL_SIZE + 10, 20, BLACK);
    }
}