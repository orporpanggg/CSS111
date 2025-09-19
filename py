
def weight_score(weight, maxscore, stdscore):
    count = len(maxscore)
    finalscore = 0
    if not weight:
        new_weight = 100/count
        for i in range(count):
            finalscore += (stdscore[i] / maxscore[i]) * new_weight
    else:
        for i in range(count):
            finalscore += (stdscore[i] / maxscore[i]) * weight[i]
    return round(finalscore, 2)

weight = [30,30,40]
maxscore = [50, 40, 60]
stdscore = [45, 30, 50]
print("Final weighted score is", weight_score(weight, maxscore, stdscore))

weight = []
maxscore = [50, 40, 80]
stdscore = [45, 30, 50]
print("Final weighted score is", weight_score(weight, maxscore, stdscore))

weight = [10,20,30,40]
maxscore = [50, 40, 80,80]
stdscore = [45, 30, 50,40]
print("Final weighted score is", weight_score(weight, maxscore, stdscore))
