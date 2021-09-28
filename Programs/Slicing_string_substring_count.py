#https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    sub_len = len(sub_string) 
    count = 0
    for search in range(0,len(string)):
        sub = string[search:search+sub_len]
        print(sub)
        if sub == sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)