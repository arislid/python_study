my_tuple = ('sample', 4, 0x12)
print(my_tuple)
# del my_tuple[1] : error!
print(my_tuple[2])


person = { 'name': 'Sam',
  'age': 25,
  'profession': 'Programmer'
}

del person['profession']

# Output: {'name': 'Sam', 'age': 25}
print(person)



