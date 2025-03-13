# List of student dictionaries
students = [
    {
        "first_name": "Hasan",
        "last_name": "Yıldiz",
        "index_number": "57454"
    },
    {
        "first_name": "Ummu",
        "last_name": "Bozdemir",
        "index_number": "35449"
    },
    {
        "first_name": "Bob",
        "last_name": "Johnson",
        "index_number": "58606"
    }
]

# Loop to display each student's name and index number
print("Students List:")
for student in students:
    print(f"Name: {student['first_name']} {student['last_name']}, Index Number: {student['index_number']}")
