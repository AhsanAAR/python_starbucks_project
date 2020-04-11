usersList = []

class star_card:
    def __init__(self, cardNum, credit):
        self.m_cardNum = cardNum
        self.m_credit = credit

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
    def __init__(self, uName, password, fullName, address, telNum, email, starCard, points):
        super(member, self).__init__(uName,password,fullName,address,telNum,email,starCard, [self])
        self.m_points = points
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

def loadRecord
