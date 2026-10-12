import pandas as pd
import pytest


@pytest.fixture
def sample_posts():
    """ return a sample posts DataFrame for testing """

    return pd.DataFrame(
        {
            "userId": [1, 2, 1],
            "id": [1, 2, 3],
            "title": ["Short Post", "Medium Post", "Long Post"],
            "body": [
                "one tww three four five",
                "one two three four five six seven eight nine ten",
                " ".join(["word"] * 35),


            ],
        }
    )