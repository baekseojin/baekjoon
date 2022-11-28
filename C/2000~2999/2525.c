#include <stdio.h>

int main() {
    int h,m,p;
    scanf("%d %d %d", &h, &m, &p);
    m = m + p;
    if(m>=60) {
        h = h + m/60;
        m = m%60; 
        if(h>=24) h = h-24; 
    }
    printf("%d %d", h, m);
    return 0;
}