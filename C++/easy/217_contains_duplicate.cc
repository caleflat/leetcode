#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution
{
public:
    bool containsDuplicate(vector<int> &nums)
    {
        unordered_map<int, int> m;
        for (size_t i : nums)
        {
            m[i]++;
            if (m[i] == 2)
                return true;
        }

        return false;
    }
};
