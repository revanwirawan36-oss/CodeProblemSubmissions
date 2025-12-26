#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    long n;
    long stick[100000];
    long hitung=0;
    cin>>n;
    for(int i=0; i<n; i++){
        cin>> stick[i];
        if(stick[i]>0) hitung++;
    }
    sort(stick,stick+n);
    cout <<hitung <<endl;
    int min=stick[0];
    while(hitung>0){
        hitung=0;
            sort(stick,stick+n);
            for(int i=0; i<n; i++){
                if(stick[i]>0){
                    min=stick[i];
                    break;
                }
            }
        
        for(int i=0; i<n; i++){
            stick[i]=stick[i]-min;
            if(stick[i]>0) hitung++;
        }
       
        if(hitung!=0)cout <<hitung<<endl;
        
    }
    return 0;
}
