if __name__ == '__main__':
    print("enter number of student: ")
    number_of_students = int(input())
    student_data=[]
    highest =0.0
    runner_up=0.0
    runner_up_list=[]
    #taking input of students
    for student in range(number_of_students):
        name_of_student = input()
        score = float(input())
        student_data.append([name_of_student,score])
    

    for students in range(len(student_data)):
        
        if student_data[students][1] > runner_up:
            if student_data[students][1] > highest:
                runner_up=highest
                highest=student_data[students][1]
                
            else:
                runner_up=student_data[students][1]
    print("runner_up is: ",runner_up)
    for runner in range(len(student_data)):
        if student_data[runner][1] == runner_up:
            print(student_data[runner][0])
