import glob
from contextlib import contextmanager
from package.task5.timer import Timer


QUESTIONS_DIRECTORY_PATH = "Questionnaire"
QUESTIONNAIRE_FILE_PATH = "questionnaire.txt"
TIMING_FILE_PATH = "timing.txt"


def main():
    files_path_list = glob.glob(QUESTIONS_DIRECTORY_PATH + "/*.txt")

    with file_manager(TIMING_FILE_PATH, "a") as timing_file:
        with Timer() as timer:
            filled_questionnaire = get_user_answers(files_path_list)
            timing_file.write(f"Received answers to questions from {QUESTIONS_DIRECTORY_PATH} "
                              f"in {str(timer.time_elapsed)} seconds\n")

    create_questionnaire_file(filled_questionnaire)


def get_user_answers(files_path_list) -> dict:
    """Open each questionnaire file. Display all questions line by line in console. Get answer for each question.
    :return all_answers(dict) with question(key), answer(value)"""
    with file_manager(TIMING_FILE_PATH, "a+") as timing_file:
        filled_questionnaire = {}
        for file_path in files_path_list:
            with file_manager(file_path, "r") as questionnaire_file:
                with Timer() as timer:

                    for question in questionnaire_file:
                        user_answer = input(str(question.replace("\n", " ")))
                        filled_questionnaire[question.replace("\n", " ")] = user_answer

                    timing_file.write(f"Received answers to questions from {file_path} "
                                      f"in {str(timer.time_elapsed)} seconds\n")
        return filled_questionnaire


def create_questionnaire_file(filled_questionnaire):
    """Fill questionnaire file by questions and user answers.
    :param filled_questionnaire(dict) with question(key), answer(value)"""
    with file_manager(QUESTIONNAIRE_FILE_PATH) as questionnaire_file:
        for question in filled_questionnaire:
            questionnaire_file.write(f"{str(question)} {str(filled_questionnaire[question])}\n")

    print("Questionnaire file with <question> : <answer> was created. "
          "File with tracking time answering in each file and the total time "
          "filling out the questionnaire was created.")


@contextmanager
def file_manager(name, mode="w"):
    file = open(name, mode)
    try:
        yield file
    finally:
        file.close()


if __name__ == '__main__':
    main()