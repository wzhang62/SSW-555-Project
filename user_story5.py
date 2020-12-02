#user story5: Each family member's name and date of marriage are unique and do not repeat with other families.

def unique_family(family):
    family_list = []
    for i in family.values():
        if (i.Married,i.Husband_Name,i.Wife_Name) not in family_list:
            family_list.append((i.Married, i.Husband_Name, i.Wife_Name))
        else:
            print("ERROR: same spouse name and marriage date has already in GEDCOM!")

        if (i.Married,i.Husband_Name) not in family_list:
            family_list.append((i.Married, i.Husband_Name))
        else:
            print("ERROR: same husband name and marriage date has already in GEDCOM!")

        if (i.Married,i.Wife_Name) not in family_list:
            family_list.append((i.Married, i.Wife_Name))
        else:
            print("ERROR: same wife name marriage date has already in GEDCOM!")
