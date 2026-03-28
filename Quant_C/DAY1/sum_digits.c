#include <stdio.h>

int main(){

    int num,sum;
    int x,original;

    printf("ENTER AN INTEGER:\n");
    scanf("%d",&num);
    original = num;
    sum = 0;
    
    if (num < 0){
    num = -original;}
        
        while(num>0){
            x = num%10;
            sum += x;
            num = num/10;

    }


    printf("THE SUM OF %d is %d", original,sum);

return 0;
    
}