t = int(input())
while t:
    a, b = map(int, input().split())
    if b==0:
        print('0',end=" ")
        print(a)
    else:
        x = "{0:b}".format(a)
        y = "{0:b}".format(b)
        lx = len(x)
        ly = len(y)
        if ly < lx:
            s = '0'+str(lx)+'b'
            y = format(b,s)
            lyy = len(y)
            maxi = 0
            for k in range(lyy):
                l = [ord(i)^ord(j) for i,j in zip(x,y)]
                xor = int(str(int(''.join(map(str,l)))),2)
                if xor > maxi:
                    maxi = xor
                    count = k
                else:
                    pass
                y = y[-1]+y[:-1]
            print(count,end=" ")
            print(maxi)
        else:
            y0 = y[0]
            if (all(c == y0 for c in y[1:])):
                maxi = a^b
                count = 0
            else:
                maxi = 0
                for k in range(ly):
                    xor = a^b
                    if xor > maxi:
                        maxi = xor
                        count = k
                    else:
                        pass
                    y = y[-1]+y[:-1]
                    b = int(y,2)
            print(count,end=" ")
            print(maxi)
    t -= 1