"""
Ajay Shah, Jack Kjar, Shreyas Sao
CSE 163
This file tests the functions in data_analysis.py on smaller data files in the
test_data folder. The tests run inside test_data, so none of our real data
files are being used, read, or overwritten.
"""
import os
import io
import contextlib

import data_analysis

TEST_FOLDER = 'test_data'

def run_analysis()->str:
    '''
    Runs the main method in data_analysis.py and returns everything it prints
    '''
    start_folder = os.getcwd()
    os.chdir(TEST_FOLDER)

    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        data_analysis.main()

    os.chdir(start_folder)

    return output.getvalue()

def test_shapes(output: str) -> None:
    '''
    Tests to see if the merged shape sizes work for the smaller testing datasets
    '''
    assert '(Rows,Columns) Merged:(4, 6). Injuries:(5, 5)' in output


def test_missing_outputs(output: str) -> None:
    '''
    Tests to see if the merged datasets have any missing values
    '''
    assert 'rest_days     0' in output
    assert 'injuries      0' in output
    assert 'report_status    1' in output


def test_describe(output: str) -> None:
    '''
    Tests the describe method
    '''
    assert 'mean   2024.0  1.400000' in output
    assert 'mean     1.500000  2019.0  1.50000    7.00000       0.5' in output
    assert 'min      0.000000  2019.0  1.00000    4.00000       0.0' in output
    assert '25%      0.750000  2019.0  1.00000    6.25000       0.0' in output
    assert '50%      1.500000  2019.0  1.50000    7.00000       0.0' in output
    assert '75%      2.250000  2019.0  2.00000    7.75000       0.5' in output
    assert 'max      3.000000  2019.0  2.00000   10.00000       2.0' in output


def test_counts(output: str) -> None:
    '''
    Tests the counts of Positions, Statuses, and Teams 
    '''
    assert 'WR    2' in output
    assert 'QB    1' in output
    assert 'Out             3' in output
    assert 'Questionable    1' in output
    assert 'LAC    1' in output
    assert 'SEA    3' in output


def main() -> None:
    output = run_analysis()
    test_shapes(output)
    test_missing_outputs(output)
    test_describe(output)
    test_counts(output)
    print("All tests passed!")


if __name__ == '__main__':
    main()
