#include <iostream>
#include <algorithm>
using namespace std;
string organizingContainers(long container[][100], int n){
    long type[1000]={0};
    long ball[1000]={0};
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            ball[i]+=container[i][j];
            type[i]+=container[j][i];
        }
    }
    sort(ball,ball+n);
    sort(type,type+n);
    for(int i=0; i<n; i++){
        if(ball[i]!=type[i]){
            return "Impossible";
        }
    }
    return "Possible";
}
int main(){
    int q;
    int n;
    long container[100][100];
    cin>>q;
    while(q--){
        cin>>n;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                cin>>container[i][j];
            }
        }
        cout<<organizingContainers(container,n)<<endl;
    }
    return 0;
}
