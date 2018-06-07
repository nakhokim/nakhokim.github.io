import random

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"

lorem2 = lorem.split(" ")





rand_seg = random.randint(0,10)

#print (lorem2[rand_seg:(rand_seg+100)])

lorem3 = lorem2[rand_seg:(rand_seg+100)]

lorem4 = ' '.join(lorem3)

print(lorem4)
