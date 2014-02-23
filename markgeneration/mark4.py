import matplotlib.pyplot as plt
import random as random
import numpy as np
import math

side = 5
angle = 20
field = 100
rnd_point_num = 10
max_error = 0.0001

def point_dist(p1,p2):
	dist = ((p1[0] - p2[0])**2+(p1[1] - p2[1])**2)**0.5
	return dist

def move_to_point(p,dist,angle):
	p_r = (p[0]+dist*math.cos(math.radians(angle)),p[1]+dist*math.sin(math.radians(angle)))
	return p_r

def is_rect(p1,p2,p3,p4,max_error):
	d1 = point_dist(p1,p2) 
	d2 = point_dist(p1,p3) 
	d3 = point_dist(p1,p4) 
	d4 = point_dist(p2,p3) 
	d5 = point_dist(p2,p4) 
	d6 = point_dist(p3,p4)

	p_ar = [d1,d2,d3,d4,d5,d6]
	p_max = max(p_ar)
	p_min = min(p_ar)
	diag_cnt = 0
	side_cnt = 0
	for distance in p_ar:
		if abs(distance - p_max) < max_error :
			diag_cnt += 1
		if abs(distance - p_min) < max_error:
			side_cnt += 1
	if side_cnt == 4 and diag_cnt == 2:
		return p1,p2,p3,p4
	else:
		return False

def check_points(a,max_error):
	i_a = []
	i = 0
	for k in a:
		i_a.append(i)
		i += 1
	for q in i_a:
		for qq in xrange(q+1,len(i_a)):
			for qqq in xrange(qq+1,len(i_a)):
				for qqqq in xrange(qqq+1,len(i_a)):
					res = is_rect(a[q],a[qq],a[qqq],a[qqqq],max_error)
					if res:
						return res
	return False

def prepare_plot(a):
	x = []
	y = []
	for p in a:
		x.append(p[0])
		y.append(p[1])
	return x,y

def generate_square(side,field,angle):
	ox = random.uniform(side, field - side)
	oy = random.uniform(side, field - side)
	p1 = (ox,oy)
	p2 = move_to_point(p1,side,angle)
	p3 = move_to_point(p2,side,90+angle)
	p4 = move_to_point(p3,side,180+angle)

	points = [p1,p2,p3,p4]
	return points
def add_noize_points(points,rnd_point_num,field):
	for m in xrange(0,rnd_point_num):
		points.append((random.uniform(0, field),random.uniform(0, field)))

	random.shuffle(points)
	return points

square = generate_square(side,field,angle)

points = add_noize_points(square,rnd_point_num,field)

good_p = check_points(points,max_error)

print good_p 

#draw
all_p = prepare_plot(points)
good_p = prepare_plot(good_p)

ax = plt.axes()
ax.axis([0,field,0,field])
ax.plot(all_p[0],all_p[1],'ro')
ax.plot(good_p[0],good_p[1],'go')
plt.show()