def count(n):
    if n == 0:
        return "0"
    else:
        s = str(n) + " " + count(n-1)
        return s

print(count(1))