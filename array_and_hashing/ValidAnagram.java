import java.util.HashMap;
import java.util.Map;

public class ValidAnagram {

    public static boolean isAnagramCounter(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> counter = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            counter.merge(s.charAt(i), 1, Integer::sum);
            counter.merge(t.charAt(i), -1, Integer::sum);
        }

        return counter.values().stream().allMatch(v -> v == 0);
    }

    public static boolean isAnagramAscii(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] counter = new int[26];
        for (char c : s.toCharArray()) counter[c - 'a']++;
        for (char c : t.toCharArray()) {
            if (counter[c - 'a'] == 0) return false;
            counter[c - 'a']--;
        }

        return true;
    }
}
