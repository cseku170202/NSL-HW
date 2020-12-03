def merge_the_tools(string, k):
    s1 = ""
    length = len(string)
    for i in range(0, length, k):
        for j in range(i,i+k):
            s1 = s1 + string[j]
        #print(s1)
        t = 0
        s2 = ""
        for p in s1:
            if s1.index(p)==t:
                s2 = s2 + p
            t += 1
        print(s2)
        s1 = ""

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)