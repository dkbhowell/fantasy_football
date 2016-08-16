import nflgame
from fantasy import calc_fantasy_pts

season2015 = nflgame.games(2015)
last_three_2015 = nflgame.games(2015, week=[14, 15, 16])
first_2015 = nflgame.games(2015, week=1)
first_six_2015 = nflgame.games(2015, week=[1, 2, 3, 4, 5, 6])

games = season2015

players = nflgame.combine_max_stats(games)

# calculate fantasy points for each player
for p in players.rushing().filter(guess_position='RB'):
    fantasy_pts, rec_pct = calc_fantasy_pts(p, games)
    p.fantasy_pts = fantasy_pts
    p.fantasy_pct_rec = rec_pct

    msg = '%s: %d total points (%d receiving)'
    print msg % (p.name, fantasy_pts, rec_pct)

print '----------------'

players = players.sort('fantasy_pts')
top_rushers = players.limit(10)
for p in top_rushers:
    msg = '%s: %d total points (%d%% receiving)'
    print msg % (p.name, p.fantasy_pts, p.fantasy_pct_rec)
