#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
	int r11, r12, r21, r22, r31, r32;
	scanf("%d%d", &r11, &r12);
	scanf("%d%d", &r21, &r22);
	scanf("%d%d", &r31, &r32);

	int _x, _y;
	int x[3] = {r11, r21, r31};
	int y[3] = {r12, r22, r32};

	int max_x, max_y;
	max_x = x[0] ? x[0] >= x[1] : x[1] ? x[1] >= x[2] : x[2];
	_x = (x[0] + x[1] + x[2]) - (2 * max_x);

	max_y = y[0] ? y[0] >= y[1] : y[1] ? y[1] >= y[2] : y[2];
	_y = (y[0] + y[1] + y[2]) - (2 * max_y);

	if(x[0] == x[1])
		_x = x[2];
	else if(x[0] == x[2])
		_x = x[1];
	else
		_x = x[0];

	if (y[0] == y[1])
		_y = y[2];
	else if (y[0] == y[2])
		_y = y[1];
	else
		_y = y[0];

	printf("%d %d\n", _x, _y);
	return 0;
}	