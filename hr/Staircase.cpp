#include <iostream>
using namespace std;

int main(){
    int batas;
    cin >> batas;
    
    for(int i=batas-1; i>=0; i--){
        for(int j=0; j<i; j++){
            cout << " ";
        }
        for(int j=batas-1; j>=i; j--){
            cout << "#";
        } cout << endl;
    } 
    return 0;
}
