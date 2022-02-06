

course1 = {
    "Room Number":"3004",
    "Instructor":"Haynes",
    "Meeting time":"8:00 a.m."

}

course2 = {
    "Room Number":"4501",
    "Instructor":"Alvarado",
    "Meeting time":"9:00 a.m."
}

course3 = {
    "Room Number":"6755",
    "Instructor":"Rich",
    "Meeting time":"10:00 a.m."
}

course4 = {
    "Room Number":"1244",
    "Instructor":"Burke",
    "Meeting time":"11:00 a.m."
}

course5 = {
    "Room Number":"1411",
    "Instructor":"Lee",
    "Meeting time":"1:00 p.m."
}


courses = {
    "CS101":course1,
    "CS102":course2,
    "CS103":course3,
    "NT110":course4,
    "CM241":course5
}

txt = input("Please enter a course number: ")


if txt in courses:
    print(courses[txt])
else:
    print(txt, "is not in the courses dictionary")
    



