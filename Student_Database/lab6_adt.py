##############################
# -------------------------- #
# Student Abstract Data Type #
# -------------------------- #
##############################


####################################################################        
### def make_student(sid,fname,lname,dob_yy,dob_mm,dob_dd):      ###
####################################################################        
### ADD CODE FOR Problem 1a                                      ###
###                                                              ###
### A student record contains a tuple of a tag 'student' and the ###
### the student data as a list.                                  ###
### Define the constructor  make_student  that takes arguments   ###
### student id, first name, last name, date of birth year, month,###
### day, uses  make_name  to create the name list to be included ###
### in the record, uses  make_date  to create the date of birth  ###
### tuple, inserts 0 for the number of courses, and empty list   ###
### for the list of courses.                                     ###
###                                                              ###
####################################################################

def make_student(id, first_name, last_name, yyyy, mm, dd):
    return ('student', [id, make_name(first_name, last_name), make_date(yyyy, mm, dd), 0, []])

def make_name(fname, lname):
    return [fname, lname]


def make_date(yyyy, mm, dd):
    return (yyyy, mm, dd)


def make_course(ccode, cgrade):
    return (ccode, cgrade)


def stud_data(std):
    return std[1]


def student_id(std):
    """Returns students ID"""
    return stud_data(std)[0]


def student_name(std):
    """Returns students Name"""
    return stud_data(std)[1]


def student_dob(std):
    """Returns students Date"""
    return stud_data(std)[2]


def student_no_of_courses(std):
    """Returns students number of courses"""
    return stud_data(std)[3]


def student_courses(std):
    """Returns a list of tuples of course codes and grade"""
    return stud_data(std)[4]


def student_fname(name):
    """Returns first name"""
    return name[0]


def student_lname(name):
    """Returns last name"""
    return name[1]


def get_ccode(course_det):
    """Returns course code part of the tuple"""
    return course_det[0]


def get_grade(course_det):
    """Returns grade part of the tuple"""
    return course_det[1]


def date_yyyy(date):
    return date[0]


def date_mm(date):
    return date[1]


def date_dd(date):
    return date[2]


def is_student(obj):
    return type(obj) == type(()) and obj[0] == 'student' and type(obj[1]) == type([])


def has_no_course(std):
    return get_courses(std) == []


def update_no_of_courses(std, no):
    std[1][3] = no
