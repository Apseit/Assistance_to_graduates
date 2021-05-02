import os
from typing import Dict, List, Tuple

import sqlite3

conn = sqlite3.connect(os.path.join("db", "finance.db"))
cursor = conn.cursor()


def select(univer):
    univer = univer.replace("__", "-")
    univer = univer.replace("_", ".")
    cursor.execute(f"SELECT * FROM univer WHERE univer_email = '{univer}'")
    rows = cursor.fetchall()
    faculty = select_faculty(rows[0][1])
    result = []
    for i in rows[0]:
        result.append(i)
    result.append(faculty)
    return result


def select_all():
    cursor.execute(f"SELECT * FROM univer")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        email = str(row[0])
        email = email.replace(".", "_")
        email = email.replace("-", "__")
        print(email)
        result.append([row[1], email])
    return result


def select_faculty(uni_name):
    print(uni_name)
    cursor.execute(f"SELECT faculty_name FROM faculty WHERE faculty_uni = '{uni_name}'")
    return cursor.fetchall()