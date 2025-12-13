#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    string kata;
    string hack = "hackerrank";

    for (int i = 0; i < n; i++) {
        cin >> kata;
        int panjang = kata.length();
        int temp = -1;
        bool valid = true;

       
        for (int h = 0; h < hack.length(); h++) {
            bool found = false;
            for (int j = temp + 1; j < panjang; j++) {
                if (kata[j] == hack[h]) {
                    temp = j;
                    found = true;
                    break;
                }
            }
            if (!found) {
                valid = false;
                break;
            }
        }

        if (valid)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}
