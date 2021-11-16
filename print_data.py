def print_data_for_periods(dict_of_all_periods, user_chosen_periods):
    print("Here is the total data corresponding to both periods:")
    for keys in dict_of_all_periods.keys():
        if keys[0].lower() in user_chosen_periods:
            period_title = keys[1]
            print('=' * len(keys[0]))
            print(f"{keys[0]}")
            print('=' * len(keys[0]))
            print(f"Date: {period_title}")
            print(f"Revenue: {dict_of_all_periods[keys][0]}")
            print(f"Resurgence Payments: {dict_of_all_periods[keys][1]}")
            print(f"Rental Payments: {dict_of_all_periods[keys][2]}\n")


