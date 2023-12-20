def makeMax(arr):
    temp = 0
    last = 0
    n = len(arr)
    if n%2==1:
        n -= 1
        last = arr[-1]
    for i in range(0, n, 2):
        temp += arr[i] * arr[i+1]
    return temp + last

def prac():
    one = 0
    if sz ==1 :
        return inp[0]
    for x in inp:
        if x <= 0:
            neg.append(x)
        else:
            if x != 1 :
                pos.append(x)
            else:
                one+=1
    neg.sort()
    pos.sort(reverse=True)
    return makeMax(neg) + makeMax(pos) + one

sz = int(input())
inp = []
for _ in range(sz):
    inp.append(int(input()))
pos =[]
neg= []

print("answer : ",prac())
