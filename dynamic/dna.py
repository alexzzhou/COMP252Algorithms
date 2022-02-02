
def add_to_matrix(a, b):
    try:
        a += b
    except IndexError:
        return

def solve(na: int, nc: int, nt: int, ng: int):

    #setting up array
    dp = [[[[[0 for i in range(4)] for j in range(ng+1)] for k in range(nt+1)] for l in range(nc+1)] for m in range(na+1)]

    
    #Setting up base cases where there is only a single element in the array
    try:
        dp[1][0][0][0][0] = 1
    except IndexError:
        pass
    try:
        dp[0][1][0][0][1] = 1
    except IndexError:
        pass
    try:
        dp[0][0][1][0][2] = 1
    except IndexError:
        pass
    try:
        dp[0][0][0][1][3] = 1
    except IndexError:
        pass

    for a in range(na+1):
        for c in range(nc+1):
            for t in range(nt+1):
                for g in range(ng+1):
                    for char in "ACTG":
                        #debug
                        print(str(a)+str(c)+str(t)+str(g)+char)

                        if char == "A":
                            if a == 0:
                                continue
                            else:
                                for i in range(4):
                                    dp[a][c][t][g][0] += dp[a-1][c][t][g][i]
                                    

                        elif char == "C":
                            if c == 0:
                                continue
                            else:
                                for i in range(4):
                                    dp[a][c][t][g][1] += dp[a][c-1][t][g][i]
                                    
                        elif char == "T":
                            if t == 0:
                                continue
                            else:
                                for i in range(4):
                                    if i == 2:
                                        pass
                                    else:
                                        dp[a][c][t][g][2] += dp[a][c][t-1][g][i]

                        elif char == "G":
                            if g == 0:
                                continue
                            else:
                                for i in range(4):
                                    if i == 3:
                                        pass
                                    else:
                                        dp[a][c][t][g][3] += dp[a][c][t][g-1][i]


    print(dp)
    final = 0

    for i in range(4):
        try:
            final += dp[na][nc][nt][ng][i]
        except IndexError:
            pass

    return final
    

print(solve(2,2,4,4))
