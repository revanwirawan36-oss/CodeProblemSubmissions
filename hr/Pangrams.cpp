#include <iostream>
using namespace std;

int main(){
    string kata;
    bool ada;
    getline(cin,kata);
    string alph="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int n=kata.length();
    
    for(int i=0; i<26; i++){
        ada=false;
        for(int j=0; j<n; j++){
            if(alph[i]==kata[j] || alph[i+26]==kata[j]){
                ada=true;
                break;
            }
        } if(!ada){
                cout << "not pangram"; return 0;
            }
    }
    
    cout << "pangram";
    return 0;
}
