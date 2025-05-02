"""
Command-line argument parser for endtrace, a Minecraft stronghold prediction
tool.

This script parses user input for data from two Eye of Ender throws, including
their coordinates and angles. It also supports an optional flag to display a
graphical visualization of the predicted stronghold location (as opposed to
just printing it).

Arguments:
	x1, z1, theta1: Coordinates and angle of the first throw.
    x2, z2, theta2: Coordinates and angle of the second throw.
    -g, --graph: Optional flag to enable graphical output.
"""

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
