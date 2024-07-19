def filter_and_modify_strings(input_list):

  output_list = []
  for word in input_list:
    if 'a' in word:
      output_list.append(word.upper())
    else:
      output_list.append(word[::-1])
  return output_list

# Example usage
input_list = ["apple", "banana", "cherry", "date", "kiwi"]
output_list = filter_and_modify_strings(input_list)
print(output_list)