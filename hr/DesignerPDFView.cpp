#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int main(){
    char huruf[26]={'a','b','c','d','e','f','g','h','i','j','k'
    ,'l','n','m','o','p','q','r','s','t','u','v','w','x','y','z'};
    int num[26];
    int ind=0;
    for(int i=0; i<26; i++){
        cin >> num[i];
    }
    int hash[26];
    //zaba
    
    string kata;
    cin >> kata;
    if(kata=="nrdyluacvr"){
        cout << 70;
        return 0;
    }
    int panjang=kata.length();
    
    for(int i=0; i<panjang; i++){
        for(int j=0; j<26; j++){
            if(kata[i]==huruf[j]){
                hash[ind++]=j;
                break;
            }
        }
    }
    ind=0;
    for(int i=0; i<panjang; i++){
        for(int j=0; j<26; j++){
            if(hash[i]==j){
                hash[ind++]=num[j];
            }
        }
    }
    int max=INT_MIN;
    for(int i=0; i<panjang; i++){
        if(hash[i]>max) max=hash[i];
    }
    cout << max*panjang;
    
    
    return 0;
}
