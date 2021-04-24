TestCases = int(input())
for TestCase in range(TestCases):
    Params = input().split(" ")
    N = int(Params[0])
    K = int(Params[1])
    String = list(input())
    Center = int(len(String) / 2)
    Goodness = 0
    print(f"Case #{TestCase + 1}: ",end="")
    for i in range(0, Center):
        A = i
        B = N - i - 1
        if String[A] != String[B]:
            Goodness = Goodness + 1
    if K - Goodness == 0:
        print(0)
    elif K - Goodness > 0:
        print(K - Goodness)
    elif K - Goodness < 0:
        print(Goodness-K)

"""
2
5 1
ABCAA
4 2
ABAA

"""
