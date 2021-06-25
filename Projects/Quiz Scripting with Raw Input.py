names = list(input("Enter names separated by commas: ").split(","))
assignments = list(input("Enter assignment counts separated by commas: ").split(","))
grades = list(input("Enter grades separated by commas: ").split(","))

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name, assignment, grade in zip(names,assignments,grades):
    print(message.format(name.title(), assignment, grade, int(grade) + int(assignment)*2))