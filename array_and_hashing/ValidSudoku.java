import java.util.HashSet;
import java.util.Set;

public class ValidSudoku {

    public static boolean isValidSudokuSet(char[][] board) {
        @SuppressWarnings("unchecked")
        Set<Character>[] rows = new HashSet[9];
        @SuppressWarnings("unchecked")
        Set<Character>[] cols = new HashSet[9];
        @SuppressWarnings("unchecked")
        Set<Character>[] boxes = new HashSet[9];

        for (int i = 0; i < 9; i++) {
            rows[i] = new HashSet<>();
            cols[i] = new HashSet<>();
            boxes[i] = new HashSet<>();
        }

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char val = board[r][c];
                if (val == '.')
                    continue;

                int boxIdx = (r / 3) * 3 + (c / 3);

                if (!rows[r].add(val) || !cols[c].add(val) || !boxes[boxIdx].add(val))
                    return false;
            }
        }

        return true;
    }

    public static boolean isValidSudokuBitmask(char[][] board) {
        int[] rows = new int[9];
        int[] cols = new int[9];
        int[] boxes = new int[9];

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char val = board[r][c];
                if (val == '.')
                    continue;

                int idx = val - '1';
                int bit = 1 << idx;
                int boxId = (r / 3) * 3 + (c / 3);

                if ((rows[r] & bit) != 0 || (cols[c] & bit) != 0 || (boxes[boxId] & bit) != 0)
                    return false;

                rows[r] |= bit;
                cols[c] |= bit;
                boxes[boxId] |= bit;
            }
        }

        return true;
    }
}
