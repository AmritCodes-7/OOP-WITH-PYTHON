# schecking the name in the namelist

namelist = ["amrit", "auraj", "rohan"]
name = input("Enter a name: ")

if name in namelist:
    print(name + " is present in the namelist.")
else:
    print(name + " is not present in the namelist.")
   
