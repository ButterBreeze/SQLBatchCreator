"""
    Programmer: ButterBreeze
    Program: Read in an sql file delimited by spaces
    Outputs: A sql batch file based on what the specified table is and the fields
"""

#import sys #for arguments passed

#print(sys.argv)

#will change to arguement when working but path to file

#lineArray = getEntries()









def getEntries():
    lines = ""
    asdf = 0
    with open("C:\\Users\\Tallennar\\Miscellanous\\Repos\\Python\\SqlBatchFileCreator\\team_stats.txt", "r") as inputFile:
        line = inputFile.readline()
    lineArray = line.split()
    print(lineArray)
    for i in lineArray:
        if i.isalpha():
            print(i)










