"""empty message

Revision ID: 14107a12fd38
Revises: 9f87a8df07a8
Create Date: 2023-12-14 10:03:01.809784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14107a12fd38'
down_revision = '9f87a8df07a8'
branch_labels = None
depends_on = None

nsc_puj_data = [
  {
    "objectCd": "CA_BC",
    "objectDsc": "BRITISH COLUMBIA"
  },
  {
    "objectCd": "CA_AB",
    "objectDsc": "ALBERTA"
  },
  {
    "objectCd": "US_WA",
    "objectDsc": "WASHINGTON"
  },
  {
    "objectCd": "CA_MB",
    "objectDsc": "MANITOBA"
  },
  {
    "objectCd": "CA_NB",
    "objectDsc": "NEW BRUNSWICK"
  },
  {
    "objectCd": "CA_NF",
    "objectDsc": "NEWFOUNDLAND & LABRADOR"
  },
  {
    "objectCd": "CA_NS",
    "objectDsc": "NOVA SCOTIA"
  },
  {
    "objectCd": "CA_NT",
    "objectDsc": "NORTHWEST TERRITORIES"
  },
  {
    "objectCd": "CA_NU",
    "objectDsc": "NUNAVUT"
  },
  {
    "objectCd": "CA_ON",
    "objectDsc": "ONTARIO"
  },
  {
    "objectCd": "CA_PE",
    "objectDsc": "PRINCE EDWARD ISLAND"
  },
  {
    "objectCd": "CA_QC",
    "objectDsc": "QUEBEC"
  },
  {
    "objectCd": "CA_SK",
    "objectDsc": "SASKATCHEWAN"
  },
  {
    "objectCd": "CA_YT",
    "objectDsc": "YUKON"
  },
  {
    "objectCd": "US_AK",
    "objectDsc": "ALASKA"
  },
  {
    "objectCd": "US_AL",
    "objectDsc": "ALABAMA"
  },
  {
    "objectCd": "US_AR",
    "objectDsc": "ARKANSAS"
  },
  {
    "objectCd": "US_AZ",
    "objectDsc": "ARIZONA"
  },
  {
    "objectCd": "US_CA",
    "objectDsc": "CALIFORNIA"
  },
  {
    "objectCd": "US_CO",
    "objectDsc": "COLORADO"
  },
  {
    "objectCd": "US_CT",
    "objectDsc": "CONNECTICUT"
  },
  {
    "objectCd": "US_DC",
    "objectDsc": "DISTRICT OF COLUMBIA"
  },
  {
    "objectCd": "US_DE",
    "objectDsc": "DELAWARE"
  },
  {
    "objectCd": "US_FL",
    "objectDsc": "FLORIDA"
  },
  {
    "objectCd": "US_GA",
    "objectDsc": "GEORGIA"
  },
  {
    "objectCd": "US_IA",
    "objectDsc": "IOWA"
  },
  {
    "objectCd": "US_ID",
    "objectDsc": "IDAHO"
  },
  {
    "objectCd": "US_IL",
    "objectDsc": "ILLINOIS"
  },
  {
    "objectCd": "US_IN",
    "objectDsc": "INDIANA"
  },
  {
    "objectCd": "US_KS",
    "objectDsc": "KANSAS"
  },
  {
    "objectCd": "US_KY",
    "objectDsc": "KENTUCKY"
  },
  {
    "objectCd": "US_LA",
    "objectDsc": "LOUISIANA"
  },
  {
    "objectCd": "US_MA",
    "objectDsc": "MASSACHUSETTS"
  },
  {
    "objectCd": "US_MD",
    "objectDsc": "MARYLAND"
  },
  {
    "objectCd": "US_ME",
    "objectDsc": "MAINE"
  },
  {
    "objectCd": "US_MI",
    "objectDsc": "MICHIGAN"
  },
  {
    "objectCd": "US_MN",
    "objectDsc": "MINNESOTA"
  },
  {
    "objectCd": "US_MO",
    "objectDsc": "MISSOURI"
  },
  {
    "objectCd": "US_MS",
    "objectDsc": "MISSISSIPPI"
  },
  {
    "objectCd": "US_MT",
    "objectDsc": "MONTANA"
  },
  {
    "objectCd": "US_NC",
    "objectDsc": "NORTH CAROLINA"
  },
  {
    "objectCd": "US_ND",
    "objectDsc": "NORTH DAKOTA"
  },
  {
    "objectCd": "US_NE",
    "objectDsc": "NEBRASKA"
  },
  {
    "objectCd": "US_NH",
    "objectDsc": "NEW HAMPSHIRE"
  },
  {
    "objectCd": "US_NJ",
    "objectDsc": "NEW JERSEY"
  },
  {
    "objectCd": "US_NM",
    "objectDsc": "NEW MEXICO"
  },
  {
    "objectCd": "US_NV",
    "objectDsc": "NEVADA"
  },
  {
    "objectCd": "US_NY",
    "objectDsc": "NEW YORK"
  },
  {
    "objectCd": "US_OH",
    "objectDsc": "OHIO"
  },
  {
    "objectCd": "US_OK",
    "objectDsc": "OKLAHOMA"
  },
  {
    "objectCd": "US_OR",
    "objectDsc": "OREGON"
  },
  {
    "objectCd": "US_PA",
    "objectDsc": "PENNSYLVANIA"
  },
  {
    "objectCd": "US_RI",
    "objectDsc": "RHODE ISLAND"
  },
  {
    "objectCd": "US_SC",
    "objectDsc": "SOUTH CAROLINA"
  },
  {
    "objectCd": "US_SD",
    "objectDsc": "SOUTH DAKOTA"
  },
  {
    "objectCd": "US_TN",
    "objectDsc": "TENNESSEE"
  },
  {
    "objectCd": "US_TX",
    "objectDsc": "TEXAS"
  },
  {
    "objectCd": "US_UT",
    "objectDsc": "UTAH"
  },
  {
    "objectCd": "US_VA",
    "objectDsc": "VIRGINIA"
  },
  {
    "objectCd": "US_VT",
    "objectDsc": "VERMONT"
  },
  {
    "objectCd": "US_WI",
    "objectDsc": "WISCONSIN"
  },
  {
    "objectCd": "US_WV",
    "objectDsc": "WEST VIRGINIA"
  },
  {
    "objectCd": "US_WY",
    "objectDsc": "WYOMING"
  },
  {
    "objectCd": "MX",
    "objectDsc": "MEXICO"
  },
  {
    "objectCd": "ZZ",
    "objectDsc": "OTHER"
  }
]

jurisdiction_country_data = [
  {
    "objectCd": "XZ",
    "objectDsc": "--back--"
  },
  {
    "objectCd": "CA_CF",
    "objectDsc": "CANADIAN FORCES (DND)"
  },
  {
    "objectCd": "AF",
    "objectDsc": "AFGHANISTAN"
  },
  {
    "objectCd": "AL",
    "objectDsc": "ALBANIA"
  },
  {
    "objectCd": "DZ",
    "objectDsc": "ALGERIA"
  },
  {
    "objectCd": "AD",
    "objectDsc": "ANDORRA"
  },
  {
    "objectCd": "AO",
    "objectDsc": "ANGOLA"
  },
  {
    "objectCd": "AI",
    "objectDsc": "ANGUILLA"
  },
  {
    "objectCd": "AQ",
    "objectDsc": "ANTARCTICA"
  },
  {
    "objectCd": "AG",
    "objectDsc": "ANTIGUA & BARBUDA"
  },
  {
    "objectCd": "AR",
    "objectDsc": "ARGENTINA"
  },
  {
    "objectCd": "AM",
    "objectDsc": "ARMENIA"
  },
  {
    "objectCd": "AW",
    "objectDsc": "ARUBA"
  },
  {
    "objectCd": "AU",
    "objectDsc": "AUSTRALIA"
  },
  {
    "objectCd": "AT",
    "objectDsc": "AUSTRIA"
  },
  {
    "objectCd": "AZ",
    "objectDsc": "AZERBAIJAN"
  },
  {
    "objectCd": "BS",
    "objectDsc": "BAHAMAS"
  },
  {
    "objectCd": "BH",
    "objectDsc": "BAHRAIN"
  },
  {
    "objectCd": "BD",
    "objectDsc": "BANGLADESH"
  },
  {
    "objectCd": "BB",
    "objectDsc": "BARBADOS"
  },
  {
    "objectCd": "BY",
    "objectDsc": "BELARUS"
  },
  {
    "objectCd": "BE",
    "objectDsc": "BELGIUM"
  },
  {
    "objectCd": "BZ",
    "objectDsc": "BELIZE"
  },
  {
    "objectCd": "BJ",
    "objectDsc": "BENIN"
  },
  {
    "objectCd": "BM",
    "objectDsc": "BERMUDA"
  },
  {
    "objectCd": "BT",
    "objectDsc": "BHUTAN"
  },
  {
    "objectCd": "BO",
    "objectDsc": "BOLIVIA"
  },
  {
    "objectCd": "BA",
    "objectDsc": "BOSNIA & HERZEGOVINA"
  },
  {
    "objectCd": "BW",
    "objectDsc": "BOTSWANA"
  },
  {
    "objectCd": "BV",
    "objectDsc": "BOUVET ISLAND"
  },
  {
    "objectCd": "BR",
    "objectDsc": "BRAZIL"
  },
  {
    "objectCd": "IO",
    "objectDsc": "BRITISH INDIAN OCEAN TERRITORY"
  },
  {
    "objectCd": "BN",
    "objectDsc": "BRUNEI DARUSSALAM"
  },
  {
    "objectCd": "BG",
    "objectDsc": "BULGARIA"
  },
  {
    "objectCd": "BF",
    "objectDsc": "BURKINA FASO"
  },
  {
    "objectCd": "BI",
    "objectDsc": "BURUNDI"
  },
  {
    "objectCd": "KH",
    "objectDsc": "CAMBODIA"
  },
  {
    "objectCd": "CM",
    "objectDsc": "CAMEROON"
  },
  {
    "objectCd": "CV",
    "objectDsc": "CAPE VERDE"
  },
  {
    "objectCd": "KY",
    "objectDsc": "CAYMAN ISLANDS"
  },
  {
    "objectCd": "CF",
    "objectDsc": "CENTRAL AFRICAN REPUBLIC"
  },
  {
    "objectCd": "TD",
    "objectDsc": "CHAD"
  },
  {
    "objectCd": "CL",
    "objectDsc": "CHILE"
  },
  {
    "objectCd": "CN",
    "objectDsc": "CHINA"
  },
  {
    "objectCd": "CX",
    "objectDsc": "CHRISTMAS ISLAND"
  },
  {
    "objectCd": "CC",
    "objectDsc": "COCOS (KEELING) ISLANDS"
  },
  {
    "objectCd": "CO",
    "objectDsc": "COLOMBIA"
  },
  {
    "objectCd": "KM",
    "objectDsc": "COMOROS"
  },
  {
    "objectCd": "CG",
    "objectDsc": "CONGO"
  },
  {
    "objectCd": "CK",
    "objectDsc": "COOK ISLANDS"
  },
  {
    "objectCd": "CR",
    "objectDsc": "COSTA RICA"
  },
  {
    "objectCd": "CI",
    "objectDsc": "COTE D'IVOIRE"
  },
  {
    "objectCd": "HR",
    "objectDsc": "CROATIA"
  },
  {
    "objectCd": "CU",
    "objectDsc": "CUBA"
  },
  {
    "objectCd": "CY",
    "objectDsc": "CYPRUS"
  },
  {
    "objectCd": "CZ",
    "objectDsc": "CZECH REPUBLIC"
  },
  {
    "objectCd": "DK",
    "objectDsc": "DENMARK"
  },
  {
    "objectCd": "DJ",
    "objectDsc": "DJIBOUTI"
  },
  {
    "objectCd": "DM",
    "objectDsc": "DOMINICA"
  },
  {
    "objectCd": "DO",
    "objectDsc": "DOMINICAN REPUBLIC"
  },
  {
    "objectCd": "TP",
    "objectDsc": "EAST TIMOR"
  },
  {
    "objectCd": "EC",
    "objectDsc": "ECUADOR"
  },
  {
    "objectCd": "EG",
    "objectDsc": "EGYPT"
  },
  {
    "objectCd": "SV",
    "objectDsc": "EL SALVADOR"
  },
  {
    "objectCd": "GQ",
    "objectDsc": "EQUATORIAL GUINEA"
  },
  {
    "objectCd": "ER",
    "objectDsc": "ERITREA"
  },
  {
    "objectCd": "EE",
    "objectDsc": "ESTONIA"
  },
  {
    "objectCd": "ET",
    "objectDsc": "ETHIOPIA"
  },
  {
    "objectCd": "FK",
    "objectDsc": "FALKLAND ISLANDS (MALVINAS)"
  },
  {
    "objectCd": "FO",
    "objectDsc": "FAROE ISLANDS"
  },
  {
    "objectCd": "FJ",
    "objectDsc": "FIJI"
  },
  {
    "objectCd": "FI",
    "objectDsc": "FINLAND"
  },
  {
    "objectCd": "FR",
    "objectDsc": "FRANCE"
  },
  {
    "objectCd": "GF",
    "objectDsc": "FRENCH GUIANA"
  },
  {
    "objectCd": "PF",
    "objectDsc": "FRENCH POLYNESIA"
  },
  {
    "objectCd": "TF",
    "objectDsc": "FRENCH SOUTHERN & ANTARCTIC LANDS"
  },
  {
    "objectCd": "GA",
    "objectDsc": "GABON"
  },
  {
    "objectCd": "GM",
    "objectDsc": "GAMBIA"
  },
  {
    "objectCd": "GE",
    "objectDsc": "GEORGIA"
  },
  {
    "objectCd": "DE",
    "objectDsc": "GERMANY"
  },
  {
    "objectCd": "GH",
    "objectDsc": "GHANA"
  },
  {
    "objectCd": "GI",
    "objectDsc": "GIBRALTAR"
  },
  {
    "objectCd": "GR",
    "objectDsc": "GREECE"
  },
  {
    "objectCd": "GL",
    "objectDsc": "GREENLAND"
  },
  {
    "objectCd": "GD",
    "objectDsc": "GRENADA"
  },
  {
    "objectCd": "GP",
    "objectDsc": "GUADELOUPE"
  },
  {
    "objectCd": "GT",
    "objectDsc": "GUATEMALA"
  },
  {
    "objectCd": "GN",
    "objectDsc": "GUINEA"
  },
  {
    "objectCd": "GW",
    "objectDsc": "GUINEA-BISSAU"
  },
  {
    "objectCd": "GY",
    "objectDsc": "GUYANA"
  },
  {
    "objectCd": "HT",
    "objectDsc": "HAITI"
  },
  {
    "objectCd": "HM",
    "objectDsc": "HEARD & MCDONALD ISLANDS"
  },
  {
    "objectCd": "HN",
    "objectDsc": "HONDURAS"
  },
  {
    "objectCd": "HK",
    "objectDsc": "HONG KONG"
  },
  {
    "objectCd": "HU",
    "objectDsc": "HUNGARY"
  },
  {
    "objectCd": "IS",
    "objectDsc": "ICELAND"
  },
  {
    "objectCd": "IN",
    "objectDsc": "INDIA"
  },
  {
    "objectCd": "ID",
    "objectDsc": "INDONESIA"
  },
  {
    "objectCd": "IR",
    "objectDsc": "IRAN"
  },
  {
    "objectCd": "IQ",
    "objectDsc": "IRAQ"
  },
  {
    "objectCd": "IE",
    "objectDsc": "IRELAND"
  },
  {
    "objectCd": "IL",
    "objectDsc": "ISRAEL"
  },
  {
    "objectCd": "IT",
    "objectDsc": "ITALY"
  },
  {
    "objectCd": "JM",
    "objectDsc": "JAMAICA"
  },
  {
    "objectCd": "JP",
    "objectDsc": "JAPAN"
  },
  {
    "objectCd": "JO",
    "objectDsc": "JORDAN"
  },
  {
    "objectCd": "KZ",
    "objectDsc": "KAZAKHSTAN"
  },
  {
    "objectCd": "KE",
    "objectDsc": "KENYA"
  },
  {
    "objectCd": "KI",
    "objectDsc": "KIRIBATI"
  },
  {
    "objectCd": "KW",
    "objectDsc": "KUWAIT"
  },
  {
    "objectCd": "KG",
    "objectDsc": "KYRGYZSTAN"
  },
  {
    "objectCd": "LA",
    "objectDsc": "LAOS"
  },
  {
    "objectCd": "LV",
    "objectDsc": "LATVIA"
  },
  {
    "objectCd": "LB",
    "objectDsc": "LEBANON"
  },
  {
    "objectCd": "LS",
    "objectDsc": "LESOTHO"
  },
  {
    "objectCd": "LR",
    "objectDsc": "LIBERIA"
  },
  {
    "objectCd": "LY",
    "objectDsc": "LIBYA"
  },
  {
    "objectCd": "LI",
    "objectDsc": "LIECHTENSTEIN"
  },
  {
    "objectCd": "LT",
    "objectDsc": "LITHUANIA"
  },
  {
    "objectCd": "LU",
    "objectDsc": "LUXEMBOURG"
  },
  {
    "objectCd": "MO",
    "objectDsc": "MACAU"
  },
  {
    "objectCd": "MK",
    "objectDsc": "MACEDONIA"
  },
  {
    "objectCd": "MG",
    "objectDsc": "MADAGASCAR"
  },
  {
    "objectCd": "MW",
    "objectDsc": "MALAWI"
  },
  {
    "objectCd": "MY",
    "objectDsc": "MALAYSIA"
  },
  {
    "objectCd": "MV",
    "objectDsc": "MALDIVES"
  },
  {
    "objectCd": "ML",
    "objectDsc": "MALI"
  },
  {
    "objectCd": "MT",
    "objectDsc": "MALTA"
  },
  {
    "objectCd": "MH",
    "objectDsc": "MARSHALL ISLANDS"
  },
  {
    "objectCd": "MQ",
    "objectDsc": "MARTINIQUE"
  },
  {
    "objectCd": "MR",
    "objectDsc": "MAURITANIA"
  },
  {
    "objectCd": "MU",
    "objectDsc": "MAURITIUS"
  },
  {
    "objectCd": "YT",
    "objectDsc": "MAYOTTE"
  },
  {
    "objectCd": "MX",
    "objectDsc": "MEXICO"
  },
  {
    "objectCd": "FM",
    "objectDsc": "MICRONESIA"
  },
  {
    "objectCd": "MD",
    "objectDsc": "MOLDOVA"
  },
  {
    "objectCd": "MC",
    "objectDsc": "MONACO"
  },
  {
    "objectCd": "MN",
    "objectDsc": "MONGOLIA"
  },
  {
    "objectCd": "MS",
    "objectDsc": "MONTSERRAT"
  },
  {
    "objectCd": "MA",
    "objectDsc": "MOROCCO"
  },
  {
    "objectCd": "MZ",
    "objectDsc": "MOZAMBIQUE"
  },
  {
    "objectCd": "MM",
    "objectDsc": "MYANMAR"
  },
  {
    "objectCd": "NA",
    "objectDsc": "NAMIBIA"
  },
  {
    "objectCd": "NR",
    "objectDsc": "NAURU"
  },
  {
    "objectCd": "NP",
    "objectDsc": "NEPAL"
  },
  {
    "objectCd": "NL",
    "objectDsc": "NETHERLANDS"
  },
  {
    "objectCd": "AN",
    "objectDsc": "NETHERLANDS ANTILLES"
  },
  {
    "objectCd": "NC",
    "objectDsc": "NEW CALEDONIA"
  },
  {
    "objectCd": "NZ",
    "objectDsc": "NEW ZEALAND"
  },
  {
    "objectCd": "NI",
    "objectDsc": "NICARAGUA"
  },
  {
    "objectCd": "NE",
    "objectDsc": "NIGER"
  },
  {
    "objectCd": "NG",
    "objectDsc": "NIGERIA"
  },
  {
    "objectCd": "NU",
    "objectDsc": "NIUE"
  },
  {
    "objectCd": "NF",
    "objectDsc": "NORFOLK ISLAND"
  },
  {
    "objectCd": "KP",
    "objectDsc": "NORTH KOREA"
  },
  {
    "objectCd": "NO",
    "objectDsc": "NORWAY"
  },
  {
    "objectCd": "OM",
    "objectDsc": "OMAN"
  },
  {
    "objectCd": "PK",
    "objectDsc": "PAKISTAN"
  },
  {
    "objectCd": "PW",
    "objectDsc": "PALAU"
  },
  {
    "objectCd": "PA",
    "objectDsc": "PANAMA"
  },
  {
    "objectCd": "PG",
    "objectDsc": "PAPUA NEW GUINEA"
  },
  {
    "objectCd": "PY",
    "objectDsc": "PARAGUAY"
  },
  {
    "objectCd": "PE",
    "objectDsc": "PERU"
  },
  {
    "objectCd": "PH",
    "objectDsc": "PHILIPPINES"
  },
  {
    "objectCd": "PN",
    "objectDsc": "PITCAIRN"
  },
  {
    "objectCd": "PL",
    "objectDsc": "POLAND"
  },
  {
    "objectCd": "PT",
    "objectDsc": "PORTUGAL"
  },
  {
    "objectCd": "QA",
    "objectDsc": "QATAR"
  },
  {
    "objectCd": "RE",
    "objectDsc": "REUNION"
  },
  {
    "objectCd": "RO",
    "objectDsc": "ROMANIA"
  },
  {
    "objectCd": "RU",
    "objectDsc": "RUSSIAN FEDERATION"
  },
  {
    "objectCd": "RW",
    "objectDsc": "RWANDA"
  },
  {
    "objectCd": "WS",
    "objectDsc": "SAMOA"
  },
  {
    "objectCd": "SM",
    "objectDsc": "SAN MARINO"
  },
  {
    "objectCd": "ST",
    "objectDsc": "SAO TOME & PRINCIPE"
  },
  {
    "objectCd": "SA",
    "objectDsc": "SAUDI ARABIA"
  },
  {
    "objectCd": "SN",
    "objectDsc": "SENEGAL"
  },
  {
    "objectCd": "SC",
    "objectDsc": "SEYCHELLES"
  },
  {
    "objectCd": "SL",
    "objectDsc": "SIERRA LEONE"
  },
  {
    "objectCd": "SG",
    "objectDsc": "SINGAPORE"
  },
  {
    "objectCd": "SK",
    "objectDsc": "SLOVAKIA"
  },
  {
    "objectCd": "SI",
    "objectDsc": "SLOVENIA"
  },
  {
    "objectCd": "SB",
    "objectDsc": "SOLOMON ISLANDS"
  },
  {
    "objectCd": "SO",
    "objectDsc": "SOMALIA"
  },
  {
    "objectCd": "ZA",
    "objectDsc": "SOUTH AFRICA"
  },
  {
    "objectCd": "GS",
    "objectDsc": "SOUTH GEORGIA & THE SOUTH SANDWICH ISLANDS"
  },
  {
    "objectCd": "KR",
    "objectDsc": "SOUTH KOREA"
  },
  {
    "objectCd": "ES",
    "objectDsc": "SPAIN"
  },
  {
    "objectCd": "LK",
    "objectDsc": "SRI LANKA"
  },
  {
    "objectCd": "SH",
    "objectDsc": "ST. HELENA"
  },
  {
    "objectCd": "KN",
    "objectDsc": "ST. KITTS & NEVIS"
  },
  {
    "objectCd": "LC",
    "objectDsc": "ST. LUCIA"
  },
  {
    "objectCd": "PM",
    "objectDsc": "ST. PIERRE & MIQUELON"
  },
  {
    "objectCd": "VC",
    "objectDsc": "ST. VINCENT & THE GRENADINES"
  },
  {
    "objectCd": "SD",
    "objectDsc": "SUDAN"
  },
  {
    "objectCd": "SR",
    "objectDsc": "SURINAME"
  },
  {
    "objectCd": "SJ",
    "objectDsc": "SVALBARD & JAN MAYEN ISLANDS"
  },
  {
    "objectCd": "SZ",
    "objectDsc": "SWAZILAND"
  },
  {
    "objectCd": "SE",
    "objectDsc": "SWEDEN"
  },
  {
    "objectCd": "CH",
    "objectDsc": "SWITZERLAND"
  },
  {
    "objectCd": "SY",
    "objectDsc": "SYRIAN ARAB REPUBLIC"
  },
  {
    "objectCd": "TW",
    "objectDsc": "TAIWAN"
  },
  {
    "objectCd": "TJ",
    "objectDsc": "TAJIKISTAN"
  },
  {
    "objectCd": "TZ",
    "objectDsc": "TANZANIA"
  },
  {
    "objectCd": "TH",
    "objectDsc": "THAILAND"
  },
  {
    "objectCd": "TG",
    "objectDsc": "TOGO"
  },
  {
    "objectCd": "TK",
    "objectDsc": "TOKELAU"
  },
  {
    "objectCd": "TO",
    "objectDsc": "TONGA"
  },
  {
    "objectCd": "TT",
    "objectDsc": "TRINIDAD & TOBAGO"
  },
  {
    "objectCd": "TN",
    "objectDsc": "TUNISIA"
  },
  {
    "objectCd": "TR",
    "objectDsc": "TURKEY"
  },
  {
    "objectCd": "TM",
    "objectDsc": "TURKMENISTAN"
  },
  {
    "objectCd": "TC",
    "objectDsc": "TURKS & CAICOS ISLANDS"
  },
  {
    "objectCd": "TV",
    "objectDsc": "TUVALU"
  },
  {
    "objectCd": "UG",
    "objectDsc": "UGANDA"
  },
  {
    "objectCd": "UA",
    "objectDsc": "UKRAINE"
  },
  {
    "objectCd": "AE",
    "objectDsc": "UNITED ARAB EMIRATES"
  },
  {
    "objectCd": "GB",
    "objectDsc": "UNITED KINGDOM"
  },
  {
    "objectCd": "UY",
    "objectDsc": "URUGUAY"
  },
  {
    "objectCd": "UZ",
    "objectDsc": "UZBEKISTAN"
  },
  {
    "objectCd": "VU",
    "objectDsc": "VANUATU"
  },
  {
    "objectCd": "VA",
    "objectDsc": "VATICAN CITY"
  },
  {
    "objectCd": "VE",
    "objectDsc": "VENEZUELA"
  },
  {
    "objectCd": "VN",
    "objectDsc": "VIETNAM"
  },
  {
    "objectCd": "VG",
    "objectDsc": "VIRGIN ISLANDS (BRITISH)"
  },
  {
    "objectCd": "WF",
    "objectDsc": "WALLIS & FUTUNA ISLANDS"
  },
  {
    "objectCd": "EH",
    "objectDsc": "WESTERN SAHARA"
  },
  {
    "objectCd": "YE",
    "objectDsc": "YEMEN"
  },
  {
    "objectCd": "YU",
    "objectDsc": "YUGOSLAVIA"
  },
  {
    "objectCd": "ZR",
    "objectDsc": "ZAIRE"
  },
  {
    "objectCd": "ZM",
    "objectDsc": "ZAMBIA"
  },
  {
    "objectCd": "ZW",
    "objectDsc": "ZIMBABWE"
  },
  {
    "objectCd": "ZZ",
    "objectDsc": "OTHER"
  }
]

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jurisdiction_country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('objectCd', sa.String(), nullable=True),
    sa.Column('objectDsc', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nsc_puj',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('objectCd', sa.String(), nullable=True),
    sa.Column('objectDsc', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    
    with op.get_context().autocommit_block():
        bind = op.get_bind()
        meta = sa.MetaData()
        meta.bind = bind
        meta.reflect(bind=bind, only=('jurisdiction_country','nsc_puj',))
        jurisdiction_country = sa.Table('jurisdiction_country', meta)
        op.bulk_insert(jurisdiction_country, jurisdiction_country_data)
        
        nsc_puj = sa.Table('nsc_puj', meta)
        op.bulk_insert(nsc_puj, nsc_puj_data)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nsc_puj')
    op.drop_table('jurisdiction_country')
    # ### end Alembic commands ###
