import java.util.*;

public class GroupAnagrams {

    public static List<List<String>> groupAnagramsSort(String[] strs) {
        Map<String, List<String>> ans = new HashMap<>();

        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            ans.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
        }

        return new ArrayList<>(ans.values());
    }

    public static List<List<String>> groupAnagramsAscii(String[] strs) {
        Map<String, List<String>> ans = new HashMap<>();

        for (String str : strs) {
            int[] counter = new int[26];
            for (char c : str.toCharArray()) counter[c - 'a']++;
            String key = Arrays.toString(counter);
            ans.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
        }

        return new ArrayList<>(ans.values());
    }
}
