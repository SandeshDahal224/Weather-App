# sandesh dahal fist api app 
import requests
api_key = "476a021eff542835f79bd7ffd376cc4f"

user_input = input("Enter city:")
Weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if Weather_data.json()["cod"] == "404":
    print ("No City Found")


else:
    weather = Weather_data.json()['weather'][0]['main']    
    temp = round(Weather_data.json()['main']['temp']) 


    print(f"The weather in {user_input} is: {weather}")    
    print(f"The temperature in {user_input} is: {temp}ºF")
    
    