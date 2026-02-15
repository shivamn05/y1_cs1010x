#
# CS1010S --- Programming Methodology
#
# Sidequest 8.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from planets import *

# Set up the environment of the simulation
planets = (Earth, Mars, Moon)

plot_planets(planets, Mars)

##########
# Task 1 #
##########
# a)
# Follows trigonometry angle.
# E.g. 0 degree -> East
# E.g. 90 degree -> North
def get_velocity_component(angle, velocity):
    xv = velocity * cos(radians(angle))
    yv = velocity * sin(radians(angle))
    return (xv,yv)

# print(get_velocity_component(30, 50)) #(43.30127018922194, 24.999999999999996)
# note that the exact values of each component may differ slightly due to differences in precision

# b)
def calculate_total_acceleration(planets, current_x, current_y):
    x_acc = 0
    y_acc = 0
    for planet in planets:
        mass = get_mass(planet) # mass
        x_coord = get_x_coordinate(planet) # x of planet
        y_coord = get_y_coordinate(planet) # y of planet 
        dist = hypot(current_x-x_coord, current_y-y_coord) # r 
        x_acc += (G * mass * (x_coord-current_x)) / dist**3
        y_acc += (G * mass * (y_coord-current_y)) / dist**3
    return (x_acc, y_acc)


# print(calculate_total_acceleration(planets, 0.1, 0.1)) #(-1511.54410020574, -1409.327982470404)

# c)
# Do not change the return statement
def f(t, Y):
    rx, ry, vx, vy = Y[0], Y[1], Y[2], Y[3]
    ax, ay = calculate_total_acceleration(planets, rx, ry)
    return np.array([vx, vy, ax, ay])

np.set_printoptions(precision=3)
# print(f(0.5, [0.1, 0.1, 15.123, 20.211])) #[ 15.123 20.211 -1511.544 -1409.328]

##########
# Task 2 #
##########

# Uncomment and change the input parameters to alter the path of the spacecraft
vx, vy = get_velocity_component(74.9999999999999999999999999999999999999999999, 27.32)
# (angle, velocity)

##############################################################################################
# Uncomment the following line to start the plot
start_spacecraft_animation(vx, vy, f)
