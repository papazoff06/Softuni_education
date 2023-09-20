win_scores = 1250.5
actors_name = input()
scores_from_academy = float(input())
count_of_judges = int(input())
sum_of_scores = scores_from_academy

# •	Име на актьора - текст
# •	Точки от академията - реално число в интервала [2.0... 450.5]
# •	Брой оценяващи n - цяло число в интервала[1… 20]
for _ in range(count_of_judges):
    judge_name = input()
    scores_from_judge = float(input())
    sum_of_scores += len(judge_name) * scores_from_judge / 2

    if sum_of_scores > win_scores:
        print(f"Congratulations, {actors_name} got a nominee for leading role with {sum_of_scores:.1f}!")
        break
else:
    print(f"Sorry, {actors_name} you need {win_scores - sum_of_scores:.1f} more!")