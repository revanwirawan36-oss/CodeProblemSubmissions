#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
   int n,q,a,b;
   cin >>n >>q;
   
   int *arr[100000];
   int size[100000];
   
   for(int i=0; i<n; i++){
    cin >> size[i];
    arr[i]= new int[size[i]];
    
    for(int j=0; j<size[i]; j++){
        cin >> arr[i][j];
    }
   }
   
   for(int i=0; i<q; i++){
    cin >>a>>b;
    cout << arr[a][b] << endl;
   }
   for(int i=0; i<n; i++){
    delete[] arr[i];
   }
    return 0;
}
