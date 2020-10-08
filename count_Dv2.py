#!/usr/bin/env python
# coding: utf-8

# In[5]:


#kindly cheak doc ''' print (__doc__)''' if confused
import datetime# in-built libary
from pyinputplus import inputDate,inputDatetime,inputStr #external libary (kindly import)
another ='yes'
def main():
    global another 
    """ 
    title : creating a countdown with python 
    
    ################################
    the external module used is pyinputplus if not found
    kindly import it
    -- pip install pyinputplus-- 
    and rerun the program
    
    
    ========================================================
    Description :
    this is a simple programme that allows the user to know how many days 
    left from the present day to the specifyed day 
    all you need to do is to input your special day 
    eg birthday the the date it then output the precise date 
    
    this is useful for students ,women,men,civil woorkers and so on
    
    ========================================================
    ---------------------
    created by Joshua.A.Timi(JatNet™) aka CYBERPRIEST🐉
    ----------------------
    """
    while another == 'yes' or another =='Y' or another == 'y' or another == 'Yes':
        my_special_D = get_special_day()
        my_dates = get_date()# i created a func that prompt user date 
        eval_date =get_date_eval(my_dates)
        print ("    -------------------------------------------")
        print(f" >>>> {eval_date.days} Days left till {my_special_D}")
        print ("    -------------------------------------------")
        
        print ()
        
        print ("    -------------------------------------------")
        print(f" >>>> total seconds left is  {eval_date.total_seconds()} sec  till {my_special_D}")
        print ("    -------------------------------------------")
        print ()
        another  = inputStr(prompt = " do you wanna continue enter(yes/y) enter (no/n) to quit " )
def get_date():
    input_date = inputDate(prompt = " Input sepecifyed Date  (eg : 2019/10/31) ",limit = 3,timeout = None,blockRegexes = None, allowRegexes=None,blank =False,default = " Timeout ")
    return input_date
def get_date_eval(dates):
    tday = datetime.date.today()
    eval_sol = tday - dates 
    return abs(eval_sol)# print (type(eval_sol)) cheak_type = timedelta
def get_special_day():
    print(" input your special day   (eg : christmas) : ".center(30,'*'))
    print()
    special_day = inputStr("")
    return special_day.upper()
    
    
        
main()


# In[ ]:




