employee = ["Awan", "Star Curl", "Steve Job"]

empTotal = len(employee)

print(employee)
print(employee[1])
print(empTotal)

employee.append("Elon Musk")

print(employee)

employee.remove("Star Curl")

print(employee)

employee.pop(1)

print(employee)

newEmp = employee.copy()

print(newEmp)

print(newEmp.count("Awan"))

newEmp.insert(1, "Laura Heln")

print(newEmp)

newEmp.sort()

print(newEmp)

newEmp.reverse()

print(newEmp)