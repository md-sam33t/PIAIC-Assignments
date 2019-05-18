#!/usr/bin/env python
# coding: utf-8

# In[11]:


english = input('Enter marks for English: ')
urdu    = input('Enter marks for Urdu: ')
math    = input('Enter marks for Math: ')
chem    = input('Enter marks for Chemistry: ')
physics = input('Enter marks for Physics: ',)

total = int(english) + int(urdu) + int(math) + int(chem) + int(physics)
perc  = (float(total) / 500) * 100

if perc >= 40 and perc <=49:
    grad = 'Pass'
elif perc >= 50 and perc <=59:
    grad = 'C'
elif perc >= 60 and perc <=69:
    grad = 'B'
elif perc >= 70 and perc <=80:
    grad = 'A'
elif perc >= 81:
    grad = 'A+'    
else:
    grad = 'Fail'

print('')
print('********MarkSheet***********','\n')
print('English: ',english)
print('Urdu: ',urdu)
print('Math: ',math)
print('Chemistry: ',chem)
print('Physics: ',physics)
print('----------------------','\n')
print('Results :-')
print('Obtained Marks : ',total)
print('Your percentage is : %.2f ' %perc)    
print('Your Grad is : ',grad,'\n')

if grad != 'Fail':
    print('Congratulations you did it!')
else:
    print('Sorry, but seems like you are not going to advance')


# In[ ]:





# In[3]:





# In[ ]:





# In[ ]:




