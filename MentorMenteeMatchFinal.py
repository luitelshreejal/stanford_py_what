import pywhatkit as pwk
import pandas as pd
import time
import faker
import faker
import random
import tools

#Script is used to create a groupchat between Mentor/ Mentee

# Initialize the Faker library
fake = faker.Faker()

# Create data with first and last names
data = {
    "Name_y": [fake.name() for _ in range(30)],
    "Email": [f"name_{i}@example.com" for i in range(1, 31)],
    "Phone Number": ["256" + str(random.randint(100000000, 999999999)) for _ in range(30)],
    "mentor_email": [f"mentor{i}@example.com" for i in range(1, 31)]
}

# Create DataFrame
df_to_text = pd.DataFrame(data)
df_to_text

df_to_text['Name'] = df_to_text['Name_y'].str.split().str[0].str.lower().str.capitalize()

df_to_text['Phone Number'] = df_to_text['Phone Number'].astype(int)


dictionary_people_to_text = df_to_text[['Phone Number', 'Name', 'mentor_email']].set_index('Phone Number').apply(tuple, axis=1).to_dict()

dictionary_people_to_text = {f'+{phone_number}': (name, email) for phone_number, (name, email) in dictionary_people_to_text.items()}
dictionary_people_to_text

def find_index_of_key(my_dict, key_to_find):
    for index, key in enumerate(my_dict.keys()):
        if key == key_to_find:
            return index
    return None  # Key not found

current_time = time.localtime()

# Extract the hour and minute components
hours = current_time.tm_hour
minutes = current_time.tm_min + 1

contacted_people = set()

for phone_number, (name, email) in dictionary_people_to_text.items():
    
    if phone_number not in contacted_people:
        message = "Hello {}, We noticed that you submitted Homework 3 but not Homework 2 yet. Please submit this forms to complete Homework 2 immediately (since it's overdue): https://forms.gle/xx".format(name)
        print(name, email, phone_number)
        print('Number of people left: {}'.format(len(dictionary_people_to_text) - find_index_of_key(dictionary_people_to_text, phone_number) - 1))
        pwk.sendwhatmsg(phone_number, message, hours, minutes)

        contacted_people.add(phone_number)

        if minutes < 59:
            minutes += 1
        else:
            hours+=1
            minutes = 0
