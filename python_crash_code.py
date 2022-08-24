# names = ['faatihat', 'tomiwa', 'mavel']
# print(names[0].title())
# print('my first name is {}'.format(names[0].title()))
# wants = ['cars','money','peace','piece']
# print('she told me she want  {}, {} and she\'ll need {} most especially'.format(wants[0],wants[1],wants[2]))
# wants[0]='faatihat'
# print(wants)
# print('she told me she want  {}, {} and she\'ll need {} most especially'.format(wants[0],wants[1],wants[2]))
# wants.append('prince')
# names.insert(0, 'cabir')
# names.insert(3, 'cabir')
# del names[3]
# names.pop()
# print(names)
# boys = ['abdul','cabir','adams','adam','abdullah','hayat']
# print(boys)
# boys.sort()
# print(boys)
# boys.reverse()
# print(boys)
# for boy in boys:
#     print(boy.title()+' '+ 'please try again later')
lizt = [1,2,3,4,5,6,7,8,9,10]
print(sum(lizt))
print(min(lizt))
print(max(lizt))
print((lizt[0:4]))
# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# elif age >= 65:
#     price = 5
# print("Your admission cost is $" + str(price) + ".")

# alien= {'color':'green', 'points':5}
# print(alien['color'])
# print(alien['points'])
# alien['fshape']='oval'
# print(alien)


def full_name(first_name, last_name):
    person = first_name +" "+ last_name
    return person

# while True:
#     print('Thank you for choosing us!')
#     first_name = input('enter your first name')
#     last_name = input('enter your last name')
#     print('You\'re welcome!',full_name(first_name,last_name))


def say_hello():
    greeting = 'hello dear'+" "+name
    return  greeting

user_name = ['faatihat','hanifa','toshiba']
for name in user_name:
    print(say_hello())

def food(*types): """prints arbitrary inputs in tuple format"""
print('i want')

food('rice','b','te','er','hdh')
numbers = [
    [34,63,88,71,29],
    [90,78,51,27,45],
    [63,37,85,46,22],
    [51,22,34,11,18]
]

f = numbers[0]
l= len(f)
average1 = f / l
# print(average)