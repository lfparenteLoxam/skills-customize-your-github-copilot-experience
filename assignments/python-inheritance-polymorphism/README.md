# 📘 Assignment: Inheritance and Polymorphism in Python

## 🎯 Objective

Design an object-oriented model using inheritance and polymorphism in Python. You will build a small transportation system where different vehicle types share a common interface but implement their own behavior.

## 📝 Tasks

### 🛠️	Build a Base Class and Subclasses

#### Description
Create a base class named `Vehicle` and define subclasses for at least three vehicle types.

#### Requirements
Completed program should:

- Define a `Vehicle` base class with shared attributes: `brand` and `max_speed`
- Include a method `move()` in `Vehicle` that is intended to be overridden
- Create at least three subclasses such as `Car`, `Bike`, and `Boat`
- Override `move()` in each subclass with behavior specific to that vehicle type


### 🛠️	Use Polymorphism with a Fleet Function

#### Description
Create a function that processes a mixed list of vehicles and calls the same method on each object.

#### Requirements
Completed program should:

- Implement a function `show_fleet_movement(fleet)` that accepts a list of `Vehicle` objects
- Loop through the list and call `move()` for each object
- Demonstrate that each subclass returns different output through polymorphism
- Print readable output that includes the class name and movement message


### 🛠️	Stretch: Add a New Vehicle Without Changing Existing Logic

#### Description
Extend the system by adding a new vehicle type and prove the fleet function still works without modification.

#### Requirements
Completed program should:

- Add a new subclass (for example `Train` or `Helicopter`) with its own `move()` implementation
- Reuse the existing `show_fleet_movement(fleet)` function unchanged
- Include a short explanation in comments about why this demonstrates extensibility
