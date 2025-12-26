#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

// This function checks if a 1D array of 9 numbers forms a Magic Square
bool isMagic(int p[]) {
    // Check rows
    if (p[0] + p[1] + p[2] != 15) return false;
    if (p[3] + p[4] + p[5] != 15) return false;
    if (p[6] + p[7] + p[8] != 15) return false;
    // Check columns
    if (p[0] + p[3] + p[6] != 15) return false;
    if (p[1] + p[4] + p[7] != 15) return false;
    if (p[2] + p[5] + p[8] != 15) return false;
    // Check diagonals
    if (p[0] + p[4] + p[8] != 15) return false;
    if (p[2] + p[4] + p[6] != 15) return false;

    return true;
}

int main() {
    int mat[9]; // Flatten the 3x3 to a 1D array for easier comparison
    for (int i = 0; i < 9; i++) {
        cin >> mat[i];
    }

    // Start with the numbers 1-9 in order
    int p[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int min_cost = 1000;

    // next_permutation will try every single combination of 1-9
    do {
        if (isMagic(p)) {
            int current_cost = 0;
            for (int i = 0; i < 9; i++) {
                current_cost += abs(mat[i] - p[i]);
            }
            // If this magic square is cheaper than the last one, save it
            if (current_cost < min_cost) {
                min_cost = current_cost;
            }
        }
    } while (next_permutation(p, p + 9));

    cout << min_cost << endl;

    return 0;
}
