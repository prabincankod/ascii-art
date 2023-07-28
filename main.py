import os 
options= ['forrest','parrot','donut','nyan','rick']


for i in enumerate(options): 
    print(i[0],i[1])
option = int(input("pick any one"))


os.system(f"curl ascii.live/{options[option]}")