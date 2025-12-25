#include <iostream>
#include <algorithm>
using namespace std;

long taumBday(long* isi){
    long mins=min(isi[2],isi[3]);
    long indeksColorMaks;
    isi[2]==mins ? indeksColorMaks=1:indeksColorMaks=0;
    long total=isi[0]+isi[1];
    long kalogabisa=(isi[0]*isi[2])+(isi[1]*isi[3]);
    
    if(isi[2]==isi[3]||(mins*total)+(isi[indeksColorMaks]*isi[4])>kalogabisa){
        return kalogabisa;
    }
     
    return (mins*total)+(isi[indeksColorMaks]*isi[4]);
}
int main(){
    long isi[5];
    long t;
    cin>>t;
    
    while(t--){
    for(int i=0; i<5; i++){
        cin>>isi[i];
    }
    cout<<taumBday(isi)<<endl;
    }
    
    return 0;
}
