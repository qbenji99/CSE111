# TOP #
import csv



def read_students(filename, key_index):
  student_dict = {}
  with open(filename, "rt") as csv_file:
    reader = csv.reader(csv_file)

    next(reader)

    for student in reader:
      key = student[key_index]
      student_dict[key] = student

  return student_dict



def main():

  I_NUMBER_INDEX = 0
  STUDENT_NAME_INDEX = 1

  data = read_students("students.csv", I_NUMBER_INDEX)
  print(data)
  input_id = input("Enter student ID: ")
  input_id = input_id.replace("-", "")

  if len(input_id) > 9:
    print("WRONG. too many digits. are you kidding me?? what are you, 12?")

  elif len(input_id) < 9:
    print("WRONG. too few digits. don't be dumb")

  elif input_id.isdigit() == False:
    print("WRONG I-NUMBER. Yolki Palki" )

  else:
    if input_id in data:
      value = data[input_id]

      student_name = value[STUDENT_NAME_INDEX]

      print(student_name)
    else:
      print("No such student")



if __name__ == "__main__":
  main()

# BOTTOM #