from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method=='POST':
        city=request.POST['city']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ff14907ccc12545a42bb90bf1f48ae85&units=metric"
        try:
            res = urllib.request.urlopen(url).read()
            json_data=json.loads(res)

            data={
                    "country":str(json_data['sys']['country']),
                    "coordinate":str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
                    "temp":str(json_data['main']['temp'])+'*C',
                    "pressure":str(json_data['main']['pressure'])+"atm",
                    "humidity":str(json_data['main']['humidity'])
                }
        except Exception as e:
            data={}
            raise e

        

    return render(request, 'index.html',{'data':data,'city':city})
