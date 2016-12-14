from hrw3 import Ring

ip1 = "127.0.0.1:5001"
ip2 = "10.250.109.180"
ip3 = "5000"

ring = Ring()
ring.add(ip1)
ring.add(ip2)
ring.add(ip3)

print ring.hash(str(101))
print ring.hash(str(120))
print ring.hash(str(11))
print ring.hash(str(12))
print ring.hash(str(13))
print ring.hash(str(531))
print ring.hash(str(1111))
print ring.hash(str(145))
print ring.hash(str(9))
