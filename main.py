# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

G = 6.67430 * (10**-11)

def greet(name, greeting_template="Hello, <name>!"):
    if name is None or name.strip() == "":
        raise ValueError("Name cannot be None or empty string.")
    return greeting_template.replace("<name>", name)

print(greet("Sylvious"))

def force(mass, body='earth'):
    # A dictionary to store the surface gravity of different celestial bodies
    gravity_factors = {
    'mercury': 3.7,
    'venus': 8.87,
    'earth': 9.8,
    'mars': 3.711,
    'jupiter': 24.79,
    'saturn': 10.44,
    'uranus': 8.69,
    'neptune': 11.15,
    'pluto': 0.62,
    'moon': 1.62,
    'sun': 274.0
    }
    
    # rounding the gravity factor of the specified body to 1 decimal
    gravity = round(gravity_factors[body], 1)
    
    # Calculating the force
    force = mass * gravity
    
    return force

f = force(100, 'sun')
print(f)


def pull(m1, m2, d):
    G = 6.67430 * (10**-11)
    pull = G * ((m1 * m2) / (d**2))
    return '{:.6e}'.format(pull)
























