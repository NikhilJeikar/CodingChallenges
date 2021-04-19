Testcases = int(input())
for Testcase in range(Testcases):
    Length = int(input())
    String = list(input())
    Prev = 0
    Count = 0
    print(f"Case #{Testcase+1}: ",end="")
    for Char in String[:]:
        if ord(Char) > Prev:
            Prev = ord(Char)
            Count = Count + 1
        else:
            Prev = ord(Char)
            Count = 1
        print(Count,end=" ")
    print()

"""
2
4
ABBC
6
ABACDA

"""