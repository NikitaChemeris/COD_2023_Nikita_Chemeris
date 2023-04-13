# Romb with recursion

def romb(amount_lines):
    if amount_lines == 15:
        return
    else:
        top = '*' * amount_lines
        print(top.center(15))
        romb(amount_lines + 2)
        down = '*' * (amount_lines - 2)  # (n - 2) - for side corners
        print(down.center(15))
        return ''


print(romb(1))
