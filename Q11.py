def fix_dict(d):
    new_dict = {}

    for key,value in d.items():
        if value not in new_dict:
            new_dict[value] = []
        new_dict[value].append(key)

    return new_dict

d ={
    "Mubashir": "Name",
    "31": "Age",
    "Male": "Sex",
    "Pilot": "Job",
    "Matt": "Name",
    "40": "Age",
    "Programmer": "Job"
}

print(fix_dict(d))