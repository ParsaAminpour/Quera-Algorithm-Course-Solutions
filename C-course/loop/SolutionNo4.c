#include <stdio.h>
#include <math.h>

int main()
{
	int result = 0;
	int flag = false;

	while(!flag) {
		int num;
		scanf("%d", &num);
		num == 0 ? flag = true : result += num;
	}
}
