# Author: Yanling Wang yuw17@psu.edu

#Course1
lettergrade1 = input("Enter your course 1 letter grade: ")
credit1 = input("Enter your course 1 credit: ")
credit1 = int(credit1)
#loop to assign gradepoint for course 1
if lettergrade1 == "A":
  gradepoint1 = 4.0 
elif lettergrade1 == "A-":
  gradepoint1 = 3.67
elif lettergrade1 == "B+":
  gradepoint1 = 3.33
elif lettergrade1 == "B":
  gradepoint1 = 3.0
elif lettergrade1 == "B-":
  gradepoint1 = 2.67
elif lettergrade1 == "C+":
  gradepoint1 = 2.33
elif lettergrade1 == "C":
  gradepoint1 = 2.0
elif lettergrade1 =="D":
  gradepoint1 = 1.0
else:
    gradepoint1 = 0.0
print(f"Grade point for course 1 is: {gradepoint1}")

#Course2
lettergrade2 = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")
credit2 = int(credit2)
#loop to assign gradepoint for course 2
if lettergrade2 == "A":
  gradepoint2 = 4.0
elif lettergrade2 == "A-":
  gradepoint2 = 3.67
elif lettergrade2 == "B+":
  gradepoint2 = 3.33
elif lettergrade2 == "B":
  gradepoint2 = 3.0
elif lettergrade2 == "B-":
  gradepoint2 = 2.67
elif lettergrade2 == "C+":
  gradepoint2 = 2.33
elif lettergrade2 == "C":
  gradepoint2 = 2.0
elif lettergrade2 =="D":
  gradepoint2 = 1.0
else:
    gradepoint2 = 0.0
print(f"Grade point for course 2 is: {gradepoint2}")

#Course3
lettergrade3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ")
credit3 = int(credit3)
#loop to assign gradepoint for course 3
if lettergrade3 == "A":
  gradepoint3 = 4.0 
elif lettergrade3 == "A-":
  gradepoint3 = 3.67
elif lettergrade3 == "B+":
  gradepoint3 = 3.33
elif lettergrade3 == "B":
  gradepoint3 = 3.0
elif lettergrade3 == "B-":
  gradepoint3 = 2.67
elif lettergrade3 == "C+":
  gradepoint3 = 2.33
elif lettergrade3 == "C":
  gradepoint3 = 2.0
elif lettergrade3 =="D":
  gradepoint3 = 1.0
else:
    gradepoint3 = 0.0
print(f"Grade point for course 3 is: {gradepoint3}")

GPA = ((gradepoint1 * credit1) + (gradepoint2 * credit2) + (gradepoint3 * credit3) ) / (credit1 + credit2 + credit3) 
GPA = float(GPA)
print(f"Your GPA is: {GPA}")