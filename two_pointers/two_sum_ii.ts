function twoSumII(nums: number[], target: number): number[] {
    let left = 0, right = nums.length - 1;

    while (left < right) {
        const sum = nums[left] + nums[right];
        if (sum < target) left++;
        else if (sum > target) right--;
        else return [left + 1, right + 1];
    }

    return [];
}
