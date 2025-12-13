#include <iostream>
using namespace std;


int main(){
    long n,m;
    long long b;
    long long keyboard[1000];
    long long drive[1000];
    long long maxthatcanbe=0;
    cin >> b >> n >>m;
    
    for(long i=0; i<n; i++){
        cin >>keyboard[i];
    }
    for(long i=0; i<m; i++){
        cin >> drive[i];
    }
    
    long mink=keyboard[0];
    for(long i=0; i<n; i++){
        if(keyboard[i]<mink) mink=keyboard[i];
    }
    long mind=drive[0];
    for(long i=0; i<m; i++){
        if(drive[i]<mind) mind=drive[i];
    }
    if(b<mind+mink){
        cout << -1;
        return 0;
    }
    for(long i=0; i<n; i++){
        for(long j=0; j<m; j++){
            if(((keyboard[i]+drive[j])>maxthatcanbe) && ((keyboard[i]+drive[j])<=b)){ maxthatcanbe=(keyboard[i]+drive[j]);
            }
        }
    }
    cout << maxthatcanbe;
    
    return 0;
}
