function twoSum(nums: number[], target: number): number[] {
    const hashmap = new Map<number, number>();

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (hashmap.has(complement)) {
            return [i, hashmap.get(complement)!];
        }
        hashmap.set(nums[i], i);
    }

    return [];
}
