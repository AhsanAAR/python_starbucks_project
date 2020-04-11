memberList = []
customerList = []
managerList = []
starCardList = []
itemsList = []

class star_card:
    def __init__(self, cardNum, credit):
        self.m_cardNum = cardNum
        self.m_credit = credit

class shop_item:
    def __init__(self, itemName, price):
        self.m_itemName = itemName
        self.m_price = price

class web_user:
    def __init__(self, uName, password, fullName, address, telNum, email, starCard, accessList):
        self.m_uName = uName
        self.m_password = password
        self.m_fullName = fullName
        self.m_address = address
        self.m_telNum = telNum
        self.m_email = email
        self.m_starCard = starCard
        self.m_accessList = accessList

class member(web_user):
    def __init__(self, uName, password, fullName, address, telNum, email, starCard, depends, points):
        super(member, self).__init__(uName,password,fullName,address,telNum,email,starCard, [self])
        self.m_points = points
        self.depends = depends
        self.type = 'C'
        usersList.append(self)

class basic_empoyee(web_user):
    def __init__(self, uName, password, fullName, address, telNum, email, starCard, membersList):
        super(empoyee, self).__init__(uName, password, fullName, address, telNum, email, starCard, [self] + membersList)
        self.type = 'E'
        usersList.append(self)

class manager(basic_empoyee):
    def __init__(self, uName, password, fullName, address, telNum, email, starCard, webUserList):
        super(manager, self).__init__(self, uName, password, fullName, address, telNum, email, starCard, usersList)
        self.type = 'M'
        usersList.append(self)

def loadRecord():
