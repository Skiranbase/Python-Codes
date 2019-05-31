#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# TCS Inverview Questions


# In[53]:


#Petrol Or Diesel
Petrol_1 = int(input())
Petrol_2 = int(input())
Petrol_3 = int(input())
Petrol_4 = int(input())
Petrol_5 = int(input())
Petrol_6 = int(input())
Diesel_1 = int(input())
Diesel_2 = int(input())
Diesel_3 = int(input())
Diesel_4 = int(input())
Diesel_5 = int(input())
Diesel_6 = int(input())
def petrol_or_diesel(Petrol_1,Petrol_2,Petrol_3,Petrol_4,Petrol_5,Petrol_6,Diesel_1,Diesel_2,Diesel_3,Diesel_4,Diesel_5,Diesel_6):
    petrol = 0
    diesel = 0
    if Petrol_1 == Diesel_1:
        diesel = diesel + 1
    elif Petrol_1 > Diesel_1:
        diesel = diesel + 1
    else:
        petrol = petrol + 1
    if Petrol_2 == Diesel_2:
        diesel = diesel + 1
    elif Petrol_2 > Diesel_2:
        diesel = diesel + 1
    else:
        petrol = petrol + 1
    if Petrol_3 == Diesel_3:
        diesel = diesel + 1
    elif Petrol_3 > Diesel_3:
        diesel = diesel + 1
    else:
        petrol = petrol + 1
    if Petrol_4 == Diesel_4:
        diesel = diesel + 1
    elif Petrol_4 > Diesel_4:
        diesel = diesel + 1
    else:
        petrol = petrol + 1
    if Petrol_5 == Diesel_5:
        diesel = diesel + 1
    elif Petrol_5 > Diesel_5:
        diesel = diesel + 1
    else:
        petrol = petrol + 1
    if petrol == diesel:
        return 'diesel'
    elif petrol > diesel:
        return 'petrol'
    else:
        return 'diesel'
output = petrol_or_diesel(Petrol_1,Petrol_2,Petrol_3,Petrol_4,Petrol_5,Petrol_6,Diesel_1,Diesel_2,Diesel_3,Diesel_4,Diesel_5,Diesel_6)
print('Output')
print(output)


# In[55]:


#In a Tree identifying worst possible number of pair and best possible number of pair.
x = int(input('Enter Number of now in a Tree'))
list1 = []
a = 1
m = 0
list1.append(a)
while x > m:
    a = a + a
    m = a
    list1.append(a)
worst = sum(list1[0:-3])
print('Worst posible number of pair: ',worst)
best = sum(list1[0:-2])
diff = x-best
y = 0
if diff/2 == 0:
    y = diff/2
else:
    y = int(diff/2-0.)
print('Best possible number of pair: ',worst+y)

