import back_end

back_end.loadRecords()
for listItem in back_end.starCardList:
    print('!'.join([str(elem) for elem in listItem.__dict__.values()]))
print('#')
for listItem in back_end.customerList:
    print('!'.join([str(elem) for elem in listItem.__dict__.values()]))
for listItem in back_end.employeeList:
    print('!'.join([str(elem) for elem in listItem.__dict__.values()]))
for listItem in back_end.managerList:
    print('!'.join([str(elem) for elem in listItem.__dict__.values()]))
print('#')
for listItem in back_end.itemsList:
    print('!'.join([str(elem) for elem in listItem.__dict__.values()]))

