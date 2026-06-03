import java.util.HashMap;
import java.util.Map;

public class TwoSum {

    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashmap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (hashmap.containsKey(complement)) {
                return new int[]{i, hashmap.get(complement)};
            }
            hashmap.put(nums[i], i);
        }

        return new int[]{};
    }
}
