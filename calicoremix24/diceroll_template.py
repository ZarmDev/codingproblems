def solve(N: int, X: list[int]) -> int:
    """
    Return the best number to "zero out" in order to
    minimize the expected value of a dice roll.
    
    N: the number of faces on the die
    X: the list of numbers on each face of the die
    """
    # occurances = []
    # times = []
    # X.sort()
    highestProb = 0
    num = 0
    # for each dice face add up the other dice faces
    for i in range(N):
        payment = 0
        for z in range(N):
            # add all the other probabilities
            # if not(z == i):
            #     payment += X[z]
            payment += X[z]
        payment -= X[z]
        print(payment, X[i])
        if payment > highestProb:
            highestProb = payment
            num = X[i]
    
    return num


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X = [int(x) for x in input().strip().split(' ')]
        print(solve(N, X))

if __name__ == '__main__':
    main()
