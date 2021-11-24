import os
import openpyxl
import shutil
import pandas as pd
import regex as re

input_file_1 = "studentinfo.csv"
input_file_2 = "course_master_dont_open_in_excel.csv"
input_file_3 = "course_registered_by_all_students.csv"
input_file_4 = "course_feedback_submitted_by_students.csv"


def feedback_not_submitted():

    ltp_mapping_feedback_type = {1: 'lecture', 2: 'tutorial', 3: 'practical'}
    output_file_name = "course_feedback_remaining.xlsx"
    d1 = {}
    d2 = {}
    # collecting student information
    student_info = pd.read_csv(input_file_1)
    for i in range(len(student_info)):
        name = student_info.loc[i, "Name"]
        contact = student_info.loc[i, "contact"]
        aemail = student_info.loc[i, "aemail"]
        roll_number = student_info.loc[i, "Roll No."]
        email = student_info.loc[i, "email"]

        d1[roll_number] = {'subjects': {}, 'name': name,
                           'email': email, 'aemail': aemail, 'contact': contact}

    # courses registered in the
    courses_registered = pd.read_csv(input_file_3)
    for i in range(len(courses_registered)):
        roll_number = courses_registered.loc[i, "rollno"]
        subject_number = courses_registered.loc[i, "subno"]
        register_sem = courses_registered.loc[i, "register_sem"]
        schedule_sem = courses_registered.loc[i, "schedule_sem"]
        if roll_number not in d1:
            d1[roll_number] = {'subjects': {}, 'name': 'NA_IN_STUDENT_INFO',
                               'email': 'NA_IN_STUDENT_INFO', 'aemail': 'NA_IN_STUDENT_INFO', 'contact': 'NA_IN_STUDENT_INFO'}
            d1[roll_number]['subjects'][subject_number] = {
                'ltp': [], 'register_sem': register_sem, 'schedule_sem': schedule_sem}

    # collecting ltp
    course_master = pd.read_csv(input_file_2)
    for i in range(len(course_master)):
        subject_number = course_master.loc[i, "subno"]
        ltp = course_master.loc[i, "ltp"].split('-')
        if subject_number in d2:
            continue
        d2[subject_number] = []
        for p, q in enumerate(ltp):
            if q != '0':
                d2[subject_number].append(p+1)

    # feedback
    feedback = pd.read_csv(input_file_4)
    for i in range(len(feedback)):
        roll_number = feedback.loc[i, "rollno"]
        subject_number = feedback.loc[i, "subno"]
        feedback_type = feedback.loc[i, "feedback_type"]
        if roll_number not in d1:
            continue
        if len(d2[subject_number]) == 0:
            continue

        if feedback_type not in d1[roll_number]['subjects'][subject_number]['ltp']:
            d1[roll_number]['subjects'][subject_number]['ltp'].append(
                feedback_type)

    # putting into output folder
    if not os.path.exists(output_file_name):
        wb = openpyxl.Workbook()
    else:
        wb = openpyxl.load_workbook(output_file_name)
        ws = wb['Sheet']
        ws.append(["rollno", "register_sem", "schedule_sem",
                  "subno", "Name", "email", "aemail", "contact"])
        for roll_number in d1:
            for subject in d1[roll_number]['subjects']:
                subno = str(subject)
                d1[roll_number]['subjects'][subject_number]['ltp'].sort()
                if d1[roll_number]['subjects'][subject_number]['ltp'] == d2[subject_number]:
                    continue
                name = d1[roll_number]['name']
                email = d1[roll_number]['email']
                aemail = d1[roll_number]['aemail']
                contact = d1[roll_number]['contact']
                register_sem = d1[roll_number]['subjects'][subject_number]['register_sem']
                schedule_sem = d1[roll_number]['subjects'][subject_number]['schedule_sem']

                ws.append([roll_number, register_sem, schedule_sem,
                          subno, name, email, aemail, contact])
            wb.save(output_file_name)


feedback_not_submitted()
