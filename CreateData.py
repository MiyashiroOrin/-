import random
import numpy as np
import pandas as pd
AllStudentAttendance = np.zeros((5, 90, 20), dtype=int)
AllStudentGPA = np.zeros((5, 90), dtype=float)
def CreateStudentGpa():
    for CourseId in range(0, 5):  # 以正态分布为规则生成每个学生对每门课的绩点
        AllStudentGPA[CourseId] = np.random.normal(loc=2.0, scale=0.7, size=90)
        for StudentId in range(0, 90):
            if AllStudentGPA[CourseId][StudentId] > 4.0:
                AllStudentGPA[CourseId][StudentId] = 4.0
            if AllStudentGPA[CourseId][StudentId] < 0:
                AllStudentGPA[CourseId][StudentId] = 0
    return AllStudentGPA
def CreateAbsenceStudent5_8():
    for CourseId in range(0, 5):
        Count5_8 = random.randint(5, 8)
        AllCourseAbsenceStudentId=[]
        Line0=[]# 生成每个课程中80%缺勤的5-8人，他们只会产生在绩点倒数的人中
        for x in range(0,90):
            if AllStudentGPA[CourseId][x]<=1.0:
                Line0.append(x)
        if len(Line0)<Count5_8:
            Count5_8=len(Line0)
        StudentLine=random.sample(Line0,Count5_8)
        for x in range(0,Count5_8):
            AllCourseAbsenceStudentId.append(StudentLine[x])
        for StudentId in AllCourseAbsenceStudentId:  # 使得这5-8人产生缺勤记录
            CourseNoSum5_8 = 16
            Line1=[]
            for x in range(0,20):
                Line1.append(x)
            StudentLine1=random.sample(Line1,CourseNoSum5_8)
            for x in range(0,CourseNoSum5_8):
                AllStudentAttendance[CourseId][StudentId][StudentLine1[x]]=1
def CreateAbsenceStudent0_3():
    for CourseId in range(0, 5):
        for CourseNo in range(0, 20):  # 产生0-3个幸运观众并使其缺勤
            Count0_3 = random.randint(0, 3)
            while Count0_3 > 0:
                StudentId = random.randint(0, 89)
                if AllStudentAttendance[CourseId][StudentId][CourseNo] == 0:
                    AllStudentAttendance[CourseId][StudentId][CourseNo] = 1
                    Count0_3 = Count0_3 - 1
def CreateAttendanceResult():
    CreateAbsenceStudent5_8()
    CreateAbsenceStudent0_3()
    return AllStudentAttendance
def CreateCsv():
    CsvFrame0 = pd.DataFrame(AllStudentAttendance[0])
    CsvFrame0.to_csv("data0.csv")
    CsvFrame1 = pd.DataFrame(AllStudentAttendance[1])
    CsvFrame1.to_csv("data1.csv")
    CsvFrame2 = pd.DataFrame(AllStudentAttendance[2])
    CsvFrame2.to_csv("data2.csv")
    CsvFrame3 = pd.DataFrame(AllStudentAttendance[3])
    CsvFrame3.to_csv("data3.csv")
    CsvFrame4 = pd.DataFrame(AllStudentAttendance[4])
    CsvFrame4.to_csv("data4.csv")

