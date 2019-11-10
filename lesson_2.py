result=0
def common_num(x,y):
	global result
	for i in range (len(x)):
		if x[i] in (y):
			result+=1

	return result


x=[22,44,24,65]
y=[22,24,71,99]

result=common_num(x,y)
print result


	