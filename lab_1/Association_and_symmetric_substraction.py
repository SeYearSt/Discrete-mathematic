import os.path

#function for check if element exist in list
def is_exist(el,list):
    for x in list:
        if x == el:
            return True
    return False


def get_united_set(A,B):
    united_set = set()
    for x in A:
       united_set.add(x)
    for x in B:
        united_set.add(x)
    return united_set

def get_symmetric_substraction_set(A,B):
    symmetric_substraction_set = get_united_set(A,B)
    
    temp_list = [x for x in A if x in B]
    
    for x in temp_list:
        symmetric_substraction_set.remove(x)
    if len(symmetric_substraction_set) == 0:
        return 0
    else:
        return symmetric_substraction_set
    
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def get_int():
    while True:
        n = input("Input int: ")
        if is_int(n):
            return int(n)

def get_list(char):
    temp_set = set()
    while True:
        print("Enter size of array:")
        n = get_int()
        
        if n >= 1:
            break
        
    for i in range(n):
        print(char,"[{}] = ".format(i+1),end='')
        n = get_int()
        temp_set.add(n)
    return temp_set


def get_lists_from_file(file_name):
   A = set()
   B = set()
   if os.path.exists(file_name):
       file = open(file_name,'r')
       A = {int(x) for x in file.readline().split()}
       #print(A)
       B = {int(x) for x in file.readline().split()}
       #print(B)
       file.close()
   else:
        print("Fail to open file")
   return A,B

#file = input("Enter name of file: ")
#print(os.path.exists(file))

def main():
    A = set()
    B = set()
    print("Enter 1 - input list from keyboard, 2 - input list from file")
    while True:
        control = get_int()
        if control == 1:
                   A = get_list('A')
                   B = get_list('B')
        elif control == 2 :
                   file_name = input("Enter file name:")
                   A, B = get_lists_from_file(file_name)
                   if len(A) == 0 or len(B) == 0:
                       print('End of program!')
                       return;
        if (control == 1 or control == 2):
                   break
   
    print('A =',A)
    print('B =', B)
    print('A united B =',get_united_set(A,B))
    print('A symmetric_substraction_set B =',get_symmetric_substraction_set(A,B))
    print('End of program!')
