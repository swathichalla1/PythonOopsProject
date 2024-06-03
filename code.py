
class Student:
    student_dictionary = {}
    school_name = "ABC"
    def __init__(self):
        self.roll_no = input("\n\t Enter the student Roll Number : ")  
        self.name = input("\n\t Enter the student Name : ")
        self.phone_number = input("\n\t Enter the student phone number : ")
        self.address = input("\n\t Enter the student address : ")     
        student_class = input("\n\t Enter the student class [Ex: 1,2,3,...,10] : ")

        if student_class in StudentClass.classes:
            StudentClass.classes[student_class].studentList.append(self)
        else:
            new_class = StudentClass(student_class)
            new_class.studentList.append(self)
            StudentClass.classes[student_class] = new_class
        self.student_class = StudentClass.classes[student_class]

        print("\n Student added successfully")
        self.getStudent()

    def getStudent(self):
        print("\n---Student Details---\n")
        print("\tRoll Number : ",self.roll_no)
        print("\tName : ",self.name)
        print("\tPhone Number : ",self.phone_number)
        print("\tAddress : ",self.address)
        print("\tClass : ",self.student_class.name)
        print("\tSchool : ABC")
   
    def updateStudent(self):
        print("\t\tselect option to update student details\n")
        print("\t\t1) To change student name")
        print("\t\t2) To change student phone number")
        print("\t\t3) To change student Address")
        print("\t\t4) To change student class")

        option = input("select any above option : ")

        if option in ["1","2","3","4"]:
            if option == "1":
                self.name = input("\t\tEnter the updated student name : ")
                print("\n\t\t Student name changed succesfully\n")
            elif option == "2":
                self.phone_number = input("\t\tEnter the updated phone number :")
                print("\n\t\tStudent phone number changed succesfully")
            elif option=="3":
                self.address = input("\t\tEnter the updated student address : ")
                print("\n\t\tStudent address changed succesfully")
            elif option=="4":
                new_class = input("\t\tEnter the student new class : ")
                self.student_class.studentList.remove(self)
                try:
                    self.student_class = StudentClass.classes[new_class]
                    self.student_class.studentList.append(self)
                except:
                    addClass = StudentClass(new_class)
                    self.student_class = addClass 
                    addClass.studentList.append(self)
                print("\t\tstudent class chnaged successfully")

        else:
            print("You have choosen wrong option")

    @classmethod
    def updateschoolname(cls,new_school):
        cls.school_name = new_school

    @classmethod 
    def getallstudentscount(cls):
        return len(cls.student_dictionary)


class StudentClass:

    classes = {}
    def __init__(self,name):
        self.name = name 
        StudentClass.classes[name] = self 
        self.studentList = []


def main():
    print(f"---Welcome to {Student.school_name} school---\n")
    print("\t1) Get student details")
    print("\t2) Add new student")
    print("\t3) Remove student")
    print("\t4) Update student details")
    print("\t5) Update school name")
    print("\t6) Get number of students in school")
    print("\t7) Get all student details")
    print("\t8) Get any class student details")

    option = input("Enter any above given option you want: ")

    if option=="1":
        roll_no = input("\tEnter the roll number of student : ")
        try:
            Student.student_dictionary[roll_no].getStudent()
        except:
            print("\t\tEnter valid roll number")
    elif option=="2":
        new_student = Student()
        Student.student_dictionary[new_student.roll_no] = new_student 
    elif option=="3":
        roll_no = input("\tEnter the roll number of student : ")
        try:
            student = Student.student_dictionary.pop(roll_no)
            student.student_class.studentList.remove(student)
            print("\t\t""  ",roll_no," Student deleted succesfully")
        except:
            print("\t\tEnter valid roll number")
    elif option=="4":
        roll_no = input("\tEnter the roll number of student : ")
        try:
            Student.student_dictionary[roll_no].updateStudent()
        except:
            print("\n\tYou have entered the wrong roll_no")
    elif option=="5":
        new_school=input("\t\tEnter the new school name : ")
        Student.updateschoolname(new_school)
        print("\t\tschool name changed successfully")
    elif option=="6":
        print("\t\tTotal number of students are : ",Student.getallstudentscount())

    elif option=="7":
        if Student.student_dictionary:
            print("Total Number of students in school : ",Student.getallstudentscount())
            print("\n Below are total student list with details")
            for sNo,student in enumerate(Student.student_dictionary.values()):
                print("Student No : ",sNo+1)
                student.getStudent()
                print("")
        else:
            print("\t\t There are no students")
    elif option=="8":
        try:
            students = StudentClass.classes[input("\tenter the class : ")]
            print("\nstudents of class ",students.name)
            print(f"\n Total number of students in class {students.name}: {len(students.studentList)}")
            print("")
            for sNo,eachstudent in enumerate(students.studentList):
                print("Student No : ",sNo+1)
                print("student is : ",eachstudent)
                eachstudent.getStudent()
                print("")
        except:
            print("\tNo students there")

if __name__ == "__main__":
    option="y"
    while option == "y":
        main()
        option = input("\nDo you want to continue [y/n] ?")
        print("")



        

