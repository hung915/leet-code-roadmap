public class ContainerWithMostWater {

    public static int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int maxWater = 0;

        while (left < right) {
            int width = right - left;
            int currentHeight = Math.min(height[left], height[right]);
            maxWater = Math.max(maxWater, width * currentHeight);

            if (height[left] < height[right])
                left++;
            else
                right--;
        }

        return maxWater;
    }
}
