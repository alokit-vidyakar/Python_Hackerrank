#https://www.hackerrank.com/challenges/list-comprehensions/problem
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    cordinates =[]
    for x_axis in range(0,x+1):
        for y_axis in range(0,y+1):
            for z_axis in range(0,z+1):
                sum = x_axis+y_axis+z_axis
                if sum!=n:
                    cordinates.append([x_axis,y_axis,z_axis])
                    
    print(cordinates)
