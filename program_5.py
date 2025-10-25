# David Stalmakov, 10/24/2025
# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

courses = {}

# Get Info
while True:
    course_id = input("Enter course ID (or done to finish): ").strip()
    if course_id.lower() == "done":
        break
    course_name = input(f"Enter course name for {course_id}: ").strip()
    courses[course_id] = course_name

subject = input("Enter a subject code example (COS): ").strip()

print(f"Courses with subject '{subject}' are:")

found = False
for course_id, course_name in courses.items():
    if course_id.upper().startswith(subject):
        print(f"{course_id}: {course_name}")
        found = True
if not found:
    print(f"No course with subject '{subject}' found.")
