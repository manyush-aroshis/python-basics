student = {
    "name": "Manyush",
    "year": 2
}

student["branch"] = "CSE"
student["year"] = 3

student.update({"college": "SUIIT"})

print(student)

student.pop("year")

print("After removing year:", student)