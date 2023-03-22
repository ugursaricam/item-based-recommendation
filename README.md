<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--h03lU8An--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/mih10uhu1464fx1kr0by.jpg" width="100%"/>

# The history of dataset

The "movie_lens_dataset" is a popular dataset in the field of recommender systems, containing information about movies and user ratings. It includes several files, but two of the main ones are "movie.csv" and "rating.csv".

The "movie.csv" file contains information about the movies in the dataset. Specifically, it includes the following columns:

* **movieId:** a unique identifier for each movie
title: the title of the movie
* **genres:** a list of genres that the movie belongs to (e.g. "Action", "Comedy", "Drama")

The "rating.csv" file contains information about user ratings of the movies in the dataset. Specifically, it includes the following columns:

* **userId:** a unique identifier for each user
* **movieId:** a unique identifier for each movie
* **rating:** the rating that the user gave the movie, on a scale of 0.5 to 5 (in 0.5 increments)
* **timestamp:** the time at which the rating was given (measured in seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970)

Together, these two files provide a rich source of information for building and evaluating recommender systems.

datasets: https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset
