TestCases = int(input())

for TestCase in range(TestCases):
    N = int(input())
    Inputs = input()
    Inputs = [int(Input) for Input in Inputs.split(' ')]
    Cost = 0
    for i in range(0,len(Inputs) - 1):
        Min = min(Inputs[i:])
        Min = Inputs.index(Min)
        Buffer = Inputs[i:Min + 1]
        Buffer.reverse()
        Inputs = Inputs[:i] + Buffer + Inputs[Min + 1:]
        Cost = Cost + 1 + Min - i
    print(f"Case #{TestCase+1}: {Cost}")

"""
Test case
3
4
4 2 1 3
2
1 2
7
7 6 5 4 3 2 1

1
7
7 5 6 3 1 2 4
"""