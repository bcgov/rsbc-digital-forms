"""empty message

Revision ID: 13bca6387863
Revises: dc0599cd958e
Create Date: 2023-11-23 13:00:03.610986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13bca6387863'
down_revision = 'dc0599cd958e'
branch_labels = None
depends_on = None

new_data = [
  {
    "city_code": "OHMH",
    "city_name": "100 MILE HOUSE",
    "icbc_city_code": "OHMH",
    "icbc_city_name": "100 MILE HOUSE",
    "icbc_city_name_legacy": "100 MILE HOUSE",
    "vips_city_name": "100 MILE HOUSE"
  },
  {
    "city_code": "OHTM",
    "city_name": "103 MILE HOUSE",
    "icbc_city_code": "OHTM",
    "icbc_city_name": "103 MILE HOUSE",
    "icbc_city_name_legacy": "100 MILE HOUSE",
    "vips_city_name": "103 MILE HOUSE"
  },
  {
    "city_code": "OHFM",
    "city_name": "105 MILE HOUSE",
    "icbc_city_code": "OHFM",
    "icbc_city_name": "105 MILE HOUSE",
    "icbc_city_name_legacy": "100 MILE HOUSE",
    "vips_city_name": "105 MILE HOUSE"
  },
  {
    "city_code": "OHEM",
    "city_name": "108 MILE HOUSE",
    "icbc_city_code": "OHEM",
    "icbc_city_name": "108 MILE HOUSE",
    "icbc_city_name_legacy": "108 MILE HOUSE",
    "vips_city_name": "108 MILE HOUSE"
  },
  {
    "city_code": "OHER",
    "city_name": "108 MILE RANCH",
    "icbc_city_code": "OHER",
    "icbc_city_name": "108 MILE RANCH",
    "icbc_city_name_legacy": "108 MILE RANCH",
    "vips_city_name": "108 MILE RANCH"
  },
  {
    "city_code": "OFOM",
    "city_name": "141 MILE HOUSE",
    "icbc_city_code": "OFOM",
    "icbc_city_name": "141 MILE HOUSE",
    "icbc_city_name_legacy": "150 MILE HOUSE",
    "vips_city_name": "141 MILE HOUSE"
  },
  {
    "city_code": "OFMH",
    "city_name": "150 MILE HOUSE",
    "icbc_city_code": "OFMH",
    "icbc_city_name": "150 MILE HOUSE",
    "icbc_city_name_legacy": "150 MILE HOUSE",
    "vips_city_name": "150 MILE HOUSE"
  },
  {
    "city_code": "SMHS",
    "city_name": "70 MILE HOUSE",
    "icbc_city_code": "SMHS",
    "icbc_city_name": "70 MILE HOUSE",
    "icbc_city_name_legacy": "70 MILE HOUSE",
    "vips_city_name": "70 MILE HOUSE"
  },
  {
    "city_code": "NTMH",
    "city_name": "93 MILE HOUSE",
    "icbc_city_code": "NTMH",
    "icbc_city_name": "93 MILE HOUSE",
    "icbc_city_name_legacy": "93 MILE HOUSE",
    "vips_city_name": "93 MILE HOUSE"
  },
  {
    "city_code": "ABB",
    "city_name": "ABBOTSFORD",
    "icbc_city_code": "ABB",
    "icbc_city_name": "ABBOTSFORD",
    "icbc_city_name_legacy": "ABBOTSFORD",
    "vips_city_name": "ABBOTSFORD"
  },
  {
    "city_code": "ADLK",
    "city_name": "ADAMS LAKE",
    "icbc_city_code": "ADLK",
    "icbc_city_name": "ADAMS LAKE",
    "icbc_city_name_legacy": "ADAMS LAKE",
    "vips_city_name": "ADAMS LAKE"
  },
  {
    "city_code": "AGSZ",
    "city_name": "AGASSIZ",
    "icbc_city_code": "AGSZ",
    "icbc_city_name": "AGASSIZ",
    "icbc_city_name_legacy": "AGASSIZ",
    "vips_city_name": "AGASSIZ"
  },
  {
    "city_code": "AGAT",
    "city_name": "AGATE",
    "icbc_city_code": "AGAT",
    "icbc_city_name": "AGATE",
    "icbc_city_name_legacy": "SPENCES BRIDGE",
    "vips_city_name": "AGATE"
  },
  {
    "city_code": "AHST",
    "city_name": "AHOUSAHT",
    "icbc_city_code": "AHST",
    "icbc_city_name": "AHOUSAHT",
    "icbc_city_name_legacy": "AHOUSAT",
    "vips_city_name": "AHOUSAHT"
  },
  {
    "city_code": "ANWO",
    "city_name": "AINSWORTH HOT SPRINGS",
    "icbc_city_code": "ANWO",
    "icbc_city_name": "AINSWORTH HOT SPRINGS",
    "icbc_city_name_legacy": "AINSWORTH HOT S",
    "vips_city_name": "AINSWORTH HOT SPRINGS"
  },
  {
    "city_code": "ALBR",
    "city_name": "ALBREDA",
    "icbc_city_code": "ALBR",
    "icbc_city_name": "ALBREDA",
    "icbc_city_name_legacy": "ALBREDA",
    "vips_city_name": "ALBREDA"
  },
  {
    "city_code": "ALBA",
    "city_name": "ALERT BAY",
    "icbc_city_code": "ALBA",
    "icbc_city_name": "ALERT BAY",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "ALERT BAY"
  },
  {
    "city_code": "ALEX",
    "city_name": "ALEXANDRIA",
    "icbc_city_code": "ALEX",
    "icbc_city_name": "ALEXANDRIA",
    "icbc_city_name_legacy": "ALEXANDRIA",
    "vips_city_name": "ALEXANDRIA"
  },
  {
    "city_code": "ALCK",
    "city_name": "ALEXIS CREEK",
    "icbc_city_code": "ALCK",
    "icbc_city_name": "ALEXIS CREEK",
    "icbc_city_name_legacy": "ALEXIS CREEK",
    "vips_city_name": "ALEXIS CREEK"
  },
  {
    "city_code": "ALLK",
    "city_name": "ALEZA LAKE",
    "icbc_city_code": "ALLK",
    "icbc_city_name": "ALEZA LAKE",
    "icbc_city_name_legacy": "ALEZA LAKE",
    "vips_city_name": "ALEZA LAKE"
  },
  {
    "city_code": "ALAR",
    "city_name": "ALICE ARM",
    "icbc_city_code": "ALAR",
    "icbc_city_name": "ALICE ARM",
    "icbc_city_name_legacy": "ALICE ARM",
    "vips_city_name": "ALICE ARM"
  },
  {
    "city_code": "AKLK",
    "city_name": "ALKALI LAKE",
    "icbc_city_code": "AKLK",
    "icbc_city_name": "ALKALI LAKE",
    "icbc_city_name_legacy": "ALKALI LAKE",
    "vips_city_name": "ALKALI LAKE"
  },
  {
    "city_code": "ASLK",
    "city_name": "ALLISON LAKE",
    "icbc_city_code": "ASLK",
    "icbc_city_name": "ALLISON LAKE",
    "icbc_city_name_legacy": "PRINCETON",
    "vips_city_name": "ALLISON LAKE"
  },
  {
    "city_code": "ALTN",
    "city_name": "ALTONA",
    "icbc_city_code": "ALTN",
    "icbc_city_name": "ALTONA",
    "icbc_city_name_legacy": "ALTONA",
    "vips_city_name": "ALTONA"
  },
  {
    "city_code": "ANCD",
    "city_name": "ANACONDA",
    "icbc_city_code": "ANCD",
    "icbc_city_name": "ANACONDA",
    "icbc_city_name_legacy": "MIDWAY",
    "vips_city_name": "ANACONDA"
  },
  {
    "city_code": "ANLK",
    "city_name": "ANAHIM LAKE",
    "icbc_city_code": "ANLK",
    "icbc_city_name": "ANAHIM LAKE",
    "icbc_city_name_legacy": "ANAHIM LAKE",
    "vips_city_name": "ANAHIM LAKE"
  },
  {
    "city_code": "AFIR",
    "city_name": "ANAHIM'S FLAT IR",
    "icbc_city_code": "AFIR",
    "icbc_city_name": "ANAHIMS FLAT IR",
    "icbc_city_name_legacy": "ALEXIS CREEK",
    "vips_city_name": "ANAHIMS FLAT IR"
  },
  {
    "city_code": "AMIR",
    "city_name": "ANAHIM'S MEADOW IR",
    "icbc_city_code": "AMIR",
    "icbc_city_name": "ANAHIMS MEADOW IR",
    "icbc_city_name_legacy": "ALEXIS CREEK",
    "vips_city_name": "ANAHIMS MEADOW IR"
  },
  {
    "city_code": "ANMT",
    "city_name": "ANGLEMONT",
    "icbc_city_code": "ANMT",
    "icbc_city_name": "ANGLEMONT",
    "icbc_city_name_legacy": "ANGLEMONT",
    "vips_city_name": "ANGLEMONT"
  },
  {
    "city_code": "ANM",
    "city_name": "ANMORE",
    "icbc_city_code": "ANM",
    "icbc_city_name": "ANMORE",
    "icbc_city_name_legacy": "ANMORE",
    "vips_city_name": "ANMORE"
  },
  {
    "city_code": "AARM",
    "city_name": "ANSTEY ARM",
    "icbc_city_code": "AARM",
    "icbc_city_name": "ANSTEY ARM",
    "icbc_city_name_legacy": "SICAMOUS",
    "vips_city_name": "ANSTEY ARM"
  },
  {
    "city_code": "ANIS",
    "city_name": "ANVIL ISLAND",
    "icbc_city_code": "ANIS",
    "icbc_city_name": "ANVIL ISLAND",
    "icbc_city_name_legacy": "ANVIL ISLAND",
    "vips_city_name": "ANVIL ISLAND"
  },
  {
    "city_code": "ANYX",
    "city_name": "ANYOX",
    "icbc_city_code": "ANYX",
    "icbc_city_name": "ANYOX",
    "icbc_city_name_legacy": "ANYOX",
    "vips_city_name": "ANYOX"
  },
  {
    "city_code": "APEX",
    "city_name": "APEX",
    "icbc_city_code": "APEX",
    "icbc_city_name": "APEX",
    "icbc_city_name_legacy": "APEX",
    "vips_city_name": "APEX"
  },
  {
    "city_code": "APDL",
    "city_name": "APPLEDALE",
    "icbc_city_code": "APDL",
    "icbc_city_name": "APPLEDALE",
    "icbc_city_name_legacy": "APPLEDALE",
    "vips_city_name": "APPLEDALE"
  },
  {
    "city_code": "ARGT",
    "city_name": "ARGENTA",
    "icbc_city_code": "ARGT",
    "icbc_city_name": "ARGENTA",
    "icbc_city_name_legacy": "ARGENTA",
    "vips_city_name": "ARGENTA"
  },
  {
    "city_code": "AZIS",
    "city_name": "ARISTAZABAL ISLAND",
    "icbc_city_code": "AZIS",
    "icbc_city_name": "ARISTAZABAL ISLAND",
    "icbc_city_name_legacy": "BELLA BELLA",
    "vips_city_name": "ARISTAZABAL ISLAND"
  },
  {
    "city_code": "ARMS",
    "city_name": "ARMSTRONG",
    "icbc_city_code": "ARMS",
    "icbc_city_name": "ARMSTRONG",
    "icbc_city_name_legacy": "ARMSTRONG",
    "vips_city_name": "ARMSTRONG"
  },
  {
    "city_code": "ARAS",
    "city_name": "ARRAS",
    "icbc_city_code": "ARAS",
    "icbc_city_name": "ARRAS",
    "icbc_city_name_legacy": "ARRAS",
    "vips_city_name": "ARRAS"
  },
  {
    "city_code": "AWPK",
    "city_name": "ARROW PARK",
    "icbc_city_code": "AWPK",
    "icbc_city_name": "ARROW PARK",
    "icbc_city_name_legacy": "ARROW PARK",
    "vips_city_name": "ARROW PARK"
  },
  {
    "city_code": "ASCF",
    "city_name": "ASHCROFT",
    "icbc_city_code": "ASCF",
    "icbc_city_name": "ASHCROFT",
    "icbc_city_name_legacy": "ASHCROFT",
    "vips_city_name": "ASHCROFT"
  },
  {
    "city_code": "ACSR",
    "city_name": "ASHCROFT RURAL",
    "icbc_city_code": "ACSR",
    "icbc_city_name": "ASHCROFT RURAL",
    "icbc_city_name_legacy": "ASHCROFT",
    "vips_city_name": "ASHCROFT RURAL"
  },
  {
    "city_code": "ASCK",
    "city_name": "ASHTON CREEK",
    "icbc_city_code": "ASCK",
    "icbc_city_name": "ASHTON CREEK",
    "icbc_city_name_legacy": "ENDERBY",
    "vips_city_name": "ASHTON CREEK"
  },
  {
    "city_code": "ASPG",
    "city_name": "ASPEN GROVE",
    "icbc_city_code": "ASPG",
    "icbc_city_name": "ASPEN GROVE",
    "icbc_city_name_legacy": "ASPEN GROVE",
    "vips_city_name": "ASPEN GROVE"
  },
  {
    "city_code": "ATHA",
    "city_name": "ATHALMER",
    "icbc_city_code": "ATHA",
    "icbc_city_name": "ATHALMER",
    "icbc_city_name_legacy": "ATHALMER",
    "vips_city_name": "ATHALMER"
  },
  {
    "city_code": "AHIS",
    "city_name": "ATHLONE ISLAND",
    "icbc_city_code": "AHIS",
    "icbc_city_name": "ATHLONE ISLAND",
    "icbc_city_name_legacy": "BELLA BELLA",
    "vips_city_name": "ATHLONE ISLAND"
  },
  {
    "city_code": "AKIS",
    "city_name": "ATKINSON ISLAND",
    "icbc_city_code": "AKIS",
    "icbc_city_name": "ATKINSON ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "ATKINSON ISLAND"
  },
  {
    "city_code": "ATLN",
    "city_name": "ATLIN",
    "icbc_city_code": "ATLN",
    "icbc_city_name": "ATLIN",
    "icbc_city_name_legacy": "ATLIN",
    "vips_city_name": "ATLIN"
  },
  {
    "city_code": "ATCH",
    "city_name": "ATTACHIE",
    "icbc_city_code": "ATCH",
    "icbc_city_name": "ATTACHIE",
    "icbc_city_name_legacy": "ATTACHIE",
    "vips_city_name": "ATTACHIE"
  },
  {
    "city_code": "AUST",
    "city_name": "AUSTRALIAN",
    "icbc_city_code": "AUST",
    "icbc_city_name": "AUSTRALIAN",
    "icbc_city_name_legacy": "AUSTRALIAN",
    "vips_city_name": "AUSTRALIAN"
  },
  {
    "city_code": "AVLA",
    "city_name": "AVOLA",
    "icbc_city_code": "AVLA",
    "icbc_city_name": "AVOLA",
    "icbc_city_name_legacy": "AVOLA",
    "vips_city_name": "AVOLA"
  },
  {
    "city_code": "BKCK",
    "city_name": "BAKER CREEK",
    "icbc_city_code": "BKCK",
    "icbc_city_name": "BAKER CREEK",
    "icbc_city_name_legacy": "BAKER CREEK",
    "vips_city_name": "BAKER CREEK"
  },
  {
    "city_code": "BKIS",
    "city_name": "BAKER ISLAND",
    "icbc_city_code": "BKIS",
    "icbc_city_name": "BAKER ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "BAKER ISLAND"
  },
  {
    "city_code": "BVIS",
    "city_name": "BALAKLAVA ISLAND",
    "icbc_city_code": "BVIS",
    "icbc_city_name": "BALAKLAVA ISLAND",
    "icbc_city_name_legacy": "PORT HARDY",
    "vips_city_name": "BALAKLAVA ISLAND"
  },
  {
    "city_code": "BALD",
    "city_name": "BALDONNEL",
    "icbc_city_code": "BALD",
    "icbc_city_name": "BALDONNEL",
    "icbc_city_name_legacy": "BALDONNEL",
    "vips_city_name": "BALDONNEL"
  },
  {
    "city_code": "BALF",
    "city_name": "BALFOUR",
    "icbc_city_code": "BALF",
    "icbc_city_name": "BALFOUR",
    "icbc_city_name_legacy": "BALFOUR",
    "vips_city_name": "BALFOUR"
  },
  {
    "city_code": "BAMF",
    "city_name": "BAMFIELD",
    "icbc_city_code": "BAMF",
    "icbc_city_name": "BAMFIELD",
    "icbc_city_name_legacy": "BAMFIELD",
    "vips_city_name": "BAMFIELD"
  },
  {
    "city_code": "BNKR",
    "city_name": "BANKEIR",
    "icbc_city_code": "BNKR",
    "icbc_city_name": "BANKEIR",
    "icbc_city_name_legacy": "BANKEIR",
    "vips_city_name": "BANKEIR"
  },
  {
    "city_code": "BSIS",
    "city_name": "BANKS ISLAND",
    "icbc_city_code": "BSIS",
    "icbc_city_name": "BANKS ISLAND",
    "icbc_city_name_legacy": "KITKATLA",
    "vips_city_name": "BANKS ISLAND"
  },
  {
    "city_code": "BKVL",
    "city_name": "BARKERVILLE",
    "icbc_city_code": "BKVL",
    "icbc_city_name": "BARKERVILLE",
    "icbc_city_name_legacy": "BARKERVILLE",
    "vips_city_name": "BARKERVILLE"
  },
  {
    "city_code": "BARH",
    "city_name": "BARNHARTVALE",
    "icbc_city_code": "BARH",
    "icbc_city_name": "BARNHARTVALE",
    "icbc_city_name_legacy": "BARNHARTVALE",
    "vips_city_name": "BARNHARTVALE"
  },
  {
    "city_code": "BAIS",
    "city_name": "BARON ISLAND",
    "icbc_city_code": "BAIS",
    "icbc_city_name": "BARON ISLAND",
    "icbc_city_name_legacy": "PRINCE RUPERT",
    "vips_city_name": "BARON ISLAND"
  },
  {
    "city_code": "BARR",
    "city_name": "BARRIERE",
    "icbc_city_code": "BARR",
    "icbc_city_name": "BARRIERE",
    "icbc_city_name_legacy": "BARRIERE",
    "vips_city_name": "BARRIERE"
  },
  {
    "city_code": "BARV",
    "city_name": "BARRIERE RIVER",
    "icbc_city_code": "BARV",
    "icbc_city_name": "BARRIERE RIVER",
    "icbc_city_name_legacy": "BARRIERE",
    "vips_city_name": "BARRIERE RIVER"
  },
  {
    "city_code": "BKLK",
    "city_name": "BAYNES LAKE",
    "icbc_city_code": "BKLK",
    "icbc_city_name": "BAYNES LAKE",
    "icbc_city_name_legacy": "BAYNES LAKE",
    "vips_city_name": "BAYNES LAKE"
  },
  {
    "city_code": "BAFT",
    "city_name": "BEAR FLAT",
    "icbc_city_code": "BAFT",
    "icbc_city_name": "BEAR FLAT",
    "icbc_city_name_legacy": "BEAR FLAT",
    "vips_city_name": "BEAR FLAT"
  },
  {
    "city_code": "BRLK",
    "city_name": "BEAR LAKE",
    "icbc_city_code": "BRLK",
    "icbc_city_name": "BEAR LAKE",
    "icbc_city_name_legacy": "BEAR LAKE",
    "vips_city_name": "BEAR LAKE"
  },
  {
    "city_code": "BSLY",
    "city_name": "BEASLEY",
    "icbc_city_code": "BSLY",
    "icbc_city_name": "BEASLEY",
    "icbc_city_name_legacy": "BEASLEY",
    "vips_city_name": "BEASLEY"
  },
  {
    "city_code": "BEAT",
    "city_name": "BEATON",
    "icbc_city_code": "BEAT",
    "icbc_city_name": "BEATON",
    "icbc_city_name_legacy": "BEATON",
    "vips_city_name": "BEATON"
  },
  {
    "city_code": "BERV",
    "city_name": "BEATTON RIVER",
    "icbc_city_code": "BERV",
    "icbc_city_name": "BEATTON RIVER",
    "icbc_city_name_legacy": "FORT ST JOHN",
    "vips_city_name": "BEATTON RIVER"
  },
  {
    "city_code": "BVCV",
    "city_name": "BEAVER COVE",
    "icbc_city_code": "BVCV",
    "icbc_city_name": "BEAVER COVE",
    "icbc_city_name_legacy": "BEAVER COVE",
    "vips_city_name": "BEAVER COVE"
  },
  {
    "city_code": "BVFL",
    "city_name": "BEAVER FALLS",
    "icbc_city_code": "BVFL",
    "icbc_city_name": "BEAVER FALLS",
    "icbc_city_name_legacy": "BEAVER FALLS",
    "vips_city_name": "BEAVER FALLS"
  },
  {
    "city_code": "BVDL",
    "city_name": "BEAVERDELL",
    "icbc_city_code": "BVDL",
    "icbc_city_name": "BEAVERDELL",
    "icbc_city_name_legacy": "BEAVERDELL",
    "vips_city_name": "BEAVERDELL"
  },
  {
    "city_code": "BVLY",
    "city_name": "BEAVERLEY",
    "icbc_city_code": "BVLY",
    "icbc_city_name": "BEAVERLEY",
    "icbc_city_name_legacy": "PRINCE GEORGE",
    "vips_city_name": "BEAVERLEY"
  },
  {
    "city_code": "BDNM",
    "city_name": "BEDNESTI NORMAN",
    "icbc_city_code": "BDNM",
    "icbc_city_name": "BEDNESTI NORMAN",
    "icbc_city_name_legacy": "BEDNESTI",
    "vips_city_name": "BEDNESTI NORMAN"
  },
  {
    "city_code": "BELC",
    "city_name": "BELCARRA",
    "icbc_city_code": "BELC",
    "icbc_city_name": "BELCARRA",
    "icbc_city_name_legacy": "BELCARRA",
    "vips_city_name": "BELCARRA"
  },
  {
    "city_code": "BLBL",
    "city_name": "BELLA BELLA",
    "icbc_city_code": "BLBL",
    "icbc_city_name": "BELLA BELLA",
    "icbc_city_name_legacy": "BELLA BELLA",
    "vips_city_name": "BELLA BELLA"
  },
  {
    "city_code": "BLCL",
    "city_name": "BELLA COOLA",
    "icbc_city_code": "BLCL",
    "icbc_city_name": "BELLA COOLA",
    "icbc_city_name_legacy": "BELLA COOLA",
    "vips_city_name": "BELLA COOLA"
  },
  {
    "city_code": "BENN",
    "city_name": "BENNETT",
    "icbc_city_code": "BENN",
    "icbc_city_name": "BENNETT",
    "icbc_city_name_legacy": "ATIN",
    "vips_city_name": "BENNETT"
  },
  {
    "city_code": "BRIS",
    "city_name": "BERRY ISLAND",
    "icbc_city_code": "BRIS",
    "icbc_city_name": "BERRY ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "BERRY ISLAND"
  },
  {
    "city_code": "BSBG",
    "city_name": "BESSBOROUGH",
    "icbc_city_code": "BSBG",
    "icbc_city_name": "BESSBOROUGH",
    "icbc_city_name_legacy": "BESSBOROUGH",
    "vips_city_name": "BESSBOROUGH"
  },
  {
    "city_code": "BIBR",
    "city_name": "BIG BAR",
    "icbc_city_code": "BIBR",
    "icbc_city_name": "BIG BAR",
    "icbc_city_name_legacy": "CLINTON",
    "vips_city_name": "BIG BAR"
  },
  {
    "city_code": "BIBL",
    "city_name": "BIG BAR LAKE",
    "icbc_city_code": "BIBL",
    "icbc_city_name": "BIG BAR LAKE",
    "icbc_city_name_legacy": "BIG BAR CREEK",
    "vips_city_name": "BIG BAR LAKE"
  },
  {
    "city_code": "BICK",
    "city_name": "BIG CREEK",
    "icbc_city_code": "BICK",
    "icbc_city_name": "BIG CREEK",
    "icbc_city_name_legacy": "BIG CREEK",
    "vips_city_name": "BIG CREEK"
  },
  {
    "city_code": "BILK",
    "city_name": "BIG LAKE",
    "icbc_city_code": "BILK",
    "icbc_city_name": "BIG LAKE",
    "icbc_city_name_legacy": "BIG LAKE",
    "vips_city_name": "BIG LAKE"
  },
  {
    "city_code": "BLKR",
    "city_name": "BIG LAKE RANCH",
    "icbc_city_code": "BLKR",
    "icbc_city_name": "BIG LAKE RANCH",
    "icbc_city_name_legacy": "BIG LAKE RANCH",
    "vips_city_name": "BIG LAKE RANCH"
  },
  {
    "city_code": "BIWH",
    "city_name": "BIG WHITE",
    "icbc_city_code": "BIWH",
    "icbc_city_name": "BIG WHITE",
    "icbc_city_name_legacy": "KELOWNA",
    "vips_city_name": "BIG WHITE"
  },
  {
    "city_code": "BCIS",
    "city_name": "BIRCH ISLAND",
    "icbc_city_code": "BCIS",
    "icbc_city_name": "BIRCH ISLAND",
    "icbc_city_name_legacy": "BIRCH ISLAND",
    "vips_city_name": "BIRCH ISLAND"
  },
  {
    "city_code": "BRKN",
    "city_name": "BIRKEN",
    "icbc_city_code": "BRKN",
    "icbc_city_name": "BIRKEN",
    "icbc_city_name_legacy": "BIRKEN",
    "vips_city_name": "BIRKEN"
  },
  {
    "city_code": "BLCK",
    "city_name": "BLACK CREEK",
    "icbc_city_code": "BLCK",
    "icbc_city_name": "BLACK CREEK",
    "icbc_city_name_legacy": "BLACK CREEK",
    "vips_city_name": "BLACK CREEK"
  },
  {
    "city_code": "BLPN",
    "city_name": "BLACK PINES",
    "icbc_city_code": "BLPN",
    "icbc_city_name": "BLACK PINES",
    "icbc_city_name_legacy": "BLACK PINES",
    "vips_city_name": "BLACK PINES"
  },
  {
    "city_code": "BLPL",
    "city_name": "BLACKPOOL",
    "icbc_city_code": "BLPL",
    "icbc_city_name": "BLACKPOOL",
    "icbc_city_name_legacy": "BLACKPOOL",
    "vips_city_name": "BLACKPOOL"
  },
  {
    "city_code": "BLWR",
    "city_name": "BLACKWATER",
    "icbc_city_code": "BLWR",
    "icbc_city_name": "BLACKWATER",
    "icbc_city_name_legacy": "QUESNEL",
    "vips_city_name": "BLACKWATER"
  },
  {
    "city_code": "BWNR",
    "city_name": "BLACKWATER NORTH",
    "icbc_city_code": "BWNR",
    "icbc_city_name": "BLACKWATER NORTH",
    "icbc_city_name_legacy": "QUESNEL",
    "vips_city_name": "BLACKWATER NORTH"
  },
  {
    "city_code": "BLAE",
    "city_name": "BLAEBERRY",
    "icbc_city_code": "BLAE",
    "icbc_city_name": "BLAEBERRY",
    "icbc_city_name_legacy": "GOLDEN",
    "vips_city_name": "BLAEBERRY"
  },
  {
    "city_code": "BLWT",
    "city_name": "BLEWETT",
    "icbc_city_code": "BLWT",
    "icbc_city_name": "BLEWETT",
    "icbc_city_name_legacy": "BLEWETT",
    "vips_city_name": "BLEWETT"
  },
  {
    "city_code": "BLIS",
    "city_name": "BLIGH ISLAND",
    "icbc_city_code": "BLIS",
    "icbc_city_name": "BLIGH ISLAND",
    "icbc_city_name_legacy": "GOLD RIVER",
    "vips_city_name": "BLIGH ISLAND"
  },
  {
    "city_code": "BLBY",
    "city_name": "BLIND BAY",
    "icbc_city_code": "BLBY",
    "icbc_city_name": "BLIND BAY",
    "icbc_city_name_legacy": "BLIND BAY",
    "vips_city_name": "BLIND BAY"
  },
  {
    "city_code": "BLCH",
    "city_name": "BLIND CHANNEL",
    "icbc_city_code": "BLCH",
    "icbc_city_name": "BLIND CHANNEL",
    "icbc_city_name_legacy": "BLIND CHANNEL",
    "vips_city_name": "BLIND CHANNEL"
  },
  {
    "city_code": "BLUB",
    "city_name": "BLUBBER BAY",
    "icbc_city_code": "BLUB",
    "icbc_city_name": "BLUBBER BAY",
    "icbc_city_name_legacy": "BLUBBER BAY",
    "vips_city_name": "BLUBBER BAY"
  },
  {
    "city_code": "BLHL",
    "city_name": "BLUCHER HALL",
    "icbc_city_code": "BLHL",
    "icbc_city_name": "BLUCHER HALL",
    "icbc_city_name_legacy": "BARRIERE",
    "vips_city_name": "BLUCHER HALL"
  },
  {
    "city_code": "BLRV",
    "city_name": "BLUE RIVER",
    "icbc_city_code": "BLRV",
    "icbc_city_name": "BLUE RIVER",
    "icbc_city_name_legacy": "BLUE RIVER",
    "vips_city_name": "BLUE RIVER"
  },
  {
    "city_code": "BYCK",
    "city_name": "BLUEBERRY CREEK",
    "icbc_city_code": "BYCK",
    "icbc_city_name": "BLUEBERRY CREEK",
    "icbc_city_name_legacy": "BLUEBERRY CREEK",
    "vips_city_name": "BLUEBERRY CREEK"
  },
  {
    "city_code": "BYRI",
    "city_name": "BLUEBERRY RIVER IR",
    "icbc_city_code": "BYRI",
    "icbc_city_name": "BLUEBERRY RIVER IR",
    "icbc_city_name_legacy": "FORT ST JOHN",
    "vips_city_name": "BLUEBERRY RIVER IR"
  },
  {
    "city_code": "BQLK",
    "city_name": "BOB QUINN LAKE",
    "icbc_city_code": "BQLK",
    "icbc_city_name": "BOB QUINN LAKE",
    "icbc_city_name_legacy": "TELEGRAPH CREEK",
    "vips_city_name": "BOB QUINN LAKE"
  },
  {
    "city_code": "BONA",
    "city_name": "BONAPARTE IR",
    "icbc_city_code": "BONA",
    "icbc_city_name": "BONAPARTE IR",
    "icbc_city_name_legacy": "ASHCROFT",
    "vips_city_name": "BONAPARTE IR"
  },
  {
    "city_code": "BOIS",
    "city_name": "BONWICK ISLAND",
    "icbc_city_code": "BOIS",
    "icbc_city_name": "BONWICK ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "BONWICK ISLAND"
  },
  {
    "city_code": "BBAR",
    "city_name": "BOSTON BAR",
    "icbc_city_code": "BBAR",
    "icbc_city_name": "BOSTON BAR",
    "icbc_city_name_legacy": "BOSTON BAR",
    "vips_city_name": "BOSTON BAR"
  },
  {
    "city_code": "BSTF",
    "city_name": "BOSTON FLAT",
    "icbc_city_code": "BSTF",
    "icbc_city_name": "BOSTON FLAT",
    "icbc_city_name_legacy": "ASHCROFT",
    "vips_city_name": "BOSTON FLAT"
  },
  {
    "city_code": "BSWL",
    "city_name": "BOSWELL",
    "icbc_city_code": "BSWL",
    "icbc_city_name": "BOSWELL",
    "icbc_city_name_legacy": "BOSWELL",
    "vips_city_name": "BOSWELL"
  },
  {
    "city_code": "BCLK",
    "city_name": "BOUCHIE LAKE",
    "icbc_city_code": "BCLK",
    "icbc_city_name": "BOUCHIE LAKE",
    "icbc_city_name_legacy": "BOUCHIE LAKE",
    "vips_city_name": "BOUCHIE LAKE"
  },
  {
    "city_code": "BOLK",
    "city_name": "BOUDREAU LAKE",
    "icbc_city_code": "BOLK",
    "icbc_city_name": "BOUDREAU LAKE",
    "icbc_city_name_legacy": "HUDSON'S HOPE",
    "vips_city_name": "BOUDREAU LAKE"
  },
  {
    "city_code": "BOCY",
    "city_name": "BOULDER CITY",
    "icbc_city_code": "BOCY",
    "icbc_city_name": "BOULDER CITY",
    "icbc_city_name_legacy": "DEASE LAKE",
    "vips_city_name": "BOULDER CITY"
  },
  {
    "city_code": "BOW",
    "city_name": "BOWEN ISLAND",
    "icbc_city_code": "BOW",
    "icbc_city_name": "BOWEN ISLAND",
    "icbc_city_name_legacy": "BOWEN ISLAND",
    "vips_city_name": "BOWEN ISLAND"
  },
  {
    "city_code": "BOPP",
    "city_name": "BOWRON LAKES PROVINCIAL PARK",
    "icbc_city_code": "BOPP",
    "icbc_city_name": "BOWRON LAKES PROVINCIAL PARK",
    "icbc_city_name_legacy": "MCBRIDE",
    "vips_city_name": "BOWRON LAKES PROVINCIAL PARK"
  },
  {
    "city_code": "BWSR",
    "city_name": "BOWSER",
    "icbc_city_code": "BWSR",
    "icbc_city_name": "BOWSER",
    "icbc_city_name_legacy": "BOWSER",
    "vips_city_name": "BOWSER"
  },
  {
    "city_code": "BWLK",
    "city_name": "BOWSER LAKE",
    "icbc_city_code": "BWLK",
    "icbc_city_name": "BOWSER LAKE",
    "icbc_city_name_legacy": "STEWART",
    "vips_city_name": "BOWSER LAKE"
  },
  {
    "city_code": "BYLK",
    "city_name": "BOYA LAKE",
    "icbc_city_code": "BYLK",
    "icbc_city_name": "BOYA LAKE",
    "icbc_city_name_legacy": "DEASE LAKE",
    "vips_city_name": "BOYA LAKE"
  },
  {
    "city_code": "BRLN",
    "city_name": "BRALORNE",
    "icbc_city_code": "BRLN",
    "icbc_city_name": "BRALORNE",
    "icbc_city_name_legacy": "BRALORNE",
    "vips_city_name": "BRALORNE"
  },
  {
    "city_code": "BRNC",
    "city_name": "BRENNAN CREEK",
    "icbc_city_code": "BRNC",
    "icbc_city_name": "BRENNAN CREEK",
    "icbc_city_name_legacy": "ADAMS LAKE",
    "vips_city_name": "BRENNAN CREEK"
  },
  {
    "city_code": "BRAR",
    "city_name": "BRIAR",
    "icbc_city_code": "BRAR",
    "icbc_city_name": "BRIAR",
    "icbc_city_name_legacy": "BRIAR RIDGE",
    "vips_city_name": "BRIAR"
  },
  {
    "city_code": "BIVL",
    "city_name": "BRIDESVILLE",
    "icbc_city_code": "BIVL",
    "icbc_city_name": "BRIDESVILLE",
    "icbc_city_name_legacy": "BRIDESVILLE",
    "vips_city_name": "BRIDESVILLE"
  },
  {
    "city_code": "BDLK",
    "city_name": "BRIDGE LAKE",
    "icbc_city_code": "BDLK",
    "icbc_city_name": "BRIDGE LAKE",
    "icbc_city_name_legacy": "BRIDGE LAKE",
    "vips_city_name": "BRIDGE LAKE"
  },
  {
    "city_code": "BRNT",
    "city_name": "BRILLIANT",
    "icbc_city_code": "BRNT",
    "icbc_city_name": "BRILLIANT",
    "icbc_city_name_legacy": "BRILLIANT",
    "vips_city_name": "BRILLIANT"
  },
  {
    "city_code": "BRSC",
    "city_name": "BRISCO",
    "icbc_city_code": "BRSC",
    "icbc_city_name": "BRISCO",
    "icbc_city_name_legacy": "BRISCO",
    "vips_city_name": "BRISCO"
  },
  {
    "city_code": "BRTB",
    "city_name": "BRITANNIA BEACH",
    "icbc_city_code": "BRTB",
    "icbc_city_name": "BRITANNIA BEACH",
    "icbc_city_name_legacy": "BRITANNIA BEACH",
    "vips_city_name": "BRITANNIA BEACH"
  },
  {
    "city_code": "BKMR",
    "city_name": "BROOKMERE",
    "icbc_city_code": "BKMR",
    "icbc_city_name": "BROOKMERE",
    "icbc_city_name_legacy": "BROOKMERE",
    "vips_city_name": "BROOKMERE"
  },
  {
    "city_code": "BGIS",
    "city_name": "BROUGHTON ISLAND",
    "icbc_city_code": "BGIS",
    "icbc_city_name": "BROUGHTON ISLAND",
    "icbc_city_name_legacy": "PORT HARDY",
    "vips_city_name": "BROUGHTON ISLAND"
  },
  {
    "city_code": "BUKH",
    "city_name": "BUCKHORN",
    "icbc_city_code": "BUKH",
    "icbc_city_name": "BUCKHORN",
    "icbc_city_name_legacy": "PRINCE GEORGE",
    "vips_city_name": "BUCKHORN"
  },
  {
    "city_code": "BKRV",
    "city_name": "BUCKINGHORSE RIVER",
    "icbc_city_code": "BKRV",
    "icbc_city_name": "BUCKINGHORSE RIVER",
    "icbc_city_name_legacy": "FORT ST JOHN",
    "vips_city_name": "BUCKINGHORSE RIVER"
  },
  {
    "city_code": "BFCK",
    "city_name": "BUFFALO CREEK",
    "icbc_city_code": "BFCK",
    "icbc_city_name": "BUFFALO CREEK",
    "icbc_city_name_legacy": "BUFFALO CREEK",
    "vips_city_name": "BUFFALO CREEK"
  },
  {
    "city_code": "BUIC",
    "city_name": "BUICK",
    "icbc_city_code": "BUIC",
    "icbc_city_name": "BUICK",
    "icbc_city_name_legacy": "BUICK",
    "vips_city_name": "BUICK"
  },
  {
    "city_code": "BURV",
    "city_name": "BULL RIVER",
    "icbc_city_code": "BURV",
    "icbc_city_name": "BULL RIVER",
    "icbc_city_name_legacy": "BULL RIVER",
    "vips_city_name": "BULL RIVER"
  },
  {
    "city_code": "BBY",
    "city_name": "BURNABY",
    "icbc_city_code": "BBY",
    "icbc_city_name": "BURNABY",
    "icbc_city_name_legacy": "BURNABY",
    "vips_city_name": "BURNABY"
  },
  {
    "city_code": "BYIS",
    "city_name": "BURNABY ISLAND",
    "icbc_city_code": "BYIS",
    "icbc_city_name": "BURNABY ISLAND",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "BURNABY ISLAND"
  },
  {
    "city_code": "BSLK",
    "city_name": "BURNS LAKE",
    "icbc_city_code": "BSLK",
    "icbc_city_name": "BURNS LAKE",
    "icbc_city_name_legacy": "BURNS LAKE",
    "vips_city_name": "BURNS LAKE"
  },
  {
    "city_code": "BRTO",
    "city_name": "BURTON",
    "icbc_city_code": "BRTO",
    "icbc_city_name": "BURTON",
    "icbc_city_name_legacy": "BURTON",
    "vips_city_name": "BURTON"
  },
  {
    "city_code": "BUTE",
    "city_name": "BUTE INLET",
    "icbc_city_code": "BUTE",
    "icbc_city_name": "BUTE INLET",
    "icbc_city_name_legacy": "QUADRA ISLAND",
    "vips_city_name": "BUTE INLET"
  },
  {
    "city_code": "CACK",
    "city_name": "CACHE CREEK",
    "icbc_city_code": "CACK",
    "icbc_city_name": "CACHE CREEK",
    "icbc_city_name_legacy": "CACHE CREEK",
    "vips_city_name": "CACHE CREEK"
  },
  {
    "city_code": "CACV",
    "city_name": "CACHE CREEK RURAL",
    "icbc_city_code": "CACV",
    "icbc_city_name": "CACHE CREEK RURAL",
    "icbc_city_name_legacy": "CACHE CREEK",
    "vips_city_name": "CACHE CREEK RURAL"
  },
  {
    "city_code": "CHLY",
    "city_name": "CAHILTY",
    "icbc_city_code": "CHLY",
    "icbc_city_name": "CAHILTY",
    "icbc_city_name_legacy": "KAMLOOPS",
    "vips_city_name": "CAHILTY"
  },
  {
    "city_code": "CVIS",
    "city_name": "CALVERT ISLAND",
    "icbc_city_code": "CVIS",
    "icbc_city_name": "CALVERT ISLAND",
    "icbc_city_name_legacy": "BELLA BELLA",
    "vips_city_name": "CALVERT ISLAND"
  },
  {
    "city_code": "CPIS",
    "city_name": "CAMPANIA ISLAND",
    "icbc_city_code": "CPIS",
    "icbc_city_name": "CAMPANIA ISLAND",
    "icbc_city_name_legacy": "HARTLEY BAY",
    "vips_city_name": "CAMPANIA ISLAND"
  },
  {
    "city_code": "CBIS",
    "city_name": "CAMPBELL ISLAND",
    "icbc_city_code": "CBIS",
    "icbc_city_name": "CAMPBELL ISLAND",
    "icbc_city_name_legacy": "CAMPBELL ISLAND",
    "vips_city_name": "CAMPBELL ISLAND"
  },
  {
    "city_code": "CBRV",
    "city_name": "CAMPBELL RIVER",
    "icbc_city_code": "CBRV",
    "icbc_city_name": "CAMPBELL RIVER",
    "icbc_city_name_legacy": "CAMPBELL RIVER",
    "vips_city_name": "CAMPBELL RIVER"
  },
  {
    "city_code": "CNFL",
    "city_name": "CANAL FLATS",
    "icbc_city_code": "CNFL",
    "icbc_city_name": "CANAL FLATS",
    "icbc_city_name_legacy": "CANAL FLATS",
    "vips_city_name": "CANAL FLATS"
  },
  {
    "city_code": "CMLK",
    "city_name": "CANIM LAKE",
    "icbc_city_code": "CMLK",
    "icbc_city_name": "CANIM LAKE",
    "icbc_city_name_legacy": "CANIM LAKE",
    "vips_city_name": "CANIM LAKE"
  },
  {
    "city_code": "CANO",
    "city_name": "CANOE",
    "icbc_city_code": "CANO",
    "icbc_city_name": "CANOE",
    "icbc_city_name_legacy": "CANOE",
    "vips_city_name": "CANOE"
  },
  {
    "city_code": "CECK",
    "city_name": "CANOE CREEK",
    "icbc_city_code": "CECK",
    "icbc_city_name": "CANOE CREEK",
    "icbc_city_name_legacy": "CANOE CREEK",
    "vips_city_name": "CANOE CREEK"
  },
  {
    "city_code": "FCYN",
    "city_name": "CANYON ALPINE",
    "icbc_city_code": "FCYN",
    "icbc_city_name": "CANYON ALPINE",
    "icbc_city_name_legacy": "BOSTON BAR",
    "vips_city_name": "CANYON ALPINE"
  },
  {
    "city_code": "CANY",
    "city_name": "CANYON HOT SPRINGS",
    "icbc_city_code": "CANY",
    "icbc_city_name": "CANYON HOT SPRINGS",
    "icbc_city_name_legacy": "REVELSTOKE",
    "vips_city_name": "CANYON HOT SPRINGS"
  },
  {
    "city_code": "CSPK",
    "city_name": "CAPE SCOTT PARK",
    "icbc_city_code": "CSPK",
    "icbc_city_name": "CAPE SCOTT PARK",
    "icbc_city_name_legacy": "PORT HARDY",
    "vips_city_name": "CAPE SCOTT PARK"
  },
  {
    "city_code": "CARV",
    "city_name": "CARIBOO RIVER",
    "icbc_city_code": "CARV",
    "icbc_city_name": "CARIBOO RIVER",
    "icbc_city_name_legacy": "WILLIAMS LAKE",
    "vips_city_name": "CARIBOO RIVER"
  },
  {
    "city_code": "CARM",
    "city_name": "CARMI",
    "icbc_city_code": "CARM",
    "icbc_city_name": "CARMI",
    "icbc_city_name_legacy": "CARMI",
    "vips_city_name": "CARMI"
  },
  {
    "city_code": "CRLK",
    "city_name": "CARP LAKE",
    "icbc_city_code": "CRLK",
    "icbc_city_name": "CARP LAKE",
    "icbc_city_name_legacy": "TSAY KEH DENE",
    "vips_city_name": "CARP LAKE"
  },
  {
    "city_code": "CPLK",
    "city_name": "CARPENTER LAKE",
    "icbc_city_code": "CPLK",
    "icbc_city_name": "CARPENTER LAKE",
    "icbc_city_name_legacy": "PEMBERTON",
    "vips_city_name": "CARPENTER LAKE"
  },
  {
    "city_code": "CASC",
    "city_name": "CASCADE",
    "icbc_city_code": "CASC",
    "icbc_city_name": "CASCADE",
    "icbc_city_name_legacy": "CASCADE",
    "vips_city_name": "CASCADE"
  },
  {
    "city_code": "CATL",
    "city_name": "CASTLEDALE",
    "icbc_city_code": "CATL",
    "icbc_city_name": "CASTLEDALE",
    "icbc_city_name_legacy": "GOLDEN",
    "vips_city_name": "CASTLEDALE"
  },
  {
    "city_code": "CLGR",
    "city_name": "CASTLEGAR",
    "icbc_city_code": "CLGR",
    "icbc_city_name": "CASTLEGAR",
    "icbc_city_name_legacy": "CASTLEGAR",
    "vips_city_name": "CASTLEGAR"
  },
  {
    "city_code": "CLIS",
    "city_name": "CATALA ISLAND",
    "icbc_city_code": "CLIS",
    "icbc_city_name": "CATALA ISLAND",
    "icbc_city_name_legacy": "GOLD RIVER",
    "vips_city_name": "CATALA ISLAND"
  },
  {
    "city_code": "CSTN",
    "city_name": "CAWSTON",
    "icbc_city_code": "CSTN",
    "icbc_city_name": "CAWSTON",
    "icbc_city_name_legacy": "CAWSTON",
    "vips_city_name": "CAWSTON"
  },
  {
    "city_code": "CACS",
    "city_name": "CAYCUSE",
    "icbc_city_code": "CACS",
    "icbc_city_name": "CAYCUSE",
    "icbc_city_name_legacy": "LAKE COWICHAN",
    "vips_city_name": "CAYCUSE"
  },
  {
    "city_code": "CELK",
    "city_name": "CECIL LAKE",
    "icbc_city_code": "CELK",
    "icbc_city_name": "CECIL LAKE",
    "icbc_city_name_legacy": "CECIL LAKE",
    "vips_city_name": "CECIL LAKE"
  },
  {
    "city_code": "CRIS",
    "city_name": "CEDAR ISLAND",
    "icbc_city_code": "CRIS",
    "icbc_city_name": "CEDAR ISLAND",
    "icbc_city_name_legacy": "TSAY KEH DENE",
    "vips_city_name": "CEDAR ISLAND"
  },
  {
    "city_code": "CRVL",
    "city_name": "CEDARVALE",
    "icbc_city_code": "CRVL",
    "icbc_city_name": "CEDARVALE",
    "icbc_city_name_legacy": "CEDARVALE",
    "vips_city_name": "CEDARVALE"
  },
  {
    "city_code": "CLST",
    "city_name": "CELISTA",
    "icbc_city_code": "CLST",
    "icbc_city_name": "CELISTA",
    "icbc_city_name_legacy": "CELISTA",
    "vips_city_name": "CELISTA"
  },
  {
    "city_code": "CSNC",
    "city_name": "CENTRAL SAANICH",
    "icbc_city_code": "CSNC",
    "icbc_city_name": "CENTRAL SAANICH",
    "icbc_city_name_legacy": "CENTRAL SAANICH",
    "vips_city_name": "CENTRAL SAANICH"
  },
  {
    "city_code": "CHIS",
    "city_name": "CHAATL ISLAND",
    "icbc_city_code": "CHIS",
    "icbc_city_name": "CHAATL ISLAND",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "CHAATL ISLAND"
  },
  {
    "city_code": "CNLK",
    "city_name": "CHAPPERON LAKE",
    "icbc_city_code": "CNLK",
    "icbc_city_name": "CHAPPERON LAKE",
    "icbc_city_name_legacy": "MERRITT",
    "vips_city_name": "CHAPPERON LAKE"
  },
  {
    "city_code": "CLLK",
    "city_name": "CHARLIE LAKE",
    "icbc_city_code": "CLLK",
    "icbc_city_name": "CHARLIE LAKE",
    "icbc_city_name_legacy": "CHARLIE LAKE",
    "vips_city_name": "CHARLIE LAKE"
  },
  {
    "city_code": "CHAS",
    "city_name": "CHASE",
    "icbc_city_code": "CHAS",
    "icbc_city_name": "CHASE",
    "icbc_city_name_legacy": "CHASE",
    "vips_city_name": "CHASE"
  },
  {
    "city_code": "CHAR",
    "city_name": "CHASE RURAL",
    "icbc_city_code": "CHAR",
    "icbc_city_name": "CHASE RURAL",
    "icbc_city_name_legacy": "CHASE",
    "vips_city_name": "CHASE RURAL"
  },
  {
    "city_code": "CHAC",
    "city_name": "CHASE CREEK",
    "icbc_city_code": "CHAC",
    "icbc_city_name": "CHASE CREEK",
    "icbc_city_name_legacy": "CHASE",
    "vips_city_name": "CHASE CREEK"
  },
  {
    "city_code": "CHSM",
    "city_name": "CHASM",
    "icbc_city_code": "CHSM",
    "icbc_city_name": "CHASM",
    "icbc_city_name_legacy": "CHASM",
    "vips_city_name": "CHASM"
  },
  {
    "city_code": "CMIS",
    "city_name": "CHATHAM ISLAND",
    "icbc_city_code": "CMIS",
    "icbc_city_name": "CHATHAM ISLAND",
    "icbc_city_name_legacy": "VICTORIA",
    "vips_city_name": "CHATHAM ISLAND"
  },
  {
    "city_code": "CHIR",
    "city_name": "CHEAM IR",
    "icbc_city_code": "CHIR",
    "icbc_city_name": "CHEAM IR",
    "icbc_city_name_legacy": "AGASSIZ",
    "vips_city_name": "CHEAM IR"
  },
  {
    "city_code": "CHHL",
    "city_name": "CHEHALIS",
    "icbc_city_code": "CHHL",
    "icbc_city_name": "CHEHALIS",
    "icbc_city_name_legacy": "AGASSIZ",
    "vips_city_name": "CHEHALIS"
  },
  {
    "city_code": "CHNS",
    "city_name": "CHEMAINUS",
    "icbc_city_code": "CHNS",
    "icbc_city_name": "CHEMAINUS",
    "icbc_city_name_legacy": "CHEMAINUS",
    "vips_city_name": "CHEMAINUS"
  },
  {
    "city_code": "CHCK",
    "city_name": "CHERRY CREEK",
    "icbc_city_code": "CHCK",
    "icbc_city_name": "CHERRY CREEK",
    "icbc_city_name_legacy": "CHERRY CREEK",
    "vips_city_name": "CHERRY CREEK"
  },
  {
    "city_code": "CHVL",
    "city_name": "CHERRYVILLE",
    "icbc_city_code": "CHVL",
    "icbc_city_name": "CHERRYVILLE",
    "icbc_city_name_legacy": "CHERRYVILLE",
    "vips_city_name": "CHERRYVILLE"
  },
  {
    "city_code": "CHES",
    "city_name": "CHESLATTA",
    "icbc_city_code": "CHES",
    "icbc_city_name": "CHESLATTA",
    "icbc_city_name_legacy": "CHESLATTA",
    "vips_city_name": "CHESLATTA"
  },
  {
    "city_code": "CTWD",
    "city_name": "CHETWYND",
    "icbc_city_code": "CTWD",
    "icbc_city_name": "CHETWYND",
    "icbc_city_name_legacy": "CHETWYND",
    "vips_city_name": "CHETWYND"
  },
  {
    "city_code": "CHEZ",
    "city_name": "CHEZACUT",
    "icbc_city_code": "CHEZ",
    "icbc_city_name": "CHEZACUT",
    "icbc_city_name_legacy": "CHEZACUT",
    "vips_city_name": "CHEZACUT"
  },
  {
    "city_code": "CFLK",
    "city_name": "CHIEF LAKE",
    "icbc_city_code": "CFLK",
    "icbc_city_name": "CHIEF LAKE",
    "icbc_city_name_legacy": "CHIEF LAKE",
    "vips_city_name": "CHIEF LAKE"
  },
  {
    "city_code": "CLKF",
    "city_name": "CHILANKO FORKS",
    "icbc_city_code": "CLKF",
    "icbc_city_name": "CHILANKO FORKS",
    "icbc_city_name_legacy": "CHILANKO FORKS",
    "vips_city_name": "CHILANKO FORKS"
  },
  {
    "city_code": "CHIL",
    "city_name": "CHILLIWACK",
    "icbc_city_code": "CHIL",
    "icbc_city_name": "CHILLIWACK",
    "icbc_city_name_legacy": "CHILLIWACK",
    "vips_city_name": "CHILLIWACK"
  },
  {
    "city_code": "CHRV",
    "city_name": "CHILLIWACK RIVER VALLEY",
    "icbc_city_code": "CHRV",
    "icbc_city_name": "CHILLIWACK RIVER VALLEY",
    "icbc_city_name_legacy": "CHILLIWACK",
    "vips_city_name": "CHILLIWACK RIVER VALLEY"
  },
  {
    "city_code": "CMNL",
    "city_name": "CHIMNEY LAKE",
    "icbc_city_code": "CMNL",
    "icbc_city_name": "CHIMNEY LAKE",
    "icbc_city_name_legacy": "WILLIAMS LAKE",
    "vips_city_name": "CHIMNEY LAKE"
  },
  {
    "city_code": "CKCV",
    "city_name": "CHINOOK COVE",
    "icbc_city_code": "CKCV",
    "icbc_city_name": "CHINOOK COVE",
    "icbc_city_name_legacy": "CHINOOK COVE",
    "vips_city_name": "CHINOOK COVE"
  },
  {
    "city_code": "CHVY",
    "city_name": "CHRISTIAN VALLEY",
    "icbc_city_code": "CHVY",
    "icbc_city_name": "CHRISTIAN VALLEY",
    "icbc_city_name_legacy": "CHRISTIAN VALLE",
    "vips_city_name": "CHRISTIAN VALLEY"
  },
  {
    "city_code": "CSLK",
    "city_name": "CHRISTINA LAKE",
    "icbc_city_code": "CSLK",
    "icbc_city_name": "CHRISTINA LAKE",
    "icbc_city_name_legacy": "CHRISTINA LAKE",
    "vips_city_name": "CHRISTINA LAKE"
  },
  {
    "city_code": "CHCH",
    "city_name": "CHU CHUA",
    "icbc_city_code": "CHCH",
    "icbc_city_name": "CHU CHUA",
    "icbc_city_name_legacy": "CHU CHUA",
    "vips_city_name": "CHU CHUA"
  },
  {
    "city_code": "CINE",
    "city_name": "CINEMA",
    "icbc_city_code": "CINE",
    "icbc_city_name": "CINEMA",
    "icbc_city_name_legacy": "CINEMA",
    "vips_city_name": "CINEMA"
  },
  {
    "city_code": "CPLT",
    "city_name": "CLAPPERTON",
    "icbc_city_code": "CPLT",
    "icbc_city_name": "CLAPPERTON",
    "icbc_city_name_legacy": "CLAPPERTON",
    "vips_city_name": "CLAPPERTON"
  },
  {
    "city_code": "CLHT",
    "city_name": "CLAYHURST",
    "icbc_city_code": "CLHT",
    "icbc_city_name": "CLAYHURST",
    "icbc_city_name_legacy": "CLAYHURST",
    "vips_city_name": "CLAYHURST"
  },
  {
    "city_code": "CLWR",
    "city_name": "CLEARWATER",
    "icbc_city_code": "CLWR",
    "icbc_city_name": "CLEARWATER",
    "icbc_city_name_legacy": "CLEARWATER",
    "vips_city_name": "CLEARWATER"
  },
  {
    "city_code": "CLWT",
    "city_name": "CLEARWATER RURAL",
    "icbc_city_code": "CLWT",
    "icbc_city_name": "CLEARWATER RURAL",
    "icbc_city_name_legacy": "CLEARWATER",
    "vips_city_name": "CLEARWATER RURAL"
  },
  {
    "city_code": "CLEM",
    "city_name": "CLEMRETTA",
    "icbc_city_code": "CLEM",
    "icbc_city_name": "CLEMRETTA",
    "icbc_city_name_legacy": "CLEMRETTA",
    "vips_city_name": "CLEMRETTA"
  },
  {
    "city_code": "CLTN",
    "city_name": "CLINTON",
    "icbc_city_code": "CLTN",
    "icbc_city_name": "CLINTON",
    "icbc_city_name_legacy": "CLINTON",
    "vips_city_name": "CLINTON"
  },
  {
    "city_code": "CLTR",
    "city_name": "CLINTON RURAL",
    "icbc_city_code": "CLTR",
    "icbc_city_name": "CLINTON RURAL",
    "icbc_city_name_legacy": "CLINTON",
    "vips_city_name": "CLINTON RURAL"
  },
  {
    "city_code": "CLTS",
    "city_name": "CLINTON SOUTH",
    "icbc_city_code": "CLTS",
    "icbc_city_name": "CLINTON SOUTH",
    "icbc_city_name_legacy": "CLINTON",
    "vips_city_name": "CLINTON SOUTH"
  },
  {
    "city_code": "CZLK",
    "city_name": "CLUCULZ LAKE",
    "icbc_city_code": "CZLK",
    "icbc_city_name": "CLUCULZ LAKE",
    "icbc_city_name_legacy": "VANDERHOOF",
    "vips_city_name": "CLUCULZ LAKE"
  },
  {
    "city_code": "CLHB",
    "city_name": "COAL HARBOUR",
    "icbc_city_code": "CLHB",
    "icbc_city_name": "COAL HARBOUR",
    "icbc_city_name_legacy": "COAL HARBOUR",
    "vips_city_name": "COAL HARBOUR"
  },
  {
    "city_code": "CLID",
    "city_name": "COAL ISLAND",
    "icbc_city_code": "CLID",
    "icbc_city_name": "COAL ISLAND",
    "icbc_city_name_legacy": "SIDNEY",
    "vips_city_name": "COAL ISLAND"
  },
  {
    "city_code": "CRIV",
    "city_name": "COAL RIVER",
    "icbc_city_code": "CRIV",
    "icbc_city_name": "COAL RIVER",
    "icbc_city_name_legacy": "COAL RIVER",
    "vips_city_name": "COAL RIVER"
  },
  {
    "city_code": "CLMT",
    "city_name": "COALMONT",
    "icbc_city_code": "CLMT",
    "icbc_city_name": "COALMONT",
    "icbc_city_name_legacy": "COALMONT",
    "vips_city_name": "COALMONT"
  },
  {
    "city_code": "CBHL",
    "city_name": "COBBLE HILL",
    "icbc_city_code": "CBHL",
    "icbc_city_name": "COBBLE HILL",
    "icbc_city_name_legacy": "COBBLE HILL",
    "vips_city_name": "COBBLE HILL"
  },
  {
    "city_code": "CISI",
    "city_name": "COFFIN ISLAND IR",
    "icbc_city_code": "CISI",
    "icbc_city_name": "COFFIN ISLAND IR",
    "icbc_city_name_legacy": "LADYSMITH",
    "vips_city_name": "COFFIN ISLAND IR"
  },
  {
    "city_code": "CODM",
    "city_name": "COLDSTREAM",
    "icbc_city_code": "CODM",
    "icbc_city_name": "COLDSTREAM",
    "icbc_city_name_legacy": "COLDSTREAM",
    "vips_city_name": "COLDSTREAM"
  },
  {
    "city_code": "CDCK",
    "city_name": "COLDSTREAM CREEK",
    "icbc_city_code": "CDCK",
    "icbc_city_name": "COLDSTREAM CREEK",
    "icbc_city_name_legacy": "VERNON",
    "vips_city_name": "COLDSTREAM CREEK"
  },
  {
    "city_code": "CLDW",
    "city_name": "COLDWATER",
    "icbc_city_code": "CLDW",
    "icbc_city_name": "COLDWATER",
    "icbc_city_name_legacy": "MERRITT",
    "vips_city_name": "COLDWATER"
  },
  {
    "city_code": "CLLT",
    "city_name": "COLLEYMOUNT",
    "icbc_city_code": "CLLT",
    "icbc_city_name": "COLLEYMOUNT",
    "icbc_city_name_legacy": "COLLEY MOUNT",
    "vips_city_name": "COLLEYMOUNT"
  },
  {
    "city_code": "CLGS",
    "city_name": "COLUMBIA GARDENS",
    "icbc_city_code": "CLGS",
    "icbc_city_name": "COLUMBIA GARDENS",
    "icbc_city_name_legacy": "COLUMBIA GARDEN",
    "vips_city_name": "COLUMBIA GARDENS"
  },
  {
    "city_code": "CBLV",
    "city_name": "COLUMBIA VALLEY",
    "icbc_city_code": "CBLV",
    "icbc_city_name": "COLUMBIA VALLEY",
    "icbc_city_name_legacy": "COLUMBIA VALLEY",
    "vips_city_name": "COLUMBIA VALLEY"
  },
  {
    "city_code": "COLW",
    "city_name": "COLWOOD",
    "icbc_city_code": "COLW",
    "icbc_city_name": "COLWOOD",
    "icbc_city_name_legacy": "COLWOOD",
    "vips_city_name": "COLWOOD"
  },
  {
    "city_code": "COMX",
    "city_name": "COMOX",
    "icbc_city_code": "COMX",
    "icbc_city_name": "COMOX",
    "icbc_city_name_legacy": "COMOX",
    "vips_city_name": "COMOX"
  },
  {
    "city_code": "CPII",
    "city_name": "COMPTON ISLAND IR",
    "icbc_city_code": "CPII",
    "icbc_city_name": "COMPTON ISLAND IR",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "COMPTON ISLAND IR"
  },
  {
    "city_code": "CISL",
    "city_name": "CONE ISLAND",
    "icbc_city_code": "CISL",
    "icbc_city_name": "CONE ISLAND",
    "icbc_city_name_legacy": "BELLA BELLA",
    "vips_city_name": "CONE ISLAND"
  },
  {
    "city_code": "COOM",
    "city_name": "COOMBS",
    "icbc_city_code": "COOM",
    "icbc_city_name": "COOMBS",
    "icbc_city_name_legacy": "COOMBS",
    "vips_city_name": "COOMBS"
  },
  {
    "city_code": "CPCK",
    "city_name": "COOPER CREEK",
    "icbc_city_code": "CPCK",
    "icbc_city_name": "COOPER CREEK",
    "icbc_city_name_legacy": "KASLO",
    "vips_city_name": "COOPER CREEK"
  },
  {
    "city_code": "CRCK",
    "city_name": "COPPER CREEK",
    "icbc_city_code": "CRCK",
    "icbc_city_name": "COPPER CREEK",
    "icbc_city_name_legacy": "COPPER CREEK",
    "vips_city_name": "COPPER CREEK"
  },
  {
    "city_code": "CQLA",
    "city_name": "COQUIHALLA",
    "icbc_city_code": "CQLA",
    "icbc_city_name": "COQUIHALLA",
    "icbc_city_name_legacy": "COQUIHALLA",
    "vips_city_name": "COQUIHALLA"
  },
  {
    "city_code": "COQ",
    "city_name": "COQUITLAM",
    "icbc_city_code": "COQ",
    "icbc_city_name": "COQUITLAM",
    "icbc_city_name_legacy": "COQUITLAM",
    "vips_city_name": "COQUITLAM"
  },
  {
    "city_code": "CORB",
    "city_name": "CORBIN",
    "icbc_city_code": "CORB",
    "icbc_city_name": "CORBIN",
    "icbc_city_name_legacy": "CORBIN",
    "vips_city_name": "CORBIN"
  },
  {
    "city_code": "CTIS",
    "city_name": "CORTES ISLAND",
    "icbc_city_code": "CTIS",
    "icbc_city_name": "CORTES ISLAND",
    "icbc_city_name_legacy": "CORTES ISLAND",
    "vips_city_name": "CORTES ISLAND"
  },
  {
    "city_code": "CTTD",
    "city_name": "COTTONWOOD",
    "icbc_city_code": "CTTD",
    "icbc_city_name": "COTTONWOOD",
    "icbc_city_name_legacy": "COTTONWOOD",
    "vips_city_name": "COTTONWOOD"
  },
  {
    "city_code": "CRTY",
    "city_name": "COURTENAY",
    "icbc_city_code": "CRTY",
    "icbc_city_name": "COURTENAY",
    "icbc_city_name_legacy": "COURTENAY",
    "vips_city_name": "COURTENAY"
  },
  {
    "city_code": "CUTL",
    "city_name": "COUTLEE",
    "icbc_city_code": "CUTL",
    "icbc_city_name": "COUTLEE",
    "icbc_city_name_legacy": "MERRITT",
    "vips_city_name": "COUTLEE"
  },
  {
    "city_code": "CWBY",
    "city_name": "COWICHAN BAY",
    "icbc_city_code": "CWBY",
    "icbc_city_name": "COWICHAN BAY",
    "icbc_city_name_legacy": "COWICHAN BAY",
    "vips_city_name": "COWICHAN BAY"
  },
  {
    "city_code": "CXIS",
    "city_name": "COX ISLAND",
    "icbc_city_code": "CXIS",
    "icbc_city_name": "COX ISLAND",
    "icbc_city_name_legacy": "PORT HARDY",
    "vips_city_name": "COX ISLAND"
  },
  {
    "city_code": "CGCH",
    "city_name": "CRAIGELLACHIE",
    "icbc_city_code": "CGCH",
    "icbc_city_name": "CRAIGELLACHIE",
    "icbc_city_name_legacy": "CRAIGELLACHIE",
    "vips_city_name": "CRAIGELLACHIE"
  },
  {
    "city_code": "CRJC",
    "city_name": "CRANBERRY JUNCTION",
    "icbc_city_code": "CRJC",
    "icbc_city_name": "CRANBERRY JUNCTION",
    "icbc_city_name_legacy": "NEW AIYANSH",
    "vips_city_name": "CRANBERRY JUNCTION"
  },
  {
    "city_code": "CRBK",
    "city_name": "CRANBROOK",
    "icbc_city_code": "CRBK",
    "icbc_city_name": "CRANBROOK",
    "icbc_city_name_legacy": "CRANBROOK",
    "vips_city_name": "CRANBROOK"
  },
  {
    "city_code": "CFBA",
    "city_name": "CRAWFORD BAY",
    "icbc_city_code": "CFBA",
    "icbc_city_name": "CRAWFORD BAY",
    "icbc_city_name_legacy": "CRAWFORD BAY",
    "vips_city_name": "CRAWFORD BAY"
  },
  {
    "city_code": "CSIS",
    "city_name": "CREASE ISLAND",
    "icbc_city_code": "CSIS",
    "icbc_city_name": "CREASE ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "CREASE ISLAND"
  },
  {
    "city_code": "CCSR",
    "city_name": "CRESCENT SPUR",
    "icbc_city_code": "CCSR",
    "icbc_city_name": "CRESCENT SPUR",
    "icbc_city_name_legacy": "CRESCENT SPUR",
    "vips_city_name": "CRESCENT SPUR"
  },
  {
    "city_code": "CRVY",
    "city_name": "CRESCENT VALLEY",
    "icbc_city_code": "CRVY",
    "icbc_city_name": "CRESCENT VALLEY",
    "icbc_city_name_legacy": "CRESCENT VALLEY",
    "vips_city_name": "CRESCENT VALLEY"
  },
  {
    "city_code": "CETN",
    "city_name": "CRESTON",
    "icbc_city_code": "CETN",
    "icbc_city_name": "CRESTON",
    "icbc_city_name_legacy": "CRESTON",
    "vips_city_name": "CRESTON"
  },
  {
    "city_code": "CROF",
    "city_name": "CROFTON",
    "icbc_city_code": "CROF",
    "icbc_city_name": "CROFTON",
    "icbc_city_name_legacy": "CROFTON",
    "vips_city_name": "CROFTON"
  },
  {
    "city_code": "CORV",
    "city_name": "CROSS RIVER",
    "icbc_city_code": "CORV",
    "icbc_city_name": "CROSS RIVER",
    "icbc_city_name_legacy": "INVERMERE",
    "vips_city_name": "CROSS RIVER"
  },
  {
    "city_code": "CULT",
    "city_name": "CULTUS LAKE",
    "icbc_city_code": "CULT",
    "icbc_city_name": "CULTUS LAKE",
    "icbc_city_name_legacy": "CULTUS LAKE",
    "vips_city_name": "CULTUS LAKE"
  },
  {
    "city_code": "CMLD",
    "city_name": "CUMBERLAND",
    "icbc_city_code": "CMLD",
    "icbc_city_name": "CUMBERLAND",
    "icbc_city_name_legacy": "CUMBERLAND",
    "vips_city_name": "CUMBERLAND"
  },
  {
    "city_code": "QNCH",
    "city_name": "DAAJING GIIDS",
    "icbc_city_code": "QNCH",
    "icbc_city_name": "DAAJING GIIDS",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "DAAJING GIIDS"
  },
  {
    "city_code": "DNSK",
    "city_name": "DANSKIN",
    "icbc_city_code": "DNSK",
    "icbc_city_name": "DANSKIN",
    "icbc_city_name_legacy": "DANSKIN",
    "vips_city_name": "DANSKIN"
  },
  {
    "city_code": "DRCY",
    "city_name": "D'ARCY",
    "icbc_city_code": "DRCY",
    "icbc_city_name": "D'ARCY",
    "icbc_city_name_legacy": "D'ARCY",
    "vips_city_name": "D'ARCY"
  },
  {
    "city_code": "DARF",
    "city_name": "DARFIELD",
    "icbc_city_code": "DARF",
    "icbc_city_name": "DARFIELD",
    "icbc_city_name_legacy": "DARFIELD",
    "vips_city_name": "DARFIELD"
  },
  {
    "city_code": "DVIS",
    "city_name": "DAVIES ISLAND",
    "icbc_city_code": "DVIS",
    "icbc_city_name": "DAVIES ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "DAVIES ISLAND"
  },
  {
    "city_code": "DWCK",
    "city_name": "DAWSON CREEK",
    "icbc_city_code": "DWCK",
    "icbc_city_name": "DAWSON CREEK",
    "icbc_city_name_legacy": "DAWSON CREEK",
    "vips_city_name": "DAWSON CREEK"
  },
  {
    "city_code": "DCIS",
    "city_name": "DECOURCY ISLAND",
    "icbc_city_code": "DCIS",
    "icbc_city_name": "DECOURCY ISLAND",
    "icbc_city_name_legacy": "GABRIOLA",
    "vips_city_name": "DECOURCY ISLAND"
  },
  {
    "city_code": "DHIS",
    "city_name": "DEHORSEY ISLAND",
    "icbc_city_code": "DHIS",
    "icbc_city_name": "DEHORSEY ISLAND",
    "icbc_city_name_legacy": "PRINCE RUPERT",
    "vips_city_name": "DEHORSEY ISLAND"
  },
  {
    "city_code": "DSCK",
    "city_name": "DEADMANS CREEK",
    "icbc_city_code": "DSCK",
    "icbc_city_name": "DEADMANS CREEK",
    "icbc_city_name_legacy": "REVELSTOKE",
    "vips_city_name": "DEADMANS CREEK"
  },
  {
    "city_code": "DSLK",
    "city_name": "DEASE LAKE",
    "icbc_city_code": "DSLK",
    "icbc_city_name": "DEASE LAKE",
    "icbc_city_name_legacy": "DEASE LAKE",
    "vips_city_name": "DEASE LAKE"
  },
  {
    "city_code": "DKLK",
    "city_name": "DECKER LAKE",
    "icbc_city_code": "DKLK",
    "icbc_city_name": "DECKER LAKE",
    "icbc_city_name_legacy": "DECKER LAKE",
    "vips_city_name": "DECKER LAKE"
  },
  {
    "city_code": "DPCK",
    "city_name": "DEEP CREEK",
    "icbc_city_code": "DPCK",
    "icbc_city_name": "DEEP CREEK",
    "icbc_city_name_legacy": "ENDERBY",
    "vips_city_name": "DEEP CREEK"
  },
  {
    "city_code": "DCKI",
    "city_name": "DEEP CREEK IR",
    "icbc_city_code": "DCKI",
    "icbc_city_name": "DEEP CREEK IR",
    "icbc_city_name_legacy": "ENDERBY",
    "vips_city_name": "DEEP CREEK IR"
  },
  {
    "city_code": "DALK",
    "city_name": "DEKA LAKE",
    "icbc_city_code": "DALK",
    "icbc_city_name": "DEKA LAKE",
    "icbc_city_name_legacy": "100 MILE HOUSE",
    "vips_city_name": "DEKA LAKE"
  },
  {
    "city_code": "DEL",
    "city_name": "DELTA",
    "icbc_city_code": "DEL",
    "icbc_city_name": "DELTA",
    "icbc_city_name_legacy": "DELTA",
    "vips_city_name": "DELTA"
  },
  {
    "city_code": "DNIS",
    "city_name": "DENMAN ISLAND",
    "icbc_city_code": "DNIS",
    "icbc_city_name": "DENMAN ISLAND",
    "icbc_city_name_legacy": "DENMAN ISLAND",
    "vips_city_name": "DENMAN ISLAND"
  },
  {
    "city_code": "DYIS",
    "city_name": "DENNY ISLAND",
    "icbc_city_code": "DYIS",
    "icbc_city_name": "DENNY ISLAND",
    "icbc_city_name_legacy": "DENNY ISLAND",
    "vips_city_name": "DENNY ISLAND"
  },
  {
    "city_code": "DRCH",
    "city_name": "DEROCHE",
    "icbc_city_code": "DRCH",
    "icbc_city_name": "DEROCHE",
    "icbc_city_name_legacy": "DEROCHE",
    "vips_city_name": "DEROCHE"
  },
  {
    "city_code": "DVIN",
    "city_name": "DEVINE",
    "icbc_city_code": "DVIN",
    "icbc_city_name": "DEVINE",
    "icbc_city_name_legacy": "DEVINE",
    "vips_city_name": "DEVINE"
  },
  {
    "city_code": "DWDN",
    "city_name": "DEWDNEY",
    "icbc_city_code": "DWDN",
    "icbc_city_name": "DEWDNEY",
    "icbc_city_name_legacy": "DEWDNEY",
    "vips_city_name": "DEWDNEY"
  },
  {
    "city_code": "DWIS",
    "city_name": "DEWDNEY ISLAND",
    "icbc_city_code": "DWIS",
    "icbc_city_name": "DEWDNEY ISLAND",
    "icbc_city_name_legacy": "HARTLEY BAY",
    "vips_city_name": "DEWDNEY ISLAND"
  },
  {
    "city_code": "DAIS",
    "city_name": "DIANA ISLAND",
    "icbc_city_code": "DAIS",
    "icbc_city_name": "DIANA ISLAND",
    "icbc_city_name_legacy": "UCLUELET",
    "vips_city_name": "DIANA ISLAND"
  },
  {
    "city_code": "DGIS",
    "city_name": "DIGBY ISLAND",
    "icbc_city_code": "DGIS",
    "icbc_city_name": "DIGBY ISLAND",
    "icbc_city_name_legacy": "DIGBY ISLAND",
    "vips_city_name": "DIGBY ISLAND"
  },
  {
    "city_code": "DSCI",
    "city_name": "DISCOVERY ISLAND",
    "icbc_city_code": "DSCI",
    "icbc_city_name": "DISCOVERY ISLAND",
    "icbc_city_name_legacy": "VICTORIA",
    "vips_city_name": "DISCOVERY ISLAND"
  },
  {
    "city_code": "DORV",
    "city_name": "DOE RIVER",
    "icbc_city_code": "DORV",
    "icbc_city_name": "DOE RIVER",
    "icbc_city_name_legacy": "DOE RIVER",
    "vips_city_name": "DOE RIVER"
  },
  {
    "city_code": "DGCK",
    "city_name": "DOG CREEK",
    "icbc_city_code": "DGCK",
    "icbc_city_name": "DOG CREEK",
    "icbc_city_name_legacy": "DOG CREEK",
    "vips_city_name": "DOG CREEK"
  },
  {
    "city_code": "DGWD",
    "city_name": "DOGWOOD VALLEY",
    "icbc_city_code": "DGWD",
    "icbc_city_name": "DOGWOOD VALLEY",
    "icbc_city_name_legacy": "HOPE",
    "vips_city_name": "DOGWOOD VALLEY"
  },
  {
    "city_code": "DOIG",
    "city_name": "DOIG",
    "icbc_city_code": "DOIG",
    "icbc_city_name": "DOIG",
    "icbc_city_name_legacy": "FORT ST JOHN",
    "vips_city_name": "DOIG"
  },
  {
    "city_code": "DPIS",
    "city_name": "DOLPHIN ISLAND",
    "icbc_city_code": "DPIS",
    "icbc_city_name": "DOLPHIN ISLAND",
    "icbc_city_name_legacy": "KITKATLA",
    "vips_city_name": "DOLPHIN ISLAND"
  },
  {
    "city_code": "DMCK",
    "city_name": "DOME CREEK",
    "icbc_city_code": "DMCK",
    "icbc_city_name": "DOME CREEK",
    "icbc_city_name_legacy": "DOME CREEK",
    "vips_city_name": "DOME CREEK"
  },
  {
    "city_code": "DNLD",
    "city_name": "DONALD",
    "icbc_city_code": "DNLD",
    "icbc_city_name": "DONALD",
    "icbc_city_name_legacy": "DONALD",
    "vips_city_name": "DONALD"
  },
  {
    "city_code": "DMLG",
    "city_name": "DONALD LANDING",
    "icbc_city_code": "DMLG",
    "icbc_city_name": "DONALD LANDING",
    "icbc_city_name_legacy": "BURNS LAKE",
    "vips_city_name": "DONALD LANDING"
  },
  {
    "city_code": "DGLK",
    "city_name": "DOUGLAS LAKE",
    "icbc_city_code": "DGLK",
    "icbc_city_name": "DOUGLAS LAKE",
    "icbc_city_name_legacy": "DOUGLAS LAKE",
    "vips_city_name": "DOUGLAS LAKE"
  },
  {
    "city_code": "DISI",
    "city_name": "DOVE ISLAND IR",
    "icbc_city_code": "DISI",
    "icbc_city_name": "DOVE ISLAND IR",
    "icbc_city_name_legacy": "PORT HARDY",
    "vips_city_name": "DOVE ISLAND IR"
  },
  {
    "city_code": "DWRV",
    "city_name": "DRIFTWOOD RIVER",
    "icbc_city_code": "DWRV",
    "icbc_city_name": "DRIFTWOOD RIVER",
    "icbc_city_name_legacy": "NEW HAZELTON",
    "vips_city_name": "DRIFTWOOD RIVER"
  },
  {
    "city_code": "DNCN",
    "city_name": "DUNCAN",
    "icbc_city_code": "DNCN",
    "icbc_city_name": "DUNCAN",
    "icbc_city_name_legacy": "DUNCAN",
    "vips_city_name": "DUNCAN"
  },
  {
    "city_code": "DNLK",
    "city_name": "DUNCAN LAKE",
    "icbc_city_code": "DNLK",
    "icbc_city_name": "DUNCAN LAKE",
    "icbc_city_name_legacy": "KASLO",
    "vips_city_name": "DUNCAN LAKE"
  },
  {
    "city_code": "DDIS",
    "city_name": "DUNDAS ISLAND",
    "icbc_city_code": "DDIS",
    "icbc_city_name": "DUNDAS ISLAND",
    "icbc_city_name_legacy": "PRINCE RUPERT",
    "vips_city_name": "DUNDAS ISLAND"
  },
  {
    "city_code": "DUNK",
    "city_name": "DUNKLEY",
    "icbc_city_code": "DUNK",
    "icbc_city_name": "DUNKLEY",
    "icbc_city_name_legacy": "QUESNEL",
    "vips_city_name": "DUNKLEY"
  },
  {
    "city_code": "DULK",
    "city_name": "DUNN LAKE",
    "icbc_city_code": "DULK",
    "icbc_city_name": "DUNN LAKE",
    "icbc_city_name_legacy": "LITTLE FORT",
    "vips_city_name": "DUNN LAKE"
  },
  {
    "city_code": "DNSR",
    "city_name": "DUNSTER",
    "icbc_city_code": "DNSR",
    "icbc_city_name": "DUNSTER",
    "icbc_city_name_legacy": "DUNSTER",
    "vips_city_name": "DUNSTER"
  },
  {
    "city_code": "EABY",
    "city_name": "EAGLE BAY",
    "icbc_city_code": "EABY",
    "icbc_city_name": "EAGLE BAY",
    "icbc_city_name_legacy": "EAGLE BAY",
    "vips_city_name": "EAGLE BAY"
  },
  {
    "city_code": "EACK",
    "city_name": "EAGLE CREEK",
    "icbc_city_code": "EACK",
    "icbc_city_name": "EAGLE CREEK",
    "icbc_city_name_legacy": "EAGLE CREEK",
    "vips_city_name": "EAGLE CREEK"
  },
  {
    "city_code": "EBRL",
    "city_name": "EAST BARRIERE LAKE",
    "icbc_city_code": "EBRL",
    "icbc_city_name": "EAST BARRIERE LAKE",
    "icbc_city_name_legacy": "BARRIERE",
    "vips_city_name": "EAST BARRIERE LAKE"
  },
  {
    "city_code": "EBLK",
    "city_name": "EAST BLACKPOOL",
    "icbc_city_code": "EBLK",
    "icbc_city_name": "EAST BLACKPOOL",
    "icbc_city_name_legacy": "EAST BLACKPOOL",
    "vips_city_name": "EAST BLACKPOOL"
  },
  {
    "city_code": "EAPI",
    "city_name": "EAST PINE",
    "icbc_city_code": "EAPI",
    "icbc_city_name": "EAST PINE",
    "icbc_city_name_legacy": "EAST PINE",
    "vips_city_name": "EAST PINE"
  },
  {
    "city_code": "ESMA",
    "city_name": "EAST SALMON ARM",
    "icbc_city_code": "ESMA",
    "icbc_city_name": "EAST SALMON ARM",
    "icbc_city_name_legacy": "SALMON ARM",
    "vips_city_name": "EAST SALMON ARM"
  },
  {
    "city_code": "ESOK",
    "city_name": "EAST SOOKE",
    "icbc_city_code": "ESOK",
    "icbc_city_name": "EAST SOOKE",
    "icbc_city_name_legacy": "SOOKE",
    "vips_city_name": "EAST SOOKE"
  },
  {
    "city_code": "EDIS",
    "city_name": "EDEN ISLAND",
    "icbc_city_code": "EDIS",
    "icbc_city_name": "EDEN ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "EDEN ISLAND"
  },
  {
    "city_code": "EDWR",
    "city_name": "EDGEWATER",
    "icbc_city_code": "EDWR",
    "icbc_city_name": "EDGEWATER",
    "icbc_city_name_legacy": "EDGEWATER",
    "vips_city_name": "EDGEWATER"
  },
  {
    "city_code": "EDWD",
    "city_name": "EDGEWOOD",
    "icbc_city_code": "EDWD",
    "icbc_city_name": "EDGEWOOD",
    "icbc_city_name_legacy": "EDGEWOOD",
    "vips_city_name": "EDGEWOOD"
  },
  {
    "city_code": "EKIS",
    "city_name": "EDWARD KING ISLAND",
    "icbc_city_code": "EKIS",
    "icbc_city_name": "EDWARD KING ISLAND",
    "icbc_city_name_legacy": "BELLA BELLA",
    "vips_city_name": "EDWARD KING ISLAND"
  },
  {
    "city_code": "EGMT",
    "city_name": "EGMONT",
    "icbc_city_code": "EGMT",
    "icbc_city_name": "EGMONT",
    "icbc_city_name_legacy": "EGMONT",
    "vips_city_name": "EGMONT"
  },
  {
    "city_code": "EKFR",
    "city_name": "ELKFORD",
    "icbc_city_code": "EKFR",
    "icbc_city_name": "ELKFORD",
    "icbc_city_name_legacy": "ELKFORD",
    "vips_city_name": "ELKFORD"
  },
  {
    "city_code": "ELKO",
    "city_name": "ELKO",
    "icbc_city_code": "ELKO",
    "icbc_city_name": "ELKO",
    "icbc_city_name_legacy": "ELKO",
    "vips_city_name": "ELKO"
  },
  {
    "city_code": "ELCP",
    "city_name": "ELSWORTH CAMP",
    "icbc_city_code": "ELCP",
    "icbc_city_name": "ELSWORTH CAMP",
    "icbc_city_name_legacy": "STEWART",
    "vips_city_name": "ELSWORTH CAMP"
  },
  {
    "city_code": "ENDA",
    "city_name": "ENDAKO",
    "icbc_city_code": "ENDA",
    "icbc_city_name": "ENDAKO",
    "icbc_city_name_legacy": "ENDAKO",
    "vips_city_name": "ENDAKO"
  },
  {
    "city_code": "EDBY",
    "city_name": "ENDERBY",
    "icbc_city_code": "EDBY",
    "icbc_city_name": "ENDERBY",
    "icbc_city_name_legacy": "ENDERBY",
    "vips_city_name": "ENDERBY"
  },
  {
    "city_code": "EGEN",
    "city_name": "ENGEN",
    "icbc_city_code": "EGEN",
    "icbc_city_name": "ENGEN",
    "icbc_city_name_legacy": "ENGEN",
    "vips_city_name": "ENGEN"
  },
  {
    "city_code": "ERIC",
    "city_name": "ERICKSON",
    "icbc_city_code": "ERIC",
    "icbc_city_name": "ERICKSON",
    "icbc_city_name_legacy": "ERICKSON",
    "vips_city_name": "ERICKSON"
  },
  {
    "city_code": "ERIE",
    "city_name": "ERIE",
    "icbc_city_code": "ERIE",
    "icbc_city_name": "ERIE",
    "icbc_city_name_legacy": "ERIE",
    "vips_city_name": "ERIE"
  },
  {
    "city_code": "ERRN",
    "city_name": "ERRINGTON",
    "icbc_city_code": "ERRN",
    "icbc_city_name": "ERRINGTON",
    "icbc_city_name_legacy": "ERRINGTON",
    "vips_city_name": "ERRINGTON"
  },
  {
    "city_code": "EQMT",
    "city_name": "ESQUIMALT",
    "icbc_city_code": "EQMT",
    "icbc_city_name": "ESQUIMALT",
    "icbc_city_name_legacy": "ESQUIMALT",
    "vips_city_name": "ESQUIMALT"
  },
  {
    "city_code": "FRSP",
    "city_name": "FAIRMONT HOT SPRINGS",
    "icbc_city_code": "FRSP",
    "icbc_city_name": "FAIRMONT HOT SPRINGS",
    "icbc_city_name_legacy": "FAIRMONT HOT SP",
    "vips_city_name": "FAIRMONT HOT SPRINGS"
  },
  {
    "city_code": "FKLD",
    "city_name": "FALKLAND",
    "icbc_city_code": "FKLD",
    "icbc_city_name": "FALKLAND",
    "icbc_city_name_legacy": "FALKLAND",
    "vips_city_name": "FALKLAND"
  },
  {
    "city_code": "FYBA",
    "city_name": "FANNY BAY",
    "icbc_city_code": "FYBA",
    "icbc_city_name": "FANNY BAY",
    "icbc_city_name_legacy": "FANNY BAY",
    "vips_city_name": "FANNY BAY"
  },
  {
    "city_code": "FAIS",
    "city_name": "FARADAY ISLAND",
    "icbc_city_code": "FAIS",
    "icbc_city_name": "FARADAY ISLAND",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "FARADAY ISLAND"
  },
  {
    "city_code": "FRTN",
    "city_name": "FARMINGTON",
    "icbc_city_code": "FRTN",
    "icbc_city_name": "FARMINGTON",
    "icbc_city_name_legacy": "FARMINGTON",
    "vips_city_name": "FARMINGTON"
  },
  {
    "city_code": "FRIS",
    "city_name": "FARRANT ISLAND",
    "icbc_city_code": "FRIS",
    "icbc_city_name": "FARRANT ISLAND",
    "icbc_city_name_legacy": "HARTLEY BAY",
    "vips_city_name": "FARRANT ISLAND"
  },
  {
    "city_code": "FLCK",
    "city_name": "FARRELL CREEK",
    "icbc_city_code": "FLCK",
    "icbc_city_name": "FARRELL CREEK",
    "icbc_city_name_legacy": "FARRELL CREEK",
    "vips_city_name": "FARRELL CREEK"
  },
  {
    "city_code": "FAQR",
    "city_name": "FAUQUIER",
    "icbc_city_code": "FAQR",
    "icbc_city_name": "FAUQUIER",
    "icbc_city_name_legacy": "FAUQUIER",
    "vips_city_name": "FAUQUIER"
  },
  {
    "city_code": "FLHT",
    "city_name": "FELLERS HEIGHTS",
    "icbc_city_code": "FLHT",
    "icbc_city_name": "FELLERS HEIGHTS",
    "icbc_city_name_legacy": "DAWSON CREEK",
    "vips_city_name": "FELLERS HEIGHTS"
  },
  {
    "city_code": "FDTB",
    "city_name": "FERNDALE-TABOR",
    "icbc_city_code": "FDTB",
    "icbc_city_name": "FERNDALE-TABOR",
    "icbc_city_name_legacy": "FERNDALE",
    "vips_city_name": "FERNDALE-TABOR"
  },
  {
    "city_code": "FERN",
    "city_name": "FERNIE",
    "icbc_city_code": "FERN",
    "icbc_city_name": "FERNIE",
    "icbc_city_name_legacy": "FERNIE",
    "vips_city_name": "FERNIE"
  },
  {
    "city_code": "FILD",
    "city_name": "FIELD",
    "icbc_city_code": "FILD",
    "icbc_city_name": "FIELD",
    "icbc_city_name_legacy": "FIELD",
    "vips_city_name": "FIELD"
  },
  {
    "city_code": "FNIS",
    "city_name": "FIN ISLAND",
    "icbc_city_code": "FNIS",
    "icbc_city_name": "FIN ISLAND",
    "icbc_city_name_legacy": "HARTLEY BAY",
    "vips_city_name": "FIN ISLAND"
  },
  {
    "city_code": "FIRE",
    "city_name": "FIRESIDE",
    "icbc_city_code": "FIRE",
    "icbc_city_name": "FIRESIDE",
    "icbc_city_name_legacy": "FIRESIDE",
    "vips_city_name": "FIRESIDE"
  },
  {
    "city_code": "FIRV",
    "city_name": "FIRVALE",
    "icbc_city_code": "FIRV",
    "icbc_city_name": "FIRVALE",
    "icbc_city_name_legacy": "BELLA COOLA",
    "vips_city_name": "FIRVALE"
  },
  {
    "city_code": "FLAT",
    "city_name": "FLATHEAD",
    "icbc_city_code": "FLAT",
    "icbc_city_name": "FLATHEAD",
    "icbc_city_name_legacy": "FLATHEAD",
    "vips_city_name": "FLATHEAD"
  },
  {
    "city_code": "FTRK",
    "city_name": "FLATROCK",
    "icbc_city_code": "FTRK",
    "icbc_city_name": "FLATROCK",
    "icbc_city_name_legacy": "FORT ST JOHN",
    "vips_city_name": "FLATROCK"
  },
  {
    "city_code": "FLIS",
    "city_name": "FLEMING ISLAND",
    "icbc_city_code": "FLIS",
    "icbc_city_name": "FLEMING ISLAND",
    "icbc_city_name_legacy": "UCLUELET",
    "vips_city_name": "FLEMING ISLAND"
  },
  {
    "city_code": "FSIS",
    "city_name": "FLORES ISLAND",
    "icbc_city_code": "FSIS",
    "icbc_city_name": "FLORES ISLAND",
    "icbc_city_name_legacy": "AHOUSAT",
    "vips_city_name": "FLORES ISLAND"
  },
  {
    "city_code": "FLYI",
    "city_name": "FLY ISLAND IR",
    "icbc_city_code": "FLYI",
    "icbc_city_name": "FLY ISLAND IR",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "FLY ISLAND IR"
  },
  {
    "city_code": "FONT",
    "city_name": "FONTAS",
    "icbc_city_code": "FONT",
    "icbc_city_name": "FONTAS",
    "icbc_city_name_legacy": "FORT NELSON",
    "vips_city_name": "FONTAS"
  },
  {
    "city_code": "FMFL",
    "city_name": "FOREMAN FLATS",
    "icbc_city_code": "FMFL",
    "icbc_city_name": "FOREMAN FLATS",
    "icbc_city_name_legacy": "FOREMAN",
    "vips_city_name": "FOREMAN FLATS"
  },
  {
    "city_code": "FRGV",
    "city_name": "FOREST GROVE",
    "icbc_city_code": "FRGV",
    "icbc_city_name": "FOREST GROVE",
    "icbc_city_name_legacy": "FOREST GROVE",
    "vips_city_name": "FOREST GROVE"
  },
  {
    "city_code": "FGCK",
    "city_name": "FORGETMENOT CREEK",
    "icbc_city_code": "FGCK",
    "icbc_city_name": "FORGETMENOT CREEK",
    "icbc_city_name_legacy": "MCBRIDE",
    "vips_city_name": "FORGETMENOT CREEK"
  },
  {
    "city_code": "FBAB",
    "city_name": "FORT BABINE",
    "icbc_city_code": "FBAB",
    "icbc_city_name": "FORT BABINE",
    "icbc_city_name_legacy": "NEW HAZELTON",
    "vips_city_name": "FORT BABINE"
  },
  {
    "city_code": "FFRA",
    "city_name": "FORT FRASER",
    "icbc_city_code": "FFRA",
    "icbc_city_name": "FORT FRASER",
    "icbc_city_name_legacy": "FORT FRASER",
    "vips_city_name": "FORT FRASER"
  },
  {
    "city_code": "FGRG",
    "city_name": "FORT GEORGE NO 2",
    "icbc_city_code": "FGRG",
    "icbc_city_name": "FORT GEORGE NO 2",
    "icbc_city_name_legacy": "PRINCE GEORGE",
    "vips_city_name": "FORT GEORGE NO 2"
  },
  {
    "city_code": "FNEL",
    "city_name": "FORT NELSON",
    "icbc_city_code": "FNEL",
    "icbc_city_name": "FORT NELSON",
    "icbc_city_name_legacy": "FORT NELSON",
    "vips_city_name": "FORT NELSON"
  },
  {
    "city_code": "FNEI",
    "city_name": "FORT NELSON IR",
    "icbc_city_code": "FNEI",
    "icbc_city_name": "FORT NELSON IR",
    "icbc_city_name_legacy": "FORT NELSON",
    "vips_city_name": "FORT NELSON IR"
  },
  {
    "city_code": "FSJA",
    "city_name": "FORT ST JAMES",
    "icbc_city_code": "FSJA",
    "icbc_city_name": "FORT ST JAMES",
    "icbc_city_name_legacy": "FORT ST JAMES",
    "vips_city_name": "FORT ST JAMES"
  },
  {
    "city_code": "FSJO",
    "city_name": "FORT ST JOHN",
    "icbc_city_code": "FSJO",
    "icbc_city_name": "FORT ST JOHN",
    "icbc_city_name_legacy": "FORT ST JOHN",
    "vips_city_name": "FORT ST JOHN"
  },
  {
    "city_code": "FTST",
    "city_name": "FORT STEELE",
    "icbc_city_code": "FTST",
    "icbc_city_name": "FORT STEELE",
    "icbc_city_name_legacy": "FORT STEELE",
    "vips_city_name": "FORT STEELE"
  },
  {
    "city_code": "FWAR",
    "city_name": "FORT WARE",
    "icbc_city_code": "FWAR",
    "icbc_city_name": "FORT WARE",
    "icbc_city_name_legacy": "FORT WARE",
    "vips_city_name": "FORT WARE"
  },
  {
    "city_code": "FCLK",
    "city_name": "FRANCOIS LAKE",
    "icbc_city_code": "FCLK",
    "icbc_city_name": "FRANCOIS LAKE",
    "icbc_city_name_legacy": "FRANCOIS LAKE",
    "vips_city_name": "FRANCOIS LAKE"
  },
  {
    "city_code": "FRAS",
    "city_name": "FRASER",
    "icbc_city_code": "FRAS",
    "icbc_city_name": "FRASER",
    "icbc_city_name_legacy": "ATLIN",
    "vips_city_name": "FRASER"
  },
  {
    "city_code": "FRLK",
    "city_name": "FRASER LAKE",
    "icbc_city_code": "FRLK",
    "icbc_city_name": "FRASER LAKE",
    "icbc_city_name_legacy": "FRASER LAKE",
    "vips_city_name": "FRASER LAKE"
  },
  {
    "city_code": "FRDK",
    "city_name": "FREDERICK",
    "icbc_city_code": "FRDK",
    "icbc_city_name": "FREDERICK",
    "icbc_city_name_legacy": "KAMLOOPS",
    "vips_city_name": "FREDERICK"
  },
  {
    "city_code": "FRVA",
    "city_name": "FRUITVALE",
    "icbc_city_code": "FRVA",
    "icbc_city_name": "FRUITVALE",
    "icbc_city_name_legacy": "FRUITVALE",
    "vips_city_name": "FRUITVALE"
  },
  {
    "city_code": "FURY",
    "city_name": "FURRY CREEK",
    "icbc_city_code": "FURY",
    "icbc_city_name": "FURRY CREEK",
    "icbc_city_name_legacy": "FURRY CREEK",
    "vips_city_name": "FURRY CREEK"
  },
  {
    "city_code": "GBIS",
    "city_name": "GABRIOLA ISLAND",
    "icbc_city_code": "GBIS",
    "icbc_city_name": "GABRIOLA ISLAND",
    "icbc_city_name_legacy": "GABRIOLA ISLAND",
    "vips_city_name": "GABRIOLA ISLAND"
  },
  {
    "city_code": "GABY",
    "city_name": "GALENA BAY",
    "icbc_city_code": "GABY",
    "icbc_city_name": "GALENA BAY",
    "icbc_city_name_legacy": "NAKUSP",
    "vips_city_name": "GALENA BAY"
  },
  {
    "city_code": "GLIS",
    "city_name": "GALIANO ISLAND",
    "icbc_city_code": "GLIS",
    "icbc_city_name": "GALIANO ISLAND",
    "icbc_city_name_legacy": "GALIANO ISLAND",
    "vips_city_name": "GALIANO ISLAND"
  },
  {
    "city_code": "GLWY",
    "city_name": "GALLOWAY",
    "icbc_city_code": "GLWY",
    "icbc_city_name": "GALLOWAY",
    "icbc_city_name_legacy": "GALLOWAY",
    "vips_city_name": "GALLOWAY"
  },
  {
    "city_code": "GMBR",
    "city_name": "GAMBIER ISLAND",
    "icbc_city_code": "GMBR",
    "icbc_city_name": "GAMBIER ISLAND",
    "icbc_city_name_legacy": "GAMBIER ISLAND",
    "vips_city_name": "GAMBIER ISLAND"
  },
  {
    "city_code": "GARH",
    "city_name": "GANG RANCH",
    "icbc_city_code": "GARH",
    "icbc_city_name": "GANG RANCH",
    "icbc_city_name_legacy": "GANG RANCH",
    "vips_city_name": "GANG RANCH"
  },
  {
    "city_code": "GDBA",
    "city_name": "GARDEN BAY",
    "icbc_city_code": "GDBA",
    "icbc_city_name": "GARDEN BAY",
    "icbc_city_name_legacy": "GARDEN BAY",
    "vips_city_name": "GARDEN BAY"
  },
  {
    "city_code": "GRBD",
    "city_name": "GARIBALDI PARK",
    "icbc_city_code": "GRBD",
    "icbc_city_name": "GARIBALDI PARK",
    "icbc_city_name_legacy": "WHISTLER",
    "vips_city_name": "GARIBALDI PARK"
  },
  {
    "city_code": "GNLL",
    "city_name": "GENELLE",
    "icbc_city_code": "GNLL",
    "icbc_city_name": "GENELLE",
    "icbc_city_name_legacy": "GENELLE",
    "vips_city_name": "GENELLE"
  },
  {
    "city_code": "GMLG",
    "city_name": "GERMANSEN LANDING",
    "icbc_city_code": "GMLG",
    "icbc_city_name": "GERMANSEN LANDING",
    "icbc_city_name_legacy": "GERMANSEN LANDI",
    "vips_city_name": "GERMANSEN LANDING"
  },
  {
    "city_code": "GBLG",
    "city_name": "GIBSON ISLAND",
    "icbc_city_code": "GBLG",
    "icbc_city_name": "GIBSON ISLAND",
    "icbc_city_name_legacy": "KITKATLA",
    "vips_city_name": "GIBSON ISLAND"
  },
  {
    "city_code": "GIB",
    "city_name": "GIBSONS",
    "icbc_city_code": "GIB",
    "icbc_city_name": "GIBSONS",
    "icbc_city_name_legacy": "GIBSONS",
    "vips_city_name": "GIBSONS"
  },
  {
    "city_code": "GIIS",
    "city_name": "GIL ISLAND",
    "icbc_city_code": "GIIS",
    "icbc_city_name": "GIL ISLAND",
    "icbc_city_name_legacy": "HARTLEY BAY",
    "vips_city_name": "GIL ISLAND"
  },
  {
    "city_code": "GFIS",
    "city_name": "GILFORD ISLAND",
    "icbc_city_code": "GFIS",
    "icbc_city_name": "GILFORD ISLAND",
    "icbc_city_name_legacy": "GILFORD ISLAND",
    "vips_city_name": "GILFORD ISLAND"
  },
  {
    "city_code": "GLSB",
    "city_name": "GILLIES BAY",
    "icbc_city_code": "GLSB",
    "icbc_city_name": "GILLIES BAY",
    "icbc_city_name_legacy": "GILLIES BAY",
    "vips_city_name": "GILLIES BAY"
  },
  {
    "city_code": "GINX",
    "city_name": "GINGOLX",
    "icbc_city_code": "GINX",
    "icbc_city_name": "GINGOLX",
    "icbc_city_name_legacy": "KINCOLITH",
    "vips_city_name": "GINGOLX"
  },
  {
    "city_code": "GSCM",
    "city_name": "GISCOME",
    "icbc_city_code": "GSCM",
    "icbc_city_name": "GISCOME",
    "icbc_city_name_legacy": "GISCOME",
    "vips_city_name": "GISCOME"
  },
  {
    "city_code": "GTMX",
    "city_name": "GITANMAAX",
    "icbc_city_code": "GTMX",
    "icbc_city_name": "GITANMAAX",
    "icbc_city_name_legacy": "GITANMAAX",
    "vips_city_name": "GITANMAAX"
  },
  {
    "city_code": "GTYW",
    "city_name": "GITANYOW",
    "icbc_city_code": "GTYW",
    "icbc_city_name": "GITANYOW",
    "icbc_city_name_legacy": "NEW HAZELTON",
    "vips_city_name": "GITANYOW"
  },
  {
    "city_code": "GYGK",
    "city_name": "GITSEGUKLA",
    "icbc_city_code": "GYGK",
    "icbc_city_name": "GITSEGUKLA",
    "icbc_city_name_legacy": "GITSEGUKLA",
    "vips_city_name": "GITSEGUKLA"
  },
  {
    "city_code": "GTWK",
    "city_name": "GITWANGAK",
    "icbc_city_code": "GTWK",
    "icbc_city_name": "GITWANGAK",
    "icbc_city_name_legacy": "NEW HAZELTON",
    "vips_city_name": "GITWANGAK"
  },
  {
    "city_code": "GTWW",
    "city_name": "GITWINKSIHLKW",
    "icbc_city_code": "GTWW",
    "icbc_city_name": "GITWINKSIHLKW",
    "icbc_city_name_legacy": "GITWINKSIHLKW",
    "vips_city_name": "GITWINKSIHLKW"
  },
  {
    "city_code": "GLAD",
    "city_name": "GLADE",
    "icbc_city_code": "GLAD",
    "icbc_city_name": "GLADE",
    "icbc_city_name_legacy": "GLADE",
    "vips_city_name": "GLADE"
  },
  {
    "city_code": "GLEN",
    "city_name": "GLENORA",
    "icbc_city_code": "GLEN",
    "icbc_city_name": "GLENORA",
    "icbc_city_name_legacy": "GLENORA",
    "vips_city_name": "GLENORA"
  },
  {
    "city_code": "GLMP",
    "city_name": "GLIMPSE LAKE",
    "icbc_city_code": "GLMP",
    "icbc_city_name": "GLIMPSE LAKE",
    "icbc_city_name_legacy": "QUILCHENA",
    "vips_city_name": "GLIMPSE LAKE"
  },
  {
    "city_code": "GLDB",
    "city_name": "GOLD BRIDGE",
    "icbc_city_code": "GLDB",
    "icbc_city_name": "GOLD BRIDGE",
    "icbc_city_name_legacy": "GOLD BRIDGE",
    "vips_city_name": "GOLD BRIDGE"
  },
  {
    "city_code": "GLRV",
    "city_name": "GOLD RIVER",
    "icbc_city_code": "GLRV",
    "icbc_city_name": "GOLD RIVER",
    "icbc_city_name_legacy": "GOLD RIVER",
    "vips_city_name": "GOLD RIVER"
  },
  {
    "city_code": "GLDN",
    "city_name": "GOLDEN",
    "icbc_city_code": "GLDN",
    "icbc_city_name": "GOLDEN",
    "icbc_city_name_legacy": "GOLDEN",
    "vips_city_name": "GOLDEN"
  },
  {
    "city_code": "GLDP",
    "city_name": "GOLDEN EARS PARK",
    "icbc_city_code": "GLDP",
    "icbc_city_name": "GOLDEN EARS PARK",
    "icbc_city_name_legacy": "COQUITLAM",
    "vips_city_name": "GOLDEN EARS PARK"
  },
  {
    "city_code": "GHLK",
    "city_name": "GOOD HOPE LAKE",
    "icbc_city_code": "GHLK",
    "icbc_city_name": "GOOD HOPE LAKE",
    "icbc_city_name_legacy": "GOODHOPE LAKE",
    "vips_city_name": "GOOD HOPE LAKE"
  },
  {
    "city_code": "GDLW",
    "city_name": "GOODLOW",
    "icbc_city_code": "GDLW",
    "icbc_city_name": "GOODLOW",
    "icbc_city_name_legacy": "GOODLOW",
    "vips_city_name": "GOODLOW"
  },
  {
    "city_code": "GSIS",
    "city_name": "GOOSE ISLAND",
    "icbc_city_code": "GSIS",
    "icbc_city_name": "GOOSE ISLAND",
    "icbc_city_name_legacy": "COQUITLAM",
    "vips_city_name": "GOOSE ISLAND"
  },
  {
    "city_code": "GHIS",
    "city_name": "GOSCHEN ISLAND",
    "icbc_city_code": "GHIS",
    "icbc_city_name": "GOSCHEN ISLAND",
    "icbc_city_name_legacy": "KITKATLA",
    "vips_city_name": "GOSCHEN ISLAND"
  },
  {
    "city_code": "GOIS",
    "city_name": "GOSSIP ISLAND",
    "icbc_city_code": "GOIS",
    "icbc_city_name": "GOSSIP ISLAND",
    "icbc_city_name_legacy": "GOSSIP ISLAND",
    "vips_city_name": "GOSSIP ISLAND"
  },
  {
    "city_code": "GDFR",
    "city_name": "GRAND FORKS",
    "icbc_city_code": "GDFR",
    "icbc_city_name": "GRAND FORKS",
    "icbc_city_name_legacy": "GRAND FORKS",
    "vips_city_name": "GRAND FORKS"
  },
  {
    "city_code": "GRBH",
    "city_name": "GRANDVIEW BENCH",
    "icbc_city_code": "GRBH",
    "icbc_city_name": "GRANDVIEW BENCH",
    "icbc_city_name_legacy": "SALMON ARM",
    "vips_city_name": "GRANDVIEW BENCH"
  },
  {
    "city_code": "GRAN",
    "city_name": "GRANISLE",
    "icbc_city_code": "GRAN",
    "icbc_city_name": "GRANISLE",
    "icbc_city_name_legacy": "GRANISLE",
    "vips_city_name": "GRANISLE"
  },
  {
    "city_code": "GRMR",
    "city_name": "GRASMERE",
    "icbc_city_code": "GRMR",
    "icbc_city_name": "GRASMERE",
    "icbc_city_name_legacy": "GRASMERE",
    "vips_city_name": "GRASMERE"
  },
  {
    "city_code": "GLIR",
    "city_name": "GRASSLANDS IR",
    "icbc_city_code": "GLIR",
    "icbc_city_name": "GRASSLANDS IR",
    "icbc_city_name_legacy": "ASHCROFT",
    "vips_city_name": "GRASSLANDS IR"
  },
  {
    "city_code": "GIIR",
    "city_name": "GRASSY ISLAND IR",
    "icbc_city_code": "GIIR",
    "icbc_city_name": "GRASSY ISLAND IR",
    "icbc_city_name_legacy": "GOLD RIVER",
    "vips_city_name": "GRASSY ISLAND IR"
  },
  {
    "city_code": "GRPL",
    "city_name": "GRASSY PLAINS",
    "icbc_city_code": "GRPL",
    "icbc_city_name": "GRASSY PLAINS",
    "icbc_city_name_legacy": "GRASSEY PLAINS",
    "vips_city_name": "GRASSY PLAINS"
  },
  {
    "city_code": "GRCK",
    "city_name": "GRAY CREEK",
    "icbc_city_code": "GRCK",
    "icbc_city_name": "GRAY CREEK",
    "icbc_city_name_legacy": "GRAY CREEK",
    "vips_city_name": "GRAY CREEK"
  },
  {
    "city_code": "GBLK",
    "city_name": "GREAT BEAVER LAKE",
    "icbc_city_code": "GBLK",
    "icbc_city_name": "GREAT BEAVER LAKE",
    "icbc_city_name_legacy": "FORT ST JAMES",
    "vips_city_name": "GREAT BEAVER LAKE"
  },
  {
    "city_code": "GREL",
    "city_name": "GREEN LAKE",
    "icbc_city_code": "GREL",
    "icbc_city_name": "GREEN LAKE",
    "icbc_city_name_legacy": "LONE BUTTE",
    "vips_city_name": "GREEN LAKE"
  },
  {
    "city_code": "GRVL",
    "city_name": "GREENVILLE",
    "icbc_city_code": "GRVL",
    "icbc_city_name": "GREENVILLE",
    "icbc_city_name_legacy": "GREENVILLE",
    "vips_city_name": "GREENVILLE"
  },
  {
    "city_code": "GRWD",
    "city_name": "GREENWOOD",
    "icbc_city_code": "GRWD",
    "icbc_city_name": "GREENWOOD",
    "icbc_city_name_legacy": "GREENWOOD",
    "vips_city_name": "GREENWOOD"
  },
  {
    "city_code": "GGIS",
    "city_name": "GREGORY ISLAND",
    "icbc_city_code": "GGIS",
    "icbc_city_name": "GREGORY ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "GREGORY ISLAND"
  },
  {
    "city_code": "GRBI",
    "city_name": "GRIBBELL ISLAND",
    "icbc_city_code": "GRBI",
    "icbc_city_name": "GRIBBELL ISLAND",
    "icbc_city_name_legacy": "HARTLEY BAY",
    "vips_city_name": "GRIBBELL ISLAND"
  },
  {
    "city_code": "GRRD",
    "city_name": "GRINDROD",
    "icbc_city_code": "GRRD",
    "icbc_city_name": "GRINDROD",
    "icbc_city_name_legacy": "GRINDROD",
    "vips_city_name": "GRINDROD"
  },
  {
    "city_code": "GRBR",
    "city_name": "GROUNDBIRCH",
    "icbc_city_code": "GRBR",
    "icbc_city_name": "GROUNDBIRCH",
    "icbc_city_name_legacy": "GROUNDBIRCH",
    "vips_city_name": "GROUNDBIRCH"
  },
  {
    "city_code": "GUND",
    "city_name": "GUNDY",
    "icbc_city_code": "GUND",
    "icbc_city_name": "GUNDY",
    "icbc_city_name_legacy": "GUNDY",
    "vips_city_name": "GUNDY"
  },
  {
    "city_code": "GDIS",
    "city_name": "GURD ISLAND",
    "icbc_city_code": "GDIS",
    "icbc_city_name": "GURD ISLAND",
    "icbc_city_name_legacy": "KITKATLA",
    "vips_city_name": "GURD ISLAND"
  },
  {
    "city_code": "HAGG",
    "city_name": "HAGENSBORG",
    "icbc_city_code": "HAGG",
    "icbc_city_name": "HAGENSBORG",
    "icbc_city_name_legacy": "HAGENSBORG",
    "vips_city_name": "HAGENSBORG"
  },
  {
    "city_code": "HAGW",
    "city_name": "HAGWILGET",
    "icbc_city_code": "HAGW",
    "icbc_city_name": "HAGWILGET",
    "icbc_city_name_legacy": "NEW HAZELTON",
    "vips_city_name": "HAGWILGET"
  },
  {
    "city_code": "QCIS",
    "city_name": "QUEEN CHARLOTTE ISLANDS",
    "icbc_city_code": "QCIS",
    "icbc_city_name": "QUEEN CHARLOTTE ISLANDS",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "QUEEN CHARLOTTE ISLANDS"
  },
  {
    "city_code": "HMB",
    "city_name": "HALFMOON BAY",
    "icbc_city_code": "HMB",
    "icbc_city_name": "HALFMOON BAY",
    "icbc_city_name_legacy": "HALFMOON BAY",
    "vips_city_name": "HALFMOON BAY"
  },
  {
    "city_code": "HWRV",
    "city_name": "HALFWAY RIVER",
    "icbc_city_code": "HWRV",
    "icbc_city_name": "HALFWAY RIVER",
    "icbc_city_name_legacy": "HUDSON'S HOPE",
    "vips_city_name": "HALFWAY RIVER"
  },
  {
    "city_code": "HWRI",
    "city_name": "HALFWAY RIVER IR",
    "icbc_city_code": "HWRI",
    "icbc_city_name": "HALFWAY RIVER IR",
    "icbc_city_name_legacy": "HUDSON'S HOPE",
    "vips_city_name": "HALFWAY RIVER IR"
  },
  {
    "city_code": "HRPP",
    "city_name": "HAMBER PROVINCIAL PARK",
    "icbc_city_code": "HRPP",
    "icbc_city_name": "HAMBER PROVINCIAL PARK",
    "icbc_city_name_legacy": "GOLDEN",
    "vips_city_name": "HAMBER PROVINCIAL PARK"
  },
  {
    "city_code": "HNVL",
    "city_name": "HANCEVILLE",
    "icbc_city_code": "HNVL",
    "icbc_city_name": "HANCEVILLE",
    "icbc_city_name_legacy": "HANCEVILLE",
    "vips_city_name": "HANCEVILLE"
  },
  {
    "city_code": "HNIS",
    "city_name": "HANSON ISLAND",
    "icbc_city_code": "HNIS",
    "icbc_city_name": "HANSON ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "HANSON ISLAND"
  },
  {
    "city_code": "HDIS",
    "city_name": "HARBLEDOWN ISLAND",
    "icbc_city_code": "HDIS",
    "icbc_city_name": "HARBLEDOWN ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "HARBLEDOWN ISLAND"
  },
  {
    "city_code": "HWIS",
    "city_name": "HARDWICKE ISLAND",
    "icbc_city_code": "HWIS",
    "icbc_city_name": "HARDWICKE ISLAND",
    "icbc_city_name_legacy": "SAYWARD",
    "vips_city_name": "HARDWICKE ISLAND"
  },
  {
    "city_code": "HYIS",
    "city_name": "HARDY ISLAND",
    "icbc_city_code": "HYIS",
    "icbc_city_name": "HARDY ISLAND",
    "icbc_city_name_legacy": "POWELL RIVER",
    "vips_city_name": "HARDY ISLAND"
  },
  {
    "city_code": "HARR",
    "city_name": "HARRISON HOT SPRINGS",
    "icbc_city_code": "HARR",
    "icbc_city_name": "HARRISON HOT SPRINGS",
    "icbc_city_name_legacy": "HARRISON HOT SP",
    "vips_city_name": "HARRISON HOT SPRINGS"
  },
  {
    "city_code": "HRIS",
    "city_name": "HARRISON ISLAND",
    "icbc_city_code": "HRIS",
    "icbc_city_name": "HARRISON ISLAND",
    "icbc_city_name_legacy": "VICTORIA",
    "vips_city_name": "HARRISON ISLAND"
  },
  {
    "city_code": "HRLK",
    "city_name": "HARRISON LAKE",
    "icbc_city_code": "HRLK",
    "icbc_city_name": "HARRISON LAKE",
    "icbc_city_name_legacy": "HARRISON LAKE",
    "vips_city_name": "HARRISON LAKE"
  },
  {
    "city_code": "HRML",
    "city_name": "HARRISON MILLS",
    "icbc_city_code": "HRML",
    "icbc_city_name": "HARRISON MILLS",
    "icbc_city_name_legacy": "HARRISON MILLS",
    "vips_city_name": "HARRISON MILLS"
  },
  {
    "city_code": "HARP",
    "city_name": "HARROP",
    "icbc_city_code": "HARP",
    "icbc_city_name": "HARROP",
    "icbc_city_name_legacy": "HARROP",
    "vips_city_name": "HARROP"
  },
  {
    "city_code": "HYBY",
    "city_name": "HARTLEY BAY",
    "icbc_city_code": "HYBY",
    "icbc_city_name": "HARTLEY BAY",
    "icbc_city_name_legacy": "HARTLEY BAY",
    "vips_city_name": "HARTLEY BAY"
  },
  {
    "city_code": "HWDI",
    "city_name": "HARWOOD ISLAND",
    "icbc_city_code": "HWDI",
    "icbc_city_name": "HARWOOD ISLAND",
    "icbc_city_name_legacy": "POWELL RIVER",
    "vips_city_name": "HARWOOD ISLAND"
  },
  {
    "city_code": "HRFT",
    "city_name": "HASLER FLATS",
    "icbc_city_code": "HRFT",
    "icbc_city_name": "HASLER FLATS",
    "icbc_city_name_legacy": "CHETWYND",
    "vips_city_name": "HASLER FLATS"
  },
  {
    "city_code": "HATC",
    "city_name": "HAT CREEK",
    "icbc_city_code": "HATC",
    "icbc_city_name": "HAT CREEK",
    "icbc_city_name_legacy": "HAT CREEK",
    "vips_city_name": "HAT CREEK"
  },
  {
    "city_code": "HCIR",
    "city_name": "HAT CREEK IR",
    "icbc_city_code": "HCIR",
    "icbc_city_name": "HAT CREEK IR",
    "icbc_city_name_legacy": "ASHCROFT",
    "vips_city_name": "HAT CREEK IR"
  },
  {
    "city_code": "HTZC",
    "city_name": "HATZIC",
    "icbc_city_code": "HTZC",
    "icbc_city_name": "HATZIC",
    "icbc_city_name_legacy": "HATZIC",
    "vips_city_name": "HATZIC"
  },
  {
    "city_code": "HBIS",
    "city_name": "HAWKESBURY ISLAND",
    "icbc_city_code": "HBIS",
    "icbc_city_name": "HAWKESBURY ISLAND",
    "icbc_city_name_legacy": "HARTLEY BAY",
    "vips_city_name": "HAWKESBURY ISLAND"
  },
  {
    "city_code": "HAZL",
    "city_name": "HAZELTON",
    "icbc_city_code": "HAZL",
    "icbc_city_name": "HAZELTON",
    "icbc_city_name_legacy": "HAZELTON",
    "vips_city_name": "HAZELTON"
  },
  {
    "city_code": "HAZR",
    "city_name": "HAZELTON RURAL",
    "icbc_city_code": "HAZR",
    "icbc_city_name": "HAZELTON RURAL",
    "icbc_city_name_legacy": "HAZELTON",
    "vips_city_name": "HAZELTON RURAL"
  },
  {
    "city_code": "HCTI",
    "city_name": "HECATE ISLAND",
    "icbc_city_code": "HCTI",
    "icbc_city_name": "HECATE ISLAND",
    "icbc_city_name_legacy": "BELLA BELLA",
    "vips_city_name": "HECATE ISLAND"
  },
  {
    "city_code": "HDLY",
    "city_name": "HEDLEY",
    "icbc_city_code": "HDLY",
    "icbc_city_name": "HEDLEY",
    "icbc_city_name_legacy": "HEDLEY",
    "vips_city_name": "HEDLEY"
  },
  {
    "city_code": "HEFC",
    "city_name": "HEFFLEY CREEK",
    "icbc_city_code": "HEFC",
    "icbc_city_name": "HEFFLEY CREEK",
    "icbc_city_name_legacy": "HEFFLEY CREEK",
    "vips_city_name": "HEFFLEY CREEK"
  },
  {
    "city_code": "HFCK",
    "city_name": "HEFFLEY LAKE",
    "icbc_city_code": "HFCK",
    "icbc_city_name": "HEFFLEY CREEK",
    "icbc_city_name_legacy": "HEFFLEY CREEK",
    "vips_city_name": "HEFFLEY CREEK"
  },
  {
    "city_code": "HLBI",
    "city_name": "HELBY ISLAND",
    "icbc_city_code": "HLBI",
    "icbc_city_name": "HELBY ISLAND",
    "icbc_city_name_legacy": "UCLUELET",
    "vips_city_name": "HELBY ISLAND"
  },
  {
    "city_code": "HELM",
    "city_name": "HELMUT",
    "icbc_city_code": "HELM",
    "icbc_city_name": "HELMUT",
    "icbc_city_name_legacy": "FORT NELSON",
    "vips_city_name": "HELMUT"
  },
  {
    "city_code": "HMVL",
    "city_name": "HEMLOCK VALLEY",
    "icbc_city_code": "HMVL",
    "icbc_city_name": "HEMLOCK VALLEY",
    "icbc_city_name_legacy": "AGASSIZ",
    "vips_city_name": "HEMLOCK VALLEY"
  },
  {
    "city_code": "HXLK",
    "city_name": "HENDRIX LAKE",
    "icbc_city_code": "HXLK",
    "icbc_city_name": "HENDRIX LAKE",
    "icbc_city_name_legacy": "HENDRIX LAKE",
    "vips_city_name": "HENDRIX LAKE"
  },
  {
    "city_code": "HRYI",
    "city_name": "HENRY ISLAND",
    "icbc_city_code": "HRYI",
    "icbc_city_name": "HENRY ISLAND",
    "icbc_city_name_legacy": "KITKATLA",
    "vips_city_name": "HENRY ISLAND"
  },
  {
    "city_code": "HNDI",
    "city_name": "HERNANDO ISLAND",
    "icbc_city_code": "HNDI",
    "icbc_city_name": "HERNANDO ISLAND",
    "icbc_city_name_legacy": "QUADRA ISLAND",
    "vips_city_name": "HERNANDO ISLAND"
  },
  {
    "city_code": "HBBI",
    "city_name": "HIBBEN ISLAND",
    "icbc_city_code": "HBBI",
    "icbc_city_name": "HIBBEN ISLAND",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "HIBBEN ISLAND"
  },
  {
    "city_code": "HILD",
    "city_name": "HIGHLANDS",
    "icbc_city_code": "HILD",
    "icbc_city_name": "HIGHLANDS",
    "icbc_city_name_legacy": "COLWOOD",
    "vips_city_name": "HIGHLANDS"
  },
  {
    "city_code": "HILS",
    "city_name": "HILLS",
    "icbc_city_code": "HILS",
    "icbc_city_name": "HILLS",
    "icbc_city_name_legacy": "HILLS",
    "vips_city_name": "HILLS"
  },
  {
    "city_code": "HIXN",
    "city_name": "HIXON",
    "icbc_city_code": "HIXN",
    "icbc_city_name": "HIXON",
    "icbc_city_name_legacy": "HIXON",
    "vips_city_name": "HIXON"
  },
  {
    "city_code": "HXNS",
    "city_name": "HIXON SOUTH",
    "icbc_city_code": "HXNS",
    "icbc_city_name": "HIXON SOUTH",
    "icbc_city_name_legacy": "QUESNEL",
    "vips_city_name": "HIXON SOUTH"
  },
  {
    "city_code": "HOLB",
    "city_name": "HOLBERG",
    "icbc_city_code": "HOLB",
    "icbc_city_name": "HOLBERG",
    "icbc_city_name_legacy": "HOLBERG",
    "vips_city_name": "HOLBERG"
  },
  {
    "city_code": "HNYB",
    "city_name": "HONEYMOON BAY",
    "icbc_city_code": "HNYB",
    "icbc_city_name": "HONEYMOON BAY",
    "icbc_city_name_legacy": "HONEYMOON BAY",
    "vips_city_name": "HONEYMOON BAY"
  },
  {
    "city_code": "HOLK",
    "city_name": "HOODOO LAKE",
    "icbc_city_code": "HOLK",
    "icbc_city_name": "HOODOO LAKE",
    "icbc_city_name_legacy": "NEW AIYANSH",
    "vips_city_name": "HOODOO LAKE"
  },
  {
    "city_code": "HOPE",
    "city_name": "HOPE",
    "icbc_city_code": "HOPE",
    "icbc_city_name": "HOPE",
    "icbc_city_name_legacy": "HOPE",
    "vips_city_name": "HOPE"
  },
  {
    "city_code": "HOIS",
    "city_name": "HOPE ISLAND",
    "icbc_city_code": "HOIS",
    "icbc_city_name": "HOPE ISLAND",
    "icbc_city_name_legacy": "PORT HARDY",
    "vips_city_name": "HOPE ISLAND"
  },
  {
    "city_code": "HPKN",
    "city_name": "HOPKINS LANDING",
    "icbc_city_code": "HPKN",
    "icbc_city_name": "HOPKINS LANDING",
    "icbc_city_name_legacy": "HOPKINS LANDING",
    "vips_city_name": "HOPKINS LANDING"
  },
  {
    "city_code": "HPIS",
    "city_name": "HORNBY ISLAND",
    "icbc_city_code": "HPIS",
    "icbc_city_name": "HORNBY ISLAND",
    "icbc_city_name_legacy": "HORNBY ISLAND",
    "vips_city_name": "HORNBY ISLAND"
  },
  {
    "city_code": "HSFY",
    "city_name": "HORSEFLY",
    "icbc_city_code": "HSFY",
    "icbc_city_name": "HORSEFLY",
    "icbc_city_name_legacy": "HORSEFLY",
    "vips_city_name": "HORSEFLY"
  },
  {
    "city_code": "HSMR",
    "city_name": "HOSMER",
    "icbc_city_code": "HSMR",
    "icbc_city_name": "HOSMER",
    "icbc_city_name_legacy": "HOSMER",
    "vips_city_name": "HOSMER"
  },
  {
    "city_code": "HSCV",
    "city_name": "HOT SPRINGS COVE",
    "icbc_city_code": "HSCV",
    "icbc_city_name": "HOT SPRINGS COVE",
    "icbc_city_name_legacy": "HOT SPRINGS COV",
    "vips_city_name": "HOT SPRINGS COVE"
  },
  {
    "city_code": "HOUS",
    "city_name": "HOUSTON",
    "icbc_city_code": "HOUS",
    "icbc_city_name": "HOUSTON",
    "icbc_city_name_legacy": "HOUSTON",
    "vips_city_name": "HOUSTON"
  },
  {
    "city_code": "HWSR",
    "city_name": "HOWSER",
    "icbc_city_code": "HWSR",
    "icbc_city_name": "HOWSER",
    "icbc_city_name_legacy": "HOWSER",
    "vips_city_name": "HOWSER"
  },
  {
    "city_code": "HDHP",
    "city_name": "HUDSON'S HOPE",
    "icbc_city_code": "HDHP",
    "icbc_city_name": "HUDSON'S HOPE",
    "icbc_city_name_legacy": "HUDSON'S HOPE",
    "vips_city_name": "HUDSON'S HOPE"
  },
  {
    "city_code": "HLIS",
    "city_name": "HULL ISLAND",
    "icbc_city_code": "HLIS",
    "icbc_city_name": "HULL ISLAND",
    "icbc_city_name_legacy": "SAYWARD",
    "vips_city_name": "HULL ISLAND"
  },
  {
    "city_code": "HNTI",
    "city_name": "HUNTER ISLAND",
    "icbc_city_code": "HNTI",
    "icbc_city_name": "HUNTER ISLAND",
    "icbc_city_name_legacy": "BELLA BELLA",
    "vips_city_name": "HUNTER ISLAND"
  },
  {
    "city_code": "HUPE",
    "city_name": "HUPEL",
    "icbc_city_code": "HUPE",
    "icbc_city_name": "HUPEL",
    "icbc_city_name_legacy": "HUPEL",
    "vips_city_name": "HUPEL"
  },
  {
    "city_code": "HSIS",
    "city_name": "HURST ISLAND",
    "icbc_city_code": "HSIS",
    "icbc_city_name": "HURST ISLAND",
    "icbc_city_name_legacy": "PORT HARDY",
    "vips_city_name": "HURST ISLAND"
  },
  {
    "city_code": "HCHL",
    "city_name": "HUTCHISON LAKE",
    "icbc_city_code": "HCHL",
    "icbc_city_name": "HUTCHISON LAKE",
    "icbc_city_name_legacy": "70 MILE HOUSE",
    "vips_city_name": "HUTCHISON LAKE"
  },
  {
    "city_code": "HXIS",
    "city_name": "HUXLEY ISLAND",
    "icbc_city_code": "HXIS",
    "icbc_city_name": "HUXLEY ISLAND",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "HUXLEY ISLAND"
  },
  {
    "city_code": "HYSL",
    "city_name": "HYAS LAKE",
    "icbc_city_code": "HYSL",
    "icbc_city_name": "HYAS LAKE",
    "icbc_city_name_legacy": "PRITCHARD",
    "vips_city_name": "HYAS LAKE"
  },
  {
    "city_code": "IARM",
    "city_name": "INDIAN ARM",
    "icbc_city_code": "IARM",
    "icbc_city_name": "INDIAN ARM",
    "icbc_city_name_legacy": "INDIAN ARM",
    "vips_city_name": "INDIAN ARM"
  },
  {
    "city_code": "INIS",
    "city_name": "INSECT ISLAND",
    "icbc_city_code": "INIS",
    "icbc_city_name": "INSECT ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "INSECT ISLAND"
  },
  {
    "city_code": "IVMR",
    "city_name": "INVERMERE",
    "icbc_city_code": "IVMR",
    "icbc_city_name": "INVERMERE",
    "icbc_city_name_legacy": "INVERMERE",
    "vips_city_name": "INVERMERE"
  },
  {
    "city_code": "IRVN",
    "city_name": "IRVINES LANDING",
    "icbc_city_code": "IRVN",
    "icbc_city_name": "IRVINES LANDING",
    "icbc_city_name_legacy": "IRVINES LANDING",
    "vips_city_name": "IRVINES LANDING"
  },
  {
    "city_code": "ISKU",
    "city_name": "ISKUT",
    "icbc_city_code": "ISKU",
    "icbc_city_name": "ISKUT",
    "icbc_city_name_legacy": "ISKUT",
    "vips_city_name": "ISKUT"
  },
  {
    "city_code": "ISLP",
    "city_name": "ISLE PIERRE",
    "icbc_city_code": "ISLP",
    "icbc_city_name": "ISLE PIERRE",
    "icbc_city_name_legacy": "ISLE PIERRE",
    "vips_city_name": "ISLE PIERRE"
  },
  {
    "city_code": "JFLK",
    "city_name": "JACKFISH LAKE",
    "icbc_city_code": "JFLK",
    "icbc_city_name": "JACKFISH LAKE",
    "icbc_city_name_legacy": "CHETWYND",
    "vips_city_name": "JACKFISH LAKE"
  },
  {
    "city_code": "JACY",
    "city_name": "JADE CITY",
    "icbc_city_code": "JACY",
    "icbc_city_name": "JADE CITY",
    "icbc_city_name_legacy": "JADE CITY",
    "vips_city_name": "JADE CITY"
  },
  {
    "city_code": "JFRY",
    "city_name": "JAFFRAY",
    "icbc_city_code": "JFRY",
    "icbc_city_name": "JAFFRAY",
    "icbc_city_name_legacy": "JAFFRAY",
    "vips_city_name": "JAFFRAY"
  },
  {
    "city_code": "JMIS",
    "city_name": "JAMES ISLAND",
    "icbc_city_code": "JMIS",
    "icbc_city_name": "JAMES ISLAND",
    "icbc_city_name_legacy": "JAMES ISLAND",
    "vips_city_name": "JAMES ISLAND"
  },
  {
    "city_code": "JRVS",
    "city_name": "JERVIS INLET",
    "icbc_city_code": "JRVS",
    "icbc_city_name": "JERVIS INLET",
    "icbc_city_name_legacy": "POWELL RIVER",
    "vips_city_name": "JERVIS INLET"
  },
  {
    "city_code": "JESM",
    "city_name": "JESMOND",
    "icbc_city_code": "JESM",
    "icbc_city_name": "JESMOND",
    "icbc_city_name_legacy": "JESMOND",
    "vips_city_name": "JESMOND"
  },
  {
    "city_code": "JDRV",
    "city_name": "JORDAN RIVER",
    "icbc_city_code": "JDRV",
    "icbc_city_name": "JORDAN RIVER",
    "icbc_city_name_legacy": "JORDAN RIVER",
    "vips_city_name": "JORDAN RIVER"
  },
  {
    "city_code": "JUSK",
    "city_name": "JUSKATLA",
    "icbc_city_code": "JUSK",
    "icbc_city_name": "JUSKATLA",
    "icbc_city_name_legacy": "JUSKATLA",
    "vips_city_name": "JUSKATLA"
  },
  {
    "city_code": "KDIR",
    "city_name": "KADIS IR",
    "icbc_city_code": "KDIR",
    "icbc_city_name": "KADIS IR",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "KADIS IR"
  },
  {
    "city_code": "KLDN",
    "city_name": "KALEDEN",
    "icbc_city_code": "KLDN",
    "icbc_city_name": "KALEDEN",
    "icbc_city_name_legacy": "KALEDEN",
    "vips_city_name": "KALEDEN"
  },
  {
    "city_code": "KMLP",
    "city_name": "KAMLOOPS",
    "icbc_city_code": "KMLP",
    "icbc_city_name": "KAMLOOPS",
    "icbc_city_name_legacy": "KAMLOOPS",
    "vips_city_name": "KAMLOOPS"
  },
  {
    "city_code": "KNKB",
    "city_name": "KANAKA BAR",
    "icbc_city_code": "KNKB",
    "icbc_city_name": "KANAKA BAR",
    "icbc_city_name_legacy": "KANAKA BAR",
    "vips_city_name": "KANAKA BAR"
  },
  {
    "city_code": "KASL",
    "city_name": "KASLO",
    "icbc_city_code": "KASL",
    "icbc_city_name": "KASLO",
    "icbc_city_name_legacy": "KASLO",
    "vips_city_name": "KASLO"
  },
  {
    "city_code": "KTSI",
    "city_name": "KEATS ISLAND",
    "icbc_city_code": "KTSI",
    "icbc_city_name": "KEATS ISLAND",
    "icbc_city_name_legacy": "KEATS ISLAND",
    "vips_city_name": "KEATS ISLAND"
  },
  {
    "city_code": "KYLK",
    "city_name": "KELLY LAKE",
    "icbc_city_code": "KYLK",
    "icbc_city_name": "KELLY LAKE",
    "icbc_city_name_legacy": "KELLY LAKE",
    "vips_city_name": "KELLY LAKE"
  },
  {
    "city_code": "KLWN",
    "city_name": "KELOWNA",
    "icbc_city_code": "KLWN",
    "icbc_city_name": "KELOWNA",
    "icbc_city_name_legacy": "KELOWNA",
    "vips_city_name": "KELOWNA"
  },
  {
    "city_code": "KEMA",
    "city_name": "KEMANO",
    "icbc_city_code": "KEMA",
    "icbc_city_name": "KEMANO",
    "icbc_city_name_legacy": "KEMANO",
    "vips_city_name": "KEMANO"
  },
  {
    "city_code": "KYIS",
    "city_name": "KENNEDY ISLAND",
    "icbc_city_code": "KYIS",
    "icbc_city_name": "KENNEDY ISLAND",
    "icbc_city_name_legacy": "PRINCE RUPERT",
    "vips_city_name": "KENNEDY ISLAND"
  },
  {
    "city_code": "KDLK",
    "city_name": "KENNEDY LAKE",
    "icbc_city_code": "KDLK",
    "icbc_city_name": "KENNEDY LAKE",
    "icbc_city_name_legacy": "UCLUELET",
    "vips_city_name": "KENNEDY LAKE"
  },
  {
    "city_code": "KRMO",
    "city_name": "KEREMEOS",
    "icbc_city_code": "KRMO",
    "icbc_city_name": "KEREMEOS",
    "icbc_city_name_legacy": "KEREMEOS",
    "vips_city_name": "KEREMEOS"
  },
  {
    "city_code": "KRSY",
    "city_name": "KERSLEY",
    "icbc_city_code": "KRSY",
    "icbc_city_name": "KERSLEY",
    "icbc_city_name_legacy": "KERSLEY",
    "vips_city_name": "KERSLEY"
  },
  {
    "city_code": "KILD",
    "city_name": "KILDONAN",
    "icbc_city_code": "KILD",
    "icbc_city_name": "KILDONAN",
    "icbc_city_name_legacy": "KILDONAN",
    "vips_city_name": "KILDONAN"
  },
  {
    "city_code": "KNKN",
    "city_name": "KILKERRAN",
    "icbc_city_code": "KNKN",
    "icbc_city_name": "KILKERRAN",
    "icbc_city_name_legacy": "KILKERRAN",
    "vips_city_name": "KILKERRAN"
  },
  {
    "city_code": "KBLY",
    "city_name": "KIMBERLEY",
    "icbc_city_code": "KBLY",
    "icbc_city_name": "KIMBERLEY",
    "icbc_city_name_legacy": "KIMBERLEY",
    "vips_city_name": "KIMBERLEY"
  },
  {
    "city_code": "KINA",
    "city_name": "KINASKAN",
    "icbc_city_code": "KINA",
    "icbc_city_name": "KINASKAN",
    "icbc_city_name_legacy": "TELEGRAPH CREEK",
    "vips_city_name": "KINASKAN"
  },
  {
    "city_code": "KGIT",
    "city_name": "KINGCOME INLET",
    "icbc_city_code": "KGIT",
    "icbc_city_name": "KINGCOME INLET",
    "icbc_city_name_legacy": "KINGCOME INLET",
    "vips_city_name": "KINGCOME INLET"
  },
  {
    "city_code": "KGGT",
    "city_name": "KINGSGATE",
    "icbc_city_code": "KGGT",
    "icbc_city_name": "KINGSGATE",
    "icbc_city_name_legacy": "KINGSGATE",
    "vips_city_name": "KINGSGATE"
  },
  {
    "city_code": "KNGV",
    "city_name": "KINGSVALE",
    "icbc_city_code": "KNGV",
    "icbc_city_name": "KINGSVALE",
    "icbc_city_name_legacy": "MERRITT",
    "vips_city_name": "KINGSVALE"
  },
  {
    "city_code": "KISP",
    "city_name": "KISPIOX",
    "icbc_city_code": "KISP",
    "icbc_city_name": "KISPIOX",
    "icbc_city_name_legacy": "KISPIOX",
    "vips_city_name": "KISPIOX"
  },
  {
    "city_code": "KSPV",
    "city_name": "KISPIOX VALLEY",
    "icbc_city_code": "KSPV",
    "icbc_city_name": "KISPIOX VALLEY",
    "icbc_city_name_legacy": "NEW HAZELTON",
    "vips_city_name": "KISPIOX VALLEY"
  },
  {
    "city_code": "KITV",
    "city_name": "KITAMAAT VILLAGE",
    "icbc_city_code": "KITV",
    "icbc_city_name": "KITAMAAT VILLAGE",
    "icbc_city_name_legacy": "KITAMAAT VILLAG",
    "vips_city_name": "KITAMAAT VILLAGE"
  },
  {
    "city_code": "KTNR",
    "city_name": "KITCHENER",
    "icbc_city_code": "KTNR",
    "icbc_city_name": "KITCHENER",
    "icbc_city_name_legacy": "KITCHENER",
    "vips_city_name": "KITCHENER"
  },
  {
    "city_code": "KITI",
    "city_name": "KITIMAT",
    "icbc_city_code": "KITI",
    "icbc_city_name": "KITIMAT",
    "icbc_city_name_legacy": "KITIMAT",
    "vips_city_name": "KITIMAT"
  },
  {
    "city_code": "KITK",
    "city_name": "KITKATLA",
    "icbc_city_code": "KITK",
    "icbc_city_name": "KITKATLA",
    "icbc_city_name_legacy": "KITKATLA",
    "vips_city_name": "KITKATLA"
  },
  {
    "city_code": "KITS",
    "city_name": "KITSAULT",
    "icbc_city_code": "KITS",
    "icbc_city_name": "KITSAULT",
    "icbc_city_name_legacy": "KITSAULT",
    "vips_city_name": "KITSAULT"
  },
  {
    "city_code": "KITM",
    "city_name": "KITSUMKALUM",
    "icbc_city_code": "KITM",
    "icbc_city_name": "KTSUMKAYLUM IR",
    "icbc_city_name_legacy": "TERRACE",
    "vips_city_name": "KTSUMKAYLUM IR"
  },
  {
    "city_code": "KITW",
    "city_name": "KITWANGA",
    "icbc_city_code": "KITW",
    "icbc_city_name": "KITWANGA",
    "icbc_city_name_legacy": "KITWANGA",
    "vips_city_name": "KITWANGA"
  },
  {
    "city_code": "KLKL",
    "city_name": "KLEENA KLEENE",
    "icbc_city_code": "KLKL",
    "icbc_city_name": "KLEENA KLEENE",
    "icbc_city_name_legacy": "KLEENA KLEENE",
    "vips_city_name": "KLEENA KLEENE"
  },
  {
    "city_code": "KLEM",
    "city_name": "KLEMTU",
    "icbc_city_code": "KLEM",
    "icbc_city_name": "KLEMTU",
    "icbc_city_name_legacy": "KLEMTU",
    "vips_city_name": "KLEMTU"
  },
  {
    "city_code": "KGIN",
    "city_name": "KNIGHT INLET",
    "icbc_city_code": "KGIN",
    "icbc_city_name": "KNIGHT INLET",
    "icbc_city_name_legacy": "KNIGHT INLET",
    "vips_city_name": "KNIGHT INLET"
  },
  {
    "city_code": "KNUF",
    "city_name": "KNUTSFORD",
    "icbc_city_code": "KNUF",
    "icbc_city_name": "KNUTSFORD",
    "icbc_city_name_legacy": "KNUTSFORD",
    "vips_city_name": "KNUTSFORD"
  },
  {
    "city_code": "KOKS",
    "city_name": "KOKSILAH",
    "icbc_city_code": "KOKS",
    "icbc_city_name": "KOKSILAH",
    "icbc_city_name_legacy": "KOKSILAH",
    "vips_city_name": "KOKSILAH"
  },
  {
    "city_code": "KYBY",
    "city_name": "KOOTENAY BAY",
    "icbc_city_code": "KYBY",
    "icbc_city_name": "KOOTENAY BAY",
    "icbc_city_name_legacy": "KOOTENAY BAY",
    "vips_city_name": "KOOTENAY BAY"
  },
  {
    "city_code": "KTPK",
    "city_name": "KOOTENAY PARK",
    "icbc_city_code": "KTPK",
    "icbc_city_name": "KOOTENAY PARK",
    "icbc_city_name_legacy": "INVERMERE",
    "vips_city_name": "KOOTENAY PARK"
  },
  {
    "city_code": "KTPS",
    "city_name": "KOOTENAY PASS",
    "icbc_city_code": "KTPS",
    "icbc_city_name": "KOOTENAY PASS",
    "icbc_city_name_legacy": "SALMO",
    "vips_city_name": "KOOTENAY PASS"
  },
  {
    "city_code": "KCLK",
    "city_name": "KOTCHO LAKE",
    "icbc_city_code": "KCLK",
    "icbc_city_name": "KOTCHO LAKE",
    "icbc_city_name_legacy": "FORT NELSON",
    "vips_city_name": "KOTCHO LAKE"
  },
  {
    "city_code": "KRTV",
    "city_name": "KRESTOVA",
    "icbc_city_code": "KRTV",
    "icbc_city_name": "KRESTOVA",
    "icbc_city_name_legacy": "KRESTOVA",
    "vips_city_name": "KRESTOVA"
  },
  {
    "city_code": "KLDI",
    "city_name": "KSUI LA DAS IR",
    "icbc_city_code": "KLDI",
    "icbc_city_name": "KSUI LA DAS IR",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "KSUI LA DAS IR"
  },
  {
    "city_code": "KULI",
    "city_name": "KULDEKDUMA IR",
    "icbc_city_code": "KULI",
    "icbc_city_name": "KULDEKDUMA IR",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "KULDEKDUMA IR"
  },
  {
    "city_code": "KULD",
    "city_name": "KULDO",
    "icbc_city_code": "KULD",
    "icbc_city_name": "KULDO",
    "icbc_city_name_legacy": "NEW HAZELTON",
    "vips_city_name": "KULDO"
  },
  {
    "city_code": "KUIS",
    "city_name": "KUNGA ISLAND",
    "icbc_city_code": "KUIS",
    "icbc_city_name": "KUNGA ISLAND",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "KUNGA ISLAND"
  },
  {
    "city_code": "KHIS",
    "city_name": "KUNGHIT ISLAND",
    "icbc_city_code": "KHIS",
    "icbc_city_name": "KUNGHIT ISLAND",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "KUNGHIT ISLAND"
  },
  {
    "city_code": "KYLI",
    "city_name": "KYE YAA LA IR",
    "icbc_city_code": "KYLI",
    "icbc_city_name": "KYE YAA LA IR",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "KYE YAA LA IR"
  },
  {
    "city_code": "KYUQ",
    "city_name": "KYUQUOT",
    "icbc_city_code": "KYUQ",
    "icbc_city_name": "KYUQUOT",
    "icbc_city_name_legacy": "KYUQUOT",
    "vips_city_name": "KYUQUOT"
  },
  {
    "city_code": "LADB",
    "city_name": "LAC DU BOIS",
    "icbc_city_code": "LADB",
    "icbc_city_name": "LAC DU BOIS",
    "icbc_city_name_legacy": "KAMLOOPS",
    "vips_city_name": "LAC DU BOIS"
  },
  {
    "city_code": "LLHC",
    "city_name": "LAC LA HACHE",
    "icbc_city_code": "LLHC",
    "icbc_city_name": "LAC LA HACHE",
    "icbc_city_name_legacy": "LAC LA HACHE",
    "vips_city_name": "LAC LA HACHE"
  },
  {
    "city_code": "LLJN",
    "city_name": "LAC LE JEUNE",
    "icbc_city_code": "LLJN",
    "icbc_city_name": "LAC LE JEUNE",
    "icbc_city_name_legacy": "LAC LE JEUNE",
    "vips_city_name": "LAC LE JEUNE"
  },
  {
    "city_code": "LDYS",
    "city_name": "LADYSMITH",
    "icbc_city_code": "LDYS",
    "icbc_city_name": "LADYSMITH",
    "icbc_city_name_legacy": "LADYSMITH",
    "vips_city_name": "LADYSMITH"
  },
  {
    "city_code": "LDLW",
    "city_name": "LAIDLAW",
    "icbc_city_code": "LDLW",
    "icbc_city_name": "LAIDLAW",
    "icbc_city_name_legacy": "LAIDLAW",
    "vips_city_name": "LAIDLAW"
  },
  {
    "city_code": "LKCY",
    "city_name": "LAKE COUNTRY",
    "icbc_city_code": "LKCY",
    "icbc_city_name": "LAKE COUNTRY",
    "icbc_city_name_legacy": "LAKE COUNTRY",
    "vips_city_name": "LAKE COUNTRY"
  },
  {
    "city_code": "LCWC",
    "city_name": "LAKE COWICHAN",
    "icbc_city_code": "LCWC",
    "icbc_city_name": "LAKE COWICHAN",
    "icbc_city_name_legacy": "LAKE COWICHAN",
    "vips_city_name": "LAKE COWICHAN"
  },
  {
    "city_code": "LKER",
    "city_name": "LAKE ERROCK",
    "icbc_city_code": "LKER",
    "icbc_city_name": "LAKE ERROCK",
    "icbc_city_name_legacy": "LAKE ERROCK",
    "vips_city_name": "LAKE ERROCK"
  },
  {
    "city_code": "LKLK",
    "city_name": "LAKELSE LAKE",
    "icbc_city_code": "LKLK",
    "icbc_city_name": "LAKELSE LAKE",
    "icbc_city_name_legacy": "TERRACE",
    "vips_city_name": "LAKELSE LAKE"
  },
  {
    "city_code": "LGIS",
    "city_name": "LANGARA ISLAND",
    "icbc_city_code": "LGIS",
    "icbc_city_name": "LANGARA ISLAND",
    "icbc_city_name_legacy": "MASSETT",
    "vips_city_name": "LANGARA ISLAND"
  },
  {
    "city_code": "LNGD",
    "city_name": "LANGDALE",
    "icbc_city_code": "LNGD",
    "icbc_city_name": "LANGDALE",
    "icbc_city_name_legacy": "LANGDALE",
    "vips_city_name": "LANGDALE"
  },
  {
    "city_code": "LGFD",
    "city_name": "LANGFORD",
    "icbc_city_code": "LGFD",
    "icbc_city_name": "LANGFORD",
    "icbc_city_name_legacy": "LANGFORD",
    "vips_city_name": "LANGFORD"
  },
  {
    "city_code": "LANG",
    "city_name": "LANGLEY",
    "icbc_city_code": "LANG",
    "icbc_city_name": "LANGLEY",
    "icbc_city_name_legacy": "LANGLEY",
    "vips_city_name": "LANGLEY"
  },
  {
    "city_code": "LNVL",
    "city_name": "LANTZVILLE",
    "icbc_city_code": "LNVL",
    "icbc_city_name": "LANTZVILLE",
    "icbc_city_name_legacy": "LANTZVILLE",
    "vips_city_name": "LANTZVILLE"
  },
  {
    "city_code": "LZIS",
    "city_name": "LANZ ISLAND",
    "icbc_city_code": "LZIS",
    "icbc_city_name": "LANZ ISLAND",
    "icbc_city_name_legacy": "PORT HARDY",
    "vips_city_name": "LANZ ISLAND"
  },
  {
    "city_code": "LARD",
    "city_name": "LARDEAU",
    "icbc_city_code": "LARD",
    "icbc_city_name": "LARDEAU",
    "icbc_city_name_legacy": "LARDEAU",
    "vips_city_name": "LARDEAU"
  },
  {
    "city_code": "LQIS",
    "city_name": "LASQUETI ISLAND",
    "icbc_city_code": "LQIS",
    "icbc_city_name": "LASQUETI ISLAND",
    "icbc_city_name_legacy": "LASQUETI ISLAND",
    "vips_city_name": "LASQUETI ISLAND"
  },
  {
    "city_code": "LAVI",
    "city_name": "LAVINGTON",
    "icbc_city_code": "LAVI",
    "icbc_city_name": "LAVINGTON",
    "icbc_city_name_legacy": "LAVINGTON",
    "vips_city_name": "LAVINGTON"
  },
  {
    "city_code": "LXKW",
    "city_name": "LAX KW' ALAAMS",
    "icbc_city_code": "LXKW",
    "icbc_city_name": "LAX KW' ALAAMS",
    "icbc_city_name_legacy": "LAX KW'ALAAMS",
    "vips_city_name": "LAX KW' ALAAMS"
  },
  {
    "city_code": "LAXA",
    "city_name": "LAXGALTS AP",
    "icbc_city_code": "LAXA",
    "icbc_city_name": "LAXGALTS AP",
    "icbc_city_name_legacy": "KINCOLITH",
    "vips_city_name": "LAXGALTS AP"
  },
  {
    "city_code": "LNCL",
    "city_name": "LEANCHOIL",
    "icbc_city_code": "LNCL",
    "icbc_city_name": "LEANCHOIL",
    "icbc_city_name_legacy": "LEANCHOIL",
    "vips_city_name": "LEANCHOIL"
  },
  {
    "city_code": "LECK",
    "city_name": "LEE CREEK",
    "icbc_city_code": "LECK",
    "icbc_city_name": "LEE CREEK",
    "icbc_city_name_legacy": "LEE CREEK",
    "vips_city_name": "LEE CREEK"
  },
  {
    "city_code": "LWIS",
    "city_name": "LEWIS ISLAND",
    "icbc_city_code": "LWIS",
    "icbc_city_name": "LEWIS ISLAND",
    "icbc_city_name_legacy": "KITKATLA",
    "vips_city_name": "LEWIS ISLAND"
  },
  {
    "city_code": "LDRV",
    "city_name": "LIARD RIVER",
    "icbc_city_code": "LDRV",
    "icbc_city_name": "LIARD RIVER",
    "icbc_city_name_legacy": "FORT NELSON",
    "vips_city_name": "LIARD RIVER"
  },
  {
    "city_code": "LKLY",
    "city_name": "LIKELY",
    "icbc_city_code": "LKLY",
    "icbc_city_name": "LIKELY",
    "icbc_city_name_legacy": "LIKELY",
    "vips_city_name": "LIKELY"
  },
  {
    "city_code": "LILL",
    "city_name": "LILLOOET",
    "icbc_city_code": "LILL",
    "icbc_city_name": "LILLOOET",
    "icbc_city_name_legacy": "LILLOOET",
    "vips_city_name": "LILLOOET"
  },
  {
    "city_code": "LILR",
    "city_name": "LILLOOET RURAL",
    "icbc_city_code": "LILR",
    "icbc_city_name": "LILLOOET RURAL",
    "icbc_city_name_legacy": "LILLOOET",
    "vips_city_name": "LILLOOET RURAL"
  },
  {
    "city_code": "LYLK",
    "city_name": "LILY LAKE",
    "icbc_city_code": "LYLK",
    "icbc_city_name": "LILY LAKE",
    "icbc_city_name_legacy": "FRASER LAKE",
    "vips_city_name": "LILY LAKE"
  },
  {
    "city_code": "LNBH",
    "city_name": "LINDELL BEACH",
    "icbc_city_code": "LNBH",
    "icbc_city_name": "LINDELL BEACH",
    "icbc_city_name_legacy": "LINDELL BEACH",
    "vips_city_name": "LINDELL BEACH"
  },
  {
    "city_code": "LBAY",
    "city_name": "LIONS BAY",
    "icbc_city_code": "LBAY",
    "icbc_city_name": "LIONS BAY",
    "icbc_city_name_legacy": "LIONS BAY",
    "vips_city_name": "LIONS BAY"
  },
  {
    "city_code": "LSTR",
    "city_name": "LISTER",
    "icbc_city_code": "LSTR",
    "icbc_city_name": "LISTER",
    "icbc_city_name_legacy": "LISTER",
    "vips_city_name": "LISTER"
  },
  {
    "city_code": "LTFT",
    "city_name": "LITTLE FORT",
    "icbc_city_code": "LTFT",
    "icbc_city_name": "LITTLE FORT",
    "icbc_city_name_legacy": "LITTLE FORT",
    "vips_city_name": "LITTLE FORT"
  },
  {
    "city_code": "LDGP",
    "city_name": "LODGEPOLE",
    "icbc_city_code": "LDGP",
    "icbc_city_name": "LODGEPOLE",
    "icbc_city_name_legacy": "LOGAN LAKE",
    "vips_city_name": "LODGEPOLE"
  },
  {
    "city_code": "LGLK",
    "city_name": "LOGAN LAKE",
    "icbc_city_code": "LGLK",
    "icbc_city_name": "LOGAN LAKE",
    "icbc_city_name_legacy": "LOGAN LAKE",
    "vips_city_name": "LOGAN LAKE"
  },
  {
    "city_code": "LNBT",
    "city_name": "LONE BUTTE",
    "icbc_city_code": "LNBT",
    "icbc_city_name": "LONE BUTTE",
    "icbc_city_name_legacy": "LONE BUTTE",
    "vips_city_name": "LONE BUTTE"
  },
  {
    "city_code": "LNPR",
    "city_name": "LONE PRAIRIE",
    "icbc_city_code": "LNPR",
    "icbc_city_name": "LONE PRAIRIE",
    "icbc_city_name_legacy": "CHETWYND",
    "vips_city_name": "LONE PRAIRIE"
  },
  {
    "city_code": "LGBH",
    "city_name": "LONG BEACH",
    "icbc_city_code": "LGBH",
    "icbc_city_name": "LONG BEACH",
    "icbc_city_name_legacy": "LONG BEACH",
    "vips_city_name": "LONG BEACH"
  },
  {
    "city_code": "LGWT",
    "city_name": "LONGWORTH",
    "icbc_city_code": "LGWT",
    "icbc_city_name": "LONGWORTH",
    "icbc_city_name_legacy": "LONGWORTH",
    "vips_city_name": "LONGWORTH"
  },
  {
    "city_code": "LNLK",
    "city_name": "LOON LAKE",
    "icbc_city_code": "LNLK",
    "icbc_city_name": "LOON LAKE",
    "icbc_city_name_legacy": "CLINTON",
    "vips_city_name": "LOON LAKE"
  },
  {
    "city_code": "LTIS",
    "city_name": "LORETTA ISLAND",
    "icbc_city_code": "LTIS",
    "icbc_city_name": "LORETTA ISLAND",
    "icbc_city_name_legacy": "HARTLEY BAY",
    "vips_city_name": "LORETTA ISLAND"
  },
  {
    "city_code": "LSCK",
    "city_name": "LOUIS CREEK",
    "icbc_city_code": "LSCK",
    "icbc_city_name": "LOUIS CREEK",
    "icbc_city_name_legacy": "LOUIS CREEK",
    "vips_city_name": "LOUIS CREEK"
  },
  {
    "city_code": "LNIC",
    "city_name": "LOWER NICOLA",
    "icbc_city_code": "LNIC",
    "icbc_city_name": "LOWER NICOLA",
    "icbc_city_name_legacy": "CANFORD",
    "vips_city_name": "LOWER NICOLA"
  },
  {
    "city_code": "LWPT",
    "city_name": "LOWER POST",
    "icbc_city_code": "LWPT",
    "icbc_city_name": "LOWER POST",
    "icbc_city_name_legacy": "LOWER POST",
    "vips_city_name": "LOWER POST"
  },
  {
    "city_code": "LMBY",
    "city_name": "LUMBY",
    "icbc_city_code": "LMBY",
    "icbc_city_name": "LUMBY",
    "icbc_city_name_legacy": "LUMBY",
    "vips_city_name": "LUMBY"
  },
  {
    "city_code": "LUND",
    "city_name": "LUND",
    "icbc_city_code": "LUND",
    "icbc_city_name": "LUND",
    "icbc_city_name_legacy": "LUND",
    "vips_city_name": "LUND"
  },
  {
    "city_code": "LYIS",
    "city_name": "LYELL ISLAND",
    "icbc_city_code": "LYIS",
    "icbc_city_name": "LYELL ISLAND",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "LYELL ISLAND"
  },
  {
    "city_code": "LYTN",
    "city_name": "LYTTON",
    "icbc_city_code": "LYTN",
    "icbc_city_name": "LYTTON",
    "icbc_city_name_legacy": "LYTTON",
    "vips_city_name": "LYTTON"
  },
  {
    "city_code": "LYTR",
    "city_name": "LYTTON RURAL",
    "icbc_city_code": "LYTR",
    "icbc_city_name": "LYTTON RURAL",
    "icbc_city_name_legacy": "LYTTON",
    "vips_city_name": "LYTTON RURAL"
  },
  {
    "city_code": "MCKN",
    "city_name": "MACKENZIE",
    "icbc_city_code": "MCKN",
    "icbc_city_name": "MACKENZIE",
    "icbc_city_name_legacy": "MACKENZIE",
    "vips_city_name": "MACKENZIE"
  },
  {
    "city_code": "MZRU",
    "city_name": "MACKENZIE RURAL",
    "icbc_city_code": "MZRU",
    "icbc_city_name": "MACKENZIE RURAL",
    "icbc_city_name_legacy": "MACKENZIE",
    "vips_city_name": "MACKENZIE RURAL"
  },
  {
    "city_code": "MDPK",
    "city_name": "MADEIRA PARK",
    "icbc_city_code": "MDPK",
    "icbc_city_name": "MADEIRA PARK",
    "icbc_city_name_legacy": "MADEIRA PARK",
    "vips_city_name": "MADEIRA PARK"
  },
  {
    "city_code": "MGBY",
    "city_name": "MAGNA BAY",
    "icbc_city_code": "MGBY",
    "icbc_city_name": "MAGNA BAY",
    "icbc_city_name_legacy": "MAGNA BAY",
    "vips_city_name": "MAGNA BAY"
  },
  {
    "city_code": "MHRV",
    "city_name": "MAHATTA RIVER",
    "icbc_city_code": "MHRV",
    "icbc_city_name": "MAHATTA RIVER",
    "icbc_city_name_legacy": "MAHATTA RIVER",
    "vips_city_name": "MAHATTA RIVER"
  },
  {
    "city_code": "MDFL",
    "city_name": "MAHOOD FALLS",
    "icbc_city_code": "MDFL",
    "icbc_city_name": "MAHOOD FALLS",
    "icbc_city_name_legacy": "MAHOOD FALLS",
    "vips_city_name": "MAHOOD FALLS"
  },
  {
    "city_code": "MDCK",
    "city_name": "MAIDEN CREEK",
    "icbc_city_code": "MDCK",
    "icbc_city_name": "MAIDEN CREEK",
    "icbc_city_name_legacy": "ASHCROFT",
    "vips_city_name": "MAIDEN CREEK"
  },
  {
    "city_code": "MTIS",
    "city_name": "MAITLAND ISLAND",
    "icbc_city_code": "MTIS",
    "icbc_city_name": "MAITLAND ISLAND",
    "icbc_city_name_legacy": "HARTLEY BAY",
    "vips_city_name": "MAITLAND ISLAND"
  },
  {
    "city_code": "MLHT",
    "city_name": "MALAHAT",
    "icbc_city_code": "MLHT",
    "icbc_city_name": "MALAHAT",
    "icbc_city_name_legacy": "MALAHAT",
    "vips_city_name": "MALAHAT"
  },
  {
    "city_code": "MAKW",
    "city_name": "MALAKWA",
    "icbc_city_code": "MAKW",
    "icbc_city_name": "MALAKWA",
    "icbc_city_name_legacy": "MALAKWA",
    "vips_city_name": "MALAKWA"
  },
  {
    "city_code": "MMLK",
    "city_name": "MAMIT LAKE",
    "icbc_city_code": "MMLK",
    "icbc_city_name": "MAMIT LAKE",
    "icbc_city_name_legacy": "MAMIT LAKE",
    "vips_city_name": "MAMIT LAKE"
  },
  {
    "city_code": "MNPK",
    "city_name": "MANNING PARK",
    "icbc_city_code": "MNPK",
    "icbc_city_name": "MANNING PARK",
    "icbc_city_name_legacy": "MANNING PARK",
    "vips_city_name": "MANNING PARK"
  },
  {
    "city_code": "MNCK",
    "city_name": "MANSON CREEK",
    "icbc_city_code": "MNCK",
    "icbc_city_name": "MANSON CREEK",
    "icbc_city_name_legacy": "MANSON CREEK",
    "vips_city_name": "MANSON CREEK"
  },
  {
    "city_code": "MSLD",
    "city_name": "MANSONS LANDING",
    "icbc_city_code": "MSLD",
    "icbc_city_name": "MANSONS LANDING",
    "icbc_city_name_legacy": "MANSONS LANDING",
    "vips_city_name": "MANSONS LANDING"
  },
  {
    "city_code": "MRDG",
    "city_name": "MAPLE RIDGE",
    "icbc_city_code": "MRDG",
    "icbc_city_name": "MAPLE RIDGE",
    "icbc_city_name_legacy": "MAPLE RIDGE",
    "vips_city_name": "MAPLE RIDGE"
  },
  {
    "city_code": "MARA",
    "city_name": "MARA",
    "icbc_city_code": "MARA",
    "icbc_city_name": "MARA",
    "icbc_city_name_legacy": "MARA",
    "vips_city_name": "MARA"
  },
  {
    "city_code": "MRCN",
    "city_name": "MARBLE CANYON",
    "icbc_city_code": "MRCN",
    "icbc_city_name": "MARBLE CANYON",
    "icbc_city_name_legacy": "LILLOOET",
    "vips_city_name": "MARBLE CANYON"
  },
  {
    "city_code": "MARG",
    "city_name": "MARGUERITE",
    "icbc_city_code": "MARG",
    "icbc_city_name": "MARGUERITE",
    "icbc_city_name_legacy": "MARGUERITE",
    "vips_city_name": "MARGUERITE"
  },
  {
    "city_code": "MAIS",
    "city_name": "MARINA ISLAND",
    "icbc_city_code": "MAIS",
    "icbc_city_name": "MARINA ISLAND",
    "icbc_city_name_legacy": "QUADRA ISLAND",
    "vips_city_name": "MARINA ISLAND"
  },
  {
    "city_code": "MRIS",
    "city_name": "MARS ISLAND",
    "icbc_city_code": "MRIS",
    "icbc_city_name": "MARS ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "MARS ISLAND"
  },
  {
    "city_code": "MASS",
    "city_name": "MASSET",
    "icbc_city_code": "MASS",
    "icbc_city_name": "MASSET",
    "icbc_city_name_legacy": "MASSET",
    "vips_city_name": "MASSET"
  },
  {
    "city_code": "MDIS",
    "city_name": "MAUD ISLAND",
    "icbc_city_code": "MDIS",
    "icbc_city_name": "MAUD ISLAND",
    "icbc_city_name_legacy": "PARKSVILLE",
    "vips_city_name": "MAUD ISLAND"
  },
  {
    "city_code": "MEIS",
    "city_name": "MAUDE ISLAND",
    "icbc_city_code": "MEIS",
    "icbc_city_name": "MAUDE ISLAND",
    "icbc_city_name_legacy": "NANOOSE BAY",
    "vips_city_name": "MAUDE ISLAND"
  },
  {
    "city_code": "MLIS",
    "city_name": "MAURELLE ISLAND",
    "icbc_city_code": "MLIS",
    "icbc_city_name": "MAURELLE ISLAND",
    "icbc_city_name_legacy": "MAURELLE ISLAND",
    "vips_city_name": "MAURELLE ISLAND"
  },
  {
    "city_code": "MXMH",
    "city_name": "MAXHAMISH",
    "icbc_city_code": "MXMH",
    "icbc_city_name": "MAXHAMISH",
    "icbc_city_name_legacy": "FORT NELSON",
    "vips_city_name": "MAXHAMISH"
  },
  {
    "city_code": "MYIS",
    "city_name": "MAYNE ISLAND",
    "icbc_city_code": "MYIS",
    "icbc_city_name": "MAYNE ISLAND",
    "icbc_city_name_legacy": "MAYNE ISLAND",
    "vips_city_name": "MAYNE ISLAND"
  },
  {
    "city_code": "MYOK",
    "city_name": "MAYOOK",
    "icbc_city_code": "MYOK",
    "icbc_city_name": "MAYOOK",
    "icbc_city_name_legacy": "CRANBROOK",
    "vips_city_name": "MAYOOK"
  },
  {
    "city_code": "MBRD",
    "city_name": "MCBRIDE",
    "icbc_city_code": "MBRD",
    "icbc_city_name": "MCBRIDE",
    "icbc_city_name_legacy": "MCBRIDE",
    "vips_city_name": "MCBRIDE"
  },
  {
    "city_code": "MBRU",
    "city_name": "MCBRIDE RURAL",
    "icbc_city_code": "MBRU",
    "icbc_city_name": "MCBRIDE RURAL",
    "icbc_city_name_legacy": "MCBRIDE",
    "vips_city_name": "MCBRIDE RURAL"
  },
  {
    "city_code": "MCIS",
    "city_name": "MCCAULEY ISLAND",
    "icbc_city_code": "MCIS",
    "icbc_city_name": "MCCAULEY ISLAND",
    "icbc_city_name_legacy": "KITKATLA",
    "vips_city_name": "MCCAULEY ISLAND"
  },
  {
    "city_code": "MCGL",
    "city_name": "MCGILLIVRAY LAKE",
    "icbc_city_code": "MCGL",
    "icbc_city_name": "MCGILLIVRAY LAKE",
    "icbc_city_name_legacy": "HEFFLEY CREEK",
    "vips_city_name": "MCGILLIVRAY LAKE"
  },
  {
    "city_code": "MCGR",
    "city_name": "MCGREGOR",
    "icbc_city_code": "MCGR",
    "icbc_city_name": "MCGREGOR",
    "icbc_city_name_legacy": "MCGREGOR",
    "vips_city_name": "MCGREGOR"
  },
  {
    "city_code": "MCKY",
    "city_name": "MCKAY ISLAND",
    "icbc_city_code": "MCKY",
    "icbc_city_name": "MCKAY ISLAND",
    "icbc_city_name_legacy": "AHOUSAT",
    "vips_city_name": "MCKAY ISLAND"
  },
  {
    "city_code": "MLLK",
    "city_name": "MCLEESE LAKE",
    "icbc_city_code": "MLLK",
    "icbc_city_name": "MCLEESE LAKE",
    "icbc_city_name_legacy": "MCLEESE LAKE",
    "vips_city_name": "MCLEESE LAKE"
  },
  {
    "city_code": "MLDL",
    "city_name": "MCLEOD LAKE",
    "icbc_city_code": "MLDL",
    "icbc_city_name": "MCLEOD LAKE",
    "icbc_city_name_legacy": "MCLEOD LAKE",
    "vips_city_name": "MCLEOD LAKE"
  },
  {
    "city_code": "MDLK",
    "city_name": "MCLEOD LAKE RESERVE",
    "icbc_city_code": "MDLK",
    "icbc_city_name": "MCLEOD LAKE RESERVE",
    "icbc_city_name_legacy": "TSAY KEH DENE",
    "vips_city_name": "MCLEOD LAKE RESERVE"
  },
  {
    "city_code": "MCLR",
    "city_name": "MCLURE",
    "icbc_city_code": "MCLR",
    "icbc_city_name": "MCLURE",
    "icbc_city_name_legacy": "MCLURE",
    "vips_city_name": "MCLURE"
  },
  {
    "city_code": "MWCK",
    "city_name": "MEADOW CREEK",
    "icbc_city_code": "MWCK",
    "icbc_city_name": "MEADOW CREEK",
    "icbc_city_name_legacy": "MEADOW CREEK",
    "vips_city_name": "MEADOW CREEK"
  },
  {
    "city_code": "MDWL",
    "city_name": "MEADOW LAKE",
    "icbc_city_code": "MDWL",
    "icbc_city_name": "MEADOW LAKE",
    "icbc_city_name_legacy": "LITTLE FORT",
    "vips_city_name": "MEADOW LAKE"
  },
  {
    "city_code": "MSIS",
    "city_name": "MEARES ISLAND",
    "icbc_city_code": "MSIS",
    "icbc_city_name": "MEARES ISLAND",
    "icbc_city_name_legacy": "TOFINO",
    "vips_city_name": "MEARES ISLAND"
  },
  {
    "city_code": "MGLK",
    "city_name": "MEGIN LAKE",
    "icbc_city_code": "MGLK",
    "icbc_city_name": "MEGIN LAKE",
    "icbc_city_name_legacy": "AHOUSAT",
    "vips_city_name": "MEGIN LAKE"
  },
  {
    "city_code": "MVIS",
    "city_name": "MELVILLE ISLAND",
    "icbc_city_code": "MVIS",
    "icbc_city_name": "MELVILLE ISLAND",
    "icbc_city_name_legacy": "PRINE RUPERT",
    "vips_city_name": "MELVILLE ISLAND"
  },
  {
    "city_code": "MRTT",
    "city_name": "MERRITT",
    "icbc_city_code": "MRTT",
    "icbc_city_name": "MERRITT",
    "icbc_city_name_legacy": "MERRITT",
    "vips_city_name": "MERRITT"
  },
  {
    "city_code": "MELV",
    "city_name": "MERVILLE",
    "icbc_city_code": "MELV",
    "icbc_city_name": "MERVILLE",
    "icbc_city_name_legacy": "MERVILLE",
    "vips_city_name": "MERVILLE"
  },
  {
    "city_code": "MSLK",
    "city_name": "MESACHIE LAKE",
    "icbc_city_code": "MSLK",
    "icbc_city_name": "MESACHIE LAKE",
    "icbc_city_name_legacy": "MESACHIE LAKE",
    "vips_city_name": "MESACHIE LAKE"
  },
  {
    "city_code": "METC",
    "city_name": "METCHOSIN",
    "icbc_city_code": "METC",
    "icbc_city_name": "METCHOSIN",
    "icbc_city_name_legacy": "METCHOSIN",
    "vips_city_name": "METCHOSIN"
  },
  {
    "city_code": "MTKA",
    "city_name": "METLAKATLA",
    "icbc_city_code": "MTKA",
    "icbc_city_name": "METLAKATLA",
    "icbc_city_name_legacy": "METLAKATLA",
    "vips_city_name": "METLAKATLA"
  },
  {
    "city_code": "MZDN",
    "city_name": "MEZIADIN",
    "icbc_city_code": "MZDN",
    "icbc_city_name": "MEZIADIN",
    "icbc_city_name_legacy": "STEWART",
    "vips_city_name": "MEZIADIN"
  },
  {
    "city_code": "MNLK",
    "city_name": "MEZIADIN LAKE",
    "icbc_city_code": "MNLK",
    "icbc_city_name": "MEZIADIN LAKE",
    "icbc_city_name_legacy": "MEZIADIN LAKE",
    "vips_city_name": "MEZIADIN LAKE"
  },
  {
    "city_code": "MCCK",
    "city_name": "MICA CREEK",
    "icbc_city_code": "MCCK",
    "icbc_city_name": "MICA CREEK",
    "icbc_city_name_legacy": "MICA CREEK",
    "vips_city_name": "MICA CREEK"
  },
  {
    "city_code": "MMIS",
    "city_name": "MIDSUMMER ISLAND",
    "icbc_city_code": "MMIS",
    "icbc_city_name": "MIDSUMMER ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "MIDSUMMER ISLAND"
  },
  {
    "city_code": "MDWY",
    "city_name": "MIDWAY",
    "icbc_city_code": "MDWY",
    "icbc_city_name": "MIDWAY",
    "icbc_city_name_legacy": "MIDWAY",
    "vips_city_name": "MIDWAY"
  },
  {
    "city_code": "MLBY",
    "city_name": "MILL BAY",
    "icbc_city_code": "MLBY",
    "icbc_city_name": "MILL BAY",
    "icbc_city_name_legacy": "MILL BAY",
    "vips_city_name": "MILL BAY"
  },
  {
    "city_code": "MNNL",
    "city_name": "MINNIE LAKE",
    "icbc_city_code": "MNNL",
    "icbc_city_name": "MINNIE LAKE",
    "icbc_city_name_legacy": "QUILCHENA",
    "vips_city_name": "MINNIE LAKE"
  },
  {
    "city_code": "MNIS",
    "city_name": "MINSTREL ISLAND",
    "icbc_city_code": "MNIS",
    "icbc_city_name": "MINSTREL ISLAND",
    "icbc_city_name_legacy": "MINSTREL ISLAND",
    "vips_city_name": "MINSTREL ISLAND"
  },
  {
    "city_code": "MIOC",
    "city_name": "MIOCENE",
    "icbc_city_code": "MIOC",
    "icbc_city_name": "MIOCENE",
    "icbc_city_name_legacy": "MIOCENE",
    "vips_city_name": "MIOCENE"
  },
  {
    "city_code": "MILK",
    "city_name": "MIRROR LAKE",
    "icbc_city_code": "MILK",
    "icbc_city_name": "MIRROR LAKE",
    "icbc_city_name_legacy": "MIRROR LAKE",
    "vips_city_name": "MIRROR LAKE"
  },
  {
    "city_code": "MZLK",
    "city_name": "MISSEZULA LAKE",
    "icbc_city_code": "MZLK",
    "icbc_city_name": "MISSEZULA LAKE",
    "icbc_city_name_legacy": "PRINCETON",
    "vips_city_name": "MISSEZULA LAKE"
  },
  {
    "city_code": "MISS",
    "city_name": "MISSION",
    "icbc_city_code": "MISS",
    "icbc_city_name": "MISSION",
    "icbc_city_name_legacy": "MISSION",
    "vips_city_name": "MISSION"
  },
  {
    "city_code": "MWRT",
    "city_name": "MIWORTH",
    "icbc_city_code": "MWRT",
    "icbc_city_name": "MIWORTH",
    "icbc_city_name_legacy": "PRINCE GEORGE",
    "vips_city_name": "MIWORTH"
  },
  {
    "city_code": "MOLK",
    "city_name": "MOBERLY LAKE",
    "icbc_city_code": "MOLK",
    "icbc_city_name": "MOBERLY LAKE",
    "icbc_city_name_legacy": "MOBERLY LAKE",
    "vips_city_name": "MOBERLY LAKE"
  },
  {
    "city_code": "MKIS",
    "city_name": "MOKETAS ISLAND",
    "icbc_city_code": "MKIS",
    "icbc_city_name": "MOKETAS ISLAND",
    "icbc_city_name_legacy": "PORT ALICE",
    "vips_city_name": "MOKETAS ISLAND"
  },
  {
    "city_code": "MCHL",
    "city_name": "MOMICH LAKE",
    "icbc_city_code": "MCHL",
    "icbc_city_name": "MOMICH LAKE",
    "icbc_city_name_legacy": "SEYMOUR ARM",
    "vips_city_name": "MOMICH LAKE"
  },
  {
    "city_code": "MKMN",
    "city_name": "MONKMAN",
    "icbc_city_code": "MKMN",
    "icbc_city_name": "MONKMAN",
    "icbc_city_name_legacy": "TUMBLER RIDGE",
    "vips_city_name": "MONKMAN"
  },
  {
    "city_code": "MTCK",
    "city_name": "MONTE CREEK",
    "icbc_city_code": "MTCK",
    "icbc_city_name": "MONTE CREEK",
    "icbc_city_name_legacy": "MONTE CREEK",
    "vips_city_name": "MONTE CREEK"
  },
  {
    "city_code": "MTLK",
    "city_name": "MONTE LAKE",
    "icbc_city_code": "MTLK",
    "icbc_city_name": "MONTE LAKE",
    "icbc_city_name_legacy": "MONTE LAKE",
    "vips_city_name": "MONTE LAKE"
  },
  {
    "city_code": "MNTY",
    "city_name": "MONTNEY",
    "icbc_city_code": "MNTY",
    "icbc_city_name": "MONTNEY",
    "icbc_city_name_legacy": "MONTNEY",
    "vips_city_name": "MONTNEY"
  },
  {
    "city_code": "MTRS",
    "city_name": "MONTROSE",
    "icbc_city_code": "MTRS",
    "icbc_city_name": "MONTROSE",
    "icbc_city_name_legacy": "MONTROSE",
    "vips_city_name": "MONTROSE"
  },
  {
    "city_code": "MSHT",
    "city_name": "MOOSE HEIGHTS",
    "icbc_city_code": "MSHT",
    "icbc_city_name": "MOOSE HEIGHTS",
    "icbc_city_name_legacy": "MOOSE HEIGHTS",
    "vips_city_name": "MOOSE HEIGHTS"
  },
  {
    "city_code": "MBIS",
    "city_name": "MORESBY ISLAND",
    "icbc_city_code": "MBIS",
    "icbc_city_name": "MORESBY ISLAND",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "MORESBY ISLAND"
  },
  {
    "city_code": "MSVL",
    "city_name": "MOSSVALE",
    "icbc_city_code": "MSVL",
    "icbc_city_name": "MOSSVALE",
    "icbc_city_name_legacy": "PRINCE GEORGE",
    "vips_city_name": "MOSSVALE"
  },
  {
    "city_code": "MTCR",
    "city_name": "MOUNT CURRIE",
    "icbc_city_code": "MTCR",
    "icbc_city_name": "MOUNT CURRIE",
    "icbc_city_name_legacy": "MOUNT CURRIE",
    "vips_city_name": "MOUNT CURRIE"
  },
  {
    "city_code": "MTRN",
    "city_name": "MOUNT ROBSON",
    "icbc_city_code": "MTRN",
    "icbc_city_name": "MOUNT ROBSON",
    "icbc_city_name_legacy": "MOUNT ROBSON",
    "vips_city_name": "MOUNT ROBSON"
  },
  {
    "city_code": "MOYE",
    "city_name": "MOYIE",
    "icbc_city_code": "MOYE",
    "icbc_city_name": "MOYIE",
    "icbc_city_name_legacy": "MOYIE",
    "vips_city_name": "MOYIE"
  },
  {
    "city_code": "MTWN",
    "city_name": "MT WASHINGTON",
    "icbc_city_code": "MTWN",
    "icbc_city_name": "MT WASHINGTON",
    "icbc_city_name_legacy": "COURTENAY",
    "vips_city_name": "MT WASHINGTON"
  },
  {
    "city_code": "MLMY",
    "city_name": "MT LE MORAY",
    "icbc_city_code": "MLMY",
    "icbc_city_name": "MT LE MORAY",
    "icbc_city_name_legacy": "TSAY KEH DENE",
    "vips_city_name": "MT LE MORAY"
  },
  {
    "city_code": "MRPP",
    "city_name": "MT ROBSON PROVINCIAL PARK",
    "icbc_city_code": "MRPP",
    "icbc_city_name": "MT ROBSON PROVINCIAL PARK",
    "icbc_city_name_legacy": "VALEMOUNT",
    "vips_city_name": "MT ROBSON PROVINCIAL PARK"
  },
  {
    "city_code": "MTFP",
    "city_name": "MT TERRY FOX PROVINCIAL PARK",
    "icbc_city_code": "MTFP",
    "icbc_city_name": "MT TERRY FOX PROVINCIAL PARK",
    "icbc_city_name_legacy": "VALEMOUNT",
    "vips_city_name": "MT TERRY FOX PROVINCIAL PARK"
  },
  {
    "city_code": "MDRV",
    "city_name": "MUD RIVER",
    "icbc_city_code": "MDRV",
    "icbc_city_name": "MUD RIVER",
    "icbc_city_name_legacy": "MUD RIVER",
    "vips_city_name": "MUD RIVER"
  },
  {
    "city_code": "MGIS",
    "city_name": "MUDGE ISLAND",
    "icbc_city_code": "MGIS",
    "icbc_city_name": "MUDGE ISLAND",
    "icbc_city_name_legacy": "GABRIOLA",
    "vips_city_name": "MUDGE ISLAND"
  },
  {
    "city_code": "MHLK",
    "city_name": "MUNCHO LAKE",
    "icbc_city_code": "MHLK",
    "icbc_city_name": "MUNCHO LAKE",
    "icbc_city_name_legacy": "MUNCHO LAKE",
    "vips_city_name": "MUNCHO LAKE"
  },
  {
    "city_code": "MHIS",
    "city_name": "MURCHISON ISLAND",
    "icbc_city_code": "MHIS",
    "icbc_city_name": "MURCHISON ISLAND",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "MURCHISON ISLAND"
  },
  {
    "city_code": "MURD",
    "city_name": "MURDALE",
    "icbc_city_code": "MURD",
    "icbc_city_name": "MURDALE",
    "icbc_city_name_legacy": "MURDALE",
    "vips_city_name": "MURDALE"
  },
  {
    "city_code": "MUSK",
    "city_name": "MUSKWA",
    "icbc_city_code": "MUSK",
    "icbc_city_name": "MUSKWA",
    "icbc_city_name_legacy": "MUSKWA",
    "vips_city_name": "MUSKWA"
  },
  {
    "city_code": "NKSP",
    "city_name": "NAKUSP",
    "icbc_city_code": "NKSP",
    "icbc_city_name": "NAKUSP",
    "icbc_city_name_legacy": "NAKUSP",
    "vips_city_name": "NAKUSP"
  },
  {
    "city_code": "NAMU",
    "city_name": "NAMU",
    "icbc_city_code": "NAMU",
    "icbc_city_name": "NAMU",
    "icbc_city_name_legacy": "NAMU",
    "vips_city_name": "NAMU"
  },
  {
    "city_code": "NNIM",
    "city_name": "NANAIMO",
    "icbc_city_code": "NNIM",
    "icbc_city_name": "NANAIMO",
    "icbc_city_name_legacy": "NANAIMO",
    "vips_city_name": "NANAIMO"
  },
  {
    "city_code": "NSBA",
    "city_name": "NANOOSE BAY",
    "icbc_city_code": "NSBA",
    "icbc_city_name": "NANOOSE BAY",
    "icbc_city_name_legacy": "NANOOSE BAY",
    "vips_city_name": "NANOOSE BAY"
  },
  {
    "city_code": "NRMT",
    "city_name": "NARAMATA",
    "icbc_city_code": "NRMT",
    "icbc_city_name": "NARAMATA",
    "icbc_city_name_legacy": "NARAMATA",
    "vips_city_name": "NARAMATA"
  },
  {
    "city_code": "NCCK",
    "city_name": "NARCOSLI CREEK",
    "icbc_city_code": "NCCK",
    "icbc_city_name": "NARCOSLI CREEK",
    "icbc_city_name_legacy": "NARCOSLI CREEK",
    "vips_city_name": "NARCOSLI CREEK"
  },
  {
    "city_code": "NSCP",
    "city_name": "NASS CAMP",
    "icbc_city_code": "NSCP",
    "icbc_city_name": "NASS CAMP",
    "icbc_city_name_legacy": "NASS CAMP",
    "vips_city_name": "NASS CAMP"
  },
  {
    "city_code": "NZVY",
    "city_name": "NAZKO",
    "icbc_city_code": "NZVY",
    "icbc_city_name": "NAZKO",
    "icbc_city_name_legacy": "NAZKO",
    "vips_city_name": "NAZKO"
  },
  {
    "city_code": "NCKO",
    "city_name": "NECHAKO",
    "icbc_city_code": "NCKO",
    "icbc_city_name": "NECHAKO",
    "icbc_city_name_legacy": "NECHAKO",
    "vips_city_name": "NECHAKO"
  },
  {
    "city_code": "NEDS",
    "city_name": "NEEDLES",
    "icbc_city_code": "NEDS",
    "icbc_city_name": "NEEDLES",
    "icbc_city_name_legacy": "NEEDLES",
    "vips_city_name": "NEEDLES"
  },
  {
    "city_code": "NLSN",
    "city_name": "NELSON",
    "icbc_city_code": "NLSN",
    "icbc_city_name": "NELSON",
    "icbc_city_name_legacy": "NELSON",
    "vips_city_name": "NELSON"
  },
  {
    "city_code": "NLIS",
    "city_name": "NELSON ISLAND",
    "icbc_city_code": "NLIS",
    "icbc_city_name": "NELSON ISLAND",
    "icbc_city_name_legacy": "MADEIRA PARK",
    "vips_city_name": "NELSON ISLAND"
  },
  {
    "city_code": "NLWY",
    "city_name": "NELWAY",
    "icbc_city_code": "NLWY",
    "icbc_city_name": "NELWAY",
    "icbc_city_name_legacy": "NELWAY",
    "vips_city_name": "NELWAY"
  },
  {
    "city_code": "NMVY",
    "city_name": "NEMAIAH VALLEY",
    "icbc_city_code": "NMVY",
    "icbc_city_name": "NEMAIAH VALLEY",
    "icbc_city_name_legacy": "NEMAIAH VALLEY",
    "vips_city_name": "NEMAIAH VALLEY"
  },
  {
    "city_code": "NSLK",
    "city_name": "NESS LAKE",
    "icbc_city_code": "NSLK",
    "icbc_city_name": "NESS LAKE",
    "icbc_city_name_legacy": "PRINCE GEORGE",
    "vips_city_name": "NESS LAKE"
  },
  {
    "city_code": "NWAH",
    "city_name": "NEW AIYANSH",
    "icbc_city_code": "NWAH",
    "icbc_city_name": "NEW AIYANSH",
    "icbc_city_name_legacy": "NEW AIYANSH",
    "vips_city_name": "NEW AIYANSH"
  },
  {
    "city_code": "NDVR",
    "city_name": "NEW DENVER",
    "icbc_city_code": "NDVR",
    "icbc_city_name": "NEW DENVER",
    "icbc_city_name_legacy": "NEW DENVER",
    "vips_city_name": "NEW DENVER"
  },
  {
    "city_code": "NHZN",
    "city_name": "NEW HAZELTON",
    "icbc_city_code": "NHZN",
    "icbc_city_name": "NEW HAZELTON",
    "icbc_city_name_legacy": "NEW HAZELTON",
    "vips_city_name": "NEW HAZELTON"
  },
  {
    "city_code": "NEWW",
    "city_name": "NEW WESTMINSTER",
    "icbc_city_code": "NEWW",
    "icbc_city_name": "NEW WESTMINSTER",
    "icbc_city_name_legacy": "NEW WESTMINSTER",
    "vips_city_name": "NEW WESTMINSTER"
  },
  {
    "city_code": "NEWG",
    "city_name": "NEWGATE",
    "icbc_city_code": "NEWG",
    "icbc_city_name": "NEWGATE",
    "icbc_city_name_legacy": "NEWGATE",
    "vips_city_name": "NEWGATE"
  },
  {
    "city_code": "NCLK",
    "city_name": "NICOLA LAKE",
    "icbc_city_code": "NCLK",
    "icbc_city_name": "NICOLA LAKE",
    "icbc_city_name_legacy": "MERRITT",
    "vips_city_name": "NICOLA LAKE"
  },
  {
    "city_code": "NIIS",
    "city_name": "NIGEI ISLAND",
    "icbc_city_code": "NIIS",
    "icbc_city_name": "NIGEI ISLAND",
    "icbc_city_name_legacy": "PORT HARDY",
    "vips_city_name": "NIGEI ISLAND"
  },
  {
    "city_code": "NIMP",
    "city_name": "NIMPKISH",
    "icbc_city_code": "NIMP",
    "icbc_city_name": "NIMPKISH",
    "icbc_city_name_legacy": "NIMPKISH",
    "vips_city_name": "NIMPKISH"
  },
  {
    "city_code": "NMLK",
    "city_name": "NIMPO LAKE",
    "icbc_city_code": "NMLK",
    "icbc_city_name": "NIMPO LAKE",
    "icbc_city_name_legacy": "NIMPO LAKE",
    "vips_city_name": "NIMPO LAKE"
  },
  {
    "city_code": "NISK",
    "city_name": "NISKONLITH LAKE",
    "icbc_city_code": "NISK",
    "icbc_city_name": "NISKONLITH LAKE",
    "icbc_city_name_legacy": "CHASE",
    "vips_city_name": "NISKONLITH LAKE"
  },
  {
    "city_code": "NOOA",
    "city_name": "NOOAITCH",
    "icbc_city_code": "NOOA",
    "icbc_city_name": "NOOAITCH",
    "icbc_city_name_legacy": "LOWER NICOLA",
    "vips_city_name": "NOOAITCH"
  },
  {
    "city_code": "NKIS",
    "city_name": "NOOTKA ISLAND",
    "icbc_city_code": "NKIS",
    "icbc_city_name": "NOOTKA ISLAND",
    "icbc_city_name_legacy": "GOLD RIVER",
    "vips_city_name": "NOOTKA ISLAND"
  },
  {
    "city_code": "NORA",
    "city_name": "NORALEE",
    "icbc_city_code": "NORA",
    "icbc_city_name": "NORALEE",
    "icbc_city_name_legacy": "NORALEE",
    "vips_city_name": "NORALEE"
  },
  {
    "city_code": "NBRL",
    "city_name": "NORTH BARRIERE LAKE",
    "icbc_city_code": "NBRL",
    "icbc_city_name": "NORTH BARRIERE LAKE",
    "icbc_city_name_legacy": "BARRIERE",
    "vips_city_name": "NORTH BARRIERE LAKE"
  },
  {
    "city_code": "NBND",
    "city_name": "NORTH BEND",
    "icbc_city_code": "NBND",
    "icbc_city_name": "NORTH BEND",
    "icbc_city_name_legacy": "NORTH BEND",
    "vips_city_name": "NORTH BEND"
  },
  {
    "city_code": "NBON",
    "city_name": "NORTH BONAPARTE",
    "icbc_city_code": "NBON",
    "icbc_city_name": "NORTH BONAPARTE",
    "icbc_city_name_legacy": "100 MILE HOUSE",
    "vips_city_name": "NORTH BONAPARTE"
  },
  {
    "city_code": "NBIS",
    "city_name": "NORTH BROUGHTON ISLAND",
    "icbc_city_code": "NBIS",
    "icbc_city_name": "NORTH BROUGHTON ISLAND",
    "icbc_city_name_legacy": "PORT HARDY",
    "vips_city_name": "NORTH BROUGHTON ISLAND"
  },
  {
    "city_code": "NFLK",
    "city_name": "NORTH FALKLAND",
    "icbc_city_code": "NFLK",
    "icbc_city_name": "NORTH FALKLAND",
    "icbc_city_name_legacy": "FALKLAND",
    "vips_city_name": "NORTH FALKLAND"
  },
  {
    "city_code": "NKLK",
    "city_name": "NORTH KINBASKET LAKE",
    "icbc_city_code": "NKLK",
    "icbc_city_name": "NORTH KINBASKET LAKE",
    "icbc_city_name_legacy": "REVELSTOKE",
    "vips_city_name": "NORTH KINBASKET LAKE"
  },
  {
    "city_code": "NMAR",
    "city_name": "NORTH MARA",
    "icbc_city_code": "NMAR",
    "icbc_city_name": "NORTH MARA",
    "icbc_city_name_legacy": "SICAMOUS",
    "vips_city_name": "NORTH MARA"
  },
  {
    "city_code": "NPIS",
    "city_name": "NORTH PENDER ISLAND",
    "icbc_city_code": "NPIS",
    "icbc_city_name": "NORTH PENDER ISLAND",
    "icbc_city_name_legacy": "PENDER ISLAND",
    "vips_city_name": "NORTH PENDER ISLAND"
  },
  {
    "city_code": "NRPN",
    "city_name": "NORTH PINE",
    "icbc_city_code": "NRPN",
    "icbc_city_name": "NORTH PINE",
    "icbc_city_name_legacy": "NORTH PINE",
    "vips_city_name": "NORTH PINE"
  },
  {
    "city_code": "NSAA",
    "city_name": "NORTH SAANICH",
    "icbc_city_code": "NSAA",
    "icbc_city_name": "NORTH SAANICH",
    "icbc_city_name_legacy": "NORTH SAANICH",
    "vips_city_name": "NORTH SAANICH"
  },
  {
    "city_code": "NSHO",
    "city_name": "NORTH SHORE",
    "icbc_city_code": "NSHO",
    "icbc_city_name": "NORTH SHORE",
    "icbc_city_name_legacy": "NORTH VANCOUVER",
    "vips_city_name": "NORTH SHORE"
  },
  {
    "city_code": "NTIR",
    "city_name": "NORTH THOMPSON IR",
    "icbc_city_code": "NTIR",
    "icbc_city_name": "NORTH THOMPSON IR",
    "icbc_city_name_legacy": "BARRIERE",
    "vips_city_name": "NORTH THOMPSON IR"
  },
  {
    "city_code": "NVAN",
    "city_name": "NORTH VANCOUVER",
    "icbc_city_code": "NVAN",
    "icbc_city_name": "NORTH VANCOUVER",
    "icbc_city_name_legacy": "NORTH VANCOUVER",
    "vips_city_name": "NORTH VANCOUVER"
  },
  {
    "city_code": "NOHL",
    "city_name": "NOTCH HILL",
    "icbc_city_code": "NOHL",
    "icbc_city_name": "NOTCH HILL",
    "icbc_city_name_legacy": "NOTCH HILL",
    "vips_city_name": "NOTCH HILL"
  },
  {
    "city_code": "NKKL",
    "city_name": "NUKKO LAKE",
    "icbc_city_code": "NKKL",
    "icbc_city_name": "NUKKO LAKE",
    "icbc_city_name_legacy": "NUKKO LAKE",
    "vips_city_name": "NUKKO LAKE"
  },
  {
    "city_code": "OKBY",
    "city_name": "OAK BAY",
    "icbc_city_code": "OKBY",
    "icbc_city_name": "OAK BAY",
    "icbc_city_name_legacy": "OAK BAY",
    "vips_city_name": "OAK BAY"
  },
  {
    "city_code": "OSIS",
    "city_name": "OASIS",
    "icbc_city_code": "OSIS",
    "icbc_city_name": "OASIS",
    "icbc_city_name_legacy": "OASIS",
    "vips_city_name": "OASIS"
  },
  {
    "city_code": "OBIS",
    "city_name": "OBSTRUCTION ISLAND",
    "icbc_city_code": "OBIS",
    "icbc_city_name": "OBSTRUCTION ISLAND",
    "icbc_city_name_legacy": "AHOUSAT",
    "vips_city_name": "OBSTRUCTION ISLAND"
  },
  {
    "city_code": "OCFL",
    "city_name": "OCEAN FALLS",
    "icbc_city_code": "OCFL",
    "icbc_city_name": "OCEAN FALLS",
    "icbc_city_name_legacy": "OCEAN FALLS",
    "vips_city_name": "OCEAN FALLS"
  },
  {
    "city_code": "OKNF",
    "city_name": "OKANAGAN FALLS",
    "icbc_city_code": "OKNF",
    "icbc_city_name": "OKANAGAN FALLS",
    "icbc_city_name_legacy": "OKANAGAN FALLS",
    "vips_city_name": "OKANAGAN FALLS"
  },
  {
    "city_code": "ONIR",
    "city_name": "OKANAGAN IR NORTH",
    "icbc_city_code": "ONIR",
    "icbc_city_name": "OKANAGAN IR NORTH",
    "icbc_city_name_legacy": "VERNON",
    "vips_city_name": "OKANAGAN IR NORTH"
  },
  {
    "city_code": "OSIR",
    "city_name": "OKANAGAN IR SOUTH",
    "icbc_city_code": "OSIR",
    "icbc_city_name": "OKANAGAN IR SOUTH",
    "icbc_city_name_legacy": "VERNON",
    "vips_city_name": "OKANAGAN IR SOUTH"
  },
  {
    "city_code": "OLLA",
    "city_name": "OLALLA",
    "icbc_city_code": "OLLA",
    "icbc_city_name": "OLALLA",
    "icbc_city_name_legacy": "OLALLA",
    "vips_city_name": "OLALLA"
  },
  {
    "city_code": "OLVR",
    "city_name": "OLIVER",
    "icbc_city_code": "OLVR",
    "icbc_city_name": "OLIVER",
    "icbc_city_name_legacy": "OLIVER",
    "vips_city_name": "OLIVER"
  },
  {
    "city_code": "OILK",
    "city_name": "ONE ISLAND LAKE",
    "icbc_city_code": "OILK",
    "icbc_city_name": "ONE ISLAND LAKE",
    "icbc_city_name_legacy": "TUMBLER RIDGE",
    "vips_city_name": "ONE ISLAND LAKE"
  },
  {
    "city_code": "OORV",
    "city_name": "OONA RIVER",
    "icbc_city_code": "OORV",
    "icbc_city_name": "OONA RIVER",
    "icbc_city_name_legacy": "OONA RIVER",
    "vips_city_name": "OONA RIVER"
  },
  {
    "city_code": "OTCH",
    "city_name": "OOTISCHENIA",
    "icbc_city_code": "OTCH",
    "icbc_city_name": "OOTISCHENIA",
    "icbc_city_name_legacy": "CASTLEGAR",
    "vips_city_name": "OOTISCHENIA"
  },
  {
    "city_code": "OOLK",
    "city_name": "OOTSA LAKE",
    "icbc_city_code": "OOLK",
    "icbc_city_name": "OOTSA LAKE",
    "icbc_city_name_legacy": "OOTSA LAKE",
    "vips_city_name": "OOTSA LAKE"
  },
  {
    "city_code": "OSBN",
    "city_name": "OSBORN",
    "icbc_city_code": "OSBN",
    "icbc_city_name": "OSBORN",
    "icbc_city_name_legacy": "FORT ST JOHN",
    "vips_city_name": "OSBORN"
  },
  {
    "city_code": "OSYO",
    "city_name": "OSOYOOS",
    "icbc_city_code": "OSYO",
    "icbc_city_name": "OSOYOOS",
    "icbc_city_name_legacy": "OSOYOOS",
    "vips_city_name": "OSOYOOS"
  },
  {
    "city_code": "OUT",
    "city_name": "OTTER POINT",
    "icbc_city_code": "OUT",
    "icbc_city_name": "OTTER POINT",
    "icbc_city_name_legacy": "OTTER POINT",
    "vips_city_name": "OTTER POINT"
  },
  {
    "city_code": "OWEK",
    "city_name": "OWEEKENO",
    "icbc_city_code": "OWEK",
    "icbc_city_name": "OWEEKENO",
    "icbc_city_name_legacy": "BELLA BELLA",
    "vips_city_name": "OWEEKENO"
  },
  {
    "city_code": "OWIS",
    "city_name": "OWL ISLAND",
    "icbc_city_code": "OWIS",
    "icbc_city_name": "OWL ISLAND",
    "icbc_city_name_legacy": "PENDER ISLAND",
    "vips_city_name": "OWL ISLAND"
  },
  {
    "city_code": "PRPN",
    "city_name": "PACIFIC RIM PARK NORTH",
    "icbc_city_code": "PRPN",
    "icbc_city_name": "PACIFIC RIM PARK NORTH",
    "icbc_city_name_legacy": "BAMFIELD",
    "vips_city_name": "PACIFIC RIM PARK NORTH"
  },
  {
    "city_code": "PRPS",
    "city_name": "PACIFIC RIM PARK SOUTH",
    "icbc_city_code": "PRPS",
    "icbc_city_name": "PACIFIC RIM PARK SOUTH",
    "icbc_city_name_legacy": "BAMFIELD",
    "vips_city_name": "PACIFIC RIM PARK SOUTH"
  },
  {
    "city_code": "PALL",
    "city_name": "PALLING",
    "icbc_city_code": "PALL",
    "icbc_city_name": "PALLING",
    "icbc_city_name_legacy": "PALLING",
    "vips_city_name": "PALLING"
  },
  {
    "city_code": "PANO",
    "city_name": "PANORAMA",
    "icbc_city_code": "PANO",
    "icbc_city_name": "PANORAMA",
    "icbc_city_name_legacy": "PANORAMA",
    "vips_city_name": "PANORAMA"
  },
  {
    "city_code": "PKIS",
    "city_name": "PARKER ISLAND",
    "icbc_city_code": "PKIS",
    "icbc_city_name": "PARKER ISLAND",
    "icbc_city_name_legacy": "GALIANO",
    "vips_city_name": "PARKER ISLAND"
  },
  {
    "city_code": "PAVL",
    "city_name": "PARKSVILLE",
    "icbc_city_code": "PAVL",
    "icbc_city_name": "PARKSVILLE",
    "icbc_city_name_legacy": "PARKSVILLE",
    "vips_city_name": "PARKSVILLE"
  },
  {
    "city_code": "PIRP",
    "city_name": "PARSNIP",
    "icbc_city_code": "PIRP",
    "icbc_city_name": "PARSNIP",
    "icbc_city_name_legacy": "TSAY KEH DENE",
    "vips_city_name": "PARSNIP"
  },
  {
    "city_code": "PRSN",
    "city_name": "PARSON",
    "icbc_city_code": "PRSN",
    "icbc_city_name": "PARSON",
    "icbc_city_name_legacy": "PARSON",
    "vips_city_name": "PARSON"
  },
  {
    "city_code": "PRIL",
    "city_name": "PARSON ISLAND",
    "icbc_city_code": "PRIL",
    "icbc_city_name": "PARSON ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "PARSON ISLAND"
  },
  {
    "city_code": "PSKL",
    "city_name": "PASKA LAKE",
    "icbc_city_code": "PSKL",
    "icbc_city_name": "PASKA LAKE",
    "icbc_city_name_legacy": "LOGAN LAKE",
    "vips_city_name": "PASKA LAKE"
  },
  {
    "city_code": "PSCK",
    "city_name": "PASS CREEK",
    "icbc_city_code": "PSCK",
    "icbc_city_name": "PASS CREEK",
    "icbc_city_name_legacy": "CASTLEGAR",
    "vips_city_name": "PASS CREEK"
  },
  {
    "city_code": "PSMR",
    "city_name": "PASSMORE",
    "icbc_city_code": "PSMR",
    "icbc_city_name": "PASSMORE",
    "icbc_city_name_legacy": "PASSMORE",
    "vips_city_name": "PASSMORE"
  },
  {
    "city_code": "PLLK",
    "city_name": "PAUL LAKE",
    "icbc_city_code": "PLLK",
    "icbc_city_name": "PAUL LAKE",
    "icbc_city_name_legacy": "PAUL LAKE",
    "vips_city_name": "PAUL LAKE"
  },
  {
    "city_code": "PVLN",
    "city_name": "PAVILION",
    "icbc_city_code": "PVLN",
    "icbc_city_name": "PAVILION",
    "icbc_city_name_legacy": "PAVILION",
    "vips_city_name": "PAVILION"
  },
  {
    "city_code": "PCLD",
    "city_name": "PEACHLAND",
    "icbc_city_code": "PCLD",
    "icbc_city_name": "PEACHLAND",
    "icbc_city_name_legacy": "PEACHLAND",
    "vips_city_name": "PEACHLAND"
  },
  {
    "city_code": "PSIS",
    "city_name": "PEARSE ISLAND",
    "icbc_city_code": "PSIS",
    "icbc_city_name": "PEARSE ISLAND",
    "icbc_city_name_legacy": "KINCOLITH",
    "vips_city_name": "PEARSE ISLAND"
  },
  {
    "city_code": "PEEJ",
    "city_name": "PEEJAY",
    "icbc_city_code": "PEEJ",
    "icbc_city_name": "PEEJAY",
    "icbc_city_name_legacy": "FORT ST JOHN",
    "vips_city_name": "PEEJAY"
  },
  {
    "city_code": "PEMB",
    "city_name": "PEMBERTON",
    "icbc_city_code": "PEMB",
    "icbc_city_name": "PEMBERTON",
    "icbc_city_name_legacy": "PEMBERTON",
    "vips_city_name": "PEMBERTON"
  },
  {
    "city_code": "PMBM",
    "city_name": "PEMBERTON MEADOWS",
    "icbc_city_code": "PMBM",
    "icbc_city_name": "PEMBERTON MEADOWS",
    "icbc_city_name_legacy": "PEMBERTON MEADO",
    "vips_city_name": "PEMBERTON MEADOWS"
  },
  {
    "city_code": "PDDR",
    "city_name": "PEND DOREILLE",
    "icbc_city_code": "PDDR",
    "icbc_city_name": "PEND DOREILLE",
    "icbc_city_name_legacy": "TRAIL",
    "vips_city_name": "PEND DOREILLE"
  },
  {
    "city_code": "PHBR",
    "city_name": "PENDER HARBOUR",
    "icbc_city_code": "PHBR",
    "icbc_city_name": "PENDER HARBOUR",
    "icbc_city_name_legacy": "PENDER HARBOUR",
    "vips_city_name": "PENDER HARBOUR"
  },
  {
    "city_code": "PDIS",
    "city_name": "PENDER ISLAND",
    "icbc_city_code": "PDIS",
    "icbc_city_name": "PENDER ISLAND",
    "icbc_city_name_legacy": "PENDER ISLAND",
    "vips_city_name": "PENDER ISLAND"
  },
  {
    "city_code": "PNIS",
    "city_name": "PENELAKUT ISLAND",
    "icbc_city_code": "PNIS",
    "icbc_city_name": "PENELAKUT ISLAND",
    "icbc_city_name_legacy": "CHEMAINUS",
    "vips_city_name": "PENELAKUT ISLAND"
  },
  {
    "city_code": "PENK",
    "city_name": "PENNASK SUMMIT",
    "icbc_city_code": "PENK",
    "icbc_city_name": "PEACHLAND",
    "icbc_city_name_legacy": "PENNASK SUMMIT",
    "vips_city_name": "PEACHLAND"
  },
  {
    "city_code": "PENN",
    "city_name": "PENNY",
    "icbc_city_code": "PENN",
    "icbc_city_name": "PENNY",
    "icbc_city_name_legacy": "PENNY",
    "vips_city_name": "PENNY"
  },
  {
    "city_code": "PNTN",
    "city_name": "PENTICTON",
    "icbc_city_code": "PNTN",
    "icbc_city_name": "PENTICTON",
    "icbc_city_name_legacy": "PENTICTON",
    "vips_city_name": "PENTICTON"
  },
  {
    "city_code": "PRSG",
    "city_name": "PERRY SIDING",
    "icbc_city_code": "PRSG",
    "icbc_city_name": "PERRY SIDING",
    "icbc_city_name_legacy": "PERRY SIDING",
    "vips_city_name": "PERRY SIDING"
  },
  {
    "city_code": "PETH",
    "city_name": "PETER HOPE LAKE",
    "icbc_city_code": "PETH",
    "icbc_city_name": "PETER HOPE LAKE",
    "icbc_city_name_legacy": "TRAPP LAKE",
    "vips_city_name": "PETER HOPE LAKE"
  },
  {
    "city_code": "PRIS",
    "city_name": "PIERS ISLAND",
    "icbc_city_code": "PRIS",
    "icbc_city_name": "PIERS ISLAND",
    "icbc_city_name_legacy": "SIDNEY",
    "vips_city_name": "PIERS ISLAND"
  },
  {
    "city_code": "PNLK",
    "city_name": "PINANTAN LAKE",
    "icbc_city_code": "PNLK",
    "icbc_city_name": "PINANTAN LAKE",
    "icbc_city_name_legacy": "PINANTAN LAKE",
    "vips_city_name": "PINANTAN LAKE"
  },
  {
    "city_code": "PINC",
    "city_name": "PINCHI",
    "icbc_city_code": "PINC",
    "icbc_city_name": "PINCHI",
    "icbc_city_name_legacy": "FORT ST JAMES",
    "vips_city_name": "PINCHI"
  },
  {
    "city_code": "PILK",
    "city_name": "PINCHI LAKE",
    "icbc_city_code": "PILK",
    "icbc_city_name": "PINCHI LAKE",
    "icbc_city_name_legacy": "PINCHI LAKE",
    "vips_city_name": "PINCHI LAKE"
  },
  {
    "city_code": "PIPS",
    "city_name": "PINE PASS",
    "icbc_city_code": "PIPS",
    "icbc_city_name": "PINE PASS",
    "icbc_city_name_legacy": "TSAY KEH DENE",
    "vips_city_name": "PINE PASS"
  },
  {
    "city_code": "PNVY",
    "city_name": "PINE VALLEY",
    "icbc_city_code": "PNVY",
    "icbc_city_name": "PINE VALLEY",
    "icbc_city_name_legacy": "PINE VALLEY",
    "vips_city_name": "PINE VALLEY"
  },
  {
    "city_code": "PNVW",
    "city_name": "PINEVIEW",
    "icbc_city_code": "PNVW",
    "icbc_city_name": "PINEVIEW",
    "icbc_city_name_legacy": "PRINCE GEORGE",
    "vips_city_name": "PINEVIEW"
  },
  {
    "city_code": "PNMT",
    "city_name": "PINK MOUNTAIN",
    "icbc_city_code": "PNMT",
    "icbc_city_name": "PINK MOUNTAIN",
    "icbc_city_name_legacy": "PINK MOUNTAIN",
    "vips_city_name": "PINK MOUNTAIN"
  },
  {
    "city_code": "PTIS",
    "city_name": "PITT ISLAND",
    "icbc_city_code": "PTIS",
    "icbc_city_name": "PITT ISLAND",
    "icbc_city_name_legacy": "HARTLEY BAY",
    "vips_city_name": "PITT ISLAND"
  },
  {
    "city_code": "PITT",
    "city_name": "PITT MEADOWS",
    "icbc_city_code": "PITT",
    "icbc_city_name": "PITT MEADOWS",
    "icbc_city_name_legacy": "PITT MEADOWS",
    "vips_city_name": "PITT MEADOWS"
  },
  {
    "city_code": "POOL",
    "city_name": "POOLEY ISLAND",
    "icbc_city_code": "POOL",
    "icbc_city_name": "POOLEY ISLAND",
    "icbc_city_name_legacy": "BELLA BELLA",
    "vips_city_name": "POOLEY ISLAND"
  },
  {
    "city_code": "PKUM",
    "city_name": "POPKUM",
    "icbc_city_code": "PKUM",
    "icbc_city_name": "POPKUM",
    "icbc_city_name_legacy": "POPKUM",
    "vips_city_name": "POPKUM"
  },
  {
    "city_code": "PCIS",
    "city_name": "PORCHER ISLAND",
    "icbc_city_code": "PCIS",
    "icbc_city_name": "PORCHER ISLAND",
    "icbc_city_name_legacy": "PORCHER ISLAND",
    "vips_city_name": "PORCHER ISLAND"
  },
  {
    "city_code": "PTAI",
    "city_name": "PORT ALBERNI",
    "icbc_city_code": "PTAI",
    "icbc_city_name": "PORT ALBERNI",
    "icbc_city_name_legacy": "PORT ALBERNI",
    "vips_city_name": "PORT ALBERNI"
  },
  {
    "city_code": "PTAN",
    "city_name": "PORT ALBION",
    "icbc_city_code": "PTAN",
    "icbc_city_name": "PORT ALBION",
    "icbc_city_name_legacy": "PORT ALBION",
    "vips_city_name": "PORT ALBION"
  },
  {
    "city_code": "PTAC",
    "city_name": "PORT ALICE",
    "icbc_city_code": "PTAC",
    "icbc_city_name": "PORT ALICE",
    "icbc_city_name_legacy": "PORT ALICE",
    "vips_city_name": "PORT ALICE"
  },
  {
    "city_code": "PTCS",
    "city_name": "PORT CLEMENTS",
    "icbc_city_code": "PTCS",
    "icbc_city_name": "PORT CLEMENTS",
    "icbc_city_name_legacy": "PORT CLEMENTS",
    "vips_city_name": "PORT CLEMENTS"
  },
  {
    "city_code": "POCO",
    "city_name": "PORT COQUITLAM",
    "icbc_city_code": "POCO",
    "icbc_city_name": "PORT COQUITLAM",
    "icbc_city_name_legacy": "PORT COQUITLAM",
    "vips_city_name": "PORT COQUITLAM"
  },
  {
    "city_code": "PTED",
    "city_name": "PORT EDWARD",
    "icbc_city_code": "PTED",
    "icbc_city_name": "PORT EDWARD",
    "icbc_city_name_legacy": "PORT EDWARD",
    "vips_city_name": "PORT EDWARD"
  },
  {
    "city_code": "PTEN",
    "city_name": "PORT ESSINGTON",
    "icbc_city_code": "PTEN",
    "icbc_city_name": "PORT ESSINGTON",
    "icbc_city_name_legacy": "PORT ESSINGTON",
    "vips_city_name": "PORT ESSINGTON"
  },
  {
    "city_code": "PTHY",
    "city_name": "PORT HARDY",
    "icbc_city_code": "PTHY",
    "icbc_city_name": "PORT HARDY",
    "icbc_city_name_legacy": "PORT HARDY",
    "vips_city_name": "PORT HARDY"
  },
  {
    "city_code": "PTML",
    "city_name": "PORT MCNEILL",
    "icbc_city_code": "PTML",
    "icbc_city_name": "PORT MCNEILL",
    "icbc_city_name_legacy": "PORT MCNEILL",
    "vips_city_name": "PORT MCNEILL"
  },
  {
    "city_code": "PTME",
    "city_name": "PORT MELLON",
    "icbc_city_code": "PTME",
    "icbc_city_name": "PORT MELLON",
    "icbc_city_name_legacy": "PORT MELLON",
    "vips_city_name": "PORT MELLON"
  },
  {
    "city_code": "PMDY",
    "city_name": "PORT MOODY",
    "icbc_city_code": "PMDY",
    "icbc_city_name": "PORT MOODY",
    "icbc_city_name_legacy": "PORT MOODY",
    "vips_city_name": "PORT MOODY"
  },
  {
    "city_code": "PTNV",
    "city_name": "PORT NEVILLE",
    "icbc_city_code": "PTNV",
    "icbc_city_name": "PORT NEVILLE",
    "icbc_city_name_legacy": "PORT NEVILLE",
    "vips_city_name": "PORT NEVILLE"
  },
  {
    "city_code": "PTRF",
    "city_name": "PORT RENFREW",
    "icbc_city_code": "PTRF",
    "icbc_city_name": "PORT RENFREW",
    "icbc_city_name_legacy": "PORT RENFREW",
    "vips_city_name": "PORT RENFREW"
  },
  {
    "city_code": "PLIS",
    "city_name": "PORTLAND ISLAND",
    "icbc_city_code": "PLIS",
    "icbc_city_name": "PORTLAND ISLAND",
    "icbc_city_name_legacy": "PORTLAND ISLAND",
    "vips_city_name": "PORTLAND ISLAND"
  },
  {
    "city_code": "PCCP",
    "city_name": "POUCE COUPE",
    "icbc_city_code": "PCCP",
    "icbc_city_name": "POUCE COUPE",
    "icbc_city_name_legacy": "POUCE COUPE",
    "vips_city_name": "POUCE COUPE"
  },
  {
    "city_code": "PWKG",
    "city_name": "POWDER KING",
    "icbc_city_code": "PWKG",
    "icbc_city_name": "POWDER KING",
    "icbc_city_name_legacy": "TSAY KEH DENE",
    "vips_city_name": "POWDER KING"
  },
  {
    "city_code": "PWRV",
    "city_name": "POWELL RIVER",
    "icbc_city_code": "PWRV",
    "icbc_city_name": "POWELL RIVER",
    "icbc_city_name_legacy": "POWELL RIVER",
    "vips_city_name": "POWELL RIVER"
  },
  {
    "city_code": "PEIS",
    "city_name": "PRESCOTT ISLAND",
    "icbc_city_code": "PEIS",
    "icbc_city_name": "PRESCOTT ISLAND",
    "icbc_city_name_legacy": "KITKATLA",
    "vips_city_name": "PRESCOTT ISLAND"
  },
  {
    "city_code": "PSP",
    "city_name": "PRESPATOU",
    "icbc_city_code": "PSP",
    "icbc_city_name": "PRESPATOU",
    "icbc_city_name_legacy": "PRESPATOU",
    "vips_city_name": "PRESPATOU"
  },
  {
    "city_code": "PSSL",
    "city_name": "PRESSY LAKE",
    "icbc_city_code": "PSSL",
    "icbc_city_name": "PRESSY LAKE",
    "icbc_city_name_legacy": "70 MILE HOUSE",
    "vips_city_name": "PRESSY LAKE"
  },
  {
    "city_code": "PRCI",
    "city_name": "PRICE ISLAND",
    "icbc_city_code": "PRCI",
    "icbc_city_name": "PRICE ISLAND",
    "icbc_city_name_legacy": "BELLA BELLA",
    "vips_city_name": "PRICE ISLAND"
  },
  {
    "city_code": "PSLY",
    "city_name": "PRIESTLY",
    "icbc_city_code": "PSLY",
    "icbc_city_name": "PRIESTLY",
    "icbc_city_name_legacy": "PRIESTLY",
    "vips_city_name": "PRIESTLY"
  },
  {
    "city_code": "PGRG",
    "city_name": "PRINCE GEORGE",
    "icbc_city_code": "PGRG",
    "icbc_city_name": "PRINCE GEORGE",
    "icbc_city_name_legacy": "PRINCE GEORGE",
    "vips_city_name": "PRINCE GEORGE"
  },
  {
    "city_code": "PRRU",
    "city_name": "PRINCE RUPERT",
    "icbc_city_code": "PRRU",
    "icbc_city_name": "PRINCE RUPERT",
    "icbc_city_name_legacy": "PRINCE RUPERT",
    "vips_city_name": "PRINCE RUPERT"
  },
  {
    "city_code": "PROI",
    "city_name": "PRINCESS ROYAL ISLAND",
    "icbc_city_code": "PROI",
    "icbc_city_name": "PRINCESS ROYAL ISLAND",
    "icbc_city_name_legacy": "HARTLEY BAY",
    "vips_city_name": "PRINCESS ROYAL ISLAND"
  },
  {
    "city_code": "PRNT",
    "city_name": "PRINCETON",
    "icbc_city_code": "PRNT",
    "icbc_city_name": "PRINCETON",
    "icbc_city_name_legacy": "PRINCETON",
    "vips_city_name": "PRINCETON"
  },
  {
    "city_code": "PRTD",
    "city_name": "PRITCHARD",
    "icbc_city_code": "PRTD",
    "icbc_city_name": "PRITCHARD",
    "icbc_city_name_legacy": "PRITCHARD",
    "vips_city_name": "PRITCHARD"
  },
  {
    "city_code": "PRCT",
    "city_name": "PROCTER",
    "icbc_city_code": "PRCT",
    "icbc_city_name": "PROCTER",
    "icbc_city_name_legacy": "PROCTER",
    "vips_city_name": "PROCTER"
  },
  {
    "city_code": "PRGR",
    "city_name": "PROGRESS",
    "icbc_city_code": "PRGR",
    "icbc_city_name": "PROGRESS",
    "icbc_city_name_legacy": "PROGRESS",
    "vips_city_name": "PROGRESS"
  },
  {
    "city_code": "PRRV",
    "city_name": "PROPHET RIVER",
    "icbc_city_code": "PRRV",
    "icbc_city_name": "PROPHET RIVER",
    "icbc_city_name_legacy": "PROPHET RIVER",
    "vips_city_name": "PROPHET RIVER"
  },
  {
    "city_code": "PURD",
    "city_name": "PURDEN",
    "icbc_city_code": "PURD",
    "icbc_city_name": "PURDEN",
    "icbc_city_name_legacy": "PRINCE GEORGE",
    "vips_city_name": "PURDEN"
  },
  {
    "city_code": "QDIS",
    "city_name": "QUADRA ISLAND",
    "icbc_city_code": "QDIS",
    "icbc_city_name": "QUADRA ISLAND",
    "icbc_city_name_legacy": "QUADRA ISLAND",
    "vips_city_name": "QUADRA ISLAND"
  },
  {
    "city_code": "QLBH",
    "city_name": "QUALICUM BEACH",
    "icbc_city_code": "QLBH",
    "icbc_city_name": "QUALICUM BEACH",
    "icbc_city_name_legacy": "QUALICUM BEACH",
    "vips_city_name": "QUALICUM BEACH"
  },
  {
    "city_code": "QKCV",
    "city_name": "QUATHIASKI COVE",
    "icbc_city_code": "QKCV",
    "icbc_city_name": "QUATHIASKI COVE",
    "icbc_city_name_legacy": "QUATHIASKI COVE",
    "vips_city_name": "QUATHIASKI COVE"
  },
  {
    "city_code": "QTSN",
    "city_name": "QUATSINO",
    "icbc_city_code": "QTSN",
    "icbc_city_name": "QUATSINO",
    "icbc_city_name_legacy": "QUATSINO",
    "vips_city_name": "QUATSINO"
  },
  {
    "city_code": "QNBA",
    "city_name": "QUEENS BAY",
    "icbc_city_code": "QNBA",
    "icbc_city_name": "QUEENS BAY",
    "icbc_city_name_legacy": "QUEENS BAY",
    "vips_city_name": "QUEENS BAY"
  },
  {
    "city_code": "QSNL",
    "city_name": "QUESNEL",
    "icbc_city_code": "QSNL",
    "icbc_city_name": "QUESNEL",
    "icbc_city_name_legacy": "QUESNEL",
    "vips_city_name": "QUESNEL"
  },
  {
    "city_code": "QSIS",
    "city_name": "QUESNEL LAKE",
    "icbc_city_code": "QSIS",
    "icbc_city_name": "QUESNEL LAKE",
    "icbc_city_name_legacy": "WILLIAMS LAKE",
    "vips_city_name": "QUESNEL LAKE"
  },
  {
    "city_code": "QLCH",
    "city_name": "QUILCHENA",
    "icbc_city_code": "QLCH",
    "icbc_city_name": "QUILCHENA",
    "icbc_city_name_legacy": "QUILCHENA",
    "vips_city_name": "QUILCHENA"
  },
  {
    "city_code": "RADM",
    "city_name": "RADIUM HOT SPRINGS",
    "icbc_city_code": "RADM",
    "icbc_city_name": "RADIUM HOT SPRINGS",
    "icbc_city_name_legacy": "RADIUM HOT SPRI",
    "vips_city_name": "RADIUM HOT SPRINGS"
  },
  {
    "city_code": "RYIS",
    "city_name": "RAMSAY ISLAND",
    "icbc_city_code": "RYIS",
    "icbc_city_name": "RAMSAY ISLAND",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "RAMSAY ISLAND"
  },
  {
    "city_code": "RLIS",
    "city_name": "RANDALL ISLAND",
    "icbc_city_code": "RLIS",
    "icbc_city_name": "RANDALL ISLAND",
    "icbc_city_name_legacy": "PRINCE RUPERT",
    "vips_city_name": "RANDALL ISLAND"
  },
  {
    "city_code": "RBVG",
    "city_name": "RASPBERRY",
    "icbc_city_code": "RBVG",
    "icbc_city_name": "RASPBERRY",
    "icbc_city_name_legacy": "CASTLEGAR",
    "vips_city_name": "RASPBERRY"
  },
  {
    "city_code": "RDIS",
    "city_name": "READ ISLAND",
    "icbc_city_code": "RDIS",
    "icbc_city_name": "READ ISLAND",
    "icbc_city_name_legacy": "READ ISLAND",
    "vips_city_name": "READ ISLAND"
  },
  {
    "city_code": "REDL",
    "city_name": "RED LAKE",
    "icbc_city_code": "REDL",
    "icbc_city_name": "RED LAKE",
    "icbc_city_name_legacy": "RED LAKE",
    "vips_city_name": "RED LAKE"
  },
  {
    "city_code": "RROK",
    "city_name": "RED ROCK",
    "icbc_city_code": "RROK",
    "icbc_city_name": "RED ROCK",
    "icbc_city_name_legacy": "RED ROCK",
    "vips_city_name": "RED ROCK"
  },
  {
    "city_code": "REDS",
    "city_name": "REDSTONE",
    "icbc_city_code": "REDS",
    "icbc_city_name": "REDSTONE",
    "icbc_city_name_legacy": "RED STONE",
    "vips_city_name": "REDSTONE"
  },
  {
    "city_code": "RFIS",
    "city_name": "REEF ISLAND",
    "icbc_city_code": "RFIS",
    "icbc_city_name": "REEF ISLAND",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "REEF ISLAND"
  },
  {
    "city_code": "REIS",
    "city_name": "REES ISLAND",
    "icbc_city_code": "REIS",
    "icbc_city_name": "REES ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "REES ISLAND"
  },
  {
    "city_code": "RFCV",
    "city_name": "REFUGE COVE",
    "icbc_city_code": "RFCV",
    "icbc_city_name": "REFUGE COVE",
    "icbc_city_name_legacy": "REFUGE COVE",
    "vips_city_name": "REFUGE COVE"
  },
  {
    "city_code": "RIIS",
    "city_name": "REID ISLAND",
    "icbc_city_code": "RIIS",
    "icbc_city_name": "REID ISLAND",
    "icbc_city_name_legacy": "CHEMAINUS",
    "vips_city_name": "REID ISLAND"
  },
  {
    "city_code": "RILK",
    "city_name": "REID LAKE",
    "icbc_city_code": "RILK",
    "icbc_city_name": "REID LAKE",
    "icbc_city_name_legacy": "REID LAKE",
    "vips_city_name": "REID LAKE"
  },
  {
    "city_code": "RNSD",
    "city_name": "RENNELL SOUND",
    "icbc_city_code": "RNSD",
    "icbc_city_name": "RENNELL SOUND",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "RENNELL SOUND"
  },
  {
    "city_code": "RNIS",
    "city_name": "RENNISON ISLAND",
    "icbc_city_code": "RNIS",
    "icbc_city_name": "RENNISON ISLAND",
    "icbc_city_name_legacy": "HARTLEY BAY",
    "vips_city_name": "RENNISON ISLAND"
  },
  {
    "city_code": "RVST",
    "city_name": "REVELSTOKE",
    "icbc_city_code": "RVST",
    "icbc_city_name": "REVELSTOKE",
    "icbc_city_name_legacy": "REVELSTOKE",
    "vips_city_name": "REVELSTOKE"
  },
  {
    "city_code": "RCIS",
    "city_name": "RICHARDSON ISLAND",
    "icbc_city_code": "RCIS",
    "icbc_city_name": "RICHARDSON ISLAND",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "RICHARDSON ISLAND"
  },
  {
    "city_code": "RMD",
    "city_name": "RICHMOND",
    "icbc_city_code": "RMD",
    "icbc_city_name": "RICHMOND",
    "icbc_city_name_legacy": "RICHMOND",
    "vips_city_name": "RICHMOND"
  },
  {
    "city_code": "RNDL",
    "city_name": "RIONDEL",
    "icbc_city_code": "RNDL",
    "icbc_city_name": "RIONDEL",
    "icbc_city_name_legacy": "RIONDEL",
    "vips_city_name": "RIONDEL"
  },
  {
    "city_code": "RSCK",
    "city_name": "RISKE CREEK",
    "icbc_city_code": "RSCK",
    "icbc_city_name": "RISKE CREEK",
    "icbc_city_name_legacy": "RISKE CREEK",
    "vips_city_name": "RISKE CREEK"
  },
  {
    "city_code": "RCR",
    "city_name": "ROBERTS CREEK",
    "icbc_city_code": "RCR",
    "icbc_city_name": "ROBERTS CREEK",
    "icbc_city_name_legacy": "ROBERTS CREEK",
    "vips_city_name": "ROBERTS CREEK"
  },
  {
    "city_code": "RBSN",
    "city_name": "ROBSON",
    "icbc_city_code": "RBSN",
    "icbc_city_name": "ROBSON",
    "icbc_city_name_legacy": "ROBSON",
    "vips_city_name": "ROBSON"
  },
  {
    "city_code": "RCCK",
    "city_name": "ROCK CREEK",
    "icbc_city_code": "RCCK",
    "icbc_city_name": "ROCK CREEK",
    "icbc_city_name_legacy": "ROCK CREEK",
    "vips_city_name": "ROCK CREEK"
  },
  {
    "city_code": "RKIS",
    "city_name": "RODERICK ISLAND",
    "icbc_city_code": "RKIS",
    "icbc_city_name": "RODERICK ISLAND",
    "icbc_city_name_legacy": "BELLA BELLA",
    "vips_city_name": "RODERICK ISLAND"
  },
  {
    "city_code": "RELK",
    "city_name": "ROE LAKE",
    "icbc_city_code": "RELK",
    "icbc_city_name": "ROE LAKE",
    "icbc_city_name_legacy": "ROE LAKE",
    "vips_city_name": "ROE LAKE"
  },
  {
    "city_code": "RGPS",
    "city_name": "ROGERS PASS",
    "icbc_city_code": "RGPS",
    "icbc_city_name": "ROGERS PASS",
    "icbc_city_name_legacy": "ROGERS PASS",
    "vips_city_name": "ROGERS PASS"
  },
  {
    "city_code": "ROLL",
    "city_name": "ROLLA",
    "icbc_city_code": "ROLL",
    "icbc_city_name": "ROLLA",
    "icbc_city_name_legacy": "ROLLA",
    "vips_city_name": "ROLLA"
  },
  {
    "city_code": "RSVL",
    "city_name": "ROOSVILLE",
    "icbc_city_code": "RSVL",
    "icbc_city_name": "ROOSVILLE",
    "icbc_city_name_legacy": "ROOSVILLE",
    "vips_city_name": "ROOSVILLE"
  },
  {
    "city_code": "RSLK",
    "city_name": "ROSE LAKE",
    "icbc_city_code": "RSLK",
    "icbc_city_name": "ROSE LAKE",
    "icbc_city_name_legacy": "ROSE LAKE",
    "vips_city_name": "ROSE LAKE"
  },
  {
    "city_code": "RSPR",
    "city_name": "ROSE PRAIRIE",
    "icbc_city_code": "RSPR",
    "icbc_city_name": "ROSE PRAIRIE",
    "icbc_city_name_legacy": "ROSE PRAIRIE",
    "vips_city_name": "ROSE PRAIRIE"
  },
  {
    "city_code": "RSBY",
    "city_name": "ROSEBERY",
    "icbc_city_code": "RSBY",
    "icbc_city_name": "ROSEBERY",
    "icbc_city_name_legacy": "NEW DENVER",
    "vips_city_name": "ROSEBERY"
  },
  {
    "city_code": "RSLD",
    "city_name": "ROSSLAND",
    "icbc_city_code": "RSLD",
    "icbc_city_name": "ROSSLAND",
    "icbc_city_name_legacy": "ROSSLAND",
    "vips_city_name": "ROSSLAND"
  },
  {
    "city_code": "RSWD",
    "city_name": "ROSSWOOD",
    "icbc_city_code": "RSWD",
    "icbc_city_name": "ROSSWOOD",
    "icbc_city_name_legacy": "ROSSWOOD",
    "vips_city_name": "ROSSWOOD"
  },
  {
    "city_code": "ROYS",
    "city_name": "ROYSTON",
    "icbc_city_code": "ROYS",
    "icbc_city_name": "ROYSTON",
    "icbc_city_name_legacy": "ROYSTON",
    "vips_city_name": "ROYSTON"
  },
  {
    "city_code": "RUBY",
    "city_name": "RUBY LAKE",
    "icbc_city_code": "RUBY",
    "icbc_city_name": "RUBY LAKE",
    "icbc_city_name_legacy": "MADEIRA PARK",
    "vips_city_name": "RUBY LAKE"
  },
  {
    "city_code": "RXIS",
    "city_name": "RUXTON ISLAND",
    "icbc_city_code": "RXIS",
    "icbc_city_name": "RUXTON ISLAND",
    "icbc_city_name_legacy": "LADYSMITH",
    "vips_city_name": "RUXTON ISLAND"
  },
  {
    "city_code": "SNCH",
    "city_name": "SAANICH",
    "icbc_city_code": "SNCH",
    "icbc_city_name": "SAANICH",
    "icbc_city_name_legacy": "SAANICH",
    "vips_city_name": "SAANICH"
  },
  {
    "city_code": "SAIK",
    "city_name": "STONY CREEK SAIK'UZ IR",
    "icbc_city_code": "SAIK",
    "icbc_city_name": "STONY CREEK SAIK'UZ IR",
    "icbc_city_name_legacy": "STONEY CREEK",
    "vips_city_name": "STONY CREEK SAIK'UZ IR"
  },
  {
    "city_code": "SALM",
    "city_name": "SALMO",
    "icbc_city_code": "SALM",
    "icbc_city_name": "SALMO",
    "icbc_city_name_legacy": "SALMO",
    "vips_city_name": "SALMO"
  },
  {
    "city_code": "SLAM",
    "city_name": "SALMON ARM",
    "icbc_city_code": "SLAM",
    "icbc_city_name": "SALMON ARM",
    "icbc_city_name_legacy": "SALMON ARM",
    "vips_city_name": "SALMON ARM"
  },
  {
    "city_code": "SLRI",
    "city_name": "SALMON RIVER",
    "icbc_city_code": "SLRI",
    "icbc_city_name": "SALMON RIVER",
    "icbc_city_name_legacy": "SALMON RIVER",
    "vips_city_name": "SALMON RIVER"
  },
  {
    "city_code": "SRIR",
    "city_name": "SALMON RIVER IR",
    "icbc_city_code": "SRIR",
    "icbc_city_name": "SALMON RIVER IR",
    "icbc_city_name_legacy": "SAYWARD",
    "vips_city_name": "SALMON RIVER IR"
  },
  {
    "city_code": "SLVY",
    "city_name": "SALMON VALLEY",
    "icbc_city_code": "SLVY",
    "icbc_city_name": "SALMON VALLEY",
    "icbc_city_name_legacy": "SALMON VALLEY",
    "vips_city_name": "SALMON VALLEY"
  },
  {
    "city_code": "SSIS",
    "city_name": "SALT SPRING ISLAND",
    "icbc_city_code": "SSIS",
    "icbc_city_name": "SALT SPRING ISLAND",
    "icbc_city_name_legacy": "SALT SPRING ISL",
    "vips_city_name": "SALT SPRING ISLAND"
  },
  {
    "city_code": "SLTB",
    "city_name": "SALTERY BAY",
    "icbc_city_code": "SLTB",
    "icbc_city_name": "SALTERY BAY",
    "icbc_city_name_legacy": "SALTERY BAY",
    "vips_city_name": "SALTERY BAY"
  },
  {
    "city_code": "SNJF",
    "city_name": "SAN JOSEF",
    "icbc_city_code": "SNJF",
    "icbc_city_name": "SAN JOSEF",
    "icbc_city_name_legacy": "SAN JOSEF",
    "vips_city_name": "SAN JOSEF"
  },
  {
    "city_code": "SANC",
    "city_name": "SANCA",
    "icbc_city_code": "SANC",
    "icbc_city_name": "SANCA",
    "icbc_city_name_legacy": "SANCA",
    "vips_city_name": "SANCA"
  },
  {
    "city_code": "SLIS",
    "city_name": "SANDILANDS ISLAND",
    "icbc_city_code": "SLIS",
    "icbc_city_name": "SANDILANDS ISLAND",
    "icbc_city_name_legacy": "PORT HARDY",
    "vips_city_name": "SANDILANDS ISLAND"
  },
  {
    "city_code": "SNDS",
    "city_name": "SANDSPIT",
    "icbc_city_code": "SNDS",
    "icbc_city_name": "SANDSPIT",
    "icbc_city_name_legacy": "SANDSPIT",
    "vips_city_name": "SANDSPIT"
  },
  {
    "city_code": "SHIS",
    "city_name": "SARAH ISLAND",
    "icbc_city_code": "SHIS",
    "icbc_city_name": "SARAH ISLAND",
    "icbc_city_name_legacy": "BELLA BELLA",
    "vips_city_name": "SARAH ISLAND"
  },
  {
    "city_code": "SRTA",
    "city_name": "SARITA",
    "icbc_city_code": "SRTA",
    "icbc_city_name": "SARITA",
    "icbc_city_name_legacy": "SARITA",
    "vips_city_name": "SARITA"
  },
  {
    "city_code": "SNIS",
    "city_name": "SATURNA ISLAND",
    "icbc_city_code": "SNIS",
    "icbc_city_name": "SATURNA ISLAND",
    "icbc_city_name_legacy": "SATURNA ISLAND",
    "vips_city_name": "SATURNA ISLAND"
  },
  {
    "city_code": "SVIS",
    "city_name": "SAVARY ISLAND",
    "icbc_city_code": "SVIS",
    "icbc_city_name": "SAVARY ISLAND",
    "icbc_city_name_legacy": "SAVARY ISLAND",
    "vips_city_name": "SAVARY ISLAND"
  },
  {
    "city_code": "SAVN",
    "city_name": "SAVONA",
    "icbc_city_code": "SAVN",
    "icbc_city_name": "SAVONA",
    "icbc_city_name_legacy": "SAVONA",
    "vips_city_name": "SAVONA"
  },
  {
    "city_code": "SYWD",
    "city_name": "SAYWARD",
    "icbc_city_code": "SYWD",
    "icbc_city_name": "SAYWARD",
    "icbc_city_name_legacy": "SAYWARD",
    "vips_city_name": "SAYWARD"
  },
  {
    "city_code": "SCCK",
    "city_name": "SCOTCH CREEK",
    "icbc_city_code": "SCCK",
    "icbc_city_name": "SCOTCH CREEK",
    "icbc_city_name_legacy": "SCOTCH CREEK",
    "vips_city_name": "SCOTCH CREEK"
  },
  {
    "city_code": "SEC",
    "city_name": "SECHELT",
    "icbc_city_code": "SEC",
    "icbc_city_name": "SECHELT",
    "icbc_city_name_legacy": "SECHELT",
    "vips_city_name": "SECHELT"
  },
  {
    "city_code": "STNP",
    "city_name": "SETON PORTAGE",
    "icbc_city_code": "STNP",
    "icbc_city_name": "SETON PORTAGE",
    "icbc_city_name_legacy": "SETON PORTAGE",
    "vips_city_name": "SETON PORTAGE"
  },
  {
    "city_code": "SEWA",
    "city_name": "SEWALL",
    "icbc_city_code": "SEWA",
    "icbc_city_name": "SEWALL",
    "icbc_city_name_legacy": "MASSETT",
    "vips_city_name": "SEWALL"
  },
  {
    "city_code": "SWIN",
    "city_name": "SEWELL INLET",
    "icbc_city_code": "SWIN",
    "icbc_city_name": "SEWELL INLET",
    "icbc_city_name_legacy": "SEWELL INLET",
    "vips_city_name": "SEWELL INLET"
  },
  {
    "city_code": "SARM",
    "city_name": "SEYMOUR ARM",
    "icbc_city_code": "SARM",
    "icbc_city_name": "SEYMOUR ARM",
    "icbc_city_name_legacy": "SEYMOUR ARM",
    "vips_city_name": "SEYMOUR ARM"
  },
  {
    "city_code": "SYIN",
    "city_name": "SEYMOUR INLET",
    "icbc_city_code": "SYIN",
    "icbc_city_name": "SEYMOUR INLET",
    "icbc_city_name_legacy": "PORT HARDY",
    "vips_city_name": "SEYMOUR INLET"
  },
  {
    "city_code": "SHAL",
    "city_name": "SHALALTH",
    "icbc_city_code": "SHAL",
    "icbc_city_name": "SHALALTH",
    "icbc_city_name_legacy": "SHALALTH",
    "vips_city_name": "SHALALTH"
  },
  {
    "city_code": "SHLK",
    "city_name": "SHAWNIGAN LAKE",
    "icbc_city_code": "SHLK",
    "icbc_city_name": "SHAWNIGAN LAKE",
    "icbc_city_name_legacy": "SHAWNIGAN LAKE",
    "vips_city_name": "SHAWNIGAN LAKE"
  },
  {
    "city_code": "SWTR",
    "city_name": "SHEARWATER",
    "icbc_city_code": "SWTR",
    "icbc_city_name": "SHEARWATER",
    "icbc_city_name_legacy": "SHEARWATER",
    "vips_city_name": "SHEARWATER"
  },
  {
    "city_code": "SHEL",
    "city_name": "SHELLEY",
    "icbc_city_code": "SHEL",
    "icbc_city_name": "SHELLEY",
    "icbc_city_name_legacy": "SHELLEY",
    "vips_city_name": "SHELLEY"
  },
  {
    "city_code": "SHGN",
    "city_name": "SHELL-GLEN",
    "icbc_city_code": "SHGN",
    "icbc_city_name": "SHELL-GLEN",
    "icbc_city_name_legacy": "SHELLEY",
    "vips_city_name": "SHELL-GLEN"
  },
  {
    "city_code": "SRLY",
    "city_name": "SHIRLEY",
    "icbc_city_code": "SRLY",
    "icbc_city_name": "SHIRLEY",
    "icbc_city_name_legacy": "SHIRLEY",
    "vips_city_name": "SHIRLEY"
  },
  {
    "city_code": "SHAC",
    "city_name": "SHOREACRES",
    "icbc_city_code": "SHAC",
    "icbc_city_name": "SHOREACRES",
    "icbc_city_name_legacy": "SHORE ACRES",
    "vips_city_name": "SHOREACRES"
  },
  {
    "city_code": "SWIR",
    "city_name": "SHUSWAP IR",
    "icbc_city_code": "SWIR",
    "icbc_city_name": "SHUSWAP",
    "icbc_city_name_legacy": "SHUSWAP",
    "vips_city_name": "SHUSWAP"
  },
  {
    "city_code": "SHBH",
    "city_name": "SHUTTY BENCH",
    "icbc_city_code": "SHBH",
    "icbc_city_name": "SHUTTY BENCH",
    "icbc_city_name_legacy": "KASLO",
    "vips_city_name": "SHUTTY BENCH"
  },
  {
    "city_code": "SCMS",
    "city_name": "SICAMOUS",
    "icbc_city_code": "SCMS",
    "icbc_city_name": "SICAMOUS",
    "icbc_city_name_legacy": "SICAMOUS",
    "vips_city_name": "SICAMOUS"
  },
  {
    "city_code": "SDNY",
    "city_name": "SIDNEY",
    "icbc_city_code": "SDNY",
    "icbc_city_name": "SIDNEY",
    "icbc_city_name_legacy": "SIDNEY",
    "vips_city_name": "SIDNEY"
  },
  {
    "city_code": "SDIS",
    "city_name": "SIDNEY ISLAND",
    "icbc_city_code": "SDIS",
    "icbc_city_name": "SIDNEY ISLAND",
    "icbc_city_name_legacy": "SIDNEY",
    "vips_city_name": "SIDNEY ISLAND"
  },
  {
    "city_code": "SKNI",
    "city_name": "SIKANNI",
    "icbc_city_code": "SKNI",
    "icbc_city_name": "SIKANNI",
    "icbc_city_name_legacy": "FORT ST JOHN",
    "vips_city_name": "SIKANNI"
  },
  {
    "city_code": "GLNV",
    "city_name": "GLEN VOWELL",
    "icbc_city_code": "GLNV",
    "icbc_city_name": "GLEN VOWELL",
    "icbc_city_name_legacy": "GLEN VOWELL",
    "vips_city_name": "GLEN VOWELL"
  },
  {
    "city_code": "SLTN",
    "city_name": "SILVERTON",
    "icbc_city_code": "SLTN",
    "icbc_city_name": "SILVERTON",
    "icbc_city_name_legacy": "SILVERTON",
    "vips_city_name": "SILVERTON"
  },
  {
    "city_code": "SNML",
    "city_name": "SINCLAIR MILLS",
    "icbc_city_code": "SNML",
    "icbc_city_name": "SINCLAIR MILLS",
    "icbc_city_name_legacy": "SINCLAIR MILLS",
    "vips_city_name": "SINCLAIR MILLS"
  },
  {
    "city_code": "SRDR",
    "city_name": "SIRDAR",
    "icbc_city_code": "SRDR",
    "icbc_city_name": "SIRDAR",
    "icbc_city_name_legacy": "SIRDAR",
    "vips_city_name": "SIRDAR"
  },
  {
    "city_code": "SKNA",
    "city_name": "SKEENA",
    "icbc_city_code": "SKNA",
    "icbc_city_name": "SKEENA",
    "icbc_city_name_legacy": "AIYANSH",
    "vips_city_name": "SKEENA"
  },
  {
    "city_code": "SKIR",
    "city_name": "SKEETCHESTN IR",
    "icbc_city_code": "SKIR",
    "icbc_city_name": "SKEETCHESTN IR",
    "icbc_city_name_legacy": "ASHCROFT",
    "vips_city_name": "SKEETCHESTN IR"
  },
  {
    "city_code": "SKDG",
    "city_name": "SKIDEGATE",
    "icbc_city_code": "SKDG",
    "icbc_city_name": "SKIDEGATE",
    "icbc_city_name_legacy": "SKIDEGATE",
    "vips_city_name": "SKIDEGATE"
  },
  {
    "city_code": "SKMK",
    "city_name": "SKOOKUMCHUCK",
    "icbc_city_code": "SKMK",
    "icbc_city_name": "SKOOKUMCHUCK",
    "icbc_city_name_legacy": "SKOOKUMCHUCK",
    "vips_city_name": "SKOOKUMCHUCK"
  },
  {
    "city_code": "SLCN",
    "city_name": "SLOCAN",
    "icbc_city_code": "SLCN",
    "icbc_city_name": "SLOCAN",
    "icbc_city_name_legacy": "SLOCAN",
    "vips_city_name": "SLOCAN"
  },
  {
    "city_code": "SNPK",
    "city_name": "SLOCAN PARK",
    "icbc_city_code": "SNPK",
    "icbc_city_name": "SLOCAN PARK",
    "icbc_city_name_legacy": "SLOCAN PARK",
    "vips_city_name": "SLOCAN PARK"
  },
  {
    "city_code": "SMIS",
    "city_name": "SMITH ISLAND",
    "icbc_city_code": "SMIS",
    "icbc_city_name": "SMITH ISLAND",
    "icbc_city_name_legacy": "PRINCE RUPERT",
    "vips_city_name": "SMITH ISLAND"
  },
  {
    "city_code": "SMTS",
    "city_name": "SMITHERS",
    "icbc_city_code": "SMTS",
    "icbc_city_name": "SMITHERS",
    "icbc_city_name_legacy": "SMITHERS",
    "vips_city_name": "SMITHERS"
  },
  {
    "city_code": "SNYD",
    "city_name": "SNYDER",
    "icbc_city_code": "SNYD",
    "icbc_city_name": "SNYDER",
    "icbc_city_name_legacy": "BUICK",
    "vips_city_name": "SNYDER"
  },
  {
    "city_code": "SMSP",
    "city_name": "SOAMES POINT",
    "icbc_city_code": "SMSP",
    "icbc_city_name": "SOAMES POINT",
    "icbc_city_name_legacy": "GIBSONS",
    "vips_city_name": "SOAMES POINT"
  },
  {
    "city_code": "SDCK",
    "city_name": "SODA CREEK",
    "icbc_city_code": "SDCK",
    "icbc_city_name": "SODA CREEK",
    "icbc_city_name_legacy": "SODA CREEK",
    "vips_city_name": "SODA CREEK"
  },
  {
    "city_code": "SNTL",
    "city_name": "SOINTULA",
    "icbc_city_code": "SNTL",
    "icbc_city_name": "SOINTULA",
    "icbc_city_name_legacy": "SOINTULA",
    "vips_city_name": "SOINTULA"
  },
  {
    "city_code": "SLQA",
    "city_name": "SOLSQUA",
    "icbc_city_code": "SLQA",
    "icbc_city_name": "SOLSQUA",
    "icbc_city_name_legacy": "SOLSQUA",
    "vips_city_name": "SOLSQUA"
  },
  {
    "city_code": "SMVI",
    "city_name": "SOMERVILLE ISLAND",
    "icbc_city_code": "SMVI",
    "icbc_city_name": "SOMERVILLE ISLAND",
    "icbc_city_name_legacy": "KINCOLITH",
    "vips_city_name": "SOMERVILLE ISLAND"
  },
  {
    "city_code": "SOIS",
    "city_name": "SONORA ISLAND",
    "icbc_city_code": "SOIS",
    "icbc_city_name": "SONORA ISLAND",
    "icbc_city_name_legacy": "SONORA ISLAND",
    "vips_city_name": "SONORA ISLAND"
  },
  {
    "city_code": "SOKE",
    "city_name": "SOOKE",
    "icbc_city_code": "SOKE",
    "icbc_city_name": "SOOKE",
    "icbc_city_name_legacy": "SOOKE",
    "vips_city_name": "SOOKE"
  },
  {
    "city_code": "SRNT",
    "city_name": "SORRENTO",
    "icbc_city_code": "SRNT",
    "icbc_city_name": "SORRENTO",
    "icbc_city_name_legacy": "SORRENTO",
    "vips_city_name": "SORRENTO"
  },
  {
    "city_code": "SDAW",
    "city_name": "SOUTH DAWSON",
    "icbc_city_code": "SDAW",
    "icbc_city_name": "SOUTH DAWSON",
    "icbc_city_name_legacy": "DAWSON CREEK",
    "vips_city_name": "SOUTH DAWSON"
  },
  {
    "city_code": "SHAZ",
    "city_name": "SOUTH HAZELTON",
    "icbc_city_code": "SHAZ",
    "icbc_city_name": "SOUTH HAZELTON",
    "icbc_city_name_legacy": "SOUTH HAZELTON",
    "vips_city_name": "SOUTH HAZELTON"
  },
  {
    "city_code": "SKLK",
    "city_name": "SOUTH KINBASKET LAKE",
    "icbc_city_code": "SKLK",
    "icbc_city_name": "SOUTH KINBASKET LAKE",
    "icbc_city_name_legacy": "REVELSTOKE",
    "vips_city_name": "SOUTH KINBASKET LAKE"
  },
  {
    "city_code": "SPIS",
    "city_name": "SOUTH PENDER ISLAND",
    "icbc_city_code": "SPIS",
    "icbc_city_name": "SOUTH PENDER ISLAND",
    "icbc_city_name_legacy": "PENDER ISLAND",
    "vips_city_name": "SOUTH PENDER ISLAND"
  },
  {
    "city_code": "SSLC",
    "city_name": "SOUTH SLOCAN",
    "icbc_city_code": "SSLC",
    "icbc_city_name": "SOUTH SLOCAN",
    "icbc_city_name_legacy": "SOUTH SLOCAN",
    "vips_city_name": "SOUTH SLOCAN"
  },
  {
    "city_code": "SSPK",
    "city_name": "SOUTH STRATHCONA PARK",
    "icbc_city_code": "SSPK",
    "icbc_city_name": "SOUTH STRATHCONA PARK",
    "icbc_city_name_legacy": "GOLD RIVER",
    "vips_city_name": "SOUTH STRATHCONA PARK"
  },
  {
    "city_code": "STAY",
    "city_name": "SOUTH TAYLOR",
    "icbc_city_code": "STAY",
    "icbc_city_name": "SOUTH TAYLOR",
    "icbc_city_name_legacy": "FORT ST JOHN",
    "vips_city_name": "SOUTH TAYLOR"
  },
  {
    "city_code": "SBNK",
    "city_name": "SOUTHBANK",
    "icbc_city_code": "SBNK",
    "icbc_city_name": "SOUTHBANK",
    "icbc_city_name_legacy": "SOUTHBANK",
    "vips_city_name": "SOUTHBANK"
  },
  {
    "city_code": "SPAL",
    "city_name": "SPALLUMCHEEN",
    "icbc_city_code": "SPAL",
    "icbc_city_name": "SPALLUMCHEEN",
    "icbc_city_name_legacy": "SPALLUMCHEEN",
    "vips_city_name": "SPALLUMCHEEN"
  },
  {
    "city_code": "SPWD",
    "city_name": "SPARWOOD",
    "icbc_city_code": "SPWD",
    "icbc_city_name": "SPARWOOD",
    "icbc_city_name_legacy": "SPARWOOD",
    "vips_city_name": "SPARWOOD"
  },
  {
    "city_code": "SPTZ",
    "city_name": "SPATSIZI",
    "icbc_city_code": "SPTZ",
    "icbc_city_name": "SPATSIZI",
    "icbc_city_name_legacy": "TELEGRAPH CREEK",
    "vips_city_name": "SPATSIZI"
  },
  {
    "city_code": "SPAT",
    "city_name": "SPATSUM",
    "icbc_city_code": "SPAT",
    "icbc_city_name": "SPATSUM",
    "icbc_city_name_legacy": "SPATSUM",
    "vips_city_name": "SPATSUM"
  },
  {
    "city_code": "SPSB",
    "city_name": "SPENCES BRIDGE",
    "icbc_city_code": "SPSB",
    "icbc_city_name": "SPENCES BRIDGE",
    "icbc_city_name_legacy": "SPENCES BRIDGE",
    "vips_city_name": "SPENCES BRIDGE"
  },
  {
    "city_code": "SPIC",
    "city_name": "SPICER ISLAND",
    "icbc_city_code": "SPIC",
    "icbc_city_name": "SPICER ISLAND",
    "icbc_city_name_legacy": "KITKATLA",
    "vips_city_name": "SPICER ISLAND"
  },
  {
    "city_code": "SLMN",
    "city_name": "SPILLIMACHEEN",
    "icbc_city_code": "SLMN",
    "icbc_city_name": "SPILLIMACHEEN",
    "icbc_city_name_legacy": "SPILLIMACHEEN",
    "vips_city_name": "SPILLIMACHEEN"
  },
  {
    "city_code": "SPLK",
    "city_name": "SPOKIN LAKE",
    "icbc_city_code": "SPLK",
    "icbc_city_name": "SPOKIN LAKE",
    "icbc_city_name_legacy": "WILLIAMS LAKE",
    "vips_city_name": "SPOKIN LAKE"
  },
  {
    "city_code": "SPHS",
    "city_name": "SPRINGHOUSE",
    "icbc_city_code": "SPHS",
    "icbc_city_name": "SPRINGHOUSE",
    "icbc_city_name_legacy": "WILLIAMS LAKE",
    "vips_city_name": "SPRINGHOUSE"
  },
  {
    "city_code": "SPZM",
    "city_name": "SPUZZUM",
    "icbc_city_code": "SPZM",
    "icbc_city_name": "SPUZZUM",
    "icbc_city_name_legacy": "SPUZZUM",
    "vips_city_name": "SPUZZUM"
  },
  {
    "city_code": "SQUA",
    "city_name": "SQUAMISH",
    "icbc_city_code": "SQUA",
    "icbc_city_name": "SQUAMISH",
    "icbc_city_name_legacy": "SQUAMISH",
    "vips_city_name": "SQUAMISH"
  },
  {
    "city_code": "STIV",
    "city_name": "ST. IVES",
    "icbc_city_code": "STIV",
    "icbc_city_name": "ST IVES",
    "icbc_city_name_legacy": "ST IVES",
    "vips_city_name": "ST IVES"
  },
  {
    "city_code": "SCIS",
    "city_name": "STACKHOUSE ISLAND",
    "icbc_city_code": "SCIS",
    "icbc_city_name": "STACKHOUSE ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "STACKHOUSE ISLAND"
  },
  {
    "city_code": "STEM",
    "city_name": "STEIN MOUNTAIN",
    "icbc_city_code": "STEM",
    "icbc_city_name": "STEIN MOUNTAIN",
    "icbc_city_name_legacy": "LYTTON",
    "vips_city_name": "STEIN MOUNTAIN"
  },
  {
    "city_code": "STEL",
    "city_name": "STELLAKO",
    "icbc_city_code": "STEL",
    "icbc_city_name": "STELLAKO",
    "icbc_city_name_legacy": "FRASER LAKE",
    "vips_city_name": "STELLAKO"
  },
  {
    "city_code": "STPI",
    "city_name": "STEPHENS ISLAND",
    "icbc_city_code": "STPI",
    "icbc_city_name": "STEPHENS ISLAND",
    "icbc_city_name_legacy": "PRINCE RUPERT",
    "vips_city_name": "STEPHENS ISLAND"
  },
  {
    "city_code": "STEW",
    "city_name": "STEWART",
    "icbc_city_code": "STEW",
    "icbc_city_name": "STEWART",
    "icbc_city_name_legacy": "STEWART",
    "vips_city_name": "STEWART"
  },
  {
    "city_code": "STIK",
    "city_name": "STIKINE",
    "icbc_city_code": "STIK",
    "icbc_city_name": "STIKINE",
    "icbc_city_name_legacy": "STEWART",
    "vips_city_name": "STIKINE"
  },
  {
    "city_code": "STIR",
    "city_name": "STONE IR 1A",
    "icbc_city_code": "STIR",
    "icbc_city_name": "STONE IR 1A",
    "icbc_city_name_legacy": "ALEXIS CREEK",
    "vips_city_name": "STONE IR 1A"
  },
  {
    "city_code": "SMTP",
    "city_name": "STONE MOUNTAIN PARK",
    "icbc_city_code": "SMTP",
    "icbc_city_name": "STONE MOUNTAIN PARK",
    "icbc_city_name_legacy": "FORT NELSON",
    "vips_city_name": "STONE MOUNTAIN PARK"
  },
  {
    "city_code": "STON",
    "city_name": "STONER",
    "icbc_city_code": "STON",
    "icbc_city_name": "STONER",
    "icbc_city_name_legacy": "STONER",
    "vips_city_name": "STONER"
  },
  {
    "city_code": "STRI",
    "city_name": "STRANGE ISLAND",
    "icbc_city_code": "STRI",
    "icbc_city_name": "STRANGE ISLAND",
    "icbc_city_name_legacy": "GOLD RIVER",
    "vips_city_name": "STRANGE ISLAND"
  },
  {
    "city_code": "STPK",
    "city_name": "STRATHCONA PARK",
    "icbc_city_code": "STPK",
    "icbc_city_name": "STRATHCONA PARK",
    "icbc_city_name_legacy": "GOLD RIVER",
    "vips_city_name": "STRATHCONA PARK"
  },
  {
    "city_code": "STRA",
    "city_name": "STRATHNAVER",
    "icbc_city_code": "STRA",
    "icbc_city_name": "STRATHNAVER",
    "icbc_city_name_legacy": "STRATHNAVER",
    "vips_city_name": "STRATHNAVER"
  },
  {
    "city_code": "SUIS",
    "city_name": "STUART ISLAND",
    "icbc_city_code": "SUIS",
    "icbc_city_name": "STUART ISLAND",
    "icbc_city_name_legacy": "STUART ISLAND",
    "vips_city_name": "STUART ISLAND"
  },
  {
    "city_code": "STUI",
    "city_name": "STUIE",
    "icbc_city_code": "STUI",
    "icbc_city_name": "STUIE",
    "icbc_city_name_legacy": "BELLA COOLA",
    "vips_city_name": "STUIE"
  },
  {
    "city_code": "STUL",
    "city_name": "STUMP LAKE",
    "icbc_city_code": "STUL",
    "icbc_city_name": "STUMP LAKE",
    "icbc_city_name_legacy": "STUMP LAKE",
    "vips_city_name": "STUMP LAKE"
  },
  {
    "city_code": "SUVY",
    "city_name": "SUKUNKA VALLEY",
    "icbc_city_code": "SUVY",
    "icbc_city_name": "SUKUNKA VALLEY",
    "icbc_city_name_legacy": "CHETWYND",
    "vips_city_name": "SUKUNKA VALLEY"
  },
  {
    "city_code": "SLBY",
    "city_name": "SULLIVAN BAY",
    "icbc_city_code": "SLBY",
    "icbc_city_name": "SULLIVAN BAY",
    "icbc_city_name_legacy": "SULLIVAN BAY",
    "vips_city_name": "SULLIVAN BAY"
  },
  {
    "city_code": "SMLD",
    "city_name": "SUMMERLAND",
    "icbc_city_code": "SMLD",
    "icbc_city_name": "SUMMERLAND",
    "icbc_city_name_legacy": "SUMMERLAND",
    "vips_city_name": "SUMMERLAND"
  },
  {
    "city_code": "SULK",
    "city_name": "SUMMIT LAKE",
    "icbc_city_code": "SULK",
    "icbc_city_name": "SUMMIT LAKE",
    "icbc_city_name_legacy": "SUMMIT LAKE",
    "vips_city_name": "SUMMIT LAKE"
  },
  {
    "city_code": "SUPK",
    "city_name": "SUN PEAKS",
    "icbc_city_code": "SUPK",
    "icbc_city_name": "SUN PEAKS",
    "icbc_city_name_legacy": "SUN PEAKS",
    "vips_city_name": "SUN PEAKS"
  },
  {
    "city_code": "SUNL",
    "city_name": "SUNDANCE LAKES",
    "icbc_city_code": "SUNL",
    "icbc_city_name": "SUNDANCE LAKES",
    "icbc_city_name_legacy": "CHETWYND",
    "vips_city_name": "SUNDANCE LAKES"
  },
  {
    "city_code": "SRVY",
    "city_name": "SUNRISE VALLEY",
    "icbc_city_code": "SRVY",
    "icbc_city_name": "SUNRISE VALLEY",
    "icbc_city_name_legacy": "SUNRISE VALLEY",
    "vips_city_name": "SUNRISE VALLEY"
  },
  {
    "city_code": "SSPR",
    "city_name": "SUNSET PRAIRIE",
    "icbc_city_code": "SSPR",
    "icbc_city_name": "SUNSET PRAIRIE",
    "icbc_city_name_legacy": "SUNSET PRAIRIE",
    "vips_city_name": "SUNSET PRAIRIE"
  },
  {
    "city_code": "SHVL",
    "city_name": "SUNSHINE VALLEY",
    "icbc_city_code": "SHVL",
    "icbc_city_name": "SUNSHINE VALLEY",
    "icbc_city_name_legacy": "HOPE",
    "vips_city_name": "SUNSHINE VALLEY"
  },
  {
    "city_code": "SRY",
    "city_name": "SURREY",
    "icbc_city_code": "SRY",
    "icbc_city_name": "SURREY",
    "icbc_city_name_legacy": "SURREY",
    "vips_city_name": "SURREY"
  },
  {
    "city_code": "SUSI",
    "city_name": "SUSAN ISLAND",
    "icbc_city_code": "SUSI",
    "icbc_city_name": "SUSAN ISLAND",
    "icbc_city_name_legacy": "BELLA BELLA",
    "vips_city_name": "SUSAN ISLAND"
  },
  {
    "city_code": "SUSK",
    "city_name": "SUSKWA",
    "icbc_city_code": "SUSK",
    "icbc_city_name": "SUSKWA",
    "icbc_city_name_legacy": "NEW HAZELTON",
    "vips_city_name": "SUSKWA"
  },
  {
    "city_code": "SWIS",
    "city_name": "SWANSON ISLAND",
    "icbc_city_code": "SWIS",
    "icbc_city_name": "SWANSON ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "SWANSON ISLAND"
  },
  {
    "city_code": "SWRV",
    "city_name": "SWIFT RIVER",
    "icbc_city_code": "SWRV",
    "icbc_city_name": "SWIFT RIVER",
    "icbc_city_name_legacy": "SWIFT RIVER",
    "vips_city_name": "SWIFT RIVER"
  },
  {
    "city_code": "SEIS",
    "city_name": "SWINDLE ISLAND",
    "icbc_city_code": "SEIS",
    "icbc_city_name": "SWINDLE ISLAND",
    "icbc_city_name_legacy": "BELLA BELLA",
    "vips_city_name": "SWINDLE ISLAND"
  },
  {
    "city_code": "TTCK",
    "city_name": "TA TA CREEK",
    "icbc_city_code": "TTCK",
    "icbc_city_name": "TA TA CREEK",
    "icbc_city_name_legacy": "TA TA CREEK",
    "vips_city_name": "TA TA CREEK"
  },
  {
    "city_code": "TACH",
    "city_name": "TACHIE",
    "icbc_city_code": "TACH",
    "icbc_city_name": "TACHIE",
    "icbc_city_name_legacy": "GRANISLE",
    "vips_city_name": "TACHIE"
  },
  {
    "city_code": "TGHM",
    "city_name": "TAGHUM",
    "icbc_city_code": "TGHM",
    "icbc_city_name": "TAGHUM",
    "icbc_city_name_legacy": "TAGHUM",
    "vips_city_name": "TAGHUM"
  },
  {
    "city_code": "THAT",
    "city_name": "TAHLTAN",
    "icbc_city_code": "THAT",
    "icbc_city_name": "TAHLTAN",
    "icbc_city_name_legacy": "TELEGRAPH CREEK",
    "vips_city_name": "TAHLTAN"
  },
  {
    "city_code": "THSS",
    "city_name": "TAHSIS",
    "icbc_city_code": "THSS",
    "icbc_city_name": "TAHSIS",
    "icbc_city_name_legacy": "TAHSIS",
    "vips_city_name": "TAHSIS"
  },
  {
    "city_code": "THRV",
    "city_name": "TAHSISH RIVER",
    "icbc_city_code": "THRV",
    "icbc_city_name": "TAHSISH RIVER",
    "icbc_city_name_legacy": "PORT ALICE",
    "vips_city_name": "TAHSISH RIVER"
  },
  {
    "city_code": "TKLK",
    "city_name": "TAKLA LANDING",
    "icbc_city_code": "TKLK",
    "icbc_city_name": "TAKLA LANDING",
    "icbc_city_name_legacy": "TAKLA LANDING",
    "vips_city_name": "TAKLA LANDING"
  },
  {
    "city_code": "TAKU",
    "city_name": "TAKU",
    "icbc_city_code": "TAKU",
    "icbc_city_name": "TAKU",
    "icbc_city_name_legacy": "ATLIN",
    "vips_city_name": "TAKU"
  },
  {
    "city_code": "TYLK",
    "city_name": "TAKYSIE LAKE",
    "icbc_city_code": "TYLK",
    "icbc_city_name": "TAKYSIE LAKE",
    "icbc_city_name_legacy": "TAKYSIE LAKE",
    "vips_city_name": "TAKYSIE LAKE"
  },
  {
    "city_code": "TKIS",
    "city_name": "TALUNKWAN ISLAND",
    "icbc_city_code": "TKIS",
    "icbc_city_name": "TALUNKWAN ISLAND",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "TALUNKWAN ISLAND"
  },
  {
    "city_code": "TNIS",
    "city_name": "TANU ISLAND",
    "icbc_city_code": "TNIS",
    "icbc_city_name": "TANU ISLAND",
    "icbc_city_name_legacy": "DAAJING GIIDS",
    "vips_city_name": "TANU ISLAND"
  },
  {
    "city_code": "TAPP",
    "city_name": "TAPPEN",
    "icbc_city_code": "TAPP",
    "icbc_city_name": "TAPPEN",
    "icbc_city_name_legacy": "TAPPEN",
    "vips_city_name": "TAPPEN"
  },
  {
    "city_code": "TRRS",
    "city_name": "TARRYS",
    "icbc_city_code": "TRRS",
    "icbc_city_name": "TARRYS",
    "icbc_city_name_legacy": "TARRYS",
    "vips_city_name": "TARRYS"
  },
  {
    "city_code": "TATA",
    "city_name": "TATALROSE",
    "icbc_city_code": "TATA",
    "icbc_city_name": "TATALROSE",
    "icbc_city_name_legacy": "TATAL ROSE",
    "vips_city_name": "TATALROSE"
  },
  {
    "city_code": "TLLK",
    "city_name": "TATLA LAKE",
    "icbc_city_code": "TLLK",
    "icbc_city_name": "TATLA LAKE",
    "icbc_city_name_legacy": "TATLA LAKE",
    "vips_city_name": "TATLA LAKE"
  },
  {
    "city_code": "TTLK",
    "city_name": "TATLATUI LAKE",
    "icbc_city_code": "TTLK",
    "icbc_city_name": "TATLATUI LAKE",
    "icbc_city_name_legacy": "NEW HAZELTON",
    "vips_city_name": "TATLATUI LAKE"
  },
  {
    "city_code": "TYKL",
    "city_name": "TATLAYOKO LAKE",
    "icbc_city_code": "TYKL",
    "icbc_city_name": "TATLAYOKO LAKE",
    "icbc_city_name_legacy": "TATLAYOKO LAKE",
    "vips_city_name": "TATLAYOKO LAKE"
  },
  {
    "city_code": "TATS",
    "city_name": "TATSHENSHINI",
    "icbc_city_code": "TATS",
    "icbc_city_name": "TATSHENSHINI",
    "icbc_city_name_legacy": "ATLIN",
    "vips_city_name": "TATSHENSHINI"
  },
  {
    "city_code": "TAYL",
    "city_name": "TAYLOR",
    "icbc_city_code": "TAYL",
    "icbc_city_name": "TAYLOR",
    "icbc_city_name_legacy": "TAYLOR",
    "vips_city_name": "TAYLOR"
  },
  {
    "city_code": "TCLK",
    "city_name": "TCHESINKUT LAKE",
    "icbc_city_code": "TCLK",
    "icbc_city_name": "TCHESINKUT LAKE",
    "icbc_city_name_legacy": "BURNS LAKE",
    "vips_city_name": "TCHESINKUT LAKE"
  },
  {
    "city_code": "TECV",
    "city_name": "TELEGRAPH COVE",
    "icbc_city_code": "TECV",
    "icbc_city_name": "TELEGRAPH COVE",
    "icbc_city_name_legacy": "TELEGRAPH COVE",
    "vips_city_name": "TELEGRAPH COVE"
  },
  {
    "city_code": "TECK",
    "city_name": "TELEGRAPH CREEK",
    "icbc_city_code": "TECK",
    "icbc_city_name": "TELEGRAPH CREEK",
    "icbc_city_name_legacy": "TELEGRAPH CREEK",
    "vips_city_name": "TELEGRAPH CREEK"
  },
  {
    "city_code": "TLWA",
    "city_name": "TELKWA",
    "icbc_city_code": "TLWA",
    "icbc_city_name": "TELKWA",
    "icbc_city_name_legacy": "TELKWA",
    "vips_city_name": "TELKWA"
  },
  {
    "city_code": "TERR",
    "city_name": "TERRACE",
    "icbc_city_code": "TERR",
    "icbc_city_name": "TERRACE",
    "icbc_city_name_legacy": "TERRACE",
    "vips_city_name": "TERRACE"
  },
  {
    "city_code": "TJCH",
    "city_name": "TETE JAUNE",
    "icbc_city_code": "TJCH",
    "icbc_city_name": "TETE JAUNE CACHE",
    "icbc_city_name_legacy": "TETE JAUNE CACH",
    "vips_city_name": "TETE JAUNE CACHE"
  },
  {
    "city_code": "TTRV",
    "city_name": "TETSA RIVER",
    "icbc_city_code": "TTRV",
    "icbc_city_name": "TETSA RIVER",
    "icbc_city_name_legacy": "FORT NELSON",
    "vips_city_name": "TETSA RIVER"
  },
  {
    "city_code": "TXIS",
    "city_name": "TEXADA ISLAND",
    "icbc_city_code": "TXIS",
    "icbc_city_name": "TEXADA ISLAND",
    "icbc_city_name_legacy": "TEXADA ISLAND",
    "vips_city_name": "TEXADA ISLAND"
  },
  {
    "city_code": "TSIS",
    "city_name": "THETIS ISLAND",
    "icbc_city_code": "TSIS",
    "icbc_city_name": "THETIS ISLAND",
    "icbc_city_name_legacy": "THETIS ISLAND",
    "vips_city_name": "THETIS ISLAND"
  },
  {
    "city_code": "THNH",
    "city_name": "THORNHILL",
    "icbc_city_code": "THNH",
    "icbc_city_name": "THORNHILL",
    "icbc_city_name_legacy": "THORNHILL",
    "vips_city_name": "THORNHILL"
  },
  {
    "city_code": "THVY",
    "city_name": "THREE VALLEY",
    "icbc_city_code": "THVY",
    "icbc_city_name": "THREE VALLEY",
    "icbc_city_name_legacy": "THREE VALLEY",
    "vips_city_name": "THREE VALLEY"
  },
  {
    "city_code": "THUM",
    "city_name": "THRUMS",
    "icbc_city_code": "THUM",
    "icbc_city_name": "THRUMS",
    "icbc_city_name_legacy": "THRUMS",
    "vips_city_name": "THRUMS"
  },
  {
    "city_code": "THIS",
    "city_name": "THURLOW ISLANDS",
    "icbc_city_code": "THIS",
    "icbc_city_name": "THURLOW ISLANDS",
    "icbc_city_name_legacy": "SAYWARD",
    "vips_city_name": "THURLOW ISLANDS"
  },
  {
    "city_code": "TNTG",
    "city_name": "TINTAGEL",
    "icbc_city_code": "TNTG",
    "icbc_city_name": "TINTAGEL",
    "icbc_city_name_legacy": "TINTAGEL",
    "vips_city_name": "TINTAGEL"
  },
  {
    "city_code": "TLEL",
    "city_name": "TLELL",
    "icbc_city_code": "TLEL",
    "icbc_city_name": "TLELL",
    "icbc_city_name_legacy": "TLELL",
    "vips_city_name": "TLELL"
  },
  {
    "city_code": "TDRV",
    "city_name": "TOAD RIVER",
    "icbc_city_code": "TDRV",
    "icbc_city_name": "TOAD RIVER",
    "icbc_city_name_legacy": "TOAD RIVER",
    "vips_city_name": "TOAD RIVER"
  },
  {
    "city_code": "TOBA",
    "city_name": "TOBA INLET",
    "icbc_city_code": "TOBA",
    "icbc_city_name": "TOBA INLET",
    "icbc_city_name_legacy": "TOBA INLET",
    "vips_city_name": "TOBA INLET"
  },
  {
    "city_code": "TOBI",
    "city_name": "TOBIANO",
    "icbc_city_code": "TOBI",
    "icbc_city_name": "TOBIANO",
    "icbc_city_name_legacy": "TOBIANO/KAMLOOP",
    "vips_city_name": "TOBIANO"
  },
  {
    "city_code": "TFNO",
    "city_name": "TOFINO",
    "icbc_city_code": "TFNO",
    "icbc_city_name": "TOFINO",
    "icbc_city_name_legacy": "TOFINO",
    "vips_city_name": "TOFINO"
  },
  {
    "city_code": "TOLK",
    "city_name": "TOMSLAKE",
    "icbc_city_code": "TOLK",
    "icbc_city_name": "TOMSLAKE",
    "icbc_city_name_legacy": "TOMS LAKE",
    "vips_city_name": "TOMSLAKE"
  },
  {
    "city_code": "TOPL",
    "city_name": "TOPLEY",
    "icbc_city_code": "TOPL",
    "icbc_city_name": "TOPLEY",
    "icbc_city_name_legacy": "TOPLEY",
    "vips_city_name": "TOPLEY"
  },
  {
    "city_code": "TOLG",
    "city_name": "TOPLEY LANDING",
    "icbc_city_code": "TOLG",
    "icbc_city_name": "TOPLEY LANDING",
    "icbc_city_name_legacy": "GRANISLE",
    "vips_city_name": "TOPLEY LANDING"
  },
  {
    "city_code": "TRIS",
    "city_name": "TRACEY ISLAND",
    "icbc_city_code": "TRIS",
    "icbc_city_name": "TRACEY ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "TRACEY ISLAND"
  },
  {
    "city_code": "TRAL",
    "city_name": "TRAIL",
    "icbc_city_code": "TRAL",
    "icbc_city_name": "TRAIL",
    "icbc_city_name_legacy": "TRAIL",
    "vips_city_name": "TRAIL"
  },
  {
    "city_code": "TRAP",
    "city_name": "TRAPP LAKE",
    "icbc_city_code": "TRAP",
    "icbc_city_name": "TRAPP LAKE",
    "icbc_city_name_legacy": "TRAPP LAKE",
    "vips_city_name": "TRAPP LAKE"
  },
  {
    "city_code": "TRLK",
    "city_name": "TROUT LAKE",
    "icbc_city_code": "TRLK",
    "icbc_city_name": "TROUT LAKE",
    "icbc_city_name_legacy": "TROUT LAKE",
    "vips_city_name": "TROUT LAKE"
  },
  {
    "city_code": "TRUT",
    "city_name": "TRUTCH",
    "icbc_city_code": "TRUT",
    "icbc_city_name": "TRUTCH",
    "icbc_city_name_legacy": "TRUTCH",
    "vips_city_name": "TRUTCH"
  },
  {
    "city_code": "TCIS",
    "city_name": "TRUTCH ISLAND",
    "icbc_city_code": "TCIS",
    "icbc_city_name": "TRUTCH ISLAND",
    "icbc_city_name_legacy": "HARTLEY BAY",
    "vips_city_name": "TRUTCH ISLAND"
  },
  {
    "city_code": "TSAY",
    "city_name": "TSAY KEH DENE",
    "icbc_city_code": "TSAY",
    "icbc_city_name": "TSAY KEH DENE",
    "icbc_city_name_legacy": "TSAY KEH DENE",
    "vips_city_name": "TSAY KEH DENE"
  },
  {
    "city_code": "TIIR",
    "city_name": "TUGWELL ISLAND IR",
    "icbc_city_code": "TIIR",
    "icbc_city_name": "TUGWELL ISLAND IR",
    "icbc_city_name_legacy": "PRINCE RUPERT",
    "vips_city_name": "TUGWELL ISLAND IR"
  },
  {
    "city_code": "TLMN",
    "city_name": "TULAMEEN",
    "icbc_city_code": "TLMN",
    "icbc_city_name": "TULAMEEN",
    "icbc_city_name_legacy": "TULAMEEN",
    "vips_city_name": "TULAMEEN"
  },
  {
    "city_code": "TMRG",
    "city_name": "TUMBLER RIDGE",
    "icbc_city_code": "TMRG",
    "icbc_city_name": "TUMBLER RIDGE",
    "icbc_city_name_legacy": "TUMBLER RIDGE",
    "vips_city_name": "TUMBLER RIDGE"
  },
  {
    "city_code": "TUNK",
    "city_name": "TUNKWA LAKE",
    "icbc_city_code": "TUNK",
    "icbc_city_name": "TUNKWA LAKE",
    "icbc_city_name_legacy": "LOGAN LAKE",
    "vips_city_name": "TUNKWA LAKE"
  },
  {
    "city_code": "TUPR",
    "city_name": "TUPPER",
    "icbc_city_code": "TUPR",
    "icbc_city_name": "TUPPER",
    "icbc_city_name_legacy": "TUPPER",
    "vips_city_name": "TUPPER"
  },
  {
    "city_code": "TRNI",
    "city_name": "TURNOUR ISLAND",
    "icbc_city_code": "TRNI",
    "icbc_city_name": "TURNOUR ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "TURNOUR ISLAND"
  },
  {
    "city_code": "TRTV",
    "city_name": "TURTLE VALLEY",
    "icbc_city_code": "TRTV",
    "icbc_city_name": "TURTLE VALLEY",
    "icbc_city_name_legacy": "CHASE",
    "vips_city_name": "TURTLE VALLEY"
  },
  {
    "city_code": "TWPP",
    "city_name": "TWEEDSMUIR PROVINCIAL PARK",
    "icbc_city_code": "TWPP",
    "icbc_city_name": "TWEEDSMUIR PROVINCIAL PARK",
    "icbc_city_name_legacy": "ANAHIM LAKE",
    "vips_city_name": "TWEEDSMUIR PROVINCIAL PARK"
  },
  {
    "city_code": "TWPS",
    "city_name": "TWEEDSMUIR PARK SOUTH",
    "icbc_city_code": "TWPS",
    "icbc_city_name": "TWEEDSMUIR PARK SOUTH",
    "icbc_city_name_legacy": "ANAHIM LAKE",
    "vips_city_name": "TWEEDSMUIR PARK SOUTH"
  },
  {
    "city_code": "TWOM",
    "city_name": "TWO MILE",
    "icbc_city_code": "TWOM",
    "icbc_city_name": "TWO MILE",
    "icbc_city_name_legacy": "NEW HAZELTON",
    "vips_city_name": "TWO MILE"
  },
  {
    "city_code": "TWRV",
    "city_name": "TWO RIVERS",
    "icbc_city_code": "TWRV",
    "icbc_city_name": "TWO RIVERS",
    "icbc_city_name_legacy": "TWO RIVERS",
    "vips_city_name": "TWO RIVERS"
  },
  {
    "city_code": "TYE",
    "city_name": "TYE",
    "icbc_city_code": "TYE",
    "icbc_city_name": "TYE",
    "icbc_city_name_legacy": "TYE",
    "vips_city_name": "TYE"
  },
  {
    "city_code": "TZIS",
    "city_name": "TZARTUS ISLAND",
    "icbc_city_code": "TZIS",
    "icbc_city_name": "TZARTUS ISLAND",
    "icbc_city_name_legacy": "UCLUELET",
    "vips_city_name": "TZARTUS ISLAND"
  },
  {
    "city_code": "UBC",
    "city_name": "UBC",
    "icbc_city_code": "UBC",
    "icbc_city_name": "UBC - VANCOUVER",
    "icbc_city_name_legacy": "UNIVERSITY ENDO",
    "vips_city_name": "UBC - VANCOUVER"
  },
  {
    "city_code": "UCLT",
    "city_name": "UCLUELET",
    "icbc_city_code": "UCLT",
    "icbc_city_name": "UCLUELET",
    "icbc_city_name_legacy": "UCLUELET",
    "vips_city_name": "UCLUELET"
  },
  {
    "city_code": "UNBA",
    "city_name": "UNION BAY",
    "icbc_city_code": "UNBA",
    "icbc_city_name": "UNION BAY",
    "icbc_city_name_legacy": "UNION BAY",
    "vips_city_name": "UNION BAY"
  },
  {
    "city_code": "UNIS",
    "city_name": "UNION ISLAND",
    "icbc_city_code": "UNIS",
    "icbc_city_name": "UNION ISLAND",
    "icbc_city_name_legacy": "KYUQUOT",
    "vips_city_name": "UNION ISLAND"
  },
  {
    "city_code": "UPCK",
    "city_name": "UPPER CUTBANK",
    "icbc_city_code": "UPCK",
    "icbc_city_name": "UPPER CUTBANK",
    "icbc_city_name_legacy": "DAWSON CREEK",
    "vips_city_name": "UPPER CUTBANK"
  },
  {
    "city_code": "UPFR",
    "city_name": "UPPER FRASER",
    "icbc_city_code": "UPFR",
    "icbc_city_name": "UPPER FRASER",
    "icbc_city_name_legacy": "UPPER FRASER",
    "vips_city_name": "UPPER FRASER"
  },
  {
    "city_code": "VLIS",
    "city_name": "VALDES ISLAND",
    "icbc_city_code": "VLIS",
    "icbc_city_name": "VALDES ISLAND",
    "icbc_city_name_legacy": "GABRIOLA",
    "vips_city_name": "VALDES ISLAND"
  },
  {
    "city_code": "VLMT",
    "city_name": "VALEMOUNT",
    "icbc_city_code": "VLMT",
    "icbc_city_name": "VALEMOUNT",
    "icbc_city_name_legacy": "VALEMOUNT",
    "vips_city_name": "VALEMOUNT"
  },
  {
    "city_code": "VMRU",
    "city_name": "VALEMOUNT RURAL",
    "icbc_city_code": "VMRU",
    "icbc_city_name": "VALEMOUNT RURAL",
    "icbc_city_name_legacy": "VALEMOUNT",
    "vips_city_name": "VALEMOUNT RURAL"
  },
  {
    "city_code": "VLCN",
    "city_name": "VALLICAN",
    "icbc_city_code": "VLCN",
    "icbc_city_name": "VALLICAN",
    "icbc_city_name_legacy": "VALLICAN",
    "vips_city_name": "VALLICAN"
  },
  {
    "city_code": "VNDA",
    "city_name": "VAN ANDA",
    "icbc_city_code": "VNDA",
    "icbc_city_name": "VAN ANDA",
    "icbc_city_name_legacy": "VAN ANDA",
    "vips_city_name": "VAN ANDA"
  },
  {
    "city_code": "VAN",
    "city_name": "VANCOUVER",
    "icbc_city_code": "VAN",
    "icbc_city_name": "VANCOUVER",
    "icbc_city_name_legacy": "VANCOUVER",
    "vips_city_name": "VANCOUVER"
  },
  {
    "city_code": "VNHF",
    "city_name": "VANDERHOOF",
    "icbc_city_code": "VNHF",
    "icbc_city_name": "VANDERHOOF",
    "icbc_city_name_legacy": "VANDERHOOF",
    "vips_city_name": "VANDERHOOF"
  },
  {
    "city_code": "VGIS",
    "city_name": "VARGAS ISLAND",
    "icbc_city_code": "VGIS",
    "icbc_city_name": "VARGAS ISLAND",
    "icbc_city_name_legacy": "TOFINO",
    "vips_city_name": "VARGAS ISLAND"
  },
  {
    "city_code": "VNBY",
    "city_name": "VAVENBY",
    "icbc_city_code": "VNBY",
    "icbc_city_name": "VAVENBY",
    "icbc_city_name_legacy": "VAVENBY",
    "vips_city_name": "VAVENBY"
  },
  {
    "city_code": "VEVV",
    "city_name": "VENABLES VALLEY",
    "icbc_city_code": "VEVV",
    "icbc_city_name": "VENABLES VALLEY",
    "icbc_city_name_legacy": "SPATSUM",
    "vips_city_name": "VENABLES VALLEY"
  },
  {
    "city_code": "VERN",
    "city_name": "VERNON",
    "icbc_city_code": "VERN",
    "icbc_city_name": "VERNON",
    "icbc_city_name_legacy": "VERNON",
    "vips_city_name": "VERNON"
  },
  {
    "city_code": "VCTA",
    "city_name": "VICTORIA",
    "icbc_city_code": "VCTA",
    "icbc_city_name": "VICTORIA",
    "icbc_city_name_legacy": "VICTORIA",
    "vips_city_name": "VICTORIA"
  },
  {
    "city_code": "VROY",
    "city_name": "VIEW ROYAL",
    "icbc_city_code": "VROY",
    "icbc_city_name": "VIEW ROYAL",
    "icbc_city_name_legacy": "VIEW ROYAL",
    "vips_city_name": "VIEW ROYAL"
  },
  {
    "city_code": "VLVI",
    "city_name": "VILLAVERDE ISLANDS",
    "icbc_city_code": "VLVI",
    "icbc_city_name": "VILLAVERDE ISLANDS",
    "icbc_city_name_legacy": "GOLD RIVER",
    "vips_city_name": "VILLAVERDE ISLANDS"
  },
  {
    "city_code": "VINS",
    "city_name": "VINSULLA",
    "icbc_city_code": "VINS",
    "icbc_city_name": "VINSULLA",
    "icbc_city_name_legacy": "VINSULLA",
    "vips_city_name": "VINSULLA"
  },
  {
    "city_code": "VCIS",
    "city_name": "VISCOUNT ISLAND",
    "icbc_city_code": "VCIS",
    "icbc_city_name": "VISCOUNT ISLAND",
    "icbc_city_name_legacy": "ALERT BAY",
    "vips_city_name": "VISCOUNT ISLAND"
  },
  {
    "city_code": "WLIS",
    "city_name": "WALES ISLAND",
    "icbc_city_code": "WLIS",
    "icbc_city_name": "WALES ISLAND",
    "icbc_city_name_legacy": "KINCOLITH",
    "vips_city_name": "WALES ISLAND"
  },
  {
    "city_code": "WHCN",
    "city_name": "WALHACHIN",
    "icbc_city_code": "WHCN",
    "icbc_city_name": "WALHACHIN",
    "icbc_city_name_legacy": "WALHACHIN",
    "vips_city_name": "WALHACHIN"
  },
  {
    "city_code": "WPRV",
    "city_name": "WAPITI RIVER",
    "icbc_city_code": "WPRV",
    "icbc_city_name": "WAPITI RIVER",
    "icbc_city_name_legacy": "TUMBLER RIDGE",
    "vips_city_name": "WAPITI RIVER"
  },
  {
    "city_code": "WDNR",
    "city_name": "WARDNER",
    "icbc_city_code": "WDNR",
    "icbc_city_name": "WARDNER",
    "icbc_city_name_legacy": "WARDNER",
    "vips_city_name": "WARDNER"
  },
  {
    "city_code": "WRFD",
    "city_name": "WARFIELD",
    "icbc_city_code": "WRFD",
    "icbc_city_name": "WARFIELD",
    "icbc_city_name_legacy": "WARFIELD",
    "vips_city_name": "WARFIELD"
  },
  {
    "city_code": "WASA",
    "city_name": "WASA",
    "icbc_city_code": "WASA",
    "icbc_city_name": "WASA",
    "icbc_city_name_legacy": "WASA",
    "vips_city_name": "WASA"
  },
  {
    "city_code": "WTLK",
    "city_name": "WATCH LAKE",
    "icbc_city_code": "WTLK",
    "icbc_city_name": "WATCH LAKE",
    "icbc_city_name_legacy": "WATCH LAKE",
    "vips_city_name": "WATCH LAKE"
  },
  {
    "city_code": "WHLK",
    "city_name": "WATHUS ISLAND",
    "icbc_city_code": "WHLK",
    "icbc_city_name": "WATHUS ISLAND",
    "icbc_city_name_legacy": "MASSET",
    "vips_city_name": "WATHUS ISLAND"
  },
  {
    "city_code": "WNLK",
    "city_name": "WATSON LAKE",
    "icbc_city_code": "WNLK",
    "icbc_city_name": "WATSON LAKE",
    "icbc_city_name_legacy": "WATSON LAKE",
    "vips_city_name": "WATSON LAKE"
  },
  {
    "city_code": "WELL",
    "city_name": "WELLS",
    "icbc_city_code": "WELL",
    "icbc_city_name": "WELLS",
    "icbc_city_name_legacy": "WELLS",
    "vips_city_name": "WELLS"
  },
  {
    "city_code": "WLGP",
    "city_name": "WELLS GRAY PARK",
    "icbc_city_code": "WLGP",
    "icbc_city_name": "WELLS GRAY PARK",
    "icbc_city_name_legacy": "CLEARWATER",
    "vips_city_name": "WELLS GRAY PARK"
  },
  {
    "city_code": "WCIS",
    "city_name": "WEST CRACROFT ISLAND",
    "icbc_city_code": "WCIS",
    "icbc_city_name": "WEST CRACROFT ISLAND",
    "icbc_city_name_legacy": "SAYWARD",
    "vips_city_name": "WEST CRACROFT ISLAND"
  },
  {
    "city_code": "WFRN",
    "city_name": "WEST FERNIE",
    "icbc_city_code": "WFRN",
    "icbc_city_name": "WEST FERNIE",
    "icbc_city_name_legacy": "FERNIE",
    "vips_city_name": "WEST FERNIE"
  },
  {
    "city_code": "WKLN",
    "city_name": "WEST KELOWNA",
    "icbc_city_code": "WKLN",
    "icbc_city_name": "WEST KELOWNA",
    "icbc_city_name_legacy": "WEST KELOWNA",
    "vips_city_name": "WEST KELOWNA"
  },
  {
    "city_code": "WLAK",
    "city_name": "WEST LAKE",
    "icbc_city_code": "WLAK",
    "icbc_city_name": "WEST LAKE",
    "icbc_city_name_legacy": "PRINCE GEORGE",
    "vips_city_name": "WEST LAKE"
  },
  {
    "city_code": "WVAN",
    "city_name": "WEST VANCOUVER",
    "icbc_city_code": "WVAN",
    "icbc_city_name": "WEST VANCOUVER",
    "icbc_city_name_legacy": "WEST VANCOUVER",
    "vips_city_name": "WEST VANCOUVER"
  },
  {
    "city_code": "WTBR",
    "city_name": "WESTBRIDGE",
    "icbc_city_code": "WTBR",
    "icbc_city_name": "WESTBRIDGE",
    "icbc_city_name_legacy": "WESTBRIDGE",
    "vips_city_name": "WESTBRIDGE"
  },
  {
    "city_code": "WSHM",
    "city_name": "WESTHOLME",
    "icbc_city_code": "WSHM",
    "icbc_city_name": "WESTHOLME",
    "icbc_city_name_legacy": "WESTHOLME",
    "vips_city_name": "WESTHOLME"
  },
  {
    "city_code": "WTWD",
    "city_name": "WESTWOLD",
    "icbc_city_code": "WTWD",
    "icbc_city_name": "WESTWOLD",
    "icbc_city_name_legacy": "WESTWOLD",
    "vips_city_name": "WESTWOLD"
  },
  {
    "city_code": "WLTN",
    "city_name": "WHALETOWN",
    "icbc_city_code": "WLTN",
    "icbc_city_name": "WHALETOWN",
    "icbc_city_name_legacy": "WHALETOWN",
    "vips_city_name": "WHALETOWN"
  },
  {
    "city_code": "WHIS",
    "city_name": "WHISTLER",
    "icbc_city_code": "WHIS",
    "icbc_city_name": "WHISTLER",
    "icbc_city_name_legacy": "WHISTLER",
    "vips_city_name": "WHISTLER"
  },
  {
    "city_code": "WELK",
    "city_name": "WHITE LAKE",
    "icbc_city_code": "WELK",
    "icbc_city_name": "WHITE LAKE",
    "icbc_city_name_legacy": "BLIND BAY",
    "vips_city_name": "WHITE LAKE"
  },
  {
    "city_code": "WHRV",
    "city_name": "WHITE RIVER",
    "icbc_city_code": "WHRV",
    "icbc_city_name": "WHITE RIVER",
    "icbc_city_name_legacy": "STEWART",
    "vips_city_name": "WHITE RIVER"
  },
  {
    "city_code": "WHTR",
    "city_name": "WHITE ROCK",
    "icbc_city_code": "WHTR",
    "icbc_city_name": "WHITE ROCK",
    "icbc_city_name_legacy": "WHITE ROCK",
    "vips_city_name": "WHITE ROCK"
  },
  {
    "city_code": "WYIS",
    "city_name": "WHITELEY ISLAND",
    "icbc_city_code": "WYIS",
    "icbc_city_name": "WHITELEY ISLAND",
    "icbc_city_name_legacy": "KYUQUOT",
    "vips_city_name": "WHITELEY ISLAND"
  },
  {
    "city_code": "WCKI",
    "city_name": "WICKANINNISH ISLAND",
    "icbc_city_code": "WCKI",
    "icbc_city_name": "WICKANINNISH ISLAND",
    "icbc_city_name_legacy": "TOFINO",
    "vips_city_name": "WICKANINNISH ISLAND"
  },
  {
    "city_code": "WIIS",
    "city_name": "WILLIAM ISLAND",
    "icbc_city_code": "WIIS",
    "icbc_city_name": "WILLIAM ISLAND",
    "icbc_city_name_legacy": "MADEIRA PARK",
    "vips_city_name": "WILLIAM ISLAND"
  },
  {
    "city_code": "WLLK",
    "city_name": "WILLIAMS LAKE",
    "icbc_city_code": "WLLK",
    "icbc_city_name": "WILLIAMS LAKE",
    "icbc_city_name_legacy": "WILLIAMS LAKE",
    "vips_city_name": "WILLIAMS LAKE"
  },
  {
    "city_code": "WIPT",
    "city_name": "WILLIS POINT",
    "icbc_city_code": "WIPT",
    "icbc_city_name": "WILLIS POINT",
    "icbc_city_name_legacy": "SIDNEY",
    "vips_city_name": "WILLIS POINT"
  },
  {
    "city_code": "WILK",
    "city_name": "WILLISTON LAKE",
    "icbc_city_code": "WILK",
    "icbc_city_name": "WILLISTON LAKE",
    "icbc_city_name_legacy": "MACKENZIE",
    "vips_city_name": "WILLISTON LAKE"
  },
  {
    "city_code": "WLRV",
    "city_name": "WILLOW RIVER",
    "icbc_city_code": "WLRV",
    "icbc_city_name": "WILLOW RIVER",
    "icbc_city_name_legacy": "WILLOW RIVER",
    "vips_city_name": "WILLOW RIVER"
  },
  {
    "city_code": "WLVY",
    "city_name": "WILLOW VALLEY",
    "icbc_city_code": "WLVY",
    "icbc_city_name": "WILLOW VALLEY",
    "icbc_city_name_legacy": "DAWSON CREEK",
    "vips_city_name": "WILLOW VALLEY"
  },
  {
    "city_code": "WLMR",
    "city_name": "WILMER",
    "icbc_city_code": "WLMR",
    "icbc_city_name": "WILMER",
    "icbc_city_name_legacy": "WILMER",
    "vips_city_name": "WILMER"
  },
  {
    "city_code": "WLCK",
    "city_name": "WILSON CREEK",
    "icbc_city_code": "WLCK",
    "icbc_city_name": "WILSON CREEK",
    "icbc_city_name_legacy": "WILSON CREEK",
    "vips_city_name": "WILSON CREEK"
  },
  {
    "city_code": "WNDR",
    "city_name": "WINDERMERE",
    "icbc_city_code": "WNDR",
    "icbc_city_name": "WINDERMERE",
    "icbc_city_name_legacy": "WINDERMERE",
    "vips_city_name": "WINDERMERE"
  },
  {
    "city_code": "WNLW",
    "city_name": "WINLAW",
    "icbc_city_code": "WNLW",
    "icbc_city_name": "WINLAW",
    "icbc_city_name_legacy": "WINLAW",
    "vips_city_name": "WINLAW"
  },
  {
    "city_code": "WNHR",
    "city_name": "WINTER HARBOUR",
    "icbc_city_code": "WNHR",
    "icbc_city_name": "WINTER HARBOUR",
    "icbc_city_name_legacy": "WINTER HARBOUR",
    "vips_city_name": "WINTER HARBOUR"
  },
  {
    "city_code": "WIST",
    "city_name": "WISTARIA",
    "icbc_city_code": "WIST",
    "icbc_city_name": "WISTARIA",
    "icbc_city_name_legacy": "WISTARIA",
    "vips_city_name": "WISTARIA"
  },
  {
    "city_code": "WITT",
    "city_name": "WITSET",
    "icbc_city_code": "WITT",
    "icbc_city_name": "WITSET",
    "icbc_city_name_legacy": "WITSET",
    "vips_city_name": "WITSET"
  },
  {
    "city_code": "WONO",
    "city_name": "WONOWON",
    "icbc_city_code": "WONO",
    "icbc_city_name": "WONOWON",
    "icbc_city_name_legacy": "WONOWON",
    "vips_city_name": "WONOWON"
  },
  {
    "city_code": "WOOD",
    "city_name": "WOODPECKER",
    "icbc_city_code": "WOOD",
    "icbc_city_name": "WOODPECKER",
    "icbc_city_name_legacy": "WOODPECKER",
    "vips_city_name": "WOODPECKER"
  },
  {
    "city_code": "WSLK",
    "city_name": "WOSS",
    "icbc_city_code": "WSLK",
    "icbc_city_name": "WOSS",
    "icbc_city_name_legacy": "WOSS",
    "vips_city_name": "WOSS"
  },
  {
    "city_code": "WYCF",
    "city_name": "WYCLIFFE",
    "icbc_city_code": "WYCF",
    "icbc_city_name": "WYCLIFFE",
    "icbc_city_name_legacy": "WYCLIFFE",
    "vips_city_name": "WYCLIFFE"
  },
  {
    "city_code": "WNDL",
    "city_name": "WYNNDEL",
    "icbc_city_code": "WNDL",
    "icbc_city_name": "WYNNDEL",
    "icbc_city_name_legacy": "WYNNDEL",
    "vips_city_name": "WYNNDEL"
  },
  {
    "city_code": "YAHK",
    "city_name": "YAHK",
    "icbc_city_code": "YAHK",
    "icbc_city_name": "YAHK",
    "icbc_city_name_legacy": "YAHK",
    "vips_city_name": "YAHK"
  },
  {
    "city_code": "YALE",
    "city_name": "YALE",
    "icbc_city_code": "YALE",
    "icbc_city_name": "YALE",
    "icbc_city_name_legacy": "YALE",
    "vips_city_name": "YALE"
  },
  {
    "city_code": "YMIR",
    "city_name": "YMIR",
    "icbc_city_code": "YMIR",
    "icbc_city_name": "YMIR",
    "icbc_city_name_legacy": "YMIR",
    "vips_city_name": "YMIR"
  },
  {
    "city_code": "YOBO",
    "city_name": "YOUBOU",
    "icbc_city_code": "YOBO",
    "icbc_city_name": "YOUBOU",
    "icbc_city_name_legacy": "YOUBOU",
    "vips_city_name": "YOUBOU"
  },
  {
    "city_code": "YOYO",
    "city_name": "YOYO",
    "icbc_city_code": "YOYO",
    "icbc_city_name": "YOYO",
    "icbc_city_name_legacy": "FORT NELSON",
    "vips_city_name": "YOYO"
  },
  {
    "city_code": "ZYIS",
    "city_name": "ZAYAS ISLAND",
    "icbc_city_code": "ZYIS",
    "icbc_city_name": "ZAYAS ISLAND",
    "icbc_city_name_legacy": "PRINCE RUPERT",
    "vips_city_name": "ZAYAS ISLAND"
  },
  {
    "city_code": "ZBLS",
    "city_name": "ZEBALLOS",
    "icbc_city_code": "ZBLS",
    "icbc_city_name": "ZEBALLOS",
    "icbc_city_name_legacy": "ZEBALLOS",
    "vips_city_name": "ZEBALLOS"
  }
]

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city_cross_ref',
    sa.Column('city_code', sa.String(), nullable=False),
    sa.Column('city_name', sa.String(), nullable=True),
    sa.Column('icbc_city_code', sa.String(), nullable=True),
    sa.Column('icbc_city_name', sa.String(), nullable=True),
    sa.Column('icbc_city_name_legacy', sa.String(), nullable=True),
    sa.Column('vips_city_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('city_code')
    )
    
    with op.get_context().autocommit_block():
        bind = op.get_bind()
        meta = sa.MetaData()
        meta.bind = bind
        meta.reflect(bind=bind, only=('city_cross_ref',))
        city_cross_ref = sa.Table('city_cross_ref', meta)
        op.bulk_insert(city_cross_ref, new_data)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('city_cross_ref')
    # ### end Alembic commands ###
