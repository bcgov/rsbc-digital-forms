"""empty message

Revision ID: f76bbde02978
Revises: 0134c884845f
Create Date: 2023-11-22 20:03:25.778970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f76bbde02978'
down_revision = '0134c884845f'
branch_labels = None
depends_on = None

new_data = [
  {
    "agency_name": "Abbotsford Police Dept.",
    "agency_id": "AB",
    "agency_city": "Abbotsford",
    "prime_vjur": "AB",
    "icbc_detachment_name": "ABBOTSFORD POLICE DEPARTMENT",
    "icbc_city_name": "ABBOTSFORD",
    "vips_policedetachments_agency_id": "92",
    "vips_policedetachments_agency_nm": "Abbotsford"
  },
  {
    "agency_name": "BCHP 100 Mile House",
    "agency_id": "3303",
    "agency_city": "100 Mile House",
    "prime_vjur": "3303",
    "icbc_detachment_name": "100 MILE HOUSE RCMP",
    "icbc_city_name": "100 MILE HOUSE",
    "vips_policedetachments_agency_id": "56",
    "vips_policedetachments_agency_nm": "100 Mile House/TS"
  },
  {
    "agency_name": "BCHP Ashcroft",
    "agency_id": "2100",
    "agency_city": "Ashcroft",
    "prime_vjur": "2100",
    "icbc_detachment_name": "SOUTHEAST DISTRICT RCMP",
    "icbc_city_name": "ASHCROFT",
    "vips_policedetachments_agency_id": "44",
    "vips_policedetachments_agency_nm": "Ashcroft"
  },
  {
    "agency_name": "BCHP Burnaby",
    "agency_id": "1003",
    "agency_city": "Burnaby",
    "prime_vjur": "1003",
    "icbc_detachment_name": "BCHP - BURNABY",
    "icbc_city_name": "BURNABY",
    "vips_policedetachments_agency_id": "261",
    "vips_policedetachments_agency_nm": "Port Mann Highway Patrol"
  },
  {
    "agency_name": "BCHP Campbell River",
    "agency_id": "4323",
    "agency_city": "Campbell River",
    "prime_vjur": "4323",
    "icbc_detachment_name": "BCHP - CAMPBELL RIVER",
    "icbc_city_name": "CAMPBELL RIVER",
    "vips_policedetachments_agency_id": "258",
    "vips_policedetachments_agency_nm": "North Island Traffic Services"
  },
  {
    "agency_name": "BCHP Chemainus",
    "agency_id": "4206",
    "agency_city": "Chemainus",
    "prime_vjur": "4206",
    "icbc_detachment_name": "BCHP - CHEMAINUS",
    "icbc_city_name": "CHEMAINUS",
    "vips_policedetachments_agency_id": "209",
    "vips_policedetachments_agency_nm": "BCHP - Chemainus"
  },
  {
    "agency_name": "BCHP Chilliwack",
    "agency_id": "1501",
    "agency_city": "Chilliwack",
    "prime_vjur": "1501",
    "icbc_detachment_name": "UPPER FRASER VALLEY REG RCMP",
    "icbc_city_name": "CHILLIWACK",
    "vips_policedetachments_agency_id": "10",
    "vips_policedetachments_agency_nm": "Fraser Valley Traffic Services"
  },
  {
    "agency_name": "BCHP Clearwater",
    "agency_id": "2100",
    "agency_city": "Clearwater",
    "prime_vjur": "2100",
    "icbc_detachment_name": "SOUTHEAST DISTRICT RCMP",
    "icbc_city_name": "CLEARWATER",
    "vips_policedetachments_agency_id": "414",
    "vips_policedetachments_agency_nm": "BCHP - Clearwater"
  },
  {
    "agency_name": "BCHP CRD IRSU",
    "agency_id": "4110",
    "agency_city": "Victoria",
    "prime_vjur": "4110",
    "icbc_detachment_name": "BCHP - CRD IRSU",
    "icbc_city_name": "VICTORIA",
    "vips_policedetachments_agency_id": "246",
    "vips_policedetachments_agency_nm": "IRSU - CRD - Victoria"
  },
  {
    "agency_name": "BCHP Dawson Creek",
    "agency_id": "3403",
    "agency_city": "Dawson Creek",
    "prime_vjur": "3403",
    "icbc_detachment_name": "DAWSON CREEK RCMP",
    "icbc_city_name": "DAWSON CREEK",
    "vips_policedetachments_agency_id": "231",
    "vips_policedetachments_agency_nm": "IRSU - Dawson Creek"
  },
  {
    "agency_name": "BCHP Falkland",
    "agency_id": "2100",
    "agency_city": "Falkland",
    "prime_vjur": "2100",
    "icbc_detachment_name": "SOUTHEAST DISTRICT RCMP",
    "icbc_city_name": "FALKLAND",
    "vips_policedetachments_agency_id": "257",
    "vips_policedetachments_agency_nm": "BCHP - Falkland"
  },
  {
    "agency_name": "BCHP Fort Nelson",
    "agency_id": "3402",
    "agency_city": "Fort Nelson",
    "prime_vjur": "3402",
    "icbc_detachment_name": "NORTHERN ROCKIES RCMP",
    "icbc_city_name": "FORT NELSON",
    "vips_policedetachments_agency_id": "234",
    "vips_policedetachments_agency_nm": "IRSU - Fort Nelson"
  },
  {
    "agency_name": "BCHP Fort St. John",
    "agency_id": "3401",
    "agency_city": "Fort St. John",
    "prime_vjur": "3401",
    "icbc_detachment_name": "FORT ST. JOHN RCMP",
    "icbc_city_name": "FORT ST. JOHN",
    "vips_policedetachments_agency_id": "233",
    "vips_policedetachments_agency_nm": "IRSU - Fort St. John"
  },
  {
    "agency_name": "BCHP Fraser Coast IRSU",
    "agency_id": "1305",
    "agency_city": "Langley",
    "prime_vjur": "1305",
    "icbc_detachment_name": "BCHP - FRASER COAST IRSU",
    "icbc_city_name": "LANGLEY",
    "vips_policedetachments_agency_id": "226",
    "vips_policedetachments_agency_nm": "IRSU - Fraser Valley (LMD E.)"
  },
  {
    "agency_name": "BCHP Golden",
    "agency_id": "2100",
    "agency_city": "Golden",
    "prime_vjur": "2100",
    "icbc_detachment_name": "SOUTHEAST DISTRICT RCMP",
    "icbc_city_name": "GOLDEN",
    "vips_policedetachments_agency_id": "240",
    "vips_policedetachments_agency_nm": "IRSU-E TCH (Golden/Revelstoke)"
  },
  {
    "agency_name": "BCHP Kamloops",
    "agency_id": "2100",
    "agency_city": "Kamloops",
    "prime_vjur": "2100",
    "icbc_detachment_name": "SOUTHEAST DISTRICT RCMP",
    "icbc_city_name": "KAMLOOPS",
    "vips_policedetachments_agency_id": "243",
    "vips_policedetachments_agency_nm": "IRSU-S.E. Dist DRE/SFST Kamlps"
  },
  {
    "agency_name": "BCHP Kelowna",
    "agency_id": "2100",
    "agency_city": "Kelowna",
    "prime_vjur": "2100",
    "icbc_detachment_name": "SOUTHEAST DISTRICT RCMP",
    "icbc_city_name": "KELOWNA",
    "vips_policedetachments_agency_id": "416",
    "vips_policedetachments_agency_nm": "BCHP - Kelowna"
  },
  {
    "agency_name": "BCHP Keremeos",
    "agency_id": "2100",
    "agency_city": "Keremeos",
    "prime_vjur": "2100",
    "icbc_detachment_name": "SOUTHEAST DISTRICT RCMP",
    "icbc_city_name": "KEREMEOS",
    "vips_policedetachments_agency_id": "417",
    "vips_policedetachments_agency_nm": "BCHP - Keremeos"
  },
  {
    "agency_name": "BCHP Merritt",
    "agency_id": "2100",
    "agency_city": "Merritt",
    "prime_vjur": "2100",
    "icbc_detachment_name": "SOUTHEAST DISTRICT RCMP",
    "icbc_city_name": "MERRITT",
    "vips_policedetachments_agency_id": "418",
    "vips_policedetachments_agency_nm": "BCHP - Merritt"
  },
  {
    "agency_name": "BCHP Nelson",
    "agency_id": "2301",
    "agency_city": "Nelson",
    "prime_vjur": "2301",
    "icbc_detachment_name": "CENTRAL KOOTENAY RCMP",
    "icbc_city_name": "NELSON",
    "vips_policedetachments_agency_id": "225",
    "vips_policedetachments_agency_nm": "IRSU - W. Kootenay (Nelson)"
  },
  {
    "agency_name": "BCHP Parksville",
    "agency_id": "4307",
    "agency_city": "Parksville",
    "prime_vjur": "4307",
    "icbc_detachment_name": "BCHP - PARKSVILLE",
    "icbc_city_name": "PARKSVILLE",
    "vips_policedetachments_agency_id": "15",
    "vips_policedetachments_agency_nm": "Central Island Highway Patrol"
  },
  {
    "agency_name": "BCHP Prince George",
    "agency_id": "3100",
    "agency_city": "Prince George",
    "prime_vjur": "3100",
    "icbc_detachment_name": "NORTH DISTRICT RCMP",
    "icbc_city_name": "PRINCE GEORGE",
    "vips_policedetachments_agency_id": "227",
    "vips_policedetachments_agency_nm": "IRSU - Prince George"
  },
  {
    "agency_name": "BCHP Quesnel",
    "agency_id": "3301",
    "agency_city": "Quesnel",
    "prime_vjur": "3301",
    "icbc_detachment_name": "QUESNEL RCMP",
    "icbc_city_name": "QUESNEL",
    "vips_policedetachments_agency_id": "433",
    "vips_policedetachments_agency_nm": "BCHP - Quesnel"
  },
  {
    "agency_name": "BCHP Revelstoke",
    "agency_id": "2100",
    "agency_city": "Revelstoke",
    "prime_vjur": "2100",
    "icbc_detachment_name": "SOUTHEAST DISTRICT RCMP",
    "icbc_city_name": "REVELSTOKE",
    "vips_policedetachments_agency_id": "240",
    "vips_policedetachments_agency_nm": "IRSU-E TCH (Golden/Revelstoke)"
  },
  {
    "agency_name": "BCHP Smithers",
    "agency_id": "3305",
    "agency_city": "Smithers",
    "prime_vjur": "3305",
    "icbc_detachment_name": "ALEXIS CREEK RCMP",
    "icbc_city_name": "SMITHERS",
    "vips_policedetachments_agency_id": "42",
    "vips_policedetachments_agency_nm": "Alexis Creek"
  },
  {
    "agency_name": "BCHP Squamish",
    "agency_id": "1104",
    "agency_city": "Squamish",
    "prime_vjur": "1104",
    "icbc_detachment_name": "SQUAMISH RCMP",
    "icbc_city_name": "SQUAMISH",
    "vips_policedetachments_agency_id": "158",
    "vips_policedetachments_agency_nm": "Squamish"
  },
  {
    "agency_name": "BCHP Terrace",
    "agency_id": "3501",
    "agency_city": "Terrace",
    "prime_vjur": "3501",
    "icbc_detachment_name": "TERRACE RCMP",
    "icbc_city_name": "TERRACE",
    "vips_policedetachments_agency_id": "131",
    "vips_policedetachments_agency_nm": "Terrace"
  },
  {
    "agency_name": "BCHP Vanderhoof",
    "agency_id": "3201",
    "agency_city": "Vanderhoof",
    "prime_vjur": "3201",
    "icbc_detachment_name": "VANDERHOOF RCMP",
    "icbc_city_name": "VANDERHOOF",
    "vips_policedetachments_agency_id": "113",
    "vips_policedetachments_agency_nm": "Vanderhoof/ TS"
  },
  {
    "agency_name": "BCHP Williams Lake",
    "agency_id": "3304",
    "agency_city": "Williams Lake",
    "prime_vjur": "3304",
    "icbc_detachment_name": "WILLIAMS LAKE RCMP",
    "icbc_city_name": "WILLIAMS LAKE",
    "vips_policedetachments_agency_id": "58",
    "vips_policedetachments_agency_nm": "Williams Lake/ TS"
  },
  {
    "agency_name": "Central Saanich Police Svc.",
    "agency_id": "CS",
    "agency_city": "Central Saanich",
    "prime_vjur": "CS",
    "icbc_detachment_name": "CENTRAL SAANICH POLICE SERVICE",
    "icbc_city_name": "CENTRAL SAANICH",
    "vips_policedetachments_agency_id": "89",
    "vips_policedetachments_agency_nm": "Central Saanich"
  },
  {
    "agency_name": "Delta Police Dept.",
    "agency_id": "DE",
    "agency_city": "Delta",
    "prime_vjur": "DE",
    "icbc_detachment_name": "DELTA POLICE DEPARTMENT",
    "icbc_city_name": "DELTA",
    "vips_policedetachments_agency_id": "91",
    "vips_policedetachments_agency_nm": "Delta"
  },
  {
    "agency_name": "Metro Vancouver Transit Police",
    "agency_id": "GV",
    "agency_city": "New Westminster",
    "prime_vjur": "GV",
    "icbc_detachment_name": "SCBCTAPS - TRANSIT POLICE",
    "icbc_city_name": "NEW WESTMINSTER",
    "vips_policedetachments_agency_id": "251",
    "vips_policedetachments_agency_nm": "Metro Vancouver Transit Police"
  },
  {
    "agency_name": "Nelson Police Dept.",
    "agency_id": "NP",
    "agency_city": "Nelson",
    "prime_vjur": "NP",
    "icbc_detachment_name": "NELSON POLICE DEPARTMENT",
    "icbc_city_name": "NELSON",
    "vips_policedetachments_agency_id": "95",
    "vips_policedetachments_agency_nm": "Nelson City Police"
  },
  {
    "agency_name": "New Westminster Police Dept.",
    "agency_id": "NW",
    "agency_city": "New Westminster",
    "prime_vjur": "NW",
    "icbc_detachment_name": "NEW WESTMINSTER POLICE DEPT",
    "icbc_city_name": "NEW WESTMINSTER",
    "vips_policedetachments_agency_id": "93",
    "vips_policedetachments_agency_nm": "New Westminster"
  },
  {
    "agency_name": "Oak Bay Police Dept.",
    "agency_id": "OB",
    "agency_city": "Oak Bay",
    "prime_vjur": "OB",
    "icbc_detachment_name": "OAK BAY POLICE DEPARTMENT",
    "icbc_city_name": "OAK BAY",
    "vips_policedetachments_agency_id": "40",
    "vips_policedetachments_agency_nm": "Oak Bay"
  },
  {
    "agency_name": "Port Moody Police Dept.",
    "agency_id": "PO",
    "agency_city": "Port Moody",
    "prime_vjur": "PO",
    "icbc_detachment_name": "PORT MOODY POLICE DEPARTMENT",
    "icbc_city_name": "PORT MOODY",
    "vips_policedetachments_agency_id": "96",
    "vips_policedetachments_agency_nm": "Port Moody"
  },
  {
    "agency_name": "RCMP 100 Mile House",
    "agency_id": "3303",
    "agency_city": "100 Mile House",
    "prime_vjur": "3303",
    "icbc_detachment_name": "100 MILE HOUSE RCMP",
    "icbc_city_name": "100 MILE HOUSE",
    "vips_policedetachments_agency_id": "56",
    "vips_policedetachments_agency_nm": "100 Mile House/TS"
  },
  {
    "agency_name": "RCMP Agassiz",
    "agency_id": "1501",
    "agency_city": "Agassiz",
    "prime_vjur": "1501",
    "icbc_detachment_name": "UPPER FRASER VALLEY REG RCMP",
    "icbc_city_name": "AGASSIZ",
    "vips_policedetachments_agency_id": "138",
    "vips_policedetachments_agency_nm": "Agassiz"
  },
  {
    "agency_name": "RCMP Ahousaht",
    "agency_id": "4304",
    "agency_city": "Ahousaht",
    "prime_vjur": "4304",
    "icbc_detachment_name": "TOFINO RCMP (AHOUSAHT)",
    "icbc_city_name": "AHOUSAHT",
    "vips_policedetachments_agency_id": "203",
    "vips_policedetachments_agency_nm": "Tofino"
  },
  {
    "agency_name": "RCMP Alert Bay",
    "agency_id": "4322",
    "agency_city": "Alert Bay",
    "prime_vjur": "4322",
    "icbc_detachment_name": "ALERT BAY RCMP",
    "icbc_city_name": "ALERT BAY",
    "vips_policedetachments_agency_id": "185",
    "vips_policedetachments_agency_nm": "Alert Bay"
  },
  {
    "agency_name": "RCMP Alexis Creek",
    "agency_id": "3305",
    "agency_city": "Alexis Creek",
    "prime_vjur": "3305",
    "icbc_detachment_name": "ALEXIS CREEK RCMP",
    "icbc_city_name": "ALEXIS CREEK",
    "vips_policedetachments_agency_id": "42",
    "vips_policedetachments_agency_nm": "Alexis Creek"
  },
  {
    "agency_name": "RCMP Anahim Lake",
    "agency_id": "3306",
    "agency_city": "Anahim Lake",
    "prime_vjur": "3306",
    "icbc_detachment_name": "ANAHIM LAKE RCMP",
    "icbc_city_name": "ANAHIM LAKE",
    "vips_policedetachments_agency_id": "43",
    "vips_policedetachments_agency_nm": "Anahim Lake"
  },
  {
    "agency_name": "RCMP Armstrong",
    "agency_id": "2111",
    "agency_city": "Armstrong",
    "prime_vjur": "2111",
    "icbc_detachment_name": "NORTH OKANAGAN RCMP",
    "icbc_city_name": "ARMSTRONG",
    "vips_policedetachments_agency_id": "19",
    "vips_policedetachments_agency_nm": "Armstrong"
  },
  {
    "agency_name": "RCMP Ashcroft",
    "agency_id": "2208",
    "agency_city": "Ashcroft",
    "prime_vjur": "2208",
    "icbc_detachment_name": "ASHCROFT RCMP",
    "icbc_city_name": "ASHCROFT",
    "vips_policedetachments_agency_id": "44",
    "vips_policedetachments_agency_nm": "Ashcroft"
  },
  {
    "agency_name": "RCMP Atlin",
    "agency_id": "3608",
    "agency_city": "Atlin",
    "prime_vjur": "3608",
    "icbc_detachment_name": "ATLIN RCMP",
    "icbc_city_name": "ATLIN",
    "vips_policedetachments_agency_id": "118",
    "vips_policedetachments_agency_nm": "Atlin"
  },
  {
    "agency_name": "RCMP Barriere",
    "agency_id": "2204",
    "agency_city": "Barriere",
    "prime_vjur": "2204",
    "icbc_detachment_name": "BARRIERE RCMP",
    "icbc_city_name": "BARRIERE",
    "vips_policedetachments_agency_id": "45",
    "vips_policedetachments_agency_nm": "Barriere"
  },
  {
    "agency_name": "RCMP Bella Bella",
    "agency_id": "3308",
    "agency_city": "Bella Bella",
    "prime_vjur": "3308",
    "icbc_detachment_name": "BELLA BELLA RCMP",
    "icbc_city_name": "BELLA BELLA",
    "vips_policedetachments_agency_id": "134",
    "vips_policedetachments_agency_nm": "Bella Bella"
  },
  {
    "agency_name": "RCMP Bella Coola",
    "agency_id": "3307",
    "agency_city": "Bella Coola",
    "prime_vjur": "3307",
    "icbc_detachment_name": "BELLA COOLA RCMP",
    "icbc_city_name": "BELLA COOLA",
    "vips_policedetachments_agency_id": "119",
    "vips_policedetachments_agency_nm": "Bella Coola"
  },
  {
    "agency_name": "RCMP Boston Bar",
    "agency_id": "1501",
    "agency_city": "Boston Bar",
    "prime_vjur": "1501",
    "icbc_detachment_name": "UPPER FRASER VALLEY REG RCMP",
    "icbc_city_name": "BOSTON BAR",
    "vips_policedetachments_agency_id": "140",
    "vips_policedetachments_agency_nm": "Boston Bar"
  },
  {
    "agency_name": "RCMP Bowen Island",
    "agency_id": "1103",
    "agency_city": "Bowen Island",
    "prime_vjur": "1103",
    "icbc_detachment_name": "BOWEN ISLAND RCMP",
    "icbc_city_name": "BOWEN ISLAND",
    "vips_policedetachments_agency_id": "167",
    "vips_policedetachments_agency_nm": "Bowen Island"
  },
  {
    "agency_name": "RCMP Burnaby",
    "agency_id": "1202",
    "agency_city": "Burnaby",
    "prime_vjur": "1202",
    "icbc_detachment_name": "BURNABY RCMP",
    "icbc_city_name": "BURNABY",
    "vips_policedetachments_agency_id": "139",
    "vips_policedetachments_agency_nm": "Burnaby"
  },
  {
    "agency_name": "RCMP Burns Lake",
    "agency_id": "3205",
    "agency_city": "Burns Lake",
    "prime_vjur": "3205",
    "icbc_detachment_name": "BURNS LAKE RCMP",
    "icbc_city_name": "BURNS LAKE",
    "vips_policedetachments_agency_id": "98",
    "vips_policedetachments_agency_nm": "Burns Lake"
  },
  {
    "agency_name": "RCMP Campbell River",
    "agency_id": "4315",
    "agency_city": "Campbell River",
    "prime_vjur": "4315",
    "icbc_detachment_name": "CAMPBELL RIVER RCMP",
    "icbc_city_name": "CAMPBELL RIVER",
    "vips_policedetachments_agency_id": "186",
    "vips_policedetachments_agency_nm": "Campbell River"
  },
  {
    "agency_name": "RCMP Castlegar",
    "agency_id": "2303",
    "agency_city": "Castlegar",
    "prime_vjur": "2303",
    "icbc_detachment_name": "CASTLEGAR RCMP",
    "icbc_city_name": "CASTLEGAR",
    "vips_policedetachments_agency_id": "59",
    "vips_policedetachments_agency_nm": "Castlegar"
  },
  {
    "agency_name": "RCMP Chase",
    "agency_id": "2203",
    "agency_city": "Chase",
    "prime_vjur": "2203",
    "icbc_detachment_name": "CHASE RCMP",
    "icbc_city_name": "CHASE",
    "vips_policedetachments_agency_id": "46",
    "vips_policedetachments_agency_nm": "Chase"
  },
  {
    "agency_name": "RCMP Chetwynd",
    "agency_id": "3405",
    "agency_city": "Chetwynd",
    "prime_vjur": "3405",
    "icbc_detachment_name": "CHETWYND RCMP",
    "icbc_city_name": "CHETWYND",
    "vips_policedetachments_agency_id": "99",
    "vips_policedetachments_agency_nm": "Chetwynd"
  },
  {
    "agency_name": "RCMP Chilliwack",
    "agency_id": "1501",
    "agency_city": "Chilliwack",
    "prime_vjur": "1501",
    "icbc_detachment_name": "UPPER FRASER VALLEY REG RCMP",
    "icbc_city_name": "CHILLIWACK",
    "vips_policedetachments_agency_id": "141",
    "vips_policedetachments_agency_nm": "Chilliwack"
  },
  {
    "agency_name": "RCMP Clearwater",
    "agency_id": "2205",
    "agency_city": "Clearwater",
    "prime_vjur": "2205",
    "icbc_detachment_name": "CLEARWATER RCMP",
    "icbc_city_name": "CLEARWATER",
    "vips_policedetachments_agency_id": "47",
    "vips_policedetachments_agency_nm": "Clearwater"
  },
  {
    "agency_name": "RCMP Clinton",
    "agency_id": "2211",
    "agency_city": "Clinton",
    "prime_vjur": "2211",
    "icbc_detachment_name": "CLINTON RCMP",
    "icbc_city_name": "CLINTON",
    "vips_policedetachments_agency_id": "48",
    "vips_policedetachments_agency_nm": "Clinton"
  },
  {
    "agency_name": "RCMP Columbia Valley",
    "agency_id": "2405",
    "agency_city": "Invermere",
    "prime_vjur": "2405",
    "icbc_detachment_name": "COLUMBIA VALLEY RCMP",
    "icbc_city_name": "INVERMERE",
    "vips_policedetachments_agency_id": "68",
    "vips_policedetachments_agency_nm": "Invermere"
  },
  {
    "agency_name": "RCMP Comox Valley",
    "agency_id": "4301",
    "agency_city": "Comox Valley",
    "prime_vjur": "4301",
    "icbc_detachment_name": "COMOX VALLEY RCMP",
    "icbc_city_name": "COMOX VALLEY",
    "vips_policedetachments_agency_id": "188",
    "vips_policedetachments_agency_nm": "Comox"
  },
  {
    "agency_name": "RCMP Coquitlam",
    "agency_id": "1203",
    "agency_city": "Coquitlam",
    "prime_vjur": "1203",
    "icbc_detachment_name": "COQUITLAM RCMP",
    "icbc_city_name": "COQUITLAM",
    "vips_policedetachments_agency_id": "143",
    "vips_policedetachments_agency_nm": "Coquitlam"
  },
  {
    "agency_name": "RCMP Cranbrook",
    "agency_id": "2401",
    "agency_city": "Cranbrook",
    "prime_vjur": "2401",
    "icbc_detachment_name": "CRANBROOK/KIMBERLEY RCMP",
    "icbc_city_name": "CRANBROOK",
    "vips_policedetachments_agency_id": "60",
    "vips_policedetachments_agency_nm": "Cranbrook"
  },
  {
    "agency_name": "RCMP Creston",
    "agency_id": "2404",
    "agency_city": "Creston",
    "prime_vjur": "2404",
    "icbc_detachment_name": "CRESTON RCMP",
    "icbc_city_name": "CRESTON",
    "vips_policedetachments_agency_id": "62",
    "vips_policedetachments_agency_nm": "Creston"
  },
  {
    "agency_name": "RCMP Daajing Giids",
    "agency_id": "3607",
    "agency_city": "Daajing Giids",
    "prime_vjur": "3607",
    "icbc_detachment_name": "DAAJING GIIDS RCMP",
    "icbc_city_name": "DAAJING GIIDS",
    "vips_policedetachments_agency_id": "127",
    "vips_policedetachments_agency_nm": "Queen Charlotte City"
  },
  {
    "agency_name": "RCMP Dawson Creek",
    "agency_id": "3403",
    "agency_city": "Dawson Creek",
    "prime_vjur": "3403",
    "icbc_detachment_name": "DAWSON CREEK RCMP",
    "icbc_city_name": "DAWSON CREEK",
    "vips_policedetachments_agency_id": "100",
    "vips_policedetachments_agency_nm": "Dawson Creek/ TS"
  },
  {
    "agency_name": "RCMP Dease Lake",
    "agency_id": "3604",
    "agency_city": "Dease Lake",
    "prime_vjur": "3604",
    "icbc_detachment_name": "DEASE LAKE RCMP",
    "icbc_city_name": "DEASE LAKE",
    "vips_policedetachments_agency_id": "130",
    "vips_policedetachments_agency_nm": "Dease Lake"
  },
  {
    "agency_name": "RCMP Elkford",
    "agency_id": "2403",
    "agency_city": "Elkford",
    "prime_vjur": "2403",
    "icbc_detachment_name": "ELK VALLEY RCMP",
    "icbc_city_name": "ELKFORD",
    "vips_policedetachments_agency_id": "84",
    "vips_policedetachments_agency_nm": "Elkford"
  },
  {
    "agency_name": "RCMP Enderby",
    "agency_id": "2111",
    "agency_city": "Enderby",
    "prime_vjur": "2111",
    "icbc_detachment_name": "NORTH OKANAGAN RCMP",
    "icbc_city_name": "ENDERBY",
    "vips_policedetachments_agency_id": "20",
    "vips_policedetachments_agency_nm": "Enderby"
  },
  {
    "agency_name": "RCMP Fernie",
    "agency_id": "2403",
    "agency_city": "Fernie",
    "prime_vjur": "2403",
    "icbc_detachment_name": "ELK VALLEY RCMP",
    "icbc_city_name": "FERNIE",
    "vips_policedetachments_agency_id": "63",
    "vips_policedetachments_agency_nm": "Fernie"
  },
  {
    "agency_name": "RCMP Fort Nelson",
    "agency_id": "3402",
    "agency_city": "Fort Nelson",
    "prime_vjur": "3402",
    "icbc_detachment_name": "NORTHERN ROCKIES RCMP",
    "icbc_city_name": "FORT NELSON",
    "vips_policedetachments_agency_id": "102",
    "vips_policedetachments_agency_nm": "Fort Nelson"
  },
  {
    "agency_name": "RCMP Fort St. James",
    "agency_id": "3202",
    "agency_city": "Fort St. James",
    "prime_vjur": "3202",
    "icbc_detachment_name": "FORT ST. JAMES RCMP",
    "icbc_city_name": "FORT ST. JAMES",
    "vips_policedetachments_agency_id": "103",
    "vips_policedetachments_agency_nm": "Fort St. James"
  },
  {
    "agency_name": "RCMP Fort St. John",
    "agency_id": "3401",
    "agency_city": "Fort St. John",
    "prime_vjur": "3401",
    "icbc_detachment_name": "FORT ST. JOHN RCMP",
    "icbc_city_name": "FORT ST. JOHN",
    "vips_policedetachments_agency_id": "104",
    "vips_policedetachments_agency_nm": "Fort St. John/ TS"
  },
  {
    "agency_name": "RCMP Fraser Lake",
    "agency_id": "3204",
    "agency_city": "Fraser Lake",
    "prime_vjur": "3204",
    "icbc_detachment_name": "FRASER LAKE RCMP",
    "icbc_city_name": "FRASER LAKE",
    "vips_policedetachments_agency_id": "106",
    "vips_policedetachments_agency_nm": "Fraser Lake"
  },
  {
    "agency_name": "RCMP Gabriola",
    "agency_id": "4202",
    "agency_city": "Gabriola Island",
    "prime_vjur": "4202",
    "icbc_detachment_name": "GABRIOLA ISLAND RCMP",
    "icbc_city_name": "GABRIOLA ISLAND",
    "vips_policedetachments_agency_id": "173",
    "vips_policedetachments_agency_nm": "Gabriola Island"
  },
  {
    "agency_name": "RCMP Gibsons",
    "agency_id": "1106",
    "agency_city": "Gibsons",
    "prime_vjur": "1106",
    "icbc_detachment_name": "SUNSHINE COAST RCMP",
    "icbc_city_name": "GIBSONS",
    "vips_policedetachments_agency_id": "149",
    "vips_policedetachments_agency_nm": "Gibsons"
  },
  {
    "agency_name": "RCMP Golden/Field",
    "agency_id": "2406",
    "agency_city": "Golden",
    "prime_vjur": "2406",
    "icbc_detachment_name": "GOLDEN RCMP",
    "icbc_city_name": "GOLDEN",
    "vips_policedetachments_agency_id": "66",
    "vips_policedetachments_agency_nm": "Golden/ TS"
  },
  {
    "agency_name": "RCMP Grand Forks",
    "agency_id": "2305",
    "agency_city": "Grand Forks",
    "prime_vjur": "2305",
    "icbc_detachment_name": "BOUNDARY RCMP",
    "icbc_city_name": "GRAND FORKS",
    "vips_policedetachments_agency_id": "67",
    "vips_policedetachments_agency_nm": "Grand Forks"
  },
  {
    "agency_name": "RCMP Granisle",
    "agency_id": "3503",
    "agency_city": "Granisle",
    "prime_vjur": "3503",
    "icbc_detachment_name": "HOUSTON RCMP",
    "icbc_city_name": "GRANISLE",
    "vips_policedetachments_agency_id": "133",
    "vips_policedetachments_agency_nm": "Granisle"
  },
  {
    "agency_name": "RCMP Hope",
    "agency_id": "1501",
    "agency_city": "Hope",
    "prime_vjur": "1501",
    "icbc_detachment_name": "UPPER FRASER VALLEY REG RCMP",
    "icbc_city_name": "HOPE",
    "vips_policedetachments_agency_id": "148",
    "vips_policedetachments_agency_nm": "Hope"
  },
  {
    "agency_name": "RCMP Houston",
    "agency_id": "3503",
    "agency_city": "Houston",
    "prime_vjur": "3503",
    "icbc_detachment_name": "HOUSTON RCMP",
    "icbc_city_name": "HOUSTON",
    "vips_policedetachments_agency_id": "121",
    "vips_policedetachments_agency_nm": "Houston"
  },
  {
    "agency_name": "RCMP Hudson's Hope",
    "agency_id": "3406",
    "agency_city": "Hudson's Hope",
    "prime_vjur": "3406",
    "icbc_detachment_name": "HUDSON'S HOPE RCMP",
    "icbc_city_name": "HUDSON'S HOPE",
    "vips_policedetachments_agency_id": "107",
    "vips_policedetachments_agency_nm": "Hudson's Hope"
  },
  {
    "agency_name": "RCMP Kamloops",
    "agency_id": "2201",
    "agency_city": "Kamloops",
    "prime_vjur": "2201",
    "icbc_detachment_name": "KAMLOOPS CITY RCMP",
    "icbc_city_name": "KAMLOOPS",
    "vips_policedetachments_agency_id": "50",
    "vips_policedetachments_agency_nm": "Kamloops (M)"
  },
  {
    "agency_name": "RCMP Kaslo",
    "agency_id": "2301",
    "agency_city": "Kaslo",
    "prime_vjur": "2301",
    "icbc_detachment_name": "CENTRAL KOOTENAY RCMP",
    "icbc_city_name": "KASLO",
    "vips_policedetachments_agency_id": "70",
    "vips_policedetachments_agency_nm": "Kaslo"
  },
  {
    "agency_name": "RCMP Kelowna",
    "agency_id": "2101",
    "agency_city": "Kelowna",
    "prime_vjur": "2101",
    "icbc_detachment_name": "KELOWNA RCMP",
    "icbc_city_name": "KELOWNA",
    "vips_policedetachments_agency_id": "22",
    "vips_policedetachments_agency_nm": "Kelowna"
  },
  {
    "agency_name": "RCMP Keremeos",
    "agency_id": "2105",
    "agency_city": "Keremeos",
    "prime_vjur": "2105",
    "icbc_detachment_name": "KEREMEOS RCMP",
    "icbc_city_name": "KEREMEOS",
    "vips_policedetachments_agency_id": "24",
    "vips_policedetachments_agency_nm": "Keremeos"
  },
  {
    "agency_name": "RCMP Kimberley",
    "agency_id": "2401",
    "agency_city": "Kimberley",
    "prime_vjur": "2401",
    "icbc_detachment_name": "CRANBROOK/KIMBERLEY RCMP",
    "icbc_city_name": "KIMBERLEY",
    "vips_policedetachments_agency_id": "71",
    "vips_policedetachments_agency_nm": "Kimberley"
  },
  {
    "agency_name": "RCMP Kitimat",
    "agency_id": "3502",
    "agency_city": "Kitimat",
    "prime_vjur": "3502",
    "icbc_detachment_name": "KITIMAT RCMP",
    "icbc_city_name": "KITIMAT",
    "vips_policedetachments_agency_id": "122",
    "vips_policedetachments_agency_nm": "Kitimat"
  },
  {
    "agency_name": "RCMP Ladysmith",
    "agency_id": "4203",
    "agency_city": "Ladysmith",
    "prime_vjur": "4203",
    "icbc_detachment_name": "LADYSMITH RCMP",
    "icbc_city_name": "LADYSMITH",
    "vips_policedetachments_agency_id": "175",
    "vips_policedetachments_agency_nm": "Ladysmith"
  },
  {
    "agency_name": "RCMP Lake Country",
    "agency_id": "2101",
    "agency_city": "Lake Country",
    "prime_vjur": "2101",
    "icbc_detachment_name": "KELOWNA RCMP",
    "icbc_city_name": "LAKE COUNTRY",
    "vips_policedetachments_agency_id": "210",
    "vips_policedetachments_agency_nm": "Lake Country"
  },
  {
    "agency_name": "RCMP Lake Cowichan",
    "agency_id": "4208",
    "agency_city": "Lake Cowichan",
    "prime_vjur": "4208",
    "icbc_detachment_name": "LAKE COWICHAN RCMP",
    "icbc_city_name": "LAKE COWICHAN",
    "vips_policedetachments_agency_id": "176",
    "vips_policedetachments_agency_nm": "Lake Cowichan"
  },
  {
    "agency_name": "RCMP Langley",
    "agency_id": "1303",
    "agency_city": "Langley",
    "prime_vjur": "1303",
    "icbc_detachment_name": "LANGLEY RCMP",
    "icbc_city_name": "LANGLEY",
    "vips_policedetachments_agency_id": "151",
    "vips_policedetachments_agency_nm": "Langley District"
  },
  {
    "agency_name": "RCMP Lillooet",
    "agency_id": "2209",
    "agency_city": "Lillooet",
    "prime_vjur": "2209",
    "icbc_detachment_name": "LILLOOET RCMP",
    "icbc_city_name": "LILLOOET",
    "vips_policedetachments_agency_id": "51",
    "vips_policedetachments_agency_nm": "Lillooet"
  },
  {
    "agency_name": "RCMP Lisims/Nass Valley",
    "agency_id": "3602",
    "agency_city": "New Aiyansh",
    "prime_vjur": "3602",
    "icbc_detachment_name": "LISIMS/NASS VALLEY RCMP",
    "icbc_city_name": "NEW AIYANSH",
    "vips_policedetachments_agency_id": "135",
    "vips_policedetachments_agency_nm": "Nass Valley/Lisims"
  },
  {
    "agency_name": "RCMP Logan Lake",
    "agency_id": "2206",
    "agency_city": "Logan Lake",
    "prime_vjur": "2206",
    "icbc_detachment_name": "LOGAN LAKE RCMP",
    "icbc_city_name": "LOGAN LAKE",
    "vips_policedetachments_agency_id": "52",
    "vips_policedetachments_agency_nm": "Logan Lake"
  },
  {
    "agency_name": "RCMP Lumby",
    "agency_id": "2111",
    "agency_city": "Lumby",
    "prime_vjur": "2111",
    "icbc_detachment_name": "NORTH OKANAGAN RCMP",
    "icbc_city_name": "LUMBY",
    "vips_policedetachments_agency_id": "25",
    "vips_policedetachments_agency_nm": "Lumby"
  },
  {
    "agency_name": "RCMP Lytton",
    "agency_id": "2210",
    "agency_city": "Lytton",
    "prime_vjur": "2210",
    "icbc_detachment_name": "LYTTON RCMP",
    "icbc_city_name": "LYTTON",
    "vips_policedetachments_agency_id": "53",
    "vips_policedetachments_agency_nm": "Lytton"
  },
  {
    "agency_name": "RCMP Mackenzie",
    "agency_id": "3104",
    "agency_city": "Mackenzie",
    "prime_vjur": "3104",
    "icbc_detachment_name": "MACKENZIE RCMP",
    "icbc_city_name": "MACKENZIE",
    "vips_policedetachments_agency_id": "108",
    "vips_policedetachments_agency_nm": "MacKenzie"
  },
  {
    "agency_name": "RCMP Masset",
    "agency_id": "3606",
    "agency_city": "Masset",
    "prime_vjur": "3606",
    "icbc_detachment_name": "MASSET RCMP",
    "icbc_city_name": "MASSET",
    "vips_policedetachments_agency_id": "124",
    "vips_policedetachments_agency_nm": "Masset"
  },
  {
    "agency_name": "RCMP McBride",
    "agency_id": "3102",
    "agency_city": "McBride",
    "prime_vjur": "3102",
    "icbc_detachment_name": "MCBRIDE RCMP",
    "icbc_city_name": "MCBRIDE",
    "vips_policedetachments_agency_id": "109",
    "vips_policedetachments_agency_nm": "McBride"
  },
  {
    "agency_name": "RCMP Merritt",
    "agency_id": "2207",
    "agency_city": "Merritt",
    "prime_vjur": "2207",
    "icbc_detachment_name": "MERRITT RCMP",
    "icbc_city_name": "MERRITT",
    "vips_policedetachments_agency_id": "54",
    "vips_policedetachments_agency_nm": "Merritt"
  },
  {
    "agency_name": "RCMP Midway",
    "agency_id": "2305",
    "agency_city": "Midway",
    "prime_vjur": "2305",
    "icbc_detachment_name": "BOUNDARY RCMP",
    "icbc_city_name": "MIDWAY",
    "vips_policedetachments_agency_id": "73",
    "vips_policedetachments_agency_nm": "Midway"
  },
  {
    "agency_name": "RCMP Mission",
    "agency_id": "1503",
    "agency_city": "Mission",
    "prime_vjur": "1503",
    "icbc_detachment_name": "MISSION RCMP",
    "icbc_city_name": "MISSION",
    "vips_policedetachments_agency_id": "152",
    "vips_policedetachments_agency_nm": "Mission"
  },
  {
    "agency_name": "RCMP Nakusp",
    "agency_id": "2301",
    "agency_city": "Nakusp",
    "prime_vjur": "2301",
    "icbc_detachment_name": "CENTRAL KOOTENAY RCMP",
    "icbc_city_name": "NAKUSP",
    "vips_policedetachments_agency_id": "74",
    "vips_policedetachments_agency_nm": "Nakusp"
  },
  {
    "agency_name": "RCMP Nanaimo",
    "agency_id": "4201",
    "agency_city": "Nanaimo",
    "prime_vjur": "4201",
    "icbc_detachment_name": "NANAIMO RCMP",
    "icbc_city_name": "NANAIMO",
    "vips_policedetachments_agency_id": "177",
    "vips_policedetachments_agency_nm": "Nanaimo"
  },
  {
    "agency_name": "RCMP Nelson",
    "agency_id": "2301",
    "agency_city": "Nelson",
    "prime_vjur": "2301",
    "icbc_detachment_name": "CENTRAL KOOTENAY RCMP",
    "icbc_city_name": "NELSON",
    "vips_policedetachments_agency_id": "41",
    "vips_policedetachments_agency_nm": "Nelson RCMP"
  },
  {
    "agency_name": "RCMP New Hazelton",
    "agency_id": "3506",
    "agency_city": "New Hazelton",
    "prime_vjur": "3506",
    "icbc_detachment_name": "NEW HAZELTON RCMP",
    "icbc_city_name": "NEW HAZELTON",
    "vips_policedetachments_agency_id": "120",
    "vips_policedetachments_agency_nm": "New Hazelton"
  },
  {
    "agency_name": "RCMP Nootka Sound",
    "agency_id": "4317",
    "agency_city": "Nootka Sound",
    "prime_vjur": "4317",
    "icbc_detachment_name": "NOOTKA SOUND RCMP",
    "icbc_city_name": "NOOTKA SOUND",
    "vips_policedetachments_agency_id": "191",
    "vips_policedetachments_agency_nm": "Gold River"
  },
  {
    "agency_name": "RCMP North Cowichan/Duncan",
    "agency_id": "4204",
    "agency_city": "Duncan",
    "prime_vjur": "4204",
    "icbc_detachment_name": "NORTH COWICHAN/DUNCAN RCMP",
    "icbc_city_name": "DUNCAN",
    "vips_policedetachments_agency_id": "171",
    "vips_policedetachments_agency_nm": "Duncan"
  },
  {
    "agency_name": "RCMP North Vancouver",
    "agency_id": "1101",
    "agency_city": "North Vancouver",
    "prime_vjur": "1101",
    "icbc_detachment_name": "NORTH VANCOUVER RCMP",
    "icbc_city_name": "NORTH VANCOUVER",
    "vips_policedetachments_agency_id": "154",
    "vips_policedetachments_agency_nm": "North Vancouver City"
  },
  {
    "agency_name": "RCMP Oceanside",
    "agency_id": "4302",
    "agency_city": "Parksville",
    "prime_vjur": "4302",
    "icbc_detachment_name": "OCEANSIDE RCMP",
    "icbc_city_name": "PARKSVILLE",
    "vips_policedetachments_agency_id": "192",
    "vips_policedetachments_agency_nm": "Parksville (OCEANSIDE)"
  },
  {
    "agency_name": "RCMP Oliver",
    "agency_id": "2104",
    "agency_city": "Oliver",
    "prime_vjur": "2104",
    "icbc_detachment_name": "SOUTH OKANAGAN RCMP",
    "icbc_city_name": "OLIVER",
    "vips_policedetachments_agency_id": "26",
    "vips_policedetachments_agency_nm": "Oliver"
  },
  {
    "agency_name": "RCMP Osoyoos",
    "agency_id": "2104",
    "agency_city": "Osoyoos",
    "prime_vjur": "2104",
    "icbc_detachment_name": "SOUTH OKANAGAN RCMP",
    "icbc_city_name": "OSOYOOS",
    "vips_policedetachments_agency_id": "27",
    "vips_policedetachments_agency_nm": "Osoyoos"
  },
  {
    "agency_name": "RCMP Outer Gulf Islands",
    "agency_id": "4109",
    "agency_city": "Pender Island",
    "prime_vjur": "4109",
    "icbc_detachment_name": "OUTER GULF ISLANDS RCMP",
    "icbc_city_name": "PENDER ISLAND",
    "vips_policedetachments_agency_id": "179",
    "vips_policedetachments_agency_nm": "Pender Island"
  },
  {
    "agency_name": "RCMP Peachland",
    "agency_id": "2101",
    "agency_city": "Peachland",
    "prime_vjur": "2101",
    "icbc_detachment_name": "KELOWNA RCMP",
    "icbc_city_name": "PEACHLAND",
    "vips_policedetachments_agency_id": "22",
    "vips_policedetachments_agency_nm": "Kelowna"
  },
  {
    "agency_name": "RCMP Pemberton",
    "agency_id": "1105",
    "agency_city": "Pemberton",
    "prime_vjur": "1105",
    "icbc_detachment_name": "WHISTLER/PEMBERTON RCMP",
    "icbc_city_name": "PEMBERTON",
    "vips_policedetachments_agency_id": "163",
    "vips_policedetachments_agency_nm": "Pemberton"
  },
  {
    "agency_name": "RCMP Penticton",
    "agency_id": "2102",
    "agency_city": "Penticton",
    "prime_vjur": "2102",
    "icbc_detachment_name": "PENTICTON RCMP",
    "icbc_city_name": "PENTICTON",
    "vips_policedetachments_agency_id": "28",
    "vips_policedetachments_agency_nm": "Penticton"
  },
  {
    "agency_name": "RCMP Port Alberni",
    "agency_id": "4303",
    "agency_city": "Port Alberni",
    "prime_vjur": "4303",
    "icbc_detachment_name": "PORT ALBERNI RCMP",
    "icbc_city_name": "PORT ALBERNI",
    "vips_policedetachments_agency_id": "193",
    "vips_policedetachments_agency_nm": "Port Alberni"
  },
  {
    "agency_name": "RCMP Port Alice",
    "agency_id": "4321",
    "agency_city": "Port Alice",
    "prime_vjur": "4321",
    "icbc_detachment_name": "PORT ALICE RCMP",
    "icbc_city_name": "PORT ALICE",
    "vips_policedetachments_agency_id": "195",
    "vips_policedetachments_agency_nm": "Port Alice"
  },
  {
    "agency_name": "RCMP Port Hardy",
    "agency_id": "4319",
    "agency_city": "Port Hardy",
    "prime_vjur": "4319",
    "icbc_detachment_name": "PORT HARDY RCMP",
    "icbc_city_name": "PORT HARDY",
    "vips_policedetachments_agency_id": "196",
    "vips_policedetachments_agency_nm": "Port Hardy"
  },
  {
    "agency_name": "RCMP Port McNeill",
    "agency_id": "4320",
    "agency_city": "Port McNeill",
    "prime_vjur": "4320",
    "icbc_detachment_name": "PORT MCNEILL RCMP",
    "icbc_city_name": "PORT MCNEILL",
    "vips_policedetachments_agency_id": "197",
    "vips_policedetachments_agency_nm": "Port McNeill"
  },
  {
    "agency_name": "RCMP Powell River",
    "agency_id": "4306",
    "agency_city": "Powell River",
    "prime_vjur": "4306",
    "icbc_detachment_name": "POWELL RIVER RCMP",
    "icbc_city_name": "POWELL RIVER",
    "vips_policedetachments_agency_id": "198",
    "vips_policedetachments_agency_nm": "Powell River"
  },
  {
    "agency_name": "RCMP Prince George",
    "agency_id": "3101",
    "agency_city": "Prince George",
    "prime_vjur": "3101",
    "icbc_detachment_name": "PRINCE GEORGE RCMP",
    "icbc_city_name": "PRINCE GEORGE",
    "vips_policedetachments_agency_id": "115",
    "vips_policedetachments_agency_nm": "Prince George (M)"
  },
  {
    "agency_name": "RCMP Prince Rupert",
    "agency_id": "3601",
    "agency_city": "Prince Rupert",
    "prime_vjur": "3601",
    "icbc_detachment_name": "PRINCE RUPERT RCMP",
    "icbc_city_name": "PRINCE RUPERT",
    "vips_policedetachments_agency_id": "126",
    "vips_policedetachments_agency_nm": "Prince Rupert (M)"
  },
  {
    "agency_name": "RCMP Princeton",
    "agency_id": "2106",
    "agency_city": "Princeton",
    "prime_vjur": "2106",
    "icbc_detachment_name": "PRINCETON RCMP",
    "icbc_city_name": "PRINCETON",
    "vips_policedetachments_agency_id": "30",
    "vips_policedetachments_agency_nm": "Princeton"
  },
  {
    "agency_name": "RCMP Quadra Island",
    "agency_id": "4316",
    "agency_city": "Quadra Island",
    "prime_vjur": "4316",
    "icbc_detachment_name": "QUADRA ISLAND RCMP",
    "icbc_city_name": "QUADRA ISLAND",
    "vips_policedetachments_agency_id": "200",
    "vips_policedetachments_agency_nm": "Quadra Island"
  },
  {
    "agency_name": "RCMP Quesnel",
    "agency_id": "3301",
    "agency_city": "Quesnel",
    "prime_vjur": "3301",
    "icbc_detachment_name": "QUESNEL RCMP",
    "icbc_city_name": "QUESNEL",
    "vips_policedetachments_agency_id": "111",
    "vips_policedetachments_agency_nm": "Quesnel/ TS (CCR TS)"
  },
  {
    "agency_name": "RCMP Revelstoke",
    "agency_id": "2114",
    "agency_city": "Revelstoke",
    "prime_vjur": "2114",
    "icbc_detachment_name": "REVELSTOKE RCMP",
    "icbc_city_name": "REVELSTOKE",
    "vips_policedetachments_agency_id": "31",
    "vips_policedetachments_agency_nm": "Revelstoke/ TS"
  },
  {
    "agency_name": "RCMP Richmond",
    "agency_id": "1401",
    "agency_city": "Richmond",
    "prime_vjur": "1401",
    "icbc_detachment_name": "RICHMOND RCMP",
    "icbc_city_name": "RICHMOND",
    "vips_policedetachments_agency_id": "156",
    "vips_policedetachments_agency_nm": "Richmond"
  },
  {
    "agency_name": "RCMP Ridge Meadows",
    "agency_id": "1206",
    "agency_city": "Maple Ridge",
    "prime_vjur": "1206",
    "icbc_detachment_name": "RIDGE MEADOWS RCMP",
    "icbc_city_name": "MAPLE RIDGE",
    "vips_policedetachments_agency_id": "147",
    "vips_policedetachments_agency_nm": "Maple Ridge"
  },
  {
    "agency_name": "RCMP Salmo",
    "agency_id": "2301",
    "agency_city": "Salmo",
    "prime_vjur": "2301",
    "icbc_detachment_name": "CENTRAL KOOTENAY RCMP",
    "icbc_city_name": "SALMO",
    "vips_policedetachments_agency_id": "79",
    "vips_policedetachments_agency_nm": "Salmo"
  },
  {
    "agency_name": "RCMP Salmon Arm",
    "agency_id": "2112",
    "agency_city": "Salmon Arm",
    "prime_vjur": "2112",
    "icbc_detachment_name": "SALMON ARM RCMP",
    "icbc_city_name": "SALMON ARM",
    "vips_policedetachments_agency_id": "32",
    "vips_policedetachments_agency_nm": "Salmon Arm"
  },
  {
    "agency_name": "RCMP Salt Spring",
    "agency_id": "4108",
    "agency_city": "Salt Spring Island",
    "prime_vjur": "4108",
    "icbc_detachment_name": "SALT SPRING ISLAND RCMP",
    "icbc_city_name": "SALT SPRING ISLAND",
    "vips_policedetachments_agency_id": "174",
    "vips_policedetachments_agency_nm": "Salt Spring Island"
  },
  {
    "agency_name": "RCMP Sayward",
    "agency_id": "4318",
    "agency_city": "Sayward",
    "prime_vjur": "4318",
    "icbc_detachment_name": "SAYWARD RCMP",
    "icbc_city_name": "SAYWARD",
    "vips_policedetachments_agency_id": "201",
    "vips_policedetachments_agency_nm": "Sayward"
  },
  {
    "agency_name": "RCMP Shawnigan Lake",
    "agency_id": "4205",
    "agency_city": "Shawnigan Lake",
    "prime_vjur": "4205",
    "icbc_detachment_name": "SHAWNIGAN LAKE RCMP",
    "icbc_city_name": "SHAWNIGAN LAKE",
    "vips_policedetachments_agency_id": "18",
    "vips_policedetachments_agency_nm": "Shawnigan Lake"
  },
  {
    "agency_name": "RCMP Sicamous",
    "agency_id": "2113",
    "agency_city": "Sicamous",
    "prime_vjur": "2113",
    "icbc_detachment_name": "SICAMOUS RCMP",
    "icbc_city_name": "SICAMOUS",
    "vips_policedetachments_agency_id": "34",
    "vips_policedetachments_agency_nm": "Sicamous"
  },
  {
    "agency_name": "RCMP Sidney/North Saanich",
    "agency_id": "4106",
    "agency_city": "Sidney",
    "prime_vjur": "4106",
    "icbc_detachment_name": "NORTH SAANICH/SIDNEY RCMP",
    "icbc_city_name": "SIDNEY",
    "vips_policedetachments_agency_id": "181",
    "vips_policedetachments_agency_nm": "Sidney"
  },
  {
    "agency_name": "RCMP Slocan Lake",
    "agency_id": "2301",
    "agency_city": "Slocan Lake",
    "prime_vjur": "2301",
    "icbc_detachment_name": "CENTRAL KOOTENAY RCMP",
    "icbc_city_name": "SLOCAN LAKE",
    "vips_policedetachments_agency_id": "70",
    "vips_policedetachments_agency_nm": "Kaslo"
  },
  {
    "agency_name": "RCMP Smithers",
    "agency_id": "3505",
    "agency_city": "Smithers",
    "prime_vjur": "3505",
    "icbc_detachment_name": "SMITHERS RCMP",
    "icbc_city_name": "SMITHERS",
    "vips_policedetachments_agency_id": "128",
    "vips_policedetachments_agency_nm": "Smithers"
  },
  {
    "agency_name": "RCMP Sooke",
    "agency_id": "4107",
    "agency_city": "Sooke",
    "prime_vjur": "4107",
    "icbc_detachment_name": "SOOKE RCMP",
    "icbc_city_name": "SOOKE",
    "vips_policedetachments_agency_id": "183",
    "vips_policedetachments_agency_nm": "Sooke"
  },
  {
    "agency_name": "RCMP Sparwood",
    "agency_id": "2403",
    "agency_city": "Sparwood",
    "prime_vjur": "2403",
    "icbc_detachment_name": "ELK VALLEY RCMP",
    "icbc_city_name": "SPARWOOD",
    "vips_policedetachments_agency_id": "80",
    "vips_policedetachments_agency_nm": "Sparwood"
  },
  {
    "agency_name": "RCMP Squamish",
    "agency_id": "1104",
    "agency_city": "Squamish",
    "prime_vjur": "1104",
    "icbc_detachment_name": "SQUAMISH RCMP",
    "icbc_city_name": "SQUAMISH",
    "vips_policedetachments_agency_id": "158",
    "vips_policedetachments_agency_nm": "Squamish"
  },
  {
    "agency_name": "RCMP Stewart",
    "agency_id": "3603",
    "agency_city": "Stewart",
    "prime_vjur": "3603",
    "icbc_detachment_name": "STEWART RCMP",
    "icbc_city_name": "STEWART",
    "vips_policedetachments_agency_id": "129",
    "vips_policedetachments_agency_nm": "Stewart"
  },
  {
    "agency_name": "RCMP Summerland",
    "agency_id": "2103",
    "agency_city": "Summerland",
    "prime_vjur": "2103",
    "icbc_detachment_name": "SUMMERLAND RCMP",
    "icbc_city_name": "SUMMERLAND",
    "vips_policedetachments_agency_id": "36",
    "vips_policedetachments_agency_nm": "Summerland"
  },
  {
    "agency_name": "RCMP Sunshine Coast",
    "agency_id": "1106",
    "agency_city": "Sechelt",
    "prime_vjur": "1106",
    "icbc_detachment_name": "SUNSHINE COAST RCMP",
    "icbc_city_name": "SECHELT",
    "vips_policedetachments_agency_id": "157",
    "vips_policedetachments_agency_nm": "Sechelt"
  },
  {
    "agency_name": "RCMP Surrey",
    "agency_id": "1301",
    "agency_city": "Surrey",
    "prime_vjur": "1301",
    "icbc_detachment_name": "SURREY RCMP",
    "icbc_city_name": "SURREY",
    "vips_policedetachments_agency_id": "160",
    "vips_policedetachments_agency_nm": "Surrey (M)"
  },
  {
    "agency_name": "RCMP Takla Landing",
    "agency_id": "3203",
    "agency_city": "Takla Landing",
    "prime_vjur": "3203",
    "icbc_detachment_name": "TAKLA LANDING RCMP",
    "icbc_city_name": "TAKLA LANDING",
    "vips_policedetachments_agency_id": "103",
    "vips_policedetachments_agency_nm": "Fort St. James"
  },
  {
    "agency_name": "RCMP Telegraph Creek",
    "agency_id": "3604",
    "agency_city": "Telegraph Creek",
    "prime_vjur": "3604",
    "icbc_detachment_name": "DEASE LAKE RCMP",
    "icbc_city_name": "TELEGRAPH CREEK",
    "vips_policedetachments_agency_id": "17",
    "vips_policedetachments_agency_nm": "Telegraph Creek"
  },
  {
    "agency_name": "RCMP Terrace",
    "agency_id": "3501",
    "agency_city": "Terrace",
    "prime_vjur": "3501",
    "icbc_detachment_name": "TERRACE RCMP",
    "icbc_city_name": "TERRACE",
    "vips_policedetachments_agency_id": "131",
    "vips_policedetachments_agency_nm": "Terrace"
  },
  {
    "agency_name": "RCMP Texada Island",
    "agency_id": "4306",
    "agency_city": "Texada Island",
    "prime_vjur": "4306",
    "icbc_detachment_name": "POWELL RIVER RCMP",
    "icbc_city_name": "TEXADA ISLAND",
    "vips_policedetachments_agency_id": "207",
    "vips_policedetachments_agency_nm": "Texada Island"
  },
  {
    "agency_name": "RCMP TK'EMLUPS",
    "agency_id": "2201",
    "agency_city": "Kamloops",
    "prime_vjur": "2201",
    "icbc_detachment_name": "KAMLOOPS CITY RCMP",
    "icbc_city_name": "KAMLOOPS",
    "vips_policedetachments_agency_id": "265",
    "vips_policedetachments_agency_nm": "T'Kumlups"
  },
  {
    "agency_name": "RCMP Tofino",
    "agency_id": "4304",
    "agency_city": "Tofino",
    "prime_vjur": "4304",
    "icbc_detachment_name": "TOFINO RCMP (AHOUSAHT)",
    "icbc_city_name": "TOFINO",
    "vips_policedetachments_agency_id": "203",
    "vips_policedetachments_agency_nm": "Tofino"
  },
  {
    "agency_name": "RCMP Trail",
    "agency_id": "2304",
    "agency_city": "Trail",
    "prime_vjur": "2304",
    "icbc_detachment_name": "TRAIL AND GREATER DIST RCMP",
    "icbc_city_name": "TRAIL",
    "vips_policedetachments_agency_id": "81",
    "vips_policedetachments_agency_nm": "Trail"
  },
  {
    "agency_name": "RCMP Tsay Keh Dene",
    "agency_id": "3105",
    "agency_city": "Tsay Keh Dene",
    "prime_vjur": "3105",
    "icbc_detachment_name": "TSAY KEH DENE RCMP",
    "icbc_city_name": "TSAY KEH DENE",
    "vips_policedetachments_agency_id": "266",
    "vips_policedetachments_agency_nm": "Tsay Keh"
  },
  {
    "agency_name": "RCMP Tumbler Ridge",
    "agency_id": "3404",
    "agency_city": "Tumbler Ridge",
    "prime_vjur": "3404",
    "icbc_detachment_name": "TUMBLER RIDGE RCMP",
    "icbc_city_name": "TUMBLER RIDGE",
    "vips_policedetachments_agency_id": "117",
    "vips_policedetachments_agency_nm": "Tumbler Ridge"
  },
  {
    "agency_name": "RCMP Ucluelet",
    "agency_id": "4305",
    "agency_city": "Ucluelet",
    "prime_vjur": "4305",
    "icbc_detachment_name": "UCLUELET RCMP",
    "icbc_city_name": "UCLUELET",
    "vips_policedetachments_agency_id": "204",
    "vips_policedetachments_agency_nm": "Ucluelet"
  },
  {
    "agency_name": "RCMP University BC",
    "agency_id": "1402",
    "agency_city": "Vancouver",
    "prime_vjur": "1402",
    "icbc_detachment_name": "UNIVERSITY RCMP",
    "icbc_city_name": "VANCOUVER",
    "vips_policedetachments_agency_id": "161",
    "vips_policedetachments_agency_nm": "University"
  },
  {
    "agency_name": "RCMP Valemount",
    "agency_id": "3103",
    "agency_city": "Valemount",
    "prime_vjur": "3103",
    "icbc_detachment_name": "VALEMOUNT RCMP",
    "icbc_city_name": "VALEMOUNT",
    "vips_policedetachments_agency_id": "57",
    "vips_policedetachments_agency_nm": "Valemount/ TS"
  },
  {
    "agency_name": "RCMP Vanderhoof",
    "agency_id": "3201",
    "agency_city": "Vanderhoof",
    "prime_vjur": "3201",
    "icbc_detachment_name": "VANDERHOOF RCMP",
    "icbc_city_name": "VANDERHOOF",
    "vips_policedetachments_agency_id": "113",
    "vips_policedetachments_agency_nm": "Vanderhoof/ TS"
  },
  {
    "agency_name": "RCMP Vernon",
    "agency_id": "2111",
    "agency_city": "Vernon",
    "prime_vjur": "2111",
    "icbc_detachment_name": "NORTH OKANAGAN RCMP",
    "icbc_city_name": "VERNON",
    "vips_policedetachments_agency_id": "35",
    "vips_policedetachments_agency_nm": "Vernon"
  },
  {
    "agency_name": "RCMP West Kelowna",
    "agency_id": "2101",
    "agency_city": "West Kelowna",
    "prime_vjur": "2101",
    "icbc_detachment_name": "KELOWNA RCMP",
    "icbc_city_name": "WEST KELOWNA",
    "vips_policedetachments_agency_id": "270",
    "vips_policedetachments_agency_nm": "West Kelowna"
  },
  {
    "agency_name": "RCMP West Shore",
    "agency_id": "4105",
    "agency_city": "Langford",
    "prime_vjur": "4105",
    "icbc_detachment_name": "WEST SHORE RCMP",
    "icbc_city_name": "LANGFORD",
    "vips_policedetachments_agency_id": "170",
    "vips_policedetachments_agency_nm": "West Shore"
  },
  {
    "agency_name": "RCMP Whistler",
    "agency_id": "1105",
    "agency_city": "Whistler",
    "prime_vjur": "1105",
    "icbc_detachment_name": "WHISTLER/PEMBERTON RCMP",
    "icbc_city_name": "WHISTLER",
    "vips_policedetachments_agency_id": "164",
    "vips_policedetachments_agency_nm": "Whistler"
  },
  {
    "agency_name": "RCMP White Rock",
    "agency_id": "1304",
    "agency_city": "White Rock",
    "prime_vjur": "1304",
    "icbc_detachment_name": "WHITE ROCK RCMP",
    "icbc_city_name": "WHITE ROCK",
    "vips_policedetachments_agency_id": "162",
    "vips_policedetachments_agency_nm": "White Rock"
  },
  {
    "agency_name": "RCMP Williams Lake",
    "agency_id": "3304",
    "agency_city": "Williams Lake",
    "prime_vjur": "3304",
    "icbc_detachment_name": "WILLIAMS LAKE RCMP",
    "icbc_city_name": "WILLIAMS LAKE",
    "vips_policedetachments_agency_id": "58",
    "vips_policedetachments_agency_nm": "Williams Lake/ TS"
  },
  {
    "agency_name": "Saanich Police Dept.",
    "agency_id": "SA",
    "agency_city": "Saanich",
    "prime_vjur": "SA",
    "icbc_detachment_name": "SAANICH POLICE DEPARTMENT",
    "icbc_city_name": "SAANICH",
    "vips_policedetachments_agency_id": "88",
    "vips_policedetachments_agency_nm": "Saanich"
  },
  {
    "agency_name": "Stl'atl'imx Tribal Police Svc.",
    "agency_id": "1107",
    "agency_city": "Mount Currie",
    "prime_vjur": "1107",
    "icbc_detachment_name": "STL' ATL' IMX POLICE FNAPS",
    "icbc_city_name": "MOUNT CURRIE",
    "vips_policedetachments_agency_id": "264",
    "vips_policedetachments_agency_nm": "Stl'alt'imx Tribal Police"
  },
  {
    "agency_name": "Surrey Police Svc.",
    "agency_id": "SP",
    "agency_city": "Surrey",
    "prime_vjur": "SP",
    "icbc_detachment_name": "SURREY POLICE SERVICE",
    "icbc_city_name": "SURREY",
    "vips_policedetachments_agency_id": "268",
    "vips_policedetachments_agency_nm": "Detachment name not provided"
  },
  {
    "agency_name": "Vancouver Police Dept.",
    "agency_id": "VA",
    "agency_city": "Vancouver",
    "prime_vjur": "VA",
    "icbc_detachment_name": "VANCOUVER POLICE DEPARTMENT",
    "icbc_city_name": "VANCOUVER",
    "vips_policedetachments_agency_id": "86",
    "vips_policedetachments_agency_nm": "Vancouver City Police"
  },
  {
    "agency_name": "Victoria Police Dept.",
    "agency_id": "VI",
    "agency_city": "Victoria",
    "prime_vjur": "VI",
    "icbc_detachment_name": "VICTORIA POLICE DEPARTMENT",
    "icbc_city_name": "VICTORIA",
    "vips_policedetachments_agency_id": "87",
    "vips_policedetachments_agency_nm": "Victoria City Police"
  },
  {
    "agency_name": "West Vancouver Police Dept.",
    "agency_id": "WV",
    "agency_city": "West Vancouver",
    "prime_vjur": "WV",
    "icbc_detachment_name": "WEST VANCOUVER POLICE DEPT.",
    "icbc_city_name": "WEST VANCOUVER",
    "vips_policedetachments_agency_id": "94",
    "vips_policedetachments_agency_nm": "West Vancouver"
  }
]

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agency_cross_refs',
    sa.Column('agency_name', sa.String(), nullable=False),
    sa.Column('agency_id', sa.String(), nullable=True),
    sa.Column('agency_city', sa.String(), nullable=True),
    sa.Column('prime_vjur', sa.String(), nullable=True),
    sa.Column('icbc_detachment_name', sa.String(), nullable=True),
    sa.Column('icbc_city_name', sa.String(), nullable=True),
    sa.Column('vips_policedetachments_agency_id', sa.String(), nullable=True),
    sa.Column('vips_policedetachments_agency_nm', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('agency_name')
    )
    
    with op.get_context().autocommit_block():
        bind = op.get_bind()
        meta = sa.MetaData()
        meta.bind = bind
        meta.reflect(bind=bind, only=('agency_cross_refs',))
        agency_cross_refs = sa.Table('agency_cross_refs', meta)
        op.bulk_insert(agency_cross_refs, new_data)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('agency_cross_refs')
    # ### end Alembic commands ###
