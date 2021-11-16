from print_data import print_data_for_periods


def calculate_percentage_diff(all_period_dict):
    count = 1
    users_periods = []
    period_key_check = []
    print('\nChoose two periods from the options below:\n')
    for keys in all_period_dict:
        print(f"Period {count}: {keys[1]} with weekly revenue of {all_period_dict[keys][0]}")
        period_key_check.append(keys[0].lower())
        count += 1
    print()

    while len(users_periods) < 2:
        if len(users_periods) == 0:
            get_first_period = input('Enter the first period for the comparison: ').lower().strip()
            check_if_valid = True if get_first_period.strip().lower() in period_key_check else False
            if check_if_valid:
                users_periods.append(get_first_period.strip())
            else:
                print('Invalid period, please select a valid period.')
        if len(users_periods) == 1:
            get_second_period = input('Enter the second period for the comparison: ').lower().strip()
            check_if_valid = True if get_second_period.strip().lower() in period_key_check else False
            if check_if_valid:
                users_periods.append(get_second_period.strip())
            else:
                print('Invalid period, please select a valid period.')

    periods_to_find_avgs_for = {}
    dates_for_user_keys = {}
    for keys in all_period_dict.keys():
        if keys[0].lower() in users_periods:
            periods_to_find_avgs_for[keys[0]] = [keys[1]] + all_period_dict[keys]
            dates_for_user_keys[keys[0].lower()] = keys[1]

    print(f"You have chosen {users_periods[0].title()} which correlates to the {dates_for_user_keys[users_periods[0]]} period"
          f" and {users_periods[1].title()} which correlates to the {dates_for_user_keys[users_periods[1]]} period.\n")

    print_data_for_periods(all_period_dict, users_periods)

    calc_diff = float(periods_to_find_avgs_for[users_periods[0].title()][1][1:]) - float(periods_to_find_avgs_for[users_periods[1].title()][1][1:])
    print(f"Revenue during {periods_to_find_avgs_for[users_periods[0].title()][0]} period was {periods_to_find_avgs_for[users_periods[0].title()][1]}\n"
          f"Revenue during {periods_to_find_avgs_for[users_periods[1].title()][0]} period was {periods_to_find_avgs_for[users_periods[1].title()][1]}\n"
          f"Difference in revenue is ${round(calc_diff, 2)}\n"
          f"${round(calc_diff, 2)} as a percentage of pre-lockdown revenue of ${float(periods_to_find_avgs_for[users_periods[0].title()][1][1:])}"
          f" is {round(calc_diff / float(periods_to_find_avgs_for[users_periods[0].title()][1][1:]) * 100, 2)}%")