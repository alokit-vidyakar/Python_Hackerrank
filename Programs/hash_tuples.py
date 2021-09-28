#https://www.hackerrank.com/challenges/python-tuples/problem
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    list1=list(integer_list)
    tuple1=tuple(list1)
    print(hash(tuple1))