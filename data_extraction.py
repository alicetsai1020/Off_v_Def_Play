import time
import requests
import pandas as pd


def get_teams_and_players():
    from nba_api.stats.static import teams
    from nba_api.stats.static import players
    
    teams_df = pd.DataFrame(teams.get_teams())
    players_df = pd.DataFrame(players.get_players())
    
    return teams_df, players_df

def get_gamelog():
    from nba_api.stats.endpoints import leaguegamelog
    
    game_log = leaguegamelog.LeagueGameLog(counter = 0, direction = "DESC",
                    league_id = "00", player_or_team_abbreviation = "T", season = "2018-19",
                    season_type_all_star = "Regular Season", sorter = "DATE").get_data_frames()

    game_log[0].to_csv(r'data/game_log.csv', index=False)
  
    
def get_teamstats():
    from nba_api.stats.endpoints import leaguedashteamstats
    
    leaguedashteamstats = leaguedashteamstats.LeagueDashTeamStats(season = "2018-19", season_type_all_star='Regular Season').get_data_frames()
    
    leaguedashteamstats[0].to_csv(r'data/leaguedashteamstats.csv', index=False)

    
def get_boxscoreadv(game_id_lst):
    from nba_api.stats.endpoints import boxscoreadvancedv2

    boxscoreadvancedv2_df = pd.DataFrame()
    for game_id in game_id_lst:
        a = boxscoreadvancedv2.BoxScoreAdvancedV2(game_id=game_id).team_stats
        b = a.get_data_frame()
        boxscoreadvancedv2_df = boxscoreadvancedv2_df.append(b, ignore_index=True)
        time.sleep(2)

    boxscoreadvancedv2_df = boxscoreadvancedv2_df.drop_duplicates(ignore_index=True)

    boxscoreadvancedv2_df.to_csv(r'data/boxscoreadvancedv2.csv', index=False)

    
def get_boxscorefourfactors(game_id_lst):
    from nba_api.stats.endpoints import boxscorefourfactorsv2
    
    boxscorefourfactorsv2_df = pd.DataFrame()
    for game_id in game_id_lst:
        a = boxscorefourfactorsv2.BoxScoreFourFactorsV2(game_id=game_id).sql_teams_four_factors
        b = a.get_data_frame()
        boxscorefourfactorsv2_df = boxscorefourfactorsv2_df.append(b, ignore_index=True)
        time.sleep(2)    

    boxscorefourfactorsv2_df = boxscorefourfactorsv2_df.drop_duplicates(ignore_index=True)

    return boxscorefourfactorsv2_df


def get_boxscoremisc(game_id_lst):
    from nba_api.stats.endpoints import boxscoremiscv2
        
    boxscoremiscv2_df = pd.DataFrame()
    for game_id in game_id_lst:
        a = boxscoremiscv2.BoxScoreMiscV2(game_id=game_id).sql_teams_misc
        b = a.get_data_frame()
        boxscoremiscv2_df = boxscoremiscv2_df.append(b, ignore_index=True)
        time.sleep(2)
        
    boxscoremiscv2_df = boxscoremiscv2_df.drop_duplicates(ignore_index=True)
    
    return boxscoremiscv2_df
