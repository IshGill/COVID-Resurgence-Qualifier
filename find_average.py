def calculate_average(period, total_revenue):
    clean_period1 = period.strip()[:period.rfind(" ")]
    second_space_idx = clean_period1.rfind(" ")
    num_weeks = int(period[second_space_idx:period.rfind(" ")])
    return total_revenue if num_weeks <= 1 else round(total_revenue / num_weeks, 2)