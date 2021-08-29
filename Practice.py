MATH = 'Math'
PHYSICS = 'Physics'
SPORT = 'Sport'
HISTORY = 'History'

def main():
    students = {}
    id = 203834643
    grade = 86
    for i in range(10):
        students.update({(id+i): {}})
        students[id+i].update({MATH: (grade+i)})
        students[id + i].update({PHYSICS: (grade - i)})
        students[id + i].update({SPORT: (grade - (2*i))})
        students[id + i].update({HISTORY: (grade - (3 * i))})
    print(students)


if __name__ == "__main__":
    main()
