# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:37:31 2019

@author: vicvo

176. Second Highest Salary
https://leetcode.com/problems/second-highest-salary/
"""


import pandas as pd
import numpy as np




#Employee=pd.DataFrame({'ID':[1,2],
#        'Salary':[100,100]})
#
# 
#def second_value(column):
#    col=list(set(column))
#    if len(col)<2:
#        return np.nan
#    new_column = sorted(col, reverse=False)
#    return new_column[1]
#
#print('工资第二高的是： ', second_value(Employee.Salary))



'''
181. Employees Earning More Than Their Managers
https://leetcode.com/problems/employees-earning-more-than-their-managers/
'''

#Employee=pd.DataFrame({
#        'Id':[1,2,3,4],
#        'Name':['Joe','Henry','Sam','Max'],
#        'Salary':[70000,80000,60000,90000],
#        'ManagerId':[3,4,np.nan,np.nan]
#        })
#
#
#Employee2=Employee
#
#table=pd.merge(Employee,Employee2,left_on='ManagerId',right_on='Id',how='outer')
#
#print('员工比经理工资高的是：',table[table.Salary_x>table.Salary_y].values[0,1])
#

'''
182. Duplicate Emails
https://leetcode.com/problems/duplicate-emails/
'''

#
#Person=pd.DataFrame({
#        'Id':[1,2,3],
#        'Email':['a@b.com','c@b.com','a@b.com']
#        })
#
#count_P=Person.groupby('Email')['Email'].count()
#
#print('重复的邮箱是',count_P[count_P>1].index.values[0])

'''
183. Customers Who Never Order
https://leetcode.com/problems/customers-who-never-order/
'''
#Customers=pd.DataFrame({
#        'Id':[1,2,3,4],
#        'Name':['Joe','Henry','Sam','Max']
#        })
#
#Orders=pd.DataFrame({
#        'Id':[1,2],
#        'CustomersId':[3,1]
#        })




'''
197. Rising Temperature
https://leetcode.com/problems/rising-temperature/
'''

#Weather=pd.DataFrame({
#        'Id':[1,2,3,4],
#        'RecordDate':['2015-01-01','2015-01-02','2015-01-03','2015-01-04'],
#        'Temperatur':[10,25,20,30]
#            
#        })
#Weather['RecordDate']=pd.to_datetime(Weather['RecordDate'],format='%Y-%m-%d')
#
#w=Weather.shift(axis=0)
#
#table=Weather.join(w, on=None, how='left', lsuffix='_l', rsuffix='_r', sort=False)
#print('温度比昨天高的是：',table[table.Temperatur_l>table.Temperatur_r].RecordDate_l.values)
##怎么把今天的日期和昨天的日期merge一起



'''
596. Classes More Than 5 Students
https://leetcode.com/problems/classes-more-than-5-students/
'''
#courses=pd.DataFrame({
#        'stu':[1,2,3,4,5,6,7,8,9],
#        'class':['M','E','M','B','M','C','M','M','M']
#        })
#table=courses.groupby('class')['stu'].size()
#
#print('人数超过3的课是：',table[table>=3].index.values)
#







'''
627. Swap Salary
https://leetcode.com/problems/swap-salary/
'''
#salary=pd.DataFrame({
#        'Id':[1,2,3,4],
#        'Name':['Joe','Henry','Sam','Max'],
#        'sex':['f','m','f','m'],
#        'salary':[10,25,20,30]
#        })
#
#
#salary['sex']=salary['sex'].map(lambda x: 'f' if x=='m' else 'm')

'''
1179. Reformat Department Table
https://leetcode.com/problems/reformat-department-table/
'''

#Department=pd.DataFrame({
#        'id':[1,2,3,1,1],
#        'revenue':[8000,9000,10000,7000,6000],
#        'month':['Jan','Jan','Feb','Feb','Mar']
#        })
#
#D=Department.groupby(['id','month'])['revenue'].max()
#D=D.reset_index()
#
#
#Jan_Revenue=[ D[(D.id==i) & (D.month=='Jan')].revenue.values if 
#                D[(D.id==i) & (D.month=='Jan')].month.values in 
#                D[D.id==i].month.values 
#                else np.nan for i in set(D.id)]
#
#Feb_Revenue=[ D[(D.id==i) & (D.month=='Feb')].revenue.values if 
#                D[(D.id==i) & (D.month=='Feb')].month.values in 
#                D[D.id==i].month.values 
#                else np.nan for i in set(D.id)]
#Mar_Revenue=[ D[(D.id==i) & (D.month=='Mar')].revenue.values if 
#                D[(D.id==i) & (D.month=='Mar')].month.values in 
#                D[D.id==i].month.values 
#                else np.nan for i in set(D.id)]
#
#new=pd.DataFrame({
#        'id':[1,2,3],
#        'Jan_Revenue':Jan_Revenue,
#        'Feb_Revenue':Feb_Revenue,
#        'Mar_Revenue':Mar_Revenue
#        })



#MEDIUM
'''
177. Nth Highest Salary
https://leetcode.com/problems/nth-highest-salary/
'''
e=pd.DataFrame({
        'id':[1,2,3],
        'salary':[100,200,300]
        })


e.sort_values('salary',inplace=True,ascending=False)

print('工资第二高的是：',e.iloc[1,:].salary)




