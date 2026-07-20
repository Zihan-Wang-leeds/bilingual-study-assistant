#!/usr/bin/env python3
"""Fix Unicode matrix bracket characters in generated guides → LaTeX pmatrix."""
import sys

LEFT_TOP, LEFT_MID, LEFT_BOT = '⎛', '⎜', '⎝'
RIGHT_TOP, RIGHT_MID, RIGHT_BOT = '⎞', '⎟', '⎠'
LEFT_CHARS = {LEFT_TOP, LEFT_MID, LEFT_BOT}
RIGHT_CHARS = {RIGHT_TOP, RIGHT_MID, RIGHT_BOT}
ALL_BRACKET = LEFT_CHARS | RIGHT_CHARS


def _has_left_bracket(line):
    """Check if a line is a left-bracket line (may have arbitrary prefix)."""
    stripped = line.strip()
    if not stripped:
        return False
    # Find the bracket sequence: last contiguous run of LEFT_CHARS
    in_bracket = False
    for c in stripped:
        if c in LEFT_CHARS:
            if not in_bracket:
                in_bracket = True
        elif in_bracket:
            # Non-bracket char after bracket sequence means mixed content
            return False
    return in_bracket


def _has_right_bracket(line):
    """Check if a line is a right-bracket line."""
    stripped = line.strip()
    if not stripped:
        return False
    in_bracket = False
    for c in stripped:
        if c in RIGHT_CHARS:
            if not in_bracket:
                in_bracket = True
        elif in_bracket:
            return False
    return in_bracket


def fix_text(text):
    """Find and replace all Unicode matrix blocks in text."""
    lines = text.split('\n')
    out = []
    i = 0
    changes = 0

    while i < len(lines):
        line = lines[i]

        # Check if this line starts a matrix: has LEFT_TOP (possibly with prefix like "Q =")
        left_idx = line.find(LEFT_TOP)
        if left_idx >= 0:
            first_prefix = line[:left_idx]
            bracket_part = line[left_idx:].strip()

            # Count left bracket chars on this line
            left_count = sum(1 for c in bracket_part if c in LEFT_CHARS)

            if left_count >= 2:
                # === COMPACT format: all brackets on one line ===
                # "Q = ⎛⎜⎝" on one line, matching "⎞⎟⎠" on another
                bracket_height = left_count
                if LEFT_BOT not in bracket_part:
                    out.append(line)
                    i += 1
                    continue

                # Collect elements until right bracket line
                elements = []
                k = i + 1
                while k < len(lines):
                    r_count = sum(1 for c in lines[k].strip() if c in RIGHT_CHARS)
                    if r_count >= 2:
                        break
                    stripped = lines[k].strip()
                    if stripped:
                        elements.append(stripped)
                    k += 1
                else:
                    out.append(line)
                    i += 1
                    continue

                # Right bracket line should have matching count
                right_line = lines[k].strip()
                r_count = sum(1 for c in right_line if c in RIGHT_CHARS)
                if r_count != bracket_height or RIGHT_BOT not in right_line:
                    out.append(line)
                    i += 1
                    continue

                right_lines = [lines[k]]
                k += 1

            else:
                # === MULTI-LINE format: each bracket char on its own line ===
                left_lines = []
                j = i
                while j < len(lines) and _has_left_bracket(lines[j]):
                    left_lines.append(lines[j])
                    j += 1

                bracket_height = len(left_lines)
                if bracket_height < 2:
                    out.append(line)
                    i += 1
                    continue

                if LEFT_BOT not in left_lines[-1]:
                    out.append(line)
                    i += 1
                    continue

                # Collect elements between left and right brackets
                elements = []
                k = j
                while k < len(lines):
                    if _has_right_bracket(lines[k]):
                        break
                    stripped = lines[k].strip()
                    if stripped:
                        elements.append(stripped)
                    k += 1

                # Collect right bracket lines
                right_lines = []
                while k < len(lines) and _has_right_bracket(lines[k]):
                    right_lines.append(lines[k])
                    k += 1

                if not right_lines or RIGHT_BOT not in right_lines[-1] or len(right_lines) != bracket_height:
                    out.append(line)
                    i += 1
                    continue

            # Determine matrix dimensions — split each line into space-separated columns
            split_rows = []
            for el in elements:
                parts = el.split()
                if parts:
                    split_rows.append(parts)

            # Check if all rows have the same number of columns (and > 1)
            col_counts = set(len(r) for r in split_rows)
            if len(col_counts) == 1:
                cols = col_counts.pop()
                if cols >= 2:
                    # Build from split rows
                    matrix_rows = [' & '.join(r) for r in split_rows]
                else:
                    # Single column: elements are already one per line
                    matrix_rows = elements[:]
            else:
                # Uneven rows, fallback to flat list
                matrix_rows = elements[:]

            latex = first_prefix + '\n$$\n\\begin{pmatrix}\n'
            latex += ' \\\\\n'.join(matrix_rows)
            latex += '\n\\end{pmatrix}\n$$'

            out.append(latex)
            i = k
            changes += 1
        else:
            out.append(line)
            i += 1

    return '\n'.join(out), changes


def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    if not any(c in text for c in ALL_BRACKET):
        return 0

    fixed, changes = fix_text(text)
    if changes == 0:
        return 0

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed)
    return changes


def main():
    files = sys.argv[1:]
    if not files:
        print("Usage: fix_unicode_matrices.py <file1> <file2> ...")
        sys.exit(1)

    total = 0
    for f in files:
        try:
            n = fix_file(f)
            if n > 0:
                print(f"  ✓ {f} ({n} matrices)")
                total += n
            else:
                print(f"  - {f} (no changes)")
        except Exception as e:
            print(f"  ✗ {f}: {e}")

    print(f"\nTotal: {total} matrices fixed in {len(files)} files")


if __name__ == '__main__':
    main()
