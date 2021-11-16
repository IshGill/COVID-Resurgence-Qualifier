def print_all_time_period_data(time_period_data):
    values_dict = {'Time Period': 0, 'Revenue': 1, 'Resurgence Payments': 2, 'Rental Payments': 3}
    for current_period in time_period_data:
        print('=' * 200)
        current_period_clean1 = current_period[values_dict['Time Period']][
                                :current_period[values_dict['Time Period']].rfind(' ')]
        current_period_cleaned = current_period_clean1[:current_period_clean1.rfind(' ')]
        print(f"Time Period: {current_period_cleaned}")
        print(f"Revenue: {current_period[values_dict['Revenue']]}")
        print(f"Resurgence Payments: {current_period[values_dict['Resurgence Payments']]}")
        print(f"Rental Payments: {current_period[values_dict['Rental Payments']]}")
        print('=' * 200)