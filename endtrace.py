"""
endtrace - A simple tool for locating Minecraft strongholds.

Author: Mason Law
Date: 02-19-2025

This program predicts the location of Minecraft strongholds based on data
from two Eye of Ender throws. It predicts the stronghold coordinates by using
the inputted (x, z) coordinates and angles of each throw. Additionally, this
program can display a graph visualizing the prediction.

Usage:
    python endtrace.py x1 z1 theta1 x2 z2 theta2
    python endtrace.py x1 z1 theta1 x2 z2 theta2 --graph

Attributes:
    None
"""


from endtrace.parser import parser
from endtrace.validators import *
import math
import matplotlib.pyplot as plt
import sys


args = parser.parse_args()
x1, z1, theta1 = args.x1, args.z1, args.theta1
x2, z2, theta2 = args.x2, args.z2, args.theta2
graph = args.graph


# validate the inputted args
try:
    validate_coords(x1, z1, x2, z2)
    validate_angles(theta1, theta2)
except CoordsError as coords_error:
    print(f"CoordsError: {coords_error}")
    sys.exit(1)
except AngleError as angle_error:
    print(f"AngleError: {angle_error}")
    sys.exit(1)


def _transform_angle_to_rad(theta: float) -> float:
    """
    Transforms a Minecraft angle (in degrees) to a Cartesian angle (in
    radians).

    Args:
        theta (float): The angle from Minecraft (in degrees).

    Returns:
        float: The new Cartesian angle (in radians).
    """
    # check images/endtrace-math.pdf for an explanation

    # add a small nudge at boundaries to prevent errors with math.tan
    if theta == 0 or theta == -180 or theta == 180:
        theta += sys.float_info.epsilon 

    # transform angles to be in radians and the cartesian plane
    if theta > 0: return math.radians(-theta + 270)
    else: return math.radians(-theta - 90)


# transform minecraft angles to radians in the cartesian plane
theta1 = _transform_angle_to_rad(theta1)
theta2 = _transform_angle_to_rad(theta2)


def predict_stronghold(
    x1: float, z1: float, theta1: float,
    x2: float, z2: float, theta2: float
) -> None:
    """
    Predicts the (Cartesian) stronghold coordinates based on data from
    two Eye of Ender throws. Prints the stronghold prediction.

    Args:
        x1 (float): X-coord of the first throw.
        z1 (float): Z-coord of the first throw.
        theta1 (float): Angle of the first throw (in Cartesian radians).
        x2 (float): X-coord of the second throw.
        z2 (float): Z-coord of the second throw.
        theta2 (float): Angle of the second throw (in Cartesian radians).

    Returns:
        None
    """
    # get the slopes of each throw
    m1 = math.tan(theta1)
    m2 = math.tan(theta2)
    rounded_m1 = round(m1, 2)
    rounded_m2 = round(m2, 2)

    # check images/endtrace-math.pdf for work
    pred_x = (m2*x2 - m1*x1 + z1 - z2)/(m2 - m1)
    pred_z = (m1*m2*(x2 - x1) + m2*z1 - m1*z2)/(m2 - m1)
    rounded_pred_x = round(pred_x, 2)
    rounded_pred_z = round(pred_z, 2)

    # print regardless of graphing or not
    print(
        f"predicted stronghold coords:\n",
        f"\t(x={rounded_pred_x},",
        f"y=?,",
        f"z={rounded_pred_z})"
    )

    if graph:
        fig, ax = plt.subplots(figsize=(8, 5))

        # set up the plot
        ax.invert_yaxis()
        ax.set_title("endtrace visualization")
        ax.set_xlabel("x-axis")
        ax.set_ylabel("z-axis (inverted)")
        plt.tight_layout(pad=3.0)

        # round the intercepts for visual appeal
        intercept1 = round(-m1*x1 + z1, 2)
        intercept2 = round(-m2*x2 + z2, 2)
        sign1 = sign2 = "+"

        # format the intercept for the first throw
        if intercept1 < 0:
            sign1 = "-"
            intercept1 = abs(intercept1)

        # format the intercept for the second throw
        if intercept2 < 0: 
            sign2 = "-"
            intercept2 = abs(intercept2)

        # calculate the slope-intercept form
        throw1 = f"throw1: z = {rounded_m1}x {sign1} {intercept1}"
        throw2 = f"throw2: z = {rounded_m2}x {sign2} {intercept2}"

        # plot the throws and prediction
        dx = dz = 250  # the block distance around the prediction
        bounds = [pred_x - dx, pred_x, pred_x + dz]
        ax.plot(
            bounds,
            list(map(lambda x: m1*x - m1*x1 + z1, bounds)),
            "-",
            lw=2.0,
            label=throw1,
            color="#316364"
        )
        ax.plot(
            bounds,
            list(map(lambda x: m2*x - m2*x2 + z2, bounds)),
            "-",
            lw=2.0,
            label=throw2,
            color="#659B7D"
        )
        sh = f"stronghold prediction: ({rounded_pred_x}, {rounded_pred_z})"
        ax.plot(pred_x, pred_z, "o", label=sh, color="#102C31")

        plt.legend(loc="upper left")
        plt.grid()
        plt.show()


predict_stronghold(x1, z1, theta1, x2, z2, theta2)