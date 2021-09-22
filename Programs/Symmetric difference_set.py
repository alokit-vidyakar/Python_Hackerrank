if __name__ == "__main__":
    print("number of students in english class: ")
    number_of_student_for_english=int(input())
    print("Enter set for english: ")
    """english= set()
    for value in range(0,number_of_student_for_english):
        #print("enter", value, "element: ")
        rollNumber=input()
        english.add(rollNumber)"""

    english = set(input().split())

    print("number of students in french class: ")
    number_of_student_for_french=int(input())
    print("Enter set for french: ")
    """french=set()
    for value in range(0,number_of_student_for_french):
       # print("enter", value, "element: ")
        rollNumber=input()
        french.add(rollNumber)"""
    french = set(input().split())


    #print(english,french)
    #result_set=english.symmetric_difference(french)
    #print("the length:", len(result_set))
    
    print(len(english.symmetric_difference(french)))   
        
    