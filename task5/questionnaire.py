import glob
import time
from contextlib import contextmanager


QUESTIONS_DIRECTORY_PATH = "Questionnaire"
QUESTIONNAIRE_FILE_PATH = "questionnaire.txt"
TIMING_FILE_PATH = "timing.txt"


def main():
    files_path_list = glob.glob(QUESTIONS_DIRECTORY_PATH + "/*.txt")

    with timing(QUESTIONS_DIRECTORY_PATH):
        filled_questionnaire = get_user_answers(files_path_list)

    create_questionnaire_file(filled_questionnaire)

    print("Questionnaire file with <question> : <answer> was created. "
          "File with tracking time answering in each file and the total time "
          "filling out the questionnaire was created.")


def get_user_answers(files_path_list: list) -> dict:
    """Open each questionnaire file. Display all questions line by line in console. Get answer for each question.
    :param files_path_list(list) with file path.
    :return all_answers(dict) with question(key), answer(value)."""
    filled_questionnaire = {}
    for file_path in files_path_list:
        with timing(file_path), file_manager(file_path, "r") as questionnaire_file:
            for question in questionnaire_file:
                question = question.replace("\n", "")
                filled_questionnaire[question] = input(question)

    return filled_questionnaire


def create_questionnaire_file(filled_questionnaire: dict) -> None:
    """Fill questionnaire file by questions and user answers.
    :param filled_questionnaire(dict) with question(key), answer(value)."""
    with file_manager(QUESTIONNAIRE_FILE_PATH) as questionnaire_file:
        for question in filled_questionnaire:
            questionnaire_file.write(f"{question} {filled_questionnaire[question]}\n")


@contextmanager
def file_manager(file_path: str, mode:str="a+") -> None:
    """Context manager to open and close file.
    :param file_path(str), mode(str)"""
    file = open(file_path, mode)
    try:
        yield file
    finally:
        file.close()


@contextmanager
def timing(path: str) -> None:
    """Context manager to tracking time of executing some function. Elapsed time is written to a file.
    :param path(str) of directory or file."""
    with file_manager(TIMING_FILE_PATH) as timing_file:
        start = time.time()
        yield
        elapsed_time = round((time.time() - start), 1)
        timing_file.write(f"End {path} in {elapsed_time} seconds\n")


if __name__ == '__main__':
    main()