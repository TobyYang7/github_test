#include <stdio.h>
int main()
{
    int *p, x; x = 3; p = &x;
    printf("p points to %d\n", *p);

    return 0;
}