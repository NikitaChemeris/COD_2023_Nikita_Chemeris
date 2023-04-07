# Romb with recursion

def romb(n):
    if n == 15:
        return
    else:
        top = '*' * n
        print(top.center(15))
        romb(n + 2)
        down = '*' * (n - 2)  # (n - 2) - for side corners
        print(down.center(15))
        return ''


print(romb(1))
