d = ['x', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
t = ['x', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def numberToEnglish(n):
    # Numbers up to 999
    if n < 20 and n > -1:
        return d[n]
    elif n < 100:
        if n % 10 == 0:
            return t[(n//10)]
        a = (n % 10) 
        h =(n // 10) 
        s = str(t[h]) + '-' + str(d[a])
        return s
    else:
        a = (n % 10)
        n = (n // 10)
        b = n%10
        c = (n // 10)
        x = b*10 + a
        if x > 10 and x < 20:
            s = str(d[c]) + ' hundred and ' + str(d[x])
            return s
        if a == 0 and b == 0:
            return str(d[c]) + ' hundred'
        elif a == 0:
            s = str(d[c]) + ' hundred and ' + str(t[b])
            return s
        elif b == 0:
            s = str(d[c]) + ' hundred and ' + str(d[a])
            return s
        else:
            s = str(d[c]) + ' hundred and ' + str(t[b]) + '-' + str(d[a])
            return s

def count(s):
    res = 0
    for i in s:
        if i not in [' ', '-']:
            res += 1
    return res

def f():
    res = 0
    for i in range(1, 1000):
        res += count(numberToEnglish(i))
    res += len('onethousand')
    return res
print(f())  

def g():
    res = 0
    for i in range(1, 1000):
        print(numberToEnglish(i))


