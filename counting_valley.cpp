//for clear problem understanding refer "https://www.youtube.com/watch?v=aisHQWphVsQ"

#include <iostream>
#include<string.h>

using namespace std;

int main()
{
    int n, step = 0, valley = 0;
    string val;
    //cout<<"N?: ";
    cin>>n;
    //cout<<"val? ";
    cin>>val;
    for(int i = 0; i < n; i++)
    {
        if(val[i] == 'U')
        {
            step += 1;
            if(step == 0)
            {
                valley += 1;
            }
        }
        else if(val[i] == 'D')
        {
            step -= 1;
        }
        
    }
    //cout<<"The number of valley crossed by the hiker is: "<<valley;
    cout<<valley;
    return 0;
}
