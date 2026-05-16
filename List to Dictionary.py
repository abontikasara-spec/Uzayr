def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [[1, "Jean Castro", "V"], [2, "Luna Powell", "V"], [3, "Brian Howell", "VI"], [4, "Lynne Foster", "VI"], [5, "Zach Smith", "VII"]]

print("\nOriginal list of lists :")
print(students)
print("\nConverted lists a dictionary :")
print(test(students))