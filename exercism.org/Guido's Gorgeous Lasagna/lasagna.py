EXPECTED_BAKE_TIME = 40 # in minutes


def bake_time_remaining(ActTime):
    return EXPECTED_BAKE_TIME - ActTime


def preparation_time_in_minutes(Num_lrs):
    return 2 * Num_lrs


def elapsed_time_in_minutes(Num_lrs, ActTime):
    return 2*Num_lrs + ActTime


# print(bake_time_remaining(30))
# print(preparation_time_in_minutes(2))
print(elapsed_time_in_minutes(3, 20))