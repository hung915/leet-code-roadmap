public class ProductArrayExceptSelf {

    public static int[] productExceptSelfLeftRight(int[] nums) {
        int length = nums.length;
        int[] leftProduct = new int[length];
        int[] rightProduct = new int[length];
        int[] result = new int[length];

        leftProduct[0] = 1;
        for (int i = 1; i < length; i++) {
            leftProduct[i] = leftProduct[i - 1] * nums[i - 1];
        }

        rightProduct[length - 1] = 1;
        for (int i = length - 2; i >= 0; i--) {
            rightProduct[i] = rightProduct[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < length; i++) {
            result[i] = leftProduct[i] * rightProduct[i];
        }

        return result;
    }

    public static int[] productExceptSelfO1Space(int[] nums) {
        int length = nums.length;
        int[] result = new int[length];

        result[0] = 1;
        for (int i = 1; i < length; i++) {
            result[i] = result[i - 1] * nums[i - 1];
        }

        int right = 1;
        for (int i = length - 1; i >= 0; i--) {
            result[i] *= right;
            right *= nums[i];
        }

        return result;
    }
}
