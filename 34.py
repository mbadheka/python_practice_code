def func(names,**kwargs):
    if kwargs.get('revers_string')== True:
        return [i[::-1].title() for i in names]
    else:
        return[i.title() for i in names]    

name = ['malhar','badheka']

print(func(name,revers_string= True))