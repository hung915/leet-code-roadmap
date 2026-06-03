function majorityElementHashmap(nums: number[]): number {
    const counter = new Map<number, number>();
    for (const num of nums) counter.set(num, (counter.get(num) ?? 0) + 1);

    let maxCount = 0, result = 0;
    for (const [num, count] of counter) {
        if (count > maxCount) { maxCount = count; result = num; }
    }
    return result;
}

function majorityElementBoyerMoore(nums: number[]): number {
    let candidate = 0, count = 0;

    for (const num of nums) {
        if (count === 0) candidate = num;
        count += candidate === num ? 1 : -1;
    }

    return candidate;
}

function majorityElementSort(nums: number[]): number {
    const sorted = [...nums].sort((a, b) => a - b);
    return sorted[Math.floor(sorted.length / 2)];
}

function majorityElementBitManipulation(nums: number[]): number {
    const n = nums.length;
    let majority = 0;

    for (let i = 0; i < 32; i++) {
        const bit = 1 << i;
        const bitCount = nums.filter(num => num & bit).length;
        if (bitCount > n / 2) majority |= bit;
    }

    // Handle negative numbers — convert from unsigned 32-bit to signed
    return majority >= (1 << 31) ? majority - (1 << 32) : majority;
}
