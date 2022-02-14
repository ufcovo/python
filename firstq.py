def dels(list1,list2):
    Length1=len(list1)
    Length2= len(list2)
    if Length1>Length2:
       newlist=list1[Length2:]
    elif Length1<Length2:
         newlist=list()
         newlist=list2[0]
         newlist.append(list1)
         list2.pop(0)
         newlist.append(list2)
    else:
         newlist=list()
    print(newlist)

l1 = input("Enter first list: ")
l2 = input ("Enter second list: ")
dels(l1,l2)
