#include <iostream>
#include <algorithm>
using namespace std;
int iniForMaks(string* bin, int n, int m){
    int hitung=0;
    int maks=INT32_MIN;
    for(int i=0; i<n-1; i++){
        for(int j=i+1; j<n; j++){
            hitung=0;
            for(int k=0; k<m; k++){
                if(bin[i][k]=='1'||bin[j][k]=='1'){
                    hitung++;
                }
            } maks=max(hitung,maks);
        }
    }
    
    return maks;
}

int iniForBerapa(string* bin, int maks, int n, int m){
    int hitungBrp=0;
    int hitung=0;
    for(int i=0; i<n-1; i++){
        for(int j=i+1; j<n; j++){
            hitung=0;
            for(int k=0; k<m; k++){
                if(bin[i][k]=='1'||bin[j][k]=='1'){
                    hitung++;
                }
            } if(hitung==maks){
                hitungBrp++;
            }
        }
    }
    return hitungBrp;
}
int main(){
    int n,m;
    cin>>n>>m;
    string bin[1000];
    
    for(int i=0; i<n; i++){
        cin>>bin[i];
    }
    
    cout<<iniForMaks(bin,n,m)<<endl<<iniForBerapa(bin, iniForMaks(bin,n,m),n,m);
    return 0;
}
