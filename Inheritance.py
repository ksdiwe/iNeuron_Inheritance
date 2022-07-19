import logging
from exceptionfile import String_Exception
from exceptionfile import Integer_Exception
from exceptionfile import Range_Exception

logging.basicConfig(filename="Inheritance.log", level=logging.DEBUG, format="%(levelname)s %(asctime)s %(name)s %(message)s")

"""
with reference: https://github.com/BokkisamRohit/task7_09-07-2022/blob/main/Inheritance_and_Polymorphism.py
"""
#############################################################################################################################################################################
# Example 01: Single Inheritance
# Single inheritance enables a derived class to inherit properties from a single parent class,
# thus enabling code reusability and the addition of new features to existing code.
class iNeuron_Students:
    name = ""
    _coursetype = ""
    __background = ""
    __qualification = ""
    __statusOfemployment = ""

    def __init__(self, name, coursetype, background, qualification, statusOfemployment):
        """

        :param name: Name of the Student
        :param coursetype: Student opted for which course
        :param background: Student belongs to CS or Non-CS background
        :param qualification: Qualification of the Student before applying to iNeuron Course
        :param statusOfemployment: Status of Student whether he/she is employed or not
        """
        try:
            logging.info("The given name is %s", name)
            if type(name) != str:
                raise (String_Exception("The given input is not of string type."))
            else:
                self.name = name

            logging.info("Student opted for course is %s", coursetype)
            if type(coursetype) != str:
                raise(String_Exception("Given Course is not of string type. Please enter a valid course."))
            else:
                self._coursetype = coursetype

            logging.info("Background of Student is %s", background)
            if type(background) != str:
                raise (String_Exception("Invalid Course. Not in string type. Please enter a valid course"))
            else:
                self.__background = background

            logging.info("Qualification of Student is %s", qualification)
            if type(qualification) != str:
                raise (String_Exception("The given values are not of string type. Please enter a valid Qualification."))
            else:
                self.__qualification = qualification

            logging.info("Employment status of a student is %s", statusOfemployment)
            if type(statusOfemployment) != str:
                raise (String_Exception("Entered status is not in string type. Please enter a valid status"))
            else:
                self.__statusOfemployment = statusOfemployment

        except Exception as e:
            logging.exception("The Exceptions we have got:" + "\n" + str(e))
            self.name = ""
            self._coursetype = ""
            self.__background = ""
            self.__qualification = ""
            self.__statusOfemployment = ""

    def Student_Details(self):
        """

        :return: Student Details
        """
        print(self.name, self._coursetype, self.__background, self.__qualification, self.__statusOfemployment)

    def Welcome_Note(self):
        print(f"Hola..!! {self.name}, Welcome to iNeuron.")

class iNeuron_Internship(iNeuron_Students):
    Project_Name = ""
    Project_Details = ""
    Project_members = ""
    Project_OfferLetter = ""

    def __init__(self, name, coursetype, background, qualification, statusOfemployment, Project_Name, Project_Details, Project_members, Project_OfferLetter):
        super().__init__(name, coursetype, background, qualification, statusOfemployment)
        #  In a class hierarchy with single inheritance, super can be used to refer to parent classes without naming them explicitly.
        # Super() support cooperative multiple inheritance in a dynamic execution environment.
        try:
            logging.info("Project Name %s", Project_Name)
            if type(Project_Name) != str:
                raise (String_Exception("Invalid Project Name. Name is not in string type. Please enter valid project name."))
            else:
                self.Project_Name = Project_Name

            logging.info("Details of Project are: %s", Project_Details)
            if type(Project_Details) != str:
                raise (String_Exception("Invalid Details. Not in string type. Please enter valid details."))
            else:
                self.Project_Details = Project_Details

            logging.info("Project Member are: %s", Project_members)
            if type(Project_members) != str:
                raise (String_Exception("Invalid Members name. Not in string type. Please enter valid names."))
            else:
                self.Project_members = Project_members

            logging.info("Offer letter of iNeuron Internship: %s", Project_OfferLetter)
            if type(Project_OfferLetter) != str:
                raise (String_Exception("Invalid. Letter not string type. Please enter valid offer letter."))
            else:
                self.Project_OfferLetter = Project_OfferLetter

        except Exception as e:
            logging.exception("Exceptions that we have got:" + "\n" + str(e))
            self.Project_Name = ""
            self.Project_Details = ""
            self.Project_members = ""
            self.Project_OfferLetter = ""


    def Internship_Details(self):
        print(self.name, self._coursetype, self.Project_Name, self.Project_Details, self.Project_members, self.Project_OfferLetter)

    def Welcome_Note(self):
        print("Hola..!! {}, Welcome to iNeuron Internship.", format(self.name))

