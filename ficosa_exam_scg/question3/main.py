import PySimpleGUI as sg


def menu():
    sql = """
            SELECT  t.name as Teacher, 
                    c.courseCode as CourseCode,
                    c.dayOfWeek as Day,
                    c.timeStart as Start,
                    c.timeEnd as End
            FROM Teacher t
            LEFT JOIN Classes c ON c.teacherID = t.id 
            """
    sg.popup(sql)
