#function for check if element exist in list
def exist_in_list(el,list):
    for x in list:
        if x == el:
            return True
    return False

#opening file in working directory
lists_file = open('lists_file.txt','r')

#create lists with int numbers from file
first_list = [ int(x) for x in lists_file.readline().split()]
second_list = [ int(x) for x in lists_file.readline().split()]

#closing file
lists_file.close()

# creating list that contain first list without the second one
substraction = [el for el in first_list if not exist_in_list(el,second_list)]

#create list that contain elements that exist in both lists
joint = [x for x in first_list if exist_in_list(x,second_list)]

print("A =",first_list)
print("B =",second_list)
print("A(joint)B=",joint)
print("A\B =",substraction)

#pause
#n = input("end of program")
input("Press any key.")