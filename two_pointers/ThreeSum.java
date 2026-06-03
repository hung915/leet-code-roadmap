import java.util.*;

public class ThreeSum {

    public static List<List<Integer>> threeSumTwoPointers(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int left = i + 1, right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum > 0) right--;
                else if (sum < 0) left++;
                else {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;
                    while (left < right && nums[left] == nums[left - 1]) left++;
                }
            }
        }

        return res;
    }

    public static List<List<Integer>> threeSumHashset(int[] nums) {
        Set<List<Integer>> res = new HashSet<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            Set<Integer> seen = new HashSet<>();
            for (int j = i + 1; j < nums.length; j++) {
                int complement = -nums[i] - nums[j];
                if (seen.contains(complement)) {
                    int[] triplet = {nums[i], complement, nums[j]};
                    Arrays.sort(triplet);
                    res.add(Arrays.asList(triplet[0], triplet[1], triplet[2]));
                }
                seen.add(nums[j]);
            }
        }

        return new ArrayList<>(res);
    }
}
