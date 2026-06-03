function isValidSudokuSet(board: string[][]): boolean {
    const rows: Set<string>[] = Array.from({ length: 9 }, () => new Set());
    const cols: Set<string>[] = Array.from({ length: 9 }, () => new Set());
    const boxes: Set<string>[] = Array.from({ length: 9 }, () => new Set());

    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            const val = board[r][c];
            if (val === '.') continue;

            const boxIdx = Math.floor(r / 3) * 3 + Math.floor(c / 3);

            if (rows[r].has(val) || cols[c].has(val) || boxes[boxIdx].has(val)) return false;

            rows[r].add(val);
            cols[c].add(val);
            boxes[boxIdx].add(val);
        }
    }

    return true;
}

function isValidSudokuBitmask(board: string[][]): boolean {
    const rows = new Array(9).fill(0);
    const cols = new Array(9).fill(0);
    const boxes = new Array(9).fill(0);

    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            const val = board[r][c];
            if (val === '.') continue;

            const idx = parseInt(val) - 1;
            const bit = 1 << idx;
            const boxId = Math.floor(r / 3) * 3 + Math.floor(c / 3);

            if (rows[r] & bit || cols[c] & bit || boxes[boxId] & bit) return false;

            rows[r] |= bit;
            cols[c] |= bit;
            boxes[boxId] |= bit;
        }
    }

    return true;
}
