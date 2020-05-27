import glob
from package.task5.timer import Timer
from package.task5.management_file import FileManagement


def main():
    with FileManagement("timing") as timing_file:
        with Timer() as timer:
            answers = get_answers(read_answers)
            timing_file.write(f"Received answers to questions from Questionnaire "
                              f"in {str(round(timer.time_elapsed, 2))} seconds\n")
    create_all_answers_file(answers)


def get_sections_path():
    return glob.glob("Questionnaire/*.txt")


def get_questions(file_path):
    file = open(file_path)
    user_answers = {}
    for line in file:
        user_answers[line.replace("\n", "")] = input(f"{line} ")
    file.close()
    return user_answers


def read_answers(sections_path):
    with FileManagement("timing") as timing_file:
        i = 0
        while i < len(sections_path):
            with Timer() as timer:
                yield get_questions(sections_path[i])
                timing_file.write(f"Received answers to questions from {sections_path[i]} "
                                  f"in {str(round(timer.time_elapsed, 2))} seconds\n")
                i += 1


def get_answers(read_answers):
    answers_list = {}
    for i in read_answers(get_sections_path()):
        answers_list.update(i)
    return answers_list


def create_all_answers_file(answers):
    file_name = input('File name: ')
    with FileManagement(file_name) as answers_file:
        for key in answers:
            answers_file.write(f"{str(key)} {str(answers[key])}\n")


if __name__ == '__main__':
    main()