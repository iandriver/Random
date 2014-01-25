import sys
from sets import Set
import matplotlib.pyplot as plt

def slope(l):
    """Returns gradient 'm' of a line"""
    m = None
    # Ensure that the line is not vertical
    if l[0] != l[2] and l[1] != l[3]:
        m = (1./(l[0]-l[2]))*(l[1] - l[3])
        return m

def parallel(l1,l2):
    if slope(l1) != slope(l2):
        return False
    return True


def intersect(l):
    """Returns intersect (b) of a line using the equation of
    a line in slope and intercepet form (y = mx+b)"""
    return l[1] - (slope(l)*l[0])


def line_intersection(l1,l2):
	"""Returns the intersection point (x,y) of two line segments. Returns False
	for parallel lines"""
	# Not parallel
	x = -1
	y = -1
	if not parallel(l1,l2):
		if slope(l1) is not None and slope(l2) is not None:
			x_try = (1./(slope(l1) - slope(l2))) * (intersect(l2) - intersect(l1))
			y_try = (slope(l1)*x_try) + intersect(l1)
			if x_try <= l1[0] and x_try >= l1[2] and x_try <= l2[0] and x_try >= l2[2]:
				x = x_try
			elif x_try >= l1[0] and x_try <= l1[2] and x_try >= l2[0] and x_try <= l2[2]:
				x = x_try
			elif x_try <= l1[0] and x_try >= l1[2] and x_try >= l2[0] and x_try <= l2[2]:
				x = x_try
			elif x_try >= l1[0] and x_try <= l1[2] and x_try <= l2[0] and x_try >= l2[2]:
				x = x_try		
			if y_try <= l1[1] and y_try >= l1[3] and y_try <= l2[1] and y_try >= l2[3]:
				y = y_try
			elif y_try >= l1[1] and y_try <= l1[3] and y_try >= l2[1] and y_try <= l2[3]:
				y = y_try
			elif y_try <= l1[1] and y_try >= l1[3] and y_try >= l2[1] and y_try <= l2[3]:
				y = y_try
			elif y_try >= l1[1] and y_try <= l1[3] and y_try <= l2[1] and y_try >= l2[3]:
				y = y_try				
		else:
			if slope(l1) is None:
				x = l1[0]
				y = (slope(l2)*x) + intersect(l2)
			elif slope(l2) is None:
				x = l2[0]
				y = (slope(l1)*x) + intersect(l1)
		if x != -1 and y != -1:
			return [x,y]
	else:
		return False
			

geop_list = []
fin_list = []
fin_dict ={}
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	test = test.rstrip()
	if(0 == len(test)):
		continue
	parts = test.split(":")
	num = int(parts[0])
	geopoints = parts[1].strip()
	gp1 = geopoints.strip('()').split(',')
	for x in gp1:
		y = x.strip()
		geop_list.append(float(y.strip('[]')))
	if len(geop_list) == 4:
		fin_list.append(geop_list)
		fin_dict[num] = geop_list
		geop_list = []
print fin_dict		
end_check = 1	
del_list = []	
while end_check != 0:		
	c = 0
	clist = []
	crossing_dict ={}
	for fk, v in fin_dict.items():
		if v != 'X':
			crossing_dict[fk] = 0
	for k, l1 in fin_dict.items():
		if l1 != 'X':	
			c = k
			for k2, l2 in fin_dict.items():
				c2 = k2
				if c != c2 and Set([c, c2]) not in clist and l2 != 'X':
					clist.append(Set([c,c2]))
					l_int = line_intersection(l1,l2)
					if l_int:
						newc = crossing_dict[c] + 1
						newc2 = crossing_dict[c2] + 1
						crossing_dict[c] = newc
						crossing_dict[c2] = newc2	
	check = max(crossing_dict, key=crossing_dict.get)
	end_check = crossing_dict[check]
	if end_check != 0:
		fin_dict[check] = 'X'
print crossing_dict
c3 = 0
fig = plt.figure()
for l1 in fin_list:	
	c3+=1
	ax1 = fig.add_subplot(211)
	ax1.plot([l1[0],l1[2]],[l1[1],l1[3]])
	ax1.text(l1[0]-.01, l1[1]-.01, str(c3))
for kl,fl in fin_dict.items():
	if 	fl != 'X':
		ax2 = fig.add_subplot(212)
		ax2.plot([fl[0],fl[2]],[fl[1],fl[3]])
		ax2.text(fl[0]-.01, fl[1]-.01, str(kl))
plt.show()			
			

	
    

test_cases.close()