"""

object1 = iNeuron_Internship("Komal Diwe","FSDS","CS","M.tech","Non-employee","Travel Analysis","Analysis of traveling plans","None","Offer Letter")
object1.Internship_Details()
object1.Welcome_Note()

object1 = iNeuron_Internship("Komal Diwe","FSDS","CS",9076,"Non-employee","Travel Analysis","Analysis of traveling plans","None","Offer Letter")
object1.Internship_Details()
"""
#############################################################################################################################################################################
# Example 02: Multilevel Inheritence
# In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class.
# This is similar to a relationship representing a child and a grandfather.
class iNeuron_courses:
    courseName = ""
    courseDuration = ""

    def setCourse_Name(self, courseName, courseDuration):
        try:
            logging.info("Course registered: %s", courseName)
            if type(courseName) != str:
                raise (String_Exception("Course Name is not in string type. Please enter valid Course Name."))
            else:
                self.courseName = courseName

            logging.info("Course Duration: %s", courseDuration)
            if type(courseDuration) != int:
                raise (Integer_Exception("Not in interger type. Please enter valid duration time."))
            else:
                self.courseDuration = courseDuration

        except Exception as e:
            logging.exception("The exceptions we have got:" + "\n" + str(e))
            self.courseName = ""
            self.courseDuration = ""


    def getCourse_Details(self):
        """

        :return: Course Details: Name of Course, its duration.
        """
        print("Course Name: ", self.courseName)
        print("Course Duration: ", self.courseDuration)

class iNeuron_class(iNeuron_courses):
    Instructor_Name = ""
    topics = []

    def subTopics(self, *st):
        """

        :param st: List of tuples, which consists of string variables with values for topics to be cover/covered.
        :return: prints topics
        """
        logging.info("Topic to be Cover: %s", str(st))
        self.topics = list(st)
        print("Topics: ", self.topics)

    def Instructor(self, Instructor_Name):
        """

        :param Instructor_Name: Course Instructor's Name
        :return: prints name of instructor
        """
        try:
            logging.info("Name of Instructor: %s", Instructor_Name)
            if type(Instructor_Name) != str:
                raise (String_Exception("Name should be in string type. Enter valid name."))
            else:
                self.Instructor_Name = Instructor_Name
        except Exception as e:
            logging.exception("Exception we got:" + str(e))
            self.Instructor_Name = ""

        print("Instructor Name: ", self.Instructor_Name)

class Instructor_Details(iNeuron_class):
    LinkedIn_Profile = ""
    Youtube_Profile = ""

    def Instructors_LinkedIN(self, link):
        """

        :param link: Instructor's LinkedIn profile link
        :return: prints the LinkedIn profile link
        """
        try:
            logging.info("Instructor's LinkedIn Profile: %s", link)
            if type(link) != str:
                raise (String_Exception("Profile link not in String type. Please enter valid link."))
            else:
                self.LinkedIn_Profile = link
        except Exception as e:
            logging.exception("Exception:" + str(e))
            self.LinkedIn_Profile = ""

        print("Instructor's LinkedIn Profile:", self.LinkedIn_Profile)

    def Instructor_Youtube(self, youtube):
        """

        :param youtube: Instructor's Youtube Profile link
        :return: prints the youtube link of Instructor
        """
        try:
            logging.info("Instructor's Youtube Link: %s", youtube)
            if type(youtube) != str:
                raise (String_Exception("Not in string type. Enter Valid Link."))
            else:
                self.Youtube_Profile = youtube
        except Exception as e:
            logging.exception("Exception:" + str(e))
            self.Youtube_Profile = ""

        print("Instructor's Youtube Link: ", self.Youtube_Profile)

