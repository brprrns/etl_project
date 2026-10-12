import pytest

from transformer import (
    add_word_count,
    categorize_post,
    filter_posts,
)


def test_add_word_count(sample_posts):
    result = add_word_count(sample_posts)

    assert result["word_count"].tolist() == [5, 10, 35]


@pytest.mark.parametrize(
    "word_count, expected",
    [
        (0, "Short"),
        (1, "Short"),
        (29, "Short"),
        (30, "Long"),
        (50, "Long"),
        (100, "Long"),
    ],
)
def test_categorize_post(word_count, expected):
    import pandas as pd

    df = pd.DataFrame({"word_count": [word_count]})

    result = categorize_post(df)

    assert result["category"].iloc[0] == expected


def test_filter_posts(sample_posts):
    df = add_word_count(sample_posts)

    result = filter_posts(df)

    assert len(result) == 1
    assert result["word_count"].iloc[0] == 35