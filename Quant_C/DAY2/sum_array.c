#include <stdio.h>
#include <stdlib.h>

int cal_sum(int n,int *x);
int *init_array(int n);
void print_arr(int *x, int n);
int *reverse_arr(int *x, int n);

int main(){

    int n, sum;
    int *arr = NULL;

    printf("Enter the size of the array\n");
    scanf("%d",&n);

    arr = init_array(n);  //RETURNS THE ADDRESS OF THE FIRST ELEMENT OF THE ARRAY
    print_arr(arr,n);

    sum = cal_sum(n,arr);
    printf("The sum of the %d elements of the array = %d\n",n, sum);
    arr = reverse_arr(arr, n);
    printf("Array after reverse\n");
    print_arr(arr,n);

    free(arr);

    return 0;
}



int *init_array(int n){             //THIS FUNCTION RETURNS A POINTER TO INTEGER (FOR INITIALIZING 1D ARRAy)

    int *arr = malloc(n*sizeof(int));
    if (arr == NULL){
        printf("Memory allocation failed!");
        return NULL;
        
    }

    printf("Enter your %d elements \n",n);

    for (int i=0; i<n;++i){
        scanf("%d",&arr[i]);
    }
    return arr;

}

int cal_sum(int n, int *x){

    int sum=0;

    for (int k=0; k<n; k++){
        sum += x[k];
    }
    return sum;
}

void print_arr(int *x,int n){
    
    printf("The corresponding array is = [");
     
    for (int j = 0; j<n; ++j){
        printf("%d",x[j]);
        if (j != n-1) printf(",");
    }
    printf("]\n");
}

int *reverse_arr(int *x, int n){
    int i, temp;

        for (i=0;i<n/2;++i){            //FOR N = ODD, WE DONT CHANGE THE MIDDLE ELEMENT
            temp = x[i];
            x[i] = x[n-i-1];
            x[n-i-1] = temp; 
        }
    return x;


}