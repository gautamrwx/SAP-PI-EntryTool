from tkinter import *
import main

root = Tk()

def createXSD():
    nameSpace = nameSpaceVal.get()
    dataType = dataTypeVal.get()
    xmlField = xmlInputText.get(1.0,END)

    main.run(nameSpace,dataType,xmlField)


root.geometry("350x350")

# Heading
Label(root, text="Welcome to XSD Genrator",
      font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

# Text for our form
nameSpaceL = Label(root, text="NameSpace")
dataTypeL = Label(root, text="Data Type")
xmlFieldsL = Label(root, text="Plain Text for XSD")

# Pack text for our form
nameSpaceL.grid(row=1, column=2)
dataTypeL.grid(row=2, column=2)
xmlFieldsL.grid(row=3, column=2)

# Tkinter variable for storing entries
nameSpaceVal = StringVar()
dataTypeVal = StringVar()

# Entries for our form
nameSpaceEntry = Entry(root, textvariable=nameSpaceVal)
dataTypeEntry = Entry(root, textvariable=dataTypeVal)
xmlInputText = Text(root, height=10, width=20)


# Packing the Entries
nameSpaceEntry.grid(row=1, column=3)
dataTypeEntry.grid(row=2, column=3)
xmlInputText.grid(row=3, column=3)


# Button & packing it and assigning it a command
Button(text="Create XSD", command=createXSD).grid(row=10, column=3)

root.mainloop()
