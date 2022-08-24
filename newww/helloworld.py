# # # # # # greeting = 'hello'
# # # # # # name = input('please enter your name')
# # # # # # print(greeting +'' + name)
# # # # # #
# # # # # # splitString = 'this string has been\nsplit over\nseveral times'
# # # # # # print(splitString)
# # # # # # splitString = 'this string has been\tsplit over\tseveral times'
# # # # # # print(splitString)
# # # # # #print('the pet shop owner said e\'s uh,...he\'s resting')
# # # # #
# # # # #  # msplitString = """this string has beensplit overseveral times"""
# # # # #  # print(splitString)
# # # # # greetings = ' faatihat is '
# # # # # age = 20
# # # # # print((greetings) +''+str(age))
# # # # a = 10
# # # # b = 5
# # # # print(a/b)
# # # # print(a//b)
# # # # print(a%b)
def someinfo():
    for i in range(1, 4):
        print(i)
    HerName = "faatihat"
    print(HerName[-1])
    print(HerName[0:4])
    print(HerName[0:3:2])
    print(HerName[0:4:4])
# # # stringsFormatting
# # age=24
# # print('my age is ' + str(age)+' '+'years')
# # print('my age is {0} years'.format(age))
# # print('i am the girl {0} {1} diffrent {2}'.format('with', 10, 'guys'))
# # girl='faatihat'
# # surname='mohammed'
# # most_favourite="barakat"
# # dream="to be very rich inshaAllah"
# # how= 'still figuring out'
# # Age=20
# # print(girl+' '+'is in love with'+' '+ most_favourite
# #       +dream+'is what shes'+how)
# # greg='looking so beautiful, i dont deserve this \n baby iii dancing in the dark\t with you between my arms'
# # print(greg)
# # print('my age is %d years'%age)
# # print('my age is %d i attend %s school'%(age, most_favourite))
# # # %s= strings and %d= integer
# #
# #
# name = input('please enter yur name')
# age = int(input('how old are you {0}'.format(name)))
# # print(age)
# if age >= 18:
#     print('you are old enough to vote')
# else:
#     print('please come back in {0} years'.format(18-age))
#     print('thank you')
# guess = int(input('please guess a number'))
# if guess < 5:
#     print('please guess higher')
#     guess = int(input('put another number'))
#     if guess == 5:
#         print('you\'ve guessed correctly')
#     else:
#         print('you\'ve guessed wrongly')
#         # guess = int(input('try another number'))
# elif guess > 5:
#     print('please guess lower')
#     guess = int(input('put another number'))
# else:
#
#     print('you guessed a number greater than five')
# '''arithmetic operators '''


word = 'tell'
for i in word:
    n = word[::-1]
print(n)

def sum(x,y):
    return x+y

def minus(a,b):
    return a-b