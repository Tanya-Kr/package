import os


def main():
    total_file_statistic(get_file_name())


def total_file_statistic(file_path):
    file_name = open(file_path)
    tuple_file_name = tuple(file_name)
    static_text = []
    print("File: " + os.path.abspath('run2019.txt'))
    static_text.append("total lines:      " + str(len([line.strip() for line in tuple_file_name])))
    static_text.append("empty lines:      " + str(len([line for line in tuple_file_name if not line.strip()])))
    static_text.append("""lines with "z":   """ + str(len([line for line in tuple_file_name if line.find('z') != -1])))
    static_text.append(""""z" count":       """ + str((' '.join(tuple_file_name)).count("z")))
    static_text.append("""lines with "and": """ + str(len([line for line in tuple_file_name if line.find('and') != -1])))
    print('\n'.join(static_text))
    file_name.close()
    continue_or_close_program()


def get_file_name():
    return str(input("Enter file name: "))


def continue_or_close_program():
    print("Do you want make another file statistic (yes / no)")
    user_answer = input()
    if user_answer == "yes":
        total_file_statistic(get_file_name())
    else:
        print("Thanks for using our program")


if __name__ == '__main__':
    main()
