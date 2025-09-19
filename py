weight = []
maxscore = [50,40,60]
stdscore = [45,30,50]

def weight_score(weight,maxscore,stdscore):
    count = len(maxscore)
    if not weight:
        weight =[100/count]*count
    finalscore = 0
    for w,m,s in zip(weight,maxscore,stdscore):
        finalscore += (s/m)*w
    return round(finalscore,2)
        
print("Final weighted score is",weight_score(weight,maxscore,stdscore))