"""
object2 = Instructor_Details()
object2.Instructors_LinkedIN("https://www.linkedin.com/in/-sudhanshu-kumar/")
object2.setCourse_Name("FSDS", 1)
object2.getCourse_Details()
"""
############################################################################################################################################################################
# Example 03: Multiple Inheritence
# When a class can be derived from more than one base class this type of inheritance is called multiple inheritances.
# In multiple inheritances, all the features of the base classes are inherited into the derived class.
class FSDS_Bootcamp:
    FSDS_details = ""

    def FSDSbootcamp_Details(self, FSDS_details):
        try:
            logging.info("Full Stack Data Science Bootcamp Details: s", FSDS_details)
            if type(FSDS_details) != str:
                raise (String_Exception("Details are not in string type."))
            else:
                self.FSDS_details = FSDS_details
        except Exception as e:
            logging.exception("Exception: " + str(e))
            self.FSDS_details = ""

        print("Full Stack Data Science Bootcamp details are: ", self.FSDS_details)

class Hackathon:
    Hackathon_details = ""

    def Hackathon_Details(self, Hackathon_details):
        """

        :param Hackathon_details: Details of Hackathons take place in iNeuron
        :return: prints detail of Hackathon.
        """
        try:
            logging.info("Hackathon Details: %s", Hackathon_details)
            if type(Hackathon_details) != str:
                raise (String_Exception("Details are not in string type."))
            else:
                self.Hackathon_details = Hackathon_details
        except Exception as e:
            logging.exception("Exception: " + str(e))
            self.Hackathon_details = ""

        print("Details of Hackathon: ", self.Hackathon_details)

class Blogs:
    blog_title = ""
    blog_url = ""
    blog_content = ""
    def Blog_details(self, blog_title, blog_url):
        """

        :param blog_title: Title of Blog
        :param blog_url: URL of blog
        """
        try:
            logging.info("Blog Title: %s", blog_title)
            if type(blog_title) != blog_title:
                raise (String_Exception("Blog title should be in string format only."))
            else:
                self.blog_title = blog_title

            logging.info("Blog url: %s", blog_url)
            if type(blog_url) != str:
                raise (String_Exception("Invalid url. should in string format."))
            else:
                self.blog_url = blog_url
        except Exception as e:
            logging.exception("Exception: " + "\n" + str(e))
            self.blog_title = ""
            self.blog_url = ""
        print("Blog Title:", self.blog_title)
        print("Blog url:", self.blog_url)

    def Blog_content(self):
        """
        Write content to the blog
        :return: blog Information
        """
        logging.info("Content of the blog:")
        content = input("start typing your content for your blog. Do not press enter Enter untill you finish your writing.")
        self.blog_content = content

        return (self.blog_title, self.blog_url, self.blog_content)

class iNeuron(FSDS_Bootcamp, Hackathon, Blogs):
    pass

"""
object3 = iNeuron()
object3.Hackathon_Details("iNeuron Hackathon conducted for 24hrs.")
object3.Blog_content()
"""
#############################################################################################################################################################################
# Example 04: Hierarchical Inheritence
# When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance.
#method overriding iNeuron Students. we will be using iNeuron_Students from example 01.

class Tech_Neuron(iNeuron_Students):
    CourseName = ""

    def __init__(self, name, coursetype, background, qualification, statusOfemployment, CourseName):
        super().__init__(name, coursetype, background, qualification, statusOfemployment)
        try:
            logging.info("Course name: %s", CourseName)
            if type(CourseName) != CourseName:
                raise (String_Exception("Course not in string type. Please enter valid course name."))
            else:
                self.CourseName = CourseName
        except Exception as e:
            logging.exception("Exception" + str(e))
            self.CourseName = ""

    def techNeuron_details(self):
        """

        :return: prints the detail of tech neuron courses
        """
        print(self.name, self.CourseName)

    def Welcome_Note(self):
        print(f"Hola..!! {self.name},Welcom to Tech Neuron")

