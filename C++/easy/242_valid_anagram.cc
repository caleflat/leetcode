#include <iostream>

using namespace std;

class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        int m[26] = {0};

        for (char c : s)
            m[c - 'a']++;

        for (char c : t)
            m[c - 'a']--;

        for (int i : m)
            if (i != 0)
                return false;

        return true;
    }
};