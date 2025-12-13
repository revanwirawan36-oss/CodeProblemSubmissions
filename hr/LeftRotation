#include <iostream>
using namespace std;

int main(){
    int n,d;
    int angka[100000];
    int temp[100000];
    int index=0;
    cin>>n>>d;
    
    for(int i=0; i<n; i++){
        cin>>angka[i];
    }
    for(int i=0; i<d;i++){
        temp[i]=angka[i];
    }
    for(int i=d; i<n; i++){
        angka[i-d]=angka[i];
    }
    for(int i=n-d; i<n; i++){
        angka[i]=temp[index++];
    }
    for(int i=0; i<n; i++){
        cout<<angka[i]<<" ";
    }
    return 0;
}
