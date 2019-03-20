'''
Created on 20190319
@author: csjdli
'''

#BigARM Project
#Implement a timer for the purpose of running carousel allocation algorithm or function in a regular time (00:01:00 am) 
#reference: https://blog.csdn.net/weixin_39461443/article/details/75537240
import time
import sched
import datetime

schedule = sched.scheduler(time.time, time.sleep)

start_time = 0
end_time = 0
class Timer(object):
    # 被周期性调度触发的函数
    def execute_command(self, inc):
        start_time = datetime.datetime.now()
        dt = datetime.datetime.now()
        print ("jiandong hello" + str(dt)) # test, print date
        time.sleep(3)
        end_time = datetime.datetime.now()
        delay = round((end_time-start_time).total_seconds())
        
        #dt_jd = datetime.datetime(dt.year,dt.month,dt.day)
        
        print (u'mytimer => 开始时间：%s' % start_time)
        print (u'mytimer => 耗时:%smin' %(delay/60))
        schedule.enter(int(inc-delay), 0, self.execute_command, (inc, ))
        print (u'mytimer => 结束时间：%s' % end_time)
        
        print (u'mytimer => 还有%s秒开始任务' %inc)
        

    def cmd_timer(self, time_str, inc=60):
        # time_str：哪一个时间点开始第一次执行
        # inc：两次执行的间隔时间
        # enter四个参数分别为：间隔时间、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，
        # 给该触发函数的参数（tuple形式）
        now = datetime.datetime.now()
        schedule_time = datetime.datetime.strptime(time_str,'%H:%M').replace(year=now.year,month=now.month,day=now.day)
        if schedule_time < now:
            schedule_time = schedule_time + datetime.timedelta(days=1)
        time_before_start = int(round((schedule_time-datetime.datetime.now()).total_seconds()))
        print (u'mytimer => 还有%s秒开始任务' %time_before_start)
        schedule.enter(time_before_start, 0, self.execute_command, argument=(inc, ))
        schedule.run()

if __name__ == '__main__':
    timer = Timer()
    # 每天的00:01执行行李传送算法， 间隔为一天，即86400秒
    timer.cmd_timer('00:01', 86400)

     