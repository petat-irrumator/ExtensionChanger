import os

dir_user_input = input('Directory: ')
extension_user_input = input('Extension to be added (with .): ')
extension_space_number = 16
output_file_name_var = 'OUTPUT.txt'
newline_output_file_name_var = 'NewLine'+output_file_name_var
# a function that gets a list of files in a given directory then puts that list in  two text files whose names is given by output_file_name


def directory_getter(dir, output_file_name):

    raw_dir_list = os.listdir(dir)
    ouput_file = open(output_file_name, 'w')
    with_new_line_output_file = open(newline_output_file_name_var, 'w')

    for directory in raw_dir_list:
        ouput_file.write(str(directory))
        with_new_line_output_file.write(str(directory+'\n'))

    ouput_file.close()
    with_new_line_output_file.close()
    print(
        f'RawDirectory list is in {output_file_name} and NewLine{output_file_name}')


directory_getter(dir_user_input, output_file_name_var)

# a function that takes an input txt file (full of file names where extensions are to be added) and then adds an specified extension in every file name in that txt file.Function also takes a number of character after which the extension is to add for example: in notes after 5 characters we want to add .txt
# add the extension name with dot e.g : .txt OR .png


def filename_extension_adder(input_file_name, extension_space, input_extension):

    input_file = open(input_file_name, 'r')
    contents_of_input_file = input_file.read()

    list_based_on_extension_space = [contents_of_input_file[i:i+extension_space]
                                     for i in range(0, len(contents_of_input_file)+1, extension_space)]

    extension_to_add = input_extension+'\n'
    extension_added_list = extension_to_add.join(list_based_on_extension_space)

    output_list = []
    temporary_list = []

    for name in extension_added_list:
        if name == '\n':
            output_list.append(''.join(temporary_list))
            temporary_list = []
        else:
            temporary_list.append(name)
    else:
        if temporary_list:
            output_list.append(''.join(temporary_list))

    return output_list


output_list = filename_extension_adder(
    'OUTPUT.txt', extension_space_number, extension_user_input)

# a function that finally renames the files


def rename_file(newline_output_format):

    newline_output_file = open(newline_output_format, 'r')
    newline_output_file_list = newline_output_file.readlines()

    modified_newline_output_file_list = []

    for entry in newline_output_file_list:
        item = entry.strip('\n')
        modified_newline_output_file_list.append(item)

    for item in range(modified_newline_output_file_list.__len__()):

        src = modified_newline_output_file_list[item]

        for entry in range(output_list.__len__()):

            dest = output_list[entry]
            to_compare = dest[:extension_space_number]

            if src == to_compare:

                os.rename(f'{dir_user_input}/{src}',
                          f'{dir_user_input}/{dest}')


rename_file(newline_output_file_name_var)

print(
    f'All the files in {dir_user_input} are renamed with extension {extension_user_input}')

os.remove(output_file_name_var)
os.remove(newline_output_file_name_var)
