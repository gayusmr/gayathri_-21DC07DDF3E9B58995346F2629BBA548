






class student:

   def __init__(self, name, roll_number, cgpa):
     self.name = name
     self.roll_number = roll_number
     self.cgpa = cgpa


def sort_students (student_list):

  sorted_students=sorted(student_list,
                 key=lambda student:student.cgpa,reverse=True)


  return sorted_students


students=[
  student("Hari","A123",7.8),
  student("Srikanth","A124",7.9),
  student("Samunya","A125",8.1),
  student("Mahindhar","A126",8.2),
]

sorted_student = sort_students(students)


for student in sorted_student:
  print("Name: {},Roll_Number:{},CGPA {}".format(student.name,
                                     student.roll_number,
                 student.cgpa))