class FSDS(iNeuron_Students):

    def __init__(self, name, coursetype, background, qualification, statusOfemployment, CourseName):
        super().__init__(name, coursetype, background, qualification, statusOfemployment)

    def FSDS_details(self):
        """

        :return: Students details from tech neuron
        """
        print(self.name, self._coursetype)

    def Welcome_Note(self):
        print(f"Hola..! {self.name}, Welcome to Full Stack Data Science Bootcamp.")

"""
object4 = FSDS("Komal Diwe", "FSDS", "CS", "Mtech", "Non-employee", "FSDS Bootcamp")
object4.FSDS_details()
object4.Student_Details()
"""
############################################################################################################################################################################
# Example 05: Polymorphism on Contact details using Students and Instructors class and single function outside of both classes to check the detatils.

class Student_ContactDetails:
    student_mailID = ""
    student_phoneNo = ""

    def Student_EmailID(self, student_mailID):
        """

        :param student_mailID: Students Email Address
        :return: None
        """
        try:
            logging.info("Student's Email ID: %s", student_mailID)
            if type(student_mailID) != str:
                raise (String_Exception("Not in string format. enter valid Email ID."))
            else:
                self.student_mailID = student_mailID
        except Exception as e:
            logging.exception("Exception" + str(e))
            self.student_mailID = ""

    def Student_PhoneNumber(self, student_phoneNo):
        """

        :param student_phoneNo: Student's Mobile Number
        :return: None
        """
        try:
            logging.info("Student's Mobile Number: %s", student_phoneNo)
            if type(student_phoneNo) != int:
                raise (Integer_Exception("Not in interger format. enter valid mobile number."))
            else:
                self.student_phoneNo = student_phoneNo
        except Exception as e:
            logging.exception("Exception" + str(e))
            self.student_phoneNo = ""

    def print_EmailID(self):
        """

        :return: Prints student's Email address
        """
        print("Student's Email ID: ", self.student_mailID)

    def print_PhoneNo(self):
        """

        :return: Prints STudent's Mobile number
        """
        print("STudent's Mobile number:", self.student_phoneNo)

class Instructor_ContactDetails:
    instructor_mailID = ""
    instructor_phoneNo = ""

    def Instructor_EmailID(self, instructor_mailID):
        """

        :param instructor_mailID: Instructor Email Address
        :return: None
        """
        try:
            logging.info("Instructore's Email ID: %s", instructor_mailID)
            if type(instructor_mailID) != str:
                raise (String_Exception("Not in string format. enter valid Email ID."))
            else:
                self.instructor_mailID = instructor_mailID
        except Exception as e:
            logging.exception("Exception" + str(e))
            self.instructor_mailID = ""

    def Instructor_PhoneNumber(self, instructor_phoneNo):
        """

        :param instructor_phoneNo: Instructor's Mobile Number
        :return: None
        """
        try:
            logging.info("Instructor's Mobile Number: %s", instructor_phoneNo)
            if type(instructor_phoneNo) != int:
                raise (Integer_Exception("Not in interger format. enter valid mobile number."))
            else:
                self.instructor_phoneNo = instructor_phoneNo
        except Exception as e:
            logging.exception("Exception" + str(e))
            self.instructor_phoneNo = ""

    def print_EmailID(self):
        """

        :return: Prints instructor's Email address
        """
        print("Instructor's Email ID: ", self.instructor_mailID)

    def print_PhoneNo(self):
        """

        :return: Prints instructor's Mobile number
        """
        print("Instructor's Mobile number:", self.instructor_phoneNo)

def check(details):
    details.print_EmailID()
    details.print_PhoneNo()

