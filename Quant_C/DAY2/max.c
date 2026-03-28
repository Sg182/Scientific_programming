#include <stdio.h>

int max(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

void pr(){
    printf("Hello Guys\n");
}

int main() {
    int x, y, z;
    printf("Enter three numbers:\n");
    scanf("%d %d %d", &x, &y,&z);

    int result = max(z,max(x, y));
    pr();
    printf("The max is %d\n", result);

    return 0;
}