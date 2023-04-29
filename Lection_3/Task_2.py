# Romb with recursion

print("""Size romb, it must be odd number!
TYPE:
1.small 5 - 11
2.medium 13 - 21
3.big 23>
-----------------""")
amount_lines = int(input('Enter size romb: '))


def romb(process):
    if process == amount_lines:
        return
    else:
        top = '*' * process
        print(top.center(amount_lines))
        romb(process + 2)
        down = '*' * (process - 2)
        print(down.center(amount_lines))
        return ''


print(romb(1))
