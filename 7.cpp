#include <fstream>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

ifstream f("input.txt");

char line[256];

struct hand{
    int card[6];
    int bet, power;
}v[1001];

int frecv[15];

int sort_order(hand a, hand b)
{
    int j;
    if(a.power != b.power)
    {
        return a.power < b.power;
    }
    for(j = 1; j <= 5; j++)
    {
        if(a.card[j] != b.card[j])
        {
            return a.card[j] < b.card[j];
        }
    }
}

int part1()
{
    int i = 0, j, ans1 = 0;
    while(f.getline(line,256))
    {
        i++;
        for(j = 1; j <= 14; j++)
        {
            frecv[j] = 0;
        }
        for(j = 0; j <= 4; j++)
        {
            if(line[j] >= '0' && line[j] <= '9')
            {
                v[i].card[j+1] = line[j] - '0';
            }
            else
            {
                if(line[j] == 'T') v[i].card[j+1] = 10;
                if(line[j] == 'J') v[i].card[j+1] = 11;
                if(line[j] == 'Q') v[i].card[j+1] = 12;
                if(line[j] == 'K') v[i].card[j+1] = 13;
                if(line[j] == 'A') v[i].card[j+1] = 14;
            }
            frecv[v[i].card[j+1]]++;
        }
        v[i].bet = 0;
        for(j = 6; j <strlen(line); j++)
        {
            v[i].bet = v[i].bet * 10 + (line[j] - '0');
        }
        int max1, max2;
        max1 = max2 = 0;
        for(j = 1; j <= 14; j++)
        {
            if(frecv[j] > max2 && frecv[j] <= max1){max2 = frecv[j];}
            if(frecv[j] > max1){max2 = max1; max1 = frecv[j];}
        }
        if(max1 == 5){v[i].power = 7;}
        if(max1 == 4){v[i].power = 6;}
        if(max1 == 3)
        {
            if(max2 == 2){v[i].power = 5;}
            else{v[i].power = 4;}
        }
        if(max1 == 2)
        {
            if(max2 == 2){v[i].power = 3;}
            else{v[i].power = 2;}
        }
        if(max1 == 1){v[i].power = 1;}

    }
    sort(v+1, v+i+1, sort_order);
    int k;
    for(k = 1; k <= i; k++)
    {
        ans1 += v[k].bet*k;
    }
    cout<<ans1;
    return 0;
}

int part2()
{
    int i = 0, j;
    long long int ans2 = 0;
    while(f.getline(line,256))
    {
        i++;
        for(j = 0; j <= 14; j++)
        {
            frecv[j] = 0;
        }
        for(j = 0; j <= 4; j++)
        {
            if(line[j] >= '0' && line[j] <= '9')
            {
                v[i].card[j+1] = line[j] - '0';
            }
            else
            {
                if(line[j] == 'T') v[i].card[j+1] = 10;
                if(line[j] == 'J') v[i].card[j+1] = 0;
                if(line[j] == 'Q') v[i].card[j+1] = 12;
                if(line[j] == 'K') v[i].card[j+1] = 13;
                if(line[j] == 'A') v[i].card[j+1] = 14;
            }
            frecv[v[i].card[j+1]]++;
        }
        v[i].bet = 0;
        for(j = 6; j <strlen(line); j++)
        {
            v[i].bet = v[i].bet * 10 + (line[j] - '0');
        }
        int max1, max2;
        max1 = max2 = 0;
        for(j = 1; j <= 14; j++)
        {
            if(frecv[j] > max2 && frecv[j] <= max1){max2 = frecv[j];}
            if(frecv[j] > max1){max2 = max1; max1 = frecv[j];}
        }
        max1 = max1 + frecv[0];
        if(max1 == 5){v[i].power = 7;}
        if(max1 == 4){v[i].power = 6;}
        if(max1 == 3)
        {
            if(max2 == 2){v[i].power = 5;}
            else{v[i].power = 4;}
        }
        if(max1 == 2)
        {
            if(max2 == 2){v[i].power = 3;}
            else{v[i].power = 2;}
        }
        if(max1 == 1){v[i].power = 1;}

    }
    sort(v+1, v+i+1, sort_order);
    int k;
    for(k = 1; k <= i; k++)
    {
      ans2 += v[k].bet*k;;
    }
    cout<<ans2;
    return 0;
}

int main()
{
    part2();
}
