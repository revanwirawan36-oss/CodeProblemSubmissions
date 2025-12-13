#include <iostream>
using namespace std;
void hilangkan(string &kata, int n){
    for(int i=0; i<n; i++){
        if(kata[i]==0){
            continue;
        }
        for(int j=0; j<n; j++){
            if(kata[j]==0||j==i){
                continue;
            }
            
            if(kata[j]==kata[i]){
                
                bool nol=true;
                
        if(j>i){
         for(int k=i+1; k<j; k++){
            if(kata[k]!=0){
                nol=false;
            }
        }
    } else{
        for(int k=j+1; k<i; k++){
            if(kata[k]!=0){
                nol=false;
                        }
                    }
                }
        if(nol){       
        kata[i]=0;
        kata[j]=0;
        break;
        }
            } 
        
        } 
    
    }
}
    
int cekada(string kata, int n){
    int ada=0;
    for(int i=0; i<n; i++){
        if(kata[i]!=0){
            ada=1;
        }
    }
    return ada;
}

void print(string kata, int n){
    for(int i=0; i<n; i++){
        if(kata[i]!=0){
            cout << kata[i];
        }
    }
}
int main(){
    string kata;
    bool ada=false;
    cin >> kata;
    
    int n= kata.length();
    hilangkan(kata,n);
    ada=cekada(kata,n);
    
    if(ada==1){
        print(kata,n);
    } else {
        cout << "Empty String";
    }
        
    return 0;
}