"""
object5S = Student_ContactDetails()
object5I = Instructor_ContactDetails()

object5S.print_EmailID()
#object5S.print_PhoneNo()
#object5I.print_EmailID()
#object5I.print_PhoneNo()

check(object5I)
#check(object5S)
"""
###########################################################################################################################################################################
# Example 06: Affiliate class
class Affiliate:
    _affiliateName = ""
    stepsToBecomeMember = ""
    def __init__(self, affiliateName):
        """

        :param affiliateName: Affiliate's Name
        """
        try:
            logging.info("Affiliate's Name: %s", str(affiliateName))
            if type(affiliateName) != str:
                raise (String_Exception("Entered name is not in string type."))
            else:
                self._affiliateName = affiliateName

        except Exception as e:
            logging.exception("Exception:" + str(e))
            self._affiliateName = ""

    def BecomeMember(self, affiliateName, stepsToBecomeMember):
        """

        :param stepsToBecomeMember: describes how many steps are needed to become a member
        :param affiliateName: Name of affiliate
        :return: Affiliate name
        """
        try:
            logging.info("Affiliate's Name: %s", stepsToBecomeMember)
            if type(stepsToBecomeMember) != int:
                raise (Integer_Exception("Entered name is not in integer."))
            else:
                self.stepsToBecomeMember = stepsToBecomeMember

        except Exception as e:
            logging.exception("Exception:" + str(e))
            self.stepsToBecomeMember = ""
        print("Affiliate Name:", self._affiliateName)
        print("Total steps requires to become an member", stepsToBecomeMember)

"""
object6 = Affiliate("Sudhanshu Kumar")
object6.BecomeMember("Sudhanshu Kumar", 4)
"""
###########################################################################################################################################################################
# Example 07: Internship Class

class Internship:
    project_name = ""
    project_description = ""
    project_members = ""

    def __init__(self, project_name, project_description, project_members):
        """

        :param project_name: Internship Project Title
        :param project_description: Desciption of Project
        :param project_members: total number of students working together
        """
        try:
            logging.info("Project Name: %s", project_name)
            if type(project_name) != str:
                raise (String_Exception("The given input is not of string type."))
            else:
                self.project_name = project_name

            logging.info("Project description: %s", project_description)
            if type(project_description) != str:
                raise(String_Exception("Given Course is not of string type. Please enter a valid course."))
            else:
                self.project_description = project_description

            logging.info("Total project members %s", project_members)
            if type(project_members) != int:
                raise (Integer_Exception("Invalid member details.. Not in integer type. Please enter a valid count."))
            else:
                self.project_members = project_members

        except Exception as e:
            logging.exception("The Exceptions we have got:" + "\n" + str(e))
            self.project_name = ""
            self.project_description= ""
            self.project_members = ""

"""
project = Internship("Downscaling Methods", "Low resolution to high resolution", 2)
print("Project Name:",project.project_name)
print("Project Description:", project.project_description)
print("Project Members:", project.project_members)
"""

###########################################################################################################################################################################
# Example 08: Login class

class Student_LogIN:
    student_name = ""
    _student_email = ""
    __student_password = ""

    def __init__(self, student_name, student_email, student_password):
        """

        :param student_name: Student Name who have any iNeuron course
        :param student_email: student email address
        :param student_password: login password
        """
        try:
            logging.info("STudent Name: %s", student_name)
            if type(student_name) != str:
                raise (String_Exception("Please enter valid name."))
            else:
                self.student_name = student_name

            logging.info("STudent Email ID: %s", student_email)
            if type(student_email) != str:
                raise (String_Exception("Please enter valid email."))
            else:
                self._student_email = student_email

            logging.info("Student password: %s", student_password)
            if type(student_password) != str:
                raise (String_Exception("Please enter correct password."))
            else:
                self.__student_password = student_password

        except Exception as e:
            logging.exception("Exception:" + str(e))
            self.student_name = ""
            self._student_email = ""
            self.__student_password = ""

    def printStudent_LoginDetails(self):
        """

        :return: Student Login details
        """
        print(f"Student Name: { self.student_name}")
        print(f"Student EmailID: {self._student_email}")
        print(f"Student Password: {self.__student_password}")

    def Welcome_Note(self):
        print(f"Hola..! {self.student_name}, Welcome to iNeuron.")

"""
object8 = Student_LogIN("Komal Diwe", "kdiwe@gmail.com", "ghsyghsbk845")
object8.Welcome_Note()
object8.printStudent_LoginDetails()
"""