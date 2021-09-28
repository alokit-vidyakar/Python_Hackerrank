def max_squre(array):
	max =0
	for items in array:
		items = items*items
		if items>max:
			max=items
	fmax_i.append(max)

def fx(fmax_i,m):
	sum = 0
	for items in fmax_i:
		sum += items
	fx = sum % m 
	print(fx)

if __name__== "__main__":
	#values = map(int,input().split())
	k,m = int(input()), int(input())
	fmax_i =[]
	for i in range(0,k):
		listing = map(int, input().split())
		max_squre(listing)
	print("fmax_i is:",fmax_i)
	fx(fmax_i,m)