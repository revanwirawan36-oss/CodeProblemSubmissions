#include <iostream>
using namespace std;

int main(){
    int array[100][100];
    int q;
    cin >> q;
    for(int i=0; i<q; i++){
        for(int j=0; j<3; j++){
            cin >> array[i][j];
        }
    }
    for(int i=0; i<q; i++){
        int com1= array[i][2]-array[i][1];
        int com2= array[i][2]-array[i][0];
        
        com1<0 ? com1*=-1 : com1=com1;
        com2<0 ? com2*=-1 : com2=com2;
        if(com1< com2){
            cout << "Cat B";
        } else if(com1 > com2){
            cout << "Cat A";
        } else {
            cout << "Mouse C";
        }
        cout << endl;
    }
    
    return 0;
}
