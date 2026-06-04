import java.util.HashSet;
import java.util.Set;

public class LongestConsecutiveSequence {

    public static int longestConsecutiveSequence(int[] nums) {
        Set<Integer> hashSet = new HashSet<>();
        for (int num : nums)
            hashSet.add(num);

        int longestStreak = 0;

        for (int num : hashSet) {
            if (!hashSet.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;

                while (hashSet.contains(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;
                }

                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }
}
