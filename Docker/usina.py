import requests
import json
import urllib3

API_HOST     = "http://127.0.0.1:8000"
API_ENDPOINT = "/api/electricity/solar/insert/content"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ips = [
    "172.16.249.1",
    "172.16.249.4",
    "172.16.249.3",
    "172.16.249.2"
]

urls = {
    'info': '/solar_api/v1/GetInverterInfo.cgi',
    'energia': '/solar_api/v1/GetInverterRealtimeData.cgi?Scope=System',
    'led': '/solar_api/v1/GetLoggerLEDInfo.cgi'
}
count = 0
for ip in ips: 
    try:
        count += 1
        print(ip)
        # url = 'http://' + ip + urls['info']
        # response = requests.get(url)
        # result = response.text

        # info = json.loads(result)

        # Painel = info['Body']['Data']

        # url = 'http://' + ip + urls['energia']
        # response = requests.get(url)
        # result = response.text

        # energia = json.loads(result)

        # url = 'http://' + ip + urls['led']
        # response = requests.get(url)
        # result = response.text

        # led = json.loads(result)    

        indice = str(count)
        # dados_solar = {
        #     'painel': Painel,
        #     'energia_diaV2': energia['Body']['Data']['DAY_ENERGY']['Values'][indice],
        #     'energia_ano': energia['Body']['Data']['YEAR_ENERGY']['Values'][indice],
        #     'energia_total': energia['Body']['Data']['TOTAL_ENERGY']['Values'][indice],
        #     'potenciav2': energia['Body']['Data']['PAC']['Values'][indice],
        #     'power_led': True if led['Body']['Data']['PowerLED']['State'] == 'on' else False,
        #     'solarnet_led': True if led['Body']['Data']['SolarNetLED']['State'] == 'on' else False,
        #     'solarweb_led': True if led['Body']['Data']['SolarWebLED']['State'] == 'on' else False,
        # }
        dados_solar = {
            'painel': indice,
            'energia_diaV2': indice,
            'energia_ano': indice,
            'energia_total': indice,
            'potenciav2': indice,
            'power_led': True,
            'solarnet_led': True,
            'solarweb_led': True,
        }
        print(dados_solar)

        requests.post(f'{API_HOST}{API_ENDPOINT}', data=dados_solar)
    except Exception as error:
        print(error)
        pass
