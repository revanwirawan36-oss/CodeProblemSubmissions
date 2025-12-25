#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;
string numberToString(long a){
    if(a==0) return "0";
    string s="";
    while(a>0){
        int digit= a%10;
        s+=(char)(digit+'0');
        a/=10;
    }
    
    reverse(s.begin(),s.end());
    return s;
}
void kaprekar(long a, long& itung){
    long kuadrat=(long)a*a;
    string ori=numberToString(a);
    long d=ori.length();
    string s=numberToString(kuadrat);
    long n=s.length();
    string depan,belakang;
    long kiri, kanan;
    
    if(n!=d){
    depan=s.substr(0,n-d);
    belakang=s.substr(n-d,n);
    
    kiri=stol(depan);
    kanan=stol(belakang);
    
    if(kiri+kanan==a){
        cout << a<< " ";
        itung++;
    }
    }
}

int main(){
    long p,q;
    cin>>p>>q;
    long itung=0;
    if(p==1){
        cout << 1 << " ";
        p++;
        itung++;
    }
    
    for(int i=p; i<=q; i++){
        kaprekar(i,itung);
    }
    if(itung==0){
        cout <<"INVALID RANGE";
    }
    return 0;
}
