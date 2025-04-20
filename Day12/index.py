def time_increment(h: int, m: int) -> tuple[int, int]:
    m += 1
    if m == 60:
        m = 0
        h += 1
        if h == 24:
            h = 0
    return h, m
print(time_increment(23, 59))  # Output: (0, 0)
print(time_increment(12, 30))  # Output: (12, 31)
print(time_increment(5, 59))   # Output: (6, 0)
