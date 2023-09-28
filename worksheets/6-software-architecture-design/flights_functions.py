import pandas as pd


def get_key(line):
    """
    Given a single line of flight data, create a tuple that can be used as the
    basis for a sorting function.

    Args:
        line: A string representing the comma-separated column values.

    Returns:
        A tuple of the flight time, airport city name, and flight number to be
        used to sort the lines.
    """
    columns = line.strip().split(",")
    airport = columns[1]
    time = columns[3]
    flight_number = columns[4]

    # Separate the time into hour and minute to make comparisons between lines
    # easier.
    hh_mm_strings = time.split(":")
    hour = int(hh_mm_strings[0])
    minute = int(hh_mm_strings[1])

    return hour, minute, airport, flight_number


def chron_sort_nonpandas(input_file, output_file):
    # Read all of the lines into a list, without their ending newlines.
    lines = []
    with open(input_file, "r") as f:
        for line in f:
            lines.append(line.strip())

    # Use the get_key function and Python's tuple sorting to get the lines in
    # the correct order.
    sorted_lines = sorted(lines, key=get_key)

    with open(output_file, "w") as f:
        # The join function doesn't add a trailing newline usually put at the
        # end of files, so we have to add it ourselves.
        f.write("\n".join(sorted_lines) + "\n")


def chron_sort_pandas(input_file, output_file):
    # For importing into Pandas, we need to set the names of each column. This
    # also makes it easier to refer to specific columns later.
    column_names = ["Departure/Arrival", "Origin/Destination", "Code", "Time",
                    "Flight Number", "Airline", "Terminal"]
    # Pandas doesn't automatically interpret time strings as such, so we have to
    # manually tell it to do so with the appropriate column.
    data_frame = pd.read_csv(input_file, names=column_names, parse_dates=[3])

    # With Pandas, sorting can be done using the columns in order.
    sorted_data = data_frame.sort_values(by=[column_names[3], column_names[1],
                                             column_names[4]])

    # Pandas data frames will write the column header names and index by
    # default, so disable that. Also, ensure that the flight time is printed
    # only as the 24-hour time.
    sorted_data.to_csv(output_file, header=False, index=False,
                       date_format="%H:%M")


def chron_sort(input_file, output_file):
    """
    Sort a CSV of flight data chronologically, and write to a new file.

    Given a path to a CSV file containing flight data arranged into specific
    columns, sort the flights first by departure/arrival time, then by city
    name, then by flight number. Write this sorted data into a new file.

    The columns in the data are:

    * An `A` for arrival or `D` for departure
    * The origin/destination city
    * The origin/destination airport's IATA code
    * The flight time
    * The flight number
    * The terminal number or letter

    Args:
        input_file: A string representing the path to the input CSV file.
        output_file: A string representing the path to the output CSV file.
    """
    # This just uses one of the solutions above.
    chron_sort_nonpandas(input_file, output_file)
