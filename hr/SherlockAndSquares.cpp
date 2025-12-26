#include <iostream>
#include <cmath>
using namespace std;
long akar(long a){
    if(a<0) return 0;
    return (long)sqrt(a);
}
int main(){
    long queries;
    cin>>queries;
    
    while(queries--){
        long a,b;
        cin>>a>>b;
        long hasil=akar(b)-akar(a-1);
        
        cout <<hasil<<endl;
    }
    return 0;
}
