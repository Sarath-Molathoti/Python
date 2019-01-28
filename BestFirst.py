def heuristic_function(a, b, goal):
	c = (abs(a - goal) + abs(b -goal))
	return c

def bfs(start, goal, x_capacity, y_capacity):
	path = []
	PriorityQ = []
	PriorityQ.append(start)
	visited = []
	while(not (not PriorityQ)):
		p = PriorityQ.pop(0)
		x = p[0]
		y = p[1]
		path.append(p)
		if x == goal or y == goal:
			print "Path Found!"
			return path
		# x<4 => (4,y)     FILL 4-GAL WATER JUG
		if p[0] < x_capacity and ([x_capacity, p[1], heuristic_function(x_capacity, p[1], goal)] not in visited):
			PriorityQ.append([x_capacity, p[1], heuristic_function(x_capacity, p[1], goal)])
			visited.append([x_capacity, p[1], heuristic_function(x_capacity, p[1], goal)])
		# y<3 => (x,3)      FILL 3-GAL WATER JUG
		if p[1] < y_capacity and ([p[0], y_capacity, heuristic_function(p[0], y_capacity, goal)] not in visited):
			PriorityQ.append([p[0], y_capacity, heuristic_function(p[0], y_capacity, goal)])
			visited.append([p[0], y_capacity, heuristic_function(p[0], y_capacity, goal)])
		# x>0 => (0,y)      EMPTY 4-GAL JUG ON GROUND
		if p[0] > 0 and ([0, p[1], heuristic_function(0, p[1], goal)] not in visited):
			PriorityQ.append([0, p[1], heuristic_function(0, p[1], goal)])
			visited.append([0, p[1], heuristic_function(0, p[1], goal)])
		# y>0 => (x,0)      EMPTY 3-GAL JUG ON GROUND
		if p[1] > 0 and ([p[0], 0, heuristic_function(p[0], 0, goal)] not in visited):
			PriorityQ.append([p[0], 0, heuristic_function(p[0], 0, goal)])
			visited.append([p[0], 0, heuristic_function(p[0], 0, goal)])
		# 0<x+y>=4 and y>0 => (4, y-(4-x))  POUR WATER FROM 3-GAL JUG TO FILL 4-GAL JUG
		if (p[1] + p[0]) > 0 and (p[1] + p[0]) >= x_capacity and p[1] > 0 and ([x_capacity, 
p[1] - (x_capacity - p[0]), heuristic_function(x_capacity, (p[1] - (x_capacity - p[0])), goal)] not in visited):
			PriorityQ.append([x_capacity, p[1] - (x_capacity - p[0]), heuristic_function(x_capacity, (p[1] - (x_capacity - p[0])), goal)])
			visited.append([x_capacity, p[1] - (x_capacity - p[0]), heuristic_function(x_capacity, (p[1] - (x_capacity - p[0])), goal)])
		# 0<x+y>=3 and x>0 => (x-(3-y), 3)  POUR WATER FROM 4-GAL JUG TO FILL 3-GAL JUG
		if (p[1] + p[0]) > 0 and (p[1] + p[0]) >= y_capacity and p[0] > 0 and ([p[0] -  (y_capacity - p[1]), y_capacity, heuristic_function((p[0] - (y_capacity - p[1])), y_capacity, goal)] not in visited):
			PriorityQ.append([p[0] - (y_capacity - p[1]), y_capacity, heuristic_function((p[0] - (y_capacity - p[1])), y_capacity, goal)])
			visited.append([p[0] - (y_capacity - p[1]), y_capacity, heuristic_function((p[0] - (y_capacity - p[1])), y_capacity, goal)])
		# 0<x+y<=4 and y>=0 => (x+y, 0)    POUR ALL OF WATER FROM 3-GAL JUG INTO 4-GAL JUG
		if (p[1] + p[0]) > 0 and (p[1] + p[0]) <= x_capacity and p[1] >= 0 and ([p[0] + 
p[1], 0, heuristic_function(p[0] + p[1], 0, goal)] not in visited):
			PriorityQ.append([p[0] + p[1], 0, heuristic_function(p[0] + p[1], 0, goal)])
			visited.append([p[0] + p[1], 0, heuristic_function(p[0] + p[1], 0, goal)])		
		# 0<x+y<=3 and x>=0 => (0, x+y)    POUR ALL OF WATER FROM 4-GAL JUG INTO 3-GAL JUG
		if (p[1] + p[0]) > 0 and (p[1] + p[0]) <= y_capacity and p[0] >= 0 and ([0, p[0] + 
p[1], heuristic_function(0, p[0] + p[1], goal)] not in visited):
			PriorityQ.append([0, p[0] + p[1], heuristic_function(0, p[0] + p[1], goal)])
			visited.append([0, p[0] + p[1], heuristic_function(0, p[0] + p[1], goal)])
		PriorityQ.sort(key=sr)
		
	return "Not found"

x_capacity = input("Enter Jug 1 capacity:")
y_capacity = input("Enter Jug 2 capacity:")
goal = input("Enter target volume:")

def sr(res):
	return res[2]

def gcd(a, b):
	if a == 0:
		return b
	return gcd(b%a, a)

start = [0, 0, heuristic_function(0, 0, goal)] 

if goal % gcd(x_capacity,y_capacity) == 0:
	print bfs(start, goal, x_capacity, y_capacity)
else:
	print "No Path Found."

