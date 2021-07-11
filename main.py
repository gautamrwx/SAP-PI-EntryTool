import underscoreToCamelCase
import removeEmptyLines
import xsdBuildHelper
import countIndentedTabs


def run(nameSpaceString,dataTypeName,inputPlainText):

    '''
    Remove empty lines from this Text File
    '''
    newText = removeEmptyLines.performAction(inputPlainText)

    '''
    Convert all text into Camel Case
    '''
    textWithCamelCase = underscoreToCamelCase.convert(newText)

    '''
    Count Tabs in begining of all lines for XML structuring
    '''
    indentedTabsEachLine = countIndentedTabs.getList(textWithCamelCase)

    '''
    Create XML with help of tabs count and new camelCase Converted Text
    '''

    # Step - 1 > Start XML Wrapper
    xsdOutputString = xsdBuildHelper.startWarpperElement(
        nameSpaceString, dataTypeName)

    # Step - 2 > Create Inner XML
    splittedLines = textWithCamelCase.split("\n")

    i = 0
    # Append A last count value of same to carry loop upto i+1
    indentedTabsEachLine.append(indentedTabsEachLine[-1])

    for line in splittedLines:
        currLineIndentedTabs = indentedTabsEachLine[i]
        nextLineIndentedTabs = indentedTabsEachLine[i+1]

        # Remove tabs and special chars
        stringwithoutTabs = ''.join(e for e in line.strip() if e.isalnum())

        if(nextLineIndentedTabs == currLineIndentedTabs):
            xsdOutputString += xsdBuildHelper.createStringElement(
                stringwithoutTabs)

        elif(nextLineIndentedTabs > currLineIndentedTabs):
            xsdOutputString += xsdBuildHelper.startComplexElement(
                stringwithoutTabs)

        else:
            xsdOutputString += xsdBuildHelper.createStringElement(
                stringwithoutTabs)
            xsdOutputString += xsdBuildHelper.endComplexElement()

        i += 1

    # Check if Last Complex Element Closed Properly Or Not
    for i in range(currLineIndentedTabs):
        print(i)
        xsdOutputString += xsdBuildHelper.endComplexElement()

    # Step - 3 > End XML Warapper
    xsdOutputString += xsdBuildHelper.endWarpperElement()

    '''
    Create XSD with help of tabs count and new camelCase Converted Text
    '''
    newFile = 'Output.xsd'  # Define New Filename
    filew = open(newFile, "w")  # write mode
    filew.write(xsdOutputString)
    filew.close()
