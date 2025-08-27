sum = 0
order = []
cup = []

while True:
    User_menu = int(input())
    if User_menu == 0:
        break
    order.append(User_menu)
    User_cup = int(input())
    cup.append(User_cup)

for i in range(len(order)):
    if order[i] == 1:
        sum += 25 * cup[i]
    elif order[i] == 2:
        sum += 30 * cup[i]
    elif order[i] == 3:
        sum += 35 * cup[i]
            
total_cup = 0         
for User_cup in cup:
    total_cup += User_cup

if sum >= 300:
    sum = sum - (sum*0.05)
elif total_cup >= 10:
    sum = sum - (sum*0.10)
            
print(round(sum))