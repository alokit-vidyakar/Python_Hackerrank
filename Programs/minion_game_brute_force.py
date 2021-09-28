#https://www.hackerrank.com/challenges/the-minion-game/problem

def mininon_game(string):
	
	length =0
	for i in range(len(string)):
		for j in range(len(string)): 
				if (i+j+1) <= len(string):
					sub_string = string[j:i+j+1]
					#print(sub_string)
					subsets.append(sub_string)

if __name__ =="__main__":
	string = input()
	subsets = []
	stuart=[]
	kevin =[]
	mininon_game(string)
	vowels =['A','E','I','O','U']
	print(subsets)
	for subset in subsets:
		count=0
		for vowel in vowels:
			if subset[0] == vowel:
				count =1
		if count ==1:
			kevin.append(subset)
		else:
			stuart.append(subset)	
print("*****************************stuart********************")
print(*stuart)
print("*****************************kevin********************")
print( *kevin)

a = len(stuart)
b = len(kevin)
print(a,b)

if a>b:
	print("Stuart",a)
if(b>a):
	print("Kevin",b)
else:
	print("Draw")