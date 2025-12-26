#include <iostream>
#include <string>
using namespace std;
long long berapaA(string s, long long n){
    if(s=="a") return n;
    long long ah=0;
    long long tambah=0;
    long long sisa=n%s.length();
    for(int i=0; i<s.length(); i++){
        if(s[i]=='a') ah++;
        if(s[i]=='a'&&i<sisa) tambah++;
    }
    long long rep=n/s.length();
    ah=(ah*rep)+tambah;
    return ah;
}
int main(){
    string s;
    long long n;
    cin>>s>>n;
    cout<<berapaA(s,n);
    return 0;
}
