# Author: Heiður Þórey Atladóttir
# Date:28.01.25
# Project: Skiladæmi 2
# Acknowledgements:Dæmatímakennari

a=int(input('Value: '))
max_a=1
max_a2=2

while not a<=0:
    if a>max_a:
        max_a2=max_a
        max_a=a
    elif a>max_a2:
        max_a2=a
    a=int(input('Value: '))
print('Largest:',max_a)
print('Second largest:',max_a2 )


