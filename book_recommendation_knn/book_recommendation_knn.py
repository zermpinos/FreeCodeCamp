import pandas as pd
import pytest
from sklearn.neighbors import NearestNeighbors

# File names
books_filename = 'BX-Books.csv'
ratings_filename = 'BX-Book-Ratings.csv'


# Import CSV data into dataframes
def import_data():
    books_df_inner = pd.read_csv(books_filename,
                                 encoding="ISO-8859-1",
                                 sep=";",
                                 header=0,
                                 names=['isbn', 'title', 'author'],
                                 usecols=['isbn', 'title', 'author'],
                                 dtype={'isbn': 'str', 'title': 'str', 'author': 'str'})

    ratings_df_inner = pd.read_csv(ratings_filename,
                                   encoding="ISO-8859-1",
                                   sep=";",
                                   header=0,
                                   names=['user', 'isbn', 'rating'],
                                   usecols=['user', 'isbn', 'rating'],
                                   dtype={'user': 'int32', 'isbn': 'str', 'rating': 'float32'})
    return books_df_inner, ratings_df_inner


# Filter ratings data based on user and book counts
def filter_ratings(ratings_df_outer):
    user_counts = ratings_df_outer['user'].value_counts()
    isbn_counts = ratings_df_outer['isbn'].value_counts()

    filtered_ratings = ratings_df_outer[
        ~ratings_df_outer['user'].isin(user_counts[user_counts < 200].index) &
        ~ratings_df_outer['isbn'].isin(isbn_counts[isbn_counts < 100].index)
        ]

    return filtered_ratings


# Create a pivot table from filtered ratings
def create_pivot_table(ratings_df_outer_2, books_df_outer):
    table_df = ratings_df_outer_2.pivot_table(index='isbn', columns='user', values='rating').fillna(0)

    table_df.index = table_df.join(books_df_outer.set_index('isbn'))['title']
    return table_df


# Create a k-Nearest Neighbors model using the Scikit-learn library
def create_knn_model(table_df):
    knn_model = NearestNeighbors(metric='cosine', algorithm='brute')
    knn_model.fit(table_df)
    return knn_model


# Function to get recommendations based on user input
def user_input_recommendations(knn_model, table_df):
    book_title = input("Enter the title of a book you like: ")

    if book_title in table_df.index:
        recommends = get_recommends(book_title, table_df, knn_model)
        recommended_books = recommends[1]

        print(f"Book: {recommends[0]}")
        print("Recommended Books:")
        for book, distance in recommended_books:
            print(f"- {book} (Distance: {distance})")
    else:
        print("I don't know that book.")


# Function to get recommendations based on a book title
def get_recommends(book_title, table_df, knn_model):
    query_index = table_df.index.get_loc(book_title)
    distances, indices = knn_model.kneighbors(table_df.iloc[query_index, :].values.reshape(1, -1), n_neighbors=6)

    recommended_books = []
    for i in range(1, len(distances.flatten())):
        recommended_books.append((table_df.index[indices.flatten()[i]], distances.flatten()[i]))

    return book_title, recommended_books


@pytest.fixture
def table_df():
    books_df_outer, ratings_df_outer_3 = import_data()
    ratings_df_outer_3 = filter_ratings(ratings_df_outer_3)
    pivot_table_df_inner = create_pivot_table(ratings_df_outer_3, books_df_outer)
    return pivot_table_df_inner


@pytest.fixture
def knn_model(table_df):
    knn_model = NearestNeighbors(metric='cosine', algorithm='brute')
    knn_model.fit(table_df)
    return knn_model


def test_book_recommendation(knn_model, table_df):
    recommends = get_recommends("The Queen of the Damned (Vampire Chronicles (Paperback))", table_df, knn_model)
    recommended_books = recommends[1]

    print(f"Book: {recommends[0]}")
    print("Recommended Books:")
    for book, distance in recommended_books:
        print(f"- {book} (Distance: {distance})")

    expected_books = ['Catch 22',
                      'The Witching Hour (Lives of the Mayfair Witches)',
                      'Interview with the Vampire',
                      'The Tale of the Body Thief (Vampire Chronicles (Paperback))',
                      'The Vampire Lestat (Vampire Chronicles, Book II)']
    expected_distances = [0.793983519077301,
                          0.7448656558990479,
                          0.7345068454742432,
                          0.5376338362693787,
                          5178412199020386]

    for i in range(2):
        if recommended_books[i][0] not in expected_books \
                or abs(recommended_books[i][1] - expected_distances[i]) >= 0.05:
            print("Test failed.")
            return

    print("You passed the challenge! 🎉🎉🎉🎉🎉")


# Main execution
if __name__ == "__main__":
    books_df, ratings_df = import_data()
    ratings_df = filter_ratings(ratings_df)
    pivot_table_df = create_pivot_table(ratings_df, books_df)
    knn_model = create_knn_model(pivot_table_df)
    test_book_recommendation(knn_model, pivot_table_df)
    user_input_recommendations(knn_model, pivot_table_df)

input('Type anything to exit the program...')