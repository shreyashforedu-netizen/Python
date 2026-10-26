L1=[1,2,3,4,5,6]
L2=["Mumbai","Pune","Nashik"]
print(L1)
print(L2)

L3=print(L1+L2)

L3=L2+[9,8,7]
print(L3)

L4=[28,66,37,99]
L5=L4
print(L5)


L4=[28,66,37,99]
L5=[68,77]
L6=L4+L5
print(L6)

L6.sort()
print(L6)


Cars=["BMW","MERCEDESE","FERARRI","VOLSWEGEN","MARUTI"]
print(f"Cars Tuples:",Cars)

print(len(Cars))

print(f"Count of Lamborgini:",{Cars.count("Lamborgini")})

print(f"Index of Maruti",{Cars.index("MARUTI")})
print(f"Printing all:,{Cars[1:5]}")