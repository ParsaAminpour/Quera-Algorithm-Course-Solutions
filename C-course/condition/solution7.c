#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{   
    // s -> 10% | 7 -> 5% | * -> 30%
    char symbol1[10], symbol2[10], symbol3[10];
    scanf("%s%s%s", symbol1, symbol2, symbol3);

    int discount_amount = 0;

    if (strcmp(symbol1, "s") == 0 || strcmp(symbol2, "s") == 0 || strcmp(symbol3, "s") == 0) {
        discount_amount += 10;
    }

    if (strcmp(symbol1, "*") == 0 || strcmp(symbol2, "*") == 0 || strcmp(symbol3, "*") == 0) {
        discount_amount += 30;
    }
    
    if (strcmp(symbol1, "7") == 0 || strcmp(symbol2, "7") == 0 || strcmp(symbol3, "7") == 0) {
        discount_amount += 5;
    }
    
    printf("%d\n", discount_amount);
    return 0;
}
