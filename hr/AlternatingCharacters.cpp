#include <iostream>
#include <string>
using namespace std;
long alternatingChar(string s){
    long n=s.length();
    int idx=0;
    long itung=0;
    bool baru=false;
    for(int i=1; i<n; i++){
        if(!baru){
           if(s[i]==s[idx]){
            itung++;
            if(s[i+1]!=s[idx]&&i+1!=n){
                baru=true;
                idx=i+1;
                continue;
               // cout<<"idx baru: "<<idx<<endl;
            }
        } idx++;
        }else if(baru){
            baru=false;
           // cout<<"i skrg: "<< i<<endl;
            continue;
        }
    }
       return itung;
}
void utama(){
    int q;
    cin>>q;
    while(q--){
        string s;
        cin>>s;
        cout<<alternatingChar(s)<<endl;
    }
}
int main(){
    utama();
}
