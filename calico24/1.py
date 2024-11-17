def solve(A: int, B: int) -> int:
    """
    Return the sum of A and B.
    
    A: a non-negative integer
    B: another non-negative integer
    """
    # YOUR CODE HERE
    return 0

def main():
    T = int(input())
    for _ in range(T):
        curr = input()
        # print(curr)
        for i in range(len(curr)):
            if curr[i] == "O":
                print("[###OREO###]")
            elif curr[i] == "R":
                print("[--------]")
                i += 2
            elif curr[i] == "&":
                print()

if __name__ == '__main__':
    main()
