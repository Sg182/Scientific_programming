#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define N 20
 

int main(){

    int *arr;
    int final_sum = 0;
    int *partial_sum;

    int num_threads;

    arr = (int *)malloc(N*sizeof(int));
    
    if (arr == NULL) {
        printf("Memory allocation failed for arr\n");
        return 1;
    }
    
    for(int i=0; i<N;i++){
        arr[i] = i+1;
    }

    #pragma omp parallel
        {
            #pragma omp master
            {
                num_threads = omp_get_num_threads(); //PRINTS TOTAL NUM OF THREADS IN THE PARALLEL REGION

            }
        }
    printf("THE TOTAL NUMBER OF THREADS PROGRAM USING %d\n", num_threads);
    
    partial_sum = (int *)malloc(num_threads*sizeof(int));
    if (partial_sum == NULL) {
        printf("Memory allocation failed for partial_sum\n");
        free(arr);
        return 1;
    }

    #pragma omp parallel
    {
        int id = omp_get_thread_num();  //GET THE THREAD ID
        int start = id * N / num_threads;
        int end   = (id + 1) * N / num_threads;

        int local_sum = 0;
        for (int i = start; i<end;i++){
            local_sum+= arr[i];
        }
        partial_sum[id] =local_sum;
        printf("LOCAL SUM FROM THREAD %d is %d\n", id, local_sum);

        #pragma omp barrier

            #pragma omp single      //ONLY ONE THREAD RUNS THE SCOPE
            {
                int tid = omp_get_thread_num();
                for (int i=0;i<num_threads;i++){
                    final_sum += partial_sum[i];
                     
                }
                printf("Final sum = %d\n", final_sum);
                printf("Printed by THREAD %d\n",tid ); //SHOULD SEE ONLY ONE THREAD NUMBER
            }
        }
        free(partial_sum);
        free(arr);
        return 0;
    

    }



