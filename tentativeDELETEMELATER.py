"""
> ##### Tungsten Ore : 399960x
> ##### Silver Ore : 399960x
> ##### Sand : 26997300x (3.70 % used in item B, 3.70 % used in item C, 92.59% used in item D) 
> ##### Copper Ore : 31108x (14.29% used in item B, 14.29% used in item C, 71.43% used in item D)
> ##### Titanium Ore : 119988x
> ##### Gold Ore : 279972x (28.57% used in item B, 71.43 % used in item C)
> ##### Coal : 399960x
> ##### Pixels : 3999600x
> ##### Sulphur : 79992x
> ##### Hydrogen : 79992x
> ##### Water : 159984x
"""
mylist : list = []
#! replace all ']' chracters with the '%' chracter on sorted output
mylist.append('> ##### Tungsten Ore : 399960x')
mylist.append('> ##### Silver Ore : 399960x')
mylist.append("> ##### Sand : 26997300x (3.70 ] used in item B, 3.70 ] used in item C, 92.59] used in item D) ")
mylist.append("> ##### Copper Ore : 31108x (14.29] used in item B, 14.29] used in item C, 71.43] used in item D)")
mylist.append("> ##### Titanium Ore : 119988x")
mylist.append("> ##### Gold Ore : 279972x (28.57] used in item B, 71.43 ] used in item C)")
mylist.append("> ##### Coal : 399960x")
mylist.append("> ##### Pixels : 3999600x")
mylist.append("> ##### Sulphur : 79992x")
mylist.append("> ##### Hydrogen : 79992x")
mylist.append("> ##### Water : 159984x")
mylist.sort()
for line in mylist:
    print(line)
