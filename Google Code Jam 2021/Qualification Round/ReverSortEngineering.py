"""
# BruteForce Method

TestCases = int(input())

def ReverSort(Inputs):
    Cost = 0
    for i in range(len(Inputs) - 1):
        Min = min(Inputs[i:])
        Min = Inputs.index(Min)
        Buffer = Inputs[i:Min + 1]
        Buffer.reverse()
        Inputs = Inputs[:i] + Buffer + Inputs[Min + 1:]
        Cost = Cost + 1 + Min - i
    return Cost

def permute(data, i, length, Cost):
    global Stop, Break
    if i == length:
        C = ReverSort(data)
        if C == Cost:
            Str = " ".join([str(i) for i in data])
            print(f"Case #{TestCase + 1}: {Str}")
            Stop = False
            Break = False
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length, Cost)
            data[i], data[j] = data[j], data[i]

for TestCase in range(TestCases):
    Break = True
    Stop = True
    Raw = input().split(' ')
    N = int(Raw[0])
    C = int(Raw[1])
    if C + 1 < N or C + 1 > ((N + 1) * N) / 2:
        Final = []
        print(f"Case #{TestCase + 1}: IMPOSSIBLE")
        Stop = False
    else:
        Final = []
        for i in range(1, N + 1):
            Final.append(i)
        permute(Final, 0, N, C)

    if Stop:
        print(f"Case #{TestCase + 1}: IMPOSSIBLE")

"""

# Logical Method

TestCases = int(input())

for TestCase in range(TestCases):
    Raw = input().split(' ')
    N = int(Raw[0])
    C = int(Raw[1]) + 1
    if C < N or C > ((N + 1) * N) / 2:
        print(f"Case #{TestCase + 1}: IMPOSSIBLE")
    else:
        Sorted = [i for i in range(N)]
        C = C - N
        for i in range(N-1,-1,-1):
            Min = min(C,N-1-i)
            C = C - Min
            Buffer = Sorted[i:i+Min+1]
            Buffer.reverse()
            Sorted = Sorted[0:i] + Buffer + Sorted[i+Min+1:]

        Str = " ".join(str(i+1) for i in Sorted)
        print(f"Case #{TestCase + 1}: {Str}")


"""
TestCase
5
4 6
2 1
7 12
7 2
2 1000
"""
