from tihclient import TIHClient
from tihclient import DataframeResponseHandler


def test_api() -> None:
    """Test the api."""
    client = TIHClient()
    response = client.get_accommodation(keyword='hotel')
    print(response)
    bars = client.get_bar_clubs(keyword='bar')
    print(bars)
    response = client.get_accommodation(keyword='hotel')
    print(response)


def test_df() -> None:
    """Test the api."""
    client = TIHClient(response_handler=DataframeResponseHandler)
    response = client.get_accommodation(keyword='hotel')
    print(response)
    bars = client.get_bar_clubs(keyword='bar')
    print(bars)
    response = client.get_accommodation(keyword='hotel')
    print(response)


if __name__ == '__main__':
    test_api()
    test_df()
