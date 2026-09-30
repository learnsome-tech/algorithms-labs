n=10000
front_moves=sum(range(n))
append_ops=n
print('inserting at front,', n, 'calls:', front_moves, 'shifts')
print('appending,', n, 'calls:', append_ops, 'ops')
print('front insert is costlier:', front_moves > append_ops)
