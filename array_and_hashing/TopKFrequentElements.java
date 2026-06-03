import java.util.*;

public class TopKFrequentElements {

    public static int[] topKFrequentHeap(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) count.merge(num, 1, Integer::sum);

        // Min-heap of size k, ordered by frequency
        PriorityQueue<Integer> heap = new PriorityQueue<>(Comparator.comparingInt(count::get));
        for (int num : count.keySet()) {
            heap.offer(num);
            if (heap.size() > k) heap.poll();
        }

        int[] result = new int[k];
        for (int i = k - 1; i >= 0; i--) result[i] = heap.poll();
        return result;
    }

    public static int[] topKFrequentBucketSort(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) freq.merge(num, 1, Integer::sum);

        // Create buckets where index = frequency
        @SuppressWarnings("unchecked")
        List<Integer>[] buckets = new List[nums.length + 1];
        for (int i = 0; i <= nums.length; i++) buckets[i] = new ArrayList<>();
        for (Map.Entry<Integer, Integer> e : freq.entrySet()) buckets[e.getValue()].add(e.getKey());

        // Collect top k elements from highest frequency bucket down
        int[] result = new int[k];
        int idx = 0;
        for (int i = buckets.length - 1; i > 0 && idx < k; i--) {
            for (int num : buckets[i]) {
                result[idx++] = num;
                if (idx == k) return result;
            }
        }
        return result;
    }
}
