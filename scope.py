name = [1,2,3,4] 
# name2 = name.copy()
# name2 = name 

# print(name is name2)

# def print_name():
#      username = 'anirudh'
#      print(username)

# print_name()

def parent():
     x = 'anirudh'
     def child():
          print(x)
     return child

result = parent()