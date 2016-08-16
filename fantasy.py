import nflgame
from const import *


def calc_bonus_pts(player, games):
    player_name = player.name
    player_team = player.team
    rush_bonus = 0
    rec_bonus = 0

    for i, game in enumerate(games):
        if (game.home == player_team or game.away == player_team) and game.players.name(player_name):
            rush_yds = game.players.name(player_name).rushing_yds
            if 100 < rush_yds < 200:
                print 'Game {:2}, Week {:2} - Rush: {:4}'.format(i + 1, game.schedule['week'], rush_yds)
                rush_bonus += 1
            elif rush_yds > 200:
                print 'Game {:2}, Week {:2} - Rush: {:4}'.format(i + 1, game.schedule['week'], rush_yds)
                rush_bonus += 2

            rec_yds = game.players.name(player_name).receiving_yds
            if 100 < rec_yds < 200:
                print 'Game {:2}, Week {:2} - Rec: {:4}'.format(i + 1, game.schedule['week'], rec_yds)
                rush_bonus += 1
            elif rec_yds > 200:
                print 'Game {:2}, Week {:2} - Rec: {:4}'.format(i + 1, game.schedule['week'], rec_yds)
                rush_bonus += 2

    return rush_bonus, rec_bonus


def calc_fantasy_pts(player, games):
    global total_pts
    rush_yds_pts = player.rushing_yds * rush_pts_per_yd
    rush_td_pts = player.rushing_tds * rush_td
    rush_conversion_pts = player.rushing_twoptm * rush_conversion
    rec_yds_pts = player.receiving_yds * rec_pts_per_yd
    rec_td_pts = player.receiving_tds * rec_td
    rec_conversion_pts = player.receiving_twoptm * rec_conversion
    rec_pts = player.receiving_rec * rec_ppr
    fumble_pts = player.fumbles_tot * fumble_penalty

    if include_bonus_pts:
        rush_bonus_pts, rec_bonus_pts = calc_bonus_pts(player, games)
    else:
        rush_bonus_pts, rec_bonus_pts = 0, 0

    rush_pts = rush_yds_pts + rush_td_pts + rush_conversion_pts + rush_bonus_pts
    rec_pts = rec_yds_pts + rec_td_pts + rec_conversion_pts + rec_pts + rec_bonus_pts
    total_pts = rush_pts + rec_pts + fumble_pts

    rec_percent = (rec_pts / total_pts)*100 if total_pts > 0 else -1

    return total_pts, rec_percent
