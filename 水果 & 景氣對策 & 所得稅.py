#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

fruits = ['Apple', 'Orange', 'Banana', 'pear', 'Tomato']
cf = random.choice(fruits)

print("Today's fruit is : " + cf)


# In[2]:


score = int(input('請輸入景氣對策信號綜合分數'))
if score >= 45 or score< 9 :
    print('錯誤')
elif score >= 37:
    print('紅燈')
elif score >=31:
    print('黃紅燈')
elif score >= 22:
    print('綠燈')
elif score >=16:
    print('黃藍燈')
elif score >=9:
    print('藍燈')


# In[2]:


level1=520000*0.05
level2=(1170000-520000)*0.12
level3=(2350000-1170000)*0.2
level4=(4400000-2350000)*0.3
level5=(10000000-4400000)*0.4
income=int(input('請輸入淨年所得額: '))

if income <= 520000:
    tax=income*0.05

elif income <= 1170000:
    tax=level1+((income-520000)*0.12)

elif income <= 2350000:
    tax=level1+level2+((income-1170000)*0.2)

elif income <=4400000:
    tax=level1+level2+level3+((income-2350000)*0.3)

elif income <=10000000:
    tax=level1+level2+level3+level4+((income-4400000)*0.4)
    
else:
    tax=level1+level2+level3+level4+level5+((income-10000000)*0.45)

print('應繳稅額=', tax)


# In[ ]:




