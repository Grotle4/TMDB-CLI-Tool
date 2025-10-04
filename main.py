import argparse
import requests
import json

parser = argparse.ArgumentParser(description= "Will call Api to get movie information")

parser.add_argument("-t", "--type", type=str, required=True,  help= "Will retrieve type of movie information")

args = parser.parse_args()

def process_data(response_data):
    print("Movies now playing \n")
    for idx2, page in enumerate(response_data["results"]):
        print(f"{idx2 + 1}: {page["original_title"]}")
       




if args.type:
    match args.type:
        case "playing":
            url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OTNjNGZiOWI4MTZhNWM1MTYwNGI5ODg2ZjczOTU0OCIsIm5iZiI6MTc1OTU0NDM1My43NTksInN1YiI6IjY4ZTA4NDIxMjdkMmNhYTNiZTI1YTg3NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.FKp9qSBT0H3GAUa2kDJQ7oiCoDN_EzkCXPfR3rF0DH8"
            }

            response = requests.get(url, headers=headers)

            response_data = response.json()
            #print(response_data)
            process_data(response_data)



        case "popular":
            pass
        case "top":
            pass
        case "upcoming":
            pass

