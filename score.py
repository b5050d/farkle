def calculate_score(values):
    score = 0
    # if len(values) == 6:
    
    # elif len(values) == 

    # Count the amount of values per dice value:
    d = {}
    for i in range(1,7):
        d[i] = 0

    for val in values:
        d[val] += 1
    
    # TODO - Check for the big scoring items
    dlist = []
    for key in d:
        dlist.append(d[key])


    if 0 not in dlist:
        return 2000
    
    elif 0 not in dlist[1:]:
        score+=1500
        if d[1] == 1:
            score += 100
        elif d[5] == 2:
            score+= 50
        return score
    elif 0 not in dlist[:-1]:
        score+=1500
        if d[1] == 2:
            score += 100
        elif d[5] == 2:
            score += 50
        return score
    else:
        # TODO - Check for 6's 5's quads or triples

        # Check the ones
        if d[1] < 3:
            score+=100*d[1]
        
        if d[5] < 3:
            score+=50*d[5]
        
        print(values)
        print(score)
        return score
