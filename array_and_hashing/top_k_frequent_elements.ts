function topKFrequentSort(nums: number[], k: number): number[] {
  const count = new Map<number, number>();
  for (const num of nums) count.set(num, (count.get(num) ?? 0) + 1);

  return [...count.keys()]
    .sort((a, b) => count.get(b)! - count.get(a)!)
    .slice(0, k);
}

function topKFrequentBucketSort(nums: number[], k: number): number[] {
  const freq = new Map<number, number>();
  for (const num of nums) freq.set(num, (freq.get(num) ?? 0) + 1);

  // Create buckets where index = frequency
  const buckets: number[][] = Array.from({ length: nums.length + 1 }, () => []);
  for (const [num, count] of freq) buckets[count].push(num);

  // Collect top k elements from highest frequency bucket down
  const result: number[] = [];
  for (let i = buckets.length - 1; i > 0 && result.length < k; i--) {
    for (const num of buckets[i]) {
      result.push(num);
      if (result.length === k) return result;
    }
  }
  return result;
}

function topKFrequentQuickSelect(nums: number[], k: number): number[] {
  const count = new Map<number, number>();
  for (const num of nums) count.set(num, (count.get(num) ?? 0) + 1);

  const unique = [...count.keys()];
  const n = unique.length;

  if (k >= n) return unique;

  function partition(left: number, right: number, pivotIndex: number): number {
    const pivotFreq = count.get(unique[pivotIndex])!;
    [unique[pivotIndex], unique[right]] = [unique[right], unique[pivotIndex]];

    let storeIndex = left;
    for (let i = left; i < right; i++) {
      if (count.get(unique[i])! < pivotFreq) {
        [unique[i], unique[storeIndex]] = [unique[storeIndex], unique[i]];
        storeIndex++;
      }
    }
    [unique[right], unique[storeIndex]] = [unique[storeIndex], unique[right]];
    return storeIndex;
  }

  function quickSelect(left: number, right: number, kSmallest: number): void {
    if (left >= right) return;
    const pivotIndex = left + Math.floor(Math.random() * (right - left + 1));
    const finalIndex = partition(left, right, pivotIndex);

    if (finalIndex === kSmallest) return;
    else if (finalIndex > kSmallest)
      quickSelect(left, finalIndex - 1, kSmallest);
    else quickSelect(finalIndex + 1, right, kSmallest);
  }

  quickSelect(0, n - 1, n - k);
  return unique.slice(n - k);
}
