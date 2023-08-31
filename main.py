# a = 'HI my dear man'
# print(a)
# print(5)
#
# line01 = "***********"
# line02 = "*         *"
# line03 = "* WELCOME *"
#
# print('')
# print(line01)
# print(line02)
# print(line03)
# print(line02)
# print(line01)
#
#
# first = "Dave"
# last = "Gray"
#
# print(type(first))
# print(type(first) == str)
# print(isinstance(first,str))
#
# pizza = str("paperoni")
# print(type(first))
# print(type(first) == str)
# print(isinstance(first,str))
#
# fullname = first + " " + last
# print(fullname)

# user = ['Dave','nina','Oleg']
# data = ['Dave',42,True]
# emptylist = []
# print("Dave" in emptylist)
#
# print(user[0])
# print(user[-2])
#
# print(user.index('nina'))
#
# print(user[0:2])
# print(user[1:])
# print(user[-3:-1])
#
# print(len(data))
# user.append('Elsa')
# print(user)
#
# user += ['Jason']
# print(user)
# user.extend(['Robert','Jimmy'])
# print(user)
#
# user.insert(0,'Bob')
# print(user)
#
# user[2:2] = ['Eddie','Alex']
# print(user)
#
# user[1:3] = ['Robert','JPJ']
# print(user)
#
# user.remove('Bob')
# print(user)
#
# print(user.pop())
# print(user)
#
# del user[0]
# print(user)
#
# # del data
# data.clear()
# print(data)
#
# user[1:2] = ['dave']
# user.sort()
# print(user)
#
# user.sort(key=str.lower)
# print(user)
#
# num = [1,2,3,4]
# num.reverse()
# print(num)
# # num.sort(reverse=True)
# # print(num)
#
# print(sorted(num,reverse=True))
# print(num)
#
# numcopy = num.copy()
# mynum = list(num)
# mycopy = num[:]
#
# print(numcopy)
# print(mynum)
# print(mycopy.sort())
# print(num)
# print(type(num))



def add_one(num):
    if(num >= 9):
        return num +1

    total = num + 1
    print(total)

    add_one(total)

mynewtotal = add_one(0)
print(mynewtotal)