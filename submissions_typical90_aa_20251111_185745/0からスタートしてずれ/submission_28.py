# My AtCoder Templates for Python ver0.1.3
# Edit:2024/09/10
import sys


def single_int_input():
    return int(sys.stdin.readline().rstrip())


def multi_int_input():
    return map(int, sys.stdin.readline().rstrip().split())


def list_int_input():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def single_string_input():
    return sys.stdin.readline().rstrip()


def multi_string_input():
    return sys.stdin.readline().rstrip().split()


def list_string_input():
    return list(sys.stdin.readline().rstrip().split())


# ----------------
def retry():
    N = single_int_input()
    set_ = set()
    
    for i in range(N):
        s = single_string_input()
        if s in set_:
            continue
        set_.add(s)
        print(i)

if __name__ == '__main__':
    retry()