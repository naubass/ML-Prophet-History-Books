import pandas as pd

# load data
books_df = pd.read_csv("book_metadata.csv")
data = pd.read_csv('library_borrowing_book_data.csv')
forecast_df = pd.read_csv('library_borrowing_forecast.csv')

# recomendation function
def recommend_books(borrower_id, top_n=5):
    # get borrow history of the borrower
    borrower_history = data[data['borrower_id'] == borrower_id]
    if borrower_history.empty:
        return "No borrowing history found for this borrower."

    # get most frequently borrowed categories
    top_categories = borrower_history['category'].value_counts().head(3).index.tolist()

    # filter books in these categories that the borrower hasn't borrowed yet
    borrowed_book_ids = borrower_history['book_id'].unique()
    candidate_books = books_df[(books_df['category'].isin(top_categories)) & (~books_df['book_id'].isin(borrowed_book_ids))]

    if candidate_books.empty:
        return "No new books to recommend in the preferred categories."

    # recommend top N books based on publication year (newest first)
    recommended_books = candidate_books.sort_values(by='publication_year', ascending=False).head(top_n)

    return recommended_books[['book_id', 'title', 'author', 'category', 'publication_year']]

# example usage
borrower_id = 5000  # example borrower ID
recommendations = recommend_books(borrower_id)
print(f"Book recommendations for borrower ID {borrower_id}:")
print(recommendations)
