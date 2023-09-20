purchase_doc_food = int(input())
purchase_doc_food_in_grams = purchase_doc_food * 1000

eaten_food = 0

command = input()
while command != 'Adopted':
    given_food = int(command)
    eaten_food += given_food


    command = input()
if eaten_food <= purchase_doc_food_in_grams:
    print(f"Food is enough! Leftovers: {purchase_doc_food_in_grams - eaten_food} grams.")
elif eaten_food > purchase_doc_food_in_grams:
    print(f"Food is not enough. You need {abs(eaten_food - purchase_doc_food_in_grams)} grams more." )
