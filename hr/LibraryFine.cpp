#include <iostream>
using namespace std;
int bayar(int d1, int m1, int y1, int d2, int m2, int y2){
    bool bulanTahunSama=(m1==m2)&&(y1==y2);
    bool tahunSama=(y1==y2);
    bool tahunBeda=(y1!=y2);
    bool tepat=(tahunBeda&&y1<y2)||(tahunSama&&m1<m2)||(bulanTahunSama&&d1<d2);
    int denda=0;
    if(!tepat){
        if(bulanTahunSama) denda=(d1-d2)*15;
        else if(tahunSama) denda=(m1-m2)*500;
        else if(tahunBeda) denda=10000;
    }
    return denda;
}
int main(){
    int d1,m1,y1,d2,m2,y2;
    cin>>d1>>m1>>y1>>d2>>m2>>y2;
    int denda=bayar(d1,m1,y1,d2,m2,y2);
    cout <<denda;
    return 0;
}
