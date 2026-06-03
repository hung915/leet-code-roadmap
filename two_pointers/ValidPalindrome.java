public class ValidPalindrome {

    public static boolean isPalindromeReverse(String s) {
        StringBuilder filtered = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) filtered.append(Character.toLowerCase(c));
        }
        String str = filtered.toString();
        return str.equals(new StringBuilder(str).reverse().toString());
    }

    public static boolean isPalindromeTwoPointers(String s) {
        int left = 0, right = s.length() - 1;

        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) left++;
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) right--;

            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) return false;
            left++;
            right--;
        }

        return true;
    }
}
