# README.md

# Gravity Calculator

This project contains functions for calculating gravity-related values. Specifically, it contains functions for calculating the force of gravity on a given mass, the gravitational pull between two masses, and a function to create a greeting.

## Installation

This project requires Python 3.6 or later.

## Usage

### Greet

This function takes a name and a greeting template as parameters and returns a greeting with the name passed in.

```python
greet("John")
# Output: "Hello, John!"
```

### Force

This function takes a mass (in kilograms) and a body as parameters and returns the force of gravity (in newtons) on that mass on the given body. The body must be one of the following strings: `'mercury'`, `'venus'`, `'earth'`, `'mars'`, `'jupiter'`, `'saturn'`, `'uranus'`, `'neptune'`, `'pluto'`, `'moon'`, or `'sun'`.

```python
force(5, 'earth')
# Output: 49.0
```

### Pull

This function takes two masses (in kilograms) and a distance between them (in meters) and returns the gravitational pull (in newtons) between them.
