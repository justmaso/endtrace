import argparse

parser = argparse.ArgumentParser(
	prog="endtrace",
	description="approximates the location of minecraft strongholds"
)

# add the first throw's arguments
parser.add_argument(
	"x1",
	type=float,
	help="the x-coord of your first throw"
)

parser.add_argument(
	"z1",
	type=float,
	help="the z-coord of your first throw"
)

parser.add_argument(
	"theta1",
	type=float,
	help="the angle of your first throw (in degrees)"
)

# add the second throw's arguments
parser.add_argument(
	"x2",
	type=float,
	help="the x-coord of your second throw"
)

parser.add_argument(
	"z2",
	type=float,
	help="the z-coord of your second throw"
)

parser.add_argument(
	"theta2",
	type=float,
	help="the angle of your second throw (in degrees)"
)

# add the (optional) graphing argument
parser.add_argument(
	"-g",
	"--graph",
	help="show a graph of the endtrace stronghold prediction",
	action="store_true"
)