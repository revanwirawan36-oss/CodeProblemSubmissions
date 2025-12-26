#include <iostream>
using namespace std;
int equ(int n, int* arr){
    for(int i=0; i<n; i++){
        arr[arr[i]+100]++;
    }
    int max=0;int indeks=0;int hitung=0;
    for(int i=0; i<=100; i++){
        if(arr[i+100]>max){
            max=arr[i+100];
            indeks=100+i;
    }
    }
    for(int i=0; i<=100; i++){
        if(i+100==indeks){
            continue;
        }
        hitung+=arr[i+100];
    }
    return hitung;
}
int main(){
    int n;
    int arr[201]={0};
    
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }
    cout<<equ(n,arr);
    return 0;
}
