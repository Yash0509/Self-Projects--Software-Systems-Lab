from fileinput import close
from importlib.resources import path
import json
from operator import truediv
from student import Student
from exception import Lab5Exception
class StudentBuilder:
    r"""
        You are expected to define a static method
        by the name build_student_object. It should take in 
        path to a json file and read the contents of the file.

        You are also expected to validate the contents read from 
        the JSON file and raise Exception accordingly
    """
    # def __init__(self,data.json)
    # self.path=data.json
    @staticmethod
    def build_student_object(path_to_file):
        D={}
        #f=open('path_to_file.json')
        file=open(path_to_file)
        data=json.load(file)
        q=Student(data["name"], data["age"], data["cgpa"], data["gender"], data["home_town"])
        boo=False
        if(data["gender"]=='Male' or data["gender"]=='Female' or data["gender"]=='Non-Binary' or data["gender"]=='Prefer Not To Say'):
            boo=True
        L=[['name',q.get_name()], ['age',q.get_age()], ['cgpa',q.get_cgpa()], ['gender',q.get_gender()], ['hometown',q.get_home_town()]]
        key=q.get_name()
        if D.get(q.get_name) is not None:
                print("Same Data")
        else:       
            for i in range(len(L)):
                if key in D:
                    print("Same Data")
                    raise Lab5Exception("Already Exists")
                    pass
                else:
                    D[L[i][0]]=[]
                    D[L[i][0]].append(L[i][1])
        
        if(data["age"]<=35 and data["cgpa"]<=10.0 and boo ):
            print(D)
            #print(q.get_name(),q.get_age(),q.get_cgpa(),q.get_gender(),q.get_home_town())
        else:
            print("Not Correct data")