from operator import itemgetter, attrgetter, methodcaller

s = 'The time has come the Walrus said'
upcase = methodcaller('upper')
print(upcase(s))