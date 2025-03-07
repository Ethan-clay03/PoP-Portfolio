#include "raylib.h"
#include <stdio.h>
#include <string.h>
#include "connect4.c"

// Variables for main menu
bool showMainMenu = true;
bool showNameScreen = false;
char player1Name[64] = "";
char player2Name[64] = "";
bool enterPlayer1Name = true;

void validateGameNames() {
    if (strlen(player1Name) == 0) {
        strcpy(player1Name, "Player 1");
    }
    if (strlen(player2Name) == 0) {
        strcpy(player2Name, "Player 2");
    }
}

bool IsMouseOverButton(Rectangle button) {
    Vector2 mousePoint = GetMousePosition();
    return CheckCollisionPointRec(mousePoint, button);
}

void HandlePlayerNameInput() {
    int key = GetKeyPressed();
    char* currentPlayerName = enterPlayer1Name ? player1Name : player2Name;
    if (key >= 32 && key <= 126) {
        int len = strlen(currentPlayerName);
        if (len < 63) {
            currentPlayerName[len] = (char)key;
            currentPlayerName[len + 1] = '\0';
        }
    }
    if (IsKeyPressed(KEY_ENTER)) {
        //Set flag to false to show player 2
        if (enterPlayer1Name) {
            enterPlayer1Name = false;
        //Second enter is player 2, show game screen
        } else {
            showNameScreen = false;
        }
    }
    if (IsKeyPressed(KEY_BACKSPACE)) {
        int len = strlen(currentPlayerName);
        if (len > 0) {
            currentPlayerName[len - 1] = '\0';
        }
    }
}

void ShowMainMenu(Rectangle startButton, Rectangle nameButton) {
    DrawText("Connect 4 Game", 100, 100, 20, BLACK);
    if (IsMouseOverButton(startButton)) {
        DrawRectangleRec(startButton, LIGHTGRAY);
        if (IsMouseButtonPressed(MOUSE_BUTTON_LEFT)) {
            showMainMenu = false;
        }
    } else {
        DrawRectangleRec(startButton, GRAY);
    }
    DrawText("Start Game (without names)", 110, 160, 20, BLACK);
    if (IsMouseOverButton(nameButton)) {
        DrawRectangleRec(nameButton, LIGHTGRAY);
        if (IsMouseButtonPressed(MOUSE_BUTTON_LEFT)) {
            showMainMenu = false;
            showNameScreen = true;
        }
    } else {
        DrawRectangleRec(nameButton, GRAY);
    }
    DrawText("Start Game (name selection)", 110, 210, 20, BLACK);
}

void ShowNameScreen() {
    DrawText("Enter Player Names", 100, 100, 20, BLACK);
    if (enterPlayer1Name) {
        DrawText("Enter Player 1 Name:", 100, 150, 20, BLACK);
        DrawText(player1Name, 350, 150, 20, BLACK);
    } else {
        DrawText("Enter Player 2 Name:", 100, 150, 20, BLACK);
        DrawText(player2Name, 350, 150, 20, BLACK);
    }
    HandlePlayerNameInput();
}

int main(void) {
    InitWindow(COLUMNS * CELL_SIZE, ROWS * CELL_SIZE + 100, "Connect 4");

    Rectangle startButton = { 100, 150, 325, 40 };
    Rectangle nameButton = { 100, 200, 325, 40 };

    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(RAYWHITE);
        if (showMainMenu) {
            ShowMainMenu(startButton, nameButton);
        } else if (showNameScreen) {
            ShowNameScreen();
        } else {
            validateGameNames();
            gameStart();
        }
        EndDrawing();
    }

    CloseWindow();
    return 0;
}
