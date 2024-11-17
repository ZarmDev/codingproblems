import math
# ● N:startinghealth
# ● H:healingpersecond
# ● D:distancetoexitstorm(inmeters)
# ● S:runningspeed(inmeterspersecond)
# ● P:stormdamagepersecond

def solve(N,H,D,S,P) -> int:
    mintime = 0
    # first try running
    D2 = D
    health = N
    seconds = 0
    while (True):
        D2 -= S
        health -= P
        if D <= 0:
            mintime = seconds
            break
        if health <= 0:
            break
        seconds += 1
    
    while (True):
        health -= P
        if health <= 0:
            break
        seconds += 1
    
    print(mintime)
    # if(C/D) <= (A/E):
    #     return C/D
    # if(B<E):
    #     return - 1
    # need = C/D
    # needHealth = abs(A - need*E)
    # timeHeal = B-E
    # extraT = needHealth/timeHeal
    # return need + extraT

def main():
    T = int(input())
    for _ in range(T):
        AB= input().split(' ')
        A, B , C ,D ,E = int(AB[0]), int(AB[1]), int(AB[2]), int(AB[3]), int(AB[4])
        print(solve(A, B,C,D,E))


if __name__ == '__main__':
    main()

