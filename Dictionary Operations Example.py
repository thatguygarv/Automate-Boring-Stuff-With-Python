student = {
    "Name": "Garv",
    "GPA": 6.9,
    "Year": 2024
}

student["GPA"] = 6.9
student["skills"] = ["Python", "Linux"]

for key, value in student.items():
    print(f"{key}: {value}")
