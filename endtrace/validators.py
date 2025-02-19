class CoordsError(Exception):
    pass


class AngleError(Exception):
    pass


def validate_coords(x1: float, z1: float, x2: float, z2: float) -> None:
	"""
	Checks that two Minecraft coordinates are valid for a stronghold
	prediction.

	Args:
		x1 (float): X-coord of the first throw.
		z1 (float): Z-coord of the first throw.
		x2 (float): X-coord of the second throw.
		z2 (float): Z-coord of the second throw.
	
	Raises:
		CoordsError: If the coords are invalid for a prediction.
	"""
	if (x1, z1) == (x2, z2):
		raise CoordsError("coords must be different")


def _angle_out_of_bounds(theta: float) -> bool:
	"""
	Checks whether a Minecraft angle is out of bounds.

	Args:
		theta (float): The angle (in degrees).

	Returns:
		bool: True if the angle is out of bounds (less than -180
			degrees or greater than 180). False otherwise.
	"""
	return not (-180 <= theta <= 180)


def validate_angles(theta1: float, theta2: float) -> None:
	"""
	Checks that two Minecraft angles are valid for a stronghold
	prediction.

	Args:
		theta1 (float): The first angle (in degrees).
 		theta2 (float): The second angle (in degrees).
	
	Returns:
		None: This function does not return anything.

	Raises:
		AngleError: If the angles are identical or if one or more
			angles are outside of the angle bounds in Minecraft.
	"""
	if (theta1 == theta2):
		raise AngleError("angles must be different")
	elif _angle_out_of_bounds(theta1) or _angle_out_of_bounds(theta2):
		raise AngleError("angle(s) out of bounds")