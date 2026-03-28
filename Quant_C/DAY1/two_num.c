#include <stdio.h>
#include <math.h>

int main(){

    int x,y;
     
     
    printf("ENTER TWO INTEGERS:\n");
    scanf("%d %d", &x,&y);

    double xf = (double)(x);
    double yf = (double)(y);

    printf("THE SUM OF %d + %d =%d\n",x,y,x+y);
    printf("THE DIFFERENCE OF %d - %d =%d\n",x,y,x - y);
    printf("THE PRODUCT %d * %d = %d\n",x,y,x*y);

    if (y){
    printf("THE QUOTIENT %.3f / %.3f =%.3f\n",xf,yf,xf/yf);
    }
    else{
        printf("DIVISION BY 0 IS NOT ALLOWED");
    }

    return 0;



}