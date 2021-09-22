if __name__ == '__main__':
    N = int(input())  # denotes tehe number of commands to run
    final_list= []
    for n in range(0,N):
        command = input().split()
        if (command[0] == "append"):
            final_list.append(int(command[1]))

        elif (command[0] == "print"):
            print(final_list)
        
        elif (command[0] == "remove"):
            final_list.remove(int(command[1]))
                    

        elif (command[0] == "insert"):
            final_list.insert(int(command[1]),int(command[2]))

        elif (command[0]=="sort"):
            final_list.sort()

        elif (command[0]=="pop"):
            final_list.pop()

        else:
            final_list.reverse()