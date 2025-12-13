#include <iostream>
using namespace std;

int main(){
    long batas;
    long angka=0;
    long lilin[100000];
    
    cin >> batas;
    for(int i=0; i<batas; i++){
        cin >> lilin [i];
    }
    long max=lilin[0];
    for(int i=0; i<batas; i++){
        if(lilin[i]>max){
            max=lilin[i];
        }
    }
    for(int i=0; i<batas; i++){
        if(lilin[i]==max){
            angka++;
        }
    }
    cout << angka;
    return 0;
}
