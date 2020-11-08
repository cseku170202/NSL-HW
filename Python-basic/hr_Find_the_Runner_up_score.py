from collections import Counter
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    List = []
    for i in arr:
        List.append(i)
    List.sort()
    List.reverse()
    unigram = list(Counter(List))
    print(unigram[1])