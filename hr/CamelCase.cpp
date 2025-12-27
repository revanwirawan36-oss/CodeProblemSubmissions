#include <iostream>
#include <algorithm>
using namespace std;

long jumlah(string s){
    long n=s.length(),jml=1;
    sort(s.begin(),s.end());
    for(long i=0; i<n; i++){
        if((long)s[i]>90){
            jml=i+1;
            break;
        }
    }
    return jml;
}
void utama(){
    string s;
    cin>>s;
    cout<< jumlah(s);
}
int main(){
    utama();
}
