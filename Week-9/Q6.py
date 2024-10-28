def count_courses(file_path):
    course_count = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            program, course = line.strip().split(',')
            if program in course_count:
                course_count[program] += 1
            else:
                course_count[program] = 1

    for program, count in course_count.items():
        print(f"{program}-{count}")

# Example usage
count_courses('Week-9/programs.csv')
