#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int array[100];
    int angka=1;
    int maxi=0;
    int n,temp;
    cin >>n;
    
    for(int i=0; i<n; i++){
        cin >> array[i];
    }
    
    sort(array, array+n);
    
    for(int i=0; i<n-1; i++){
        angka=1;
        for(int j=i+1; j<n; j++){
            if(array[j]-array[i]<=1){
                angka++;
                maxi=max(angka,maxi);
            }
        }
        maxi=max(angka,maxi);
    }
    cout << maxi;
    
    return 0;
}
