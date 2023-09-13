from tihclient import TihClient

def test_api():
    client = TihClient()
    response = client.get_accommodation(keyword='hotel')
    print(response)