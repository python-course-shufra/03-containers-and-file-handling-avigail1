classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]

def findStudent(s):
      for x,i in enumerate(classroom):
         if(i['name']==s ):
            return x,i

def add_student(name, email=None):
    """Add a new student to the classroom
    with the following keys:
    'name': the given name
    'email': if email is given use it otherwise use <name>@example.com
             in lowercase, you can use the `s.lower()` method
    'grade': initialize with empty list
    """
    newStunent={
        'name': name,
        'grades': [],
    }
    if(email):
        newStunent["email"]=email.lower()
    else:
        newStunent["email"]=f'{newStunent["name"].lower()}@example.com'
    classroom.append(newStunent)


    pass



def delete_student(name):
    """Delete a student from the classroom"""
    fstudent= findStudent(name)
    if(fstudent):
        classroom.remove(fstudent[1])
    pass



def set_email(name, email):
    """Sets the email of the student"""
    fstudent= findStudent(name)
    if(fstudent):
        classroom[fstudent[0]]["email"]=email
    pass

def add_grade(name, profession, grade):
    """Adds a new grade to the student grades"""
    fstudent= findStudent(name)
    if(fstudent):
        classroom[fstudent[0]]["grades"].append((profession, grade))
    pass


def avg_grade(name, profession):
    """Returns the average of grades of the student
    in the specified profession
    """
    sum=0
    count=0
    fstudent= findStudent(name)
    if(fstudent):
        for idx,val in enumerate(classroom[fstudent[0]]["grades"]):
            if(val[0]== profession):
                sum+=val[1]
                count+=1
    return sum/ count
    pass

def get_professions(name):
    prof=[]
    fstudent= findStudent(name)
    if(fstudent):
        for val in classroom[fstudent[0]]["grades"]:
            if not any (val[0]==x for x in prof):
               prof.append(val[0])
    return prof
    pass