in1 = input()

def fillIn(sz):
    half = sz/2
    ans = ""
    if sz == 2 :
        return "BB"
    elif sz == 4 :
        return "AAAA"
    else :
        ans += "AAAA" * (sz//4)
        if half % 2 == 1 :
            ans += "BB"
        return ans
        
in1 += "."
cnt = 0
ans = ""
size = len(in1)
for i in range(len(in1)):
    if in1[i] == 'X':
        cnt += 1
    else:
        if cnt % 2 != 0:
            ans = "-1"
            break
        ans += fillIn(cnt)
        if (i < size-1):
            ans += "."
        cnt = 0

print(ans)
