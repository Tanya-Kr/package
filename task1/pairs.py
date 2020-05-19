import sys


def main():
    numbers_list = [int(numb) for numb in sys.argv[1:]]
    find_pairs_of_numbers(numbers_list, get_pair_sum())


def find_pairs_of_numbers(numbers, pair_sum):
    pairs_list = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == pair_sum:
                pairs_list.append(f"{numbers[i]} + {numbers[j]}")
    print('\n'.join(pairs_list))


def get_pair_sum():
    return int(input("Enter pairs sum: "))


if __name__ == '__main__':
    main()