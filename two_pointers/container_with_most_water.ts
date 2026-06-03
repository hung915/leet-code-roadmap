function maxArea(height: number[]): number {
    let left = 0, right = height.length - 1;
    let maxWater = 0;

    while (left < right) {
        const width = right - left;
        const currentHeight = Math.min(height[left], height[right]);
        maxWater = Math.max(maxWater, width * currentHeight);

        if (height[left] < height[right]) left++;
        else right--;
    }

    return maxWater;
}
