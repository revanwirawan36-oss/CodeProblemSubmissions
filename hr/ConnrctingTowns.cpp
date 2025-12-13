#include <iostream>
using namespace std;

int main(){
    int t;
    int n;
    int routes[100]={0};;
    cin >>t;
    
    for(int i=0; i<t; i++){
        cin >>n;
        for(int i=0; i<n-1; i++){
            cin >> routes[i];
        }
        long long hasil=1;
        for(int i=0; i<n-1;i++){
            hasil*=routes[i];
            hasil%=1234567;
        }
        routes[100]={0};
        cout << hasil<< endl;
    }
    return 0;
}
