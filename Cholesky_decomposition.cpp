#include <iostream>
#include <vector>
#include <cmath>
using namespace std;


// Check if it is a square matrix

bool is_square(const vector<vector<double>> &A) {

    size_t n = A.size();
    for (const auto &row : A){
        if ( row.size() != n)    // row.size() gives us the number of columns
            return false;
    }
    return true;

};

// Check if the matrix is symmetric

bool is_symmetric(const vector<vector<double>> &A) {
    bool symmetric = true;
    size_t n = A.size();
    for (size_t i=0;i < n; ++i) {
        for (size_t j=0; j < n; ++j){
            if (A[i][j]!=A[j][i])
                symmetric = false;
               return false;
               break;
        if (!symmetric);
            break;

        }
    
    }
    return true;
};

