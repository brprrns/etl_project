import pandas as pd


def add_word_count(df):
    """ Add a word_count column on post body """

    result = df.copy()
    result["word_count"] = result["body"].str.split().str.len()

    return result


def categorize_post(df):
    """Categorize posts based on their word count"""

    result = df.copy()
    result["category"] = result["word_count"].apply(lambda count: "Long" if count >= 30 else "Short")

    return result


def merge_with_users(posts_df, users_df):
    """ Merge posts with user information"""

    result = posts_df.merge(
        users_df,
        left_on="userId",
        right_on="id",
        suffixes=("_post", "_user")
    )

    return result


def filter_posts(df, min_word = 30):
    """ Return posts containing at least min_word words in their body """

    return df[df["word_count"] >= min_word].copy()

