#include <iostream>
using namespace std;

int main(){
    string numbers= "0123456789";
    string lowercase= "abcdefghijklmnopqrstuvwxyz";
    string uppercase= "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string special= "!@#$%^&*()-+";
    int hash[4]={0,0,0,0};
    
    int n;
    cin >> n;
    
    char pass[100000];
    for(int i=0; i<n; i++){
        cin>>pass[i];
    }
    
    for(int i=0; i<n; i++){
        for(int j=0; j<26; j++){
            if(pass[i]==lowercase[j]){
                hash[1]=1;
            }
            if(pass[i]==uppercase[j]){
                hash[2]=1;
            }
        }
    }
    
    for(int i=0; i<n; i++){
        for(int j=0; j<10; j++){
            if(pass[i]==numbers[j]){
                hash[0]=1;
            }
        }
    }
    
    for(int i=0; i<n; i++){
        for(int j=0; j<12; j++){
            if(pass[i]==special[j]){
                hash[3]=1;
            }
        }
    }
    
    int kurang=0;
    for(int i=0; i<4; i++){
        if(hash[i]==0){
            kurang++;
        }
    }
    
    int kurangdigit=6-n;
    kurangdigit<kurang ? cout << kurang:cout << kurangdigit;
    
    return 0;
}
