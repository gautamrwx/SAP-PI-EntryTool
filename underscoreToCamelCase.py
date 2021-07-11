def convert(inpString):
    newString = ''
    underScoreFlag = False

    for currChar in inpString:
        # remember the underscore character if found
        if currChar == '_':
            underScoreFlag = True
            continue

        # If previous char is underscore than current char will uppercase
        if underScoreFlag:
            newString += currChar.upper()
            underScoreFlag = False
            continue

        newString += currChar

    return newString
