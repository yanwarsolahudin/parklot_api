from django.shortcuts import render


def calculate_long_term_park(checkin, checkout):
    diff = checkout - checkin

    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    # minutes = (seconds % 3600) // 60
    # seconds = seconds % 60
    if hours == 0:
        hours = 1

    return hours


def calculate_payment(hours):
    if hours == 1:
        return 4
    elif hours > 1 or hours <= 2:
        return 3.5
    else:
        return 2.5 * hours
