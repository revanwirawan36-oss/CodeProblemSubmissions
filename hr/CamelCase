#include <iostream>
using namespace std;

int main(){
    char capital[] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    int angka=1;
    string kata;
    cin >> kata;
    
    int panjang=kata.length();
    
    for(int i=0; i<panjang; i++){
        for(int j=0; j<26; j++){
            if(kata[i]==capital[j]){
                angka++;
                break;
            }
        }
    }
    cout << angka;
    return 0;
}
