#https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
    character = ""
    for loop in s:
        if loop.isupper()==1:
            character+=loop.lower()
        else:
            character+= loop.upper()
            
    return character

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)