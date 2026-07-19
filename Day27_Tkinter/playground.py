
def  add(*args):
    print(args[2])
    print(type(args))
    sum = 0
    for number in args:
        sum += number
    return sum


print(f"Total: {add(10,20,30,40,50)}")


