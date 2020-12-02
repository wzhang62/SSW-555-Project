#user story4: I want to make sure that the parents are not too old, that they are within a certain age range of their children
from datetime import datetime

def age_diff(family,indi):
    for k, v in family.items():
        if v.Husband_ID != 'NA' and v.Wife_ID != 'NA':
            bd_father = datetime.strptime(indi[v.Husband_ID].Birthday, '%d %b %Y')
            bd_mother = datetime.strptime(indi[v.Wife_ID].Birthday, '%d %b %Y')
            for a in v.Children:
                if indi[a].Birthday != 'NA':
                    bd_child = datetime.strptime(indi[a].Birthday, '%d %b %Y')
                    if old_father(bd_father,bd_child) is True:
                        print(f"ERROR: US4: In family {k}，Husband {v.Husband_ID}'s age is more than 70 years old than his child {indi[a].ID}!")
                    if old_mother(bd_mother,bd_child) is True:
                        print(f"ERROR: US4: In family {k}, Wife {v.Wife_ID}'s age is more than 65 years old than her child {indi[a].ID}!")

def old_father(father, child):
    age_diff = (abs((father - child).days)) / 365
    if age_diff > 70:
        return True
    else:
        return False

def old_mother(mother,child):
    age_diff = (abs((mother - child).days)) / 365
    if age_diff > 65:
        return True
    else:
        return False