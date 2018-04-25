import os

global posible_placements
posible_placements = []

def get_students_from_file(file_name):
    if os.path.exists(file_name):
       file = open(file_name, 'r')
       file_2 = open(file_name,'r') # change like in cpp move ptr to first line
       return  ([0 for student in file.readline().split()],[x for x in file_2.readline().split()])
    else:
        print("File don`t exist")
        return


def set_placement(place, objects, index):
    new_place = place[:]

    if not objects:
        posible_placements.append(new_place)
        return

    for el in objects:
        temp_objects = [x for x in objects if x != el]
        new_place[index] = el
        set_placement(new_place, temp_objects, index + 1)


def print_students_in_rooms(placement):
    count = 0
    for el in placement:
        print(el,end="")
        count = count + 1
        if count == 1:
            print(" ",end="")
        elif count == 4:
            print(" ",end="")
        elif count == 8:
            print()

def write_placements_to_file(file_name):
    result = open(file_name, "w")
    def write_students_in_room(placement):
        count = 0
        for el in placement:
            result.writelines(el)
            count = count + 1
            if count == 1:
                result.writelines(" ")
            elif count == 4:
                result.writelines(" ")
            elif count == 8:
                result.writelines("\n")
    count_placments = 0
    for placement in posible_placements:
        count_placments = count_placments + 1
        write_students_in_room(placement)

def print_some_placements(N = 20):
    count = 0
    for el in posible_placements:
        count = count + 1
        print_students_in_rooms(el)
        if count == N:
            break



rooms,students = get_students_from_file("students.txt")
print("students: ",students)
set_placement(rooms,students,0)

print_some_placements()

write_placements_to_file("result.txt")
#write_placements_to_file("result.txt")


# print(posible_placements)
