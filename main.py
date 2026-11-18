"""
Jack Kjar, Shreyas Sao, Ajay Shah
CSE 163
This file contains a script that runs all of our code for the EDA, including
data cleaning, analysis, and visualization.
"""
import data_cleaning
import data_analysis
import variable_visualizations


def main() -> None:
    """
    Calls all of our data cleaning, analysis, and visualization functions.
    """
    data_cleaning.main()
    data_analysis.main()
    variable_visualizations.main()


if __name__ == "__main__":
    main()
