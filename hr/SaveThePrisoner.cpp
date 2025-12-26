#include <iostream>
using namespace std;
int prisoners(int n, int m, int s){
    s-=1;
    s+=m;
    if(s>n) s%=n;
    if(s==0)s=n;
    return s;
}
int main(){
    int t,n,m,s;
    cin >> t;
    while(t--){
        cin>>n>>m>>s;
        
        cout <<prisoners(n,s,m)<<endl;
    }
    return 0;
}
