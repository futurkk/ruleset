import requests

rawSpotify = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Spotify/Spotify.list").text
rawApple = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Apple/Apple.list").text
rawYouTube = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/YouTube/YouTube.list").text
rawMicrosoft = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Microsoft/Microsoft.list").text
rawGoogle = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Google/Google.list").text

result = list()
for rawresult in [rawSpotify, rawApple, rawYouTube, rawMicrosoft, rawGoogle]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Entertain.conf", "w") as f:
    f.write("\n".join(result))
