dic = {'c': 2, 'a': 3, 'b': 1}
list = ['a','a','a','b','b','b']

print 'print key - value pairs'
for key in dic:
    print key, dic[key]

print 'sorted by keys'
for key in sorted(dic):
    print key, dic[key]

print 'sorted by values'
for key in sorted(dic, key=dic.get):# reverse=True):
    print key, dic[key]

print 'grouping (accumulating) values by keys'
dic_accum = {}
for element in list:
    if element in dic_accum:
        dic_accum[element] += 1
    else:
        dic_accum[element] = 1
print dic_accum

print 'add pair key-value'
dic['d'] = 5
print dic
