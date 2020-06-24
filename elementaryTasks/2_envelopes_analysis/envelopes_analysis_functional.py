def main():
    flag = True
    while flag:
        print(envelopes_analysis(get_envelopes_size("first"), get_envelopes_size("second")))
        flag = input("Do you want to continue(y/n): ").lower() == ("y" or "yes")


def get_envelopes_size(envelope_number):
    return [input(f"Enter {envelope_number} envelope width: "),
            input(f"Enter {envelope_number} envelope height: ")]


def envelopes_analysis(first_env_size, second_env_size):
    first_env_size.sort()
    second_env_size.sort()
    if (first_env_size[0] < second_env_size[0]) and (first_env_size[1] < second_env_size[1]):
        result = "You can put the first envelope in the second one"
    elif (second_env_size[0] < first_env_size[0]) and (second_env_size[1] < first_env_size[1]):
        result = "You can put the second envelope in the first one"
    else:
        result = "You cannot put one envelope in another"

    return result


if __name__ == '__main__':
    main()

