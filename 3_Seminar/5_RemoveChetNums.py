#5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 


def read_nums_from_file(file_name):
    nums_file = open(file_name, 'r')
    nums_input = [int(num) for num in nums_file.read().split()]
    nums_file.close()
    return nums_input

def write_nums_in_file(file_name, nums):
    nums_file = open(file_name, 'w')
    nums_file.write(nums)
    nums_file.close()

def remove_chet_num(nums):
    return [num for num in nums if num % 2 != 0]

def convert_nums_to_str(nums):
    nums_str = ' '.join(str(x) for x in nums)
    return nums_str

nums_input_file_name = u"nums_input.txt"
nums_output_file_name = u"nums_output.txt"
nums_input = read_nums_from_file(nums_input_file_name)

nums_output = convert_nums_to_str(remove_chet_num(nums_input))
write_nums_in_file(nums_output_file_name, nums_output)