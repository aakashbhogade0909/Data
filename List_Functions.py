Modi = 'MODI'
names = ['Obama', "Hillary", Modi, 'Putin', 'MODI']
print names

names.append('Mao') 
print names.count(Modi)

print names

t = ('Indira', 'Bill')
r = ['Lal', 'Bill']
names.extend(t)
print names
names.extend(r)
print names

print "Index : ", names.index('MODI', 3, 5)

print len(names)

names.insert(5, 'MODI')
print names

d = names.pop(9)
print names
print d

e = names.remove('Mao')
print names
print e
sort(key=, reverse=True)
learn_sort = ['Obama', "Hillary", Modi, 'Putin', 'MODI', 'ant', 'modi', 'mOdi', 'moDi']
def MyFn(s):
	return s[-1]
learn_sort.sort(key=MyFn)
print learn_sort