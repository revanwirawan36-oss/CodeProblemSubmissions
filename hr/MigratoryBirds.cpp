#include <iostream>
using namespace std;
int maxo(int a, int b, int c, int d, int e){
    int maksi=a;
    if(b>maksi) maksi=b;
    if(c>maksi) maksi=c;
    if(d>maksi) maksi=d;
    if(e>maksi) maksi=e;
    
    return maksi;
}

int main(){
    int angka[150000];
    int tipe1=0;
    int tipe2=0;
    int tipe3=0;
    int tipe4=0;
    int tipe5=0;
    int batas;
    cin >> batas;
    
    for(int i=0; i<batas; i++){
        cin >> angka[i];
    }
    for(int i=0; i<batas; i++){
        if(angka[i]==1){
            tipe1++;
        } else if(angka[i]==2){
            tipe2++;
        } else if(angka[i]==3){
            tipe3++;
        } else if(angka[i]==4){
            tipe4++;
        } else if(angka[i]==5){
            tipe5++;
        }
    }
    
    int maxi= maxo(tipe1,tipe2,tipe3,tipe4,tipe5);
    
    if(maxi==tipe1){
        cout << 1;
    } else if(maxi==tipe2){
        cout << 2;
    } else if(maxi==tipe3){
        cout << 3;
    } else if(maxi==tipe4){
        cout << 4;
    } else if(maxi==tipe5){
        cout << 5;
    }
    
    
    return 0;
}
