#include <iostream>
using namespace std;

int main(){
     int n;
     int t;
     int angka=1;
     cin >>n;
     
     for(int i=0; i<n; i++){
        angka=1;
        cin >>t;
        for(int i=1; i<=t; i++){
            if(i%2==0){
                angka+=1;
            } else{
                angka*=2;
            }
        } cout << angka << endl;
     }
     
    return 0;
}
