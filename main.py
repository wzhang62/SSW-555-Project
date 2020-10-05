key_words = ['INDI','NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM',
'MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE']
levels = ['1','2','3']
text_file = open('export-BloodTree.ged', 'r')


y = '000'
lerp = '000'
derp = '000'

def gedcom_reader_func(gedcom.ged):
  for line in text_file:
    level_number = line[:1]
    line = line.split()
    for word in key_words:
        if word in line:
        derp = word
        y = 'Y'

    for burb in levels:
        if burb in line:
          lerp = burb
    print('<-- |' + derp + '|' + lerp + '|' + y)
    print("-->", line)

##This is user story to add functionality to print all males in a genealogy (Sprint 1)
def males_in_family(gedcom.ged):
  if line[1] == "NAME":
    name = line[2]
  while line[2] != "M" or line[2] != "F":
    if line[2] == "M":
      print(name)

##This user story prints all the females of a family.
  if line[1] == "NAME":
    name = line[2]
  while line[2] != "M" or "F":
    if line[2] == "F":
      print(name)
"""
##Will print all the children of a family tree, may need to be separate function.
    if line[1] == "CHIL":
      name = line
##Total number of deaths in the family

##Host database via MySQL or Sqlite
"""

