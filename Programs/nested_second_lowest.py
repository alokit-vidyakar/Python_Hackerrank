#https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    print("enter number of student: ")
    number_of_students = int(input())
    student_data=[]
    set_mark = set()

    #taking input of students"""
    for student in range(number_of_students):
        name_of_student = input()
        score = float(input())
        student_data.append([name_of_student,score])
        set_mark.add(score)

    """for students in range(len(student_data)):

        if student_data[students][1] < second_lowest:
            if student_data[students][1] < lowest:
                second_lowest=lowest
                lowest=student_data[students][1]
                
            else:
                second_lowest=student_data[students][1]
    listing=[]
    for runner in range(len(student_data)):
        if student_data[runner][1] == second_lowest:
            listing.append(student_data[runner][0])
    listing.sort()
    for n in range(len(listing)):
        print(listing[n])"""
    print(set_mark)
    set_mark=sorted(set_mark)
    second_lowest = set_mark[1]

    for students in student_data:
        if students[1] == second_lowest:
            name.append(students[0])
    
    name.sort()
    for nm in name:
        print(nm)
    

