#include <iostream>

class Board {
    private:
    int rows;
    int columns;
    int space[][];

    public:
    Board(int r, int c) {
        rows = r;
        columns = c;
    }

    void printBoard() {
        for (int i = 0; i < sizeof(rows); i++) {
            for (int j = 0; j < sizeof(columns); j++) {
                std::cout << Board[i][j];
            }
        }
    }
};