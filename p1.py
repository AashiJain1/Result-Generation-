import sys
import pyodbc
print ('RESULTS')
class StudentResult:
    college=0
    course=0
    enroll=0
    year=0
    def inputdata(self):
        print('Choose your college:  ')
        print('1. College of Engineering and Technology')
        print('2. College of Business Management, Economics and Commerce')
        print('3. College of Arts, Science and Humanities')
        print('4. College of Law and Governance')
        print('5. College of Fashion Design and Merchandising')
        print('6. College of Architecture and Design')
        StudentResult.college=int(input('Enter your college number:  '))
        print('Choose your course')
        if StudentResult.college==1:
            print('1. B.Tech CS&E')
            print('2. B.Tech ECE')
        elif StudentResult.college==2:
            print('1. B.A.')
            print('2. B.B.A.')
        elif StudentResult.college==3:
            print('1. B.A.')
            print('2. M.A.')
        elif StudentResult.college==4:
            print('1. B.A. LLB')
            print('2. B.B.A. LLB')
        elif StudentResult.college==5:
            print('1. Bachelors')
            print('2. Masters')
        elif StudentResult.college==6:
            print('1. Bachelor of Architecture')
            print('2. Bachelor of Interior Design')
        else:
            sys.exit('Invalid College')
        StudentResult.course=int(input('Enter your course number:  '))
        StudentResult.enroll=int(input('Enter your enrollment number:  '))
        StudentResult.year=int(input('Enter your year:  '))    
    def outputdata(self):
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Aashi Jain\Desktop\result.accdb;')
        cursor = conn.cursor()
        cursor.execute('select * from Table1')
            
        c=0          
        for row in cursor.fetchall():
            if row.Enrollment==StudentResult.enroll and row.College==StudentResult.college and row.Course==StudentResult.course and row.Year==StudentResult.year:
                print(row.Marks)
                c=1
        if c==0:
            print('You have inserted wrong information')
        return;

s=StudentResult()
s.inputdata()
s.outputdata()            
