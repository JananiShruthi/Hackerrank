#include<stdio.h>

int main()
{
    int t;
    scanf("%d", &t);
    for(int T = 0; T < t; T++)
    {
        int n;
        scanf("%d", &n);
        int arr[n], result = 0;
        for(int i = 0; i < n; i++)
        {
            scanf("%d", &arr[i]);
        }
        if((n % 2) != 0)
        {
            for(int i = 0; i < n; i++)
            {
                if(i%2 == 0)
                {
                    result ^= arr[i];
                }
            }
        } 
        printf("%d", result);  
    }
}
