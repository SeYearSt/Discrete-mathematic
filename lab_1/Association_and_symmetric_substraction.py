#function for check if element exist in list
def is_exist(el,list):
    for x in list:
        if x == el:
            return True
    return False

#opening file in working directory
lists_file = open('lists_file.txt','r')


first_set = {int(x) for x in lists_file.readline().split()}
second_set = {int(x) for x in lists_file.readline().split()}
lists_file.close()

united_set = set()



for x in first_set:
    united_set.add(x)
for x in second_set:
    united_set.add(x)
    
symmetric_substraction_set = {x for x in united_set}

temp_list = [x for x in first_set if is_exist(x,second_set)]


for x in temp_list:
    symmetric_substraction_set.remove(x)
    
print("A =",first_set)
print("B =",second_set)
print("A(united)B =",united_set)
print("common_elements = ",temp_list)
print("symmetric substraction of sets A, B =",symmetric_substraction_set)
