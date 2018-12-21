import random
import math

def get_distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d

if __name__ == '__main__':
	cnt = 0
	div = -1
	hit = 0
	while (cnt != div):
		cnt = cnt + 1
		x = random.uniform(0, 1)
		y = random.uniform(0, 1)
		if(get_distance(0,0,x,y) <= 1):hit = hit + 1
		pi = hit*4/cnt
		print("pi=",pi)
		
	print("pi=",pi)
	temp = input("終了するにはEnterキーを押してください。")
