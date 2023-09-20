# 1.	Рекордът в секунди – реално число;
# 2.	Разстоянието в метри – реално число;
# 3.	Времето в секунди, за което плува разстояние от 1 м. - реално число.
champions_record = float(input())
distance_in_meters = float(input())
time_in_seconds = float(input())
# На конзолата се въвежда рекордът в секунди, който Иван трябва да подобри,  разстоянието в метри,
# което трябва да преплува и времето в секунди, за което плува разстояние от 1 м. Да се напише програма,
# която изчислява дали се е справил със задачата, като се има предвид, че:
# съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди. Когато се изчислява колко пъти Иван ще се забави,
# в резултат на съпротивлението на водата, резултатът трябва да се закръгли надолу до най-близкото цяло число.
# Да се изчисли времето в секунди, за което Иван ще преплува разстоянието и разликата спрямо Световния рекорд.
time = distance_in_meters * time_in_seconds
extra_time_pur_15_meters = (distance_in_meters // 15) * 12.5
ivan_time = time + extra_time_pur_15_meters
if champions_record > ivan_time:
    print(f" Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {ivan_time - champions_record:.2f} seconds slower.")



