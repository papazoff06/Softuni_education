# •	Име на актьора – текст
# •	Точки от академията - реално число в интервала [2.0... 450.5]
# •	Брой оценяващи n – цяло число в интервала[1… 20]
# На следващите n-на брой реда:
# o	Име на оценяващия – текст
# o	Точки от оценяващия – реално число в интервала [1.0... 50.0]
actors_name = input()
scores_from_academy = float(input())
count_of_judges = int(input())
actor_score = scores_from_academy
for i in range(count_of_judges):
    judge_name = input()
    judge_score = float(input())
    actor_score += (len(judge_name) * judge_score) / 2
    if actor_score > 1250.5:
        break
if actor_score > 1250.5:
    print(f"Congratulations, {actors_name} got a nominee for leading role with {actor_score:.1f}!")
else:
    print(f"Sorry, {actors_name} you need {1250.5 - actor_score:.1f} more!")