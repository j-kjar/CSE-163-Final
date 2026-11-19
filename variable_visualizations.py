"""
Jack Kjar, Ajay Shah, Shreyas Sao
CSE 163
This file contains a script that creates a visualization for every variable
of interest outlined in our report.
"""
import pandas as pd
import plotly.express as px


def visualizations() -> None:
    """
    Creates a visualization for every variable of interest in our report.
    """
    injuries = pd.read_csv("cleaned_injuries.csv")
    merged = pd.read_csv("games_and_injuries.csv")

    ireport_counts = injuries["report_status"].value_counts()
    ireports = px.bar(
        x=ireport_counts.index,
        y=ireport_counts.to_numpy(),
        labels={"x": "Report Status", "y": "Number of entries"},
        title="Number of entries per report status in "
              "cleaned_injuries.csv (2012-2025)"
    )
    ireports.write_html("injuries_report_status.html")

    iseason_counts = injuries["season"].value_counts()
    iseasons = px.bar(
        x=iseason_counts.index,
        y=iseason_counts.to_numpy(),
        labels={"x": "Season", "y": "Number of entries"},
        title="Number of entries per season in "
              "cleaned_injuries.csv (2012-2025)"
    )
    iseasons.write_html("injuries_season.html")

    iweek_counts = injuries["week"].value_counts()
    iweeks = px.bar(
        x=iweek_counts.index,
        y=iweek_counts.to_numpy(),
        labels={"x": "Week", "y": "Number of entries"},
        title="Number of entries per week in "
              "cleaned_injuries.csv (2012-2025)"
    )
    iweeks.write_html("injuries_week.html")

    iteam_counts = injuries["team"].value_counts()
    iteams = px.bar(
        x=iteam_counts.index,
        y=iteam_counts.to_numpy(),
        labels={"x": "Team", "y": "Number of entries"},
        title="Number of entries per team in "
              "cleaned_injuries.csv (2012-2025)"
    )
    iteams.write_html("injuries_team.html")

    ipos_counts = injuries["position"].value_counts()
    ipositions = px.bar(
        x=ipos_counts.index,
        y=ipos_counts.to_numpy(),
        labels={"x": "Position", "y": "Number of entries"},
        title="Number of entries per position in "
              "cleaned_injuries.csv (2012-2025)"
    )
    ipositions.write_html("injuries_positions.html")

    mseason_counts = merged["season"].value_counts()
    mseasons = px.bar(
        x=mseason_counts.index,
        y=mseason_counts.to_numpy(),
        labels={"x": "Season", "y": "Number of entries"},
        title="Number of entries per season in "
              "games_and_injuries.csv (2012-2025)"
    )
    mseasons.write_html("merged_season.html")

    mweek_counts = merged["week"].value_counts()
    mweeks = px.bar(
        x=mweek_counts.index,
        y=mweek_counts.to_numpy(),
        labels={"x": "Week", "y": "Number of entries"},
        title="Number of entries per week in "
              "games_and_injuries.csv (2012-2025)"
    )
    mweeks.write_html("merged_week.html")

    mteam_counts = merged["team"].value_counts()
    mteams = px.bar(
        x=mteam_counts.index,
        y=mteam_counts.to_numpy(),
        labels={"x": "Team", "y": "Number of entries"},
        title="Number of entries per team in "
              "games_and_injuries.csv (2012-2025)"
    )
    mteams.write_html("merged_team.html")

    mrest_counts = merged["rest_days"].value_counts()
    mrest = px.bar(
        x=mrest_counts.index,
        y=mrest_counts.to_numpy(),
        labels={"x": "Rest Days", "y": "Number of entries"},
        title="Number of entries per rest day in "
              "games_and_injuries.csv (2012-2025)"
    )
    mrest.write_html("merged_rest_days.html")

    minjuries_counts = merged["injuries"].value_counts()
    minjuries = px.bar(
        x=minjuries_counts.index,
        y=minjuries_counts.to_numpy(),
        labels={"x": "Number of Injuries", "y": "Number of entries"},
        title="Number of entries per number of injuries in "
              "games_and_injuries.csv (2012-2025)"
    )
    minjuries.write_html("merged_injuries.html")


def main():
    visualizations()
    print("All visualizations created!")


if __name__ == "__main__":
    main()
