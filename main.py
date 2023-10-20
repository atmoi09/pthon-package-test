# from config.py import config_value_1, config_value_2, config_value_3

# import config
from config import config_value_1, config_value_2, config_value_3


def read_config_value_1():
    return config_value_1


def complicated_function(value):
    if value == config_value_2:
        return "Value matches config_value_2"
    elif value > config_value_2:
        return "Value is greater than config_value_2"
    else:
        return "Value is less than config_value_2"


def my_function():
    value = 3
    result = complicated_function(value)
    if result == "Value is less than config_value_2":
        return value * read_config_value_1()
    elif result == "Value is greater than config_value_2":
        return value / read_config_value_1()
    else:
        return value


def my_new_function(value):
    return value * config_value_3


print(my_function())
