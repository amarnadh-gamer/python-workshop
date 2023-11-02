color_dict={'red': '#FF0000', 'green': '#008000', 'black': '#000000', 'white': 'FFFFFF'}
color_dict1={}
x=color_dict.keys()
l_ist=[]
for i in x:
    l_ist.append(i)
l_ist1=sorted(l_ist)
for j in l_ist1:
    color_dict1[j] = color_dict[j]
print(color_dict1)
print(type(color_dict1))