import sys
list=[]
list2=[]
list3=[]
list4=[]
list=['prachi',2.6,5,7,'mamata']
print("list is", list)
for x in list:
    if type(x)==int:
        list2.append(x)
    elif type(x)==float:
        list3.append(x)
    elif type(x)==str:
        list4.append(x)
    else:
          sys.exit("unclassified")
print("integers:",list2)
print("floats:",list3)
print("strings:",list4)