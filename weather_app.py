import requests
import json
import collections
import settings_local

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, loc, country')


def main():
    print_the_header()

    city_name = raw_input('Which city weather you like to know ? ')
    country_name = raw_input('Which country are you in ? ')

    webjson = get_json_from_web(city_name, country_name)
    report = get_weather(webjson)

    try:
        print(u"The temperature in %s, %s is %.1f\u2103 and weather reports %s" % (
        report.loc,
        report.country,
        report.temp,
        report.cond
        ))
    except:
        print("The temperature in %s, %s is %.1f deg Celcius and weather reports %s" % (
        report.loc,
        report.country,
        report.temp,
        report.cond
        ))
    # display for the forecast

def print_the_header():
    print '---------------------------------'
    print '           WEATHER APP'
    print '---------------------------------'
    print ''


def get_json_from_web(city_name, country_name, apikey=settings_local.api['key']):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}'.format(city_name, country_name, apikey)
    response = requests.get(url)
    #print(response.status_code)
    # print(response.text[0:250])
    return response.json()


def get_weather(webjson):
    loc = webjson['name']
    country = webjson['sys']['country']
    condition = webjson['weather'][0]['description']
    act_temp = webjson['main']['temp']
    temp = act_temp - 273.15
    report = WeatherReport(cond=condition, temp=temp, loc=loc, country=country)
    return report


if __name__ == '__main__':
    main()