import urllib.request
import requests
import json

def thingspeak_host():
    c=int(input("enter your choice :\n\t 1 to send message\n\t 2 to check message\n"))
    if(c==1):
        KEY=input("enter recipient key : ")
        val=input("enter your message : ")
        URl="https://api.thingspeak.com/update?api_key=" 
        HEADER='&field1={}'.format(val)
        NEW_URL = URl+KEY+HEADER
        data=urllib.request.urlopen(NEW_URL)
        print("your message has been delivered")
    elif(c==2):
        RID=input("ENter your Application Id : ")
        RKEY=input("enter your key to check your messages : ")
        RURL1="https://api.thingspeak.com/channels/"
        RURL2="/feeds.json?api_key="
        RHEADER="&results=2"
        RNEW_URL=RURL1+RID+RURL2+RKEY+RHEADER
        b=requests.get(RNEW_URL)
        c=b.json()
        d=c["feeds"][0]["field1"]
        print("your message is :  ",d)
    else:
        print("invalid choice")
            
if __name__ == '__main__':
    while 1:
        s=input("do you want to continue: Y/N\n")
        if(s=='Y' or s=='y'):
            thingspeak_host()
        else:
            exit()
