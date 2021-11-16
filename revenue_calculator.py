import csv
from find_average import calculate_average
from find_percentage_diff import calculate_percentage_diff
from print_all_time import print_all_time_period_data


def calculate_revenue(f):
    revenue = 0
    resurgence_payments = []
    rental_income = []
    found_non_revenue_item = False
    try:
        with open(f, 'r') as file:
            file_name = str(file.name)
            period = file_name[file_name.rfind('/') + 1:-4].replace('_', " ").replace('-', ' ').strip().replace("  ", " ")
            reader = csv.reader(file)
            unaccountable_income = set()
            user_done = False
            while not user_done:
                get_unaccountable_income = input(
                    'Enter keyword for income/revenue which you do not want to account for: ')
                if get_unaccountable_income == '' or get_unaccountable_income.strip() is None:
                    print(get_unaccountable_income)
                    user_done = True
                else:
                    unaccountable_income.add(get_unaccountable_income.strip())
            for row in reader:
                if row:
                    find_resurgence_payment = row[5].strip()
                    find_rental_income = row[5].strip()
                    if find_resurgence_payment.lower() in unaccountable_income:
                        if row[-1] == '':
                            resurgence_payments.append([find_resurgence_payment.upper(), 'Removed from CSV'])
                        else:
                            resurgence_payments.append([find_resurgence_payment.upper(), float(row[-1])])
                        found_non_revenue_item = True

                    if 'rent' in find_rental_income.lower():
                        if row[-1] == '':
                            rental_income.append([find_rental_income.upper(), 'Removed from CSV'])
                        else:
                            rental_income.append([find_rental_income.upper(), float(row[-1])])
                        found_non_revenue_item = True

                    if found_non_revenue_item:
                        found_non_revenue_item = False
                        continue

                    if not row[-1].isalpha() and not row[-1].strip() == '' and float(row[-1]) > 0:
                        revenue += float(row[-1])

            file.close()
    except FileNotFoundError:
        print("No such file exists in your directory!")
        return False, False, False, False
    return round(revenue, 2), period, resurgence_payments, rental_income


def main():
    file_name_list = []
    check_finished = True
    while check_finished:
        get_file_names = input("Please enter the file name: ")
        file_name_list.append(get_file_names)
        user_done = input("Press Y if done: ")
        if user_done.lower().strip() == 'y':
            check_finished = False

    list_of_revenues = []
    valid_file_flag = False
    for file in file_name_list:
        calculated_revenue, time_period, resurgence, rental_revenue = calculate_revenue(file.replace('\\', '/'))
        if calculated_revenue:
            valid_file_flag = True
            calculated_revenue = calculate_average(time_period, calculated_revenue)
            list_of_revenues.append([time_period, f"${calculated_revenue}",
                                     f"{len(resurgence)} {'payment' if len(resurgence) == 1 else 'payments'} of "
                                     f"{[(payment + 1, '$' + str(resurgence[payment][1])) if resurgence[payment][1] != 'Removed from CSV' else (payment + 1, resurgence[payment][1]) for payment in range(len(resurgence))]}"
                                     f" from {[(provider + 1, resurgence[provider][0]) for provider in range(len(resurgence))]}"
                                     if resurgence else 'No resurgence payments during this period',
                                     f"{[(rent + 1, '$' + str(rental_revenue[rent][1])) for rent in range(len(rental_revenue))]}"
                                     f" from {[(provider + 1, rental_revenue[provider][0]) for provider in range(len(rental_revenue))]}"
                                     if rental_revenue else 'No rental payments during this period'])

    if valid_file_flag:
        print_all_time_period_data(list_of_revenues)
        dict_of_periods = {(f"Period {x+1}", list_of_revenues[x][0]): list_of_revenues[x][1:] for x in range(len(list_of_revenues))}
        if len(list_of_revenues) > 1:
            calculate_percentage_diff(dict_of_periods)


main()

