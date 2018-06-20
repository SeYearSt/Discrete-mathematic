import string
operators = {'!':1, '&':2, '|':2}

#for op in operators:
#    operators_list.append(op.keys())

def get_count_operators(operator):
    for op in operators:
        if operator in list(op):
            return op[operator]
    return 0


'''symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' , 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']'''

first_symbols = list(string.ascii_lowercase)

all_symbols = list(string.ascii_lowercase)
all_symbols.extend(list(string.digits))




def get_characters(str):
    res = []
    for c in str:
        if c != " ":
            res.append(c)
    return res

def get_operators_vars_mistakes(characters):
    res = []
    i = 0
    while i < len(characters):
        pr = 0
        if characters[i] in first_symbols:
            pr = 1
            var = characters[i]

            while(True):
                if i >= len(characters):
                    res.append({var: 'variable'})
                    return res
                if characters[i] in all_symbols:
                    var += characters[i]
                else:
                    res.append({var: 'variable'})
                    pr = 0
                    #i -= 1
                    break
                i += 1

        if characters[i] in operators:
            operator = characters[i]
            count = operators[operator]
            j = 1
            while j < count:
                i += 1
                if i >= len(characters):
                    i -= 1
                    break
                if characters[i] in operators and operator == characters[i]:
                    operator += characters[i]
                    j += 1
                else:
                    i -= j
                    break
            if j == count:
                res.append({operator: 'operator'})
                pr = 1
        if not pr:
            mistake = ""
            mistake += characters[i]
            res.append({mistake: 'mistake'})

        i += 1
    return res

def avail_mistakes(op_var):
    for e in op_var:
        if 'mistake' == list(e.values())[0]:
            return 1
    return 0

def right(operators_vars_mistakes):
#operators_vars_mistakes[0].get()
    if  any([list(e.values())[0] == "variable" for e in operators_vars_mistakes]):

        #перевіряємо чи перед першою змінною є який оператор окрім дов. к-сть !
        for i in range(len(operators_vars_mistakes)):
            if list(operators_vars_mistakes[i].values())[0] == "variable":
                for j in range(i):
                    if list(operators_vars_mistakes[j].keys())[0] != "!":
                        return False
                break

        #перевіряємо чи в кінці є якийсь оператор
        if list(operators_vars_mistakes[len(operators_vars_mistakes) - 1].values())[0] == "operator":
            return False

        #перевіряємо чи є між змінними один опертора
        for i in range(len(operators_vars_mistakes)):
            if list(operators_vars_mistakes[i].values())[0] == "variable":
                for j in range(i+1, len(operators_vars_mistakes)):
                    if list(operators_vars_mistakes[j].values())[0] == "variable":
                        operator_count = 0
                        for k in range(i+1, j):
                            if list(operators_vars_mistakes[k].values())[0] == "operator" and \
                                    list(operators_vars_mistakes[k].keys())[0] != "!":
                                operator_count += 1
                        if operator_count == 0 or operator_count > 1:
                            return False
                        break

        return True

    else:
        return False

def main():

    str = input("Input string: ")

   # print("You input:", str)

    operators_vars_mistakes = get_operators_vars_mistakes(get_characters(str))

   # print(operators_vars_mistakes)

    if avail_mistakes(operators_vars_mistakes):
        print("Input is incorrect!\n")
        return -1

    if not right(operators_vars_mistakes):
        print("Input is incorrect!\n")
        return -1
    else:
        print("Input is correct\n")

    input('Press any key to exit')

main()