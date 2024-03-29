"""empty message

Revision ID: 9f87a8df07a8
Revises: 237614f969cf
Create Date: 2023-12-11 21:08:20.252366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f87a8df07a8'
down_revision = '237614f969cf'
branch_labels = None
depends_on = None

new_data = [
  {
    "name": "5 STAR TOWING",
    "name_print": "5 STAR TOWING",
    "lot_address": "733 2ND AVE",
    "city": "PRINCE GEORGE",
    "phone": "250-614-9393"
  },
  {
    "name": "A & M TOWING",
    "name_print": "A & M TOWING",
    "lot_address": "305 MOORE AVE",
    "city": "100 MILE HOUSE",
    "phone": "250-395-4334"
  },
  {
    "name": "A J TOWING",
    "name_print": "A J TOWING",
    "lot_address": "8945 NOWELL ST",
    "city": "CHILLIWACK",
    "phone": "604-795-3374"
  },
  {
    "name": "ABLE TOWING",
    "name_print": "ABLE TOWING",
    "lot_address": "2384 210 RD",
    "city": "DAWSON CREEK",
    "phone": "250-782-4239"
  },
  {
    "name": "AGGRESSIVE AUTO TOWING",
    "name_print": "AGGRESSIVE TOWING",
    "lot_address": "34523 2ND AVE",
    "city": "ABBOTSFORD",
    "phone": "604-854-5669"
  },
  {
    "name": "ALBERNI TOWING",
    "name_print": "ALBERNI TOWING",
    "lot_address": "2490 TIMBERLANE RD",
    "city": "PORT ALBERNI",
    "phone": "250-724-4050"
  },
  {
    "name": "ALL COAST TOWING SERVICES",
    "name_print": "ALL COAST TOWING",
    "lot_address": "1178 STEWART RD",
    "city": "GIBSONS",
    "phone": "604-886-7280"
  },
  {
    "name": "ALL-WAYS TOWING",
    "name_print": "ALL-WAYS TOWING",
    "lot_address": "647B DUPPLIN RD",
    "city": "VICTORIA",
    "phone": "250-381-0110"
  },
  {
    "name": "ANTLE TOWING",
    "name_print": "ANTLE TOWING",
    "lot_address": "802 EXETER STATION RD",
    "city": "LAC LA HACHE",
    "phone": "250-396-7306"
  },
  {
    "name": "APPLEWOOD TOWING",
    "name_print": "APPLEWOOD TOWING",
    "lot_address": "4800 BYNG RD",
    "city": "PORT HARDY",
    "phone": "250-949-6042"
  },
  {
    "name": "ARROWSMITH TOWING",
    "name_print": "ARROWSMITH TOWING",
    "lot_address": "20 HILLIERS RD",
    "city": "QUALICUM BEACH",
    "phone": "250-752-1662"
  },
  {
    "name": "AURORA TOWING",
    "name_print": "AURORA TOWING",
    "lot_address": "2206 NADINA AVE N",
    "city": "HOUSTON",
    "phone": "250-845-7600"
  },
  {
    "name": "AUTOW / QUESNEL TOWING",
    "name_print": "AUTOW TOWING",
    "lot_address": "402 JUNIPER RD",
    "city": "QUESNEL",
    "phone": "250-992-9128"
  },
  {
    "name": "BAILLIE'S TOWING",
    "name_print": "BAILLIE'S TOWING",
    "lot_address": "4833 GILBERT DR",
    "city": "BARRIERE",
    "phone": "250-672-9529"
  },
  {
    "name": "BARRIERE AUTO & TRUCK TOW",
    "name_print": "BARRIERE TOW",
    "lot_address": "4403 AIRFIELD RD",
    "city": "BARRIERE",
    "phone": "250-319-7767"
  },
  {
    "name": "BAYVIEW AUTO TOWING",
    "name_print": "BAYVIEW TOWING",
    "lot_address": "155 176 AVE #201",
    "city": "SURREY",
    "phone": "604-538-2032"
  },
  {
    "name": "BEE JAY TOWING",
    "name_print": "BEE JAY TOWING",
    "lot_address": "765 MACKENZIE AVE N",
    "city": "WILLIAMS LAKE",
    "phone": "250-398-8311"
  },
  {
    "name": "BEN'S TOWING",
    "name_print": "BEN'S TOWING",
    "lot_address": "230 42 ST SW",
    "city": "SALMON ARM",
    "phone": "250-832-6512"
  },
  {
    "name": "BKV TOWING",
    "name_print": "BKV TOWING",
    "lot_address": "13200 BARTLETT RD",
    "city": "BURNS LAKE",
    "phone": "250-692-3413"
  },
  {
    "name": "BLACK BEAR TOWING",
    "name_print": "BLACK BEAR TOWING",
    "lot_address": "1080 INDUSTRIAL WAY",
    "city": "PARKSVILLE",
    "phone": "250-468-1458"
  },
  {
    "name": "BOYCE AUTO TOWING",
    "name_print": "BOYCE AUTO TOWING",
    "lot_address": "15700 RIVER RD",
    "city": "RICHMOND",
    "phone": "604-278-1106"
  },
  {
    "name": "BRIDGE LAKE TOWING",
    "name_print": "BRIDGE LAKE TOWING",
    "lot_address": "310 MOORE AVE",
    "city": "100 MILE HOUSE",
    "phone": "250-593-4056"
  },
  {
    "name": "BUSTER'S TOWING",
    "name_print": "BUSTER'S TOWING",
    "lot_address": "425 INDUSTRIAL AVE",
    "city": "VANCOUVER",
    "phone": "604-685-8181"
  },
  {
    "name": "CARIBOO TOWING",
    "name_print": "CARIBOO TOWING",
    "lot_address": "750 MACKENZIE AVE S",
    "city": "WILLIAMS LAKE",
    "phone": "250-392-2888"
  },
  {
    "name": "CARIBOU SERVICE",
    "name_print": "CARIBOU SERVICE",
    "lot_address": "5549 BURTON FRONTAGE RD",
    "city": "BURTON",
    "phone": "250-265-3191"
  },
  {
    "name": "CENTRAL TOWING",
    "name_print": "CENTRAL TOWING",
    "lot_address": "10930 WESTDOWNE RD",
    "city": "LADYSMITH",
    "phone": "250-245-4411"
  },
  {
    "name": "CHANOR TRUCK & AUTO REPAIR",
    "name_print": "CHANOR REPAIR",
    "lot_address": "1371 QUARTZ RD",
    "city": "CACHE CREEK",
    "phone": "250-457-6753"
  },
  {
    "name": "CHARLOTTE ISLAND TIRE",
    "name_print": "CHARLOTTE TIRE",
    "lot_address": "605 OCEANVIEW DR",
    "city": "DAAJING GIIDS",
    "phone": "250-559-4641"
  },
  {
    "name": "CHRISTINA LAKE TOWING",
    "name_print": "CHRISTINA LAKE TOW",
    "lot_address": "1648 MAIDA FRONTAGE RD",
    "city": "CHRISTINA LAKE",
    "phone": "250-442-9477"
  },
  {
    "name": "CITY MOTORS",
    "name_print": "CITY MOTORS",
    "lot_address": "5951 ARBUTUS AVE",
    "city": "POWELL RIVER",
    "phone": "604-483-3210"
  },
  {
    "name": "CITY OF NEW WESTMINSTER TOWING",
    "name_print": "NEWWEST TOWING",
    "lot_address": "420 BOYNE ST",
    "city": "NEW WESTMINSTER",
    "phone": "604-519-1026"
  },
  {
    "name": "CLASSIC TOWING (GOLDEN)",
    "name_print": "CLASSIC TOWING",
    "lot_address": "1025 11 AVE N",
    "city": "GOLDEN",
    "phone": "250-344-6659"
  },
  {
    "name": "CLASSIC TOWING (REVELSTOKE)",
    "name_print": "CLASSIC TOWING",
    "lot_address": "2100 BIG EDDY RD",
    "city": "REVELSTOKE",
    "phone": "250-837-6216"
  },
  {
    "name": "CLEARWATER TOWING",
    "name_print": "CLEARWATER TOWING",
    "lot_address": "516 SWANSON AVE",
    "city": "CLEARWATER",
    "phone": "250-674-3123"
  },
  {
    "name": "CLOVER TOWING",
    "name_print": "CLOVER TOWING",
    "lot_address": "5340 192 AVE",
    "city": "SURREY",
    "phone": "604-513-1900"
  },
  {
    "name": "CLUB TOWING & HEAVY RECOVERY",
    "name_print": "CLUB TOWING",
    "lot_address": "505 INDUSTRIAL RD #2",
    "city": "INVERMERE",
    "phone": "250-342-9551"
  },
  {
    "name": "COASTLINE TOWING",
    "name_print": "COASTLINE TOWING",
    "lot_address": "1893 COULTER RD",
    "city": "CAMPBELL RIVER",
    "phone": "250-923-8111"
  },
  {
    "name": "COLLISION CRAFT / USHER'S TOWING",
    "name_print": "COLLISION CRAFT",
    "lot_address": "101 11129 115 AVE",
    "city": "OSOYOOS",
    "phone": "250-495-6331"
  },
  {
    "name": "COMOX VALLEY DODGE",
    "name_print": "COMOX VALLEY DODGE",
    "lot_address": "2400 COUSINS RD",
    "city": "COURTENAY",
    "phone": "250-338-4665"
  },
  {
    "name": "COOPER'S TOWING",
    "name_print": "COOPER'S TOWING",
    "lot_address": "8065 NESTERS RD",
    "city": "WHISTLER",
    "phone": "604-902-1930"
  },
  {
    "name": "COQUITLAM TOWING",
    "name_print": "COQUITLAM TOWING",
    "lot_address": "218 CAYER ST",
    "city": "COQUITLAM",
    "phone": "604-939-6474"
  },
  {
    "name": "DAKOTA TOWING",
    "name_print": "DAKOTA TOWING",
    "lot_address": "1505 HARDY AVE",
    "city": "KELOWNA",
    "phone": "250-300-3999"
  },
  {
    "name": "DAY & NITE TOWING",
    "name_print": "DAY & NITE TOWING",
    "lot_address": "1933 FIELD RD",
    "city": "SECHELT",
    "phone": "604-885-0699"
  },
  {
    "name": "DEL ORO TOWING",
    "name_print": "DEL ORO TOWING",
    "lot_address": "2535 JULIANN RD",
    "city": "WEST KELOWNA",
    "phone": "250-769-2100"
  },
  {
    "name": "DOLLAR TOWING",
    "name_print": "DOLLAR TOWING",
    "lot_address": "1700 NALABILA BLVD",
    "city": "KITIMAT",
    "phone": "250-632-2261"
  },
  {
    "name": "DON'S AUTO TOWING",
    "name_print": "DON'S AUTO TOWING",
    "lot_address": "671 ATHABASCA AVE",
    "city": "KAMLOOPS",
    "phone": "250-374-6281"
  },
  {
    "name": "DRAKE TOWING",
    "name_print": "DRAKE TOWING",
    "lot_address": "1553 POWELL AVE",
    "city": "VANCOUVER",
    "phone": "604-251-3344"
  },
  {
    "name": "DUNN RIGHT TOWING & RECOVERY",
    "name_print": "DUNN RIGHT TOWING",
    "lot_address": "691 MCPHEE AVE",
    "city": "COURTENAY",
    "phone": "250-650-8697"
  },
  {
    "name": "EAGLE EYE MARINE SERVICES",
    "name_print": "EAGLE EYE",
    "lot_address": "127 FULFORD-GANGES RD",
    "city": "SALT SPRING ISLAND",
    "phone": "250-883-7865"
  },
  {
    "name": "EAGLE ROCK TOWING (ARMSTRONG)",
    "name_print": "EAGLE ROCK TOWING",
    "lot_address": "1645 EAGLE ROCK RD",
    "city": "ARMSTRONG",
    "phone": "250-546-8290"
  },
  {
    "name": "EAGLE ROCK TOWING (SALMON ARM)",
    "name_print": "EAGLE ROCK TOWING",
    "lot_address": "5270 AUTO RD",
    "city": "SALMON ARM",
    "phone": "250-804-4442"
  },
  {
    "name": "EAGLE ROCK TOWING (SICAMOUS)",
    "name_print": "EAGLE ROCK TOWING",
    "lot_address": "901 TRANS CANADA HWY FRONTAGE RD",
    "city": "SICAMOUS",
    "phone": "250-836-0333"
  },
  {
    "name": "EFM TOWING",
    "name_print": "EFM TOWING",
    "lot_address": "741 INDUSTRIAL RD 2",
    "city": "CRANBROOK",
    "phone": "250-417-7334"
  },
  {
    "name": "EISENKRIEN SERVICES",
    "name_print": "EISENKRIEN SVCS",
    "lot_address": "101 EXTENSION RD",
    "city": "WONOWON",
    "phone": "250-263-8733"
  },
  {
    "name": "ENCORE TOWING & SERVICE",
    "name_print": "ENCORE TOWING",
    "lot_address": "38926 PRODUCTION WAY",
    "city": "SQUAMISH",
    "phone": "604-892-5051"
  },
  {
    "name": "EXCEPTIONAL TOWING & RECOVERY",
    "name_print": "EXCEPTIONAL TOWING",
    "lot_address": "1529 99 AVE",
    "city": "DAWSON CREEK",
    "phone": "250-782-4845"
  },
  {
    "name": "FIRST CHOICE TOWING",
    "name_print": "FIRST CHOICE TOW",
    "lot_address": "10150 ALDER CRES",
    "city": "FORT ST. JOHN",
    "phone": "250-785-2271"
  },
  {
    "name": "FREIGHTLINER OF CRANBROOK",
    "name_print": "FREIGHTLINER",
    "lot_address": "301 SLATER RD",
    "city": "CRANBROOK",
    "phone": "250-489-8781"
  },
  {
    "name": "GAMMOND TOWING",
    "name_print": "GAMMOND TOWING",
    "lot_address": "31539 TELEGRAPH RD",
    "city": "FORT FRASER",
    "phone": "250-996-3377"
  },
  {
    "name": "GARRICK AUTOMOTIVE",
    "name_print": "GARRICK AUTOMOTIVE",
    "lot_address": "246 ALYMER RD",
    "city": "CHASE",
    "phone": "250-679-3167"
  },
  {
    "name": "GATEWAY TOWING & RECOVERY",
    "name_print": "GATEWAY TOWING",
    "lot_address": "524 INDUSTRIAL PARK PL",
    "city": "GOLD RIVER",
    "phone": "250-283-9141"
  },
  {
    "name": "GEM TOWING",
    "name_print": "GEM TOWING",
    "lot_address": "2359 164 AVE",
    "city": "WHITE ROCK",
    "phone": "604-531-8765"
  },
  {
    "name": "GEORGIA STRAIGHT TOWING",
    "name_print": "GEORGIA STRAIGHT",
    "lot_address": "2317 COUSINS RD",
    "city": "COURTENAY",
    "phone": "250-338-9899"
  },
  {
    "name": "GINO'S TOWING",
    "name_print": "GINO'S TOWING",
    "lot_address": "296 OSILINKA DR",
    "city": "MACKENZIE",
    "phone": "250-271-4466"
  },
  {
    "name": "GIVER A YANK TOWING",
    "name_print": "GIVER A YANK",
    "lot_address": "611 STEWART ST E",
    "city": "VANDERHOOF",
    "phone": "250-570-0077"
  },
  {
    "name": "GOOD SHEPHERD TOWING",
    "name_print": "GOOD SHEPHERD",
    "lot_address": "230 SHELLY RD",
    "city": "PARKSVILLE",
    "phone": "250-248-3110"
  },
  {
    "name": "GRANTON MOTORS",
    "name_print": "GRANTON MOTORS",
    "lot_address": "3335 HWY 3",
    "city": "ROCK CREEK",
    "phone": "250-446-2311"
  },
  {
    "name": "GRASS CREEK VENTURES",
    "name_print": "GRASS CREEK",
    "lot_address": "415 HWY 37",
    "city": "ISKUT",
    "phone": "250-234-3434"
  },
  {
    "name": "HOGIES TOWING",
    "name_print": "HOGIES TOWING",
    "lot_address": "1360 PLEASANT VALLEY RD",
    "city": "ARMSTRONG",
    "phone": "250-546-3472"
  },
  {
    "name": "HOPE TOWING",
    "name_print": "HOPE TOWING",
    "lot_address": "1060 5TH AVE",
    "city": "HOPE",
    "phone": "604-869-3444"
  },
  {
    "name": "ISLAND THUNDER TOWING",
    "name_print": "ISLAND THUNDER TOW",
    "lot_address": "1801 TWIN PEAKS RD",
    "city": "PORT MCNEILL",
    "phone": "250-956-2656"
  },
  {
    "name": "J D TOWING",
    "name_print": "J D TOWING",
    "lot_address": "6585 INDUSTRIAL PARK WAY",
    "city": "GRAND FORKS",
    "phone": "250-442-2551"
  },
  {
    "name": "JACK'S TOWING (ABBOTSFORD)",
    "name_print": "JACK'S TOWING",
    "lot_address": "63 WEST RAILWAY",
    "city": "ABBOTSFORD",
    "phone": "604-607-0772"
  },
  {
    "name": "JACK'S TOWING (MISSION)",
    "name_print": "JACK'S TOWING",
    "lot_address": "7143 WREN ST",
    "city": "MISSION",
    "phone": "604-607-0772"
  },
  {
    "name": "JAMIE DAVIS TOWING (GOLDEN)",
    "name_print": "JAMIE DAVIS TOWING",
    "lot_address": "920 KING PLACE",
    "city": "GOLDEN",
    "phone": "250-344-6690"
  },
  {
    "name": "JAMIE DAVIS TOWING (HOPE)",
    "name_print": "JAMIE DAVIS TOWING",
    "lot_address": "19683 SILVER SKAGIT RD",
    "city": "HOPE",
    "phone": "604-869-8440"
  },
  {
    "name": "JAY'S TOWING",
    "name_print": "JAY'S TOWING",
    "lot_address": "121 HAST RD",
    "city": "PRINCE RUPERT",
    "phone": "250-624-8094"
  },
  {
    "name": "JIMCO TOWING",
    "name_print": "JIMCO TOWING",
    "lot_address": "3982 SQUILAX-ANGLEMONT RD",
    "city": "SCOTCH CREEK",
    "phone": "250-319-5250"
  },
  {
    "name": "KBM AUTOWORKS & TOWING",
    "name_print": "KBM TOWING",
    "lot_address": "1862 VERNON AVE",
    "city": "LUMBY",
    "phone": "250-547-2356"
  },
  {
    "name": "KEEGZ SOUTH COUNTRY TOWING",
    "name_print": "KEEGZ TOWING",
    "lot_address": "1010 COMMERCIAL WAY",
    "city": "GENELLE",
    "phone": "250-693-8850"
  },
  {
    "name": "KMB AUTOBODY",
    "name_print": "KMB AUTOBODY",
    "lot_address": "1527 TIE LAKE LOOP RD",
    "city": "JAFFRAY",
    "phone": "250-429-3413"
  },
  {
    "name": "KOMAR TOWING",
    "name_print": "KOMAR TOWING",
    "lot_address": "1300 TACHIE RD",
    "city": "FORT ST. JAMES",
    "phone": "250-996-2206"
  },
  {
    "name": "KOOL COUNTRY TOWING",
    "name_print": "KOOL TOWING",
    "lot_address": "150 INDUSTRIAL 2 RD #2",
    "city": "INVERMERE",
    "phone": "250-342-5188"
  },
  {
    "name": "KOOTENAY TOWING",
    "name_print": "KOOTENAY TOWING",
    "lot_address": "6635 HWY 31",
    "city": "KASLO",
    "phone": "250-353-2110"
  },
  {
    "name": "L J'S TOWING & TRANSPORT",
    "name_print": "L J'S TOWING",
    "lot_address": "7519 TRANS CANADA HWY",
    "city": "CHASE",
    "phone": "250-679-8600"
  },
  {
    "name": "LANE'S AUTO TOWING",
    "name_print": "LANE'S AUTO TOWING",
    "lot_address": "258 GLEN RD",
    "city": "AVOLA",
    "phone": "250-678-2300"
  },
  {
    "name": "LARSEN TOWING",
    "name_print": "LARSEN TOWING",
    "lot_address": "8590 GAUDET RD",
    "city": "POWELL RIVER",
    "phone": "604-316-8187"
  },
  {
    "name": "LILLOOET AUTOBODY & TOWING",
    "name_print": "LILLOOET TOWING",
    "lot_address": "205 MAIN ST",
    "city": "LILLOOET",
    "phone": "250-256-4687"
  },
  {
    "name": "LITTLE MOUNTAIN TOWING",
    "name_print": "LITTLE MTN TOWING",
    "lot_address": "1130 DOBLER RD",
    "city": "ERRINGTON",
    "phone": "250-248-1132"
  },
  {
    "name": "LONG BEACH TOWING",
    "name_print": "LONG BEACH TOWING",
    "lot_address": "671 INDUSTRIAL WAY #3",
    "city": "TOFINO",
    "phone": "250-725-2030"
  },
  {
    "name": "MAC'S TOWING (MISSION)",
    "name_print": "MAC'S TOWING",
    "lot_address": "33201 LONDON AVE",
    "city": "MISSION",
    "phone": "604-826-9076"
  },
  {
    "name": "MAC'S TOWING (NEW HAZELTON)",
    "name_print": "MAC'S TOWING",
    "lot_address": "4167 15 AVE",
    "city": "NEW HAZELTON",
    "phone": "250-842-5404"
  },
  {
    "name": "MAPLE RIDGE TOWING",
    "name_print": "MAPLE RIDGE TOWING",
    "lot_address": "23283 MCKAY AVE",
    "city": "MAPLE RIDGE",
    "phone": "604-463-5146"
  },
  {
    "name": "MARIO'S TOWING (HOPE)",
    "name_print": "MARIO'S TOWING",
    "lot_address": "64211 FLOOD HOPE RD",
    "city": "HOPE",
    "phone": "888-292-1581"
  },
  {
    "name": "MARIO'S TOWING (KAMLOOPS)",
    "name_print": "MARIO'S TOWING",
    "lot_address": "726 CARRIER AVE",
    "city": "KAMLOOPS",
    "phone": "888-292-1581"
  },
  {
    "name": "MARIO'S TOWING (KELOWNA)",
    "name_print": "MARIO'S TOWING",
    "lot_address": "3015 SEXSMITH RD",
    "city": "KELOWNA",
    "phone": "250-765-6009"
  },
  {
    "name": "MARIO'S TOWING (MERRITT)",
    "name_print": "MARIO'S TOWING",
    "lot_address": "2676 NICOLA AVE",
    "city": "MERRITT",
    "phone": "250-378-9241"
  },
  {
    "name": "MARIO'S TOWING (PRINCETON)",
    "name_print": "MARIO'S TOWING",
    "lot_address": "401 HWY 3",
    "city": "PRINCETON",
    "phone": "888-292-1581"
  },
  {
    "name": "MARIO'S TOWING (WEST KELOWNA)",
    "name_print": "MARIO'S TOWING",
    "lot_address": "2535 JULIANN RD",
    "city": "WEST KELOWNA",
    "phone": "250-769-2100"
  },
  {
    "name": "MAYNE ISLAND TOWING",
    "name_print": "MAYNE ISLAND TOW",
    "lot_address": "273 WOODDALE DR",
    "city": "MAYNE ISLAND",
    "phone": "250-508-8908"
  },
  {
    "name": "MCBRIDE'S TOWING",
    "name_print": "MCBRIDE'S TOWING",
    "lot_address": "9616 CHEMAINUS RD",
    "city": "CHEMAINUS",
    "phone": "250-246-3595"
  },
  {
    "name": "ME & RON'S TOWING",
    "name_print": "ME & RON'S TOWING",
    "lot_address": "178 KINGS LANE",
    "city": "SALT SPRING ISLAND",
    "phone": "250-537-9383"
  },
  {
    "name": "MECHAM SALES & SERVICE",
    "name_print": "MECHAM SVC",
    "lot_address": "1843 MACKENZIE HWY",
    "city": "HAGENSBORG",
    "phone": "250-982-2345"
  },
  {
    "name": "MERRITT JJ'S TOWING & RECOVERY",
    "name_print": "MERRITT JJ'S TOW",
    "lot_address": "1141 MCFARLANE WAY",
    "city": "MERRITT",
    "phone": "866-670-6887"
  },
  {
    "name": "MID ISLAND TOWING",
    "name_print": "MID ISLAND TOWING",
    "lot_address": "4900 JORDAN AVE",
    "city": "NANAIMO",
    "phone": "250-758-1728"
  },
  {
    "name": "MID-NYTES TOWING",
    "name_print": "MID-NYTES TOWING",
    "lot_address": "1835 COALCHUTE RD",
    "city": "GRAND FORKS",
    "phone": "250-442-2233"
  },
  {
    "name": "MIKE'S AUTOMOTIVE SERVICES",
    "name_print": "MIKE'S AUTO SVCS",
    "lot_address": "37024 97 AVE",
    "city": "OLIVER",
    "phone": "250-498-2004"
  },
  {
    "name": "MILL BAY TOWING",
    "name_print": "MILL BAY TOWING",
    "lot_address": "3855B TRANS CANADA HWY",
    "city": "COBBLE HILL",
    "phone": "250-743-1552"
  },
  {
    "name": "MISSION TOWING (AGASSIZ)",
    "name_print": "MISSION TOWING",
    "lot_address": "7428 PIONEER AVE",
    "city": "AGASSIZ",
    "phone": "604-796-8697"
  },
  {
    "name": "MISSION TOWING (MISSION)",
    "name_print": "MISSION TOWING",
    "lot_address": "7143 WREN ST",
    "city": "MISSION",
    "phone": "604-826-1251"
  },
  {
    "name": "MITCHELL'S TOWING (NORTH VAN)",
    "name_print": "MITCHELL'S TOWING",
    "lot_address": "1255 WELCH ST",
    "city": "NORTH VANCOUVER",
    "phone": "604-982-0115"
  },
  {
    "name": "MITCHELL'S TOWING (VANCOUVER)",
    "name_print": "MITCHELL'S TOWING",
    "lot_address": "997 1ST AVE W",
    "city": "VANCOUVER",
    "phone": "604-982-0115"
  },
  {
    "name": "MONASHEE MOTORS",
    "name_print": "MONASHEE MOTORS",
    "lot_address": "3050 BIRCH RD",
    "city": "VALEMOUNT",
    "phone": "250-566-4318"
  },
  {
    "name": "MUNDIE'S TOWING (BURNABY)",
    "name_print": "MUNDIE'S TOWING",
    "lot_address": "6938 KINGSWAY",
    "city": "BURNABY",
    "phone": "604-526-9677"
  },
  {
    "name": "MUNDIE'S TOWING (COQUITLAM)",
    "name_print": "MUNDIE'S TOWING",
    "lot_address": "923 DELESTRE AVE",
    "city": "COQUITLAM",
    "phone": "604-298-1733"
  },
  {
    "name": "MUNDIE'S TOWING (DELTA)",
    "name_print": "MUNDIE'S TOWING",
    "lot_address": "9341 LADNER TRUNK RD",
    "city": "DELTA",
    "phone": "604-240-9706"
  },
  {
    "name": "MUNDIE'S TOWING (NEW WEST)",
    "name_print": "MUNDIE'S TOWING",
    "lot_address": "319 14 ST",
    "city": "NEW WESTMINSTER",
    "phone": "604-525-3535"
  },
  {
    "name": "MUNDIE'S TOWING (RICHMOND)",
    "name_print": "MUNDIE'S TOWING",
    "lot_address": "11211 BRIDGEPORT RD",
    "city": "RICHMOND",
    "phone": "604-278-0383"
  },
  {
    "name": "MUNDIE'S TOWING (SURREY)",
    "name_print": "MUNDIE'S TOWING",
    "lot_address": "19511 92 AVE",
    "city": "SURREY",
    "phone": "604-888-9633"
  },
  {
    "name": "MUNDIE'S TOWING (VANCOUVER)",
    "name_print": "MUNDIE'S TOWING",
    "lot_address": "1385 EAST KENT AVE N",
    "city": "VANCOUVER",
    "phone": "604-295-8638"
  },
  {
    "name": "NANOOSE BAY TOWING",
    "name_print": "NANOOSE BAY TOWING",
    "lot_address": "1130 DOBLER RD",
    "city": "PARKSVILLE",
    "phone": "250-468-9700"
  },
  {
    "name": "NORTH NAKUSP TOWING",
    "name_print": "NORTH NAKUSP TOW",
    "lot_address": "1350 13 AVE NW",
    "city": "NAKUSP",
    "phone": "250-265-2265"
  },
  {
    "name": "NORTH RIVER TOWING",
    "name_print": "NORTH RIVER TOWING",
    "lot_address": "5115 BARRIERE TOWN RD",
    "city": "BARRIERE",
    "phone": "250-672-0110"
  },
  {
    "name": "NORTHERN CAPITAL TOWING",
    "name_print": "NORTHERN TOWING",
    "lot_address": "1385 FOLEY CRES",
    "city": "PRINCE GEORGE",
    "phone": "250-563-6715"
  },
  {
    "name": "O'BRIEN'S SERVICE & REPAIRS",
    "name_print": "O'BRIEN'S SVC",
    "lot_address": "1007 HWY 23",
    "city": "NAKUSP",
    "phone": "250-265-4577"
  },
  {
    "name": "O'CONNOR MOTORS",
    "name_print": "O'CONNOR MOTORS",
    "lot_address": "44840 YALE RD",
    "city": "CHILLIWACK",
    "phone": "604-792-3170"
  },
  {
    "name": "OK REGION TOWING (PENTICTON)",
    "name_print": "OK REGION TOWING",
    "lot_address": "1898 DARTMOUTH RD",
    "city": "PENTICTON",
    "phone": "250-490-8697"
  },
  {
    "name": "OK REGION TOWING (SUMMERLAND)",
    "name_print": "OK REGION TOWING",
    "lot_address": "9403 CEDAR AVE",
    "city": "SUMMERLAND",
    "phone": "250-494-8697"
  },
  {
    "name": "ON CALL TOWING & TRAFFIC CONTROL",
    "name_print": "ON CALL TOWING",
    "lot_address": "851 YELLOWHEAD HWY S",
    "city": "CLEARWATER",
    "phone": "250-674-1869"
  },
  {
    "name": "PARKSVILLE TOWING",
    "name_print": "PARKSVILLE TOWING",
    "lot_address": "440 ISLAND HWY E",
    "city": "PARKSVILLE",
    "phone": "250-248-9913"
  },
  {
    "name": "PARTEL TOWING & RECOVERY",
    "name_print": "PARTEL TOWING",
    "lot_address": "5933 200 AVE",
    "city": "LANGLEY",
    "phone": "604-533-4044"
  },
  {
    "name": "PAYLESS TOWING (NORTH VAN)",
    "name_print": "PAYLESS TOWING",
    "lot_address": "301 MANSFIELD PL",
    "city": "NORTH VANCOUVER",
    "phone": "604-988-4176"
  },
  {
    "name": "PAYLESS TOWING (PEMBERTON)",
    "name_print": "PAYLESS TOWING",
    "lot_address": "1931 CARPENTER RD",
    "city": "PEMBERTON",
    "phone": "604-894-0024"
  },
  {
    "name": "PAYLESS TOWING (SQUAMISH)",
    "name_print": "PAYLESS TOWING",
    "lot_address": "1115 ENTERPRISE WAY",
    "city": "SQUAMISH",
    "phone": "604-892-5206"
  },
  {
    "name": "PAYLESS TOWING (WHISTLER)",
    "name_print": "PAYLESS TOWING",
    "lot_address": "1212 ALPHA LAKE RD",
    "city": "WHISTLER",
    "phone": "604-932-3222"
  },
  {
    "name": "PENINSULA TOWING",
    "name_print": "PENINSULA TOWING",
    "lot_address": "6678 BERTRAM PL",
    "city": "CENTRAL SAANICH",
    "phone": "250-656-6911"
  },
  {
    "name": "PENTICTON TOWING",
    "name_print": "PENTICTON TOWING",
    "lot_address": "1325 COMMERCIAL WAY",
    "city": "PENTICTON",
    "phone": "250-493-1991"
  },
  {
    "name": "PETRO CANADA TOWING",
    "name_print": "PETROCAN TOWING",
    "lot_address": "2040 PENINSULA RD",
    "city": "UCLUELET",
    "phone": "250-726-3832"
  },
  {
    "name": "PIONEER MOTORS",
    "name_print": "PIONEER MOTORS",
    "lot_address": "7387 PIONEER AVE",
    "city": "AGASSIZ",
    "phone": "604-796-9055"
  },
  {
    "name": "PIRATE TOWING",
    "name_print": "PIRATE TOWING",
    "lot_address": "417 TILLER RD",
    "city": "PENDER ISLAND",
    "phone": "250-538-7067"
  },
  {
    "name": "PRISM TOWING",
    "name_print": "PRISM TOWING",
    "lot_address": "1443 JADE AVE",
    "city": "QUESNEL",
    "phone": "250-992-8868"
  },
  {
    "name": "PRONTO TOWING",
    "name_print": "PRONTO TOWING",
    "lot_address": "2290 QUEENSWAY DR",
    "city": "TERRACE",
    "phone": "250-635-3113"
  },
  {
    "name": "PROTOW",
    "name_print": "PROTOW",
    "lot_address": "4505 23 AVE #1",
    "city": "VERNON",
    "phone": "250-549-2077"
  },
  {
    "name": "QUIRING MOTORS",
    "name_print": "QUIRING MOTORS",
    "lot_address": "26744 16 AVE",
    "city": "LANGLEY",
    "phone": "604-856-8721"
  },
  {
    "name": "RELIABLE TOWING (MERRITT)",
    "name_print": "RELIABLE TOWING",
    "lot_address": "1141 MCFARLANE WAY",
    "city": "MERRITT",
    "phone": "250-378-5000"
  },
  {
    "name": "RELIABLE TOWING (MISSION)",
    "name_print": "RELIABLE TOWING",
    "lot_address": "7143 WREN ST",
    "city": "MISSION",
    "phone": "604-826-8621"
  },
  {
    "name": "RELIABLE TOWING (PRINCETON)",
    "name_print": "RELIABLE TOWING",
    "lot_address": "233 DAVID BROWN WAY",
    "city": "PRINCETON",
    "phone": "250-378-5000"
  },
  {
    "name": "REZILLIANT TOWING (FORT NELSON)",
    "name_print": "REZILLIANT TOWING",
    "lot_address": "4900 44 AVE",
    "city": "FORT NELSON",
    "phone": "250-774-8697"
  },
  {
    "name": "REZILLIANT TOWING (FORT ST JOHN)",
    "name_print": "REZILLIANT TOWING",
    "lot_address": "10147 TUNDRA ST",
    "city": "FORT ST. JOHN",
    "phone": "250-793-7139"
  },
  {
    "name": "RICH BOYZ MECHANICAL",
    "name_print": "RICH BOYZ MECH",
    "lot_address": "1098 N E FRONTAGE RD",
    "city": "MCBRIDE",
    "phone": "250-569-2470"
  },
  {
    "name": "ROADHOUSE TOWING",
    "name_print": "ROADHOUSE TOWING",
    "lot_address": "517 TRANS CANADA HWY S",
    "city": "CACHE CREEK",
    "phone": "250-457-9594"
  },
  {
    "name": "ROADKILL TOWING",
    "name_print": "ROADKILL TOWING",
    "lot_address": "684 PLAZA RD",
    "city": "QUADRA ISLAND",
    "phone": "250-287-1686"
  },
  {
    "name": "ROADWAY TOWING",
    "name_print": "ROADWAY TOWING",
    "lot_address": "7391 PROGRESS PL",
    "city": "DELTA",
    "phone": "604-940-0329"
  },
  {
    "name": "ROBERT'S TOWING",
    "name_print": "ROBERT'S TOWING",
    "lot_address": "6233 WILDMARE RD",
    "city": "CHETWYND",
    "phone": "250-788-9194"
  },
  {
    "name": "RON'S TOWING",
    "name_print": "RON'S TOWING",
    "lot_address": "1360 FOLEY CRES",
    "city": "PRINCE GEORGE",
    "phone": "250-564-8444"
  },
  {
    "name": "RUPERT TOWING",
    "name_print": "RUPERT TOWING",
    "lot_address": "101 SHAWATLANS RD",
    "city": "PRINCE RUPERT",
    "phone": "250-624-4361"
  },
  {
    "name": "RUSTY'S TOWING",
    "name_print": "RUSTY'S TOWING",
    "lot_address": "15700 RIVER RD",
    "city": "RICHMOND",
    "phone": "604-273-1645"
  },
  {
    "name": "SCRAP KING AUTO WRECKING & TOWING (CRESTON)",
    "name_print": "SCRAP KING TOWING",
    "lot_address": "211 COLLIS ST",
    "city": "CRESTON",
    "phone": "250-428-2323"
  },
  {
    "name": "SCRAP KING AUTO WRECKING & TOWING (SALMO)",
    "name_print": "SCRAP KING TOWING",
    "lot_address": "1660 AIRPORT RD",
    "city": "SALMO",
    "phone": "250-357-2091"
  },
  {
    "name": "SKOOKUM TOWING",
    "name_print": "SKOOKUM TOWING",
    "lot_address": "414 FOUNTAIN VALLEY RD",
    "city": "LILLOOET",
    "phone": "250-256-4789"
  },
  {
    "name": "SMOKEY CREEK SALVAGE",
    "name_print": "SMOKEY CREEK SLVG",
    "lot_address": "3453 YEATMAN RD",
    "city": "SOUTH SLOCAN",
    "phone": "250-359-7815"
  },
  {
    "name": "SOOKE TOWING",
    "name_print": "SOOKE TOWING",
    "lot_address": "3366 OTTER POINT RD",
    "city": "SOOKE",
    "phone": "250-642-3171"
  },
  {
    "name": "SORRENTO TOWING & RECOVERY",
    "name_print": "SORRENTO TOWING",
    "lot_address": "2827 HILLTOP RD",
    "city": "SORRENTO",
    "phone": "250-833-7722"
  },
  {
    "name": "SPARWOOD TOWING (FERNIE)",
    "name_print": "SPARWOOD TOWING",
    "lot_address": "25 SHADOW DR",
    "city": "FERNIE",
    "phone": "250-425-2721"
  },
  {
    "name": "SPARWOOD TOWING (SPARWOOD)",
    "name_print": "SPARWOOD TOWING",
    "lot_address": "INDUSTRIAL 3 RD",
    "city": "SPARWOOD",
    "phone": "250-425-2721"
  },
  {
    "name": "SPECIALIZED TOWING",
    "name_print": "SPECIALIZED TOWING",
    "lot_address": "150 GLACIER ST",
    "city": "COQUITLAM",
    "phone": "604-209-9917"
  },
  {
    "name": "SPEEDWAY TOWING",
    "name_print": "SPEEDWAY TOWING",
    "lot_address": "755 WILLOW RD",
    "city": "VANDERHOOF",
    "phone": "250-570-8844"
  },
  {
    "name": "TERRY'S TOWING SERVICE",
    "name_print": "TERRY'S TOWING",
    "lot_address": "252 1ST AVE",
    "city": "TRAIL",
    "phone": "250-368-0070"
  },
  {
    "name": "THUNDER VALLEY TOWING",
    "name_print": "THUNDER VALLEY TOW",
    "lot_address": "1455 5TH AVE",
    "city": "MCBRIDE",
    "phone": "250-569-7007"
  },
  {
    "name": "TIGER TOWING",
    "name_print": "TIGER TOWING",
    "lot_address": "4860 TRANS CANADA HWY",
    "city": "DUNCAN",
    "phone": "250-701-8697"
  },
  {
    "name": "TJ'S TOWING & STORAGE",
    "name_print": "TJ'S TOWING",
    "lot_address": "1301 RAILWAY AVE",
    "city": "FERNIE",
    "phone": "250-423-1646"
  },
  {
    "name": "TLC AUTOMOTIVE SERVICES",
    "name_print": "TLC AUTO SVCS",
    "lot_address": "1963 COLLISON AVE",
    "city": "MASSET",
    "phone": "250-626-3756"
  },
  {
    "name": "TOTEM TOWING",
    "name_print": "TOTEM TOWING",
    "lot_address": "3333 TENNYSON AVE",
    "city": "VICTORIA",
    "phone": "250-475-3211"
  },
  {
    "name": "TYLER'S TOWING",
    "name_print": "TYLER'S TOWING",
    "lot_address": "3612 VICTORIA DR",
    "city": "SMITHERS",
    "phone": "250-847-2413"
  },
  {
    "name": "UNITOW (SURREY)",
    "name_print": "UNITOW",
    "lot_address": "13065 76 AVE",
    "city": "SURREY",
    "phone": "604-592-1255"
  },
  {
    "name": "UNITOW (VANCOUVER)",
    "name_print": "UNITOW",
    "lot_address": "1717 VERNON DR",
    "city": "VANCOUVER",
    "phone": "604-659-1255"
  },
  {
    "name": "VAN HORNE TOWING",
    "name_print": "VAN HORNE TOWING",
    "lot_address": "412 COBHAM AVE W",
    "city": "CRANBROOK",
    "phone": "250-426-4243"
  },
  {
    "name": "VERNON AUTO TOWING",
    "name_print": "VERNON AUTO TOWING",
    "lot_address": "4617B 34 ST",
    "city": "VERNON",
    "phone": "250-545-2311"
  },
  {
    "name": "WALLY'S AUTOBODY",
    "name_print": "WALLY'S AUTOBODY",
    "lot_address": "8832 YOUNG RD",
    "city": "CHILLIWACK",
    "phone": "604-795-9108"
  },
  {
    "name": "WALT'S TOWING",
    "name_print": "WALT'S TOWING",
    "lot_address": "694 GIBSONS WAY",
    "city": "GIBSONS",
    "phone": "604-886-9500"
  },
  {
    "name": "WARBRICK TOWING & SALVAGE",
    "name_print": "WARBRICK TOWING",
    "lot_address": "170 HWY 93/95",
    "city": "INVERMERE",
    "phone": "250-342-5851"
  },
  {
    "name": "WAYNE'S TOWING",
    "name_print": "WAYNE'S TOWING",
    "lot_address": "140 METLAKATLA RD",
    "city": "PRINCE RUPERT",
    "phone": "250-627-6166"
  },
  {
    "name": "WESTERN AUTOWRECKERS",
    "name_print": "WESTERN WRECKERS",
    "lot_address": "2374 GRANITE RD",
    "city": "NELSON",
    "phone": "250-354-4802"
  },
  {
    "name": "WESTSHORE TOWING",
    "name_print": "WESTSHORE TOWING",
    "lot_address": "1247 PARKDALE DR",
    "city": "VICTORIA",
    "phone": "250-474-1369"
  },
  {
    "name": "WHITE KNIGHT AUTO RESCUE",
    "name_print": "WHITE KNIGHT TOW",
    "lot_address": "601 BASS AVE",
    "city": "ENDERBY",
    "phone": "250-838-6402"
  },
  {
    "name": "WRENCH BENDER TOWING",
    "name_print": "WRENCH BENDER TOW",
    "lot_address": "8898 SHAUGHNESSY AVE",
    "city": "CANAL FLATS",
    "phone": "250-349-5655"
  },
  {
    "name": "ZIGGY'S TOWING",
    "name_print": "ZIGGY'S TOWING",
    "lot_address": "3558 VICTORIA DR",
    "city": "SMITHERS",
    "phone": "250-877-8687"
  }
]

old_data = [
	{
		"name" : "24 HOUR TOWING",
		"lot_address" : "728 PAYNE ST",
		"city" : "CRESTON",
		"phone" : "250-428-2323"
	},
	{
		"name" : "5 STAR TOWING",
		"lot_address" : "733 2ND AVE",
		"city" : "PRINCE GEORGE",
		"phone" : "250-614-9393"
	},
	{
		"name" : "A J TOWING",
		"lot_address" : "8945 NOWELL ST",
		"city" : "CHILLIWACK",
		"phone" : "604-795-3374"
	},
	{
		"name" : "A & M TOWING",
		"lot_address" : "305 MOORE AVE",
		"city" : "100 MILE HOUSE",
		"phone" : "250-395-4334"
	},
	{
		"name" : "ABLE TOWING",
		"lot_address" : "2384 210 RD",
		"city" : "DAWSON CREEK",
		"phone" : "250-782-4239"
	},
	{
		"name" : "AGGRESSIVE AUTO TOWING",
		"lot_address" : "34523 2ND AVE",
		"city" : "ABBOTSFORD",
		"phone" : "604-854-5669"
	},
	{
		"name" : "ALBERNI TOWING",
		"lot_address" : "2490 TIMBERLANE RD",
		"city" : "PORT ALBERNI",
		"phone" : "250-724-4050"
	},
	{
		"name" : "ALL COAST TOWING SERVICES",
		"lot_address" : "1178 STEWART RD",
		"city" : "GIBSONS",
		"phone" : "604-886-7280"
	},
	{
		"name" : "ALL-WAYS TOWING",
		"lot_address" : "647B DUPPLIN RD",
		"city" : "VICTORIA",
		"phone" : "250-381-0110"
	},
	{
		"name" : "ANCHORS AWAY TOWING",
		"lot_address" : "4068 NIMPKISH CRES",
		"city" : "WOSS",
		"phone" : "250-281-3483"
	},
	{
		"name" : "ANTLE TOWING",
		"lot_address" : "802 EXETER STATION RD",
		"city" : "LAC LA HACHE",
		"phone" : "250-396-7306"
	},
	{
		"name" : "APPLEWOOD TOWING",
		"lot_address" : "4800 BYNG RD",
		"city" : "PORT HARDY",
		"phone" : "250-949-6042"
	},
	{
		"name" : "ARCHIE'S TOWING",
		"lot_address" : "7496 OLD ALASKA HWY",
		"city" : "FORT NELSON",
		"phone" : "250-774-3054"
	},
	{
		"name" : "ARROWSMITH TOWING",
		"lot_address" : "20 HILLIERS RD",
		"city" : "QUALICUM BEACH",
		"phone" : "250-752-1662"
	},
	{
		"name" : "AURORA TOWING",
		"lot_address" : "2206 NADINA AVE N",
		"city" : "HOUSTON",
		"phone" : "250-845-7600"
	},
	{
		"name" : "AUTOW \/ QUESNEL TOWING",
		"lot_address" : "402 JUNIPER RD",
		"city" : "QUESNEL",
		"phone" : "250-992-9128"
	},
	{
		"name" : "BAILLIE'S TOWING",
		"lot_address" : "4833 GILBERT DR",
		"city" : "BARRIERE",
		"phone" : "250-672-9529"
	},
	{
		"name" : "BARRIERE AUTO & TRUCK TOW",
		"lot_address" : "4403 AIRFIELD RD",
		"city" : "BARRIERE",
		"phone" : "250-319-7767"
	},
	{
		"name" : "BAYVIEW AUTO TOWING",
		"lot_address" : "155 176 AVE #201",
		"city" : "SURREY",
		"phone" : "604-538-2032"
	},
	{
		"name" : "BEE JAY TOWING",
		"lot_address" : "765 MACKENZIE AVE N",
		"city" : "WILLIAMS LAKE",
		"phone" : "250-398-8311"
	},
	{
		"name" : "BEN'S TOWING",
		"lot_address" : "230 42 ST SW",
		"city" : "SALMON ARM",
		"phone" : "250-832-6512"
	},
	{
		"name" : "BKV TOWING",
		"lot_address" : "13200 BARTLETT RD",
		"city" : "BURNS LAKE",
		"phone" : "250-692-3413"
	},
	{
		"name" : "BLACK BEAR TOWING",
		"lot_address" : "1080 INDUSTRIAL WAY",
		"city" : "PARKSVILLE",
		"phone" : "250-468-1458"
	},
	{
		"name" : "BOWSER TOWING",
		"lot_address" : "6970 ISLAND HWY W",
		"city" : "BOWSER",
		"phone" : "250-757-8341"
	},
	{
		"name" : "BOYCE AUTO TOWING",
		"lot_address" : "15700 RIVER RD",
		"city" : "RICHMOND",
		"phone" : "604-278-1106"
	},
	{
		"name" : "BRIDGE LAKE TOWING",
		"lot_address" : "310 MOORE AVE",
		"city" : "100 MILE HOUSE",
		"phone" : "250-593-4056"
	},
	{
		"name" : "BUSTER'S TOWING",
		"lot_address" : "425 INDUSTRIAL AVE",
		"city" : "VANCOUVER",
		"phone" : "604-685-8181"
	},
	{
		"name" : "C A TOWING",
		"lot_address" : "13525 SUNSHINE COAST HWY",
		"city" : "MADEIRA PARK",
		"phone" : "604-740-1900"
	},
	{
		"name" : "CAPITAL TOWING & AUTO SERVICE",
		"lot_address" : "118 GYPSUM RD",
		"city" : "WHITEHORSE",
		"phone" : "867-667-2403"
	},
	{
		"name" : "CARE TOWING",
		"lot_address" : "4505 23 AVE",
		"city" : "VERNON",
		"phone" : "250-542-0207"
	},
	{
		"name" : "CARIBOO TOWING",
		"lot_address" : "750 MACKENZIE AVE S",
		"city" : "WILLIAMS LAKE",
		"phone" : "250-392-2888"
	},
	{
		"name" : "CARIBOU SERVICE",
		"lot_address" : "5549 BURTON FRONTAGE RD",
		"city" : "BURTON",
		"phone" : "250-265-3191"
	},
	{
		"name" : "CENTRAL TOWING",
		"lot_address" : "10930 WESTDOWN RD",
		"city" : "LADYSMITH",
		"phone" : "250-245-4411"
	},
	{
		"name" : "CHANOR TRUCK & AUTO REPAIR",
		"lot_address" : "1371 QUARTZ RD",
		"city" : "CACHE CREEK",
		"phone" : "250-457-6753"
	},
	{
		"name" : "CHARLOTTE TIRE",
		"lot_address" : "605 OCEAN VIEW DR",
		"city" : "QUEEN CHARLOTTE ISLAND",
		"phone" : "250-559-4641"
	},
	{
		"name" : "CHESNEY TOWING",
		"lot_address" : "8646 GAUDET RD",
		"city" : "POWELL RIVER",
		"phone" : "604-413-1457"
	},
	{
		"name" : "CHRISTINA LAKE TOWING",
		"lot_address" : "1648 MAIDA FRONTAGE RD",
		"city" : "CHRISTINA LAKE",
		"phone" : "250-442-9477"
	},
	{
		"name" : "CITY MOTORS",
		"lot_address" : "5951 ARBUTUS AVE",
		"city" : "POWELL RIVER",
		"phone" : "604-483-3210"
	},
	{
		"name" : "CITY OF NEW WEST TOWING",
		"lot_address" : "420 BOYNE ST",
		"city" : "NEW WESTMINSTER",
		"phone" : "604-519-1026"
	},
	{
		"name" : "CLASSIC TOWING (GOLDEN)",
		"lot_address" : "1025 11 AVE N",
		"city" : "GOLDEN",
		"phone" : "250-344-6659"
	},
	{
		"name" : "CLASSIC TOWING (REVELSTOKE)",
		"lot_address" : "2100 BIG EDDY RD",
		"city" : "REVELSTOKE",
		"phone" : "250-837-6216"
	},
	{
		"name" : "CLEARWATER TOWING",
		"lot_address" : "516 SWANSON AVE",
		"city" : "CLEARWATER",
		"phone" : "250-674-3123"
	},
	{
		"name" : "CLOVER TOWING",
		"lot_address" : "5340 192 AVE",
		"city" : "SURREY",
		"phone" : "604-513-1900"
	},
	{
		"name" : "CLUB TOWING & HEAVY RECOVERY",
		"lot_address" : "505 INDUSTRIAL RD #2",
		"city" : "INVERMERE",
		"phone" : "250-342-9551"
	},
	{
		"name" : "COASTLINE TOWING",
		"lot_address" : "1893 COULTER RD",
		"city" : "CAMPBELL RIVER",
		"phone" : "250-923-8111"
	},
	{
		"name" : "COLD COUNTRY TOWING (KIMBERLEY)",
		"lot_address" : "321 316 AVE",
		"city" : "KIMBERLY",
		"phone" : "250-426-3680"
	},
	{
		"name" : "COLD COUNTRY TOWING (CRANBROOK)",
		"lot_address" : "3584 COLLINSON RD",
		"city" : "CRANBROOK",
		"phone" : "250-426-3680"
	},
	{
		"name" : "COLLISION CRAFT",
		"lot_address" : "11129 115 AVE",
		"city" : "OSOYOOS",
		"phone" : "250-495-6331"
	},
	{
		"name" : "COLUMBIA TOWING (REVELSTOKE)",
		"lot_address" : "96 MACPHERSON AVE",
		"city" : "REVELSTOKE",
		"phone" : "250-837-9391"
	},
	{
		"name" : "COLUMBIA TOWING (SICAMOUS)",
		"lot_address" : "729 FRONTAGE RD",
		"city" : "SICAMOUS",
		"phone" : "250-836-2000"
	},
	{
		"name" : "COMOX VALLEY DODGE",
		"lot_address" : "2400 COUSINS RD",
		"city" : "COURTENAY",
		"phone" : "250-338-4665"
	},
	{
		"name" : "COOPER'S TOWING",
		"lot_address" : "1212 ALPHA LAKE RD",
		"city" : "WHISTLER",
		"phone" : "604-902-1930"
	},
	{
		"name" : "COQUITLAM TOWING",
		"lot_address" : "218 CAYER ST",
		"city" : "COQUITLAM",
		"phone" : "604-939-6474"
	},
	{
		"name" : "DAKOTA TOWING",
		"lot_address" : "1505 HARDY AVE",
		"city" : "KELOWNA",
		"phone" : "250-300-3999"
	},
	{
		"name" : "DALY'S TOWING",
		"lot_address" : "10514 YOUBOU RD",
		"city" : "YOUBOU",
		"phone" : "250-745-3433"
	},
	{
		"name" : "DAY & NITE TOWING",
		"lot_address" : "1933 FIELD RD",
		"city" : "SECHELT",
		"phone" : "604-885-0699"
	},
	{
		"name" : "DEL ORO TOWING",
		"lot_address" : "2535 JULIANN RD",
		"city" : "WEST KELOWNA",
		"phone" : "250-769-2100"
	},
	{
		"name" : "DIRECT TOWING",
		"lot_address" : "4513 44 AVE NE",
		"city" : "CHETWYND",
		"phone" : "250-788-3001"
	},
	{
		"name" : "DOLLAR TOWING",
		"lot_address" : "312B ENTERPRISE AVE",
		"city" : "KITIMAT",
		"phone" : "250-632-9947"
	},
	{
		"name" : "DON'S AUTO TOWING",
		"lot_address" : "671 ATHABASCA AVE",
		"city" : "KAMLOOPS",
		"phone" : "250-374-6281"
	},
	{
		"name" : "DOWNTOWN SERVICE & TOWING",
		"lot_address" : "750 MACKENZIE AVE S",
		"city" : "WILLIAMS LAKE",
		"phone" : "250-392-2888"
	},
	{
		"name" : "DRAKE TOWING",
		"lot_address" : "1553 POWELL AVE",
		"city" : "VANCOUVER",
		"phone" : "604-251-3344"
	},
	{
		"name" : "DUNN RIGHT TOWING & RECOVERY",
		"lot_address" : "691 MCPHEE AVE",
		"city" : "COURTENAY",
		"phone" : "250-650-8697"
	},
	{
		"name" : "DUNNMORE TOWING & RECOVERY",
		"lot_address" : "3447B ROYSTON RD",
		"city" : "COURTENAY",
		"phone" : "250-650-8224"
	},
	{
		"name" : "EAGLE EYE MARINE SERVICES",
		"lot_address" : "127 FULFORD-GANGES RD",
		"city" : "SALT SPRING ISLAND",
		"phone" : "250-883-7865"
	},
	{
		"name" : "EAGLE ROCK TOWING (ARMSTRONG)",
		"lot_address" : "1645 EAGLE ROCK RD",
		"city" : "ARMSTRONG",
		"phone" : "250-546-8290"
	},
	{
		"name" : "EAGLE ROCK TOWING (SALMON ARM)",
		"lot_address" : "5270 AUTO RD",
		"city" : "SALMON ARM",
		"phone" : "250-804-4442"
	},
	{
		"name" : "EAGLE ROCK TOWING (SICAMOUS)",
		"lot_address" : "901 TRANS CANADA HWY FRONTAGE RD",
		"city" : "SICAMOUS",
		"phone" : "250-836-0333"
	},
	{
		"name" : "EFM TOWING",
		"lot_address" : "741 INDUSTRIAL RD 2",
		"city" : "CRANBROOK",
		"phone" : "250-417-7334"
	},
	{
		"name" : "EISENKRIEN SERVICES",
		"lot_address" : "101 EXTENSION RD",
		"city" : "WONOWON",
		"phone" : "250-263-8733"
	},
	{
		"name" : "ENCORE TOWING & SERVICE",
		"lot_address" : "38926 PRODUCTION WAY",
		"city" : "SQUAMISH",
		"phone" : "604-892-5051"
	},
	{
		"name" : "EXCEPTIONAL TOWING & RECOVERY",
		"lot_address" : "1529 99 AVE",
		"city" : "DAWSON CREEK",
		"phone" : "250-782-4845"
	},
	{
		"name" : "FIRST CHOICE TOWING",
		"lot_address" : "10150 ALDER CRES",
		"city" : "FORT ST JOHN",
		"phone" : "250-785-2271"
	},
	{
		"name" : "FRASER LAKE TOWING",
		"lot_address" : "13936 HWY 16 W",
		"city" : "FRASER LAKE",
		"phone" : "250-699-6132"
	},
	{
		"name" : "FREIGHTLINER OF CRANBROOK",
		"lot_address" : "301 SLATER RD",
		"city" : "CRANBROOK",
		"phone" : "250-489-8781"
	},
	{
		"name" : "GAMMOND TOWING",
		"lot_address" : "31539 TELEGRAPH RD",
		"city" : "FORT FRASER",
		"phone" : "250-996-3377"
	},
	{
		"name" : "GARRICK AUTOMOTIVE",
		"lot_address" : "246 ALYMER RD",
		"city" : "CHASE",
		"phone" : "250-679-3167"
	},
	{
		"name" : "GATEWAY TOWING & RECOVERY",
		"lot_address" : "524 INDUSTRIAL PARK PL",
		"city" : "GOLD RIVER",
		"phone" : "250-283-9141"
	},
	{
		"name" : "GEM TOWING",
		"lot_address" : "2359 164 AVE",
		"city" : "WHITE ROCK",
		"phone" : "604-531-8765"
	},
	{
		"name" : "GEORGIA STRAIGHT TOWING",
		"lot_address" : "2317 COUSINS RD",
		"city" : "COURTENAY",
		"phone" : "250-338-9899"
	},
	{
		"name" : "GINO'S TOWING",
		"lot_address" : "296 OSILINKA DR",
		"city" : "PORT COQUITLAM",
		"phone" : "250-271-4466"
	},
	{
		"name" : "GIVER A YANK TOWING",
		"lot_address" : "611 STEWART ST E",
		"city" : "VANDERHOOF",
		"phone" : "250-570-0077"
	},
	{
		"name" : "GOOD SHEPHERD TOWING",
		"lot_address" : "230 SHELLY RD",
		"city" : "PARKSVILLE",
		"phone" : "250-248-3110"
	},
	{
		"name" : "GRANTON MOTORS",
		"lot_address" : "3335 HWY 3",
		"city" : "ROCK CREEK",
		"phone" : "250-446-2311"
	},
	{
		"name" : "GRASS CREEK VENTURES",
		"lot_address" : "415 HWY 37",
		"city" : "ISKUT",
		"phone" : "250-234-3434"
	},
	{
		"name" : "HOGIES TOWING",
		"lot_address" : "2310 KIRTON AVE",
		"city" : "ARMSTRONG",
		"phone" : "250-546-3472"
	},
	{
		"name" : "HOPE TOWING",
		"lot_address" : "1060 5TH AVE",
		"city" : "HOPE",
		"phone" : "604-869-3444"
	},
	{
		"name" : "IRWIN COLLISION REPAIRS",
		"lot_address" : "115 DESMOND CRESCENT",
		"city" : "SALT SPRING ISLAND",
		"phone" : "250-537-2513"
	},
	{
		"name" : "ISLAND THUNDER TOWING",
		"lot_address" : "1801 TWIN PEAKS RD",
		"city" : "PORT MCNEIL",
		"phone" : "250-956-2656"
	},
	{
		"name" : "J D TOWING",
		"lot_address" : "6585 INDUSTRIAL PARK WAY",
		"city" : "GRAND FORKS",
		"phone" : "250-442-2551"
	},
	{
		"name" : "JACK'S TOWING (ABBOTSFORD)",
		"lot_address" : "63 WEST RAILWAY",
		"city" : "ABBOTSFORD",
		"phone" : "604-607-0772"
	},
	{
		"name" : "JACK'S TOWING (MISSION)",
		"lot_address" : "7168 WREN ST",
		"city" : "MISSION",
		"phone" : "604-607-0772"
	},
	{
		"name" : "JAMIE DAVIS TOWING (GOLDEN)",
		"lot_address" : "920 KING PLACE",
		"city" : "GOLDEN",
		"phone" : "250-344-6690"
	},
	{
		"name" : "JAMIE DAVIS TOWING (HOPE)",
		"lot_address" : "19683 SILVER SKAGIT RD",
		"city" : "HOPE",
		"phone" : "604-869-8440"
	},
	{
		"name" : "JAY'S CUSTOM TOWING",
		"lot_address" : "341 KAIEN RD",
		"city" : "PRINCE RUPERT",
		"phone" : "250-624-8094"
	},
	{
		"name" : "JIMCO TOWING",
		"lot_address" : "3982 SQUILAX-ANGLEMONT RD",
		"city" : "SCOTCH CREEK",
		"phone" : "250-319-5250"
	},
	{
		"name" : "KBM AUTOWORKS & TOWING",
		"lot_address" : "1862 VERNON AVE",
		"city" : "LUMBY",
		"phone" : "250-547-2356"
	},
	{
		"name" : "KEEGZ SOUTH COUNTRY TOWING",
		"lot_address" : "1010 COMMERCIAL WAY",
		"city" : "GENELLE",
		"phone" : "250-693-8850"
	},
	{
		"name" : "KMB AUTOBODY",
		"lot_address" : "1527 TIE LAKE LOOP RD",
		"city" : "JAFFRAY",
		"phone" : "250-429-3413"
	},
	{
		"name" : "KOMAR TOWING",
		"lot_address" : "1300 TACHIE RD",
		"city" : "FORT ST JAMES",
		"phone" : "250-996-2206"
	},
	{
		"name" : "KOOL COUNTRY AUTO PARTS TOWING & RADS",
		"lot_address" : "150 INDUSTRIAL 2 RD #2",
		"city" : "INVERMERE",
		"phone" : "250-342-5188"
	},
	{
		"name" : "KOOTENAY TOWING",
		"lot_address" : "6635 HWY 31",
		"city" : "KASLO",
		"phone" : "250-353-2110"
	},
	{
		"name" : "L J'S TOWING & TRANSPORT",
		"lot_address" : "7519 TRANS CANADA HWY",
		"city" : "CHASE",
		"phone" : "250-679-8600"
	},
	{
		"name" : "LANE'S AUTO TOWING",
		"lot_address" : "258 GLEN RD",
		"city" : "AVOLA",
		"phone" : "250-678-2300"
	},
	{
		"name" : "LARSON TOWING",
		"lot_address" : "8590 GAUDET RD",
		"city" : "POWELL RIVER",
		"phone" : "604-316-8187"
	},
	{
		"name" : "LILLOOET AUTOBODY & TOWING",
		"lot_address" : "205 MAIN AVE",
		"city" : "LILLOOET",
		"phone" : "250-256-4687"
	},
	{
		"name" : "LITTLE MOUNTAIN TOWING",
		"lot_address" : "1130 DOBLER RD",
		"city" : "ERRINGTON",
		"phone" : "250-248-1132"
	},
	{
		"name" : "LONG BEACH TOWING",
		"lot_address" : "671 INDUSTRIAL WAY #3",
		"city" : "TOFINO",
		"phone" : "250-725-2030"
	},
	{
		"name" : "MAC'S TOWING (MISSION)",
		"lot_address" : "33201 LONDON AVE",
		"city" : "MISSION",
		"phone" : "604-826-9076"
	},
	{
		"name" : "MAC'S TOWING (NEW HAZELTON)",
		"lot_address" : "4167 15 AVE",
		"city" : "NEW HAZELTON",
		"phone" : "250-842-5404"
	},
	{
		"name" : "MAPLE RIDGE TOWING",
		"lot_address" : "23283 MCKAY AVE",
		"city" : "MAPLE RIDGE",
		"phone" : "604-463-5146"
	},
	{
		"name" : "MARIO'S TOWING (BOSTON BAR)",
		"lot_address" : "48150 TRANS CANADA HWY",
		"city" : "BOSTON BAR",
		"phone" : "250-295-1427"
	},
	{
		"name" : "MARIO'S TOWING (HOPE)",
		"lot_address" : "64211 FLOOD HOPE RD",
		"city" : "HOPE",
		"phone" : "604-860-0725"
	},
	{
		"name" : "MARIO'S TOWING (KAMLOOPS)",
		"lot_address" : "726 CARRIER AVE",
		"city" : "KAMLOOPS",
		"phone" : "888-292-6054"
	},
	{
		"name" : "MARIO'S TOWING (KELOWNA)",
		"lot_address" : "3015 SEXSMITH RD",
		"city" : "KELOWNA",
		"phone" : "250-765-6009"
	},
	{
		"name" : "MARIO'S TOWING (MERRITT)",
		"lot_address" : "2636 NICOLA AVE",
		"city" : "MERRITT",
		"phone" : "250-378-9241"
	},
	{
		"name" : "MARIO'S TOWING (PRINCETON)",
		"lot_address" : "401 HWY 3",
		"city" : "PRINCETON",
		"phone" : "888-292-6054"
	},
	{
		"name" : "MASSULLO MOTORS",
		"lot_address" : "4493 JOYCE AVE",
		"city" : "POWELL RIVER",
		"phone" : "604-485-7981"
	},
	{
		"name" : "MAYNE ISLAND TOWING",
		"lot_address" : "273 WOODDALE DR",
		"city" : "MAYNE ISLAND",
		"phone" : "250-508-8908"
	},
	{
		"name" : "MCBRIDE'S TOWING",
		"lot_address" : "9616 CHEMAINUS RD",
		"city" : "CHEMAINUS",
		"phone" : "250-246-3595"
	},
	{
		"name" : "ME & RON'S TOWING",
		"lot_address" : "178 KINGS LANE",
		"city" : "GANGES",
		"phone" : "250-537-9383"
	},
	{
		"name" : "MECHAM SALES & SERVICE",
		"lot_address" : "1843 MACKENZIE HWY",
		"city" : "HAGENSBORG",
		"phone" : "250-982-2345"
	},
	{
		"name" : "MID ISLAND TOWING",
		"lot_address" : "4900 JORDAN AVE",
		"city" : "NANAIMO",
		"phone" : "250-758-1728"
	},
	{
		"name" : "MID-NYTES TOWING",
		"lot_address" : "1835 COALCHUTE RD",
		"city" : "GRAND FORKS",
		"phone" : "250-442-2233"
	},
	{
		"name" : "MIKE'S AUTOMOTIVE SERVICES",
		"lot_address" : "37024 97 AVE",
		"city" : "OLIVER",
		"phone" : "250-498-2004"
	},
	{
		"name" : "MILL BAY TOWING",
		"lot_address" : "3855B TRANS CANADA HWY",
		"city" : "COBBLE HILL",
		"phone" : "250-743-1552"
	},
	{
		"name" : "MISSION TOWING (AGASSIZ)",
		"lot_address" : "7428 PIONEER AVE",
		"city" : "AGASSIZ",
		"phone" : "604-796-8697"
	},
	{
		"name" : "MISSION TOWING (MISSION)",
		"lot_address" : "7143 WREN ST",
		"city" : "MISSION",
		"phone" : "604-826-1251"
	},
	{
		"name" : "MITCHELL'S TOWING (VANCOUVER)",
		"lot_address" : "997 1ST AVE W",
		"city" : "VANCOUVER",
		"phone" : "604-982-0115"
	},
	{
		"name" : "MITCHELL'S TOWING (NORTH VAN)",
		"lot_address" : "1255 WELCH ST",
		"city" : "NORTH VANCOUVER",
		"phone" : "604-982-0115"
	},
	{
		"name" : "MODERN TIRE & TOWING",
		"lot_address" : "1756 #9 HWY",
		"city" : "AGASSIZ",
		"phone" : "604-796-2611"
	},
	{
		"name" : "MONASHEE MOTORS",
		"lot_address" : "3050 BIRCH RD",
		"city" : "VALEMOUNT",
		"phone" : "250-566-4318"
	},
	{
		"name" : "MUNDIE'S TOWING (BURNABY)",
		"lot_address" : "6938 KINGSWAY",
		"city" : "BURNABY",
		"phone" : "604-526-9677"
	},
	{
		"name" : "MUNDIE'S TOWING (COQUITLAM)",
		"lot_address" : "923 DELESTRE AVE",
		"city" : "COQUITLAM",
		"phone" : "604-298-1733"
	},
	{
		"name" : "MUNDIE'S TOWING (DELTA)",
		"lot_address" : "9341 LADNER TRUNK RD",
		"city" : "DELTA",
		"phone" : "604-240-9706"
	},
	{
		"name" : "MUNDIE'S TOWING (NEW WEST)",
		"lot_address" : "319 14 ST",
		"city" : "NEW WESTMINSTER",
		"phone" : "604-525-3535"
	},
	{
		"name" : "MUNDIE'S TOWING (RICHMOND)",
		"lot_address" : "11211 BRIDGEPORT RD",
		"city" : "RICHMOND",
		"phone" : "604-278-0383"
	},
	{
		"name" : "MUNDIE'S TOWING (SURREY)",
		"lot_address" : "19511 92 AVE",
		"city" : "SURREY",
		"phone" : "604-888-9633"
	},
	{
		"name" : "MUNDIE'S TOWING (VANCOUVER)",
		"lot_address" : "1385 EAST KENT AVE N",
		"city" : "VANCOUVER",
		"phone" : "604-295-8638"
	},
	{
		"name" : "MURAL TOWN AUTO SERVICE",
		"lot_address" : "3483 HENRY RD",
		"city" : "CHEMAINUS",
		"phone" : "250-246-3322"
	},
	{
		"name" : "NANOOSE BAY TOWING",
		"lot_address" : "1130 DOBLER RD",
		"city" : "PARKSVILLE",
		"phone" : "250-468-9700"
	},
	{
		"name" : "NORTH NAKUSP TOWING",
		"lot_address" : "1350 13 AVE NW",
		"city" : "NAKUSP",
		"phone" : "250-265-2265"
	},
	{
		"name" : "NORTH RIVER TOWING",
		"lot_address" : "5115 BARRIERE TOWN RD",
		"city" : "BARRIERE",
		"phone" : "250-672-0110"
	},
	{
		"name" : "NORTHERN CAPITAL TOWING",
		"lot_address" : "1385 FOLEY CRES",
		"city" : "PRINCE GEORGE",
		"phone" : "250-563-6715"
	},
	{
		"name" : "O'BRIEN'S SERVICE & REPAIRS",
		"lot_address" : "1007 HWY 23",
		"city" : "NAKUSP",
		"phone" : "250-265-4577"
	},
	{
		"name" : "O'CONNOR MOTORS",
		"lot_address" : "44840 YALE RD",
		"city" : "CHILLIWACK",
		"phone" : "604-792-3170"
	},
	{
		"name" : "OFF ROAD AUTO BODY",
		"lot_address" : "1901 HWY 99",
		"city" : "PEMBERTON",
		"phone" : "604-894-6767"
	},
	{
		"name" : "OK REGION TOWING (PENTICTON)",
		"lot_address" : "1898 DARTMOUTH RD",
		"city" : "PENTICTON",
		"phone" : "250-490-8697"
	},
	{
		"name" : "OK REGION TOWING (SUMMERLAND)",
		"lot_address" : "9403 CEDAR AVE",
		"city" : "SUMMERLAND",
		"phone" : "250-494-8697"
	},
	{
		"name" : "ON CALL TOWING & TRAFFIC CONTROL",
		"lot_address" : "851 YELLOWHEAD HWY S",
		"city" : "CLEARWATER",
		"phone" : "250-674-1869"
	},
	{
		"name" : "PARKSVILLE TOWING",
		"lot_address" : "440 ISLAND HWY E",
		"city" : "PARKSVILLE",
		"phone" : "250-248-9913"
	},
	{
		"name" : "PARTEL TOWING & RECOVERY",
		"lot_address" : "5933 200 AVE",
		"city" : "LANGLEY",
		"phone" : "604-533-4044"
	},
	{
		"name" : "PAYLESS TOWING (NORTH VAN)",
		"lot_address" : "301 MANSFIELD PL",
		"city" : "NORTH VANCOUVER",
		"phone" : "604-988-4176"
	},
	{
		"name" : "PAYLESS TOWING (PEMBERTON)",
		"lot_address" : "1931 CARPENTER RD",
		"city" : "PEMBERTON",
		"phone" : "604-894-0024"
	},
	{
		"name" : "PAYLESS TOWING (SQUAMISH)",
		"lot_address" : "1115 ENTERPRISE WAY",
		"city" : "SQUAMISH",
		"phone" : "604-892-5206"
	},
	{
		"name" : "PAYLESS TOWING (WHISTLER)",
		"lot_address" : "1212 ALPHA LAKE RD",
		"city" : "WHISTLER",
		"phone" : "604-932-3222"
	},
	{
		"name" : "PENINSULA TOWING",
		"lot_address" : "6678 BERTRAM PL",
		"city" : "SAANICHTON",
		"phone" : "250-656-6911"
	},
	{
		"name" : "PENTICTON TOWING",
		"lot_address" : "1325 COMMERCIAL WAY",
		"city" : "PENTICTON",
		"phone" : "250-493-1991"
	},
	{
		"name" : "PETRO CAN TOWING",
		"lot_address" : "2040 PENINSULA RD",
		"city" : "UCLUELET",
		"phone" : "250-726-3832"
	},
	{
		"name" : "PIONEER MOTORS",
		"lot_address" : "7387 PIONEER AVE",
		"city" : "AGASSIZ",
		"phone" : "604-796-9055"
	},
	{
		"name" : "PIRATE TOWING",
		"lot_address" : "417 TILLER RD",
		"city" : "PENDER ISLAND",
		"phone" : "250-538-7067"
	},
	{
		"name" : "POCO AUTO RESCUE & RECOVERY",
		"lot_address" : "10-2270 TYNER ST",
		"city" : "PORT COQUITLAM",
		"phone" : "604-933-4497"
	},
	{
		"name" : "PRISM TOWING",
		"lot_address" : "1443 JADE AVE",
		"city" : "QUESNEL",
		"phone" : "250-992-8868"
	},
	{
		"name" : "PRONTO TOWING",
		"lot_address" : "2290 QUEENSWAY DR",
		"city" : "TERRACE",
		"phone" : "250-635-3113"
	},
	{
		"name" : "PROTOW",
		"lot_address" : "4505 23 AVE #1",
		"city" : "VERNON",
		"phone" : "250-549-2077"
	},
	{
		"name" : "QUIRING MOTORS",
		"lot_address" : "26744 16 AVE",
		"city" : "ALDERGROVE",
		"phone" : "604-856-8721"
	},
	{
		"name" : "RELIABLE TOWING (MISSION)",
		"lot_address" : "7143 WREN ST",
		"city" : "MISSION",
		"phone" : "604-826-8621"
	},
	{
		"name" : "RELIABLE TOWING (MERRITT)",
		"lot_address" : "1141 MCFARLANE WAY",
		"city" : "MERRITT",
		"phone" : "250-378-5000"
	},
	{
		"name" : "REZILLIANT TOWING (FORT NELSON)",
		"lot_address" : "4900 44 AVE",
		"city" : "FORT NELSON",
		"phone" : "250-774-8697"
	},
	{
		"name" : "REZILLIANT TOWING (FORT ST JOHN)",
		"lot_address" : "10147 TUNDRA ST",
		"city" : "FORT ST JOHN",
		"phone" : "250-793-7139"
	},
	{
		"name" : "RICH BOYZ MECHANICAL",
		"lot_address" : "1098 N E FRONTAGE RD",
		"city" : "MCBRIDE",
		"phone" : "250-569-2470"
	},
	{
		"name" : "ROADHOUSE TOWING",
		"lot_address" : "517 TRANS CANADA HWY S",
		"city" : "CACHE CREEK",
		"phone" : "250-457-9594"
	},
	{
		"name" : "ROADKILL TOWING",
		"lot_address" : "684 PLAZA RD",
		"city" : "QUADRA ISLAND",
		"phone" : "250-287-1686"
	},
	{
		"name" : "ROADWAY TOWING",
		"lot_address" : "7391 PROGRESS PL",
		"city" : "DELTA",
		"phone" : "604-940-0329"
	},
	{
		"name" : "ROBERT'S TOWING",
		"lot_address" : "6233 WILDMARE RD",
		"city" : "CHETWYND",
		"phone" : "250-788-9194"
	},
	{
		"name" : "RON'S TOWING",
		"lot_address" : "1360 FOLEY CRES",
		"city" : "PRINCE GEORGE",
		"phone" : "250-564-8444"
	},
	{
		"name" : "ROOKZ'S AUTOBODY",
		"lot_address" : "1994 HWY 3",
		"city" : "FERNIE",
		"phone" : "250-423-7900"
	},
	{
		"name" : "RUPERT TOWING",
		"lot_address" : "101 SHAWATLAN RD",
		"city" : "PRINCE RUPERT",
		"phone" : "250-624-2722"
	},
	{
		"name" : "RUSTY'S TOWING",
		"lot_address" : "15700 RIVER RD",
		"city" : "RICHMOND",
		"phone" : "604-273-1645"
	},
	{
		"name" : "SCRAP KING AUTO WRECKING & TOWING",
		"lot_address" : "1660 AIRPORT RD",
		"city" : "SALMO",
		"phone" : "250-357-2091"
	},
	{
		"name" : "SEELEY LAKE SERVICE",
		"lot_address" : "3060 HWY 62",
		"city" : "HAZELTON",
		"phone" : "250-842-6465"
	},
	{
		"name" : "SKOOKUM TOWING",
		"lot_address" : "414 FOUNTAIN VALLEY RD",
		"city" : "LILLOOET",
		"phone" : "250-256-4789"
	},
	{
		"name" : "SMOKEY CREEK SALVAGE",
		"lot_address" : "3453 YEATMAN RD",
		"city" : "SOUTH SLOCAN",
		"phone" : "250-359-7815"
	},
	{
		"name" : "SOOKE TOWING",
		"lot_address" : "3366 OTTER POINT RD",
		"city" : "SOOKE",
		"phone" : "250-642-3171"
	},
	{
		"name" : "SORRENTO TOWING & RECOVERY",
		"lot_address" : "2827 HILLTOP RD",
		"city" : "SORRENTO",
		"phone" : "250-833-7722"
	},
	{
		"name" : "SOUTHVIEW AUTO TOWING",
		"lot_address" : "15700 RIVER RD",
		"city" : "RICHMOND",
		"phone" : "604-435-7211"
	},
	{
		"name" : "SPARWOOD TOWING (SPARWOOD)",
		"lot_address" : "INDUSTRIAL 3 RD",
		"city" : "SPARWOOD",
		"phone" : "250-425-2721"
	},
	{
		"name" : "SPARWOOD TOWING (FERNIE)",
		"lot_address" : "25 SHADOW DR",
		"city" : "FERNIE",
		"phone" : "250-425-2721"
	},
	{
		"name" : "SPECIALIZED TOWING",
		"lot_address" : "150 GLACIER ST",
		"city" : "COQUITLAM",
		"phone" : "604-209-9917"
	},
	{
		"name" : "SPEEDWAY TOWING",
		"lot_address" : "755 WILLOW RD",
		"city" : "VANDERHOOF",
		"phone" : "250-570-8844"
	},
	{
		"name" : "SUNSHINE COAST AUTO TOWING",
		"lot_address" : "5880 SECHELT INLET RD",
		"city" : "SECHELT",
		"phone" : "604-740-3939"
	},
	{
		"name" : "TERRY'S TOWING SERVICE",
		"lot_address" : "252 1ST AVE",
		"city" : "TRAIL",
		"phone" : "250-368-0070"
	},
	{
		"name" : "THUNDER VALLEY TOWING",
		"lot_address" : "1455 5TH AVE",
		"city" : "MCBRIDE",
		"phone" : "250-569-7007"
	},
	{
		"name" : "TIGER TOWING",
		"lot_address" : "4860 TRANS CANADA HWY",
		"city" : "DUNCAN",
		"phone" : "250-701-8697"
	},
	{
		"name" : "TJ'S TOWING & STORAGE",
		"lot_address" : "1301 RAILWAY AVE",
		"city" : "FERNIE",
		"phone" : "250-423-1646"
	},
	{
		"name" : "TLC AUTOMOTIVE SERVICES",
		"lot_address" : "1981 COLLISION AVE",
		"city" : "MASSET",
		"phone" : "250-626-3756"
	},
	{
		"name" : "TOTEM TOWING",
		"lot_address" : "3333 TENNYSON AVE",
		"city" : "VICTORIA",
		"phone" : "250-475-3211"
	},
	{
		"name" : "TYLER'S TOWING",
		"lot_address" : "3612 VICTORIA DR",
		"city" : "SMITHERS",
		"phone" : "250-847-2413"
	},
	{
		"name" : "UNITED TOWING SERVICES",
		"lot_address" : "1025 10 AVE NORTH",
		"city" : "GOLDEN",
		"phone" : "250-344-5900"
	},
	{
		"name" : "UNITOW (SURREY)",
		"lot_address" : "13065 76 AVE",
		"city" : "SURREY",
		"phone" : "604-592-1255"
	},
	{
		"name" : "UNITOW (VANCOUVER)",
		"lot_address" : "1717 VERNON DR",
		"city" : "VANCOUVER",
		"phone" : "604-659-1255"
	},
	{
		"name" : "USHER'S TOWING",
		"lot_address" : "101 11129 115 AVE",
		"city" : "OSOYOOS",
		"phone" : "250-495-7752"
	},
	{
		"name" : "VAN HORNE TOWING",
		"lot_address" : "412 COBHAM AVE W",
		"city" : "CRANBROOK",
		"phone" : "250-426-4243"
	},
	{
		"name" : "VERNON AUTO TOWING",
		"lot_address" : "4617B 34 AVE",
		"city" : "VERNON",
		"phone" : "250-545-2311"
	},
	{
		"name" : "WALLY'S AUTOBODY",
		"lot_address" : "8832 YOUNG RD",
		"city" : "CHILLIWACK",
		"phone" : "604-795-9108"
	},
	{
		"name" : "WALT'S TOWING",
		"lot_address" : "694 GIBSONS WAY",
		"city" : "GIBSONS",
		"phone" : "604-886-9500"
	},
	{
		"name" : "WARBRICK TOWING & SALVAGE",
		"lot_address" : "170 HWY 93\/95",
		"city" : "INVERMERE",
		"phone" : "250-342-5851"
	},
	{
		"name" : "WAYNE'S TOWING",
		"lot_address" : "140 METLAKATLA RD",
		"city" : "PRINCE RUPERT",
		"phone" : "250-627-6166"
	},
	{
		"name" : "WESTSHORE TOWING",
		"lot_address" : "1247 PARKDALE DR",
		"city" : "VICTORIA",
		"phone" : "250-474-1369"
	},
	{
		"name" : "WESTERN AUTOWRECKERS",
		"lot_address" : "2374 GRANITE RD",
		"city" : "NELSON",
		"phone" : "250-354-4802"
	},
	{
		"name" : "WHITE KNIGHT AUTO RESCUE",
		"lot_address" : "601 BASS AVE",
		"city" : "ENDERBY",
		"phone" : "250-838-6402"
	},
	{
		"name" : "WRENCH BENDER TOWING",
		"lot_address" : "8898 SHAUGHNESSY AVE",
		"city" : "CANAL FLATS",
		"phone" : "250-349-5655"
	},
	{
		"name" : "ZIGGY'S TOWING",
		"lot_address" : "3558 VICTORIA DR",
		"city" : "SMITHERS",
		"phone" : "250-877-8687"
	}
]

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('impound_lot_operator', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name_print', sa.String(), nullable=True))
    
    with op.get_context().autocommit_block():
        bind = op.get_bind()
        meta = sa.MetaData()
        meta.bind = bind
        meta.reflect(bind=bind, only=('impound_lot_operator',))
        impound_lot_operator = sa.Table('impound_lot_operator', meta)
        op.execute('DELETE FROM impound_lot_operator')
        op.bulk_insert(impound_lot_operator, new_data)
        
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('impound_lot_operator', schema=None) as batch_op:
        batch_op.drop_column('name_print')

    with op.get_context().autocommit_block():
        bind = op.get_bind()
        meta = sa.MetaData()
        meta.bind = bind
        meta.reflect(bind=bind, only=('impound_lot_operator',))
        impound_lot_operator = sa.Table('impound_lot_operator', meta)
        op.execute('DELETE FROM impound_lot_operator')
        op.bulk_insert(impound_lot_operator, old_data)
    # ### end Alembic commands ###
