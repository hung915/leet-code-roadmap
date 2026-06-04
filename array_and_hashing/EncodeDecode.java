import java.util.ArrayList;
import java.util.List;

public class EncodeDecode {

    // Approach 1 — Length Prefix (Most Optimal)
    public static String encode(List<String> strs) {
        StringBuilder result = new StringBuilder();
        for (String s : strs) {
            result.append(s.length()).append('#').append(s);
        }
        return result.toString();
    }

    public static List<String> decode(String s) {
        List<String> result = new ArrayList<>();
        int i = 0;

        while (i < s.length()) {
            int j = i;
            while (s.charAt(j) != '#')
                j++;

            int length = Integer.parseInt(s.substring(i, j));
            result.add(s.substring(j + 1, j + 1 + length));
            i = j + 1 + length;
        }

        return result;
    }
}
