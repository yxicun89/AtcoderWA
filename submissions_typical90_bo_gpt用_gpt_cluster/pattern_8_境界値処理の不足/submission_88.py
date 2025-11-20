def convert_base_n_to_base_m(num_str: str, from_base: int, to_base: int, length: int) -> int or None:

    num_str = str(num_str).lower()
    valid_char = '0123456789abcdefghijklmnopqrstuvwxyz'

    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
        return None

    #from_base進数から１０進数に変換.
    base_10_num = 0
    for i, char in enumerate(reversed(num_str)):
        value = valid_char.index(char)
        if value >= from_base:
            return None
        base_10_num += value * (from_base ** i)

    #10進数からto_base進数に変換.
    base_new_str = ''
    while base_10_num > 0:
        base_new_str = valid_char[base_10_num % to_base] + base_new_str
        base_10_num //= to_base

    return base_new_str.zfill(length)

N, K = input().split()
for _ in range(int(K)):
    N = convert_base_n_to_base_m(N, 8, 9, 0).replace('8', '5')
print(N)