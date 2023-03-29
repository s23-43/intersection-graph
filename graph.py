#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt
import matplotlib.patches as pch
from typing import Tuple

class Point:
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y
		self.p = (x,y)
	def __str__(self):
		return str(self.p)

def distance_between(a: Tuple[float, float], b: Tuple[float, float]) -> float:
	"""
	Calculates the distance between two coordinates in a 2D space using the Pythagorean theorem

	Args:
		a: A 2D coordinate
		b: A 2D coordinate

	Returns:
		The distance between the given 2D coordinates
	"""

	dxs = (a[0] - b[0])**2
	dys = (a[1] - b[1])**2
	return math.sqrt(dxs + dys)

def main():
	p1 = Point( 0, 0)
	p2 = Point( 3, 8)
	p3 = Point(10, 5)
	pc = Point( 4, 4)
	_, ax = plt.subplots()
	LINESTYLE = ":"
	CIRCLESTYLE = "-"

	# OP1
	plt.plot(p1.x, p1.y, "r.")
	plt.plot( [p1.x,pc.x], [p1.y,pc.y], "r", linestyle=LINESTYLE )
	ax.annotate( f"OP1 {p1.p}" , p1.p )
	ax.add_artist( pch.Circle(p1.p, distance_between(p1.p,pc.p), color="r", fill=False, linestyle=CIRCLESTYLE) )

	# OP2
	plt.plot(p2.x, p2.y, "g.")
	plt.plot( [p2.x,pc.x], [p2.y,pc.y], "g", linestyle=LINESTYLE )
	ax.annotate( f"OP2 {p2.p}" , p2.p )
	ax.add_artist( pch.Circle(p2.p, distance_between(p2.p,pc.p), color="g", fill=False, linestyle=CIRCLESTYLE) )

	# OP3
	plt.plot(p3.x, p3.y, "b.")
	plt.plot( [p3.x,pc.x], [p3.y,pc.y], "b", linestyle=LINESTYLE )
	ax.annotate( f"OP3 {p3.p}" , p3.p )
	ax.add_artist( pch.Circle(p3.p, distance_between(p3.p,pc.p), color="b", fill=False, linestyle=CIRCLESTYLE) )

	# Tracked object
	plt.plot(pc.x, pc.y, "mo")
	ax.annotate( f"Tracked object {pc.p}", pc.p )

	# Display
	ax.set_aspect("equal", adjustable="box")
	plt.xlabel("x-position (m)")
	plt.ylabel("y-position (m)")
	plt.title("Representation of intersecting radii method")
	plt.show(block=True)

if __name__ == "__main__":
	main()