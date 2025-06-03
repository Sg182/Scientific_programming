#include <iostream>
#include <cstdlib>
using namespace std;

int main(){
    int cols,rows;
    
    cout << "Enter the number of rows and columns respectively: "<<endl;
    cin >>  rows >> cols;
    cout << "You entered rows: "<<rows<<" columns: "<< cols <<endl;

    // now initialize a 'matrix' to allocate memory (pointer to pointer)
    int** matrix = (int**)malloc(rows*sizeof(int*));

    for (int i=0; i<rows; ++i){
        matrix[i]= (int*)malloc(cols*sizeof(int)); // now initiate memory (pointers to integers) for each rows
    }

    for (int i=0; i<rows; ++i){
        for (int j =0; j<cols;++j){
            cout << "Enter the elements of row "<<i+1<<endl;
            cin >> matrix[i][j];}
    }

    // print the original matrix
    cout <<"The original matrix"<<endl;
    for (int i=0; i<rows; ++i){
        for (int j =0; j<cols;++j){
         
        cout << matrix[i][j]<< " ";}
        cout <<endl;
    }
    cout <<"---------------------"<<endl;
    cout <<"The transposed matrix is "<<endl;

    for (int j=0; j<cols; ++j){
        for (int i =0; i<rows;++i){
         
        cout << matrix[i][j]<< " ";}
        cout <<endl;
    }

    // intialize the result = matrix1*matrix2

    int** result = (int**)malloc(rows*sizeof(int*));

    for (int i=0; i<rows; ++i){
        result[i]= (int*)malloc(rows*sizeof(int)); // now initiate memory !!!!note: malloc(rows*sizeof(int))
    }

    for (int i=0; i<rows; ++i){
        for (int j =0; j<rows;++j){
            result[i][j]=0;
            for(int k =0; k<cols;++k){
                result[i][j] += matrix[i][k]*matrix[j][k];   // (MM^T)ij = \sum_k M_ik*(M_kj)^T

            }
             
    }}

    cout <<"---------------------"<<endl;
    cout <<"The M*M^T matrix is = "<<endl;

    for (int i=0; i<rows; ++i){
        for (int j =0; j<rows;++j){
         
        cout << result[i][j]<< " ";}
        cout <<endl;
    }


    // free the memory

    for (int i=0; i<rows; ++i){
        free(matrix[i]);
    }
    free(matrix);

    for (int i=0; i<rows; ++i){
        free(result[i]);
    }
    free(result);

    }