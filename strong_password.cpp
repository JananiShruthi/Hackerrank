#include<iostream>
#include<string.h>
using namespace std;

int lf = 0, digit = 0, lowf = 0, upf = 0, spf = 0; //indicating that no condition is satisfied

int length_pass(string pass)
{
    if(pass.length() >= 6)
    {
        lf = 1;
    }
    return lf;
}

int isDigit(string pass)
{
    int n = pass.length();
    for(int i = 0; i < n; i++)
    {
        if(isdigit(pass[i]))
        {
            digit = 1;
            break;
        }
    }
    return digit;
}

int lowercase(string pass)
{
    int n = pass.length();
    for(int i = 0; i < n; i++)
    {
        if(islower(pass[i]))
        {
            lowf = 1;
            break;
        }
    }
    return lowf;
}

int uppercase(string pass)
{
    int n = pass.length();
    for(int i = 0; i < n; i++)
    {
        if(isupper(pass[i]))
        {
            upf = 1;
            break;
        }
    }
    return upf;
}

int special_char(string pass)
{
    int n = pass.length();
    for(int i = 0; i < n; i++)
    {
        if((pass[i] == '!') || (pass[i] == '@') || (pass[i] == '#') || (pass[i] == '$') || (pass[i] == '%') || (pass[i] == '^') || (pass[i] == '&') || (pass[i] == '*') || (pass[i] == '(') ||  (pass[i] == ')') || (pass[i] == '-') || (pass[i] == '+'))
        {
            spf = 1;
            break;
        }
    }
    return spf;
}

int main()
{
    string pass;
    int cnt = 5, s, u, l, d, len;
    cin>>len;
    cin>>pass;
    int n = pass.length();
    if(!length_pass(pass))
    {
        cnt = 0;
        if(!special_char(pass))
        {
            n += 1;
            cnt++;
        }
        if(!uppercase(pass))
        {
            n += 1;
            cnt++;
        }
        if(!lowercase(pass))
        {
            n += 1;
            cnt++;
        }
        if(!isDigit(pass))
        {
            n += 1;
            cnt++;
        }
        if(n < 6)
        {
            cnt += (6 - n);
        }
    }
    else
    {
        cnt -= special_char(pass);
        cnt -= length_pass(pass);
        cnt -= uppercase(pass);
        cnt -= lowercase(pass);
        cnt -= isDigit(pass);
    }
    cout<<cnt<<"\n";
    
}
