#include <iostream>
using namespace std;

int main(){
    string pukul;
    cin >> pukul;
    
    int kiri= pukul[0]-48;
    if(kiri==1) kiri=10;
    int kanan= pukul[1]-48;;
    int jam=kiri+kanan;
    
    if(pukul[8]=='A'){
        if(jam==12) jam=0;
    } else if(pukul[8]=='P'){
        if(jam<12) jam+=12;
    }
    
   if(jam<10) cout << 0;
   cout<<jam;
    for(int i=2; i<8; i++){
        cout << pukul[i];
    }
    return 0;
}
