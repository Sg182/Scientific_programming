#include <stdio.h>

int main(){

    int n;
    int sidx; //START INDEX
    int curr_sum;
    int max_sum;

    int arr [] =  {1,4,2,3};

    n = sizeof(arr)/sizeof(arr[0]);
    printf("The size of the array is %d\n", n);

    curr_sum = arr[0];
    max_sum = arr[0];  //Tracks the max sum

    sidx = 0;
    int temp_sidx = 0;
    int end =0;

    for (int i = 1; i < n; i++){
        if (curr_sum + arr[i] > arr[i]){
            curr_sum += arr[i];
        }
        else{
            curr_sum = arr[i];
            temp_sidx=i;
        }

        if (curr_sum > max_sum){
            max_sum = curr_sum;
            sidx = temp_sidx;
            end = i;
        }
         


    }
    printf("The maximum sum of the contiguous array = %d\n", max_sum);
    printf("sidx is %d and end is %d\n ", sidx,end);
    //Printing the final contiguos array
    printf("The corresponding contiguous array is = [");
    for (int j = sidx; j<=end; ++j){
        printf("%d",arr[j]);
        if (j != end) printf(",");
    }
    printf("]\n");
    


    return 0;

}