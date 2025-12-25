#include <iostream>
using namespace std;

int main(){
    int n,k;
    cin>>n>>k;
    int c[100000];
    for(int i=0; i<n; i++){
        cin >> c[i];
    }
    int e=100;
    int start=0;
    while(true){
        if(c[start]==0) e--;
        else e-=3;
        start+=k;
        start%=n;
        if(start==0) break;
    }
    cout <<e;
    return 0;
}
