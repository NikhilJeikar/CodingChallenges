TestCases = int(input())

for TestCase in range(TestCases):
    Prices = input()
    Prices = Prices.split(' ')
    X = int(Prices[0])
    Y = int(Prices[1])
    String = []
    Cost = 0
    for i in Prices[2]:
        String.append(i)
    Out = (0, 0)
    for Char in range(len(String)):
        # print(Char,len(String))
        Prev = ""
        Next = ""
        if String[Char] == "?":
            if Char == len(String) - 1:
                Prev = String[Char - 1]
            elif Char == 0:
                Next = String[Char + 1]
            else:
                Prev = String[Char - 1]
                Next = String[Char + 1]

            Current = ""
            if Prev == "J":
                if Next == "J":
                    Current = "J"
                elif Next == "C":
                    Current = "J"
                elif Next == "?":
                    Current = Prev
                else:
                    Current = Prev
            elif Prev == "C":
                if Next == "J":
                    Current = "C"
                elif Next == "C":
                    Current = "C"
                elif Next == "?":
                    Current = Prev
                else:
                    Current = Prev
            elif Prev == "":
                x, y = Out
                Out = (x, Char)
                if Next != "?":
                    XR, YR = Out
                    for i in range(YR + 1):
                        Current = Next
                        String[i] = Current

            String[Char] = Current

    Prev = String[0]
    for Char in String[1:]:
        if Prev == "J" and Char == "C":
            Cost = Cost + Y
        elif Prev == "C" and Char == "J":
            Cost = Cost + X
        else:
            pass
        Prev = Char

    print(f"Case #{TestCase+1}: {Cost}")

"""
Test Set 1 and 2 solved 
Test Set 3 pending
"""