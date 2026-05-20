from collections import defaultdict


def is_valid_sudoku_set(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue

            # Map the 3x3 sub-box to an index from 0 to 8
            box_idx = (r // 3) * 3 + (c // 3)

            # Check for duplicates
            if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                return False

            # Add to the respective sets
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)

    return True


def is_valid_sudoku_dict(board: list[list[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            box = (r // 3, c // 3)
            if val == '.':
                continue

            # Check for duplicates
            if val in rows[r] or val in cols[c] or val in boxes[box]:
                return False

            # Add to the respective sets
            rows[r].add(val)
            cols[c].add(val)
            boxes[box].add(val)

    return True


def is_valid_sudoku_one_set(board: list[list[str]]) -> bool:
    seen = set()
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val != '.':
                # Create unique identifiers for row, column, and 3x3 block
                # Format: (value, row_index), (value, col_index), (value, block_row, block_col)
                row_key = (val, r, 'row')
                col_key = (val, c, 'col')
                box_key = (val, r // 3, c // 3, 'box')

                # If any of these "claims" already exist, it's a duplicate
                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                # Add current digit's unique constraints to the single set
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

    return True


def is_valid_sudoku_fixed_size_array(board: list[list[str]]) -> bool:
    rows = [[0] * 9 for _ in range(9)]
    cols = [[0] * 9 for _ in range(9)]
    boxes = [[0] * 9 for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]

            if val == '.':
                continue

            idx = int(val) - 1
            box_id = (r // 3) * 3 + (c // 3)

            if rows[r][idx] or cols[c][idx] or boxes[box_id]:
                return False

            rows[r][idx] = 1
            cols[c][idx] = 1
            boxes[box_id][idx] = 1

    return True


def is_valid_sudoku_bitmask(board: list[list[int]]) -> bool:
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9

    for r in range(9):
        for c in range(9):
            val = board[r][c]

            if val == '.':
                continue

            idx = int(val) - 1
            bit = 1 << idx
            box_id = (r // 3) * 3 + (c // 3)

            if rows[r] & bit or cols[c] & bit or boxes[box_id] & bit:
                return False

            rows[r] |= bit
            cols[c] |= bit
            boxes[box_id] |= bit

    return True
