#include <stdio.h>
#include <math.h>

void towerOfHanoi(int n, char from_rod, char to_rod, char aux_rod)
{
    if (n == 1)
    {
        printf("1 %c %c\n", from_rod, to_rod);
        return;
    }
    towerOfHanoi(n-1, from_rod, aux_rod, to_rod);
    printf("%d %c %c\n", n, from_rod, to_rod);
    towerOfHanoi(n-1, aux_rod, to_rod, from_rod);
}
 
int main()
{
    int n;
    scanf("%d", &n);
    towerOfHanoi((pow(2,n) - 1), 'A', 'C', 'B');
    return 0;
}