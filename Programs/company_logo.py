#https://www.hackerrank.com/challenges/most-commons/problem

if __name__=="__main__":
	company_logo = input()
	list1=[]
	dictionary = {}
	"""for s in company_logo:
		key= dictionary.keys()
		for keys in key: 
			check =false
			if keys == s:
				check = true"""
	for alpha in company_logo:
		list1.append(alpha)
	list1.sort()
	key = dictionary.keys()
	for index in list1:
		check = 0
		for keys in key:
			if keys == index:
				check = 1
		if check == 0:
			dictionary[index]= 1
		else:
			value = dictionary[index]
			value+=1 
			dictionary[index]= value
	

	"""dictionary= sorted(dictionary)
	print(dictionary) 
	This prints only keys and loses values"""

	dic2=dict(sorted(dictionary.items(),key= lambda x:x[1],reverse=True))
	count =0
	for x,y in dic2.items():
		if count<3:
			print(x,y)
			count+=1




