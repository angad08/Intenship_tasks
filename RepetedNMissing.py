def repetedNumber(a):
    # Returns the repeting number
    return max(a,key=a.count)
item=[1,3,4,6,2,1,5] #Original List of all items
for i in range(1,len(item)+1):
    if i not in item:
        missingValue=i #getting missing items
print(f"Repeted Number :{repetedNumber(item)}\nMissing Number :{missingValue}")