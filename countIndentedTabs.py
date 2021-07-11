def getList(inputString):

    indentedTabsEachLine = []

    splittedLines = inputString.split("\n")

    for line in splittedLines:
        # Remove all spaces from selected line
        stringwithoutTabs = line.strip()
        # LOGIC : tabs at beginning = substring index
        tabsAtBeginnning = line.index(stringwithoutTabs)

        indentedTabsEachLine.append(tabsAtBeginnning)

    return indentedTabsEachLine
