def solve():
    # m row, n column
    [rows, columns] = input().split(' ')
    rows = int(rows)
    columns = int(columns)
    firstOccuranceFound = False
    expectedSideLength = 0
    # First, to see if it's a rectangle, find the first "chunk" and see if it matches the below
    for r in range(rows):
        row = input()
        currentSideLength = 0
        for c in range(columns):
            if row[c] == "#":
                currentSideLength += 1
        
        if not firstOccuranceFound and currentSideLength != 0:
            firstOccuranceFound = True
            expectedSideLength = currentSideLength
        else:
            # if the above hastags don't match the below and it's not just the end of the rectange than we have a problem
            if currentSideLength > 0 and currentSideLength != expectedSideLength:
                # print(currentSideLength, r)
                for i in range((rows) - (r + 1)):
                    input()
                print("phineas")
                return
    print("ferb")

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()