alien_0 = {'color': 'green', 'points': 5}
print(alien_0)


alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

new_points = alien_0['points']

print(f"You just earned {new_points} points!")
print(alien_0['color'])
print(alien_0['points'])

alien_1 = {}

alien_1['color'] = 'violet'
alien_1['points'] = 7
print(alien_1)

alien_2 = {'color': 'yellow'}
print(f"The alien is {alien_2['color']}.")

alien_2['color'] = "orange"
print(f"The alien is now {alien_2['color']}.")

print("\n")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New Position: {alien_0['x_position']}")

print('\n')

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
