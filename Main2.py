class School:
    def __init__(self, professors, Student,Cources):
        self.professors = professors
        self.Student = Student
        self.Cources  = Cources 

    def addCource( Students , Code,Prof,Min,Max):#done
        Cources.append(Cources( Students , Code,Prof,Min,Max))
    
    def addStudent(CorcesList,Grades,id,address, phoneNumber,age,name):#ddone
         Student.append(Student(CorcesList,Grades,id,address, phoneNumber,age,name))

    def addProf(Corces,salaried , address, phoneNumber,age,name ):#done
        professors.append(professors(CorcesList,salaried , address, phoneNumber,age,name ))



 
class  courses: 
    def __init__(self, Students , Code,Prof,Min,Max):
        self.Students  = Students 
        self.Code = Code
        self.Prof  = Prof 
        self.Min  = Min 
        self.Max  = Max 
    def addStudent(s1):
        Students.append(s1)
    def addProf(p1):
        Prof.append(p1)
 
class Grades :
    grads=0
    def __init__(self, Corce  ):
        self.Corce  = Corce 
    def adjestMarks(grads):
        if 0<grads<100:
            print("Pleas put marks from 0 to 100 ")
    

class People:#done
    def __init__(self, address, phoneNumber,age,name):
        self.address =  address
        self.phoneNumber = phoneNumber
        self.name =  name
        self.age = age 
class employees(People):#done
    def __init__(self, salaried , address, phoneNumber,age,name):
        super().__init__( address, phoneNumber,age,name)
        self.salaried  = salaried  
class  professors(employees):# done 
    OneTimeBonusDone = False  
  
    def __init__(self, CorcesList,salaried , address, phoneNumber,age,name ):
        self.CorcesList =CorcesList
        super().__init__( salaried , address, phoneNumber,age,name)
        
    def addCource(CorcesList):
        if len(CorcesList)>3 and OneTimeBonusDone==flase:
            salaried=salaried+20000
            OneTimeBonusDone=true
        CorcesList.append(Corces)       
        Cources.addProf(self)



class Student(People):#done
    
    def __init__(self,CorcesList, Grades,id,address, phoneNumber,age,name):
        super().__init__( address, phoneNumber,age,name)
        self.Grades   = Grades
        self.Id   = id  
        self.CorcesList=CorcesList
    def addCource(Cource):
        
        if len(Cource)==6:
            print("Can't allow more than 6 ")
            return null
        Cource.addStudent(self)
        CorcesList.append(Cource)
    def CheckifHeisAPartTime():
        if len(Cource)<3:
            print("he is a part time")
        else :
            print("he is a reguler student ")
    def CheckifHeIsonAcademicProbation():
        sum=0
        for i in range(len(Grades)):
            sum=sum+Grades[i].grads
        if sum/(len(Grades)*100)<.6:
            print("on academic probation.")



p=professors([],8000 , "abc2", "dasdasd","40","dr" )
s=Student(None,None,"41710033","abc", "123","16","Hosam")
c=courses( [s] , "Code",[s],1,5)
x= School([p],[s],[c])

print(x.Student[0].name)