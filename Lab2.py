# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    # TODO: Implement this function
    h0=float(input("Enter initial height: "))
    time=int(input("Enter time: "))
    g=9.8
    height=h0-0.5*g*time**2
    print(f"The height of the ball at time {time} seconds is {height} meters.")

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    speed=20
    time=float(input("Enter time (in seconds): "))
    distance=speed*time
    print(f"The car will travel {distance} meters in {time} seconds,")
