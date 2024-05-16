import os
import mysql.connector

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_DATABASE = os.environ.get("DB_DATABASE")

conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)
cursor = conn.cursor()

currency_country_mapping = {
    "AFN": ("Afghanistan", "AFG"),  # Afghan Afghani
    "ALL": ("Albania", "ALB"),  # Albanian Lek
    "DZD": ("Algeria", "DZA"),  # Algerian Dinar
    "EUR": ("Andorra", "AND"),  # Euro
    "AOA": ("Angola", "AGO"),  # Angolan Kwanza
    "XCD": ("Antigua and Barbuda", "ATG"),  # East Caribbean Dollar
    "ARS": ("Argentina", "ARG"),  # Argentine Peso
    "AMD": ("Armenia", "ARM"),  # Armenian Dram
    "AUD": ("Australia", "AUS"),  # Australian Dollar
    "EUR": ("Austria", "AUT"),  # Euro
    "AZN": ("Azerbaijan", "AZE"),  # Azerbaijani Manat
    "BSD": ("Bahamas", "BHS"),  # Bahamian Dollar
    "BHD": ("Bahrain", "BHR"),  # Bahraini Dinar
    "BDT": ("Bangladesh", "BGD"),  # Bangladeshi Taka
    "BBD": ("Barbados", "BRB"),  # Barbadian Dollar
    "BYN": ("Belarus", "BLR"),  # Belarusian Ruble
    "EUR": ("Belgium", "BEL"),  # Euro
    "BZD": ("Belize", "BLZ"),  # Belize Dollar
    "XOF": ("Benin", "BEN"),  # West African CFA Franc
    "BTN": ("Bhutan", "BTN"),  # Bhutanese Ngultrum
    "BOB": ("Bolivia", "BOL"),  # Bolivian Boliviano
    "BAM": ("Bosnia and Herzegovina", "BIH"),  # Bosnia and Herzegovina Convertible Mark
    "BWP": ("Botswana", "BWA"),  # Botswana Pula
    "BRL": ("Brazil", "BRA"),  # Brazilian Real
    "BND": ("Brunei", "BRN"),  # Brunei Dollar
    "BGN": ("Bulgaria", "BGR"),  # Bulgarian Lev
    "XOF": ("Burkina Faso", "BFA"),  # West African CFA Franc
    "BIF": ("Burundi", "BDI"),  # Burundian Franc
    "CVE": ("Cabo Verde", "CPV"),  # Cape Verdean Escudo
    "KHR": ("Cambodia", "KHM"),  # Cambodian Riel
    "XAF": ("Cameroon", "CMR"),  # Central African CFA Franc
    "CAD": ("Canada", "CAN"),  # Canadian Dollar
    "XAF": ("Central African Republic", "CAF"),  # Central African CFA Franc
    "XAF": ("Chad", "TCD"),  # Central African CFA Franc
    "CLP": ("Chile", "CHL"),  # Chilean Peso
    "CNY": ("China", "CHN"),  # Chinese Yuan
    "COP": ("Colombia", "COL"),  # Colombian Peso
    "KMF": ("Comoros", "COM"),  # Comorian Franc
    "XAF": ("Congo", "COG"),  # Central African CFA Franc
    "CRC": ("Costa Rica", "CRI"),  # Costa Rican Colon
    "HRK": ("Croatia", "HRV"),  # Croatian Kuna
    "CUP": ("Cuba", "CUB"),  # Cuban Peso
    "EUR": ("Cyprus", "CYP"),  # Euro
    "CZK": ("Czech Republic", "CZE"),  # Czech Koruna
    "DKK": ("Denmark", "DNK"),  # Danish Krone
    "DJF": ("Djibouti", "DJI"),  # Djiboutian Franc
    "XCD": ("Dominica", "DMA"),  # East Caribbean Dollar
    "DOP": ("Dominican Republic", "DOM"),  # Dominican Peso
    "USD": ("Ecuador", "ECU"),  # United States Dollar
    "EGP": ("Egypt", "EGY"),  # Egyptian Pound
    "USD": ("El Salvador", "SLV"),  # United States Dollar
    "XAF": ("Equatorial Guinea", "GNQ"),  # Central African CFA Franc
    "ERN": ("Eritrea", "ERI"),  # Eritrean Nakfa
    "EUR": ("Estonia", "EST"),  # Euro
    "SZL": ("Eswatini", "SWZ"),  # Swazi Lilangeni
    "ETB": ("Ethiopia", "ETH"),  # Ethiopian Birr
    "FJD": ("Fiji", "FJI"),  # Fijian Dollar
    "EUR": ("Finland", "FIN"),  # Euro
    "EUR": ("France", "FRA"),  # Euro
    "XAF": ("Gabon", "GAB"),  # Central African CFA Franc
    "GMD": ("Gambia", "GMB"),  # Gambian Dalasi
    "GEL": ("Georgia", "GEO"),  # Georgian Lari
    "EUR": ("Germany", "DEU"),  # Euro
    "GHS": ("Ghana", "GHA"),  # Ghanaian Cedi
    "EUR": ("Greece", "GRC"),  # Euro
    "XCD": ("Grenada", "GRD"),  # East Caribbean Dollar
    "GTQ": ("Guatemala", "GTM"),  # Guatemalan Quetzal
    "GNF": ("Guinea", "GIN"),  # Guinean Franc
    "XOF": ("Guinea-Bissau", "GNB"),  # West African CFA Franc
    "GYD": ("Guyana", "GUY"),  # Guyanese Dollar
    "HTG": ("Haiti", "HTI"),  # Haitian Gourde
    "HNL": ("Honduras", "HND"),  # Honduran Lempira
    "HKD": ("Hong Kong", "HKG"),  # Hong Kong Dollar
    "HUF": ("Hungary", "HUN"),  # Hungarian Forint
    "ISK": ("Iceland", "ISL"),  # Icelandic Krona
    "INR": ("India", "IND"),  # Indian Rupee
    "IDR": ("Indonesia", "IDN"),  # Indonesian Rupiah
    "IRR": ("Iran", "IRN"),  # Iranian Rial
    "IQD": ("Iraq", "IRQ"),  # Iraqi Dinar
    "EUR": ("Ireland", "IRL"),  # Euro
    "ILS": ("Israel", "ISR"),  # Israeli Shekel
    "EUR": ("Italy", "ITA"),  # Euro
    "JMD": ("Jamaica", "JAM"),  # Jamaican Dollar
    "JPY": ("Japan", "JPN"),  # Japanese Yen
    "JOD": ("Jordan", "JOR"),  # Jordanian Dinar
    "KZT": ("Kazakhstan", "KAZ"),  # Kazakhstani Tenge
    "KES": ("Kenya", "KEN"),  # Kenyan Shilling
    "AUD": ("Kiribati", "KIR"),  # Australian Dollar
    "KPW": ("North Korea", "PRK"),  # North Korean Won
    "KRW": ("South Korea", "KOR"),  # South Korean Won
    "KWD": ("Kuwait", "KWT"),  # Kuwaiti Dinar
    "KGS": ("Kyrgyzstan", "KGZ"),  # Kyrgyzstani Som
    "LAK": ("Laos", "LAO"),  # Lao Kip
    "EUR": ("Latvia", "LVA"),  # Euro
    "LBP": ("Lebanon", "LBN"),  # Lebanese Pound
    "LSL": ("Lesotho", "LSO"),  # Lesotho Loti
    "LRD": ("Liberia", "LBR"),  # Liberian Dollar
    "LYD": ("Libya", "LBY"),  # Libyan Dinar
    "CHF": ("Liechtenstein", "LIE"),  # Swiss Franc
    "EUR": ("Lithuania", "LTU"),  # Euro
    "EUR": ("Luxembourg", "LUX"),  # Euro
    "MGA": ("Madagascar", "MDG"),  # Malagasy Ariary
    "MWK": ("Malawi", "MWI"),  # Malawian Kwacha
    "MYR": ("Malaysia", "MYS"),  # Malaysian Ringgit
    "MVR": ("Maldives", "MDV"),  # Maldivian Rufiyaa
    "XOF": ("Mali", "MLI"),  # West African CFA Franc
    "EUR": ("Malta", "MLT"),  # Euro
    "USD": ("Marshall Islands", "MHL"),  # United States Dollar
    "EUR": ("Martinique", "MTQ"),  # Euro
    "MRU": ("Mauritania", "MRT"),  # Mauritanian Ouguiya
    "MUR": ("Mauritius", "MUS"),  # Mauritian Rupee
    "MXN": ("Mexico", "MEX"),  # Mexican Peso
    "USD": ("Micronesia", "FSM"),  # United States Dollar
    "MDL": ("Moldova", "MDA"),  # Moldovan Leu
    "EUR": ("Monaco", "MCO"),  # Euro
    "MNT": ("Mongolia", "MNG"),  # Mongolian Tugrik
    "EUR": ("Montenegro", "MNE"),  # Euro
    "MAD": ("Morocco", "MAR"),  # Moroccan Dirham
    "MZN": ("Mozambique", "MOZ"),  # Mozambican Metical
    "MMK": ("Myanmar", "MMR"),  # Burmese Kyat
    "NAD": ("Namibia", "NAM"),  # Namibian Dollar
    "AUD": ("Nauru", "NRU"),  # Australian Dollar
    "NPR": ("Nepal", "NPL"),  # Nepalese Rupee
    "ANG": ("Netherlands", "NLD"),  # Euro
    "NZD": ("New Zealand", "NZL"),  # New Zealand Dollar
    "NIO": ("Nicaragua", "NIC"),  # Nicaraguan Cordoba
    "XOF": ("Niger", "NER"),  # West African CFA Franc
    "NGN": ("Nigeria", "NGA"),  # Nigerian Naira
    "NZD": ("Niue", "NIU"),  # New Zealand Dollar
    "AUD": ("Norfolk Island", "NFK"),  # Australian Dollar
    "NOK": ("Norway", "NOR"),  # Norwegian Krone
    "OMR": ("Oman", "OMN"),  # Omani Rial
    "PKR": ("Pakistan", "PAK"),  # Pakistani Rupee
    "USD": ("Palau", "PLW"),  # United States Dollar
    "PAB": ("Panama", "PAN"),  # Panamanian Balboa
    "PGK": ("Papua New Guinea", "PNG"),  # Papua New Guinean Kina
    "PYG": ("Paraguay", "PRY"),  # Paraguayan Guarani
    "PEN": ("Peru", "PER"),  # Peruvian Sol
    "PHP": ("Philippines", "PHL"),  # Philippine Peso
    "PLN": ("Poland", "POL"),  # Polish Zloty
    "EUR": ("Portugal", "PRT"),  # Euro
    "USD": ("Puerto Rico", "PRI"),  # United States Dollar
    "QAR": ("Qatar", "QAT"),  # Qatari Riyal
    "EUR": ("Reunion", "REU"),  # Euro
    "RON": ("Romania", "ROU"),  # Romanian Leu
    "RUB": ("Russia", "RUS"),  # Russian Ruble
    "RWF": ("Rwanda", "RWA"),  # Rwandan Franc
    "SHP": ("Saint Helena", "SHN"),  # Saint Helena Pound
    "XCD": ("Saint Kitts and Nevis", "KNA"),  # East Caribbean Dollar
    "XCD": ("Saint Lucia", "LCA"),  # East Caribbean Dollar
    "XCD": ("Saint Vincent and the Grenadines", "VCT"),  # East Caribbean Dollar
    "WST": ("Samoa", "WSM"),  # Samoan Tala
    "EUR": ("San Marino", "SMR"),  # Euro
    "STN": ("Sao Tome and Principe", "STP"),  # Sao Tome and Principe Dobra
    "SAR": ("Saudi Arabia", "SAU"),  # Saudi Riyal
    "XOF": ("Senegal", "SEN"),  # West African CFA Franc
    "RSD": ("Serbia", "SRB"),  # Serbian Dinar
    "SCR": ("Seychelles", "SYC"),  # Seychellois Rupee
    "SLL": ("Sierra Leone", "SLE"),  # Sierra Leonean Leone
    "SGD": ("Singapore", "SGP"),  # Singapore Dollar
    "EUR": ("Slovakia", "SVK"),  # Euro
    "EUR": ("Slovenia", "SVN"),  # Euro
    "SBD": ("Solomon Islands", "SLB"),  # Solomon Islands Dollar
    "SOS": ("Somalia", "SOM"),  # Somali Shilling
    "ZAR": ("South Africa", "ZAF"),  # South African Rand
    "EUR": ("Spain", "ESP"),  # Euro
    "LKR": ("Sri Lanka", "LKA"),  # Sri Lankan Rupee
    "SDG": ("Sudan", "SDN"),  # Sudanese Pound
    "SRD": ("Suriname", "SUR"),  # Surinamese Dollar
    "SEK": ("Sweden", "SWE"),  # Swedish Krona
    "CHF": ("Switzerland", "CHE"),  # Swiss Franc
    "SYP": ("Syria", "SYR"),  # Syrian Pound
    "TWD": ("Taiwan", "TWN"),  # New Taiwan Dollar
    "TJS": ("Tajikistan", "TJK"),  # Tajikistani Somoni
    "TZS": ("Tanzania", "TZA"),  # Tanzanian Shilling
    "THB": ("Thailand", "THA"),  # Thai Baht
    "USD": ("Timor-Leste", "TLS"),  # United States Dollar
    "XOF": ("Togo", "TGO"),  # West African CFA Franc
    "TOP": ("Tonga", "TON"),  # Tongan Pa'anga
    "TTD": ("Trinidad and Tobago", "TTO"),  # Trinidad and Tobago Dollar
    "TND": ("Tunisia", "TUN"),  # Tunisian Dinar
    "TRY": ("Turkey", "TUR"),  # Turkish Lira
    "TMT": ("Turkmenistan", "TKM"),  # Turkmenistani Manat
    "AUD": ("Tuvalu", "TUV"),  # Australian Dollar
    "UGX": ("Uganda", "UGA"),  # Ugandan Shilling
    "UAH": ("Ukraine", "UKR"),  # Ukrainian Hryvnia
    "AED": ("United Arab Emirates", "ARE"),  # UAE Dirham
    "GBP": ("United Kingdom", "GBR"),  # British Pound
    "USD": ("United States", "USA"),  # United States Dollar
    "UYU": ("Uruguay", "URY"),  # Uruguayan Peso
    "UZS": ("Uzbekistan", "UZB"),  # Uzbekistani Som
    "VUV": ("Vanuatu", "VUT"),  # Vanuatu Vatu
    "EUR": ("Vatican City", "VAT"),  # Euro
    "VES": ("Venezuela", "VEN"),  # Venezuelan Bolivar
    "VND": ("Vietnam", "VNM"),  # Vietnamese Dong
    "XPF": ("Wallis and Futuna", "WLF"),  # CFP Franc
    "YER": ("Yemen", "YEM"),  # Yemeni Rial
    "ZMW": ("Zambia", "ZMB"),  # Zambian Kwacha
    "ZWL": ("Zimbabwe", "ZWE"),  # Zimbabwean Dollar
    "AWG": ("Aruba", "ARB"),
    "BMD": ("Bermuda", "BERM"),
    "CDF": ("Democratic Republic of Congo", "DRC"),
    "FKP": ("Falkland island", "FK"),
    "FOK": ("Faroe Island", "FO"),
    "GGP": ("Guernsey", "GG"),
    "GIP": ("Gilbraltar", "GI"),
    "IMP": ("Isle of man", "IM"),
    "BMD": ("Bermuda", "BERM"),
    "JEP": ("Jersey", "JE"),
    "KID": ("Republic of Kiribati", "KI"),
    "KYD": ("Cayman islands", "KY"),
    "MKD": ("North macedonia", "MK"),
    "MOP": ("Macau", "MO"),
    "SSP": ("South sudan", "SS"),
    "XDR": ("IMF", "IMF"),
    "TVD": ("Tuvalu", "TV"),
}


cursor.execute("SELECT DISTINCT Currency_code FROM rates")
currency_codes = cursor.fetchall()

# Iterate through each currency code
for (Currency_code,) in currency_codes:
 
    if Currency_code in currency_country_mapping:
        country_name, country_code = currency_country_mapping[Currency_code]
    else:
        
        country_name = None
        country_code = None
        currency_name = None

   
    update_query = "UPDATE rates SET Country = %s, Country_Code = %s WHERE Currency_code = %s"
    cursor.execute(update_query, (country_name, country_code, Currency_code))
    conn.commit()


cursor.close()
conn.close()
