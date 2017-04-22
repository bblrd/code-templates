# IPython example for timing a very large list of strings (Python for Data Analysis Chapter 3)
strings = ['foo', 'foobar', 'baz', 'qux','python', 'Guido Van Rossum'] * 100000
method1 = [x for x in strings if x.startswith('foo')]
method2 = [x for x in strings if x[:3] == 'foo']

print 'time method1'
%time method1 = [x for x in strings if x.startswith('foo')]
print '\n'

print 'time method2'
%time method2 = [x for x in strings if x[:3] == 'foo']
print '\n'

print 'timeit method1'
%timeit [x for x in strings if x.startswith('foo')]
print '\n'

print 'timeit method2'
%timeit [x for x in strings if x[:3] == 'foo']
