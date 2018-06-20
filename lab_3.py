def input_func():
    func = []
    try:
        temp_list = [int(el) for el in input().split()]
    except ValueError:
        print('Cannot convert to int')
        return func
    for el in temp_list:
        if el == 0 or el == 1:
            func.append(el)
    return func

def is_power2(num):
	return num != 0 and ((num & (num - 1)) == 0)

def check_for_conflict(f):
    pr = True
    for el in f:
        if el == 1:
            pr = False
    return pr

def check_for_saving_zero(f):
    if f[0] == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print('Please input your function: ',end=' ')
    f = input_func()

    if is_power2(len(f)):
        if (check_for_conflict(f)):
            print("Function is conflictive (є суперечністтю)")
        else:
            print("Function  isn`t conflictive (не є суперечністтю)")
        if check_for_saving_zero(f):
            print("Function save zero (зберігає константу нуля)")
        else:
            print("Function don`t save zero (не зберігає константу нуля)")
    else:
        print('Incorrect data!')
    input('Press any key to exit')