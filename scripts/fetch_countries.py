import requests
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codefusion_project.settings')
django.setup()

from countries.models import Country

def fetch_and_save():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    countries = response.json()

    for c in countries:
        Country.objects.create(
            name=c.get('name', {}).get('common', ''),
            cca2=c.get('cca2', ''),
            capital=', '.join(c.get('capital', [])),
            population=c.get('population', 0),
            timezone=', '.join(c.get('timezones', [])),
            flag_url=c.get('flags', {}).get('png', ''),
            region=c.get('region', ''),
            languages=c.get('languages', {})
        )

if __name__ == '__main__':
    fetch_and_save()