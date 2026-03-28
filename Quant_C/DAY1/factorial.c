#include <stdio.h>

int main(){

    int num,factorial;
     

    printf("ENTER A NUMBER:\n");
    scanf("%d",&num);

    factorial = 1;

    for (int n=num; n>0; n--){
        factorial = factorial*n;
    }

    printf("THE FACTORIAL OF %d is = %d\n", num,factorial);

    return 0;
}