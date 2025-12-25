#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
long minim(long n, long* clouds){
    bool dua=true;
    for(long i=0; i<n; i+=2){
        if(clouds[i]==1){
            dua=false;
            break;
        }
    } if(dua){
        return n/2;
    }
    long lompat=0;
    for(long i=0; i<n; i++){
        if(i==n-1){
            break;
        }
        if(clouds[i+1]==1){
            lompat++;
            i++;
            continue;
        }else if(clouds[i+2]==0){
            lompat++;
            i++;
            continue;
        }else{
            lompat++;
        }
    }
    return lompat;
}

int main(){
    long clouds[100000];
    long n;
    cin>>n;
    for(long i=0; i<n; i++){
        cin>>clouds[i];
    }
    cout<<minim(n,clouds);
    return 0;
}
