number_of_rooms = int(input())
my_list = []
room = 1
left_chairs = 0
for i in range(number_of_rooms):
    current_people_and_chairs = input().split()
    my_list.append(current_people_and_chairs)
for chairs_people in my_list[1:len(my_list) + 1]:
    chairs = len(chairs_people[0])
    people = int(chairs_people[1])
    difference = chairs - people
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {room}")
        room += 1
        left_chairs = 0
    else:
        room += 1
        left_chairs += difference
if left_chairs > 0:
    print(f"Game On, {left_chairs} free chairs left")






