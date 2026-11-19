"""
Ajay Shah, Jack Kjar, Shreyas Sao
CSE 163
This file tests the functions in data_cleaning.py on smaller data files in the
test_data folder. The tests run inside test_data, so none of our real data
files are being used, read, or overwritten.
"""
import os

import data_cleaning

TEST_FOLDER = 'test_data'


def test_clean_games() -> None:
    '''
    Tests the clean_games method
    '''
    games = data_cleaning.clean_games()

    assert len(games) == 2
    assert list(games['season']) == [2019, 2019]
    assert list(games.columns) == ['season', 'week', 'home_team',
                                   'away_team', 'home_rest', 'away_rest']
    assert list(games['home_team']) == ['LV', 'LAC']
    assert list(games['away_team']) == ['DEN', 'LV']


def test_clean_injuries() -> None:
    '''
    Test the clean_injuries method
    '''
    injuries = data_cleaning.clean_injuries()

    assert len(injuries) == 16
    assert sorted(injuries['season'].unique()) == list(range(2012, 2026))
    assert list(injuries.columns) == ['season', 'team', 'week', 'position',
                                      'report_status']
    assert 'STL' not in set(injuries['team'])
    assert 'OAK' not in set(injuries['team'])
    assert (injuries['team'] == 'CLE').sum() == 12
    assert (injuries['team'] == 'LA').sum() == 1
    assert (injuries['team'] == 'LV').sum() == 2


def test_count_outs() -> None:
    '''
    Tests the count_out method
    '''
    injuries = data_cleaning.clean_injuries()
    outs = data_cleaning.count_outs(injuries)

    assert len(outs) == 1
    assert outs['team'].iloc[0] == 'LV'
    assert outs['week'].iloc[0] == 1
    assert outs['injuries'].iloc[0] == 2


def test_team_rest() -> None:
    '''
    Test team_rest method
    '''
    rest = data_cleaning.team_rest(data_cleaning.clean_games())

    assert len(rest) == 4
    week2 = rest[rest['week'] == 2]
    lac = week2[week2['team'] == 'LAC']
    lv = week2[week2['team'] == 'LV']
    assert lac['rest_days'].iloc[0] == 4
    assert lv['rest_days'].iloc[0] == 10


def test_match_injuries_to_games() -> None:
    '''
    Tests the match_injuries_to_games method
    '''
    outs = data_cleaning.count_outs(data_cleaning.clean_injuries())
    rest = data_cleaning.team_rest(data_cleaning.clean_games())
    merged = data_cleaning.match_injuries_to_games(outs, rest)

    # Every team-game is kept, even ones with no injuries
    assert len(merged) == 4

    lv_week1 = merged[(merged['team'] == 'LV') & (merged['week'] == 1)]
    assert lv_week1['injuries'].iloc[0] == 2
    assert merged['injuries'].sum() == 2
    assert merged['injuries'].isna().sum() == 0

    assert os.path.exists('games_and_injuries.csv')


def main() -> None:
    start_folder = os.getcwd()
    os.chdir(TEST_FOLDER)
    test_clean_games()
    test_clean_injuries()
    test_count_outs()
    test_team_rest()
    test_match_injuries_to_games()
    os.chdir(start_folder)
    print('All tests passed')


if __name__ == '__main__':
    main()
