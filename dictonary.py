student = {'name':'alice','age':25,'grade':'a',}
print(dict(student))
print(student.values())
for key,value in student.items():
    print(f"{key}:{value}")
for age in student:
    print("age is key in student")


squares = {num: num**2 for num in range(1,6)}
squares1 = {num: num**3 for num in range(1,6)}
print(squares)
print(squares1)

dict={0:10,1:20}
dict[2]=30
print(dict)
#question-3
d={'x':10,'y':20,'z':30}
for key,value in d.items():
    print(f"{key}:{value}")
#question-4
n=int(input("give a number"))
sample={n:n*n for n in range(1,n+1)}
print(dict(sample))
#question-5
n=15
dict = {n:n**2 for n in range(1,n+1)}
print(dict)
