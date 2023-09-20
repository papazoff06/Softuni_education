count_of_visitors = int(input())
back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0
training_people = 0

for i in range(count_of_visitors):
    training = input()
    if training == 'Back':
        back += 1
        training_people += 1
    elif training == 'Chest':
        chest += 1
        training_people += 1
    elif training == 'Legs':
        legs += 1
        training_people += 1
    elif training == 'Abs':
        abs += 1
        training_people += 1
    elif training == 'Protein shake':
        protein_shake += 1
    elif training == 'Protein bar':
        protein_bar += 1
percentage_training_people = training_people / count_of_visitors * 100
percentage_people_bought_protein = (protein_shake + protein_bar) / count_of_visitors * 100
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{percentage_training_people:.2f}% - work out")
print(f"{percentage_people_bought_protein:.2f}% - protein")



