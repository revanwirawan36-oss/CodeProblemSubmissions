#include <iostream>
using namespace std;
void reverse(long *arr, long start, long end){
    int n= abs(end-start)+1;
    for(int i=start; i<start+(n/2); i++){
        int temp=arr[i];
        arr[i]=arr[start+n-1-(i-start)];
        arr[start+n-1-(i-start)]=temp;
    }
}
void circularArrayRotation(long n, long k, long queries) {
    long arr[1000000];
    k%=n;
    for(long i=0; i<n; i++){
        cin>>arr[i];
    }
    reverse(arr,0,n-k-1);
    reverse(arr,n-k,n-1);
    reverse(arr,0,n-1);
    
    long q;
    while(queries--){
        cin>>q;
        cout << arr[q]<<endl;
    }
    return;
}

int main(){
   long n,queries;
   long k;
   cin>>n>>k>>queries;
   
   circularArrayRotation(n,k,queries);

    return 0;
}
