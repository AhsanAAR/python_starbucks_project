from back_end import *

loadRecords()

#jani ye loop un saray objects ko string mein convert ker kay usi format mein le ati hain.
#so ab jeb program end hoga hum ye sari file mein write ker dain gaye to exact objects ki states
#print ho jayein gi

#also text WebUser.txt k end pe aik khali line zeroor dalin

[print(item) for item in starCardList]
print('#')
[print(item) for item in memberList]
[print(item) for item in employeeList]
[print(item) for item in managerList]
print('#')
[print(item) for item in itemsList]






