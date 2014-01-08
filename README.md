Python script om automatisch de DNS entries op mijndomein.nl bij te werken naar je dynamisch IP adres. Mijndomein biedt geen goede API om deze data automatisch bij te werken, daarom heb ik uit overmacht dit script ontwikkeld. Dit pythonscript emuleert een brower die op de mijndomein.nl dashboard inlogt en via gesimuleerde gebruikersacties de entries bijwerkt.

Vereisten:
phantomjs v 1.5+ (http://phantomjs.org/download.html)
python (sudo apt-get install python)
selenium (sudo pip install selenium)

Gebruiksaanwijzing:
Pas dnsrecords.nl aan. Vul jouw gebruikersnaam + wachtwoord in. Configureer alle domeinen en subdomeinen waarvan je wilt dat entries worden bijgewerkt.
Start vervolgens update_dns_records.py.

Debug tips:
Voor elke afzonderlijke actie(denk aan: inloggen, klikken op een link, gegevens invoeren) wordt er een screenshot opgeslagen. Mocht het bijwerken van de entries falen dan kun je uit deze screenshots herleiden waar je de oorzaak in moet zoeken.

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
