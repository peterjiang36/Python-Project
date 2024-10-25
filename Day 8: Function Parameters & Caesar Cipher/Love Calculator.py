def calculate_love_score(name1, name2):
    score1 = 0
    for letter in name1:
        if letter.upper() == "T":
            score1 += 1
        elif letter.upper() == "R":
            score1 += 1
        elif letter.upper() == "U":
            score1 += 1
        elif letter.upper() == "E":
            score1 += 1
    for letter in name2:
        if letter.upper() == "T":
            score1 += 1
        elif letter.upper() == "R":
            score1 += 1
        elif letter.upper() == "U":
            score1 += 1
        elif letter.upper() == "E":
            score1 += 1

    score2 = 0
    for letter in name1:
        if letter.upper() == "L":
            score2 += 1
        elif letter.upper() == "O":
            score2 += 1
        elif letter.upper() == "V":
            score2 += 1
        elif letter.upper() == "E":
            score2 += 1
    for letter in name2:
        if letter.upper() == "L":
            score2 += 1
        elif letter.upper() == "O":
            score2 += 1
        elif letter.upper() == "V":
            score2 += 1
        elif letter.upper() == "E":
            score2 += 1
    print(score1 * 10 + score2)


calculate_love_score("Kanye West", "Kim Kardashian")
