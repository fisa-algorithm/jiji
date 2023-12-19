# 다이나믹 프로그래밍

def prac(a,b):
    sz = int(a)
    inp = [int(x) for x in b.split(" ")]
    total = inp[0]
    big = inp[0]

    for x in inp[1:]:
        if total + x > x:
            total += x
        else:
            if(total < x):
                total = x
        if (total > big):
            big = total
    print(big)







prac("10", "10 -4 3 1 5 6 -35 12 21 -1")
prac("10","2 1 -4 3 4 -4 6 5 -5 1")
prac("5","-1 -2 -3 -4 -5")
