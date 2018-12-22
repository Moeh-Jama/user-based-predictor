# user based predictor
using a csv of ratings &  movies that was gotten from https://grouplens.org/datasets/movielens/

collect n-users and their ratings. Purpose of the repo is to find the predictive rating for a user a on an unseen, to user a, item j. Find the k nearest neighbours of user a who have high correalation to them and have previously rated item j. Use the resnick algorithm to then find the predicitive rating for item j for user a.

Main-File: main_script.py
