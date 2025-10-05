import argparse
import requests

parser = argparse.ArgumentParser(description= "Will call Api to get movie information")

parser.add_argument("-t", "--type", type=str, required=True,  help= "Will retrieve type of movie information")

args = parser.parse_args()

def process_data(type, response_data):
    match type:
        case "playing":
            print("Movies now playing \n")
        case "popular":
            print("Most Popular movies \n")
        case "top":
            print("Top rated movies \n")
        case "upcoming":
            print("Upcoming movies \n")
        
    for idx2, page in enumerate(response_data["results"]):
        print(f"{idx2 + 1}: {page["original_title"]}")
       


def process_args(args):
    if args.type:
        try:
            match args.type:
                case "playing":
                    url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

                    headers = {
                        "accept": "application/json",
                        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OTNjNGZiOWI4MTZhNWM1MTYwNGI5ODg2ZjczOTU0OCIsIm5iZiI6MTc1OTU0NDM1My43NTksInN1YiI6IjY4ZTA4NDIxMjdkMmNhYTNiZTI1YTg3NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.FKp9qSBT0H3GAUa2kDJQ7oiCoDN_EzkCXPfR3rF0DH8"
                    }

                    response = requests.get(url, headers=headers)

                    response_data = response.json()
                    process_data("playing", response_data)

                case "popular":
                    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

                    headers = {
                        "accept": "application/json",
                        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OTNjNGZiOWI4MTZhNWM1MTYwNGI5ODg2ZjczOTU0OCIsIm5iZiI6MTc1OTU0NDM1My43NTksInN1YiI6IjY4ZTA4NDIxMjdkMmNhYTNiZTI1YTg3NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.FKp9qSBT0H3GAUa2kDJQ7oiCoDN_EzkCXPfR3rF0DH8"
                    }

                    response = requests.get(url, headers=headers)

                    response_data = response.json()
                    process_data("popular", response_data)
                case "top":
                    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

                    headers = {
                        "accept": "application/json",
                        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OTNjNGZiOWI4MTZhNWM1MTYwNGI5ODg2ZjczOTU0OCIsIm5iZiI6MTc1OTU0NDM1My43NTksInN1YiI6IjY4ZTA4NDIxMjdkMmNhYTNiZTI1YTg3NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.FKp9qSBT0H3GAUa2kDJQ7oiCoDN_EzkCXPfR3rF0DH8"
                    }

                    response = requests.get(url, headers=headers)

                    response_data = response.json()
                    process_data("top", response_data)
                case "upcoming":
                    url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"

                    headers = {
                        "accept": "application/json",
                        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OTNjNGZiOWI4MTZhNWM1MTYwNGI5ODg2ZjczOTU0OCIsIm5iZiI6MTc1OTU0NDM1My43NTksInN1YiI6IjY4ZTA4NDIxMjdkMmNhYTNiZTI1YTg3NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.FKp9qSBT0H3GAUa2kDJQ7oiCoDN_EzkCXPfR3rF0DH8"
                    }

                    response = requests.get(url, headers=headers)

                    response_data = response.json()
                    process_data("upcoming", response_data)

        except requests.exceptions.HTTPError as errh:
            print(f"A HTTP Error occurred: {repr(errh)}")
        except requests.exceptions.ConnectionError as errc:
            print(f"An Error trying to connect to the API occurred: {repr(errc)}")
        except requests.exceptions.Timeout as errt:
            print(f"A Timeout error occurred: {repr(errt)}")
        except requests.exceptions.RequestException as err:
            print(f"An Unknown Error occurred: {repr(err)}")

process_args(args)
