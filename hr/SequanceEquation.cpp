#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int clone[10000];
    int indeks[10000];
    int angka[10000];
    int n;
    cin >>n;
    n+=1;
    for(int i=1; i<n; i++){
        cin >> angka[i];
        clone[i]=angka[i];
    }
    sort(clone+1,clone+n);
     for(int i=1; i<n; i++){
        for(int j=1; j<n; j++){
            if(clone[i]==angka[j]){
                indeks[i]=j;
                break;
            }
        }
    }
    for(int i=1; i<n; i++){
        for(int j=1;j<n;j++){
            if(indeks[i]==angka[j]){
                cout << j <<endl;
                break;
            }
        }
    }
    return 0;
}
