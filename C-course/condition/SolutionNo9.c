#include <stdio.h>
#include <math.h>

int reverse_number(int _num) {
    int tmp = 0;
    for (int i = 0; i < 3; i++) {
        tmp += (_num % 10) * pow(10, 2-i);
        _num = _num / 10;
    }
    printf("%d\n", tmp);
    return tmp;
}

int main() {
    int num1, num2;
    scanf("%d%d", &num1, &num2);
    
    int reversed1 = reverse_number(num1);
    int reversed2 = reverse_number(num2);

    printf("reversed1 is %d\nreversed2 is %d\n\n", reversed1, reversed2);

    if (reversed1 < reversed2) 
        printf("%d < %d\n", num1, num2);
    else if(reversed2 < reversed1)
        printf("%d < %d\n", num2, num1);
    else
        printf("%d = %d", num1, num2);
}