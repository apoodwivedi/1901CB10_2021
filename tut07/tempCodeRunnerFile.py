import os
import openpyxl
import shutil
import pandas as pd
import regex as re

dict1 = {}
dict2 = {}


def student():
    df = pd.read_csv('studentinfo.csv')
    for i in range(len(df)):
        rolln = df.loc[i, "Roll No."]
        email = df.loc[i, "email"]
        aemail = df.loc[i, "aemail"]
        contact = df.loc[i, "contact"]
        name = df.loc[i, "Name"]

        dict1[rolln] = {'subjects': {}, 'name': name,
                        'email': email, 'aemail': aemail, 'contact': contact}
        return


def course_master():
    df = pd.read_csv('course_master_dont_open_in_excel.csv')
    for i in range(len(df)):
        subno = df.loc[i, "subno"]
        ltp = df.loc[i, "ltp"].split('-')
        if subno in dict2:
            continue
        dict2[subno] = []
        for j, s in enumerate(ltp):
            if s != '0':
                dict2[subno].append(j+1)


def course_registered():
    df = pd.read_csv('course_registered_by_all_students.csv')
    for i in range(len(df)):
        rolln = df.loc[i, "rollno"]
        subno = df.loc[i, "subno"]
        register_sem = df.loc[i, "register_sem"]
        schedule_sem = df.loc[i, "schedule_sem"]
        if rolln not in dict1:
            dict1[rolln] = {'subjects': {}, 'name': 'NA_IN_STUDENT_INFO',
                            'email': 'NA_IN_STUDENT_INFO', 'aemail': 'NA_IN_STUDENT_INFO', 'contact': 'NA_IN_STUDENT_INFO'}
            dict1[rolln]['subjects'][subno] = {
                'ltp': [], 'register_sem': register_sem, 'schedule_sem': schedule_sem}


def feedback():
    df = pd.read_csv('course_feedback_submitted_by_students.csv')
    for i in range(len(df)):
        rolln = df.loc[i, "rollno"]
        subno = df.loc[i, "subno"]
        feedback_type = df.loc[i, "feedback_type"]
        if rolln not in dict1:
            continue
        if len(dict2[subno]) == 0:
            continue

        if feedback_type not in dict1[rolln]['subjects'][subno]['ltp']:
            dict1[rolln]['subjects'][subno]['ltp'].append(feedback_type)


def correlate(output_file):
    if not os.path.exists(output_file):
        wb = openpyxl.Workbook()
    else:
        wb = openpyxl.load_workbook(output_file)
        ws = wb['Sheet']
        ws.append(["rollno", "register_sem", "schedule_sem",
                  "subno", "Name", "email", "aemail", "contact"])
        for rolln in dict1:
            for subject in dict1[rolln]['subjects']:
                subno = str(subject)
                dict1[rolln]['subjects'][subno]['ltp'].sort()
                if dict1[rolln]['subjects'][subno]['ltp'] == dict2[subno]:
                    continue
                register_sem = dict1[rolln]['subjects'][subno]['register_sem']
                schedule_sem = dict1[rolln]['subjects'][subno]['schedule_sem']
                name = dict1[rolln]['name']
                email = dict1[rolln]['email']
                aemail = dict1[rolln]['aemail']
                contact = dict1[rolln]['contact']

                ws.append([rolln, register_sem, schedule_sem,
                          subno, name, email, aemail, contact])
            wb.save(output_file)


def feedback_not_submitted():

    ltp_mapping_feedback_type = {1: 'lecture', 2: 'tutorial', 3: 'practical'}
    output_file_name = "course_feedback_remaining.xlsx"
    student()
    course_master()
    course_registered()
    feedback()
    correlate(output_file_name)


feedback_not_submitted()
