#string
a="Python"
print(a[:3])

print(a.upper())
print(a.lower())

a="Python".join(["a","b"])
print(a)

a=a.replace("P","T")
print(a)

print(a.split())
print(a.count("T"))

set1={1,2,3,4,5}
set2={4,5,6,7,8}

print(f"Union of both:{set1.union(set2)}")
print(f"intersection of both:{set1.intersection(set2)}")
print(f"Difference of both:{set1.difference(set2)}")
print(f"Symmetric difference of both:{set1.symmetric_difference(set2)}")

Dictonary={"Name":"Shreyash","Age":18,"City":"Mumbai"}
print(f"My Dictonary,Dictonary")

print(f"Name:{Dictonary["Name"]}")

Dictonary["Occupation"]="Engineer"
print(f"My modified dictionary",Dictonary)

del Dictonary["Age"]
print(f"New Dictionary:",Dictonary)