function threeSumTwoPointers(nums: number[]): number[][] {
    const res: number[][] = [];
    nums.sort((a, b) => a - b);

    for (let i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let left = i + 1, right = nums.length - 1;
        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];
            if (sum > 0) right--;
            else if (sum < 0) left++;
            else {
                res.push([nums[i], nums[left], nums[right]]);
                left++;
                right--;
                while (left < right && nums[left] === nums[left - 1]) left++;
            }
        }
    }

    return res;
}

function threeSumHashset(nums: number[]): number[][] {
    const res = new Set<string>();
    nums.sort((a, b) => a - b);

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > 0) break;
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        const seen = new Set<number>();
        for (let j = i + 1; j < nums.length; j++) {
            const complement = -nums[i] - nums[j];
            if (seen.has(complement)) {
                res.add(JSON.stringify([nums[i], complement, nums[j]]));
            }
            seen.add(nums[j]);
        }
    }

    return [...res].map(s => JSON.parse(s));
}
