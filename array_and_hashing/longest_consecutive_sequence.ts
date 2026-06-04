function longestConsecutiveSequence(nums: number[]): number {
  const hashSet = new Set(nums);
  let longestStreak = 0;

  for (const num of hashSet) {
    if (!hashSet.has(num - 1)) {
      let currentNum = num;
      let currentStreak = 1;

      while (hashSet.has(currentNum + 1)) {
        currentNum++;
        currentStreak++;
      }

      longestStreak = Math.max(longestStreak, currentStreak);
    }
  }

  return longestStreak;
}
