"""
Written by b5050d
3.20.2025

Scoring utility
"""


def remove_from_dict(d, to_remove):
    """
    Replaces All occurrences of a value in a dictionary with 0
    """
    for key, value in d.items():
        if value == to_remove:
            d[key] = 0
    return d


def calculate_score(values):
    """
    Calculate the score from a roll
    """
    score = 0

    # Count the amount of values per dice value:
    d = {}
    for i in range(1, 7):
        d[i] = 0

    for val in values:
        d[val] += 1

    #  Check for the big scoring items
    dlist = []
    for key in d:
        dlist.append(d[key])

    if 0 not in dlist:
        return 1500

    elif 0 not in dlist[1:]:
        score += 1500
        if d[1] == 1:
            score += 100
        elif d[5] == 2:
            score += 50
        return score
    elif 0 not in dlist[:-1]:
        score += 1500
        if d[1] == 2:
            score += 100
        elif d[5] == 2:
            score += 50
        return score
    else:
        if dlist.count(3) == 2:
            return 2500

        if dlist.count(2) == 3:
            return 1500

        # TODO - Check for 6's 5's quads or triples
        if 6 in dlist:
            return 3000

        if 5 in dlist:
            score += 2000
            # remove from the dlist and the d
            dlist = [0 if i == 5 else i for i in dlist]
            d = remove_from_dict(d, 5)

        if 4 in dlist:
            score += 1000
            dlist = [0 if i == 4 else i for i in dlist]
            d = remove_from_dict(d, 4)

        if 3 in dlist:
            # check where the 3 is
            triple_value = dlist.index(3) + 1

            if triple_value == 1:
                score += 1000
            else:
                score += triple_value * 100

            dlist = [0 if i == 3 else i for i in dlist]
            d = remove_from_dict(d, 3)

        # Check the ones
        if d[1] < 3:
            score += 100 * d[1]

        if d[5] < 3:
            score += 50 * d[5]

        print(values)
        print(score)
        return score
