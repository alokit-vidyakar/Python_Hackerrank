"""come to this after brute forcce file
what happeded earlier is I creted all the subsets from the string and looped through each subset to check if first letter 
is vowel or not. But it majorly increased the complexity as it had four for loops. Two nested each. 

Another approach in order to approach this problem is to understand below points:

1. You don't need subsets, you just need count of subset
2. If the string of length 6 has a vowel at position 1st index then number of susbsets created from that position is 
	6-1. In order to geralize len(S)-i. All the subsets will be of vowel starting

3. The memory and time complexity can be O(1) for this. 

"""
def minion_game(string):
	vowel = ['A','E','I','O','U']
	count_kevin =0
	count_stuart =0
	for i in range(len(string)):
		if string[i] in vowel:
			count_kevin+=(len(string)-i)
		else:
			count_stuart+=(len(string)-i)

	if count_stuart>count_kevin:
		print("Stuart",count_stuart)
	elif count_kevin>count_stuart:
		print("Kevin",count_kevin)
	else:
		print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)