"""empty message

Revision ID: dc0599cd958e
Revises: f76bbde02978
Create Date: 2023-11-23 09:27:12.436877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc0599cd958e'
down_revision = 'f76bbde02978'
branch_labels = None
depends_on = None

jurisdiction_cros_ref_data = [
  {
    "jurisdiction_code": "AD",
    "jurisdiction_name": "ANDORRA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "AE",
    "jurisdiction_name": "UNITED ARAB EMIRATES",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "AF",
    "jurisdiction_name": "AFGHANISTAN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENSE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "AG",
    "jurisdiction_name": "ANTIGUA & BARBUDA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "AI",
    "jurisdiction_name": "ANGUILLA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "ZZ",
    "icbc_jurisdiction": "UNITED KINGDOM",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "AL",
    "jurisdiction_name": "ALBANIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENSE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "AM",
    "jurisdiction_name": "ARMENIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "AN",
    "jurisdiction_name": "NETHERLANDS ANTILLES",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "AO",
    "jurisdiction_name": "ANGOLA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "AQ",
    "jurisdiction_name": "ANTARCTICA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "AR",
    "jurisdiction_name": "ARGENTINA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "AT",
    "jurisdiction_name": "AUSTRIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "AT",
    "icbc_jurisdiction": "AUSTRIA",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "AU",
    "jurisdiction_name": "AUSTRALIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "AW",
    "jurisdiction_name": "ARUBA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "AZ",
    "jurisdiction_name": "AZERBAIJAN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENSE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BA",
    "jurisdiction_name": "BOSNIA & HERZEGOVINA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BB",
    "jurisdiction_name": "BARBADOS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BD",
    "jurisdiction_name": "BANGLADESH",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BE",
    "jurisdiction_name": "BELGIUM",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BF",
    "jurisdiction_name": "BURKINA FASO",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BG",
    "jurisdiction_name": "BULGARIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BH",
    "jurisdiction_name": "BAHRAIN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BI",
    "jurisdiction_name": "BURUNDI",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BJ",
    "jurisdiction_name": "BENIN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BM",
    "jurisdiction_name": "BERMUDA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "ZZ",
    "icbc_jurisdiction": "UNITED KINGDOM",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BN",
    "jurisdiction_name": "BRUNEI DARUSSALAM",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BO",
    "jurisdiction_name": "BOLIVIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BR",
    "jurisdiction_name": "BRAZIL",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BS",
    "jurisdiction_name": "BAHAMAS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BT",
    "jurisdiction_name": "BHUTAN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BV",
    "jurisdiction_name": "BOUVET ISLAND",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BW",
    "jurisdiction_name": "BOTSWANA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BY",
    "jurisdiction_name": "BELARUS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "BZ",
    "jurisdiction_name": "BELIZE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "CA_AB",
    "jurisdiction_name": "ALBERTA",
    "prime_jurisdiction_code": "ALTA",
    "prime_jurisdiction_name": "ALBERTA",
    "icbc_jurisdiction_code": "AB",
    "icbc_jurisdiction": "ALBERTA",
    "vips_jurisdictions_objectCd": "AB",
    "vips_jurisdictions_objectDsc": "Alberta"
  },
  {
    "jurisdiction_code": "CA_BC",
    "jurisdiction_name": "BRITISH COLUMBIA",
    "prime_jurisdiction_code": "BC",
    "prime_jurisdiction_name": "BRITISH COLUMBIA",
    "icbc_jurisdiction_code": "BC",
    "icbc_jurisdiction": "BRITISH COLUMBIA",
    "vips_jurisdictions_objectCd": "BC",
    "vips_jurisdictions_objectDsc": "British Columbia"
  },
  {
    "jurisdiction_code": "CA_CF",
    "jurisdiction_name": "CANADIAN FORCES",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "CF",
    "icbc_jurisdiction": "CANADIAN FORCES",
    "vips_jurisdictions_objectCd": "CF",
    "vips_jurisdictions_objectDsc": "Canadian Forces"
  },
  {
    "jurisdiction_code": "CA_MB",
    "jurisdiction_name": "MANITOBA",
    "prime_jurisdiction_code": "MAN",
    "prime_jurisdiction_name": "MANITOBA",
    "icbc_jurisdiction_code": "MB",
    "icbc_jurisdiction": "MANITOBA",
    "vips_jurisdictions_objectCd": "MB",
    "vips_jurisdictions_objectDsc": "Manitoba"
  },
  {
    "jurisdiction_code": "CA_NB",
    "jurisdiction_name": "NEW BRUNSWICK",
    "prime_jurisdiction_code": "NB",
    "prime_jurisdiction_name": "NEW BRUNSWICK",
    "icbc_jurisdiction_code": "NB",
    "icbc_jurisdiction": "NEW BRUNSWICK",
    "vips_jurisdictions_objectCd": "NB",
    "vips_jurisdictions_objectDsc": "New Brunswick"
  },
  {
    "jurisdiction_code": "CA_NF",
    "jurisdiction_name": "NEWFOUNDLAND & LABRADOR",
    "prime_jurisdiction_code": "NFLD",
    "prime_jurisdiction_name": "NEWFOUNDLAND",
    "icbc_jurisdiction_code": "NF",
    "icbc_jurisdiction": "NEWFOUNDLAND",
    "vips_jurisdictions_objectCd": "NL",
    "vips_jurisdictions_objectDsc": "Newfoundland"
  },
  {
    "jurisdiction_code": "CA_NS",
    "jurisdiction_name": "NOVA SCOTIA",
    "prime_jurisdiction_code": "NS",
    "prime_jurisdiction_name": "NOVA SCOTIA",
    "icbc_jurisdiction_code": "NS",
    "icbc_jurisdiction": "NOVA SCOTIA",
    "vips_jurisdictions_objectCd": "NS",
    "vips_jurisdictions_objectDsc": "Nova Scotia"
  },
  {
    "jurisdiction_code": "CA_NT",
    "jurisdiction_name": "NORTHWEST TERRITORIES",
    "prime_jurisdiction_code": "NWT",
    "prime_jurisdiction_name": "NORTHWEST TERRITORY",
    "icbc_jurisdiction_code": "NT",
    "icbc_jurisdiction": "NORTHWEST TERRITORY",
    "vips_jurisdictions_objectCd": "NT",
    "vips_jurisdictions_objectDsc": "Northwest Territories"
  },
  {
    "jurisdiction_code": "CA_NU",
    "jurisdiction_name": "NUNAVUT",
    "prime_jurisdiction_code": "NVT",
    "prime_jurisdiction_name": "NUNAVUT",
    "icbc_jurisdiction_code": "NU",
    "icbc_jurisdiction": "NUNAVUT",
    "vips_jurisdictions_objectCd": "NU",
    "vips_jurisdictions_objectDsc": "Nunavut"
  },
  {
    "jurisdiction_code": "CA_ON",
    "jurisdiction_name": "ONTARIO",
    "prime_jurisdiction_code": "ONT",
    "prime_jurisdiction_name": "ONTARIO",
    "icbc_jurisdiction_code": "ON",
    "icbc_jurisdiction": "ONTARIO",
    "vips_jurisdictions_objectCd": "ON",
    "vips_jurisdictions_objectDsc": "Ontario"
  },
  {
    "jurisdiction_code": "CA_PE",
    "jurisdiction_name": "PRINCE EDWARD ISLAND",
    "prime_jurisdiction_code": "PEI",
    "prime_jurisdiction_name": "PRINCE EDWARD ISLAND",
    "icbc_jurisdiction_code": "PE",
    "icbc_jurisdiction": "PRINCE EDWARD ISLAND",
    "vips_jurisdictions_objectCd": "PE",
    "vips_jurisdictions_objectDsc": "Prince Edward Island"
  },
  {
    "jurisdiction_code": "CA_QC",
    "jurisdiction_name": "QUEBEC",
    "prime_jurisdiction_code": "QUE",
    "prime_jurisdiction_name": "QUEBEC",
    "icbc_jurisdiction_code": "QC",
    "icbc_jurisdiction": "QUEBEC",
    "vips_jurisdictions_objectCd": "QC",
    "vips_jurisdictions_objectDsc": "Quebec"
  },
  {
    "jurisdiction_code": "CA_SK",
    "jurisdiction_name": "SASKATCHEWAN",
    "prime_jurisdiction_code": "SASK",
    "prime_jurisdiction_name": "SASKATCHEWAN",
    "icbc_jurisdiction_code": "SK",
    "icbc_jurisdiction": "SASKATCHEWAN",
    "vips_jurisdictions_objectCd": "SK",
    "vips_jurisdictions_objectDsc": "Saskatchewan"
  },
  {
    "jurisdiction_code": "CA_YT",
    "jurisdiction_name": "YUKON",
    "prime_jurisdiction_code": "YT",
    "prime_jurisdiction_name": "YUKON TERRITORY",
    "icbc_jurisdiction_code": "YT",
    "icbc_jurisdiction": "YUKON TERRITORY",
    "vips_jurisdictions_objectCd": "YT",
    "vips_jurisdictions_objectDsc": "Yukon Territory"
  },
  {
    "jurisdiction_code": "CC",
    "jurisdiction_name": "COCOS (KEELING) ISLANDS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "CF",
    "jurisdiction_name": "CENTRAL AFRICAN REPUBLIC",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "CG",
    "jurisdiction_name": "CONGO",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "CH",
    "jurisdiction_name": "SWITZERLAND",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "CH",
    "icbc_jurisdiction": "SWITZERLAND",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "CI",
    "jurisdiction_name": "COTE D'IVOIRE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "CK",
    "jurisdiction_name": "COOK ISLANDS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "CL",
    "jurisdiction_name": "CHILE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "CM",
    "jurisdiction_name": "CAMEROON",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "CN",
    "jurisdiction_name": "CHINA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "CO",
    "jurisdiction_name": "COLOMBIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "CR",
    "jurisdiction_name": "COSTA RICA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "CU",
    "jurisdiction_name": "CUBA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "CV",
    "jurisdiction_name": "CAPE VERDE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "CX",
    "jurisdiction_name": "CHRISTMAS ISLAND",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "CY",
    "jurisdiction_name": "CYPRUS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "CZ",
    "jurisdiction_name": "CZECH REPUBLIC",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "DE",
    "jurisdiction_name": "GERMANY",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "DL",
    "icbc_jurisdiction": "GERMANY",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "DJ",
    "jurisdiction_name": "DJIBOUTI",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "DK",
    "jurisdiction_name": "DENMARK",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "DM",
    "jurisdiction_name": "DOMINICA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "DO",
    "jurisdiction_name": "DOMINICAN REPUBLIC",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "DZ",
    "jurisdiction_name": "ALGERIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENSE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "EC",
    "jurisdiction_name": "ECUADOR",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "EE",
    "jurisdiction_name": "ESTONIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "EG",
    "jurisdiction_name": "EGYPT",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "EH",
    "jurisdiction_name": "WESTERN SAHARA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "ER",
    "jurisdiction_name": "ERITREA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "ES",
    "jurisdiction_name": "SPAIN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "ET",
    "jurisdiction_name": "ETHIOPIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "FI",
    "jurisdiction_name": "FINLAND",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "FJ",
    "jurisdiction_name": "FIJI",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "FK",
    "jurisdiction_name": "FALKLAND ISLANDS (MALVINAS)",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "ZZ",
    "icbc_jurisdiction": "UNITED KINGDOM",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "FM",
    "jurisdiction_name": "MICRONESIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "FO",
    "jurisdiction_name": "FAROE ISLANDS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "FR",
    "jurisdiction_name": "FRANCE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FR",
    "icbc_jurisdiction": "FRANCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GA",
    "jurisdiction_name": "GABON",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GB",
    "jurisdiction_name": "UNITED KINGDOM",
    "prime_jurisdiction_code": "UK",
    "prime_jurisdiction_name": "UNITED KINGDOM",
    "icbc_jurisdiction_code": "ZZ",
    "icbc_jurisdiction": "UNITED KINGDOM",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GD",
    "jurisdiction_name": "GRENADA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GE",
    "jurisdiction_name": "GEORGIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GF",
    "jurisdiction_name": "FRENCH GUIANA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FR",
    "icbc_jurisdiction": "FRANCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GH",
    "jurisdiction_name": "GHANA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GI",
    "jurisdiction_name": "GIBRALTAR",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "ZZ",
    "icbc_jurisdiction": "UNITED KINGDOM",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GL",
    "jurisdiction_name": "GREENLAND",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GM",
    "jurisdiction_name": "GAMBIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GN",
    "jurisdiction_name": "GUINEA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GP",
    "jurisdiction_name": "GUADELOUPE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FR",
    "icbc_jurisdiction": "FRANCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GQ",
    "jurisdiction_name": "EQUATORIAL GUINEA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GR",
    "jurisdiction_name": "GREECE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GS",
    "jurisdiction_name": "SOUTH GEORGIA & THE SOUTH SANDWICH ISLANDS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GT",
    "jurisdiction_name": "GUATEMALA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GW",
    "jurisdiction_name": "GUINEA-BISSAU",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "GY",
    "jurisdiction_name": "GUYANA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "HK",
    "jurisdiction_name": "HONG KONG",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "HM",
    "jurisdiction_name": "HEARD & MCDONALD ISLANDS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "HN",
    "jurisdiction_name": "HONDURAS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "HR",
    "jurisdiction_name": "CROATIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "HT",
    "jurisdiction_name": "HAITI",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "HU",
    "jurisdiction_name": "HUNGARY",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "ID",
    "jurisdiction_name": "INDONESIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "IE",
    "jurisdiction_name": "IRELAND",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "IL",
    "jurisdiction_name": "ISRAEL",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "IN",
    "jurisdiction_name": "INDIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "IO",
    "jurisdiction_name": "BRITISH INDIAN OCEAN TERRITORY",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "IQ",
    "jurisdiction_name": "IRAQ",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "IR",
    "jurisdiction_name": "IRAN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "IS",
    "jurisdiction_name": "ICELAND",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "IT",
    "jurisdiction_name": "ITALY",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "JM",
    "jurisdiction_name": "JAMAICA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "JO",
    "jurisdiction_name": "JORDAN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "JP",
    "jurisdiction_name": "JAPAN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "JA",
    "icbc_jurisdiction": "JAPAN",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "KE",
    "jurisdiction_name": "KENYA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "KG",
    "jurisdiction_name": "KYRGYZSTAN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "KH",
    "jurisdiction_name": "CAMBODIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "KI",
    "jurisdiction_name": "KIRIBATI",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "KM",
    "jurisdiction_name": "COMOROS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "KN",
    "jurisdiction_name": "ST. KITTS & NEVIS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "KP",
    "jurisdiction_name": "NORTH KOREA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "KR",
    "jurisdiction_name": "SOUTH KOREA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "KR",
    "icbc_jurisdiction": "REPUBLIC OF KOREA",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "KW",
    "jurisdiction_name": "KUWAIT",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "KY",
    "jurisdiction_name": "CAYMAN ISLANDS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "ZZ",
    "icbc_jurisdiction": "UNITED KINGDOM",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "KZ",
    "jurisdiction_name": "KAZAKHSTAN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "LA",
    "jurisdiction_name": "LAOS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "LB",
    "jurisdiction_name": "LEBANON",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "LC",
    "jurisdiction_name": "ST. LUCIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "LI",
    "jurisdiction_name": "LIECHTENSTEIN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "LK",
    "jurisdiction_name": "SRI LANKA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "LR",
    "jurisdiction_name": "LIBERIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "LS",
    "jurisdiction_name": "LESOTHO",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "LT",
    "jurisdiction_name": "LITHUANIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "LU",
    "jurisdiction_name": "LUXEMBOURG",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "LV",
    "jurisdiction_name": "LATVIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "LY",
    "jurisdiction_name": "LIBYA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MA",
    "jurisdiction_name": "MOROCCO",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MC",
    "jurisdiction_name": "MONACO",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MD",
    "jurisdiction_name": "MOLDOVA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MG",
    "jurisdiction_name": "MADAGASCAR",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MH",
    "jurisdiction_name": "MARSHALL ISLANDS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MK",
    "jurisdiction_name": "MACEDONIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "ML",
    "jurisdiction_name": "MALI",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MM",
    "jurisdiction_name": "MYANMAR",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MN",
    "jurisdiction_name": "MONGOLIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MO",
    "jurisdiction_name": "MACAU",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MQ",
    "jurisdiction_name": "MARTINIQUE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FR",
    "icbc_jurisdiction": "FRANCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MR",
    "jurisdiction_name": "MAURITANIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MS",
    "jurisdiction_name": "MONTSERRAT",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "ZZ",
    "icbc_jurisdiction": "UNITED KINGDOM",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MT",
    "jurisdiction_name": "MALTA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MU",
    "jurisdiction_name": "MAURITIUS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MV",
    "jurisdiction_name": "MALDIVES",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MW",
    "jurisdiction_name": "MALAWI",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MX",
    "jurisdiction_name": "MEXICO",
    "prime_jurisdiction_code": "MX",
    "prime_jurisdiction_name": "MEXICO",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "MX",
    "vips_jurisdictions_objectDsc": "Mexico"
  },
  {
    "jurisdiction_code": "MY",
    "jurisdiction_name": "MALAYSIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "MZ",
    "jurisdiction_name": "MOZAMBIQUE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "NA",
    "jurisdiction_name": "NAMIBIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "NC",
    "jurisdiction_name": "NEW CALEDONIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FR",
    "icbc_jurisdiction": "FRANCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "NE",
    "jurisdiction_name": "NIGER",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "NF",
    "jurisdiction_name": "NORFOLK ISLAND",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "NG",
    "jurisdiction_name": "NIGERIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "NI",
    "jurisdiction_name": "NICARAGUA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "NL",
    "jurisdiction_name": "NETHERLANDS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "NO",
    "jurisdiction_name": "NORWAY",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "NP",
    "jurisdiction_name": "NEPAL",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "NR",
    "jurisdiction_name": "NAURU",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "NU",
    "jurisdiction_name": "NIUE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "NZ",
    "jurisdiction_name": "NEW ZEALAND",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "OM",
    "jurisdiction_name": "OMAN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "PA",
    "jurisdiction_name": "PANAMA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "PE",
    "jurisdiction_name": "PERU",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "PF",
    "jurisdiction_name": "FRENCH POLYNESIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FR",
    "icbc_jurisdiction": "FRANCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "PG",
    "jurisdiction_name": "PAPUA NEW GUINEA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "PH",
    "jurisdiction_name": "PHILIPPINES",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "PK",
    "jurisdiction_name": "PAKISTAN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "PL",
    "jurisdiction_name": "POLAND",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "PM",
    "jurisdiction_name": "ST. PIERRE & MIQUELON",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FR",
    "icbc_jurisdiction": "FRANCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "PN",
    "jurisdiction_name": "PITCAIRN ISLANDS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "ZZ",
    "icbc_jurisdiction": "UNITED KINGDOM",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "PT",
    "jurisdiction_name": "PORTUGAL",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "PW",
    "jurisdiction_name": "PALAU",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "PY",
    "jurisdiction_name": "PARAGUAY",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "QA",
    "jurisdiction_name": "QATAR",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "RE",
    "jurisdiction_name": "REUNION",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FR",
    "icbc_jurisdiction": "FRANCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "RO",
    "jurisdiction_name": "ROMANIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "RU",
    "jurisdiction_name": "RUSSIAN FEDERATION",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "RW",
    "jurisdiction_name": "RWANDA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SA",
    "jurisdiction_name": "SAUDI ARABIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SB",
    "jurisdiction_name": "SOLOMON ISLANDS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SC",
    "jurisdiction_name": "SEYCHELLES",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SD",
    "jurisdiction_name": "SUDAN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SE",
    "jurisdiction_name": "SWEDEN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SG",
    "jurisdiction_name": "SINGAPORE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SH",
    "jurisdiction_name": "ST. HELENA, ASCENSION & TRISTAN DA CUNHA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "ZZ",
    "icbc_jurisdiction": "UNITED KINGDOM",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SI",
    "jurisdiction_name": "SLOVENIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SJ",
    "jurisdiction_name": "SVALBARD & JAN MAYEN ISLANDS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SK",
    "jurisdiction_name": "SLOVAKIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SL",
    "jurisdiction_name": "SIERRA LEONE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SM",
    "jurisdiction_name": "SAN MARINO",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SN",
    "jurisdiction_name": "SENEGAL",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SO",
    "jurisdiction_name": "SOMALIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SR",
    "jurisdiction_name": "SURINAME",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "ST",
    "jurisdiction_name": "SAO TOME & PRINCIPE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SV",
    "jurisdiction_name": "EL SALVADOR",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SY",
    "jurisdiction_name": "SYRIAN ARAB REPUBLIC",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "SZ",
    "jurisdiction_name": "SWAZILAND",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "TC",
    "jurisdiction_name": "TURKS & CAICOS ISLANDS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "ZZ",
    "icbc_jurisdiction": "UNITED KINGDOM",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "TD",
    "jurisdiction_name": "CHAD",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "TF",
    "jurisdiction_name": "FRENCH SOUTHERN & ANTARCTIC LANDS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FR",
    "icbc_jurisdiction": "FRANCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "TG",
    "jurisdiction_name": "TOGO",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "TH",
    "jurisdiction_name": "THAILAND",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "TJ",
    "jurisdiction_name": "TAJIKISTAN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "TK",
    "jurisdiction_name": "TOKELAU",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "TM",
    "jurisdiction_name": "TURKMENISTAN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "TN",
    "jurisdiction_name": "TUNISIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "TO",
    "jurisdiction_name": "TONGA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "TP",
    "jurisdiction_name": "EAST TIMOR",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "TR",
    "jurisdiction_name": "TURKEY",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "TT",
    "jurisdiction_name": "TRINIDAD & TOBAGO",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "TV",
    "jurisdiction_name": "TUVALU",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "TW",
    "jurisdiction_name": "TAIWAN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "TZ",
    "jurisdiction_name": "TANZANIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "UA",
    "jurisdiction_name": "UKRAINE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "UG",
    "jurisdiction_name": "UGANDA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "US_AK",
    "jurisdiction_name": "ALASKA",
    "prime_jurisdiction_code": "AK",
    "prime_jurisdiction_name": "ALASKA",
    "icbc_jurisdiction_code": "AK",
    "icbc_jurisdiction": "ALASKA",
    "vips_jurisdictions_objectCd": "AK",
    "vips_jurisdictions_objectDsc": "Alaska"
  },
  {
    "jurisdiction_code": "US_AL",
    "jurisdiction_name": "ALABAMA",
    "prime_jurisdiction_code": "AL",
    "prime_jurisdiction_name": "ALABAMA",
    "icbc_jurisdiction_code": "AL",
    "icbc_jurisdiction": "ALABAMA",
    "vips_jurisdictions_objectCd": "AL",
    "vips_jurisdictions_objectDsc": "Alabama"
  },
  {
    "jurisdiction_code": "US_AR",
    "jurisdiction_name": "ARKANSAS",
    "prime_jurisdiction_code": "AR",
    "prime_jurisdiction_name": "ARKANSAS",
    "icbc_jurisdiction_code": "AR",
    "icbc_jurisdiction": "ARKANSAS",
    "vips_jurisdictions_objectCd": "AR",
    "vips_jurisdictions_objectDsc": "Arkansas"
  },
  {
    "jurisdiction_code": "US_AS",
    "jurisdiction_name": "AMERICAN SAMOA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "XX",
    "vips_jurisdictions_objectDsc": "Unknown"
  },
  {
    "jurisdiction_code": "US_AZ",
    "jurisdiction_name": "ARIZONA",
    "prime_jurisdiction_code": "AZ",
    "prime_jurisdiction_name": "ARIZONA",
    "icbc_jurisdiction_code": "AZ",
    "icbc_jurisdiction": "ARIZONA",
    "vips_jurisdictions_objectCd": "AZ",
    "vips_jurisdictions_objectDsc": "Arizona"
  },
  {
    "jurisdiction_code": "US_CA",
    "jurisdiction_name": "CALIFORNIA",
    "prime_jurisdiction_code": "CA",
    "prime_jurisdiction_name": "CALIFORNIA",
    "icbc_jurisdiction_code": "CA",
    "icbc_jurisdiction": "CALIFORNIA",
    "vips_jurisdictions_objectCd": "CA",
    "vips_jurisdictions_objectDsc": "California"
  },
  {
    "jurisdiction_code": "US_CO",
    "jurisdiction_name": "COLORADO",
    "prime_jurisdiction_code": "CO",
    "prime_jurisdiction_name": "COLORADO",
    "icbc_jurisdiction_code": "CO",
    "icbc_jurisdiction": "COLORADO",
    "vips_jurisdictions_objectCd": "CO",
    "vips_jurisdictions_objectDsc": "Colorado"
  },
  {
    "jurisdiction_code": "US_CT",
    "jurisdiction_name": "CONNECTICUT",
    "prime_jurisdiction_code": "CT",
    "prime_jurisdiction_name": "CONNECTICUT",
    "icbc_jurisdiction_code": "CT",
    "icbc_jurisdiction": "CONNECTICUT",
    "vips_jurisdictions_objectCd": "CT",
    "vips_jurisdictions_objectDsc": "Connecticut"
  },
  {
    "jurisdiction_code": "US_DC",
    "jurisdiction_name": "DISTRICT OF COLUMBIA",
    "prime_jurisdiction_code": "DC",
    "prime_jurisdiction_name": "DISTRICT OF COLUMBIA",
    "icbc_jurisdiction_code": "DC",
    "icbc_jurisdiction": "DISTRICT OF COLUMBIA",
    "vips_jurisdictions_objectCd": "DC",
    "vips_jurisdictions_objectDsc": "District of Columbia"
  },
  {
    "jurisdiction_code": "US_DE",
    "jurisdiction_name": "DELAWARE",
    "prime_jurisdiction_code": "DE",
    "prime_jurisdiction_name": "DELAWARE",
    "icbc_jurisdiction_code": "DE",
    "icbc_jurisdiction": "DELAWARE",
    "vips_jurisdictions_objectCd": "DE",
    "vips_jurisdictions_objectDsc": "Delaware"
  },
  {
    "jurisdiction_code": "US_FL",
    "jurisdiction_name": "FLORIDA",
    "prime_jurisdiction_code": "FL",
    "prime_jurisdiction_name": "FLORIDA",
    "icbc_jurisdiction_code": "FL",
    "icbc_jurisdiction": "FLORIDA",
    "vips_jurisdictions_objectCd": "FL",
    "vips_jurisdictions_objectDsc": "Florida"
  },
  {
    "jurisdiction_code": "US_GA",
    "jurisdiction_name": "GEORGIA",
    "prime_jurisdiction_code": "GA",
    "prime_jurisdiction_name": "GEORGIA",
    "icbc_jurisdiction_code": "GA",
    "icbc_jurisdiction": "GEORGIA",
    "vips_jurisdictions_objectCd": "GA",
    "vips_jurisdictions_objectDsc": "Georgia"
  },
  {
    "jurisdiction_code": "US_GU",
    "jurisdiction_name": "GUAM",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "ZZ",
    "icbc_jurisdiction": "OTHER",
    "vips_jurisdictions_objectCd": "XX",
    "vips_jurisdictions_objectDsc": "Unknown"
  },
  {
    "jurisdiction_code": "US_HI",
    "jurisdiction_name": "HAWAII",
    "prime_jurisdiction_code": "HI",
    "prime_jurisdiction_name": "HAWAII",
    "icbc_jurisdiction_code": "HI",
    "icbc_jurisdiction": "HAWAII",
    "vips_jurisdictions_objectCd": "HI",
    "vips_jurisdictions_objectDsc": "Hawaii"
  },
  {
    "jurisdiction_code": "US_IA",
    "jurisdiction_name": "IOWA",
    "prime_jurisdiction_code": "IA",
    "prime_jurisdiction_name": "IOWA",
    "icbc_jurisdiction_code": "IA",
    "icbc_jurisdiction": "IOWA",
    "vips_jurisdictions_objectCd": "IA",
    "vips_jurisdictions_objectDsc": "Iowa"
  },
  {
    "jurisdiction_code": "US_ID",
    "jurisdiction_name": "IDAHO",
    "prime_jurisdiction_code": "ID",
    "prime_jurisdiction_name": "IDAHO",
    "icbc_jurisdiction_code": "ID",
    "icbc_jurisdiction": "IDAHO",
    "vips_jurisdictions_objectCd": "ID",
    "vips_jurisdictions_objectDsc": "Idaho"
  },
  {
    "jurisdiction_code": "US_IL",
    "jurisdiction_name": "ILLINOIS",
    "prime_jurisdiction_code": "IL",
    "prime_jurisdiction_name": "ILLINOIS",
    "icbc_jurisdiction_code": "IL",
    "icbc_jurisdiction": "ILLINOIS",
    "vips_jurisdictions_objectCd": "IL",
    "vips_jurisdictions_objectDsc": "Illinois"
  },
  {
    "jurisdiction_code": "US_IN",
    "jurisdiction_name": "INDIANA",
    "prime_jurisdiction_code": "IN",
    "prime_jurisdiction_name": "INDIANA",
    "icbc_jurisdiction_code": "IN",
    "icbc_jurisdiction": "INDIANA",
    "vips_jurisdictions_objectCd": "IN",
    "vips_jurisdictions_objectDsc": "Indiana"
  },
  {
    "jurisdiction_code": "US_KS",
    "jurisdiction_name": "KANSAS",
    "prime_jurisdiction_code": "KS",
    "prime_jurisdiction_name": "KANSAS",
    "icbc_jurisdiction_code": "KS",
    "icbc_jurisdiction": "KANSAS",
    "vips_jurisdictions_objectCd": "KS",
    "vips_jurisdictions_objectDsc": "Kansas"
  },
  {
    "jurisdiction_code": "US_KY",
    "jurisdiction_name": "KENTUCKY",
    "prime_jurisdiction_code": "KY",
    "prime_jurisdiction_name": "KENTUCKY",
    "icbc_jurisdiction_code": "KY",
    "icbc_jurisdiction": "KENTUCKY",
    "vips_jurisdictions_objectCd": "KY",
    "vips_jurisdictions_objectDsc": "Kentucky"
  },
  {
    "jurisdiction_code": "US_LA",
    "jurisdiction_name": "LOUISIANA",
    "prime_jurisdiction_code": "LA",
    "prime_jurisdiction_name": "LOUISIANA",
    "icbc_jurisdiction_code": "LA",
    "icbc_jurisdiction": "LOUISIANA",
    "vips_jurisdictions_objectCd": "LA",
    "vips_jurisdictions_objectDsc": "Louisiana"
  },
  {
    "jurisdiction_code": "US_MA",
    "jurisdiction_name": "MASSACHUSETTS",
    "prime_jurisdiction_code": "MA",
    "prime_jurisdiction_name": "MASSACHUSETTS",
    "icbc_jurisdiction_code": "MA",
    "icbc_jurisdiction": "MASSACHUSETTS",
    "vips_jurisdictions_objectCd": "MA",
    "vips_jurisdictions_objectDsc": "Massachusetts"
  },
  {
    "jurisdiction_code": "US_MD",
    "jurisdiction_name": "MARYLAND",
    "prime_jurisdiction_code": "MD",
    "prime_jurisdiction_name": "MARYLAND",
    "icbc_jurisdiction_code": "MD",
    "icbc_jurisdiction": "MARYLAND",
    "vips_jurisdictions_objectCd": "MD",
    "vips_jurisdictions_objectDsc": "Maryland"
  },
  {
    "jurisdiction_code": "US_ME",
    "jurisdiction_name": "MAINE",
    "prime_jurisdiction_code": "ME",
    "prime_jurisdiction_name": "MAINE",
    "icbc_jurisdiction_code": "ME",
    "icbc_jurisdiction": "MAINE",
    "vips_jurisdictions_objectCd": "ME",
    "vips_jurisdictions_objectDsc": "Maine"
  },
  {
    "jurisdiction_code": "US_MI",
    "jurisdiction_name": "MICHIGAN",
    "prime_jurisdiction_code": "MI",
    "prime_jurisdiction_name": "MICHIGAN",
    "icbc_jurisdiction_code": "MI",
    "icbc_jurisdiction": "MICHIGAN",
    "vips_jurisdictions_objectCd": "MI",
    "vips_jurisdictions_objectDsc": "Michigan"
  },
  {
    "jurisdiction_code": "US_MN",
    "jurisdiction_name": "MINNESOTA",
    "prime_jurisdiction_code": "MN",
    "prime_jurisdiction_name": "MINNESOTA",
    "icbc_jurisdiction_code": "MN",
    "icbc_jurisdiction": "MINNESOTA",
    "vips_jurisdictions_objectCd": "MN",
    "vips_jurisdictions_objectDsc": "Minnesota"
  },
  {
    "jurisdiction_code": "US_MO",
    "jurisdiction_name": "MISSOURI",
    "prime_jurisdiction_code": "MO",
    "prime_jurisdiction_name": "MISSOURI",
    "icbc_jurisdiction_code": "MO",
    "icbc_jurisdiction": "MISSOURI",
    "vips_jurisdictions_objectCd": "MO",
    "vips_jurisdictions_objectDsc": "Missouri"
  },
  {
    "jurisdiction_code": "US_MP",
    "jurisdiction_name": "NORTHERN MARIANA ISLANDS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "ZZ",
    "icbc_jurisdiction": "OTHER",
    "vips_jurisdictions_objectCd": "XX",
    "vips_jurisdictions_objectDsc": "Unknown"
  },
  {
    "jurisdiction_code": "US_MS",
    "jurisdiction_name": "MISSISSIPPI",
    "prime_jurisdiction_code": "MS",
    "prime_jurisdiction_name": "MISSISSIPPI",
    "icbc_jurisdiction_code": "MS",
    "icbc_jurisdiction": "MISSISSIPPI",
    "vips_jurisdictions_objectCd": "MS",
    "vips_jurisdictions_objectDsc": "Mississippi"
  },
  {
    "jurisdiction_code": "US_MT",
    "jurisdiction_name": "MONTANA",
    "prime_jurisdiction_code": "MT",
    "prime_jurisdiction_name": "MONTANA",
    "icbc_jurisdiction_code": "MT",
    "icbc_jurisdiction": "MONTANA",
    "vips_jurisdictions_objectCd": "MT",
    "vips_jurisdictions_objectDsc": "Montana"
  },
  {
    "jurisdiction_code": "US_NC",
    "jurisdiction_name": "NORTH CAROLINA",
    "prime_jurisdiction_code": "NC",
    "prime_jurisdiction_name": "NORTH CAROLINA",
    "icbc_jurisdiction_code": "NC",
    "icbc_jurisdiction": "NORTH CAROLINA",
    "vips_jurisdictions_objectCd": "NC",
    "vips_jurisdictions_objectDsc": "North Carolina"
  },
  {
    "jurisdiction_code": "US_ND",
    "jurisdiction_name": "NORTH DAKOTA",
    "prime_jurisdiction_code": "ND",
    "prime_jurisdiction_name": "NORTH DAKOTA",
    "icbc_jurisdiction_code": "ND",
    "icbc_jurisdiction": "NORTH DAKOTA",
    "vips_jurisdictions_objectCd": "ND",
    "vips_jurisdictions_objectDsc": "North Dakota"
  },
  {
    "jurisdiction_code": "US_NE",
    "jurisdiction_name": "NEBRASKA",
    "prime_jurisdiction_code": "NA",
    "prime_jurisdiction_name": "NEBRASKA",
    "icbc_jurisdiction_code": "NE",
    "icbc_jurisdiction": "NEBRASKA",
    "vips_jurisdictions_objectCd": "NA",
    "vips_jurisdictions_objectDsc": "Nebraska"
  },
  {
    "jurisdiction_code": "US_NH",
    "jurisdiction_name": "NEW HAMPSHIRE",
    "prime_jurisdiction_code": "NH",
    "prime_jurisdiction_name": "NEW HAMPSHIRE",
    "icbc_jurisdiction_code": "NH",
    "icbc_jurisdiction": "NEW HAMPSHIRE",
    "vips_jurisdictions_objectCd": "NH",
    "vips_jurisdictions_objectDsc": "New Hampshire"
  },
  {
    "jurisdiction_code": "US_NJ",
    "jurisdiction_name": "NEW JERSEY",
    "prime_jurisdiction_code": "NJ",
    "prime_jurisdiction_name": "NEW JERSEY",
    "icbc_jurisdiction_code": "NJ",
    "icbc_jurisdiction": "NEW JERSEY",
    "vips_jurisdictions_objectCd": "NJ",
    "vips_jurisdictions_objectDsc": "New Jersey"
  },
  {
    "jurisdiction_code": "US_NM",
    "jurisdiction_name": "NEW MEXICO",
    "prime_jurisdiction_code": "NM",
    "prime_jurisdiction_name": "NEW MEXICO",
    "icbc_jurisdiction_code": "NM",
    "icbc_jurisdiction": "NEW MEXICO",
    "vips_jurisdictions_objectCd": "NM",
    "vips_jurisdictions_objectDsc": "New Mexico"
  },
  {
    "jurisdiction_code": "US_NV",
    "jurisdiction_name": "NEVADA",
    "prime_jurisdiction_code": "NV",
    "prime_jurisdiction_name": "NEVADA",
    "icbc_jurisdiction_code": "NV",
    "icbc_jurisdiction": "NEVADA",
    "vips_jurisdictions_objectCd": "NV",
    "vips_jurisdictions_objectDsc": "Nevada"
  },
  {
    "jurisdiction_code": "US_NY",
    "jurisdiction_name": "NEW YORK",
    "prime_jurisdiction_code": "NY",
    "prime_jurisdiction_name": "NEW YORK",
    "icbc_jurisdiction_code": "NY",
    "icbc_jurisdiction": "NEW YORK",
    "vips_jurisdictions_objectCd": "NY",
    "vips_jurisdictions_objectDsc": "New York"
  },
  {
    "jurisdiction_code": "US_OH",
    "jurisdiction_name": "OHIO",
    "prime_jurisdiction_code": "OH",
    "prime_jurisdiction_name": "OHIO",
    "icbc_jurisdiction_code": "OH",
    "icbc_jurisdiction": "OHIO",
    "vips_jurisdictions_objectCd": "OH",
    "vips_jurisdictions_objectDsc": "Ohio"
  },
  {
    "jurisdiction_code": "US_OK",
    "jurisdiction_name": "OKLAHOMA",
    "prime_jurisdiction_code": "OK",
    "prime_jurisdiction_name": "OKLAHOMA",
    "icbc_jurisdiction_code": "OK",
    "icbc_jurisdiction": "OKLAHOMA",
    "vips_jurisdictions_objectCd": "OK",
    "vips_jurisdictions_objectDsc": "Oklahoma"
  },
  {
    "jurisdiction_code": "US_OR",
    "jurisdiction_name": "OREGON",
    "prime_jurisdiction_code": "OR",
    "prime_jurisdiction_name": "OREGON",
    "icbc_jurisdiction_code": "OR",
    "icbc_jurisdiction": "OREGON",
    "vips_jurisdictions_objectCd": "OR",
    "vips_jurisdictions_objectDsc": "Oregon"
  },
  {
    "jurisdiction_code": "US_PA",
    "jurisdiction_name": "PENNSYLVANIA",
    "prime_jurisdiction_code": "PA",
    "prime_jurisdiction_name": "PENNSYLVANIA",
    "icbc_jurisdiction_code": "PA",
    "icbc_jurisdiction": "PENNSYLVANIA",
    "vips_jurisdictions_objectCd": "PA",
    "vips_jurisdictions_objectDsc": "Pennsylvania"
  },
  {
    "jurisdiction_code": "US_PR",
    "jurisdiction_name": "PUERTO RICO",
    "prime_jurisdiction_code": "PR",
    "prime_jurisdiction_name": "PUERTO RICO",
    "icbc_jurisdiction_code": "PR",
    "icbc_jurisdiction": "PUERTO RICO",
    "vips_jurisdictions_objectCd": "PR",
    "vips_jurisdictions_objectDsc": "Puerto Rico"
  },
  {
    "jurisdiction_code": "US_RI",
    "jurisdiction_name": "RHODE ISLAND",
    "prime_jurisdiction_code": "RI",
    "prime_jurisdiction_name": "RHODE ISLAND",
    "icbc_jurisdiction_code": "RI",
    "icbc_jurisdiction": "RHODE ISLAND",
    "vips_jurisdictions_objectCd": "RI",
    "vips_jurisdictions_objectDsc": "Rhode Island"
  },
  {
    "jurisdiction_code": "US_SC",
    "jurisdiction_name": "SOUTH CAROLINA",
    "prime_jurisdiction_code": "SC",
    "prime_jurisdiction_name": "SOUTH CAROLINA",
    "icbc_jurisdiction_code": "SC",
    "icbc_jurisdiction": "SOUTH CAROLINA",
    "vips_jurisdictions_objectCd": "SC",
    "vips_jurisdictions_objectDsc": "South Carolina"
  },
  {
    "jurisdiction_code": "US_SD",
    "jurisdiction_name": "SOUTH DAKOTA",
    "prime_jurisdiction_code": "SD",
    "prime_jurisdiction_name": "SOUTH DAKOTA",
    "icbc_jurisdiction_code": "SD",
    "icbc_jurisdiction": "SOUTH DAKOTA",
    "vips_jurisdictions_objectCd": "SD",
    "vips_jurisdictions_objectDsc": "South Dakota"
  },
  {
    "jurisdiction_code": "US_TN",
    "jurisdiction_name": "TENNESSEE",
    "prime_jurisdiction_code": "TS",
    "prime_jurisdiction_name": "TENNESSEE",
    "icbc_jurisdiction_code": "TN",
    "icbc_jurisdiction": "TENNESSEE",
    "vips_jurisdictions_objectCd": "TS",
    "vips_jurisdictions_objectDsc": "Tennessee"
  },
  {
    "jurisdiction_code": "US_TX",
    "jurisdiction_name": "TEXAS",
    "prime_jurisdiction_code": "TX",
    "prime_jurisdiction_name": "TEXAS",
    "icbc_jurisdiction_code": "TX",
    "icbc_jurisdiction": "TEXAS",
    "vips_jurisdictions_objectCd": "TX",
    "vips_jurisdictions_objectDsc": "Texas"
  },
  {
    "jurisdiction_code": "US_UM",
    "jurisdiction_name": "U.S. MINOR OUTLYING ISLANDS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "ZZ",
    "icbc_jurisdiction": "OTHER",
    "vips_jurisdictions_objectCd": "XX",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "US_UT",
    "jurisdiction_name": "UTAH",
    "prime_jurisdiction_code": "UT",
    "prime_jurisdiction_name": "UTAH",
    "icbc_jurisdiction_code": "UT",
    "icbc_jurisdiction": "UTAH",
    "vips_jurisdictions_objectCd": "UT",
    "vips_jurisdictions_objectDsc": "Utah"
  },
  {
    "jurisdiction_code": "US_VA",
    "jurisdiction_name": "VIRGINIA",
    "prime_jurisdiction_code": "VA",
    "prime_jurisdiction_name": "VIRGINIA",
    "icbc_jurisdiction_code": "VA",
    "icbc_jurisdiction": "VIRGINIA",
    "vips_jurisdictions_objectCd": "VA",
    "vips_jurisdictions_objectDsc": "Virginia"
  },
  {
    "jurisdiction_code": "US_VI",
    "jurisdiction_name": "U.S. VIRGIN ISLANDS",
    "prime_jurisdiction_code": "VI",
    "prime_jurisdiction_name": "VIRGIN ISLANDS",
    "icbc_jurisdiction_code": "ZZ",
    "icbc_jurisdiction": "VIRGIN ISLANDS",
    "vips_jurisdictions_objectCd": "XX",
    "vips_jurisdictions_objectDsc": "Unknown"
  },
  {
    "jurisdiction_code": "US_VT",
    "jurisdiction_name": "VERMONT",
    "prime_jurisdiction_code": "VT",
    "prime_jurisdiction_name": "VERMONT",
    "icbc_jurisdiction_code": "VT",
    "icbc_jurisdiction": "VERMONT",
    "vips_jurisdictions_objectCd": "VT",
    "vips_jurisdictions_objectDsc": "Vermont"
  },
  {
    "jurisdiction_code": "US_WA",
    "jurisdiction_name": "WASHINGTON",
    "prime_jurisdiction_code": "WA",
    "prime_jurisdiction_name": "WASHINGTON",
    "icbc_jurisdiction_code": "WA",
    "icbc_jurisdiction": "WASHINGTON",
    "vips_jurisdictions_objectCd": "WA",
    "vips_jurisdictions_objectDsc": "Washington"
  },
  {
    "jurisdiction_code": "US_WI",
    "jurisdiction_name": "WISCONSIN",
    "prime_jurisdiction_code": "WI",
    "prime_jurisdiction_name": "WISCONSIN",
    "icbc_jurisdiction_code": "WI",
    "icbc_jurisdiction": "WISCONSIN",
    "vips_jurisdictions_objectCd": "WI",
    "vips_jurisdictions_objectDsc": "Wisconsin"
  },
  {
    "jurisdiction_code": "US_WV",
    "jurisdiction_name": "WEST VIRGINIA",
    "prime_jurisdiction_code": "WV",
    "prime_jurisdiction_name": "WEST VIRGINIA",
    "icbc_jurisdiction_code": "WV",
    "icbc_jurisdiction": "WEST VIRGINIA",
    "vips_jurisdictions_objectCd": "WV",
    "vips_jurisdictions_objectDsc": "West Virginia"
  },
  {
    "jurisdiction_code": "US_WY",
    "jurisdiction_name": "WYOMING",
    "prime_jurisdiction_code": "WY",
    "prime_jurisdiction_name": "WYOMING",
    "icbc_jurisdiction_code": "WY",
    "icbc_jurisdiction": "WYOMING",
    "vips_jurisdictions_objectCd": "WY",
    "vips_jurisdictions_objectDsc": "Wyoming"
  },
  {
    "jurisdiction_code": "UY",
    "jurisdiction_name": "URUGUAY",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "UZ",
    "jurisdiction_name": "UZBEKISTAN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "VA",
    "jurisdiction_name": "VATICAN CITY",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "VC",
    "jurisdiction_name": "ST. VINCENT & THE GRENADINES",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "VE",
    "jurisdiction_name": "VENEZUELA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "VG",
    "jurisdiction_name": "VIRGIN ISLANDS (BRITISH)",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "ZZ",
    "icbc_jurisdiction": "UNITED KINGDOM",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "VN",
    "jurisdiction_name": "VIET NAM",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "VU",
    "jurisdiction_name": "VANUATU",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "WF",
    "jurisdiction_name": "WALLIS & FUTUNA ISLANDS",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FR",
    "icbc_jurisdiction": "FRANCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "WS",
    "jurisdiction_name": "SAMOA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "YE",
    "jurisdiction_name": "YEMEN",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "YT",
    "jurisdiction_name": "MAYOTTE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FR",
    "icbc_jurisdiction": "FRANCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "YU",
    "jurisdiction_name": "YUGOSLAVIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "ZA",
    "jurisdiction_name": "SOUTH AFRICA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "ZM",
    "jurisdiction_name": "ZAMBIA",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "ZR",
    "jurisdiction_name": "ZAIRE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "ZW",
    "jurisdiction_name": "ZIMBABWE",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  },
  {
    "jurisdiction_code": "ZZ",
    "jurisdiction_name": "OTHER",
    "prime_jurisdiction_code": "OTH",
    "prime_jurisdiction_name": "OTHER",
    "icbc_jurisdiction_code": "FD",
    "icbc_jurisdiction": "OTHER FOREIGN LICENCE",
    "vips_jurisdictions_objectCd": "FD",
    "vips_jurisdictions_objectDsc": "Other Foreign Licence"
  }
]
def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jurisdiction_cross_ref',
    sa.Column('jurisdiction_name', sa.String(), nullable=True),
    sa.Column('jurisdiction_code', sa.String(), nullable=False),
    sa.Column('prime_jurisdiction_code', sa.String(), nullable=True),
    sa.Column('prime_jurisdiction_name', sa.String(), nullable=True),
    sa.Column('icbc_jurisdiction_code', sa.String(), nullable=True),
    sa.Column('icbc_jurisdiction', sa.String(), nullable=True),
    sa.Column('vips_jurisdictions_objectCd', sa.String(), nullable=True),
    sa.Column('vips_jurisdictions_objectDsc', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('jurisdiction_code')
    )
    
    with op.get_context().autocommit_block():
        bind = op.get_bind()
        meta = sa.MetaData()
        meta.bind = bind
        meta.reflect(bind=bind, only=('jurisdiction_cross_ref',))
        jurisdiction_cross_ref = sa.Table('jurisdiction_cross_ref', meta)
        op.bulk_insert(jurisdiction_cross_ref, jurisdiction_cros_ref_data)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jurisdiction_cross_ref')
    # ### end Alembic commands ###
