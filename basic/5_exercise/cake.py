cake_width = int(input())
cake_length = int(input())

cake_peaces_total = cake_width * cake_length
cake_peaces_left = cake_peaces_total

command = input()

while command != "Stop":
    current_peaces = int(command)
    cake_peaces_left -= current_peaces
    if cake_peaces_left <= 0:
        print(f"No more cake left! You need {-cake_peaces_left} pieces more.")



if command == "Stop":

    if cake_peaces_left > 0:
        print(f"{cake_peaces_left} pieces are left." )
command = input()











