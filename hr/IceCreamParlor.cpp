#include <iostream>
using namespace std;

int main(){
    int t;
    int m;
    int n;
    cin >> t;
    
    for(int i=0; i<t; i++){
        cin >>m;
        cin >>n;
        bool udah=false;
        int cost[n];
        for(int j=0; j<n; j++){
            cin >> cost[j];
        }
        for(int j=0; j<n; j++){
            for(int k=0; k<n; k++){
                if(j==k){
                    continue;
                }
                if(cost[j]+cost[k]==m){
                    cout << j+1 << " " << k+1 << '\n';
                    udah=true;
                    break;
                }
            }
            if(udah) break;
        }
        cost[n]={0};
    }
    return 0;
}
