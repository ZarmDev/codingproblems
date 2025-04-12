import math

def solve():
    word = input()
    c = ["u", "n", "c"]
    i = ["i", "h"]
    # lettersInCalico = ["l", "u", "n", "c", "h", "i", "o", "a"]
    # c, a, l, i, o
    letters = [0, 0, 0, 0, 0]
    for l in word:
        l = l.lower()
        if l in c:
            letters[0] += 1
        elif l in i:
            letters[3] += 1
        elif l == "a":
            letters[1] += 1
        elif l == "l":
            letters[2] += 1
        elif l == "o":
            letters[4] += 1
        else:
            print(-1)
            return
    # edge case: no letters can be used
    if max(letters) == 0:
        print(-1)
        return
    # if the max is C then make sure to account for two c's
    # print(letters.index(max(letters)))
    if max(letters) == letters[0]:
        # make sure definitivaly that c is bigger than the rest
        if (letters[0] / 2) > max(letters[1:]):
            # use c then, round up because you need extra calico characters
            print(math.ceil(letters[0] / 2))
            return
        else:
            print(max(letters[1:]))
            return
    else:
        print(max(letters))
        return
            
def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()
