#include <iostream>
using namespace std;

int main(){
    int n;
    cin >>n;
    int matrix[100][100];
    
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> matrix[i][j];
        }
    }
    int kiri=0,kanan=0;
    for(int i=0; i<n; i++){
        kiri+=matrix[i][i];
        kanan+=matrix[i][n-1-i];
    }
    int deter=kiri-kanan;
    deter<0 ? deter*=-1:0;
    cout << deter;
    return 0;
}
