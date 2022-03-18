#! /usr/bin/python3

#tp - Table Printer

def printTable(tableData):
    width = []

    for i in range(len(tableData)):
        maxWidth = 0

        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > maxWidth:
                maxWidth = len(tableData[i][j])

        width.append(maxWidth)

    for j in range(len(tableData[0])):
        for i in range(len(tableData)):
            print(tableData[i][j].rjust(width[i]), end=' ')

        print('\n')


tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

#Assume that all the inner lists will contain the same number of strings.