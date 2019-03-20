# -*- coding: utf-8 -*-
'''
Created on 20190320
@author: csjdli
'''

#BigARM Project
#Upload all windows files or a specific file in a dir to Linux server automatically by Python 
#reference: https://blog.csdn.net/weixin_40539892/article/details/79097386
import paramiko   #pip install paramiko
import datetime    
import os  

hostname= "Linux_hostName" 
username= "account_userName"
password= "account_pwd"  
port= 22 # integer

def upload(local_dir,remote_dir, file_name):  
    try:  
        t=paramiko.Transport((hostname,port))  
        t.connect(username=username,password=password)  
        sftp=paramiko.SFTPClient.from_transport(t)  
        print('upload file start %s ' % datetime.datetime.now()) 
        fileFlag = 0  # 
        for root,dirs,files in os.walk(local_dir):  
            print('[%s][%s][%s]' % (root,dirs,files))  
            for filespath in files:
                if filespath == file_name: # only upload specific file to Linux server remote path
                    fileFlag = 1  
                    local_file = os.path.join(root,filespath)  
                    print(11,'[%s][%s][%s][%s]' % (root,filespath,local_file,local_dir))  
                    a = local_file.replace(local_dir,'').replace('\\','/').lstrip('/')  
                    print('01',a,'[%s]' % remote_dir)  
                    remote_file = os.path.join(remote_dir,a)  
                    print(22,remote_file)  
                    try:  
                        sftp.put(local_file,remote_file)  
                    except Exception as e:  
                        sftp.mkdir(os.path.split(remote_file)[0])  
                        sftp.put(local_file,remote_file)  
                        print("66 upload %s to remote %s" % (local_file,remote_file))
                    
            for name in dirs:  
                local_path = os.path.join(root,name)  
                print(0,local_path,local_dir)  
                a = local_path.replace(local_dir,'').replace('\\','')  
                print(1,a)  
                print(1,remote_dir)  
                remote_path = os.path.join(remote_dir,a)  
                print(33,remote_path)  
                
                try:  
                    sftp.mkdir(remote_path)  
                    print(44,"mkdir path %s" % remote_path)  
                except Exception as e:  
                    print(55,e) 
        if fileFlag: 
            print('77,upload file success %s ' % datetime.datetime.now())  
            t.close() 
        else:
            print("99,the current dir does't have the specific file") 
            t.close()
    except Exception as e:  
        print(88,e)  

if __name__=='__main__':  
     local_dir= "C:/Users/csjdli/Desktop/bigarm0313/" # windows local dir path
     remote_dir= "/var/www/Bigarm/Bigarm/data/"  #Linux remote dir path
     fileName = "test_20-Mar-2019.csv"  # file_name to be uploaded
     upload(local_dir,remote_dir, fileName)
	 
#download files from Linux server to Windows local path
'''
def remote_scp(host_ip,remote_path,local_path,username,password):  
    t = paramiko.Transport((host_ip,22))  
    t.connect(username=username, password=password)  
    sftp = paramiko.SFTPClient.from_transport(t)  
    src = remote_path  
    des = local_path  
    sftp.get(src,des)  
    t.close() 
'''