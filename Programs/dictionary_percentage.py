#https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for student in student_marks:
        if student==query_name:
            sum =0
            for avg in student_marks[student]:
                sum = sum + avg
            average = sum / 3
            print('%.2f' % average)
                