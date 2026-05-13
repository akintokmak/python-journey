# student_score = {
#     "Akin": 100,
#     "Sule": 97,
#     "Sibel": 80,
#     "Ayla": 80,
#     "Erenay":50
# }

import random
names = ["Akin","Sule","Sibel","Ayla","Erenay"]
student_scores = {student:random.randint(50,100) for student in names}
print(student_scores)
passed_students = {student:score for (student,score) in student_scores.items() if score > 70}
print(passed_students)

#----------------------------------------------------------------------------------------------------------------------
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
new_list = sentence.split()
result = {word:len(word) for word in new_list}
print(result)

#----------------------------------------------------------------------------------------------------------------------
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}
print(weather_f)

