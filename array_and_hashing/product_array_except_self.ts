function productExceptSelfLeftRight(nums: number[]): number[] {
  const length = nums.length;
  const leftProduct = new Array(length).fill(1);
  const rightProduct = new Array(length).fill(1);
  const result: number[] = [];

  for (let i = 1; i < length; i++) {
    leftProduct[i] = leftProduct[i - 1] * nums[i - 1];
  }

  for (let i = length - 2; i >= 0; i--) {
    rightProduct[i] = rightProduct[i + 1] * nums[i + 1];
  }

  for (let i = 0; i < length; i++) {
    result.push(leftProduct[i] * rightProduct[i]);
  }

  return result;
}

function productExceptSelfO1Space(nums: number[]): number[] {
  const length = nums.length;
  const result = new Array(length).fill(1);

  for (let i = 1; i < length; i++) {
    result[i] = result[i - 1] * nums[i - 1];
  }

  let right = 1;
  for (let i = length - 1; i >= 0; i--) {
    result[i] *= right;
    right *= nums[i];
  }

  return result;
}
