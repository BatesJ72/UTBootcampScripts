dict1 = {
    "Name": "Jessica", 
    "Age": 32, 
    "Hobbies": ["Walking dogs", "Hiking"], 
    "WakeUpTime": {
        "M-F": "6", 
        "Sat-Sun": "8"
    }
}

print(f"My name is {dict1['Name']}, I have {len(dict1['Hobbies'])} hobbies, and I wake up at {dict1['WakeUpTime']['M-F']} on weekdays.")