from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """

    celsius = (fahrenheit_temp - 32) * 5 / 9
    return round(celsius, 2)
    # pass  # remove pass statement and implement me


def convert_to_fahrenheit(celsius_temp: float) -> int:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    fahr = (celsius_temp * 9 / 5) + 32
    return round(fahr, 2)
    # pass  # remove pass statement and implement me


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    outtup = []
    for temp in temperatures:
        if input_unit_of_measurement == 'c':
            # outTup[1] = convert_to_fahrenheit(temp)
            outtup.append((temp, convert_to_fahrenheit(temp)))
        elif input_unit_of_measurement == 'f':
            # outTup[1] = convert_to_celsius(temp)
            outtup.append((temp, convert_to_celsius(temp)))
        else:
            # outtup.append((temp,'invalid type'))
            break

    # Converted = (temp, conv_temp) # OUTPUT FORMAT
    return tuple(outtup)
    # tt = (), input_unit_of_measurement
    # for temp in tt:
    #     tt[temperatures] = convert_to_fahrenheit(temperatures)
    # return tt
    # pass  # remove pass statement and implement me
