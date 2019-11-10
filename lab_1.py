import math
num1 = input("input a number in between 1 and 10: ")
num2 = input("input another number in between 1 and 10: ")
print(type (num1))


end_num = math.pow(num1,num2)
print(end_num)
end_num = math.sqrt(end_num)
if end_num == 1:
	end_num += 99999
while (end_num<100000):
	end_num += 1
print(end_num)