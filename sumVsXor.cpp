#include <iostream>

using namespace std;

int main()
{
    long n, cnt = 0;
    cin>>n;
    for(int i = 0; i <= n; i++)
    {
        if((n + i) == (n ^ i))
        {
            cnt += 1;
        }
    }
    cout<<cnt;
    
}
