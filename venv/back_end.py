#this module stores all the functions and classes that handle the user's data and
#the backend processing of the applications


# lists to store all the different objects in our system
memberList = []
employeeList = []
managerList = []
starCardList = []
itemsList = []

import random

class star_card:
    'Class Represting Star Cards'

    def __init__(self, cardNum, credit):
        self.m_cardNum = str(cardNum)
        self.m_credit = int(credit)

    # constructor for making a new starCard with random Numbers
    def __init_(self):
        rand = 0
        found = True
        while found:
            rand = str(random.randrange(10000000, 99999999))
            found = False
            for test in starCardList:
                if rand == test.m_cardNum:
                    found = True
                    break
        self.m_cardNum = rand
        self.m_credit = 0

    # the __str__ function is defined for each class so that it returns a string format
    # that completely represents the object in text form. This function is then used to
    # write to the WebUser.txt file at the termination of application so the data can be loaded
    # later on

    def __str__(self):
        return '!'.join(map(str,[self.m_cardNum,self.m_credit]))

class shop_item:
    'Class respresnting shop iteams'
    def __init__(self, itemName, price):
        self.m_itemName = itemName
        self.m_price = int(price)

    def __str__(self):
        return '!'.join(map(str,[self.m_itemName,self.m_price]))

class web_user:
    'Class respresnting the abstract User on the system'
    def __init__(self, uName, password, fullName, address, telNum, email, starCardNum, accessList):
        self.m_uName = uName
        self.m_password = password
        self.m_fullName = fullName
        self.m_address = address
        self.m_telNum = telNum
        self.m_email = email
        self.m_accessList = accessList
        for test in starCardList:
            if starCardNum == test.m_cardNum:
                self.m_starCard = test
                break

    def __str__(self):
        return '!'.join(map(str, [self.m_uName, self.m_password, self.m_fullName,self.m_address,self.m_telNum
                                  ,self.m_email,self.m_starCard.m_cardNum]))

class member(web_user):
    'Class respresnting members or customers on the portal'
    def __init__(self, uName, password, fullName, address, telNum, email, starCardNum, depends, points):
        super(member, self).__init__(uName,password,fullName,address,telNum,email,starCardNum, [self])
        self.m_points = int(points)
        self.m_depends = depends
        self.m_type = 'C'

    def __str__(self):
        return self.m_type + '!' + super().__str__() + '!' + '!'.join(map(str,['Y' if self.m_depends else 'N',self.m_points]))

class basic_empoyee(web_user):
    'Class respresnting a basic employee'
    def __init__(self, uName, password, fullName, address, telNum, email, starCardNum):
        super(basic_empoyee, self).__init__(uName, password, fullName, address, telNum, email, starCardNum, [self] + memberList)
        self.m_type = 'E'

    def __str__(self):
        return self.m_type + '!' + super().__str__()


class manager(web_user):
    'Class respresnting a manager'
    def __init__(self, uName, password, fullName, address, telNum, email, starCardNum):
        super(manager, self).__init__(uName, password, fullName, address, telNum, email, starCardNum, (memberList + employeeList + managerList))
        self.m_type = 'M' + '!'

    def __str__(self):
        return self.m_type + '!' + super().__str__()

# function that converts WebUser.txt into object lists
def loadRecords():
    # opens the file in read mode
    with open("WebUser.txt","r") as f:
        # loop for loading starCards
        for line in f:
            line = line[:-1] # to ignore the \n
            if line == '#': #separates the different types of objects
                break
            line = line.split('!')
            starCardList.append(star_card(line[0],line[1]))
        # loop for loading all the users
        for line in f:
            line = line[:-1]
            if line == '#':
                break
            line = line.split('!')
            if line[0] == 'C':
                memberList.append(member(line[1],line[2],line[3],line[4],line[5],line[6],line[7],True if line[8] == 'Y' else False
                                         ,line[9]))
            elif line[0] == 'E':
                employeeList.append(basic_empoyee(line[1],line[2],line[3],line[4],line[5],line[6],line[7]))
            elif line[0] == 'M':
                managerList.append(manager(line[1],line[2],line[3],line[4],line[5],line[6],line[7]))
        # loop for loading shop items
        for line in f:
            line = line[:-1]
            line = line.split('!')
            itemsList.append(shop_item(line[0],line[1]))



