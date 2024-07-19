def process_numbers_v2(input_list):

  modified_list = [num if num > 0 else 0 for num in input_list]
  positive_sum = sum(num for num in modified_list if num > 0)
  return modified_list, positive_sum

# Example usage
input_list = [1, -2, 3, -4, 5]
output_list, positive_sum = process_numbers_v2(input_list)
print(output_list)  
print(positive_sum)