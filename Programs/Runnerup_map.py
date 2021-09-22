if __name__ == '__main__':
   # n = int(input())
    arr = map(int, input().split())
    top=-101
    runner_up= -101
    for arr_item in arr:
        if arr_item>runner_up:
            if arr_item>top and arr_item!=top:
                runner_up = top
                top=arr_item
            if arr_item<top:    
                runner_up=arr_item
    print(runner_up)
