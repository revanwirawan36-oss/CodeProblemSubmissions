#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;

string encryption(string s) {
    int n=s.length();
    string newS="";
    for(int i=0; i<n; i++){
        if(s[i]==' ') continue;
        newS+=s[i];
    }
    int newN=newS.length();
    string store[100000];
    string kata="";
    double akar=sqrt(newN);
    int bawah=akar,atas;
    if(bawah==akar){
        atas=bawah;
    }
    else{ 
        atas=bawah+1;
    }
    int idxSisa=newN%atas;
    while(bawah*atas<newN){
        bawah++;
    }
    // cout<<newS<<" "<<newN<<" "<< akar<<" "<<bawah<< " "<<atas<<" "<<idxSisa<<endl;
    
    for(int i=0; i<bawah; i++){
        if(i!=bawah-1){
            store[i]=newS.substr(i*atas,atas);
        }else if(i==bawah-1&&idxSisa==0){
            store[i]=newS.substr(i*atas,atas);
        }else{
            store[i]=newS.substr(i*atas,idxSisa);
        }
       // cout<<store[i]<<endl;
    }
    for(int i=0; i<atas; i++){
        for(int j=0; j<bawah; j++){
            if(i>=idxSisa&&j==bawah-1&&idxSisa!=0){
                continue;
            }
            kata+=store[j][i];
        }kata+=' ';
    }
   return kata;
}

int main()
{
    string s;
    getline(cin, s);
    
    encryption(s);
    string result = encryption(s);
    
    cout << result << "\n";
    
    return 0;
}
