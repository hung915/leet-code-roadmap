function containsDuplicateSet(nums: number[]): boolean {
    const seen = new Set<number>();
    for (const num of nums) {
        if (seen.has(num)) return true;
        seen.add(num);
    }
    return false;
}

function containsDuplicateSort(nums: number[]): boolean {
    const sorted = [...nums].sort((a, b) => a - b);
    return sorted.some((val, i) => i > 0 && val === sorted[i - 1]);
}
