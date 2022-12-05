def arithmetic_arranger(problems, answers = False):
  first = []
  second = []
  third = []
  final_answers = []
  # declaring lists for later on
  for problem in problems:
    if len(problems) > 5:
      return "Error: Too many problems."
    else:
      conv = problem.split()
      if conv[1] == "*" or conv[1] == "/":
        return "Error: Operator must be '+' or '-'."
      elif len(conv[0]) > 4 or len(conv[2]) > 4:
        return"Error: Numbers cannot be more than four digits."
      elif conv[0].isnumeric() == False or conv[2].isnumeric() == False:
        return "Error: Numbers must only contain digits."
        # numerous conditionals to ensure the function input is suitable
      else:
        first.append(conv[0])
        second.append(conv[1])
        third.append(conv[2])
        changed = str(' '.join(conv))
        answer = eval(changed)
        final_answer = str(answer)
        final_answers.append(final_answer)
        # splitting the equations and appending them to lists, as well as working out the calculations

  top_list = []
  bottom_list = []
  dashes_list = []
  spaces = "    "
  for a in range(len(second)):
    top_list.append("  ")
    if second[a] == "-":
      bottom_list.append("- ")
    else:
      bottom_list.append("+ ")
# applying the constant to the strings in the list i.e. " +" or " -" on the bottom and "  " on the top
  for b in range(len(problems)):
    difference = len(first[b]) - len(third[b])
    if difference > 0:
      diff = str(difference * " ")
      bottom_list[b] = bottom_list[b] + diff
    else:
      difference = difference * -1
      diff = str(difference * " ")
      top_list[b] = top_list[b] + diff
      # working out which number has the longer length and applying the gap in space to the shorter number
  for c in range(len(problems)):
    top_list[c] = top_list[c] + first[c]
    bottom_list[c] = bottom_list[c] + third[c]
    dashes_list.append(len(bottom_list[c]) * "-")
    # adding the numbers to the lists, as well as the dashes
  top_arranged = ""
  bottom_arranged = ""
  dashes_arranged = ""
  for d in range(len(problems)):
    top_arranged += top_list[d]
    bottom_arranged += bottom_list[d]
    dashes_arranged += dashes_list[d]
    if d == len(problems) - 1:
      break
    else:
      top_arranged += spaces
      bottom_arranged += spaces
      dashes_arranged += spaces
      # adding the strings in the lists to a string and breaking at the end to ensure no extra spaces

  arranged_numbers = ""
  arranged_numbers = top_arranged + "\n" + bottom_arranged + "\n" + dashes_arranged
  final_string = ""
  # moving the strings into the same string
  for n in range(len(problems)):
    answers_spaces = len(dashes_list[n]) - len(final_answers[n])
    answers_spaces = str(answers_spaces * " ")
    final_string += answers_spaces + final_answers[n]
    # adding the spaces and answers to a string, as well as ensuring no extra spaces at the end
    if n == len(problems) - 1:
      break
    else:
      final_string += spaces
  if answers != False:
    arranged_numbers = arranged_numbers + "\n" + final_string
    return arranged_numbers
  else:
    return arranged_numbers
    # returning the arranged numbers in whichever form is specified

# main code to test the function
if __name__=="__main__":
    while True:
        values = input("Please provide a list of calculations (no more than five) seperated by commas that are either addition or subtraction: ")
        if values != "":
            break
    values_list = values.split(',')
    nums = []
    for i in range(len(values_list)):
        nums.append(values_list[i])
print(arithmetic_arranger(nums, True))