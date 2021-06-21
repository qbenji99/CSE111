from datetime import datetime

def main():
  gender = input("Enter your gender (M/F): ")
  birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
  weight = float(input("Enter your weight in pounds: "))
  feet = float(input("Enter your height in feet (no remainder): "))
  inches = float(input("Enter the remainder of height in inches: "))
  height = (feet * 12) + inches
  # ^ Variables ^ #

  converted_weight = kg_from_lb(weight)
  converted_height = cm_from_in(height)
  user_age = compute_age(birthdate)
  bmi = body_mass_index(converted_weight, converted_height)
  bmr = basal_metabolic_rate(gender, converted_weight, converted_height, user_age)

  # ^ Function Variables ^ #

  meters_height = converted_height / 100
  stone_weight = converted_weight * .157473

  # ^ Stretch Variables ^ #
  print()
  
  print(f"Age (Years): {user_age:.1f}")
  print(f"Weight (kg): {converted_weight:.1f}")
  print(f"Height (cm): {converted_height:.1f}")
  print(f"Body mass index: {bmi:.1f}")
  print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")
  
  # ^ Main Output ^ #
  
  print()
  print(f"Height (m): {meters_height:.2f}")
  print(f"Weight (stone): {stone_weight:.1f}")

  # ^ Stretch Output ^ #

  #

def compute_age(birth):
  birthday = datetime.strptime(birth, "%Y-%m-%d")
  today = datetime.now()
  years = today.year - birthday.year

  if birthday.month > today.month or (birthday.month == today.month and birthday.day > today.day): 
    years -= 1

  return years

def kg_from_lb(lb):
  kg = lb * 0.45359237
  return kg

def cm_from_in(inch):
  cm = inch * 2.54

  return cm

def body_mass_index(weight, height):
  bmi = (10000 * weight)/height**2

  return bmi

def basal_metabolic_rate(gender, weight, height, age):
  if gender.lower() == "f":
    bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
  else:
    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)

  return bmr

main()