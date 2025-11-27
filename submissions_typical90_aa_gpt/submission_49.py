def function():
    S_cat = ""
    N = int(input())
    for i in range(N):
        S = str(input())
        if(not S in S_cat):
            S_cat = S_cat + '/' + S
            print(i+1)

if   __name__ == "__main__":
    function()