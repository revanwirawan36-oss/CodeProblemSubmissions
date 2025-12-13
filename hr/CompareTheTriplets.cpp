#include <iostream>
using namespace std;

int main(){
    int a,b,c,d,e,f;
    
    cin >>a>>b>>c>>d>>e>>f;
    
    int alice[3]={a,b,c};
    int bob[3]={d,e,f};
    int baru[2]={0,0};
    
    for(int i=0; i<3; i++){
        if(alice[i]>bob[i]){
            baru[0]+=1;
        } else if(bob[i]>alice[i]){
            baru[1]+=1;
        }
    }
    cout << baru[0] << " " << baru[1];
    return 0;
    
}
