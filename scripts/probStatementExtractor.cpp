#include <bits/stdc++.h>
using namespace std;

/*bool check(string cur)
{
    string tocheck = "src=";
    for (int i=0;i<4;i++){
        if (cur[i] != tocheck[i])
            return false;
    }
    return true;
}

string modify(string cur)
{
    string ret="src=http://lightoj.com/";
    for (int i=5;i<cur.size();i++)
        ret+=cur[i];
    return ret;
}*/

int main()
{
    freopen("temphtml.html","r",stdin);
    freopen("probstatement.txt","w",stdout);
    string s;
    int f=0;
    while(getline(cin,s))
    {
        istringstream is(s);
        string cur;
        while(is>>cur)
        {
            if (cur == "class=Section1>")
                f=1;
        }
        if (f==1){
            while(getline(cin,s))
            {
                istringstream is(s);
                string cur;
                while(is>>cur)
                {
                    if (cur == "<h1>Input</h1>")
                        return 0;
                    //else if (check(cur))
                    //	cur = modify(cur);
                    cout<<cur<<" ";
                }
                cout<<endl;
            }
        }
    }
    return 0;
}
