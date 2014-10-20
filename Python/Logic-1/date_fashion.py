def date_fashion(you, date):
    if (you < 3 or date < 3):
        return 0
    elif (you < 8 and date < 8):
        return 1
    else:
        return 2