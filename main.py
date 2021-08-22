import pandas
import Functions


first_decade = pandas.read_csv('2000-2009.csv')
second_decade = pandas.read_csv('2010-2019.csv')


# Title Winners (pie chart)
Functions.winning_clubs(data=first_decade, title='2000 - 2009 Winners')
Functions.winning_clubs(data=second_decade, title='2010 - 2019 Winners')

# -----------------------------------------------------------------------------

# Top Teams Qualified For UCL (barplot)
Functions.champions_league_clubs(data=first_decade, title='2000 - 2009 UCL')
Functions.champions_league_clubs(data=second_decade, title='2010 - 2019 UCL')

# Top Teams Relegated (barplot)
Functions.worst_clubs(data=first_decade, title='2000 - 2009 Relegation')
Functions.worst_clubs(data=second_decade, title='2010 - 2019 Relegation')

# ------------------------------------------------------------

# Top Teams In Win Matches (barplot)
Functions.most_in(data=first_decade, series='won', title='2000 - 2009 Wins')
Functions.most_in(data=second_decade, series='won', title='2010 - 2019 Wins')

# Top Teams In Draw Matches (barplot)
Functions.most_in(data=first_decade, series='draw', title='2000 - 2009 Draws')
Functions.most_in(data=second_decade, series='draw', title='2010 - 2019 Draws')

# Top Teams In Lose Matches (barplot)
Functions.most_in(data=first_decade, series='lost', title='2000 - 2009 Loses')
Functions.most_in(data=second_decade, series='lost', title='2010 - 2019 Loses')

# Top Teams In Goal For (barplot)
Functions.most_in(data=first_decade, series='gf', title='2000 - 2009 Goal For')
Functions.most_in(data=second_decade, series='gf', title='2010 - 2019 Goal For')

# Top Teams In Goal Against (barplot)
Functions.most_in(data=first_decade, series='ga', title='2000 - 2009 Goal Against')
Functions.most_in(data=second_decade, series='ga', title='2010 - 2019 Goal Against')

# Top Teams In Points (barplot)
Functions.most_in(data=first_decade, series='points', title='2000 - 2009 Points')
Functions.most_in(data=second_decade, series='points', title='2010 - 2019 Points')

# -----------------------------------------------------------------------------

# Teams Performance Due To Points
Functions.team_performance(data=first_decade, team='Manchester United', title='Manchester United 2000-2009')
Functions.team_performance(data=second_decade, team='Manchester United', title='Manchester United 2010-2019')

Functions.team_performance(data=first_decade, team='Manchester City', title='Manchester City 2000-2009')
Functions.team_performance(data=second_decade, team='Manchester City', title='Manchester City 2010-2019')

Functions.team_performance(data=first_decade, team='Chelsea', title='Chelsea 2000-2009')
Functions.team_performance(data=second_decade, team='Chelsea', title='Chelsea 2010-2019')

Functions.team_performance(data=first_decade, team='Liverpool', title='Liverpool 2000-2009')
Functions.team_performance(data=second_decade, team='Liverpool', title='Liverpool 2010-2019')

Functions.team_performance(data=first_decade, team='Arsenal', title='Arsenal 2000-2009')
Functions.team_performance(data=second_decade, team='Arsenal', title='Arsenal 2010-2019')

Functions.team_performance(data=first_decade, team='Tottenham Hotspur ', title='Tottenham Hotspur 2000-2009')
Functions.team_performance(data=second_decade, team='Tottenham Hotspur ', title='Tottenham Hotspur 2010-2019')