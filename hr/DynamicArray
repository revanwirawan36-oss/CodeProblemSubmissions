#include <iostream>
using namespace std;

int main(){
    int angka[6][6];
    int save[4][4];
    
    for(int i=0; i<6; i++){
        for(int j=0; j<6; j++){
            cin>>angka[i][j];
        }
    }
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            save[i][j]=angka[i][j]+angka[i][j+1]+angka[i][j+2]+angka[i+1][j+1]+angka[i+2][j]+angka[i+2][j+1]+angka[i+2][j+2];
        }
    }
    
    int max=-32767;
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            if(save[i][j]>max) max=save[i][j];
        }
    }
    cout << max;
    return 0;
}
