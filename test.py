import urllib2,os
try:
    sfacg_data = os.environ["sfacg_data"]
    cookie = os.environ["cookie"]
    auth = os.environ["auth_data"]
    requrl = "https://api.sfacg.com/user/signInfo"
    headerdata = {"Cookie":cookie,"SFSecurity":sfacg_data,"Authorization":auth,"User-Agent":"boluobao/4.6.36(android;22)/OPPO"}
    request = urllib2.Request(requrl,None,headerdata)
    request.get_method = lambda: 'PUT'
    response = urllib2.urlopen(request)
    print response.read()
except BaseException,Argument:
    print "error:",Argument