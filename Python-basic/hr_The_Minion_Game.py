
from collections import Counter

def minion_game(string):
    s1 = 0
    s2 = 0
    length = len(string)
    List = [string[i:j] for i in range(length) for j in range(i+1, length+1)]
    #print(List)
    counts = Counter(List)
    #print(counts)

    newList = list(Counter(List))

    for i in newList:
        if i.startswith("A") or i.startswith("E") or i.startswith("I") or i.startswith("O") or i.startswith("U"):
            s1 = s1 + counts[i]
        else:
            s2 = s2 + counts[i]
    #print(s1)
    #print(s2)
    if s1 > s2:
        print("Kevin" + " "+str(s1))
    if s2 > s1:
        print("Stuart" + " "+str(s2))
    if s1==s2:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)