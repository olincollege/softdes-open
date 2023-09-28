import pytest

from flights import PandasFlightSorter, LineFlightSorter


implementations = [PandasFlightSorter, LineFlightSorter]


test_cases = [
    ("data/flight_data_sample.csv", "data/flight_data_sample_sorted.csv"),
    ("data/flight_data.csv", "data/flight_data_sorted.csv"),
    ("data/flights_allsort.csv", "data/flights_allsort_sorted.csv"),
]


@pytest.mark.parametrize("implementation", implementations)
@pytest.mark.parametrize("input_file,expected", test_cases)
def test_chron_sort(implementation, input_file, expected, tmpdir):
    sorter = implementation(input_file)
    output_path = tmpdir.join("actual.csv")
    sorter.write_sorted(output_path)
    with open(output_path, "r") as output_file, \
         open(expected, "r") as expected_file:
        assert output_file.read() == expected_file.read()