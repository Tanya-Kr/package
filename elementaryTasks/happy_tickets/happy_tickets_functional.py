def main():
    comparison_calculation_methods(get_min_ticket_numb(), get_max_ticket_numb())



def get_min_ticket_numb():
    return int(input("Enter min ticket number: "))


def get_max_ticket_numb():
    return int(input("Enter max ticket number: "))


def easy_way_to_count_happy_tickets(ticket):
    first_part_ticket = 0
    for numb in ticket[:3]:
        first_part_ticket += int(numb)

    second_part_ticket = 0
    for numb in ticket[3:]:
        second_part_ticket += int(numb)

    return first_part_ticket == second_part_ticket


def hard_way_to_count_happy_tickets(ticket):
    even_numb_sum = 0
    odd_numb_sum = 0
    for numb in ticket:
        if int(numb)%2 == 0:
            even_numb_sum += int(numb)
        else:
            odd_numb_sum += int(numb)

    return even_numb_sum == odd_numb_sum


def comparison_calculation_methods(min, max):
    happy_tickets_easy_way = 0
    happy_tickets_hard_way = 0
    if int(min) < int(max):
        for i in range(int(min), int(max)):
            if easy_way_to_count_happy_tickets(str(i)):
                happy_tickets_easy_way += 1

            if hard_way_to_count_happy_tickets(str(i)):
                happy_tickets_hard_way += 1

    if happy_tickets_easy_way > happy_tickets_hard_way:
            ""


if __name__ == '__main__':
    main()



