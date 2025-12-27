#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;
string funny(string s){
    int n=s.length();
    int bedaDepan;
    int bedaBelakang;
    for(int i=0; i<n-1; i++){
        bedaDepan=abs((int)s[i]-s[i+1]);
        bedaBelakang=abs((int)s[n-1-i]-s[n-2-i]);
        if(bedaBelakang!=bedaDepan) return "Not Funny";
    }
    return "Funny";
}
void utama(){
    int q;
    cin>>q;
    
    while(q--){
        string s;
        cin>>s;
        
        cout<<funny(s)<<endl;
    }
}
int main(){
    utama();
}
