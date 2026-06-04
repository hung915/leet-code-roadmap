import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class MajorityElement {

    public static int majorityElementHashmap(int[] nums) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums)
            counter.merge(num, 1, Integer::sum);

        return counter.entrySet().stream()
                .max(Map.Entry.comparingByValue())
                .get().getKey();
    }

    public static int majorityElementBoyerMoore(int[] nums) {
        int candidate = 0, count = 0;

        for (int num : nums) {
            if (count == 0)
                candidate = num;
            count += (candidate == num) ? 1 : -1;
        }

        return candidate;
    }

    public static int majorityElementSort(int[] nums) {
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        return sorted[sorted.length / 2];
    }

    public static int majorityElementBitManipulation(int[] nums) {
        int n = nums.length;
        int majority = 0;

        for (int i = 0; i < 32; i++) {
            int bit = 1 << i;
            int bitCount = 0;
            for (int num : nums) {
                if ((num & bit) != 0)
                    bitCount++;
            }
            if (bitCount > n / 2)
                majority |= bit;
        }

        return majority;
    }
}
