def deco(func):
    def inner():
        print('running inner()')
        func()
        print('inner() done')
    return inner

@deco
def target():
    print('running target()')

target()
print(target.__name__)