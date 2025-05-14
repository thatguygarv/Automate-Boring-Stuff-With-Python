subjects = ["Math", "Python", "Cloud", "AI"]
subjects.append("ML")
subjects.remove("Math")
subjects.insert(1, "Data Structures")

for subject in subjects:
    print("Enrolled in:", subject)
