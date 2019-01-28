def bfs(start, goal, x_capacity, y_capacity):
	path = []
	queue = []
	queue.append(start)
	visited = []
	while(not (not queue)):
		p = queue.pop(0)
		x = p[0]
		y = p[1]
		path.append(p)
		if x == goal or y == goal:
			print "Found!"
			return path
		# x<4 => (4,y)     FILL 4-GAL WATER JUG
		if p[0] < x_capacity and ([x_capacity, p[1]] not in visited):
			queue.append([x_capacity, p[1]])
			visited.append([x_capacity, p[1]])
		# y<3 => (x,3)      FILL 3-GAL WATER JUG
		if p[1] < y_capacity and ([p[0], y_capacity] not in visited):
			queue.append([p[0], y_capacity])
			visited.append([p[0], y_capacity])
		# x>0 => (0,y)      EMPTY 4-GAL JUG ON GROUND
		if p[0] > 0 and ([0, p[1]] not in visited):
			queue.append([0, p[1]])
			visited.append([0, p[1]])
		# y>0 => (x,0)      EMPTY 3-GAL JUG ON GROUND
		if p[1] > 0 and ([p[0], 0] not in visited):
			queue.append([p[0], 0])
			visited.append([p[0], 0])
		# 0<x+y>=4 and y>0 => (4, y-(4-x))  POUR WATER FROM 3-GAL JUG TO FILL 4-GAL JUG
		if (p[1] + p[0]) > 0 and (p[1] + p[0]) >= x_capacity and p[1] > 0 and ([x_capacity, 
p[1] - (x_capacity - p[0])] not in visited):
			queue.append([x_capacity, p[1] - (x_capacity - p[0])])
			visited.append([x_capacity, p[1] - (x_capacity - p[0])])
		# 0<x+y>=3 and x>0 => (x-(3-y), 3)  POUR WATER FROM 4-GAL JUG TO FILL 3-GAL JUG
		if (p[1] + p[0]) > 0 and (p[1] + p[0]) >= y_capacity and p[0] > 0 and ([p[0] -  (y_capacity - p[1]), y_capacity] not in visited):
			queue.append([p[0] - (y_capacity - p[1]), y_capacity])
			visited.append([p[0] - (y_capacity - p[1]), y_capacity])
		# 0<x+y<=4 and y>=0 => (x+y, 0)    POUR ALL OF WATER FROM 3-GAL JUG INTO 4-GAL JUG
		if (p[1] + p[0]) > 0 and (p[1] + p[0]) <= x_capacity and p[1] >= 0 and ([p[0] + 
p[1], 0] not in visited):
			queue.append([p[0] + p[1], 0])
			visited.append([p[0] + p[1], 0])		
		# 0<x+y<=3 and x>=0 => (0, x+y)    POUR ALL OF WATER FROM 4-GAL JUG INTO 3-GAL JUG
		if (p[1] + p[0]) > 0 and (p[1] + p[0]) <= y_capacity and p[0] >= 0 and ([0, p[0] + 
p[1]] not in visited):
			queue.append([0, p[0] + p[1]])
			visited.append([0, p[0] + p[1]])
		
	return "Not found"

x_capacity = input("Enter Jug 1 capacity:")
y_capacity = input("Enter Jug 2 capacity:")
goal = input("Enter target volume:")

def gcd(a, b):
	if a == 0:
		return b
	return gcd(b%a, a)

start = [0, 0] 

if goal % gcd(x_capacity,y_capacity) == 0:
	print bfs(start, goal, x_capacity, y_capacity)
else:
	print "No solution possible for this combination."

