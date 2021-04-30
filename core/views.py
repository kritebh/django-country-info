from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    try:
        raw_q = request.POST.get('query','india')
        q=raw_q.lower()
        r=requests.get(f'https://restcountries.eu/rest/v2/name/{q}?fullText=true').json()
        print(r[0]['population'])
        info={
            'name':r[0]['name'],
            'capital':r[0]['capital'],
            'region':r[0]['region'],
            'population':r[0]['population'],
            'nativeName':r[0]['nativeName'],
            'currency':r[0]['currencies'][0]['name'],
            'symbol':r[0]['currencies'][0]['symbol'],
            'flag':r[0]['flag'],

        }
        context = {'info':info}
        return render(request,'core/index.html',context)
    except:
        return render(request,'core/error.html')