import pandas as pd
import re

ratings = pd.read_csv('ratings.csv')
ratings = ratings.drop('timestamp',axis = 1)
movies = pd.read_csv('movies.csv', index_col = 'movieId')

def productionYear(row):
    try:
        return int(re.findall(r'(\d{4})', row)[-1])
    except:
        return 1950


def yearing(row):
    try:
        return int(movies['year'][row])
    except:
        return 0


if __name__ == '__main__':
    movies['year'] = movies['title'].apply(productionYear)
    ratings['year'] = ratings['movieId'].apply(yearing)
    print(ratings.groupby('year').mean()['rating'].sort_values(ascending=False).head(50))
    input('Вийти:')
