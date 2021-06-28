import random
import string
import itertools
 
 
#随机生成num位数的密码，密码里面包含a-z,A-Z,0-9
def getRandomNumKey(num):
	a=string.ascii_letters+string.digits#数据源是a-z,A-Z，0-9
	key=random.sample(a,num)
	keys="".join(key)
	return keys
 
#产生所有的密码情况，其实就是全排列，全部列举出来
def generateNumKey(num):
	'''
	参数 num 是位数，返回值是一个列表
	'''
	keys=[]
	alist=list(string.ascii_letters+string.digits)#数据源是a-z,A-Z，0-9
	for i in itertools.product(alist,repeat= num):
		print(i)
		keys.append(''.join(list(i))+'\n')
	return keys
getRandomNumKey(4)
generateNumKey(4) #4为数的密码有 14776336个
 
 

