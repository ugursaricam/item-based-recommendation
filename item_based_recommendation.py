###########################################
# Item-Based Collaborative Filtering
###########################################

# 1: Preparation of the Dataset
# 2: Creating the User Movie Dataframe
# 3: Making Item-Based Movie Recommendations

######################################
# 1: Preparation of the Dataset
######################################

import pandas as pd

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
# pd.set_option('display.expand_frame_repr', False)
# pd.set_option('display.float_format', lambda x: '%.5f' % x)

movie = pd.read_csv('datasets/movie_lens_dataset/movie.csv')
rating = pd.read_csv('datasets/movie_lens_dataset/rating.csv')

df = pd.merge(movie, rating, how='left', on='movieId')


def check_df(dataframe, head=5):
    print('##################### Shape #####################')
    print(dataframe.shape)
    print('##################### Types #####################')
    print(dataframe.dtypes)
    print('##################### Head #####################')
    print(dataframe.head(head))
    print('##################### Tail #####################')
    print(dataframe.tail(head))
    print('##################### NA #####################')
    print(dataframe.isnull().sum())
    print('##################### Quantiles #####################')
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df)

######################################
# 2: Creating the User Movie Dataframe
######################################

df['title'].value_counts().head()

comment_counts = pd.DataFrame(df['title'].value_counts()) # [27262 rows x 1 columns]
comment_counts.columns = ['count']

rare_movies = comment_counts[comment_counts['count'] <= 1000].index # [24103 rows x 1 columns]
common_movies = comment_counts[comment_counts['count'] >= 1000].index # [3159 rows x 1 columns]

common_movies = df[df['title'].isin(common_movies)] # [17766015 rows x 6 columns]
rare_movies = df[df['title'].isin(rare_movies)] # [2234782 rows x 6 columns]

common_movies.shape # (17766015, 6)
rare_movies.shape # (2234782, 6)
df.shape # (20000797, 6)

user_movie_df = common_movies.pivot_table(index=['userId'], columns=['title'], values='rating')

######################################
# 3: Making Item-Based Movie Recommendations
######################################

movie_name1 = df[df['title'].str.contains('Matrix')].iloc[0,1] # 'Matrix, The (1999)'
movie_ratings1 = user_movie_df[movie_name1]
user_movie_df.corrwith(movie_ratings1).sort_values(ascending=False).head(11).iloc[1:11]

# title
# Matrix Reloaded, The (2003)                                  0.516906
# Matrix Revolutions, The (2003)                               0.449588
# Animatrix, The (2003)                                        0.367151
# Blade (1998)                                                 0.334493
# Terminator 2: Judgment Day (1991)                            0.333882
# Minority Report (2002)                                       0.332434
# Edge of Tomorrow (2014)                                      0.326762
# Mission: Impossible (1996)                                   0.320815
# Lord of the Rings: The Fellowship of the Ring, The (2001)    0.318726
# Lord of the Rings: The Two Towers, The (2002)                0.318086

movie_name2 = df[df['title'].str.contains('Dark Knight')].iloc[0,1] # 'Dark Knight, The (2008)'
movie_ratings2 = user_movie_df[movie_name2]
user_movie_df.corrwith(movie_ratings2).sort_values(ascending=False).head(11).iloc[1:11]

# title
# Dark Knight Rises, The (2012)    0.609946
# Batman Begins (2005)             0.544084
# Inception (2010)                 0.385737
# Iron Man (2008)                  0.383422
# Avengers, The (2012)             0.356096
# Trip to Bountiful, The (1985)    0.349161
# Heartbreak Ridge (1986)          0.334666
# Interstellar (2014)              0.325546
# Band of Brothers (2001)          0.324975
# Casino Royale (2006)             0.323390

def random_movie_recommender():
    random_movie = pd.Series(user_movie_df.columns).sample(1).iloc[0]
    print('Random movie is:', random_movie)
    random_movie_rating = user_movie_df[random_movie]
    return user_movie_df.corrwith(random_movie_rating).sort_values(ascending=False).head(11).iloc[1:11]

random_movie_recommender()
