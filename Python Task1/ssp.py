def categorize_numbers(list):

  output_dict = {"positive": [], "negative": [], "zero": []}
  for number in list:
    if number > 0:
      output_dict["positive"].append(number)
    elif number < 0:
      output_dict["negative"].append(number)
    else:
      output_dict["zero"].append(number)
  return output_dict

input_list = [1, -2, 3, 0, -5, 0, 4]
output_dict = categorize_numbers(input_list)
print(output_dict)