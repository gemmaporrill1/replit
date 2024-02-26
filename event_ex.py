# Exercise: Event Registration System
# Objective: Write a Python program that includes a function to register participants for an event. The registration function should handle participant details and their preferences with default values for some parameters.
# Initial Setup
# Participants need to provide their name and email. Additionally, they can specify their meal preference (vegetarian or non-vegetarian) and if they need accommodation. By default, the meal preference should be set to "non-vegetarian", and accommodation required should be False.
# Task
# Registration Function: Write a function register_participant(name, email, meal_preference="non-vegetarian", needs_accommodation=False) that registers a participant with their provided details and preferences.
# Display Registered Participants: After registration, display the participant's details, including their name, email, meal preference, and accommodation needs.
# Expected Functionality
# Registering a participant with all details specified.
# Registering a participant with only the name and email, using default values for the other parameters.

# name_input = input("Enter your name: ")
# email_input = input("Enter your email: ")
# meal_preference_input = input(
#   "Enter your meal preference (vegetarian/non-vegetarian): ")
# needs_accommodation_input = input("Do you need accommodation? (yes/no): ")

# choices = []

# def register_participant(name, email, meal_preference="non-vegetarian", needs_accommodation=False):
#   for choice in choices:
    
#     if needs_accommodation_input == "yes":
#       return True
#     if needs_accommodation == "no":
#       return False

#     register_participant.append(choice(name_input, email_input, meal_preference_input, needs_accommodation_input))

# print(choices)

choices = []

def register_participant(name, email, meal_preference="non-vegetarian", needs_accommodation= False):
  for choice in choices:
    if needs_accommodation == "yes":
      return True
    choices.append(choices)
    return choices

# Collect participant information
name_input = input("Enter your name: ")
email_input = input("Enter your email: ")
meal_preference_input = input("Enter your meal preference (vegetarian/non-vegetarian): ")
needs_accommodation_input = input("Do you need accommodation? (yes/no): ")

# Register the participant