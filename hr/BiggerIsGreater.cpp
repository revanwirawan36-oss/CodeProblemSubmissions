#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
string lexi(string s){
    string cpy=s;
    sort(cpy.begin(),cpy.end());
    next_permutation(s.begin(),s.end());
    if(s==cpy){
        return "no answer";
    }
    return s;
    
}
void utama(){
    long t;
    cin>>t;
    while(t--){
        string s;
        cin>>s;
        cout<<lexi(s)<<endl;
    }
}
int main(){
    utama(); 
}
