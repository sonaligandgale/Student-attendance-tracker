# Student Attendance Tracker Program

classes_held = int(input("Enter total classes held: "))
classes_attended = int(input("Enter total classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100

print("Classes Held:", classes_held)
print("Classes Attended:", classes_attended)
print("Attendance: {:.2f}%".format(attendance_percentage))
