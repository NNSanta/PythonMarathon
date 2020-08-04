a = ['a','b','c','d']
print (a)
a.insert(0,'z')
print("List after adding a new value: ", a)


# del a[4]
# print("List after deleting data : ", a)
# del a[3]
# print("List after deleting data : ", a)

a.sort(reverse=True)
print("List sorted desc:" , a)
b = a[2:]
print("Copied list b = ",b)