# Romb with recursion

print("""Size romb, it must be odd number!
TYPE:
1.small 5 - 11
2.medium 13 - 21
3.big 23>
-----------------""")
size = int(input('Enter size romb: '))


def romb(process):
    if process == size:
        return
    else:
        top = '*' * process
        print(top.center(size))
        romb(process + 2)
        down = '*' * (process - 2)
        print(down.center(size))
        return ''


print(romb(1))
