#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
int minDis(long* arr, int n){
    int currVal;
    int mini=INT32_MAX;
    bool ada=false;
    for(int i=0; i<n-1; i++){
        for(int j=i+1; j<n; j++){
            if(arr[i]==arr[j]){
                ada=true;
                currVal=abs(i-j);
                mini=min(mini,currVal);
            }
        }
    }
    if(!ada) return -1;
    return mini;
}
void utama(){
    int n;
    cin>>n;
    long arr[100001];
    
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }
    cout<<minDis(arr,n);
}
int main(){
    utama();
}
