from enum import Enum
from abc import ABC, abstractmethod
import sys


class Filter(ABC):
    @abstractmethod
    def name(self) -> str:
        """Provides a name of the rule (like FP005)."""
        pass

    @abstractmethod
    def matches(self, line: str) -> bool:
        """Returns True if a given line matches the filter, otherwise, returns False."""
        pass


class IsEndsDot(Filter):
    def name(self) -> str:
        return "FP001"

    def matches(self, line: str) -> bool:
        """Check if line ends with a dot"""
        return line.endswith(".") is True


class IsLessHundredCharacters(Filter):
    def name(self) -> str:
        return "FP002"

    def matches(self, line: str) -> bool:
        """Check if line is less than 100 characters"""
        return 0 < len(line) < 100


class HasMoreFiveLetterA(Filter):
    def name(self) -> str:
        return "FP003"

    def matches(self, line: str) -> bool:
        """Check if line has at least 5 a letters"""
        return line.count("a") > 5


class HasMoreThreeLetterZ(Filter):
    def name(self) -> str:
        return "FN201"

    def matches(self, line: str) -> bool:
        """Check if line has more than 3 z letters"""
        return line.count("z") > 3


class IsEmptyLine(Filter):
    def name(self) -> str:
        return "FN202"

    def matches(self, line: str) -> bool:
        """Check if line is an empty line"""
        return not line.strip()


class OnlyNonLetterCharacters (Filter):
    def name(self) -> str:
        return "FN203"

    def matches(self, line: str) -> bool:
        """Check if line consists only from non-letter characters"""
        return not line.isalpha()


class DisplayRules(Enum):
    isEndsDot = IsEndsDot()
    isLessHundredCharacters = IsLessHundredCharacters()
    hasMoreFiveLetterA = HasMoreFiveLetterA()


class DontDisplayRules(Enum):
    hasMoreThreeLetterZ = HasMoreThreeLetterZ()
    isEmptyLine = IsEmptyLine()
    onlyNonLetterCharacters = OnlyNonLetterCharacters()


class Option(ABC):
    def filter(self, lines: list):
        pass

    @staticmethod
    def get_option(option: str):
        
        if option == 'filter':
            return FilterOption()
        if option == 'annotate':
            return AnnotateOption()


class FilterOption(Option):
    def filter(self, file_lines: list) -> None:
        """Filtered lines. The line is displayed if the number of positive rules to which the line matches
        is more than negative ones.
        :param file_lines(list) of lines in given file"""
        for line in file_lines:
            line = line.strip()
            display_count = 0
            dont_display_count = 0

            for rule in DisplayRules:
                if rule.value.matches(line):
                    display_count += 1

            for rule in DontDisplayRules:
                if rule.value.matches(line):
                    dont_display_count += 1

            if display_count >= dont_display_count and display_count > 0:
                print(line)


class AnnotateOption(Option):
    def filter(self, file_lines: list) -> None:
        """Display the information about which rules are applicable for each line.
        :param file_lines(list) of lines in given file."""
        for line_number, line in enumerate(file_lines, 1):
            line_annatations = list()
            line = line.strip()

            for rule in DisplayRules:
                if rule.value.matches(line):
                    line_annatations.append(rule.value.name())

            for rule in DontDisplayRules:
                if rule.value.matches(line):
                    line_annatations.append(rule.value.name())

            print(f"{line_number}. {' '.join(line_annatations)}")


if __name__ == '__main__':
    option = Option.get_option(sys.argv[1])
    file_path = sys.argv[2]
    file = open(file_path, 'r')
    file_lines = file.readlines()
    file.close()
    option.filter(file_lines)
