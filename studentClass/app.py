
# Importing the student object we created from the studentinfo.py file
from studentinfo import student

student1 = student('Joseph', 'Programmer', 79.5, False)
student2 = student('Raphael', 'Data Analyst', 65.3, False)
student3 = student('Fred', 'Designer', 60.9, True)
student4 = student('Simon', 'Writer', 75.0, False)
student5 = student('Lucy', 'Journalist', 70.6, False)
student6 = student('Irene', 'Model', 63.8, True)
student7 = student('Joel', 'Teacher', 80.1, False)


print(student5.name, student5.gpa, student5.is_on_probation)
print(student2.name, student2.gpa, student2.is_on_probation)
print(student3.name, student3.gpa, student3.is_on_probation)