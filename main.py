import os
import requests
APIKey = os.environ['APIKey']
def main():
  region = (str)(input('Region: '))
  summonerName = (str)(input('IGN: '))
  responseJSON = makeURL(region, summonerName, APIKey)

  ID = responseJSON['id']
  ID = str(ID)
  responseJSON2 = rankedURL(region, ID, APIKey)
  print(responseJSON["name"])
  print(responseJSON2[0]["tier"])
  print(responseJSON2[0]["rank"])
  
def makeURL(region, summonerName, APIKey):
  URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" +summonerName + "?api_key=" + APIKey 
  response = requests.get(URL)
  return response.json()
  
def rankedURL(region, ID, APIKey):
  URL = "https://"+ region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + ID + "?api_key=" + APIKey
  response = requests.get(URL)
  return response.json()
