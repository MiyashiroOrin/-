import random
import numpy as np
import pandas as pd
import CreateData
CueValidStudent=np.zeros((5,90),dtype=int)
CueInvalidStudent=np.zeros((5,90),dtype=int)
LowGpa=np.zeros((5,90),dtype=float)
LowGpa13=[[]for i in range(5)]
CueStudent=[[]for i in range(5)]
AllStudentGPA=np.zeros((5,90),dtype=int)
AllStudentAttendance=np.zeros((5,90,20),dtype=int)
AllStudentGPA=CreateData.CreateStudentGpa()
AllStudentAttendance=CreateData.CreateAttendanceResult()
def CreateLowGpaStudent():
    for CourseId in range(0,5):
        LowGpa[CourseId] = sorted(AllStudentGPA[CourseId])  # 对AllStudengGpa进行排序
        for GpaStudent in LowGpa[CourseId]:
            if GpaStudent >= 1.0:
                break
            else:
                LowGpa13[CourseId].append(GpaStudent) #填入gpa小于1.2的gpa数组
        for StudentId in range(0, 90):
            if AllStudentGPA[CourseId][StudentId] in LowGpa13[CourseId]:
                CueStudent[CourseId].append(StudentId)     # 找出gpa小于1.2的学生id,填入数组
def DianMing():
    for CourseId in range(0, 5):
        LastValidStudentId =[]
        for CourseNo in range(0,20):
            CueStudentNum=8 #点到缺勤人数
            while CueStudentNum>0:
                if len(LastValidStudentId)>0: #当以往缺勤学生数组有数据时
                    for CueStudentId in LastValidStudentId: #遍历以往缺勤学生数组
                        if CueValidStudent[CourseId][CueStudentId]>15: #已缺勤16次的学生不点名
                            LastValidStudentId.remove(CueStudentId)
                            continue
                        if CueInvalidStudent[CourseId][CueStudentId]>4: #已点名在课4次以上的学生不点名
                            LastValidStudentId.remove(CueStudentId)
                            continue
                        if AllStudentAttendance[CourseId][CueStudentId][CourseNo]==1: #点到缺勤学生
                            AllStudentAttendance[CourseId][CueStudentId][CourseNo]=2 #将其该课时缺勤情况改为2代表有效点名
                            CueValidStudent[CourseId][CueStudentId]=CueValidStudent[CourseId][CueStudentId]+1 #记录该学生有效点名次数
                            CueStudentNum=CueStudentNum-1 #成功点到一名缺勤学生
                            if CueStudentNum==0:
                                break
                        if AllStudentAttendance[CourseId][CueStudentId][CourseNo] == 0: #点到到课学生
                            AllStudentAttendance[CourseId][CueStudentId][CourseNo] =3 #将其该课时缺勤情况改为3代表无效点名
                            CueInvalidStudent[CourseId][CueStudentId]=CueInvalidStudent[CourseId][CueStudentId]+1 #记录该学生无效点名次数
                for CueStudentId in CueStudent[CourseId]: #在以往缺勤学生数组外点名
                    if AllStudentAttendance[CourseId][CueStudentId][CourseNo]<2: #排除已被点名的学生
                        if CueStudentId in LastValidStudentId: #排除以往缺勤学生数组内的学生id（可删，与上一行作用一致
                            continue
                        if CueValidStudent[CourseId][CueStudentId]>15: #已缺勤16次的学生不点名
                            continue
                        if CueInvalidStudent[CourseId][CueStudentId]>4: #已点名在课4次以上的学生不点名
                            continue
                        if AllStudentAttendance[CourseId][CueStudentId][CourseNo] == 1:
                            AllStudentAttendance[CourseId][CueStudentId][CourseNo] = 2
                            CueValidStudent[CourseId][CueStudentId] = CueValidStudent[CourseId][CueStudentId] + 1
                            LastValidStudentId.append(CueStudentId) #加入以往缺勤学生数组名单
                            CueStudentNum = CueStudentNum - 1
                            if CueStudentNum == 0:
                                break
                        if AllStudentAttendance[CourseId][CueStudentId][CourseNo] == 0:
                            AllStudentAttendance[CourseId][CueStudentId][CourseNo] = 3
                            CueInvalidStudent[CourseId][CueStudentId] = CueInvalidStudent[CourseId][CueStudentId] + 1
                break; #遍历gpa小于1.2的学生名单，即使没点满5人，仍结束点名，避免后期死循环

def CreateDianmingList():
    for CourseId in range(0, 5):
        for CourseNo in range(0, 20):
            DianMingList = []
            print(f'第{CourseId + 1}门课程第{CourseNo + 1}课时的点名方案：')
            for StudentId in range(0, 90):
                if AllStudentAttendance[CourseId][StudentId][CourseNo] > 1:
                    DianMingList.append(StudentId)
            print(DianMingList)

def CreateE():
    ValidSum=0
    InvalidSum=0
    for CourseId in range(0,5):
        for CourseNo in range(0,20):
            for StudentId in range(0,90):
                if AllStudentAttendance[CourseId][StudentId][CourseNo]==2:
                    ValidSum=ValidSum+1
                if AllStudentAttendance[CourseId][StudentId][CourseNo]==3:
                    InvalidSum=InvalidSum+1
    E=ValidSum/(ValidSum+InvalidSum)
    round(E,5)
    print(E)

