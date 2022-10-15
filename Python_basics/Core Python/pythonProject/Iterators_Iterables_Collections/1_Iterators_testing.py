from Iterators import LevelOrderIterator

expr_tree = ['*', '+', '-', 'a', 'b', 'c', 'd']

iterator = LevelOrderIterator(expr_tree)

print(next(iterator))