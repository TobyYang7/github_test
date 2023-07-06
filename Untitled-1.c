#include <stdio.h>
int main()
{
    int x[5];
    x[0] = 254;
    x[1] = 649;
    x[2] = 971;
    x[3] = 1678;
    unsigned char *y = (unsigned char *)x;
    printf("%s",(unsigned char *)x);
    printf("%d\n", *y);
    return 0;
}