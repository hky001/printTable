# def printPicnic(itemsDict,leftWidth,rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth+rightWidth,'-'))
#     for k,v in itemsDict.items():
#         print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))
# picnicItems = {'sandwicher' : 4, 'apples' : 12,'cups' : 4,'cookies': 8000}
# printPicnic(picnicItems,12,5)
# printPicnic(picnicItems,20,6)
tableData = [
    ['apples','oranges','cherries','banana'],
    ['Alice','Bob','Carol','David'],
    ['dogs','cats','moose','goose']
]
def printTable(list):
    colWidths = [0]*len(list)
    print(colWidths)
    print(len(list))
    print(len(list[0][0]))
    for i in range(len(list)):
        for j in range(len(list[i])):
            if colWidths[i]<len(list[i][j]):
                colWidths[i]= len(list[i][j])#找到每列最大的长度
    print(colWidths)
    for i in range(len(list[0])):
        for j in range(len(list)):
            print(list[j][i].rjust(colWidths[j]),end=' ')#打印字符串
        print(end='\n')
printTable(tableData)