"""
Jack Kjar, Ajay Shah, Shreyas Sao
CSE 163 AE
This file contains a script that runs all of our testing code.
"""

import test_data_analysis
import test_data_cleaning


def main() -> None:
    test_data_cleaning.main()
    test_data_analysis.main()


if __name__ == "__main__":
    main()
