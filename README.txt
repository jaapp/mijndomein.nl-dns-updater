Heb jij een dynamisch IP adres en een account bij mijndomein.nl, dan kun je dit script gebruiken om automatisch je DNS entries bij te werken.

Mijndomein biedt geen API om de DNS entries automatisch bij te werken, daarom heb ik uit overmacht dit script ontwikkeld. Dit pythonscript emuleert een brower(phantomjs) die op de mijndomein.nl dashboard inlogt en via gesimuleerde gebruikersacties de entries bijwerkt.

Vereisten:
phantomjs v 1.5+ (http://phantomjs.org/download.html)
python (sudo apt-get install python)
selenium (sudo pip install selenium)

Gebruiksaanwijzing:
1. Maak eerst een backup van je DNS entries op mijndomein.nl(bijvoorbeeld een screenshot). Je weet maar nooit...
2. Pas dnsrecords.config aan.
	2a. Vul jouw gebruikersnaam + wachtwoord in.
	2b. Configureer alle domeinen en subdomeinen waarvan je wilt dat entries worden bijgewerkt.
3. Start het script vervolgens met 'python mijndomein.nl-dns-updater.py' om te testen.
4. Voeg dit script toe aan je crontab als je tevreden bent over het resultaat.

Debug tips:
Voor elke afzonderlijke actie(denk aan: inloggen, klikken op een link, gegevens invoeren) wordt er een screenshot opgeslagen. Mocht het script falen(omdat de mijndomein.nl dashboard is gewijzigd) dan kun je dmv deze screenshots bepalen waar het mis gaat.

Voorbeeld configuratiebestand:
username = "jouw@email.nl"
password = "W8W0orD"

domains = [
	{
		"name": "eerstedomein.nl",
		"subdomains": ["www", "cloud"]
	}
#	,
#	{
#		"name": "tweededomein.com",
#		"subdomains": ["sub1", "sub2"]
#	}
]

Licentie:
- Niet jatten zonder bronvermelding. Graag jatten met bronvermelding.
- Gebruiken op eigen verantwoordelijkheid
- mijndomein.nl is op geen enkele wijze verbonden aan dit script. Voor verzoeken, vragen en klachten over dit script moet je niet bij hun zijn.
