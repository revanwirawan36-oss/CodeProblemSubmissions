#include <iostream>
#include <algorithm>
using namespace std;
struct simpan{
    int x=0;
    bool udah=false;
};
int gemStones(string* katas, int n){
    simpan save[26];
    int hitung=0;
    for(int i=0; i<n; i++){
        int p=katas[i].length();
        for(int i=0; i<26; i++){
            save[i].udah=false;
        }
        for(int j=0; j<p; j++){
            if(save[(int)katas[i][j]-97].udah==false){
                save[(int)katas[i][j]-97].x++;
                save[(int)katas[i][j]-97].udah=true;
            } 
        }
    }
    for(int i=0; i<26; i++){
        if(save[i].x==n){
            hitung++;
        }
    }
    return hitung;
}
void utama(){
    string katas[101];
    int n;
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>katas[i];
    }
    cout<<gemStones(katas,n);
}
int  main(){
    utama();
}
