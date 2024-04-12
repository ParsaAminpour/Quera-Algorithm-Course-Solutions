#include <stdio.h>

int main() {
    int no_row, c = 1, blk, i, j;

    scanf("%d", &no_row);

    for (i = 0; i < no_row; i++) {

        for (j = 0; j <= i; j++) {
            if (j == 0 || i == 0)
                c = 1;
            else
                c = c * (i - j + 1) / j;
            printf("%d ", c);
        }

        printf("\n");
    }

    return 0;
}