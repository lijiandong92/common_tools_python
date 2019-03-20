'''
Created on 20190319
@author: csjdli
'''

#BigARM Project
#Get all days(datetime type) in a period of time (from start_date to end_date)

from datetime import datetime

def main():    
    begin = datetime(2019,2,23)    
    end = datetime(2019,3,19)    
    for i in range((end - begin).days+1):        
        day = begin + timedelta(days=i)  
        begin_time=datetime.now()
        print (str(day))
        df_initial_plan = generate_initial_plan(day, plot_result=False, save_result_plot=False, save_csv=True)
        print(datetime.now()-begin_time)
        print ("-------------------------------")

main()
     