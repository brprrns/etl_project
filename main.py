import time

import pandas as pd

from extractor import fetch_posts, fetch_users
from transformer import add_word_count, categorize_post, merge_with_users, filter_posts
from loader import save_to_csv


POSTS_URL = "https://jsonplaceholder.typicode.com/posts"
USERS_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_PATH = "output/etl_output.csv"

def main():
    """Runs the Complete ETL process: Extract, Transform, Load"""

    start_time = time.time()
    print("Starting ETL pipeline...")

    posts = fetch_posts(POSTS_URL)
    users = fetch_users(USERS_URL)

    posts_df = pd.DataFrame(posts)
    users_df = pd.DataFrame(users)

    posts_df = add_word_count(posts_df)
    posts_df = categorize_post(posts_df)

    merged_df = merge_with_users(posts_df, users_df)

    filtered_df = filter_posts(merged_df)

    save_to_csv(filtered_df, OUTPUT_PATH)

    elaspsed_time = time.time() - start_time

    print(f"Posts Extracted: {len(posts_df)}")
    print(f"Users Extracted: {len(users_df)}")
    print(f"Posts after filtering: {len(filtered_df)}")
    print(f"ETL pipeline completed in {elaspsed_time:.2f} seconds.")


if __name__ == "__main__":
    main()