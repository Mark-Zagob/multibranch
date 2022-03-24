n = int(input("nhap n: "))
s = [int(input("==> ")) for i in range(n)]
k = []
min = s[0]
i = 0
while i < n :
    if min < s[i+1] :
        min = s[i]
        k[i] = s[i]
        k[i+1] = s[i+1]
    else:
        min = s[i+1]
        k[i]= s[i+1]
        k[i+1] = s[i]
    i+=1
print(type(k))
print(k)
print("hello world")
