import os
import sys
import pickle
import streamlit as st
import numpy as np
import requests
from books_recommender.logger.log import logging
from books_recommender.config.configuration import AppConfiguration
from books_recommender.pipeline.training_pipeline import TrainingPipeline
from books_recommender.exception.exception_handler import AppException


class Recommendation:
    def __init__(self,app_config = AppConfiguration()):
        try:
            self.recommendation_config= app_config.get_recommendation_config()
        except Exception as e:
            raise AppException(e, sys) from e


    def fetch_poster(self,suggestion):
        try:
            book_name = []
            ids_index = []
            poster_url = []
            book_pivot =  pickle.load(open(self.recommendation_config.book_pivot_serialized_objects,'rb'))
            final_rating =  pickle.load(open(self.recommendation_config.final_rating_serialized_objects,'rb'))

            for book_id in suggestion:
                book_name.append(book_pivot.index[book_id])

            for name in book_name[0]: 
                ids = np.where(final_rating['title'] == name)[0][0]
                ids_index.append(ids)

            for idx in ids_index:
                url = final_rating.iloc[idx]['image_url']
                poster_url.append(url)

            return poster_url
        
        except Exception as e:
            raise AppException(e, sys) from e
        


    def recommend_book(self,book_name):
        try:
            books_list = []
            model = pickle.load(open(self.recommendation_config.trained_model_path,'rb'))
            book_pivot =  pickle.load(open(self.recommendation_config.book_pivot_serialized_objects,'rb'))
            book_id = np.where(book_pivot.index == book_name)[0][0]
            distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6 )

            poster_url = self.fetch_poster(suggestion)
            
            for i in range(len(suggestion)):
                    books = book_pivot.index[suggestion[i]]
                    for j in books:
                        books_list.append(j)
            return books_list , poster_url   
        
        except Exception as e:
            raise AppException(e, sys) from e


    def train_engine(self):
        try:
            obj = TrainingPipeline()
            obj.start_training_pipeline()
            st.text("Training Completed!")
            logging.info(f"Recommended successfully!")
        except Exception as e:
            raise AppException(e, sys) from e

    
    def recommendations_engine(self,selected_books):
        try:
            recommended_books,poster_url = self.recommend_book(selected_books)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(recommended_books[1])
                st.image(poster_url[1])
            with col2:
                st.text(recommended_books[2])
                st.image(poster_url[2])

            with col3:
                st.text(recommended_books[3])
                st.image(poster_url[3])
            with col4:
                st.text(recommended_books[4])
                st.image(poster_url[4])
            with col5:
                st.text(recommended_books[5])
                st.image(poster_url[5])
        except Exception as e:
            raise AppException(e, sys) from e



if __name__ == "__main__":
    st.header(' Books Recommender System')
    st.text("This is a collaborative filtering based recommendation system!")

    obj = Recommendation()

    #Training
    if st.button('Train Recommender System'):
        obj.train_engine()

    book_names = pickle.load(open(os.path.join('templates','book_names.pkl') ,'rb'))
    selected_books = st.selectbox(
        "Type or select a book from the dropdown",
        book_names)
    
    #recommendation
    if st.button('Show Recommendation'):
        obj.recommendations_engine(selected_books)



# PLACEHOLDER_IMAGE = "https://via.placeholder.com/150?text=No+Image"

# def is_valid_image_url(url):
#     try:
#         response = requests.head(url, timeout=3)
#         return response.status_code == 200 and 'image' in response.headers.get("Content-Type", "")
#     except:
#         return False

# def main():
#     st.set_page_config(page_title="📚 Book Recommender", layout="wide")

#     # Sidebar
#     with st.sidebar:
#         st.title("📖 Book Recommender")
#         st.markdown("This app uses **collaborative filtering** to suggest books you might enjoy.")
#         st.markdown("---")

#     # Main Title
#     st.markdown("<h1 style='text-align: center;'>📚 Book Recommender System</h1>", unsafe_allow_html=True)
#     st.write("This is a collaborative filtering-based recommendation system built using Streamlit.")

#     # Instantiate recommender system
#     obj = Recommendation()

#     # Train Button
#     with st.expander("🔧 Train Recommendation Engine"):
#         if st.button("Train Now"):
#             with st.spinner("Training the recommendation engine..."):
#                 obj.train_engine()
#             st.success("Model trained successfully!")

#     # Load books
#     book_names = pickle.load(open(os.path.join('templates', 'book_names.pkl'), 'rb'))

#     # Book Selection
#     selected_books = st.selectbox("📘 Select a book to get similar recommendations:", book_names)

#     # Recommendations
#     if st.button("🔍 Show Recommendations"):
#         with st.spinner("Fetching recommendations..."):
#             recommendations = obj.recommendations_engine(selected_books)

#         if recommendations:
#             st.success(f"Here are some books similar to *{selected_books}*:")

#             # Layout: 2 columns
#             cols = st.columns(2)

#             for idx, rec in enumerate(recommendations):
#                 with cols[idx % 2]:
#                     with st.container():
#                         st.markdown(f"**{rec.get('title', 'Unknown Title')}** by *{rec.get('author', 'Unknown')}*")

#                         image_url = rec.get('image_url', '')
#                         if not image_url or not is_valid_image_url(image_url):
#                             image_url = PLACEHOLDER_IMAGE

#                         try:
#                             st.image(image_url, use_column_width=True)
#                         except:
#                             st.image(PLACEHOLDER_IMAGE, use_column_width=True)

#                         st.markdown("---")
#         else:
#             st.warning("No recommendations found. Try a different book.")

#     # Footer
#     st.markdown(
#         """
#         <hr style="border:0.5px solid #ddd">
#         <p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit</p>
#         """, unsafe_allow_html=True
#     )

# if __name__ == "__main__":
#     main()
