from datetime import timedelta

def calculate_oee(availability, performance, quality):
    return availability * performance * quality

def calculate_availability(available_time, unplanned_downtime):
    return ((available_time - unplanned_downtime) / available_time) * 100

def calculate_performance(ideal_cycle_time, actual_output, available_operating_time):
    return ((ideal_cycle_time * actual_output) / available_operating_time) * 100

def calculate_quality(good_product, total_product):
    return (good_product / total_product) * 100
