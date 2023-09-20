country = input()
device  = input()
difficulty = 0
performance = 0
if device == 'ribbon':
    if country == 'Russia':
        difficulty += 9.100
        performance += 9.400
    elif country == 'Bulgaria':
        difficulty += 9.600
        performance += 9.400
    elif country == 'Italy':
        difficulty += 9.200
        performance += 9.500
elif device == 'hoop':
    if country == 'Russia':
        difficulty += 9.300
        performance += 9.800
    elif country == 'Bulgaria':
        difficulty += 9.550
        performance += 9.750
    elif country == 'Italy':
        difficulty += 9.450
        performance += 9.350
elif device == 'rope':
    if country == 'Russia':
        difficulty += 9.600
        performance += 9.00
    elif country == 'Bulgaria':
        difficulty += 9.500
        performance += 9.400
    elif country == 'Italy':
        difficulty += 9.700
        performance += 9.150
final_score = difficulty + performance
percentage = (20 - final_score) / 20 * 100
print(f"The team of {country} get {final_score:.3f} on {device}.")
print(f"{percentage:.2f}%")