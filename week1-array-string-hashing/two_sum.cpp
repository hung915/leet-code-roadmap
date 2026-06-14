#include <iostream>
#include <unordered_map>
#include <vector>
using std::cout;
using std::unordered_map;
using std::vector;

vector<int> two_sum(vector<int>& nums, int target) {
    unordered_map<int, int> seen{};
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (seen.contains(complement)) {
            return vector<int>{seen[complement], i};
        }
        seen[nums[i]] = i;
    }
    return vector<int>{};
}

int main() {
    vector<int> nums1 = {2, 7, 11, 15};
    auto r1 = two_sum(nums1, 9);
    cout << "[" << r1[0] << ", " << r1[1] << "]\n";  // [0, 1]

    vector<int> nums2 = {3, 2, 4};
    auto r2 = two_sum(nums2, 6);
    cout << "[" << r2[0] << ", " << r2[1] << "]\n";  // [1, 2]

    vector<int> nums3 = {3, 3};
    auto r3 = two_sum(nums3, 6);
    cout << "[" << r3[0] << ", " << r3[1] << "]\n";  // [0, 1]
}