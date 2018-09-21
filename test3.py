a = 'select r from db where a > 4'
x,y = a.split('where')
print(repr(x.strip()), y.strip())
select name from db where age > 24