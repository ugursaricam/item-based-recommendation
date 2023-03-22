import pandas as pd

movie = pd.read_csv('datasets/movie_lens_dataset/movie.csv')
rating = pd.read_csv('datasets/movie_lens_dataset/rating.csv')

df = movie.merge(rating, how="left", on="movieId")

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

def create_user_movie_df():
    comment_counts = pd.DataFrame(df["title"].value_counts())
    rare_movies = comment_counts[comment_counts["title"] <= 1000].index
    common_movies = df[~df["title"].isin(rare_movies)]
    user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")
    return user_movie_df


user_movie_df = create_user_movie_df()


def item_based_recommender(movie_name, user_movie_df):
    movie_name = user_movie_df[movie_name]
    return user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(11).iloc[1:11]


item_based_recommender("Matrix, The (1999)", user_movie_df)


def random_movie_recommender():
    random_movie = pd.Series(user_movie_df.columns).sample(1).iloc[0]
    print("Random movie is:", random_movie)
    random_movie_rating = user_movie_df[random_movie]
    return user_movie_df.corrwith(random_movie_rating).sort_values(ascending=False).head(11).iloc[1:11]


random_movie_recommender()

