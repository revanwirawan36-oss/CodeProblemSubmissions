#include <iostream>
using namespace std;
string caesarCipher(string s, int n, int k){
    string kata="";
    for(int i=0; i<n; i++){
        bool lower=s[i]>=97&&s[i]<=122;
        bool upper=s[i]>=64&&s[i]<=90;
        if(lower||upper){
            if((s[i]+k>122&&lower)||(s[i]+k>90&&upper)){
                s[i]=(char)(s[i]+k-26);
            }else{
            s[i]=(char)(s[i]+k);
            }
        }
    }
   // cout<<(char)122;
    return s;
}
int main(){
    string s;
    int n,k;
    
    cin>>n>>s>>k;
    k=k%26;
    cout<<caesarCipher(s,n,k);
    
    return 0;
}
