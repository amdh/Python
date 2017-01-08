import bisect

node = [212 ,34,43,65,2,66,7,9]

node.sort()
print node

print bisect.bisect(node,5)

print node

print bisect.bisect_right(node,3)

print bisect.bisect_right(node,31)

print bisect.bisect_left(node,31)

print bisect.bisect(node,31)

print bisect.insort(node,6)

print node

server = [ 5001, 5002, 5004]

server.sort()

print bisect.bisect(server, 3)