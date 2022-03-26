from urllib import response
import requests, json

baseURL = "https://api.openweathermap.org/data/2.5/weather?"
apiID = "7aa1c34b47888e5c89e053f9bc38e4b0"
city = "New York"

URL = baseURL + "q=" + city + "&appid=" + apiID

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    main = data['main']
    tempature = (main['temp'] -273) * 1.8+32
    report = data['weather']
    weatherDes = report[0]['description'];
    print("The temperatuer in " + city + " is " +str(tempature));
    print("The weather is " + weatherDes);
