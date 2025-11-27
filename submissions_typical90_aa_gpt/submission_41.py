MOD=10**6+3
B=30
n=int(input())
table=["" for _ in range(MOD)]
def f(s):
    hash=0
    for i in range(len(s)):
        hash+=ord(s[i])*pow(B, i, MOD)
        hash%=MOD
    return hash
for i in range(n):
    s=input()
    hash=f(s)
    if table[hash]!="":
        continue
    table[hash]=s
    print(i+1)
