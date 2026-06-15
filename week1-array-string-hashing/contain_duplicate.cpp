#include "unordered_set"
#include "vector"
using std::unordered_set;
using std::vector;

bool contain_duplicate(vector<int>& nums) {
    unordered_set<int> seen;
    for (int n : nums) {
        if (!seen.insert(n).second) return true;
    }
    return false;
}
