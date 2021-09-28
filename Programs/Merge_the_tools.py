#https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    substring = []
    m =0 
    for i in range(len(string)//k):
        sub=string[m:m+k]
        substring.append(sub)
        m+= k

    for values in substring:
        array =[]
        for chars in values:
            if len(array)!=0:
                count= 0
                for i in array:
                    if i==chars:
                        count=1
                if count==0:
                    array.append(chars)
            else:
                array.append(chars)
        printing = ''.join(array)
        print(printing)
        del array
        
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)