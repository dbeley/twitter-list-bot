import configparser
import tweepy
import csv
import time
import random
import os.path
import sys

# Config file parsing
config = configparser.ConfigParser()
config.read('api')
ConsumerKey = config['CONFIGURATION']['ConsumerKey']
SecretKey = config['CONFIGURATION']['SecretKey']
AccessToken = config['CONFIGURATION']['AccessToken']
AccessTokenSecret = config['CONFIGURATION']['AccessTokenSecret']

# Twitter API Auth
auth = tweepy.OAuthHandler(ConsumerKey, SecretKey)
auth.set_access_token(AccessToken, AccessTokenSecret)
api = tweepy.API(auth)



def get_link():
    file_exists = os.path.isfile('liste_FAIT.csv')

    if not file_exists:
        with open('liste_FAIT.csv', 'w') as file:
            field = ['URL']
            writer = csv.DictWriter(file, fieldnames=field)
            writer.writeheader()

    with open('liste_FAIT.csv', 'r') as file:
        liste_FAIT = [row['URL'] for row in csv.DictReader(file)]

    with open('YouTube-Playlist.csv', 'r') as file:
        liste = [row['URL'] for row in csv.DictReader(file)]

    # Choose randomly the link to post
    choix = random.choice(list(set(liste).difference(liste_FAIT)))

    with open('liste_FAIT.csv', 'a') as file:
        field = ['URL']
        writer = csv.DictWriter(file, fieldnames=field)
        writer.writerow({'URL': choix})

    return choix

def main():
    while True:
        lien = get_link()
        print("Tweet : " + lien)
    
        api.update_status(lien)

        print("Waiting for one hour.")
        time.sleep(3600)

if __name__ == "__main__":
    main()
