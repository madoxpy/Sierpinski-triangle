from pygame import *

white=(255,255,255)
black=(0,0,0)

def draw_triangle(x1,y1,x2,y2,x3,y3,n):
	draw.polygon(window, white, [[x1, y1], [x2, y2], [x3, y3]], 1)
	if n>0:
		draw_triangle(x1,y1,(x2+x1)/2,(y2+y1)/2,(x3+x1)/2,(y3+y1)/2,n-1)
		draw_triangle((x1+x2)/2,(y1+y2)/2,x2,y2,(x3+x2)/2,(y3+y2)/2,n-1)
		draw_triangle((x1+x3)/2,(y1+y3)/2,(x2+x3)/2,(y2+y3)/2,x3,y3,n-1)

init()
window=display.set_mode((500,500))
clock = time.Clock()

end = False 
n=0
while not end:
	for z in event.get():
		if z.type ==QUIT:
			end=True
	
	window.fill(black)
	draw_triangle(250,490-346,50,490,450,490,n)
	n=n+1
	if n>6:
		n=0
	
	clock.tick(2)
	display.flip()