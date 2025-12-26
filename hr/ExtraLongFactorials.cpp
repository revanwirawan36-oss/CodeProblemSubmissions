#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string multiply(string num, int n) {
    if (n == 0 || num == "0") return "0";
    
    string result = "";
    int carry = 0;

    // Multiply each digit from right to left
    for (int i = num.length() - 1; i >= 0; i--) {
        int product = (num[i] - '0') * n + carry;
        result += (product % 10) + '0';
        carry = product / 10;
    }
    while (carry) {
        result += (carry % 10) + '0';
        carry /= 10;
    }

    reverse(result.begin(), result.end());
    return result;
}

int main() {
    int n;
    cin >> n; 

    string factorial = "1";
    for (int i = 2; i <= n; i++) {
        factorial = multiply(factorial, i);
    }
    
    cout << factorial << endl;
    return 0;
}
