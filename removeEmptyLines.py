def performAction(inputSting):

    splittedLines = inputSting.split("\n")

    linesWithoutEmptyLine = [
        line for line in splittedLines if line.strip() != ""]

    # Create a fresh sting without any lines
    stringWithoutEmptyLines = ""

    for line in linesWithoutEmptyLine:
        stringWithoutEmptyLines += line + "\n"

    # Remove and Return Unnecessary newline from end of string
    if stringWithoutEmptyLines[-1] == '\n':
        return stringWithoutEmptyLines[:-1]

    return stringWithoutEmptyLines
