# -------- U T I L I T I E S -------- #

def box_format(s, width=10, height=4):
    s_lines = s.split('\n')
    wrapped_s_lines = []
    for line in s_lines:
        if len(line) > width:
            line_chunks = [line[i:i+width] for i in range(0, len(line), width)]
            wrapped_s_lines += line_chunks
    if len(wrapped_s_lines) > height:
        wrapped_s_lines[3] = '...'
        return '\n'.join(wrapped_s_lines[0:height])
    else:
        return '\n'.join(wrapped_s_lines)

def print_side_by_side(a, b, size=75, space=4):

    a_lines = a.split('\n')
    b_lines = b.split('\n')
    wrapped_a_lines = []
    wrapped_b_lines = []

    # break them up into lines cut off at the line length limit
    for i in range(0, max(len(a_lines), len(b_lines))):
        a = a_lines[i] if i < len(a_lines) else " " * size
        b = b_lines[i] if i < len(b_lines) else " " * size
        if len(a) > size:
            wrapped_a_lines.append(a[:size])
            wrapped_a_lines.append(a[size:])
        else:
            wrapped_a_lines.append(a)
        if len(b) > size:
            wrapped_b_lines.append(b[:size])
            wrapped_b_lines.append(b[size:])
        else:
            wrapped_b_lines.append(b)

    padded_a_lines = [line + (" " * (size - len(line))) for line in wrapped_a_lines]
    padded_b_lines = [line + (" " * (size - len(line))) for line in wrapped_b_lines]

    for i in range(max(len(padded_a_lines), len(padded_b_lines))):
        a_line = padded_a_lines[i] if i < len(padded_a_lines) else " " * size
        b_line = padded_b_lines[i] if i < len(padded_b_lines) else " " * size
        print(a_line + " " * space + b_line)