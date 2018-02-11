"""
    Programmer: ButterBreeze
    Program: Read in an sql file delimited by spaces
    Outputs: A sql batch file based on what the specified table is and the fields
    the first line of the file should be

    tablename(field1 int, field2 string, field3 date, etc) (int, string, date) delimiter
    it will assume that all the fields are in the right order so food,is,good field1 = food , field2 = is, field3 = good


    Ex: cars(id int, make VARCHAR(20), model VARCHAR(30), year int) del= ','
fileEx: 12345,ford,f150,2012
        54321,tesla,model x,2017
output: Create Table cars(id int, make VARCHAR(30), model VARCHAR(30), year INT)
        INSERT INTO cars(id, make, model, year)
        Values(12345, 'ford', 'f150' 2012)
        INSERT INTO cars(id, make, model, year)
        Values(54321, 'tesla', 'modelx' 2017)

    TODO: Clean up the code and make it take arguments for whether it wants to create a table or simply input and where the file is
"""

# import sys #for arguments passed

# print(sys.argv)

# will change to argument when working but path to file

inputArray = [line.rstrip('\n') for line in open("page_visits.txt")]
lines = []

lineKey = inputArray[0]
outputFile = open('batchFile.sql', 'a')

index = 0
word = ""
tableName = ""
fields = []
types = []

for index in range(0, len(lineKey)):
    if lineKey[index] == '(':
        tableName = word
        break
    else:
        word += lineKey[index]

comma = True
sym = ""
word = ""
nextChar = ""
while sym != ")" or nextChar == ',':

    if sym.isalpha():
        word += sym
        comma = False
    elif sym == " " and not comma:
        fields.append(word)
        word = ""
    elif sym == ",":
        comma = True
        types.append(word)
        word = ""
    else:
        word += sym

    index += 1
    sym = lineKey[index]
    nextChar = lineKey[index + 1]
types.append(word)  # the loop ends and doesn't write the last type

index += 1
delimiterString = lineKey[index: len(lineKey) + 1]

firstDelimeterIndex = delimiterString.index("'")
lastDelimterIndex = delimiterString.rindex("'")

delimiter = delimiterString[firstDelimeterIndex + 1:lastDelimterIndex]

for line in inputArray[1:]:
    lines.append(line.split(delimiter))

lineKey = lines[0]

# going to now create a table
outputFile.write("Create Table " + tableName + " (")
for x in range(0, len(fields), +1):
    outputFile.write(fields[x] + " " + types[x])
    if not x == len(fields) - 1:
        outputFile.write(", ")
outputFile.write(");\n")

# insert into loop
for x in range(0, len(lines), +1):
    line = lines[x]
    outputFile.write("INSERT INTO " + tableName + " ( ")
    for y in range(0, len(fields), +1):
        outputFile.write(fields[y])
        if not y == len(fields) - 1:
            outputFile.write(", ")

    outputFile.write(") \n VALUES(")
    for y in range(0, len(fields), +1):

        if ("char" or "blob" or "text") in (''.join(types[y])).lower():
            outputFile.write("\'" + line[y] + "\'")
        else:
            outputFile.write(line[y])
        if not y == len(fields) - 1:
            outputFile.write(", ")

    outputFile.write("); \n")
