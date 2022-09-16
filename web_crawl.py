import requests


def request(url):
    try:
        return requests.get("https://"+url)
    except requests.exceptions.ConnectionError:
        pass

ta=input("Enter website name [in form of goole.com] : " )
target_url = ta



with open("C:\\Users\\user\\Downloads\\john\\prefix_name.txt", 'r') as f:
    for line in f:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)

        if response:
            print("Subdomain exists {}".format(test_url))