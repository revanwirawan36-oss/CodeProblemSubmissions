#include <iostream>
using namespace std;

void ngeprin(int* grades, int n){
    for(int i=0; i<n; i++){
        if(grades[i]>=38){
            int hitung=0;
            while(grades[i]%5!=0){
                grades[i]++;
                hitung++;
                if(hitung==3){
                    grades[i]-=3;
                    break;
                }
            }
        } cout<<grades[i]<<endl;
    }
}
void jalan(){
    int grades[100001];
    int n;
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>grades[i];
    }
    
    ngeprin(grades,n);
}

int main(){
    jalan();
}
