def main():
    flag = True
    while flag:
        file_data = get_file_data(get_file_name())
        statistic = total_file_statistic(file_data)

        for key, value in statistic.items():
            print(f"{key:<20} {value}")

        flag = input("Do you want make another statistic file (yes / no): ").lower() == "yes"


def get_file_name() -> str:
    """:return File path"""
    return str(input("Enter file name: "))


def total_file_statistic(tuple_file_data: tuple) -> dict:
    """Return statistical info about the number of: total lines, empty lines, lines with 'z',
    'z' letters in the file, lines with 'and'."""
    static_text = {"total lines:": len([line.strip() for line in tuple_file_data]),
                   "empty lines:": len([line for line in tuple_file_data if not line.strip()]),
                   "lines with 'z':": len([line for line in tuple_file_data if line.find("z") != -1]),
                   "'z' count:": (' '.join(tuple_file_data)).count("z"),
                   "lines with 'and':": str(len([line for line in tuple_file_data if line.find("and") != -1]))}
    return static_text


def get_file_data(file_path: str) -> tuple:
    """Convert data from file into tuple."""
    file_data = open(file_path)
    tuple_file_data = tuple(file_data)
    file_data.close()
    return tuple_file_data


if __name__ == '__main__':
    main()
