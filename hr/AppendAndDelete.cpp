#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main(){
    string s,t;
    long k;
    long hitung=0;
    cin>>s>>t>>k;
    long teh=t.length();long seh=s.length();
    long maksN=max(teh,seh);
    long minN=min(teh,seh);
    long indeks=minN;
    for(int i=0; i<maksN; i++){
        if(t[i]!=s[i]){
            indeks=i;
            break;
        }
    }
    
    hitung+=abs(seh-indeks);
    hitung+=abs(teh-indeks);
  
    
    bool bisa=false;
    if(hitung<=k){
        int sisa=k-hitung;
        if(sisa%2==0){
            bisa=true;
        }
    }
    
    
    if (k >= seh + teh) {
        cout << "Yes";
    } else if (k >= hitung && bisa) {
        cout << "Yes";
    } else {
        cout << "No";
    }
    return 0;
}
