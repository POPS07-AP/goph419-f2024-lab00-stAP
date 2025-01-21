def launch_angle_range(ve_v0, alpha, tol_alpha):
    """
    Compute the minimum and maximum allowable launch angles.

    Parameters:
    -----------
    ve_v0 : float
        Ratio of escape velocity to terminal velocity.
    alpha : float
        Desired maximum altitude as a fraction of Earth's radius.
    tol_alpha : float
        Tolerance for maximum altitude.

    Returns:
    --------
    numpy.array
        A two-element array with [min_angle, max_angle].
    """
    # Compute the minimum and maximum alpha values
    alpha_min = (1 - tol_alpha) * alpha
    alpha_max = (1 + tol_alpha) * alpha

    # Compute the launch angles at the bounds
    min_angle = launch_angle(ve_v0, alpha_min)
    max_angle = launch_angle(ve_v0, alpha_max)

    # Return the result as a numpy array
    return np.array([min_angle, max_angle])
