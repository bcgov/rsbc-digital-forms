"""empty message

Revision ID: eaed4d2b6dd3
Revises: 666113694229
Create Date: 2024-03-07 13:39:31.334958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eaed4d2b6dd3'
down_revision = '666113694229'
branch_labels = None
depends_on = None

vehicle_makes = [
  {
    "make_cd": "ABAR",
    "make_dsc": "ABARTH"
  },
  {
    "make_cd": "AC",
    "make_dsc": "A C (GREAT BRITAIN)"
  },
  {
    "make_cd": "ACAD",
    "make_dsc": "ACADIAN (GM OF CANADA)"
  },
  {
    "make_cd": "ACUR",
    "make_dsc": "ACURA"
  },
  {
    "make_cd": "ADET",
    "make_dsc": "ADETTE"
  },
  {
    "make_cd": "ADVA",
    "make_dsc": "ADVANCED"
  },
  {
    "make_cd": "AERO",
    "make_dsc": "AEROCAR"
  },
  {
    "make_cd": "AETA",
    "make_dsc": "AETA"
  },
  {
    "make_cd": "ALCI",
    "make_dsc": "ALLEN COACHWORKS INC."
  },
  {
    "make_cd": "ALFA",
    "make_dsc": "ALFA ROMEO"
  },
  {
    "make_cd": "ALLA",
    "make_dsc": "ALLARD"
  },
  {
    "make_cd": "ALLF",
    "make_dsc": "ALLISONS FIBERGLASS MFG.INC."
  },
  {
    "make_cd": "ALLS",
    "make_dsc": "ALL STATE"
  },
  {
    "make_cd": "ALMA",
    "make_dsc": "ALMA"
  },
  {
    "make_cd": "ALPI",
    "make_dsc": "ALPHINE"
  },
  {
    "make_cd": "ALTA",
    "make_dsc": "ALTA"
  },
  {
    "make_cd": "ALVI",
    "make_dsc": "ALVIS"
  },
  {
    "make_cd": "AMER",
    "make_dsc": "AMERICAN MOTORS"
  },
  {
    "make_cd": "AMPH",
    "make_dsc": "AMPHICAR"
  },
  {
    "make_cd": "ANSE",
    "make_dsc": "ANSER MANUFACTURING LTD"
  },
  {
    "make_cd": "ARGO",
    "make_dsc": "ARGONAUT STATE LIMOUSINE"
  },
  {
    "make_cd": "ARIS",
    "make_dsc": "ARISTA"
  },
  {
    "make_cd": "ARMS",
    "make_dsc": "ARMSTRONG SIDDELEY"
  },
  {
    "make_cd": "ARNO",
    "make_dsc": "ARNOLT-BRISTOL"
  },
  {
    "make_cd": "ASA",
    "make_dsc": "ASA"
  },
  {
    "make_cd": "ASCO",
    "make_dsc": "ASCORT"
  },
  {
    "make_cd": "ASHL",
    "make_dsc": "ASHLEY"
  },
  {
    "make_cd": "ASTO",
    "make_dsc": "ASTON-MARTIN"
  },
  {
    "make_cd": "ASUN",
    "make_dsc": "ASUNA"
  },
  {
    "make_cd": "ASVE",
    "make_dsc": "ASSEMBLED VEHICLE"
  },
  {
    "make_cd": "AUBU",
    "make_dsc": "AUBURN"
  },
  {
    "make_cd": "AUDI",
    "make_dsc": "AUDI"
  },
  {
    "make_cd": "AUKR",
    "make_dsc": "AUTOKRAFT"
  },
  {
    "make_cd": "AURO",
    "make_dsc": "AURORA"
  },
  {
    "make_cd": "AUST",
    "make_dsc": "AUSTIN-HEALY"
  },
  {
    "make_cd": "AUTA",
    "make_dsc": "AUTOBIANCHI"
  },
  {
    "make_cd": "AUTB",
    "make_dsc": "AUTOBIEU"
  },
  {
    "make_cd": "AUTO",
    "make_dsc": "AUTOCAR"
  },
  {
    "make_cd": "AUTR",
    "make_dsc": "AUTOCARRIER AND A.C."
  },
  {
    "make_cd": "AUTU",
    "make_dsc": "AUTO UNION"
  },
  {
    "make_cd": "AVAN",
    "make_dsc": "AVANTI"
  },
  {
    "make_cd": "AVEN",
    "make_dsc": "AVENGER"
  },
  {
    "make_cd": "AVIA",
    "make_dsc": "AVIA"
  },
  {
    "make_cd": "BANT",
    "make_dsc": "BANTAM"
  },
  {
    "make_cd": "BAY",
    "make_dsc": "BAYLINER"
  },
  {
    "make_cd": "BEAR",
    "make_dsc": "BEARDMORE"
  },
  {
    "make_cd": "BEDF",
    "make_dsc": "BEDFORD"
  },
  {
    "make_cd": "BEJE",
    "make_dsc": "BEIJING JEEP"
  },
  {
    "make_cd": "BENT",
    "make_dsc": "BENTLEY"
  },
  {
    "make_cd": "BERG",
    "make_dsc": "BERGANTINE"
  },
  {
    "make_cd": "BERK",
    "make_dsc": "BERKELEY"
  },
  {
    "make_cd": "BERO",
    "make_dsc": "BERTONE"
  },
  {
    "make_cd": "BESA",
    "make_dsc": "BESASIE AUTOMOBILE CO. INC."
  },
  {
    "make_cd": "BIGT",
    "make_dsc": "BIG TEX"
  },
  {
    "make_cd": "BITT",
    "make_dsc": "BITTER"
  },
  {
    "make_cd": "BIZZ",
    "make_dsc": "BIZZARRINI"
  },
  {
    "make_cd": "BLUE",
    "make_dsc": "BLUEBIRD"
  },
  {
    "make_cd": "BMC",
    "make_dsc": "B M C"
  },
  {
    "make_cd": "BMW",
    "make_dsc": "BMW"
  },
  {
    "make_cd": "BOBB",
    "make_dsc": "BOBBI-KAR"
  },
  {
    "make_cd": "BOCA",
    "make_dsc": "BOCAR"
  },
  {
    "make_cd": "BOM",
    "make_dsc": "BOMBARDIER"
  },
  {
    "make_cd": "BONA",
    "make_dsc": "BONAIR LEISURE PRODUCTS LTD."
  },
  {
    "make_cd": "BOND",
    "make_dsc": "BOND"
  },
  {
    "make_cd": "BORG",
    "make_dsc": "BORGWARD"
  },
  {
    "make_cd": "BOS",
    "make_dsc": "BOSTON WHALER"
  },
  {
    "make_cd": "BRAS",
    "make_dsc": "BRASINCA"
  },
  {
    "make_cd": "BRDL",
    "make_dsc": "BRADLEY GT"
  },
  {
    "make_cd": "BREM",
    "make_dsc": "BREMEN SPORT EQUIPMENT"
  },
  {
    "make_cd": "BRIC",
    "make_dsc": "BRICKLIN"
  },
  {
    "make_cd": "BRIS",
    "make_dsc": "BRISTOL"
  },
  {
    "make_cd": "BROD",
    "make_dsc": "BRODEX"
  },
  {
    "make_cd": "BUEL",
    "make_dsc": "BUELL"
  },
  {
    "make_cd": "BUGA",
    "make_dsc": "BUGATTI"
  },
  {
    "make_cd": "BUIC",
    "make_dsc": "BUICK"
  },
  {
    "make_cd": "BUTT",
    "make_dsc": "BUTTERFIELD MUSKETEER"
  },
  {
    "make_cd": "BZEL",
    "make_dsc": "B & Z ELECTRIC CAR CO."
  },
  {
    "make_cd": "CADI",
    "make_dsc": "CADILLAC"
  },
  {
    "make_cd": "CAM",
    "make_dsc": "CAMPION"
  },
  {
    "make_cd": "CAPR",
    "make_dsc": "CAPRI"
  },
  {
    "make_cd": "CASE",
    "make_dsc": "CASE"
  },
  {
    "make_cd": "CATE",
    "make_dsc": "CATERPILLAR"
  },
  {
    "make_cd": "CBTR",
    "make_dsc": "C & B TRAILER"
  },
  {
    "make_cd": "CHA",
    "make_dsc": "CHAMPION"
  },
  {
    "make_cd": "CHAI",
    "make_dsc": "CHAIKA"
  },
  {
    "make_cd": "CHEC",
    "make_dsc": "CHECKER"
  },
  {
    "make_cd": "CHEV",
    "make_dsc": "CHEVROLET"
  },
  {
    "make_cd": "CHIN",
    "make_dsc": "CHING-KAN-SHAN"
  },
  {
    "make_cd": "CHRY",
    "make_dsc": "CHRYSLER"
  },
  {
    "make_cd": "CISI",
    "make_dsc": "CISITALIA"
  },
  {
    "make_cd": "CITI",
    "make_dsc": "CITICAR (ELECTRIC CAR)"
  },
  {
    "make_cd": "CITR",
    "make_dsc": "CITROEN"
  },
  {
    "make_cd": "CLAC",
    "make_dsc": "CLASSIC ROADSTERS LTD."
  },
  {
    "make_cd": "CLAI",
    "make_dsc": "CLASSIC MOTOR CARRIAGES INC."
  },
  {
    "make_cd": "CLEN",
    "make_dsc": "CLENET COACH WORKS"
  },
  {
    "make_cd": "CLUA",
    "make_dsc": "CLUA"
  },
  {
    "make_cd": "CNTL",
    "make_dsc": "CONTINENTAL"
  },
  {
    "make_cd": "COBR",
    "make_dsc": "AC COBRA"
  },
  {
    "make_cd": "COCP",
    "make_dsc": "CONCEPTOR INDUSTRIES INC"
  },
  {
    "make_cd": "COMV",
    "make_dsc": "COMMUTER VEHICLES INC"
  },
  {
    "make_cd": "CONN",
    "make_dsc": "CONNAUGHT"
  },
  {
    "make_cd": "CONS",
    "make_dsc": "CONSULIER"
  },
  {
    "make_cd": "CONT",
    "make_dsc": "CONTESSA"
  },
  {
    "make_cd": "CORD",
    "make_dsc": "CORD"
  },
  {
    "make_cd": "CRI",
    "make_dsc": "CRISCRAFT"
  },
  {
    "make_cd": "CROF",
    "make_dsc": "CROFTON CUB"
  },
  {
    "make_cd": "CROS",
    "make_dsc": "CROSLEY"
  },
  {
    "make_cd": "CUBS",
    "make_dsc": "CUBSTER"
  },
  {
    "make_cd": "CUNN",
    "make_dsc": "CUNNINGHAM"
  },
  {
    "make_cd": "DAEW",
    "make_dsc": "DAEWOO"
  },
  {
    "make_cd": "DAF",
    "make_dsc": "DAF"
  },
  {
    "make_cd": "DAIH",
    "make_dsc": "DAIHATSU"
  },
  {
    "make_cd": "DAIM",
    "make_dsc": "DAIMLER"
  },
  {
    "make_cd": "DAIN",
    "make_dsc": "D & A VEHICLES INC."
  },
  {
    "make_cd": "DATS",
    "make_dsc": "DATSUN"
  },
  {
    "make_cd": "DAVI",
    "make_dsc": "DAVIS"
  },
  {
    "make_cd": "DAYT",
    "make_dsc": "DAYTONA"
  },
  {
    "make_cd": "DB",
    "make_dsc": "D.B."
  },
  {
    "make_cd": "DBL",
    "make_dsc": "DOUBLE EAGLE"
  },
  {
    "make_cd": "DEBO",
    "make_dsc": "DEBONAIR"
  },
  {
    "make_cd": "DECO",
    "make_dsc": "DECOURVILLE"
  },
  {
    "make_cd": "DEEP",
    "make_dsc": "DEEP SANDERSON"
  },
  {
    "make_cd": "DELL",
    "make_dsc": "DELLOW"
  },
  {
    "make_cd": "DELO",
    "make_dsc": "DE LOREAN"
  },
  {
    "make_cd": "DENZ",
    "make_dsc": "DENZEL"
  },
  {
    "make_cd": "DESO",
    "make_dsc": "DESOTO"
  },
  {
    "make_cd": "DETO",
    "make_dsc": "DETOMASO"
  },
  {
    "make_cd": "DITE",
    "make_dsc": "DI TELLA"
  },
  {
    "make_cd": "DIVA",
    "make_dsc": "DIVA"
  },
  {
    "make_cd": "DKW",
    "make_dsc": "DKW"
  },
  {
    "make_cd": "DODG",
    "make_dsc": "DODGE"
  },
  {
    "make_cd": "DONG",
    "make_dsc": "DONG FENG  (EAST WIND)"
  },
  {
    "make_cd": "DUCA",
    "make_dsc": "DUCATI"
  },
  {
    "make_cd": "DUEL",
    "make_dsc": "DUEL"
  },
  {
    "make_cd": "DUES",
    "make_dsc": "DUESENBERG"
  },
  {
    "make_cd": "DURA",
    "make_dsc": "DURANT"
  },
  {
    "make_cd": "DUTC",
    "make_dsc": "DUTCHMAN MANUFACTURING INC."
  },
  {
    "make_cd": "EAGL",
    "make_dsc": "EAGLE"
  },
  {
    "make_cd": "EDSE",
    "make_dsc": "EDSEL"
  },
  {
    "make_cd": "ELVA",
    "make_dsc": "ELVA"
  },
  {
    "make_cd": "ELVC",
    "make_dsc": "ELECTRIC VEHICLE CORP."
  },
  {
    "make_cd": "EMW",
    "make_dsc": "EMW"
  },
  {
    "make_cd": "ENGF",
    "make_dsc": "ENGLISH FORD (BRITISH)"
  },
  {
    "make_cd": "ENVO",
    "make_dsc": "ENVOY"
  },
  {
    "make_cd": "ENZM",
    "make_dsc": "ENZMANN"
  },
  {
    "make_cd": "ERSK",
    "make_dsc": "ERSKINE"
  },
  {
    "make_cd": "ESCO",
    "make_dsc": "ESCORT BOAT TRAILER MFG."
  },
  {
    "make_cd": "ESHL",
    "make_dsc": "ESHELMAN SPORTABOUT"
  },
  {
    "make_cd": "ESSE",
    "make_dsc": "ESSEX"
  },
  {
    "make_cd": "EVRY",
    "make_dsc": "EVERYBODYS MOTOR CAR MFG."
  },
  {
    "make_cd": "EXCA",
    "make_dsc": "EXCALIBUR"
  },
  {
    "make_cd": "EZLO",
    "make_dsc": "EZ LOADER BOAT TRAILERS INC."
  },
  {
    "make_cd": "FACE",
    "make_dsc": "FACEL VEGA"
  },
  {
    "make_cd": "FAIR",
    "make_dsc": "FAIRTHORPE"
  },
  {
    "make_cd": "FALC",
    "make_dsc": "FALCON (BRITISH)"
  },
  {
    "make_cd": "FELB",
    "make_dsc": "FELBER"
  },
  {
    "make_cd": "FERR",
    "make_dsc": "FERRARI"
  },
  {
    "make_cd": "FIAA",
    "make_dsc": "FIAT-ABARTH"
  },
  {
    "make_cd": "FIAT",
    "make_dsc": "FIAT"
  },
  {
    "make_cd": "FIBE",
    "make_dsc": "FIBERFAB INC. (MINNEAPOLIS MN)"
  },
  {
    "make_cd": "FIES",
    "make_dsc": "FIESTA (IMPORTED BY FORD)"
  },
  {
    "make_cd": "FISK",
    "make_dsc": "FISKER"
  },
  {
    "make_cd": "FLEE",
    "make_dsc": "FLEETWOOD ENTERPRISES INC"
  },
  {
    "make_cd": "FLYE",
    "make_dsc": "FLYER"
  },
  {
    "make_cd": "FNM",
    "make_dsc": "FNM"
  },
  {
    "make_cd": "FORD",
    "make_dsc": "FORD"
  },
  {
    "make_cd": "FOUN",
    "make_dsc": "FOUNTAIN"
  },
  {
    "make_cd": "FRAN",
    "make_dsc": "FRANKLIN"
  },
  {
    "make_cd": "FRAZ",
    "make_dsc": "FRAZIER"
  },
  {
    "make_cd": "FREF",
    "make_dsc": "FRENCH FORD"
  },
  {
    "make_cd": "FREI",
    "make_dsc": "FREIGHTLINER"
  },
  {
    "make_cd": "FRIS",
    "make_dsc": "FRISKY"
  },
  {
    "make_cd": "FRNA",
    "make_dsc": "FRAZER-NASH"
  },
  {
    "make_cd": "GAZ",
    "make_dsc": "GAZ"
  },
  {
    "make_cd": "GDNE",
    "make_dsc": "GREAT DANE"
  },
  {
    "make_cd": "GENE",
    "make_dsc": "GENESIS"
  },
  {
    "make_cd": "GEO",
    "make_dsc": "GEO"
  },
  {
    "make_cd": "GIAN",
    "make_dsc": "GIANNINI"
  },
  {
    "make_cd": "GILB",
    "make_dsc": "GILBERN"
  },
  {
    "make_cd": "GINE",
    "make_dsc": "GINETTA"
  },
  {
    "make_cd": "GITA",
    "make_dsc": "GITANE"
  },
  {
    "make_cd": "GLAS",
    "make_dsc": "GLAS"
  },
  {
    "make_cd": "GLSC",
    "make_dsc": "GLASSIC"
  },
  {
    "make_cd": "GM",
    "make_dsc": "GENERAL MOTORS"
  },
  {
    "make_cd": "GMC",
    "make_dsc": "GENERAL MOTORS CORP."
  },
  {
    "make_cd": "GOLI",
    "make_dsc": "GOLIATH"
  },
  {
    "make_cd": "GORD",
    "make_dsc": "GORDON"
  },
  {
    "make_cd": "GRAC",
    "make_dsc": "GRACIELA"
  },
  {
    "make_cd": "GRAH",
    "make_dsc": "GRAHAM"
  },
  {
    "make_cd": "GRAP",
    "make_dsc": "GRAHAM-PAIGE"
  },
  {
    "make_cd": "GRIF",
    "make_dsc": "GRIFFITH"
  },
  {
    "make_cd": "GSM",
    "make_dsc": "GSM"
  },
  {
    "make_cd": "GZL",
    "make_dsc": "GAZELLE"
  },
  {
    "make_cd": "HAN",
    "make_dsc": "HANS CHRISTIAN"
  },
  {
    "make_cd": "HAR",
    "make_dsc": "HARBORCRAFT"
  },
  {
    "make_cd": "HARL",
    "make_dsc": "HARLEY DAVIDSON"
  },
  {
    "make_cd": "HARM",
    "make_dsc": "HARMON TANK CO. INC."
  },
  {
    "make_cd": "HAUL",
    "make_dsc": "HAULMARK"
  },
  {
    "make_cd": "HEIN",
    "make_dsc": "HEINKEL"
  },
  {
    "make_cd": "HENR",
    "make_dsc": "HENRY J."
  },
  {
    "make_cd": "HICK",
    "make_dsc": "HICKEY TRAIL-BLAZER"
  },
  {
    "make_cd": "HIGH",
    "make_dsc": "HIGHLINER"
  },
  {
    "make_cd": "HILL",
    "make_dsc": "HILLMAN"
  },
  {
    "make_cd": "HIND",
    "make_dsc": "HINDUSTAN"
  },
  {
    "make_cd": "HINO",
    "make_dsc": "HINO"
  },
  {
    "make_cd": "HOB",
    "make_dsc": "HOBIE CAT"
  },
  {
    "make_cd": "HOLD",
    "make_dsc": "HOLDEN"
  },
  {
    "make_cd": "HOND",
    "make_dsc": "HONDA"
  },
  {
    "make_cd": "HONG",
    "make_dsc": "HONGKI OR HONG-CHI"
  },
  {
    "make_cd": "HORC",
    "make_dsc": "HORCH LIMOUSINE"
  },
  {
    "make_cd": "HOTC",
    "make_dsc": "HOTCHKISS"
  },
  {
    "make_cd": "HRG",
    "make_dsc": "HRG"
  },
  {
    "make_cd": "HUDS",
    "make_dsc": "HUDSON"
  },
  {
    "make_cd": "HUMB",
    "make_dsc": "HUMBER"
  },
  {
    "make_cd": "HUME",
    "make_dsc": "HUMBEE SURREY"
  },
  {
    "make_cd": "HUMM",
    "make_dsc": "HUMMER"
  },
  {
    "make_cd": "HUPM",
    "make_dsc": "HUPMOBILE"
  },
  {
    "make_cd": "HYUN",
    "make_dsc": "HYUNDAI"
  },
  {
    "make_cd": "IAME",
    "make_dsc": "I.A.M.E."
  },
  {
    "make_cd": "IKA",
    "make_dsc": "I.K.A."
  },
  {
    "make_cd": "IMPB",
    "make_dsc": "I.M.P. (U.S.)"
  },
  {
    "make_cd": "IMPE",
    "make_dsc": "IMPERIAL"
  },
  {
    "make_cd": "INFI",
    "make_dsc": "INFINITI"
  },
  {
    "make_cd": "INME",
    "make_dsc": "INTERMECCANICA"
  },
  {
    "make_cd": "INNO",
    "make_dsc": "INNOCENTI"
  },
  {
    "make_cd": "INTE",
    "make_dsc": "INTERNATIONAL"
  },
  {
    "make_cd": "ISET",
    "make_dsc": "ISETTA"
  },
  {
    "make_cd": "ISO",
    "make_dsc": "ISO"
  },
  {
    "make_cd": "ISUZ",
    "make_dsc": "ISUZU"
  },
  {
    "make_cd": "ITAF",
    "make_dsc": "ITALIAN FORD"
  },
  {
    "make_cd": "ITAI",
    "make_dsc": "ITALIA"
  },
  {
    "make_cd": "JAGU",
    "make_dsc": "JAGUAR"
  },
  {
    "make_cd": "JEEP",
    "make_dsc": "JEEP"
  },
  {
    "make_cd": "JENS",
    "make_dsc": "JENSEN"
  },
  {
    "make_cd": "JETM",
    "make_dsc": "JETMOBILE"
  },
  {
    "make_cd": "JOHN",
    "make_dsc": "JOHN DEERE"
  },
  {
    "make_cd": "JOWE",
    "make_dsc": "JOWETT"
  },
  {
    "make_cd": "KAIS",
    "make_dsc": "KAISER"
  },
  {
    "make_cd": "KAWA",
    "make_dsc": "KAWASAKI"
  },
  {
    "make_cd": "KENW",
    "make_dsc": "KENWORTH"
  },
  {
    "make_cd": "KIA",
    "make_dsc": "KIA MOTORS CORPORATION"
  },
  {
    "make_cd": "KIMI",
    "make_dsc": "KING MIDGET"
  },
  {
    "make_cd": "KIOT",
    "make_dsc": "KIOTI"
  },
  {
    "make_cd": "KLIN",
    "make_dsc": "K-LINE"
  },
  {
    "make_cd": "KNIG",
    "make_dsc": "KNIGHT"
  },
  {
    "make_cd": "KUBO",
    "make_dsc": "KUBOTA"
  },
  {
    "make_cd": "KURT",
    "make_dsc": "KURTIS KRAFT"
  },
  {
    "make_cd": "LADA",
    "make_dsc": "LADA"
  },
  {
    "make_cd": "LAGO",
    "make_dsc": "LAGONDA"
  },
  {
    "make_cd": "LALL",
    "make_dsc": "LASALLE"
  },
  {
    "make_cd": "LAMB",
    "make_dsc": "LAMBRETTA"
  },
  {
    "make_cd": "LAMO",
    "make_dsc": "LAMBORGHINI"
  },
  {
    "make_cd": "LANC",
    "make_dsc": "LANCHESTER"
  },
  {
    "make_cd": "LAND",
    "make_dsc": "LAND ROVER"
  },
  {
    "make_cd": "LASE",
    "make_dsc": "LASER"
  },
  {
    "make_cd": "LDTR",
    "make_dsc": "LOAD TRAIL"
  },
  {
    "make_cd": "LEAF",
    "make_dsc": "LEA-FRANCIS"
  },
  {
    "make_cd": "LEXU",
    "make_dsc": "LEXUS"
  },
  {
    "make_cd": "LINC",
    "make_dsc": "LINCOLN-CONTINENTAL"
  },
  {
    "make_cd": "LLOY",
    "make_dsc": "LLOYD"
  },
  {
    "make_cd": "LNCI",
    "make_dsc": "LANCIA"
  },
  {
    "make_cd": "LOCO",
    "make_dsc": "LOCOMOBILE"
  },
  {
    "make_cd": "LOLA",
    "make_dsc": "LOLA"
  },
  {
    "make_cd": "LOND",
    "make_dsc": "LONDON MOTORS"
  },
  {
    "make_cd": "LONE",
    "make_dsc": "LONESTAR"
  },
  {
    "make_cd": "LOOD",
    "make_dsc": "LOODCRAFT"
  },
  {
    "make_cd": "LOTU",
    "make_dsc": "LOTUS"
  },
  {
    "make_cd": "MACK",
    "make_dsc": "MACK"
  },
  {
    "make_cd": "MAL",
    "make_dsc": "MALIBU"
  },
  {
    "make_cd": "MANA",
    "make_dsc": "MANAC"
  },
  {
    "make_cd": "MARC",
    "make_dsc": "MARCOS"
  },
  {
    "make_cd": "MARM",
    "make_dsc": "MARMON"
  },
  {
    "make_cd": "MAS",
    "make_dsc": "MASTERCRAFT"
  },
  {
    "make_cd": "MASE",
    "make_dsc": "MASERATI"
  },
  {
    "make_cd": "MASS",
    "make_dsc": "MASSEY FERGUSON"
  },
  {
    "make_cd": "MATR",
    "make_dsc": "MATRA"
  },
  {
    "make_cd": "MAXL",
    "make_dsc": "MAXWELL"
  },
  {
    "make_cd": "MAZD",
    "make_dsc": "MAZDA"
  },
  {
    "make_cd": "MBCC",
    "make_dsc": "MCBURNIE COACH CRAFT INC."
  },
  {
    "make_cd": "MBM",
    "make_dsc": "M.B.M."
  },
  {
    "make_cd": "MCI",
    "make_dsc": "MOTOR COACH INDUSTRIES"
  },
  {
    "make_cd": "MCLA",
    "make_dsc": "MCLAREN"
  },
  {
    "make_cd": "MEAN",
    "make_dsc": "MEAN"
  },
  {
    "make_cd": "MERC",
    "make_dsc": "MERCURY"
  },
  {
    "make_cd": "MERK",
    "make_dsc": "MERKUR"
  },
  {
    "make_cd": "MERZ",
    "make_dsc": "MERCEDES-BENZ"
  },
  {
    "make_cd": "MESS",
    "make_dsc": "MESSERSCHMITT"
  },
  {
    "make_cd": "METE",
    "make_dsc": "METEOR (CANADIAN MERCURY)"
  },
  {
    "make_cd": "METR",
    "make_dsc": "METROPOLITAN"
  },
  {
    "make_cd": "MG",
    "make_dsc": "MG"
  },
  {
    "make_cd": "MIKA",
    "make_dsc": "MIKASA"
  },
  {
    "make_cd": "MIKR",
    "make_dsc": "MIKRUS"
  },
  {
    "make_cd": "MINI",
    "make_dsc": "MINI"
  },
  {
    "make_cd": "MIST",
    "make_dsc": "MISTRAL"
  },
  {
    "make_cd": "MITS",
    "make_dsc": "MITSUBISHI"
  },
  {
    "make_cd": "MODE",
    "make_dsc": "MODEL A & MODEL T MOTOR CAR REPRODUCTION CORP."
  },
  {
    "make_cd": "MONA",
    "make_dsc": "MONARCH"
  },
  {
    "make_cd": "MONK",
    "make_dsc": "MONK"
  },
  {
    "make_cd": "MORE",
    "make_dsc": "MORETTI"
  },
  {
    "make_cd": "MORG",
    "make_dsc": "MORGAN"
  },
  {
    "make_cd": "MORR",
    "make_dsc": "MORRIS"
  },
  {
    "make_cd": "MOSK",
    "make_dsc": "MOSKOVITCH"
  },
  {
    "make_cd": "MOTO",
    "make_dsc": "MOTO GUZZI"
  },
  {
    "make_cd": "MUNT",
    "make_dsc": "MUNTZ"
  },
  {
    "make_cd": "MURE",
    "make_dsc": "MURENA"
  },
  {
    "make_cd": "MZMA",
    "make_dsc": "MZMA"
  },
  {
    "make_cd": "NAHA",
    "make_dsc": "NAHANNI MANUFACTURING LTD"
  },
  {
    "make_cd": "NAHE",
    "make_dsc": "NASH-HEALY"
  },
  {
    "make_cd": "NARD",
    "make_dsc": "NARDI-DANESE"
  },
  {
    "make_cd": "NASH",
    "make_dsc": "NASH"
  },
  {
    "make_cd": "NECK",
    "make_dsc": "NECKAR"
  },
  {
    "make_cd": "NEFL",
    "make_dsc": "NEW FLYER"
  },
  {
    "make_cd": "NEWM",
    "make_dsc": "NEWMAR"
  },
  {
    "make_cd": "NISS",
    "make_dsc": "NISSAN"
  },
  {
    "make_cd": "NORT",
    "make_dsc": "NORTHWOOD MANUFACTURING"
  },
  {
    "make_cd": "NOVA",
    "make_dsc": "NOVABUS"
  },
  {
    "make_cd": "NSU",
    "make_dsc": "NSU PRINZ"
  },
  {
    "make_cd": "NSUF",
    "make_dsc": "NSU-FIAT"
  },
  {
    "make_cd": "OAKL",
    "make_dsc": "OAKLAND"
  },
  {
    "make_cd": "OGLE",
    "make_dsc": "OGLE"
  },
  {
    "make_cd": "OHTA",
    "make_dsc": "OHTA"
  },
  {
    "make_cd": "OLDS",
    "make_dsc": "OLDSMOBILE"
  },
  {
    "make_cd": "OMEG",
    "make_dsc": "OMEGA (ITALIAN)"
  },
  {
    "make_cd": "OPEL",
    "make_dsc": "OPEL"
  },
  {
    "make_cd": "OPER",
    "make_dsc": "OPEN ROADSTERS OF TEXAS"
  },
  {
    "make_cd": "ORIO",
    "make_dsc": "ORION BUS INDUSTRIES"
  },
  {
    "make_cd": "OSCA",
    "make_dsc": "OSCA"
  },
  {
    "make_cd": "OSI",
    "make_dsc": "OSI"
  },
  {
    "make_cd": "OTOS",
    "make_dsc": "OTOSAN"
  },
  {
    "make_cd": "OVER",
    "make_dsc": "OVERLAND"
  },
  {
    "make_cd": "PACK",
    "make_dsc": "PACKARD"
  },
  {
    "make_cd": "PALL",
    "make_dsc": "PALLISER (RACING CAR)"
  },
  {
    "make_cd": "PANE",
    "make_dsc": "PANTHER WESTWINDS LTD."
  },
  {
    "make_cd": "PANH",
    "make_dsc": "PANHARD"
  },
  {
    "make_cd": "PANZ",
    "make_dsc": "PANOZ AUTO DEVELOPMENT"
  },
  {
    "make_cd": "PASS",
    "make_dsc": "PASSPORT"
  },
  {
    "make_cd": "PEAC",
    "make_dsc": "PEACE"
  },
  {
    "make_cd": "PEEL",
    "make_dsc": "PEEL"
  },
  {
    "make_cd": "PEER",
    "make_dsc": "PEERLESS"
  },
  {
    "make_cd": "PEGA",
    "make_dsc": "PEGASO"
  },
  {
    "make_cd": "PETE",
    "make_dsc": "PETERBILT"
  },
  {
    "make_cd": "PEUG",
    "make_dsc": "PEUGEOT"
  },
  {
    "make_cd": "PHOE",
    "make_dsc": "PHOENIX"
  },
  {
    "make_cd": "PIAG",
    "make_dsc": "PIAGGIO"
  },
  {
    "make_cd": "PINI",
    "make_dsc": "PINIFARINA"
  },
  {
    "make_cd": "PJ",
    "make_dsc": "PJ"
  },
  {
    "make_cd": "PLAY",
    "make_dsc": "PLAYBOY"
  },
  {
    "make_cd": "PLYM",
    "make_dsc": "PLYMOUTH"
  },
  {
    "make_cd": "POIR",
    "make_dsc": "POIRIER"
  },
  {
    "make_cd": "POLE",
    "make_dsc": "POLESTAR"
  },
  {
    "make_cd": "PONT",
    "make_dsc": "PONTIAC"
  },
  {
    "make_cd": "PORS",
    "make_dsc": "PORSCHE"
  },
  {
    "make_cd": "PRAI",
    "make_dsc": "PRAIRIE SCHOONER"
  },
  {
    "make_cd": "PRCA",
    "make_dsc": "PIERCE ARROW"
  },
  {
    "make_cd": "PRMO",
    "make_dsc": "PRINCE MOTORS"
  },
  {
    "make_cd": "PROG",
    "make_dsc": "PROGRESS"
  },
  {
    "make_cd": "PTV",
    "make_dsc": "PTV"
  },
  {
    "make_cd": "PUCH",
    "make_dsc": "PUCH"
  },
  {
    "make_cd": "PUMM",
    "make_dsc": "PUMA"
  },
  {
    "make_cd": "RAM",
    "make_dsc": "RAM"
  },
  {
    "make_cd": "RAMB",
    "make_dsc": "RAMBLER"
  },
  {
    "make_cd": "RAMS",
    "make_dsc": "RAMSES"
  },
  {
    "make_cd": "RAY",
    "make_dsc": "SEARAY"
  },
  {
    "make_cd": "REI",
    "make_dsc": "REINELL"
  },
  {
    "make_cd": "RELI",
    "make_dsc": "RELIANT"
  },
  {
    "make_cd": "RENA",
    "make_dsc": "RENAULT"
  },
  {
    "make_cd": "REO",
    "make_dsc": "REO"
  },
  {
    "make_cd": "REXH",
    "make_dsc": "REXHALL"
  },
  {
    "make_cd": "RILE",
    "make_dsc": "RILEY"
  },
  {
    "make_cd": "RIND",
    "make_dsc": "RICH INDUSTRIES"
  },
  {
    "make_cd": "RIVI",
    "make_dsc": "RIVIAN"
  },
  {
    "make_cd": "ROAD",
    "make_dsc": "ROADRUNNER TRAILERS MFG."
  },
  {
    "make_cd": "ROCH",
    "make_dsc": "ROCHDALE"
  },
  {
    "make_cd": "ROK",
    "make_dsc": "ROCKNE"
  },
  {
    "make_cd": "ROLL",
    "make_dsc": "ROLLS-ROYCE"
  },
  {
    "make_cd": "ROOT",
    "make_dsc": "ROOTES"
  },
  {
    "make_cd": "ROVE",
    "make_dsc": "ROVER"
  },
  {
    "make_cd": "RYCS",
    "make_dsc": "RYCSA"
  },
  {
    "make_cd": "SAAB",
    "make_dsc": "SAAB"
  },
  {
    "make_cd": "SABR",
    "make_dsc": "SABRA"
  },
  {
    "make_cd": "SANG",
    "make_dsc": "SANGYONG"
  },
  {
    "make_cd": "SATU",
    "make_dsc": "SATURN"
  },
  {
    "make_cd": "SCIO",
    "make_dsc": "SCION"
  },
  {
    "make_cd": "SEA",
    "make_dsc": "SEADOO"
  },
  {
    "make_cd": "SEAT",
    "make_dsc": "SEAT"
  },
  {
    "make_cd": "SERA",
    "make_dsc": "SERA"
  },
  {
    "make_cd": "SHEB",
    "make_dsc": "SHELBY AMERICAN"
  },
  {
    "make_cd": "SIAT",
    "make_dsc": "SIATA"
  },
  {
    "make_cd": "SILA",
    "make_dsc": "SILA AUTORETTA"
  },
  {
    "make_cd": "SIM",
    "make_dsc": "SIMCA"
  },
  {
    "make_cd": "SIN",
    "make_dsc": "SINGER"
  },
  {
    "make_cd": "SKI",
    "make_dsc": "SKI NAUTIQUE"
  },
  {
    "make_cd": "SKOD",
    "make_dsc": "SKODA"
  },
  {
    "make_cd": "SMAR",
    "make_dsc": "SMART"
  },
  {
    "make_cd": "SNOW",
    "make_dsc": "SNOWBEAR LIMITED"
  },
  {
    "make_cd": "SOUT",
    "make_dsc": "SOUTHLAND"
  },
  {
    "make_cd": "SOVA",
    "make_dsc": "SOVAM"
  },
  {
    "make_cd": "SPAR",
    "make_dsc": "SPARTAN"
  },
  {
    "make_cd": "STAN",
    "make_dsc": "STANDARD"
  },
  {
    "make_cd": "STAR",
    "make_dsc": "STAR"
  },
  {
    "make_cd": "STEW",
    "make_dsc": "STEWART"
  },
  {
    "make_cd": "STEY",
    "make_dsc": "STEYR-PUCH"
  },
  {
    "make_cd": "STLG",
    "make_dsc": "STERLING"
  },
  {
    "make_cd": "STLY",
    "make_dsc": "STANLEY"
  },
  {
    "make_cd": "STRA",
    "make_dsc": "STRALE"
  },
  {
    "make_cd": "STUD",
    "make_dsc": "STUDEBAKER"
  },
  {
    "make_cd": "STUZ",
    "make_dsc": "STUTZ"
  },
  {
    "make_cd": "SUBA",
    "make_dsc": "SUBARU"
  },
  {
    "make_cd": "SUNB",
    "make_dsc": "SUNBEAM"
  },
  {
    "make_cd": "SUPT",
    "make_dsc": "SUPER TWO"
  },
  {
    "make_cd": "SUZL",
    "make_dsc": "SUZULIGHT SU"
  },
  {
    "make_cd": "SUZU",
    "make_dsc": "SUZUKI"
  },
  {
    "make_cd": "SYRE",
    "make_dsc": "SYRENA"
  },
  {
    "make_cd": "TAMA",
    "make_dsc": "TAMA"
  },
  {
    "make_cd": "TATR",
    "make_dsc": "TATRA"
  },
  {
    "make_cd": "TAUN",
    "make_dsc": "TAUNUS (GERMAN FORD)"
  },
  {
    "make_cd": "TCHA",
    "make_dsc": "TCHAIKA"
  },
  {
    "make_cd": "TESL",
    "make_dsc": "TESLA MOTORS"
  },
  {
    "make_cd": "THOM",
    "make_dsc": "THOMAS"
  },
  {
    "make_cd": "THOR",
    "make_dsc": "THOR INDUSTRIES INC."
  },
  {
    "make_cd": "THUN",
    "make_dsc": "THUNDERJET"
  },
  {
    "make_cd": "TITA",
    "make_dsc": "TITAN MOTORCYCLE CO."
  },
  {
    "make_cd": "TJAA",
    "make_dsc": "TJAARDA"
  },
  {
    "make_cd": "TORN",
    "make_dsc": "TORNADO (BRITISH)"
  },
  {
    "make_cd": "TOYO",
    "make_dsc": "TOYOTA"
  },
  {
    "make_cd": "TOYP",
    "make_dsc": "TOYOPET"
  },
  {
    "make_cd": "TRAB",
    "make_dsc": "TRABANT"
  },
  {
    "make_cd": "TRIU",
    "make_dsc": "TRIUMPH"
  },
  {
    "make_cd": "TROJ",
    "make_dsc": "TROJAN"
  },
  {
    "make_cd": "TRPE",
    "make_dsc": "TERRAPLANE"
  },
  {
    "make_cd": "TUCK",
    "make_dsc": "TUCKER"
  },
  {
    "make_cd": "TURN",
    "make_dsc": "TURNER"
  },
  {
    "make_cd": "TVR",
    "make_dsc": "TVR"
  },
  {
    "make_cd": "TZ",
    "make_dsc": "TZ"
  },
  {
    "make_cd": "UAZ",
    "make_dsc": "UAZ (ULIANOVSK AUTOMOBILE ZAVOD)"
  },
  {
    "make_cd": "UBUI",
    "make_dsc": "U-BUILT"
  },
  {
    "make_cd": "UNIC",
    "make_dsc": "UNICAR"
  },
  {
    "make_cd": "UNIP",
    "make_dsc": "UNIPOWER"
  },
  {
    "make_cd": "USEL",
    "make_dsc": "U.S. ELECTRICAR CORP."
  },
  {
    "make_cd": "UTIL",
    "make_dsc": "UTILITY"
  },
  {
    "make_cd": "VACR",
    "make_dsc": "VECTOR AEROMOTIVE CORPORATION"
  },
  {
    "make_cd": "VAL",
    "make_dsc": "VAL"
  },
  {
    "make_cd": "VALK",
    "make_dsc": "VALKRIE"
  },
  {
    "make_cd": "VANG",
    "make_dsc": "VANGUARD (CANADA)"
  },
  {
    "make_cd": "VAUX",
    "make_dsc": "VAUXHALL"
  },
  {
    "make_cd": "VEAM",
    "make_dsc": "VEHICULOS AUTOMORES MEXICANO"
  },
  {
    "make_cd": "VERI",
    "make_dsc": "VERITAS"
  },
  {
    "make_cd": "VESP",
    "make_dsc": "VESPA"
  },
  {
    "make_cd": "VNDN",
    "make_dsc": "VANDEN PLAS"
  },
  {
    "make_cd": "VOGA",
    "make_dsc": "VOLGA"
  },
  {
    "make_cd": "VOLK",
    "make_dsc": "VOLKSWAGEN"
  },
  {
    "make_cd": "VOLV",
    "make_dsc": "VOLVO"
  },
  {
    "make_cd": "WABA",
    "make_dsc": "WABASH"
  },
  {
    "make_cd": "WARS",
    "make_dsc": "WARSZAWA"
  },
  {
    "make_cd": "WART",
    "make_dsc": "WARTBURG"
  },
  {
    "make_cd": "WARW",
    "make_dsc": "WARWICK"
  },
  {
    "make_cd": "WATF",
    "make_dsc": "WATFORD"
  },
  {
    "make_cd": "WEND",
    "make_dsc": "WENDAX"
  },
  {
    "make_cd": "WEST",
    "make_dsc": "WESTERN STAR"
  },
  {
    "make_cd": "WHIP",
    "make_dsc": "WHIPPET"
  },
  {
    "make_cd": "WILS",
    "make_dsc": "WILSON"
  },
  {
    "make_cd": "WINN",
    "make_dsc": "WINNEBEGO"
  },
  {
    "make_cd": "WLLS",
    "make_dsc": "WILLYS"
  },
  {
    "make_cd": "WOLS",
    "make_dsc": "WOLSELEY"
  },
  {
    "make_cd": "WOOD",
    "make_dsc": "WOODILL WILDFIRE"
  },
  {
    "make_cd": "WORT",
    "make_dsc": "WORTHINGTON CHAMP"
  },
  {
    "make_cd": "YAMA",
    "make_dsc": "YAMAHA"
  },
  {
    "make_cd": "YENK",
    "make_dsc": "YENKO"
  },
  {
    "make_cd": "YLN",
    "make_dsc": "YLN (YUE LOONG MOTOR CO.)"
  },
  {
    "make_cd": "ZAPO",
    "make_dsc": "ZAPOROZHETS"
  },
  {
    "make_cd": "ZARC",
    "make_dsc": "ZAR CAR"
  },
  {
    "make_cd": "ZCZY",
    "make_dsc": "ZASTAVIA (ZCZ-YUGOSLAVIA)"
  },
  {
    "make_cd": "ZETA",
    "make_dsc": "ZETA"
  },
  {
    "make_cd": "ZIL",
    "make_dsc": "ZIL"
  },
  {
    "make_cd": "ZIM",
    "make_dsc": "ZIM"
  },
  {
    "make_cd": "ZIMR",
    "make_dsc": "ZIMMERMAN AUTOMOBILES"
  },
  {
    "make_cd": "ZUND",
    "make_dsc": "ZUNDAPP"
  },
  {
    "make_cd": "ZWIC",
    "make_dsc": "ZWICKAU"
  }
]

vehicle_models = [
  {
    "model_cd": "300",
    "model_dsc": "3000 ME",
    "make_cd": "AC"
  },
  {
    "model_cd": "BEAU",
    "model_dsc": "BEAUMONT SERIES",
    "make_cd": "ACAD"
  },
  {
    "model_cd": "CANS",
    "model_dsc": "CANSO SERIES",
    "make_cd": "ACAD"
  },
  {
    "model_cd": "INVA",
    "model_dsc": "INVADER SERIES",
    "make_cd": "ACAD"
  },
  {
    "model_cd": "1.6E",
    "model_dsc": "1.6 EL",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "1.7E",
    "model_dsc": "1.7 EL",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "2.3",
    "model_dsc": "2.3",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "2.5T",
    "model_dsc": "2.5 TL",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "3.2T",
    "model_dsc": "3.2 TL",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "3.5R",
    "model_dsc": "3.5 RL",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "ATL",
    "model_dsc": "TL",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "CL",
    "model_dsc": "CL (SPORTS COUPE)",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "CSX",
    "model_dsc": "CSX",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "EL",
    "model_dsc": "EL",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "ILX",
    "model_dsc": "ILX",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "INTE",
    "model_dsc": "INTEGRA",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "LEGE",
    "model_dsc": "LEGEND",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "MDX",
    "model_dsc": "MDX",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "NSX",
    "model_dsc": "NSX",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "RDX",
    "model_dsc": "RDX",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "RL",
    "model_dsc": "RL",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "RSX",
    "model_dsc": "RSX",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "SLX",
    "model_dsc": "SLX (SPORTS UTILITY)",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "TLX",
    "model_dsc": "TLX",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "TSX",
    "model_dsc": "TSX",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "VIGO",
    "model_dsc": "VIGOR",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "3.2C",
    "model_dsc": "3.2CL",
    "make_cd": "ACUR"
  },
  {
    "model_cd": "164",
    "model_dsc": "164",
    "make_cd": "ALFA"
  },
  {
    "model_cd": "AGT",
    "model_dsc": "ALFETTA GT",
    "make_cd": "ALFA"
  },
  {
    "model_cd": "ARN",
    "model_dsc": "ARNA",
    "make_cd": "ALFA"
  },
  {
    "model_cd": "BERL",
    "model_dsc": "BERLINA",
    "make_cd": "ALFA"
  },
  {
    "model_cd": "C4",
    "model_dsc": "C4",
    "make_cd": "ALFA"
  },
  {
    "model_cd": "DUET",
    "model_dsc": "DUETTO",
    "make_cd": "ALFA"
  },
  {
    "model_cd": "G25",
    "model_dsc": "GTV6 2.5",
    "make_cd": "ALFA"
  },
  {
    "model_cd": "GIUL",
    "model_dsc": "GIULIA",
    "make_cd": "ALFA"
  },
  {
    "model_cd": "GT6",
    "model_dsc": "ALFA GT6",
    "make_cd": "ALFA"
  },
  {
    "model_cd": "MILA",
    "model_dsc": "MILANO",
    "make_cd": "ALFA"
  },
  {
    "model_cd": "MONT",
    "model_dsc": "MONTREAL",
    "make_cd": "ALFA"
  },
  {
    "model_cd": "SPRI",
    "model_dsc": "GIULIA SPRINT",
    "make_cd": "ALFA"
  },
  {
    "model_cd": "SPYD",
    "model_dsc": "SPIDER SERIES",
    "make_cd": "ALFA"
  },
  {
    "model_cd": "VELO",
    "model_dsc": "GT VELOCE",
    "make_cd": "ALFA"
  },
  {
    "model_cd": "ZAGA",
    "model_dsc": "ZAGATO",
    "make_cd": "ALFA"
  },
  {
    "model_cd": "ALLI",
    "model_dsc": "ALLIANCE",
    "make_cd": "AMER"
  },
  {
    "model_cd": "AMBA",
    "model_dsc": "AMBASSADOR",
    "make_cd": "AMER"
  },
  {
    "model_cd": "AMER",
    "model_dsc": "AMERICAN",
    "make_cd": "AMER"
  },
  {
    "model_cd": "AMX",
    "model_dsc": "AMX",
    "make_cd": "AMER"
  },
  {
    "model_cd": "CONC",
    "model_dsc": "CONCORD",
    "make_cd": "AMER"
  },
  {
    "model_cd": "EAGL",
    "model_dsc": "EAGLE",
    "make_cd": "AMER"
  },
  {
    "model_cd": "ENCO",
    "model_dsc": "ENCORE",
    "make_cd": "AMER"
  },
  {
    "model_cd": "GREM",
    "model_dsc": "GREMLIN",
    "make_cd": "AMER"
  },
  {
    "model_cd": "HORN",
    "model_dsc": "HORNET",
    "make_cd": "AMER"
  },
  {
    "model_cd": "JAVE",
    "model_dsc": "JAVELIN",
    "make_cd": "AMER"
  },
  {
    "model_cd": "MARL",
    "model_dsc": "MARLIN",
    "make_cd": "AMER"
  },
  {
    "model_cd": "MATA",
    "model_dsc": "MATADOR",
    "make_cd": "AMER"
  },
  {
    "model_cd": "MEDA",
    "model_dsc": "MEDALLION",
    "make_cd": "AMER"
  },
  {
    "model_cd": "PACE",
    "model_dsc": "PACER",
    "make_cd": "AMER"
  },
  {
    "model_cd": "RAMB",
    "model_dsc": "RAMBLER",
    "make_cd": "AMER"
  },
  {
    "model_cd": "REBE",
    "model_dsc": "REBEL",
    "make_cd": "AMER"
  },
  {
    "model_cd": "SPIR",
    "model_dsc": "SPIRIT",
    "make_cd": "AMER"
  },
  {
    "model_cd": "SPOR",
    "model_dsc": "SPORTABOUT",
    "make_cd": "AMER"
  },
  {
    "model_cd": "DB5",
    "model_dsc": "DB-5",
    "make_cd": "ASTO"
  },
  {
    "model_cd": "DB6",
    "model_dsc": "DB-6",
    "make_cd": "ASTO"
  },
  {
    "model_cd": "DB7",
    "model_dsc": "DB7(COUPE)",
    "make_cd": "ASTO"
  },
  {
    "model_cd": "LAGO",
    "model_dsc": "LAGONDA",
    "make_cd": "ASTO"
  },
  {
    "model_cd": "VANT",
    "model_dsc": "VANTAGE",
    "make_cd": "ASTO"
  },
  {
    "model_cd": "VIR",
    "model_dsc": "VIRAGE (SALOON)",
    "make_cd": "ASTO"
  },
  {
    "model_cd": "GT",
    "model_dsc": "GT",
    "make_cd": "ASUN"
  },
  {
    "model_cd": "SE",
    "model_dsc": "SE",
    "make_cd": "ASUN"
  },
  {
    "model_cd": "SUNF",
    "model_dsc": "SUNFIRE",
    "make_cd": "ASUN"
  },
  {
    "model_cd": "SUNR",
    "model_dsc": "SUNRUNNER",
    "make_cd": "ASUN"
  },
  {
    "model_cd": "100",
    "model_dsc": "100",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "1GL",
    "model_dsc": "100GL",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "1LS",
    "model_dsc": "100LS",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "200",
    "model_dsc": "200LS",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "400",
    "model_dsc": "4000",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "500",
    "model_dsc": "5000",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "850",
    "model_dsc": "850",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "A3",
    "model_dsc": "A3",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "A5",
    "model_dsc": "A5",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "A7",
    "model_dsc": "A7",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "A80",
    "model_dsc": "80",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "A90",
    "model_dsc": "90",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "AA4",
    "model_dsc": "A4",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "AA6",
    "model_dsc": "A6",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "AA8",
    "model_dsc": "A8",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "AS4",
    "model_dsc": "AS4",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "AS6",
    "model_dsc": "S6",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "AVA",
    "model_dsc": "AVANT",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "CABR",
    "model_dsc": "CABRIOLET",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "ETRO",
    "model_dsc": "E-TRON",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "FOX",
    "model_dsc": "80 LS (FOX)",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "Q3",
    "model_dsc": "Q3",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "Q5",
    "model_dsc": "Q5",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "Q7",
    "model_dsc": "Q7",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "Q8",
    "model_dsc": "Q8",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "QUAT",
    "model_dsc": "QUATTRO",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "R8",
    "model_dsc": "R8",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "RS5",
    "model_dsc": "RS5",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "RS6",
    "model_dsc": "RS6",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "S3",
    "model_dsc": "S3",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "S4",
    "model_dsc": "S4",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "S5",
    "model_dsc": "S5",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "S6",
    "model_dsc": "S6",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "S90",
    "model_dsc": "SUPER 90",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "SQ5",
    "model_dsc": "SQ5",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "TT",
    "model_dsc": "TT",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "V8",
    "model_dsc": "V-8",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "RS3",
    "model_dsc": "RS3",
    "make_cd": "AUDI"
  },
  {
    "model_cd": "100",
    "model_dsc": "100 SERIES",
    "make_cd": "AUST"
  },
  {
    "model_cd": "110",
    "model_dsc": "1100",
    "make_cd": "AUST"
  },
  {
    "model_cd": "180",
    "model_dsc": "1800",
    "make_cd": "AUST"
  },
  {
    "model_cd": "300",
    "model_dsc": "3000 SERIES",
    "make_cd": "AUST"
  },
  {
    "model_cd": "850",
    "model_dsc": "850",
    "make_cd": "AUST"
  },
  {
    "model_cd": "A10",
    "model_dsc": "A99 & 110",
    "make_cd": "AUST"
  },
  {
    "model_cd": "A40",
    "model_dsc": "A40",
    "make_cd": "AUST"
  },
  {
    "model_cd": "A55",
    "model_dsc": "A55",
    "make_cd": "AUST"
  },
  {
    "model_cd": "A60",
    "model_dsc": "CAMBRIDGE",
    "make_cd": "AUST"
  },
  {
    "model_cd": "CPS",
    "model_dsc": "COOPER S",
    "make_cd": "AUST"
  },
  {
    "model_cd": "MARI",
    "model_dsc": "MARINA",
    "make_cd": "AUST"
  },
  {
    "model_cd": "MINI",
    "model_dsc": "MINI",
    "make_cd": "AUST"
  },
  {
    "model_cd": "SPRI",
    "model_dsc": "SPRITE",
    "make_cd": "AUST"
  },
  {
    "model_cd": "WEST",
    "model_dsc": "WESTMINSTER",
    "make_cd": "AUST"
  },
  {
    "model_cd": "AAV",
    "model_dsc": "SERIES A",
    "make_cd": "AVAN"
  },
  {
    "model_cd": "ABV",
    "model_dsc": "SERIES B",
    "make_cd": "AVAN"
  },
  {
    "model_cd": "TK",
    "model_dsc": "GANG STAR",
    "make_cd": "BEJE"
  },
  {
    "model_cd": "ARN",
    "model_dsc": "ARNAGE",
    "make_cd": "BENT"
  },
  {
    "model_cd": "AZU",
    "model_dsc": "AZURE",
    "make_cd": "BENT"
  },
  {
    "model_cd": "BROO",
    "model_dsc": "BROOKLANDS",
    "make_cd": "BENT"
  },
  {
    "model_cd": "CONT",
    "model_dsc": "CONTINENTAL CONVERTIBLE",
    "make_cd": "BENT"
  },
  {
    "model_cd": "CORN",
    "model_dsc": "CORNICHE",
    "make_cd": "BENT"
  },
  {
    "model_cd": "EIGH",
    "model_dsc": "EIGHT",
    "make_cd": "BENT"
  },
  {
    "model_cd": "MULS",
    "model_dsc": "MULSANNE",
    "make_cd": "BENT"
  },
  {
    "model_cd": "TBR",
    "model_dsc": "TURBO R",
    "make_cd": "BENT"
  },
  {
    "model_cd": "CABR",
    "model_dsc": "CABRIO",
    "make_cd": "BERO"
  },
  {
    "model_cd": "PALI",
    "model_dsc": "PALINURO",
    "make_cd": "BERO"
  },
  {
    "model_cd": "X19",
    "model_dsc": "X19",
    "make_cd": "BERO"
  },
  {
    "model_cd": "BAC",
    "model_dsc": "BACI",
    "make_cd": "BESA"
  },
  {
    "model_cd": "DUMP",
    "model_dsc": "DUMP",
    "make_cd": "BIGT"
  },
  {
    "model_cd": "PRI",
    "model_dsc": "PRINCESS",
    "make_cd": "BMC"
  },
  {
    "model_cd": "M340",
    "model_dsc": "M340i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "128I",
    "model_dsc": "128i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "135I",
    "model_dsc": "135i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "160",
    "model_dsc": "1600",
    "make_cd": "BMW"
  },
  {
    "model_cd": "180",
    "model_dsc": "1800",
    "make_cd": "BMW"
  },
  {
    "model_cd": "2.8",
    "model_dsc": "2.8",
    "make_cd": "BMW"
  },
  {
    "model_cd": "200",
    "model_dsc": "2000 SERIES",
    "make_cd": "BMW"
  },
  {
    "model_cd": "202",
    "model_dsc": "2002 SERIES",
    "make_cd": "BMW"
  },
  {
    "model_cd": "230I",
    "model_dsc": "230i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "250",
    "model_dsc": "2500 SERIES",
    "make_cd": "BMW"
  },
  {
    "model_cd": "280",
    "model_dsc": "2800 SERIES",
    "make_cd": "BMW"
  },
  {
    "model_cd": "28I",
    "model_dsc": "328i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "3",
    "model_dsc": "3.0 si",
    "make_cd": "BMW"
  },
  {
    "model_cd": "318T",
    "model_dsc": "318ti",
    "make_cd": "BMW"
  },
  {
    "model_cd": "318i",
    "model_dsc": "318i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "320",
    "model_dsc": "320i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "323I",
    "model_dsc": "323i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "325",
    "model_dsc": "325",
    "make_cd": "BMW"
  },
  {
    "model_cd": "328",
    "model_dsc": "328is",
    "make_cd": "BMW"
  },
  {
    "model_cd": "328D",
    "model_dsc": "328d",
    "make_cd": "BMW"
  },
  {
    "model_cd": "32I",
    "model_dsc": "325i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "330",
    "model_dsc": "330 SERIES",
    "make_cd": "BMW"
  },
  {
    "model_cd": "330I",
    "model_dsc": "330i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "335",
    "model_dsc": "335",
    "make_cd": "BMW"
  },
  {
    "model_cd": "335D",
    "model_dsc": "335d",
    "make_cd": "BMW"
  },
  {
    "model_cd": "335I",
    "model_dsc": "335i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "335X",
    "model_dsc": "335Xi",
    "make_cd": "BMW"
  },
  {
    "model_cd": "428I",
    "model_dsc": "428i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "430I",
    "model_dsc": "430i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "435I",
    "model_dsc": "435i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "440I",
    "model_dsc": "440i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "520",
    "model_dsc": "520",
    "make_cd": "BMW"
  },
  {
    "model_cd": "524",
    "model_dsc": "524 SERIES",
    "make_cd": "BMW"
  },
  {
    "model_cd": "525",
    "model_dsc": "525ia",
    "make_cd": "BMW"
  },
  {
    "model_cd": "525I",
    "model_dsc": "525i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "528i",
    "model_dsc": "528i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "530i",
    "model_dsc": "530i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "533i",
    "model_dsc": "533i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "535",
    "model_dsc": "535 SERIES",
    "make_cd": "BMW"
  },
  {
    "model_cd": "540",
    "model_dsc": "540",
    "make_cd": "BMW"
  },
  {
    "model_cd": "540I",
    "model_dsc": "540i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "545I",
    "model_dsc": "545i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "550",
    "model_dsc": "550",
    "make_cd": "BMW"
  },
  {
    "model_cd": "600",
    "model_dsc": "600",
    "make_cd": "BMW"
  },
  {
    "model_cd": "630",
    "model_dsc": "630csi",
    "make_cd": "BMW"
  },
  {
    "model_cd": "633",
    "model_dsc": "633csi",
    "make_cd": "BMW"
  },
  {
    "model_cd": "635",
    "model_dsc": "635 SERIES",
    "make_cd": "BMW"
  },
  {
    "model_cd": "645C",
    "model_dsc": "645ci",
    "make_cd": "BMW"
  },
  {
    "model_cd": "645I",
    "model_dsc": "645i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "650",
    "model_dsc": "650 SERIES",
    "make_cd": "BMW"
  },
  {
    "model_cd": "733",
    "model_dsc": "733 SERIES",
    "make_cd": "BMW"
  },
  {
    "model_cd": "735",
    "model_dsc": "735 SERIES",
    "make_cd": "BMW"
  },
  {
    "model_cd": "740",
    "model_dsc": "740",
    "make_cd": "BMW"
  },
  {
    "model_cd": "740i",
    "model_dsc": "740i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "745i",
    "model_dsc": "745i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "750",
    "model_dsc": "750",
    "make_cd": "BMW"
  },
  {
    "model_cd": "750I",
    "model_dsc": "750il",
    "make_cd": "BMW"
  },
  {
    "model_cd": "750L",
    "model_dsc": "750li",
    "make_cd": "BMW"
  },
  {
    "model_cd": "760I",
    "model_dsc": "760i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "760L",
    "model_dsc": "760li",
    "make_cd": "BMW"
  },
  {
    "model_cd": "840",
    "model_dsc": "840ci",
    "make_cd": "BMW"
  },
  {
    "model_cd": "850",
    "model_dsc": "850i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "850C",
    "model_dsc": "850ci",
    "make_cd": "BMW"
  },
  {
    "model_cd": "BAVA",
    "model_dsc": "BAVARIA",
    "make_cd": "BMW"
  },
  {
    "model_cd": "I3",
    "model_dsc": "I3",
    "make_cd": "BMW"
  },
  {
    "model_cd": "I8",
    "model_dsc": "I8",
    "make_cd": "BMW"
  },
  {
    "model_cd": "ISLE",
    "model_dsc": "ISETTA",
    "make_cd": "BMW"
  },
  {
    "model_cd": "L6",
    "model_dsc": "L6",
    "make_cd": "BMW"
  },
  {
    "model_cd": "L7",
    "model_dsc": "L7",
    "make_cd": "BMW"
  },
  {
    "model_cd": "M235",
    "model_dsc": "M235i",
    "make_cd": "BMW"
  },
  {
    "model_cd": "M3",
    "model_dsc": "M3",
    "make_cd": "BMW"
  },
  {
    "model_cd": "M4",
    "model_dsc": "M4",
    "make_cd": "BMW"
  },
  {
    "model_cd": "M5",
    "model_dsc": "M5",
    "make_cd": "BMW"
  },
  {
    "model_cd": "M6",
    "model_dsc": "M6",
    "make_cd": "BMW"
  },
  {
    "model_cd": "TI",
    "model_dsc": "TI",
    "make_cd": "BMW"
  },
  {
    "model_cd": "X1",
    "model_dsc": "X1",
    "make_cd": "BMW"
  },
  {
    "model_cd": "X2",
    "model_dsc": "X2",
    "make_cd": "BMW"
  },
  {
    "model_cd": "X3",
    "model_dsc": "X3",
    "make_cd": "BMW"
  },
  {
    "model_cd": "X4",
    "model_dsc": "X4",
    "make_cd": "BMW"
  },
  {
    "model_cd": "X5",
    "model_dsc": "X5",
    "make_cd": "BMW"
  },
  {
    "model_cd": "X6",
    "model_dsc": "X6",
    "make_cd": "BMW"
  },
  {
    "model_cd": "Z3",
    "model_dsc": "Z3",
    "make_cd": "BMW"
  },
  {
    "model_cd": "Z4",
    "model_dsc": "Z4",
    "make_cd": "BMW"
  },
  {
    "model_cd": "BELA",
    "model_dsc": "BEL AIR",
    "make_cd": "BORG"
  },
  {
    "model_cd": "BERE",
    "model_dsc": "BERETTA",
    "make_cd": "BORG"
  },
  {
    "model_cd": "BISC",
    "model_dsc": "BISCAYNE",
    "make_cd": "BORG"
  },
  {
    "model_cd": "HANS",
    "model_dsc": "HANSA",
    "make_cd": "BORG"
  },
  {
    "model_cd": "ISAB",
    "model_dsc": "ISABELLA",
    "make_cd": "BORG"
  },
  {
    "model_cd": "CREI",
    "model_dsc": "CREIGHTON",
    "make_cd": "BREM"
  },
  {
    "model_cd": "LAUF",
    "model_dsc": "LAUFER",
    "make_cd": "BREM"
  },
  {
    "model_cd": "MAXI",
    "model_dsc": "MAXI-TAXI",
    "make_cd": "BREM"
  },
  {
    "model_cd": "MINI",
    "model_dsc": "MINI-MARK",
    "make_cd": "BREM"
  },
  {
    "model_cd": "SEBR",
    "model_dsc": "SEBRING",
    "make_cd": "BREM"
  },
  {
    "model_cd": "E10",
    "model_dsc": "EB110",
    "make_cd": "BUGA"
  },
  {
    "model_cd": "LACR",
    "model_dsc": "LACROSSE",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "ALLU",
    "model_dsc": "ALLURE",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "APOL",
    "model_dsc": "APOLLO",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "CALI",
    "model_dsc": "CALIFORNIA",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "CENT",
    "model_dsc": "CENTURY",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "CENU",
    "model_dsc": "CENTURION",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "ELEC",
    "model_dsc": "ELECTRA (PARK AVENUE)",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "ENCL",
    "model_dsc": "ENCLAVE",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "ENCO",
    "model_dsc": "ENCORE",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "ESTA",
    "model_dsc": "ESTATE WAGON",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "G35",
    "model_dsc": "GS350",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "G40",
    "model_dsc": "GS400",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "G45",
    "model_dsc": "GS455",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "GRAN",
    "model_dsc": "GRAND SPORTS (G.S.)",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "INVI",
    "model_dsc": "INVICTA",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "LESA",
    "model_dsc": "LE SABRE",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "LIMI",
    "model_dsc": "LIMITED",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "PARK",
    "model_dsc": "PARK AVENUE",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "RAIN",
    "model_dsc": "RAINIER",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "REAT",
    "model_dsc": "REATTA",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "REGA",
    "model_dsc": "REGAL",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "REND",
    "model_dsc": "RENDEZVOUS",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "RIVI",
    "model_dsc": "RIVIERA",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "ROAD",
    "model_dsc": "ROADMASTER",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "SKYH",
    "model_dsc": "SKYHAWK",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "SKYL",
    "model_dsc": "SKYLARK",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "SOME",
    "model_dsc": "SOMERSET",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "SPEC",
    "model_dsc": "SPECIAL",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "SPOR",
    "model_dsc": "SPORTSWAGON",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "SUPE",
    "model_dsc": "SUPER",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "TERR",
    "model_dsc": "TERRAZA",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "VERA",
    "model_dsc": "VERANO",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "WILD",
    "model_dsc": "WILDCAT",
    "make_cd": "BUIC"
  },
  {
    "model_cd": "CADI",
    "model_dsc": "CADILLAC",
    "make_cd": "BZEL"
  },
  {
    "model_cd": "ELEC",
    "model_dsc": "ELECTRA-KING",
    "make_cd": "BZEL"
  },
  {
    "model_cd": "60",
    "model_dsc": "60 SERIES",
    "make_cd": "CADI"
  },
  {
    "model_cd": "61",
    "model_dsc": "61 SERIES",
    "make_cd": "CADI"
  },
  {
    "model_cd": "62",
    "model_dsc": "62 SERIES",
    "make_cd": "CADI"
  },
  {
    "model_cd": "75",
    "model_dsc": "75 SERIES",
    "make_cd": "CADI"
  },
  {
    "model_cd": "ALLA",
    "model_dsc": "ALLANTE",
    "make_cd": "CADI"
  },
  {
    "model_cd": "ATS",
    "model_dsc": "ATS",
    "make_cd": "CADI"
  },
  {
    "model_cd": "BROU",
    "model_dsc": "BROUGHAM",
    "make_cd": "CADI"
  },
  {
    "model_cd": "CALA",
    "model_dsc": "CALAIS",
    "make_cd": "CADI"
  },
  {
    "model_cd": "CATE",
    "model_dsc": "CATERA",
    "make_cd": "CADI"
  },
  {
    "model_cd": "CIMA",
    "model_dsc": "CIMARRON",
    "make_cd": "CADI"
  },
  {
    "model_cd": "CONC",
    "model_dsc": "CONCOURS",
    "make_cd": "CADI"
  },
  {
    "model_cd": "CTS",
    "model_dsc": "CTS",
    "make_cd": "CADI"
  },
  {
    "model_cd": "DEVI",
    "model_dsc": "DEVILLE",
    "make_cd": "CADI"
  },
  {
    "model_cd": "ELDO",
    "model_dsc": "ELDORADO",
    "make_cd": "CADI"
  },
  {
    "model_cd": "ESCA",
    "model_dsc": "ESCALADE",
    "make_cd": "CADI"
  },
  {
    "model_cd": "ESV",
    "model_dsc": "ESV",
    "make_cd": "CADI"
  },
  {
    "model_cd": "EXT",
    "model_dsc": "EXT",
    "make_cd": "CADI"
  },
  {
    "model_cd": "FLEE",
    "model_dsc": "FLEETWOOD",
    "make_cd": "CADI"
  },
  {
    "model_cd": "SEVI",
    "model_dsc": "SEVILLE",
    "make_cd": "CADI"
  },
  {
    "model_cd": "SRX",
    "model_dsc": "SRX",
    "make_cd": "CADI"
  },
  {
    "model_cd": "STS",
    "model_dsc": "STS",
    "make_cd": "CADI"
  },
  {
    "model_cd": "TOUR",
    "model_dsc": "TOURING SEDAN",
    "make_cd": "CADI"
  },
  {
    "model_cd": "XLR",
    "model_dsc": "XLR",
    "make_cd": "CADI"
  },
  {
    "model_cd": "XT5",
    "model_dsc": "XT5",
    "make_cd": "CADI"
  },
  {
    "model_cd": "DTS",
    "model_dsc": "DTS",
    "make_cd": "CADI"
  },
  {
    "model_cd": "UTTR",
    "model_dsc": "UTILITY TRAILER",
    "make_cd": "CBTR"
  },
  {
    "model_cd": "LATR",
    "model_dsc": "LANDSCAPE TRAILER",
    "make_cd": "CBTR"
  },
  {
    "model_cd": "FLTR",
    "model_dsc": "FLAT TRAILER",
    "make_cd": "CBTR"
  },
  {
    "model_cd": "TILT",
    "model_dsc": "TILT TRAILER",
    "make_cd": "CBTR"
  },
  {
    "model_cd": "PITR",
    "model_dsc": "PINTLE PULL TRAILER",
    "make_cd": "CBTR"
  },
  {
    "model_cd": "GOTR",
    "model_dsc": "GOOSENECK TRAILER",
    "make_cd": "CBTR"
  },
  {
    "model_cd": "DUTR",
    "model_dsc": "DUMP TRAILER",
    "make_cd": "CBTR"
  },
  {
    "model_cd": "AERO",
    "model_dsc": "AEROBUS",
    "make_cd": "CHEC"
  },
  {
    "model_cd": "CUST",
    "model_dsc": "CUSTOM",
    "make_cd": "CHEC"
  },
  {
    "model_cd": "MARA",
    "model_dsc": "MARATHON",
    "make_cd": "CHEC"
  },
  {
    "model_cd": "SUPE",
    "model_dsc": "SUPERBA",
    "make_cd": "CHEC"
  },
  {
    "model_cd": "210",
    "model_dsc": "210 SERIES",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "300",
    "model_dsc": "300 DELUXE",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "ASTR",
    "model_dsc": "ASTRO VAN",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "AVAL",
    "model_dsc": "AVALANCHE",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "AVEO",
    "model_dsc": "AVEO",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "BELA",
    "model_dsc": "BEL AIR",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "BERE",
    "model_dsc": "BERETTA",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "BISC",
    "model_dsc": "BISCAYNE",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "BLAZ",
    "model_dsc": "BLAZER",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "BOLT",
    "model_dsc": "BOLT",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "BROO",
    "model_dsc": "BROOKWOOD",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "C10",
    "model_dsc": "C10",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "C15",
    "model_dsc": "C/K 1500",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "C25",
    "model_dsc": "C/K 2500",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "C35",
    "model_dsc": "C/K 3500",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CAMA",
    "model_dsc": "CAMARO",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CAPR",
    "model_dsc": "CAPRICE",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CAPT",
    "model_dsc": "CAPTIVA",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CAVA",
    "model_dsc": "CAVALIER",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CELE",
    "model_dsc": "CELEBRITY",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CHED",
    "model_dsc": "DELUXE (CHEVELLE)",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CHEG",
    "model_dsc": "GREENBRIER (CHEVELLE)",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CHEN",
    "model_dsc": "NOMAD (CHEVELLE)",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CHET",
    "model_dsc": "CHEVETTE",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CHEV",
    "model_dsc": "CHEVELLE",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CHEY",
    "model_dsc": "CHEVY II",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CITA",
    "model_dsc": "CITATION",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CITY",
    "model_dsc": "CITY EXPRESS",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "COBA",
    "model_dsc": "COBALT",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "COLO",
    "model_dsc": "COLORADO",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CONC",
    "model_dsc": "CONCOURS",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CORR",
    "model_dsc": "CORVAIR",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CORS",
    "model_dsc": "CORSICA",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CORV",
    "model_dsc": "CORVETTE",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "CRUZ",
    "model_dsc": "CRUZE",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "DELR",
    "model_dsc": "DEL RAY",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "ELCA",
    "model_dsc": "EL CAMINO",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "EPIC",
    "model_dsc": "EPICA",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "EQUI",
    "model_dsc": "EQUINOX",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "EST",
    "model_dsc": "ESTATE WAGON",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "EXP",
    "model_dsc": "EXPRESS",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "FLE",
    "model_dsc": "FLEETLINE",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "HHR",
    "model_dsc": "HHR",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "IMPA",
    "model_dsc": "IMPALA",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "KIN",
    "model_dsc": "KINGSWOOD",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "LUMA",
    "model_dsc": "LUMINA APV",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "LUMI",
    "model_dsc": "LUMINA",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "LUV",
    "model_dsc": "LUV",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "MALI",
    "model_dsc": "MALIBU",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "METR",
    "model_dsc": "METRO",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "MONT",
    "model_dsc": "MONTE CARLO",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "MONZ",
    "model_dsc": "MONZA",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "NOVA",
    "model_dsc": "NOVA (CHEVY II & CONCOURS)",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "OPTR",
    "model_dsc": "OPTRA",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "PARK",
    "model_dsc": "PARKWOOD",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "PRIS",
    "model_dsc": "PRISM",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "S10",
    "model_dsc": "S10",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "SILV",
    "model_dsc": "SILVERADO",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "SONI",
    "model_dsc": "SONIC",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "SPEC",
    "model_dsc": "SPECTRUM",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "SPOR",
    "model_dsc": "SPORTVAN",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "SPRI",
    "model_dsc": "SPRINT",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "SPRK",
    "model_dsc": "SPARK",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "SSR",
    "model_dsc": "SSR",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "STM",
    "model_dsc": "STYLE MASTER",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "STY",
    "model_dsc": "STYLE LINE",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "SUBU",
    "model_dsc": "SUBURBAN",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "TAHO",
    "model_dsc": "TAHOE",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "TOWN",
    "model_dsc": "TOWNSMAN",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "TRAC",
    "model_dsc": "TRACKER",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "TRAI",
    "model_dsc": "TRAILBLAZER",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "TRAV",
    "model_dsc": "TRAVERSE",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "TRAX",
    "model_dsc": "TRAX",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "UPLA",
    "model_dsc": "UPLANDER",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "VEGA",
    "model_dsc": "VEGA",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "VENT",
    "model_dsc": "VENTURE",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "VOLT",
    "model_dsc": "VOLT",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "G30",
    "model_dsc": "G30",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "OPT5",
    "model_dsc": "OPTRA5",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "ORLA",
    "model_dsc": "ORLANDO",
    "make_cd": "CHEV"
  },
  {
    "model_cd": "200",
    "model_dsc": "200",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "300",
    "model_dsc": "300",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "300C",
    "model_dsc": "300C",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "CIRR",
    "model_dsc": "CIRRUS",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "COMM",
    "model_dsc": "COMMANDER",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "CONC",
    "model_dsc": "CONCORDE",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "CONQ",
    "model_dsc": "CONQUEST",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "CORD",
    "model_dsc": "CORDOBA",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "CROS",
    "model_dsc": "CROSSFIRE",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "DAYT",
    "model_dsc": "DAYTONA",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "DYNA",
    "model_dsc": "DYNASTY",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "ECL",
    "model_dsc": "E CLASS",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "EXE",
    "model_dsc": "EXECUTIVE SEDAN",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "IMPE",
    "model_dsc": "IMPERIAL",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "INTR",
    "model_dsc": "INTREPID",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "LASE",
    "model_dsc": "LASER",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "LEBA",
    "model_dsc": "LEBARON",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "LHS",
    "model_dsc": "LHS",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "LID",
    "model_dsc": "LIDO",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "LIMO",
    "model_dsc": "LIMOUSINE",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "NEON",
    "model_dsc": "NEON",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "NEW5",
    "model_dsc": "FIFTH AVENUE",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "NEWP",
    "model_dsc": "NEWPORT",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "NEWT",
    "model_dsc": "TOWN & COUNTRY",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "NEWY",
    "model_dsc": "NEW YORKER",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "PACI",
    "model_dsc": "PACIFICA",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "PROW",
    "model_dsc": "PROWLER",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "PTCR",
    "model_dsc": "PT CRUISER",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "ROYA",
    "model_dsc": "ROYAL",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "SAL",
    "model_dsc": "SALON",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "SARA",
    "model_dsc": "SARATOGA",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "SEBR",
    "model_dsc": "SEBRING",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "TC",
    "model_dsc": "TC",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "TNC",
    "model_dsc": "TOWN AND COUNTRY MINIVAN",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "WIN",
    "model_dsc": "WINDSOR",
    "make_cd": "CHRY"
  },
  {
    "model_cd": "2CV",
    "model_dsc": "2CV",
    "make_cd": "CITR"
  },
  {
    "model_cd": "AM6",
    "model_dsc": "AM16",
    "make_cd": "CITR"
  },
  {
    "model_cd": "AX",
    "model_dsc": "AX",
    "make_cd": "CITR"
  },
  {
    "model_cd": "D19",
    "model_dsc": "DS-19",
    "make_cd": "CITR"
  },
  {
    "model_cd": "D21",
    "model_dsc": "DS-21 & D21",
    "make_cd": "CITR"
  },
  {
    "model_cd": "ID9",
    "model_dsc": "ID-19",
    "make_cd": "CITR"
  },
  {
    "model_cd": "SM",
    "model_dsc": "SM",
    "make_cd": "CITR"
  },
  {
    "model_cd": "ROA",
    "model_dsc": "ROADSTER",
    "make_cd": "CLEN"
  },
  {
    "model_cd": "COM",
    "model_dsc": "COMUTA-CAR",
    "make_cd": "COMV"
  },
  {
    "model_cd": "MINI",
    "model_dsc": "MINI",
    "make_cd": "#N/A"
  },
  {
    "model_cd": "LAN",
    "model_dsc": "LANOS",
    "make_cd": "DAEW"
  },
  {
    "model_cd": "LEG",
    "model_dsc": "LEGANZA",
    "make_cd": "DAEW"
  },
  {
    "model_cd": "NUB",
    "model_dsc": "NUBIRA",
    "make_cd": "DAEW"
  },
  {
    "model_cd": "CHA",
    "model_dsc": "CHARADE",
    "make_cd": "DAIH"
  },
  {
    "model_cd": "RKY",
    "model_dsc": "ROCKY",
    "make_cd": "DAIH"
  },
  {
    "model_cd": "110",
    "model_dsc": "110",
    "make_cd": "DATS"
  },
  {
    "model_cd": "120",
    "model_dsc": "1200",
    "make_cd": "DATS"
  },
  {
    "model_cd": "200S",
    "model_dsc": "200SX",
    "make_cd": "DATS"
  },
  {
    "model_cd": "210",
    "model_dsc": "210 (or B-210)",
    "make_cd": "DATS"
  },
  {
    "model_cd": "240Z",
    "model_dsc": "240Z",
    "make_cd": "DATS"
  },
  {
    "model_cd": "260Z",
    "model_dsc": "260Z",
    "make_cd": "DATS"
  },
  {
    "model_cd": "280X",
    "model_dsc": "280ZX",
    "make_cd": "DATS"
  },
  {
    "model_cd": "280Z",
    "model_dsc": "280Z",
    "make_cd": "DATS"
  },
  {
    "model_cd": "310",
    "model_dsc": "310",
    "make_cd": "DATS"
  },
  {
    "model_cd": "311",
    "model_dsc": "311",
    "make_cd": "DATS"
  },
  {
    "model_cd": "510",
    "model_dsc": "510",
    "make_cd": "DATS"
  },
  {
    "model_cd": "610",
    "model_dsc": "610",
    "make_cd": "DATS"
  },
  {
    "model_cd": "710",
    "model_dsc": "710",
    "make_cd": "DATS"
  },
  {
    "model_cd": "810",
    "model_dsc": "810",
    "make_cd": "DATS"
  },
  {
    "model_cd": "B210",
    "model_dsc": "B-210 (or 210)",
    "make_cd": "DATS"
  },
  {
    "model_cd": "F10",
    "model_dsc": "F-10",
    "make_cd": "DATS"
  },
  {
    "model_cd": "HON",
    "model_dsc": "HONEY BEE",
    "make_cd": "DATS"
  },
  {
    "model_cd": "LIL",
    "model_dsc": "LIL HUSTLER",
    "make_cd": "DATS"
  },
  {
    "model_cd": "MAXI",
    "model_dsc": "MAXIMA",
    "make_cd": "DATS"
  },
  {
    "model_cd": "MIG",
    "model_dsc": "MIGI",
    "make_cd": "DAYT"
  },
  {
    "model_cd": "MOY",
    "model_dsc": "MOYA",
    "make_cd": "DAYT"
  },
  {
    "model_cd": "ROA",
    "model_dsc": "ROADSTER",
    "make_cd": "DECO"
  },
  {
    "model_cd": "ADV",
    "model_dsc": "ADVENTURER",
    "make_cd": "DESO"
  },
  {
    "model_cd": "CUS",
    "model_dsc": "CUSTOM",
    "make_cd": "DESO"
  },
  {
    "model_cd": "DEL",
    "model_dsc": "DELUXE",
    "make_cd": "DESO"
  },
  {
    "model_cd": "FRD",
    "model_dsc": "FIREDOM",
    "make_cd": "DESO"
  },
  {
    "model_cd": "FRF",
    "model_dsc": "FIRELITE",
    "make_cd": "DESO"
  },
  {
    "model_cd": "FRS",
    "model_dsc": "FIRESWEEP",
    "make_cd": "DESO"
  },
  {
    "model_cd": "POW",
    "model_dsc": "POWERMASTER",
    "make_cd": "DESO"
  },
  {
    "model_cd": "DEA",
    "model_dsc": "DEAUVILLE",
    "make_cd": "DETO"
  },
  {
    "model_cd": "LON",
    "model_dsc": "LONGCHAMP",
    "make_cd": "DETO"
  },
  {
    "model_cd": "MNA",
    "model_dsc": "MANGUSTA",
    "make_cd": "DETO"
  },
  {
    "model_cd": "PTA",
    "model_dsc": "PANTERA",
    "make_cd": "DETO"
  },
  {
    "model_cd": "102",
    "model_dsc": "F102",
    "make_cd": "DKW"
  },
  {
    "model_cd": "AUD",
    "model_dsc": "AUDI",
    "make_cd": "DKW"
  },
  {
    "model_cd": "VEM",
    "model_dsc": "VEMAG",
    "make_cd": "DKW"
  },
  {
    "model_cd": "100",
    "model_dsc": "A 100 COMPACT",
    "make_cd": "DODG"
  },
  {
    "model_cd": "2000",
    "model_dsc": "2000",
    "make_cd": "DODG"
  },
  {
    "model_cd": "330",
    "model_dsc": "330 SERIES",
    "make_cd": "DODG"
  },
  {
    "model_cd": "400",
    "model_dsc": "400 SERIES",
    "make_cd": "DODG"
  },
  {
    "model_cd": "440",
    "model_dsc": "440 SERIES",
    "make_cd": "DODG"
  },
  {
    "model_cd": "600",
    "model_dsc": "600",
    "make_cd": "DODG"
  },
  {
    "model_cd": "880",
    "model_dsc": "880 SERIES",
    "make_cd": "DODG"
  },
  {
    "model_cd": "ARIE",
    "model_dsc": "ARIES",
    "make_cd": "DODG"
  },
  {
    "model_cd": "ASPE",
    "model_dsc": "ASPEN",
    "make_cd": "DODG"
  },
  {
    "model_cd": "AVEN",
    "model_dsc": "AVENGER",
    "make_cd": "DODG"
  },
  {
    "model_cd": "CALI",
    "model_dsc": "CALIBER",
    "make_cd": "DODG"
  },
  {
    "model_cd": "CARA",
    "model_dsc": "CARAVAN",
    "make_cd": "DODG"
  },
  {
    "model_cd": "CHAL",
    "model_dsc": "CHALLENGER",
    "make_cd": "DODG"
  },
  {
    "model_cd": "CHAR",
    "model_dsc": "CHARGER",
    "make_cd": "DODG"
  },
  {
    "model_cd": "COLT",
    "model_dsc": "COLT",
    "make_cd": "DODG"
  },
  {
    "model_cd": "COM",
    "model_dsc": "COMPACT SPORTSMAN",
    "make_cd": "DODG"
  },
  {
    "model_cd": "CONQ",
    "model_dsc": "CONQUEST",
    "make_cd": "DODG"
  },
  {
    "model_cd": "CORO",
    "model_dsc": "CORONET",
    "make_cd": "DODG"
  },
  {
    "model_cd": "D150",
    "model_dsc": "RAM 1500 PU",
    "make_cd": "DODG"
  },
  {
    "model_cd": "D250",
    "model_dsc": "RAM 2500 PU",
    "make_cd": "DODG"
  },
  {
    "model_cd": "D350",
    "model_dsc": "RAM 3500 PU",
    "make_cd": "DODG"
  },
  {
    "model_cd": "DAKO",
    "model_dsc": "DAKOTA",
    "make_cd": "DODG"
  },
  {
    "model_cd": "DART",
    "model_dsc": "DART",
    "make_cd": "DODG"
  },
  {
    "model_cd": "DAYT",
    "model_dsc": "DAYTONA",
    "make_cd": "DODG"
  },
  {
    "model_cd": "DEL",
    "model_dsc": "DELUXE",
    "make_cd": "DODG"
  },
  {
    "model_cd": "DEM",
    "model_dsc": "DEMON",
    "make_cd": "DODG"
  },
  {
    "model_cd": "DIPL",
    "model_dsc": "DIPLOMAT",
    "make_cd": "DODG"
  },
  {
    "model_cd": "DURA",
    "model_dsc": "DURANGO",
    "make_cd": "DODG"
  },
  {
    "model_cd": "DYNA",
    "model_dsc": "DYNASTY",
    "make_cd": "DODG"
  },
  {
    "model_cd": "FLS",
    "model_dsc": "FLEET SPECIAL",
    "make_cd": "DODG"
  },
  {
    "model_cd": "GRAN",
    "model_dsc": "GRAND CARAVAN",
    "make_cd": "DODG"
  },
  {
    "model_cd": "INTR",
    "model_dsc": "INTREPID",
    "make_cd": "DODG"
  },
  {
    "model_cd": "JOUR",
    "model_dsc": "JOURNEY",
    "make_cd": "DODG"
  },
  {
    "model_cd": "LANC",
    "model_dsc": "LANCER",
    "make_cd": "DODG"
  },
  {
    "model_cd": "MAGN",
    "model_dsc": "MAGNUM",
    "make_cd": "DODG"
  },
  {
    "model_cd": "MEAD",
    "model_dsc": "MEADOWBROOK",
    "make_cd": "DODG"
  },
  {
    "model_cd": "MIRA",
    "model_dsc": "MIRADA",
    "make_cd": "DODG"
  },
  {
    "model_cd": "MONA",
    "model_dsc": "MONACO",
    "make_cd": "DODG"
  },
  {
    "model_cd": "NEON",
    "model_dsc": "NEON",
    "make_cd": "DODG"
  },
  {
    "model_cd": "NITR",
    "model_dsc": "NITRO",
    "make_cd": "DODG"
  },
  {
    "model_cd": "OMNI",
    "model_dsc": "OMNI (ALSO 024)",
    "make_cd": "DODG"
  },
  {
    "model_cd": "PHOE",
    "model_dsc": "PHOENIX",
    "make_cd": "DODG"
  },
  {
    "model_cd": "PION",
    "model_dsc": "PIONEER",
    "make_cd": "DODG"
  },
  {
    "model_cd": "POLA",
    "model_dsc": "POLARA",
    "make_cd": "DODG"
  },
  {
    "model_cd": "PRM",
    "model_dsc": "POWER RAM",
    "make_cd": "DODG"
  },
  {
    "model_cd": "RAID",
    "model_dsc": "RAIDER",
    "make_cd": "DODG"
  },
  {
    "model_cd": "RCH",
    "model_dsc": "RAM CHARGER",
    "make_cd": "DODG"
  },
  {
    "model_cd": "ROYA",
    "model_dsc": "ROYAL",
    "make_cd": "DODG"
  },
  {
    "model_cd": "SENE",
    "model_dsc": "SENECA",
    "make_cd": "DODG"
  },
  {
    "model_cd": "SHAD",
    "model_dsc": "SHADOW",
    "make_cd": "DODG"
  },
  {
    "model_cd": "SPIR",
    "model_dsc": "SPIRIT",
    "make_cd": "DODG"
  },
  {
    "model_cd": "SPRI",
    "model_dsc": "SPRINT",
    "make_cd": "DODG"
  },
  {
    "model_cd": "SPRT",
    "model_dsc": "SPRINTER",
    "make_cd": "DODG"
  },
  {
    "model_cd": "SRT4",
    "model_dsc": "SRT4",
    "make_cd": "DODG"
  },
  {
    "model_cd": "STEA",
    "model_dsc": "STEALTH",
    "make_cd": "DODG"
  },
  {
    "model_cd": "STR",
    "model_dsc": "ST. REGIS",
    "make_cd": "DODG"
  },
  {
    "model_cd": "STRA",
    "model_dsc": "STRATUS",
    "make_cd": "DODG"
  },
  {
    "model_cd": "SX",
    "model_dsc": "SX",
    "make_cd": "DODG"
  },
  {
    "model_cd": "SX2",
    "model_dsc": "SX2.0",
    "make_cd": "DODG"
  },
  {
    "model_cd": "V15",
    "model_dsc": "RAM 1500 VAN",
    "make_cd": "DODG"
  },
  {
    "model_cd": "V25",
    "model_dsc": "RAM 2500 VAN",
    "make_cd": "DODG"
  },
  {
    "model_cd": "V35",
    "model_dsc": "RAM 3500 VAN",
    "make_cd": "DODG"
  },
  {
    "model_cd": "VIPE",
    "model_dsc": "VIPER",
    "make_cd": "DODG"
  },
  {
    "model_cd": "WAY",
    "model_dsc": "WAYFARER",
    "make_cd": "DODG"
  },
  {
    "model_cd": "W250",
    "model_dsc": "W250",
    "make_cd": "DODG"
  },
  {
    "model_cd": "AERO",
    "model_dsc": "AEROLITE",
    "make_cd": "DUTC"
  },
  {
    "model_cd": "ASPE",
    "model_dsc": "ASPEN TRAIL",
    "make_cd": "DUTC"
  },
  {
    "model_cd": "BAYR",
    "model_dsc": "BAYRIDGE",
    "make_cd": "DUTC"
  },
  {
    "model_cd": "BREC",
    "model_dsc": "BRECKENRIDGE",
    "make_cd": "DUTC"
  },
  {
    "model_cd": "COLE",
    "model_dsc": "COLEMAN",
    "make_cd": "DUTC"
  },
  {
    "model_cd": "DENA",
    "model_dsc": "DENALI",
    "make_cd": "DUTC"
  },
  {
    "model_cd": "DUTC",
    "model_dsc": "DUTCHMAN",
    "make_cd": "DUTC"
  },
  {
    "model_cd": "INFI",
    "model_dsc": "INFINITY",
    "make_cd": "DUTC"
  },
  {
    "model_cd": "KODI",
    "model_dsc": "KODIAK",
    "make_cd": "DUTC"
  },
  {
    "model_cd": "KOMF",
    "model_dsc": "KOMFORT",
    "make_cd": "DUTC"
  },
  {
    "model_cd": "RUBI",
    "model_dsc": "RUBICON",
    "make_cd": "DUTC"
  },
  {
    "model_cd": "VOLT",
    "model_dsc": "VOLTAGE",
    "make_cd": "DUTC"
  },
  {
    "model_cd": "MEDA",
    "model_dsc": "MEDALLION",
    "make_cd": "EAGL"
  },
  {
    "model_cd": "PRE",
    "model_dsc": "PREMIER",
    "make_cd": "EAGL"
  },
  {
    "model_cd": "SUM",
    "model_dsc": "SUMMIT",
    "make_cd": "EAGL"
  },
  {
    "model_cd": "TALO",
    "model_dsc": "TALON",
    "make_cd": "EAGL"
  },
  {
    "model_cd": "VISI",
    "model_dsc": "VISION",
    "make_cd": "EAGL"
  },
  {
    "model_cd": "CITA",
    "model_dsc": "CITATION",
    "make_cd": "EDSE"
  },
  {
    "model_cd": "CORS",
    "model_dsc": "CORSAIR",
    "make_cd": "EDSE"
  },
  {
    "model_cd": "PACE",
    "model_dsc": "PACER",
    "make_cd": "EDSE"
  },
  {
    "model_cd": "RANG",
    "model_dsc": "RANGER",
    "make_cd": "EDSE"
  },
  {
    "model_cd": "VILL",
    "model_dsc": "VILLAGER",
    "make_cd": "EDSE"
  },
  {
    "model_cd": "100",
    "model_dsc": "100 E SERIES",
    "make_cd": "ENGF"
  },
  {
    "model_cd": "105",
    "model_dsc": "105 E SERIES",
    "make_cd": "ENGF"
  },
  {
    "model_cd": "ANG",
    "model_dsc": "ANGLIA",
    "make_cd": "ENGF"
  },
  {
    "model_cd": "CAPR",
    "model_dsc": "CAPRI",
    "make_cd": "ENGF"
  },
  {
    "model_cd": "CONS",
    "model_dsc": "CONSUL",
    "make_cd": "ENGF"
  },
  {
    "model_cd": "CORS",
    "model_dsc": "CORSAIR",
    "make_cd": "ENGF"
  },
  {
    "model_cd": "CORT",
    "model_dsc": "CORTINA",
    "make_cd": "ENGF"
  },
  {
    "model_cd": "ESCO",
    "model_dsc": "ESCORT",
    "make_cd": "ENGF"
  },
  {
    "model_cd": "GT",
    "model_dsc": "GT",
    "make_cd": "ENGF"
  },
  {
    "model_cd": "LOTU",
    "model_dsc": "LOTUS",
    "make_cd": "ENGF"
  },
  {
    "model_cd": "MK2",
    "model_dsc": "MARK II",
    "make_cd": "ENGF"
  },
  {
    "model_cd": "PER",
    "model_dsc": "PERFECT",
    "make_cd": "ENGF"
  },
  {
    "model_cd": "SQU",
    "model_dsc": "SQUIRE",
    "make_cd": "ENGF"
  },
  {
    "model_cd": "THA",
    "model_dsc": "THAMES",
    "make_cd": "ENGF"
  },
  {
    "model_cd": "ZEPH",
    "model_dsc": "ZEPHYR",
    "make_cd": "ENGF"
  },
  {
    "model_cd": "ZODI",
    "model_dsc": "ZODIAC",
    "make_cd": "ENGF"
  },
  {
    "model_cd": "EPI",
    "model_dsc": "EPIC",
    "make_cd": "ENVO"
  },
  {
    "model_cd": "COBR",
    "model_dsc": "COBRA",
    "make_cd": "EXCA"
  },
  {
    "model_cd": "JAC",
    "model_dsc": "JAC 427 COBRA",
    "make_cd": "EXCA"
  },
  {
    "model_cd": "SSK",
    "model_dsc": "SSK",
    "make_cd": "EXCA"
  },
  {
    "model_cd": "SSP",
    "model_dsc": "SS PHAETON",
    "make_cd": "EXCA"
  },
  {
    "model_cd": "SSR",
    "model_dsc": "SS ROADSTER",
    "make_cd": "EXCA"
  },
  {
    "model_cd": "500",
    "model_dsc": "HK500",
    "make_cd": "FACE"
  },
  {
    "model_cd": "EXE",
    "model_dsc": "EXCELLENCE",
    "make_cd": "FACE"
  },
  {
    "model_cd": "FACE",
    "model_dsc": "FACELLIA",
    "make_cd": "FACE"
  },
  {
    "model_cd": "FII",
    "model_dsc": "FACEL II",
    "make_cd": "FACE"
  },
  {
    "model_cd": "FIII",
    "model_dsc": "FACEL III",
    "make_cd": "FACE"
  },
  {
    "model_cd": "FV",
    "model_dsc": "FV",
    "make_cd": "FACE"
  },
  {
    "model_cd": "456",
    "model_dsc": "456GT",
    "make_cd": "FERR"
  },
  {
    "model_cd": "458",
    "model_dsc": "458",
    "make_cd": "FERR"
  },
  {
    "model_cd": "512",
    "model_dsc": "512",
    "make_cd": "FERR"
  },
  {
    "model_cd": "BAR",
    "model_dsc": "BARCHETTA (OR F130)",
    "make_cd": "FERR"
  },
  {
    "model_cd": "DAYT",
    "model_dsc": "DAYTONA",
    "make_cd": "FERR"
  },
  {
    "model_cd": "F35",
    "model_dsc": "F355",
    "make_cd": "FERR"
  },
  {
    "model_cd": "F40",
    "model_dsc": "F40",
    "make_cd": "FERR"
  },
  {
    "model_cd": "F430",
    "model_dsc": "F430",
    "make_cd": "FERR"
  },
  {
    "model_cd": "MAR",
    "model_dsc": "F-550 MARANELLO",
    "make_cd": "FERR"
  },
  {
    "model_cd": "MON",
    "model_dsc": "MONDIAL",
    "make_cd": "FERR"
  },
  {
    "model_cd": "QUA",
    "model_dsc": "QUATTROVALVOLVE",
    "make_cd": "FERR"
  },
  {
    "model_cd": "TEST",
    "model_dsc": "TESTAROSSA",
    "make_cd": "FERR"
  },
  {
    "model_cd": "TIP",
    "model_dsc": "TIPO",
    "make_cd": "FERR"
  },
  {
    "model_cd": "F12B",
    "model_dsc": "F12 BERLINETTA",
    "make_cd": "FERR"
  },
  {
    "model_cd": "206",
    "model_dsc": "206",
    "make_cd": "FERR"
  },
  {
    "model_cd": "208",
    "model_dsc": "208",
    "make_cd": "FERR"
  },
  {
    "model_cd": "308",
    "model_dsc": "308",
    "make_cd": "FERR"
  },
  {
    "model_cd": "328",
    "model_dsc": "328",
    "make_cd": "FERR"
  },
  {
    "model_cd": "348",
    "model_dsc": "348",
    "make_cd": "FERR"
  },
  {
    "model_cd": "500",
    "model_dsc": "500",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "110",
    "model_dsc": "1100 - D or R",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "120",
    "model_dsc": "1200",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "124",
    "model_dsc": "124 SERIES",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "128",
    "model_dsc": "128 SERIES",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "131",
    "model_dsc": "131 SERIES",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "150",
    "model_dsc": "1500",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "600",
    "model_dsc": "600D",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "750",
    "model_dsc": "750",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "85F",
    "model_dsc": "850 FASTBACK",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "BRAV",
    "model_dsc": "BRAVA",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "PUNT",
    "model_dsc": "PUNTO",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "RIM",
    "model_dsc": "RIMTO",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "SPYD",
    "model_dsc": "SPIDER SERIES",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "STRA",
    "model_dsc": "STRADA",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "UNO",
    "model_dsc": "UNO",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "X19",
    "model_dsc": "X19",
    "make_cd": "FIAT"
  },
  {
    "model_cd": "KARM",
    "model_dsc": "KARMA",
    "make_cd": "FISK"
  },
  {
    "model_cd": "TERR",
    "model_dsc": "TERRY",
    "make_cd": "FLEE"
  },
  {
    "model_cd": "BUS",
    "model_dsc": "BUS",
    "make_cd": "FLYE"
  },
  {
    "model_cd": "300",
    "model_dsc": "300 SERIES",
    "make_cd": "FORD"
  },
  {
    "model_cd": "7LR",
    "model_dsc": "7 LITRE",
    "make_cd": "FORD"
  },
  {
    "model_cd": "AERO",
    "model_dsc": "AEROSTAR",
    "make_cd": "FORD"
  },
  {
    "model_cd": "ASPI",
    "model_dsc": "ASPIRE",
    "make_cd": "FORD"
  },
  {
    "model_cd": "BRON",
    "model_dsc": "BRONCO/BRONCO II",
    "make_cd": "FORD"
  },
  {
    "model_cd": "COBR",
    "model_dsc": "COBRA",
    "make_cd": "FORD"
  },
  {
    "model_cd": "CONT",
    "model_dsc": "CONTOUR",
    "make_cd": "FORD"
  },
  {
    "model_cd": "COQ",
    "model_dsc": "COUNTRY SQUIRE",
    "make_cd": "FORD"
  },
  {
    "model_cd": "COY",
    "model_dsc": "COUNTRY SEDAN",
    "make_cd": "FORD"
  },
  {
    "model_cd": "CRE",
    "model_dsc": "CRESTLINE",
    "make_cd": "FORD"
  },
  {
    "model_cd": "CROW",
    "model_dsc": "VICTORIA",
    "make_cd": "FORD"
  },
  {
    "model_cd": "CST",
    "model_dsc": "CUSTOMLINE",
    "make_cd": "FORD"
  },
  {
    "model_cd": "CUS",
    "model_dsc": "CUSTOM",
    "make_cd": "FORD"
  },
  {
    "model_cd": "CW1",
    "model_dsc": "CLUB WAGON E150",
    "make_cd": "FORD"
  },
  {
    "model_cd": "CW2",
    "model_dsc": "CLUB WAGON E250",
    "make_cd": "FORD"
  },
  {
    "model_cd": "CW3",
    "model_dsc": "CLUB WAGON E350",
    "make_cd": "FORD"
  },
  {
    "model_cd": "DEL",
    "model_dsc": "DELUXE",
    "make_cd": "FORD"
  },
  {
    "model_cd": "E100",
    "model_dsc": "ECONOLINE 100",
    "make_cd": "FORD"
  },
  {
    "model_cd": "E150",
    "model_dsc": "ECONOLINE E150",
    "make_cd": "FORD"
  },
  {
    "model_cd": "E250",
    "model_dsc": "ECONOLINE E250",
    "make_cd": "FORD"
  },
  {
    "model_cd": "E350",
    "model_dsc": "ECONOLINE E350",
    "make_cd": "FORD"
  },
  {
    "model_cd": "ECON",
    "model_dsc": "ECONOLINE SERIES",
    "make_cd": "FORD"
  },
  {
    "model_cd": "EDGE",
    "model_dsc": "EDGE",
    "make_cd": "FORD"
  },
  {
    "model_cd": "ELIT",
    "model_dsc": "ELITE",
    "make_cd": "FORD"
  },
  {
    "model_cd": "ESCA",
    "model_dsc": "ESCAPE",
    "make_cd": "FORD"
  },
  {
    "model_cd": "ESCO",
    "model_dsc": "ESCORT",
    "make_cd": "FORD"
  },
  {
    "model_cd": "EXCU",
    "model_dsc": "EXCURSION",
    "make_cd": "FORD"
  },
  {
    "model_cd": "EXP",
    "model_dsc": "EXP",
    "make_cd": "FORD"
  },
  {
    "model_cd": "EXPE",
    "model_dsc": "EXPEDITION",
    "make_cd": "FORD"
  },
  {
    "model_cd": "EXPL",
    "model_dsc": "EXPLORER",
    "make_cd": "FORD"
  },
  {
    "model_cd": "F100",
    "model_dsc": "F100",
    "make_cd": "FORD"
  },
  {
    "model_cd": "F150",
    "model_dsc": "F-150XLT",
    "make_cd": "FORD"
  },
  {
    "model_cd": "F250",
    "model_dsc": "F250 SUPERCAB (TRUCK)",
    "make_cd": "FORD"
  },
  {
    "model_cd": "F350",
    "model_dsc": "F350",
    "make_cd": "FORD"
  },
  {
    "model_cd": "F450",
    "model_dsc": "F450",
    "make_cd": "FORD"
  },
  {
    "model_cd": "F550",
    "model_dsc": "F550",
    "make_cd": "FORD"
  },
  {
    "model_cd": "FAIL",
    "model_dsc": "FAIRLANE",
    "make_cd": "FORD"
  },
  {
    "model_cd": "FAIR",
    "model_dsc": "FAIRMONT",
    "make_cd": "FORD"
  },
  {
    "model_cd": "FALC",
    "model_dsc": "FALCON",
    "make_cd": "FORD"
  },
  {
    "model_cd": "FEST",
    "model_dsc": "FESTIVA",
    "make_cd": "FORD"
  },
  {
    "model_cd": "FIES",
    "model_dsc": "FIESTA",
    "make_cd": "FORD"
  },
  {
    "model_cd": "FIVE",
    "model_dsc": "FIVE HUNDRED",
    "make_cd": "FORD"
  },
  {
    "model_cd": "FLEX",
    "model_dsc": "FLEX",
    "make_cd": "FORD"
  },
  {
    "model_cd": "FOCU",
    "model_dsc": "FOCUS",
    "make_cd": "FORD"
  },
  {
    "model_cd": "FREE",
    "model_dsc": "FREESTAR",
    "make_cd": "FORD"
  },
  {
    "model_cd": "FRES",
    "model_dsc": "FREESTYLE",
    "make_cd": "FORD"
  },
  {
    "model_cd": "FRO",
    "model_dsc": "FRONTENAC",
    "make_cd": "FORD"
  },
  {
    "model_cd": "FUSI",
    "model_dsc": "FUSION",
    "make_cd": "FORD"
  },
  {
    "model_cd": "FUTU",
    "model_dsc": "FUTURA",
    "make_cd": "FORD"
  },
  {
    "model_cd": "GALA",
    "model_dsc": "GALAXIE",
    "make_cd": "FORD"
  },
  {
    "model_cd": "GRA",
    "model_dsc": "GRAND MARQUIS",
    "make_cd": "FORD"
  },
  {
    "model_cd": "GRAN",
    "model_dsc": "GRANADA",
    "make_cd": "FORD"
  },
  {
    "model_cd": "KA",
    "model_dsc": "KA",
    "make_cd": "FORD"
  },
  {
    "model_cd": "LARI",
    "model_dsc": "LARIAT",
    "make_cd": "FORD"
  },
  {
    "model_cd": "LASE",
    "model_dsc": "LASER",
    "make_cd": "FORD"
  },
  {
    "model_cd": "LTD",
    "model_dsc": "LTD",
    "make_cd": "FORD"
  },
  {
    "model_cd": "LTII",
    "model_dsc": "LTD II",
    "make_cd": "FORD"
  },
  {
    "model_cd": "MAIN",
    "model_dsc": "MAINLINE",
    "make_cd": "FORD"
  },
  {
    "model_cd": "MAVE",
    "model_dsc": "MAVERICK",
    "make_cd": "FORD"
  },
  {
    "model_cd": "MOA",
    "model_dsc": "MODEL A",
    "make_cd": "FORD"
  },
  {
    "model_cd": "MOT",
    "model_dsc": "MODEL T",
    "make_cd": "FORD"
  },
  {
    "model_cd": "MUST",
    "model_dsc": "MUSTANG",
    "make_cd": "FORD"
  },
  {
    "model_cd": "NEVA",
    "model_dsc": "NEVADA",
    "make_cd": "FORD"
  },
  {
    "model_cd": "PINT",
    "model_dsc": "PINTO",
    "make_cd": "FORD"
  },
  {
    "model_cd": "PROB",
    "model_dsc": "PROBE",
    "make_cd": "FORD"
  },
  {
    "model_cd": "RAH",
    "model_dsc": "RANCH",
    "make_cd": "FORD"
  },
  {
    "model_cd": "RANC",
    "model_dsc": "RANCHERO",
    "make_cd": "FORD"
  },
  {
    "model_cd": "RANG",
    "model_dsc": "RANGER",
    "make_cd": "FORD"
  },
  {
    "model_cd": "RAW",
    "model_dsc": "RANCH WAGON",
    "make_cd": "FORD"
  },
  {
    "model_cd": "SPE",
    "model_dsc": "SPECIAL",
    "make_cd": "FORD"
  },
  {
    "model_cd": "SQU",
    "model_dsc": "SQUIRE (FALCON OR FAIRLANE)",
    "make_cd": "FORD"
  },
  {
    "model_cd": "STA",
    "model_dsc": "STARLINER",
    "make_cd": "FORD"
  },
  {
    "model_cd": "SUN",
    "model_dsc": "SUNLINER",
    "make_cd": "FORD"
  },
  {
    "model_cd": "SUP",
    "model_dsc": "SUPER",
    "make_cd": "FORD"
  },
  {
    "model_cd": "TAUR",
    "model_dsc": "TAURUS",
    "make_cd": "FORD"
  },
  {
    "model_cd": "TEMP",
    "model_dsc": "TEMPO",
    "make_cd": "FORD"
  },
  {
    "model_cd": "THUN",
    "model_dsc": "THUNDERBIRD",
    "make_cd": "FORD"
  },
  {
    "model_cd": "TORI",
    "model_dsc": "TORINO (FAIRLANE)",
    "make_cd": "FORD"
  },
  {
    "model_cd": "TRAN",
    "model_dsc": "TRANSIT",
    "make_cd": "FORD"
  },
  {
    "model_cd": "WIND",
    "model_dsc": "WINDSTAR",
    "make_cd": "FORD"
  },
  {
    "model_cd": "XL",
    "model_dsc": "XL",
    "make_cd": "FORD"
  },
  {
    "model_cd": "CMAX",
    "model_dsc": "C-MAX",
    "make_cd": "FORD"
  },
  {
    "model_cd": "COM",
    "model_dsc": "COMETE",
    "make_cd": "FREF"
  },
  {
    "model_cd": "VED",
    "model_dsc": "VEDETTE",
    "make_cd": "FREF"
  },
  {
    "model_cd": "VEN",
    "model_dsc": "VENDOME",
    "make_cd": "FREF"
  },
  {
    "model_cd": "CHA",
    "model_dsc": "CHAIKA",
    "make_cd": "GAZ"
  },
  {
    "model_cd": "VOL",
    "model_dsc": "VOLGA",
    "make_cd": "GAZ"
  },
  {
    "model_cd": "DV",
    "model_dsc": "DRY VAN",
    "make_cd": "GDNE"
  },
  {
    "model_cd": "FLBD",
    "model_dsc": "FLATBED",
    "make_cd": "GDNE"
  },
  {
    "model_cd": "RFRV",
    "model_dsc": "REEFER VAN",
    "make_cd": "GDNE"
  },
  {
    "model_cd": "G70",
    "model_dsc": "G70",
    "make_cd": "GENE"
  },
  {
    "model_cd": "G80",
    "model_dsc": "G80",
    "make_cd": "GENE"
  },
  {
    "model_cd": "G80S",
    "model_dsc": "G80 Sport",
    "make_cd": "GENE"
  },
  {
    "model_cd": "G90",
    "model_dsc": "G90",
    "make_cd": "GENE"
  },
  {
    "model_cd": "METR",
    "model_dsc": "METRO",
    "make_cd": "GEO"
  },
  {
    "model_cd": "PRIZ",
    "model_dsc": "PRIZM",
    "make_cd": "GEO"
  },
  {
    "model_cd": "STRO",
    "model_dsc": "STORM",
    "make_cd": "GEO"
  },
  {
    "model_cd": "TRAC",
    "model_dsc": "TRACKER",
    "make_cd": "GEO"
  },
  {
    "model_cd": "GOG",
    "model_dsc": "GOGGOMOBILE",
    "make_cd": "GLAS"
  },
  {
    "model_cd": "EV1",
    "model_dsc": "EV1",
    "make_cd": "GM"
  },
  {
    "model_cd": "ACAD",
    "model_dsc": "ACADIA",
    "make_cd": "GMC"
  },
  {
    "model_cd": "CAB",
    "model_dsc": "CABELLERO",
    "make_cd": "GMC"
  },
  {
    "model_cd": "CANY",
    "model_dsc": "CANYON",
    "make_cd": "GMC"
  },
  {
    "model_cd": "DEN",
    "model_dsc": "DENALI",
    "make_cd": "GMC"
  },
  {
    "model_cd": "ENVO",
    "model_dsc": "ENVOY",
    "make_cd": "GMC"
  },
  {
    "model_cd": "JIMM",
    "model_dsc": "JIMMY",
    "make_cd": "GMC"
  },
  {
    "model_cd": "RALL",
    "model_dsc": "RALLY",
    "make_cd": "GMC"
  },
  {
    "model_cd": "SAFA",
    "model_dsc": "SAFARI",
    "make_cd": "GMC"
  },
  {
    "model_cd": "SAVA",
    "model_dsc": "SAVANNA",
    "make_cd": "GMC"
  },
  {
    "model_cd": "SIER",
    "model_dsc": "SIERRA",
    "make_cd": "GMC"
  },
  {
    "model_cd": "SONO",
    "model_dsc": "SONOMA",
    "make_cd": "GMC"
  },
  {
    "model_cd": "SPRI",
    "model_dsc": "SPRINT",
    "make_cd": "GMC"
  },
  {
    "model_cd": "SUBU",
    "model_dsc": "SUBURBAN",
    "make_cd": "GMC"
  },
  {
    "model_cd": "TERR",
    "model_dsc": "TERRAIN",
    "make_cd": "GMC"
  },
  {
    "model_cd": "TYP",
    "model_dsc": "TYPHOON",
    "make_cd": "GMC"
  },
  {
    "model_cd": "VAND",
    "model_dsc": "VANDURA",
    "make_cd": "GMC"
  },
  {
    "model_cd": "YUKO",
    "model_dsc": "YUKON",
    "make_cd": "GMC"
  },
  {
    "model_cd": "3500",
    "model_dsc": "3500HD",
    "make_cd": "GMC"
  },
  {
    "model_cd": "TRAC",
    "model_dsc": "TRACKER",
    "make_cd": "GMC"
  },
  {
    "model_cd": "160",
    "model_dsc": "1600 SERIES",
    "make_cd": "HILL"
  },
  {
    "model_cd": "DEL",
    "model_dsc": "DELUXE",
    "make_cd": "HILL"
  },
  {
    "model_cd": "HUS",
    "model_dsc": "HUSKY",
    "make_cd": "HILL"
  },
  {
    "model_cd": "IMP",
    "model_dsc": "IMP",
    "make_cd": "HILL"
  },
  {
    "model_cd": "MIN",
    "model_dsc": "MINX",
    "make_cd": "HILL"
  },
  {
    "model_cd": "SCP",
    "model_dsc": "SCEPTRE",
    "make_cd": "HILL"
  },
  {
    "model_cd": "SNI",
    "model_dsc": "SNIPE",
    "make_cd": "HILL"
  },
  {
    "model_cd": "SUP",
    "model_dsc": "SUPER MINX",
    "make_cd": "HILL"
  },
  {
    "model_cd": "ACCO",
    "model_dsc": "ACCORD",
    "make_cd": "HOND"
  },
  {
    "model_cd": "CIVI",
    "model_dsc": "CIVIC (AND CRX)",
    "make_cd": "HOND"
  },
  {
    "model_cd": "CR-Z",
    "model_dsc": "CR-Z",
    "make_cd": "HOND"
  },
  {
    "model_cd": "CROS",
    "model_dsc": "CROSSTOUR",
    "make_cd": "HOND"
  },
  {
    "model_cd": "CRV",
    "model_dsc": "CRV",
    "make_cd": "HOND"
  },
  {
    "model_cd": "DELS",
    "model_dsc": "DEL SOL",
    "make_cd": "HOND"
  },
  {
    "model_cd": "ELEM",
    "model_dsc": "ELEMENT",
    "make_cd": "HOND"
  },
  {
    "model_cd": "EVP",
    "model_dsc": "EVPLUS",
    "make_cd": "HOND"
  },
  {
    "model_cd": "FIT",
    "model_dsc": "FIT",
    "make_cd": "HOND"
  },
  {
    "model_cd": "HRV",
    "model_dsc": "HR-V",
    "make_cd": "HOND"
  },
  {
    "model_cd": "INSI",
    "model_dsc": "INSIGHT",
    "make_cd": "HOND"
  },
  {
    "model_cd": "ODYS",
    "model_dsc": "ODYSSEY",
    "make_cd": "HOND"
  },
  {
    "model_cd": "PASS",
    "model_dsc": "PASSPORT",
    "make_cd": "HOND"
  },
  {
    "model_cd": "PILO",
    "model_dsc": "PILOT",
    "make_cd": "HOND"
  },
  {
    "model_cd": "PREL",
    "model_dsc": "PRELUDE",
    "make_cd": "HOND"
  },
  {
    "model_cd": "RIDG",
    "model_dsc": "RIDGELINE",
    "make_cd": "HOND"
  },
  {
    "model_cd": "S200",
    "model_dsc": "S2000",
    "make_cd": "HOND"
  },
  {
    "model_cd": "CLAR",
    "model_dsc": "CLARITY",
    "make_cd": "HOND"
  },
  {
    "model_cd": "COM",
    "model_dsc": "COMMODORE",
    "make_cd": "HUDS"
  },
  {
    "model_cd": "DEL",
    "model_dsc": "DELUXE",
    "make_cd": "HUDS"
  },
  {
    "model_cd": "HOR",
    "model_dsc": "HORNET",
    "make_cd": "HUDS"
  },
  {
    "model_cd": "ITA",
    "model_dsc": "ITALIA",
    "make_cd": "HUDS"
  },
  {
    "model_cd": "JET",
    "model_dsc": "JET",
    "make_cd": "HUDS"
  },
  {
    "model_cd": "PAC",
    "model_dsc": "PACEMAKER",
    "make_cd": "HUDS"
  },
  {
    "model_cd": "RAM",
    "model_dsc": "RAMBLER",
    "make_cd": "HUDS"
  },
  {
    "model_cd": "SUP",
    "model_dsc": "SUPER",
    "make_cd": "HUDS"
  },
  {
    "model_cd": "WAS",
    "model_dsc": "WASP",
    "make_cd": "HUDS"
  },
  {
    "model_cd": "HAW",
    "model_dsc": "HAWK",
    "make_cd": "HUMB"
  },
  {
    "model_cd": "SNI",
    "model_dsc": "SNIPE",
    "make_cd": "HUMB"
  },
  {
    "model_cd": "H1",
    "model_dsc": "H1",
    "make_cd": "HUMM"
  },
  {
    "model_cd": "H2",
    "model_dsc": "H2",
    "make_cd": "HUMM"
  },
  {
    "model_cd": "H2SU",
    "model_dsc": "H2 SUT",
    "make_cd": "HUMM"
  },
  {
    "model_cd": "H3",
    "model_dsc": "H3",
    "make_cd": "HUMM"
  },
  {
    "model_cd": "ELAN",
    "model_dsc": "ELANTRA",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "ENTO",
    "model_dsc": "ENTOURAGE",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "EXCE",
    "model_dsc": "EXCEL",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "GENE",
    "model_dsc": "GENESIS",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "ION",
    "model_dsc": "IONIQ",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "ION5",
    "model_dsc": "IONIQ 5",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "ION6",
    "model_dsc": "IONIQ 6",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "KONA",
    "model_dsc": "KONA",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "MAR",
    "model_dsc": "MARCIA",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "NIRO",
    "model_dsc": "NIRO",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "PALI",
    "model_dsc": "PALISADE",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "PONY",
    "model_dsc": "PONY",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "SANT",
    "model_dsc": "SANTA FE",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "SCOU",
    "model_dsc": "SCOUPE",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "SONA",
    "model_dsc": "SONATA",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "STEL",
    "model_dsc": "STELLAR",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "TIBU",
    "model_dsc": "TIBURON",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "TUCS",
    "model_dsc": "TUCSON",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "VELO",
    "model_dsc": "VELOSTER",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "VENU",
    "model_dsc": "VENUE",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "XG30",
    "model_dsc": "XG300",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "XG35",
    "model_dsc": "XG350",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "ACCE",
    "model_dsc": "ACCENT",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "AVAT",
    "model_dsc": "AVATAR",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "AZER",
    "model_dsc": "AZERA",
    "make_cd": "HYUN"
  },
  {
    "model_cd": "CROW",
    "model_dsc": "CROWN",
    "make_cd": "IMPE"
  },
  {
    "model_cd": "CUS",
    "model_dsc": "CUSTOM",
    "make_cd": "IMPE"
  },
  {
    "model_cd": "LEBA",
    "model_dsc": "LE BARON",
    "make_cd": "IMPE"
  },
  {
    "model_cd": "EX35",
    "model_dsc": "EX35",
    "make_cd": "INFI"
  },
  {
    "model_cd": "FX35",
    "model_dsc": "FX35",
    "make_cd": "INFI"
  },
  {
    "model_cd": "FX45",
    "model_dsc": "FX45",
    "make_cd": "INFI"
  },
  {
    "model_cd": "FX50",
    "model_dsc": "FX50",
    "make_cd": "INFI"
  },
  {
    "model_cd": "G20",
    "model_dsc": "G20",
    "make_cd": "INFI"
  },
  {
    "model_cd": "G35",
    "model_dsc": "G35",
    "make_cd": "INFI"
  },
  {
    "model_cd": "G37",
    "model_dsc": "G37",
    "make_cd": "INFI"
  },
  {
    "model_cd": "I30",
    "model_dsc": "I30",
    "make_cd": "INFI"
  },
  {
    "model_cd": "J30",
    "model_dsc": "J30",
    "make_cd": "INFI"
  },
  {
    "model_cd": "M30",
    "model_dsc": "M30",
    "make_cd": "INFI"
  },
  {
    "model_cd": "M35",
    "model_dsc": "M35",
    "make_cd": "INFI"
  },
  {
    "model_cd": "M45",
    "model_dsc": "M45",
    "make_cd": "INFI"
  },
  {
    "model_cd": "Q45",
    "model_dsc": "Q45",
    "make_cd": "INFI"
  },
  {
    "model_cd": "Q50",
    "model_dsc": "Q50",
    "make_cd": "INFI"
  },
  {
    "model_cd": "Q60",
    "model_dsc": "Q60",
    "make_cd": "INFI"
  },
  {
    "model_cd": "Q70L",
    "model_dsc": "Q70L",
    "make_cd": "INFI"
  },
  {
    "model_cd": "QX4",
    "model_dsc": "QX4",
    "make_cd": "INFI"
  },
  {
    "model_cd": "QX50",
    "model_dsc": "QX50",
    "make_cd": "INFI"
  },
  {
    "model_cd": "QX56",
    "model_dsc": "QX56",
    "make_cd": "INFI"
  },
  {
    "model_cd": "QX80",
    "model_dsc": "QX80",
    "make_cd": "INFI"
  },
  {
    "model_cd": "XQ80",
    "model_dsc": "XQ80",
    "make_cd": "INFI"
  },
  {
    "model_cd": "G37X",
    "model_dsc": "G37X",
    "make_cd": "INFI"
  },
  {
    "model_cd": "I35",
    "model_dsc": "I35",
    "make_cd": "INFI"
  },
  {
    "model_cd": "QX60",
    "model_dsc": "QX60",
    "make_cd": "INFI"
  },
  {
    "model_cd": "1652",
    "model_dsc": "1652sc",
    "make_cd": "INTE"
  },
  {
    "model_cd": "3200",
    "model_dsc": "3200",
    "make_cd": "INTE"
  },
  {
    "model_cd": "3800",
    "model_dsc": "3800",
    "make_cd": "INTE"
  },
  {
    "model_cd": "4200",
    "model_dsc": "4200",
    "make_cd": "INTE"
  },
  {
    "model_cd": "4300",
    "model_dsc": "4300",
    "make_cd": "INTE"
  },
  {
    "model_cd": "4400",
    "model_dsc": "4400",
    "make_cd": "INTE"
  },
  {
    "model_cd": "7300",
    "model_dsc": "7300",
    "make_cd": "INTE"
  },
  {
    "model_cd": "7400",
    "model_dsc": "7400",
    "make_cd": "INTE"
  },
  {
    "model_cd": "8500",
    "model_dsc": "8500",
    "make_cd": "INTE"
  },
  {
    "model_cd": "8600",
    "model_dsc": "8600",
    "make_cd": "INTE"
  },
  {
    "model_cd": "9200",
    "model_dsc": "9200i",
    "make_cd": "INTE"
  },
  {
    "model_cd": "9400",
    "model_dsc": "9400i",
    "make_cd": "INTE"
  },
  {
    "model_cd": "9900",
    "model_dsc": "9900i",
    "make_cd": "INTE"
  },
  {
    "model_cd": "9999",
    "model_dsc": "9900ix",
    "make_cd": "INTE"
  },
  {
    "model_cd": "AMG",
    "model_dsc": "AMIGO",
    "make_cd": "ISUZ"
  },
  {
    "model_cd": "HOM",
    "model_dsc": "HOMBRE",
    "make_cd": "ISUZ"
  },
  {
    "model_cd": "IMA",
    "model_dsc": "I-MARK",
    "make_cd": "ISUZ"
  },
  {
    "model_cd": "IMPU",
    "model_dsc": "IMPULSE",
    "make_cd": "ISUZ"
  },
  {
    "model_cd": "OAS",
    "model_dsc": "OASIS",
    "make_cd": "ISUZ"
  },
  {
    "model_cd": "RODE",
    "model_dsc": "RODEO",
    "make_cd": "ISUZ"
  },
  {
    "model_cd": "STYL",
    "model_dsc": "STYLUS",
    "make_cd": "ISUZ"
  },
  {
    "model_cd": "TROO",
    "model_dsc": "TROOPER",
    "make_cd": "ISUZ"
  },
  {
    "model_cd": "VCS",
    "model_dsc": "VEHICROSS",
    "make_cd": "ISUZ"
  },
  {
    "model_cd": "ANG",
    "model_dsc": "ANGLIA",
    "make_cd": "ITAF"
  },
  {
    "model_cd": "24L",
    "model_dsc": "2.4 LITRE",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "340",
    "model_dsc": "340",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "34L",
    "model_dsc": "3.4 LITRE",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "38L",
    "model_dsc": "3.8 LITRE",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "420",
    "model_dsc": "420",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "42L",
    "model_dsc": "4.2 LITRE",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "ETY",
    "model_dsc": "E-TYPE",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "J12",
    "model_dsc": "XJ12",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "MAR",
    "model_dsc": "MARK V SERIES",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "MTS",
    "model_dsc": "MARK TEN SALON",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "SOV",
    "model_dsc": "SOVEREIGN",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "STYP",
    "model_dsc": "S-TYPE",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "V12",
    "model_dsc": "V12",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "VAN",
    "model_dsc": "VANDEN PLAS",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "XF",
    "model_dsc": "XF",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "XJ",
    "model_dsc": "XJ",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "XJ4",
    "model_dsc": "XJ40",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "XJ6",
    "model_dsc": "XJ6",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "XJ8",
    "model_dsc": "XJ8",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "XJC",
    "model_dsc": "XJC",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "XJR",
    "model_dsc": "XJR",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "XJS",
    "model_dsc": "XJS",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "XK",
    "model_dsc": "XK SERIES",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "XK8",
    "model_dsc": "XK8",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "XKE",
    "model_dsc": "XK-E SERIES",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "XTYP",
    "model_dsc": "XTYPE",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "XVLR",
    "model_dsc": "XVLR",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "XE",
    "model_dsc": "XE",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "IPAC",
    "model_dsc": "I-PACE",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "FPAC",
    "model_dsc": "F-PACE",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "EPAC",
    "model_dsc": "E-PACE",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "FTYP",
    "model_dsc": "F-TYPE",
    "make_cd": "JAGU"
  },
  {
    "model_cd": "GLAD",
    "model_dsc": "GLADIATOR",
    "make_cd": "JEEP"
  },
  {
    "model_cd": "CHER",
    "model_dsc": "CHEROKEE/GRAND CHEROKEE",
    "make_cd": "JEEP"
  },
  {
    "model_cd": "CJ",
    "model_dsc": "CJ",
    "make_cd": "JEEP"
  },
  {
    "model_cd": "COMA",
    "model_dsc": "COMANCHE",
    "make_cd": "JEEP"
  },
  {
    "model_cd": "COMM",
    "model_dsc": "COMMANDER",
    "make_cd": "JEEP"
  },
  {
    "model_cd": "COMP",
    "model_dsc": "COMPASS",
    "make_cd": "JEEP"
  },
  {
    "model_cd": "DAKA",
    "model_dsc": "DAKAR",
    "make_cd": "JEEP"
  },
  {
    "model_cd": "J10",
    "model_dsc": "J-10",
    "make_cd": "JEEP"
  },
  {
    "model_cd": "LIBE",
    "model_dsc": "LIBERTY",
    "make_cd": "JEEP"
  },
  {
    "model_cd": "PATR",
    "model_dsc": "PATRIOT",
    "make_cd": "JEEP"
  },
  {
    "model_cd": "RENE",
    "model_dsc": "RENEGADE",
    "make_cd": "JEEP"
  },
  {
    "model_cd": "TJ",
    "model_dsc": "TJ",
    "make_cd": "JEEP"
  },
  {
    "model_cd": "WAGO",
    "model_dsc": "WAGONEER",
    "make_cd": "JEEP"
  },
  {
    "model_cd": "WRAN",
    "model_dsc": "WRANGLER",
    "make_cd": "JEEP"
  },
  {
    "model_cd": "YJ",
    "model_dsc": "YJ",
    "make_cd": "JEEP"
  },
  {
    "model_cd": "HEAL",
    "model_dsc": "HEALY",
    "make_cd": "JENS"
  },
  {
    "model_cd": "INTE",
    "model_dsc": "INTERCEPTOR",
    "make_cd": "JENS"
  },
  {
    "model_cd": "CARO",
    "model_dsc": "CAROLINA",
    "make_cd": "KAIS"
  },
  {
    "model_cd": "DAR",
    "model_dsc": "DARRIN",
    "make_cd": "KAIS"
  },
  {
    "model_cd": "DEL",
    "model_dsc": "DELUXE",
    "make_cd": "KAIS"
  },
  {
    "model_cd": "DRA",
    "model_dsc": "DRAGON",
    "make_cd": "KAIS"
  },
  {
    "model_cd": "MAN",
    "model_dsc": "MANHATTAN",
    "make_cd": "KAIS"
  },
  {
    "model_cd": "SELT",
    "model_dsc": "SELTOS",
    "make_cd": "KIA"
  },
  {
    "model_cd": "AMAN",
    "model_dsc": "AMANTI",
    "make_cd": "KIA"
  },
  {
    "model_cd": "AVE",
    "model_dsc": "AVELLA",
    "make_cd": "KIA"
  },
  {
    "model_cd": "CAD",
    "model_dsc": "CADENZA",
    "make_cd": "KIA"
  },
  {
    "model_cd": "FORT",
    "model_dsc": "FORTE",
    "make_cd": "KIA"
  },
  {
    "model_cd": "K900",
    "model_dsc": "K900",
    "make_cd": "KIA"
  },
  {
    "model_cd": "MAGE",
    "model_dsc": "MAGENTIS",
    "make_cd": "KIA"
  },
  {
    "model_cd": "MATI",
    "model_dsc": "MATIZ",
    "make_cd": "KIA"
  },
  {
    "model_cd": "NIRO",
    "model_dsc": "NIRO",
    "make_cd": "KIA"
  },
  {
    "model_cd": "OPT",
    "model_dsc": "OPTIMA",
    "make_cd": "KIA"
  },
  {
    "model_cd": "RIO",
    "model_dsc": "RIO",
    "make_cd": "KIA"
  },
  {
    "model_cd": "RIO5",
    "model_dsc": "RIO5",
    "make_cd": "KIA"
  },
  {
    "model_cd": "ROND",
    "model_dsc": "RONDO",
    "make_cd": "KIA"
  },
  {
    "model_cd": "SEDO",
    "model_dsc": "SEDONA",
    "make_cd": "KIA"
  },
  {
    "model_cd": "SEPH",
    "model_dsc": "SEPHIA",
    "make_cd": "KIA"
  },
  {
    "model_cd": "SORE",
    "model_dsc": "SORENTO",
    "make_cd": "KIA"
  },
  {
    "model_cd": "SOUL",
    "model_dsc": "SOUL",
    "make_cd": "KIA"
  },
  {
    "model_cd": "SPEC",
    "model_dsc": "SPECTRA",
    "make_cd": "KIA"
  },
  {
    "model_cd": "SPOR",
    "model_dsc": "SPORTAGE",
    "make_cd": "KIA"
  },
  {
    "model_cd": "STIN",
    "model_dsc": "STINGER",
    "make_cd": "KIA"
  },
  {
    "model_cd": "TELL",
    "model_dsc": "TELLURIDE",
    "make_cd": "KIA"
  },
  {
    "model_cd": "CK",
    "model_dsc": "CK",
    "make_cd": "KIOT"
  },
  {
    "model_cd": "DK",
    "model_dsc": "DK",
    "make_cd": "KIOT"
  },
  {
    "model_cd": "B",
    "model_dsc": "B",
    "make_cd": "KUBO"
  },
  {
    "model_cd": "BX",
    "model_dsc": "BX",
    "make_cd": "KUBO"
  },
  {
    "model_cd": "L",
    "model_dsc": "L",
    "make_cd": "KUBO"
  },
  {
    "model_cd": "M",
    "model_dsc": "M",
    "make_cd": "KUBO"
  },
  {
    "model_cd": "RTV",
    "model_dsc": "RTV",
    "make_cd": "KUBO"
  },
  {
    "model_cd": "TLB",
    "model_dsc": "TLB",
    "make_cd": "KUBO"
  },
  {
    "model_cd": "NIV",
    "model_dsc": "NIVA",
    "make_cd": "LADA"
  },
  {
    "model_cd": "129",
    "model_dsc": "LM129",
    "make_cd": "LAMO"
  },
  {
    "model_cd": "COUN",
    "model_dsc": "COUNTACH",
    "make_cd": "LAMO"
  },
  {
    "model_cd": "DIAB",
    "model_dsc": "DIABLO",
    "make_cd": "LAMO"
  },
  {
    "model_cd": "ESP",
    "model_dsc": "ESPADA",
    "make_cd": "LAMO"
  },
  {
    "model_cd": "GALL",
    "model_dsc": "GALLARDO",
    "make_cd": "LAMO"
  },
  {
    "model_cd": "JAL",
    "model_dsc": "JALPA",
    "make_cd": "LAMO"
  },
  {
    "model_cd": "JAR",
    "model_dsc": "JARMA",
    "make_cd": "LAMO"
  },
  {
    "model_cd": "MIU",
    "model_dsc": "MIURA SV",
    "make_cd": "LAMO"
  },
  {
    "model_cd": "ROD",
    "model_dsc": "ROADSTER",
    "make_cd": "LAMO"
  },
  {
    "model_cd": "HURA",
    "model_dsc": "HURACAN",
    "make_cd": "LAMO"
  },
  {
    "model_cd": "D110",
    "model_dsc": "DEFENDER 110",
    "make_cd": "LAND"
  },
  {
    "model_cd": "D90",
    "model_dsc": "DEFENDER 90",
    "make_cd": "LAND"
  },
  {
    "model_cd": "DEFE",
    "model_dsc": "DEFENDER SERIES",
    "make_cd": "LAND"
  },
  {
    "model_cd": "DISC",
    "model_dsc": "RANGE ROVER DISCOVERY",
    "make_cd": "LAND"
  },
  {
    "model_cd": "FREE",
    "model_dsc": "FREELANDER",
    "make_cd": "LAND"
  },
  {
    "model_cd": "HSE",
    "model_dsc": "HSE",
    "make_cd": "LAND"
  },
  {
    "model_cd": "LR2",
    "model_dsc": "LR2",
    "make_cd": "LAND"
  },
  {
    "model_cd": "LR3",
    "model_dsc": "LR3",
    "make_cd": "LAND"
  },
  {
    "model_cd": "LR4",
    "model_dsc": "LR4",
    "make_cd": "LAND"
  },
  {
    "model_cd": "RANG",
    "model_dsc": "RANGE ROVER",
    "make_cd": "LAND"
  },
  {
    "model_cd": "DISS",
    "model_dsc": "RANGE ROVER DISCOVERY SPORT",
    "make_cd": "LAND"
  },
  {
    "model_cd": "EVOQ",
    "model_dsc": "RANGE ROVER EVOQUE",
    "make_cd": "LAND"
  },
  {
    "model_cd": "VELR",
    "model_dsc": "RANGE ROVER VELAR",
    "make_cd": "LAND"
  },
  {
    "model_cd": "SPOR",
    "model_dsc": "RANGE ROVER SPORT",
    "make_cd": "LAND"
  },
  {
    "model_cd": "DK",
    "model_dsc": "DK",
    "make_cd": "LDTR"
  },
  {
    "model_cd": "250",
    "model_dsc": "ES250",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "300",
    "model_dsc": "ES300",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "350",
    "model_dsc": "ES350",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "400",
    "model_dsc": "LS400",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "CT20",
    "model_dsc": "CT200H",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "ES33",
    "model_dsc": "ES330",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "GS3",
    "model_dsc": "GS300",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "GS35",
    "model_dsc": "GS350",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "GS4",
    "model_dsc": "GS400",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "GS43",
    "model_dsc": "GS430",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "GS45",
    "model_dsc": "GS450",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "GSF",
    "model_dsc": "GSF",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "GX46",
    "model_dsc": "GX460",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "GX47",
    "model_dsc": "GX470",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "IS20",
    "model_dsc": "IS200T",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "IS25",
    "model_dsc": "IS250",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "IS30",
    "model_dsc": "IS300",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "IS35",
    "model_dsc": "IS350",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "ISF",
    "model_dsc": "ISF",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "L45",
    "model_dsc": "LX450",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "L47",
    "model_dsc": "LX470",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "L57",
    "model_dsc": "LX570",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "LS43",
    "model_dsc": "LS430",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "LS46",
    "model_dsc": "LS460",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "LS4L",
    "model_dsc": "LS460L",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "LS60",
    "model_dsc": "LS600HL",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "NX",
    "model_dsc": "NX",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "NX30",
    "model_dsc": "NX300",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "RC30",
    "model_dsc": "RC300",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "RC35",
    "model_dsc": "RC350",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "RCF",
    "model_dsc": "RCF",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "RX3",
    "model_dsc": "RX300",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "RX33",
    "model_dsc": "RX330",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "RX35",
    "model_dsc": "RX350",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "RX40",
    "model_dsc": "RX400H",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "RX45",
    "model_dsc": "RX450H",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "S30",
    "model_dsc": "SC300",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "S40",
    "model_dsc": "SC400",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "SC43",
    "model_dsc": "SC430",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "NX25",
    "model_dsc": "NX 250",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "NX35",
    "model_dsc": "NX 350",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "NX3H",
    "model_dsc": "NX 350h",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "NX45",
    "model_dsc": "NX 450h+",
    "make_cd": "LEXU"
  },
  {
    "model_cd": "AVIA",
    "model_dsc": "AVIATOR",
    "make_cd": "LINC"
  },
  {
    "model_cd": "CONT",
    "model_dsc": "CONTINENTAL",
    "make_cd": "LINC"
  },
  {
    "model_cd": "CUS",
    "model_dsc": "CUSTOM",
    "make_cd": "LINC"
  },
  {
    "model_cd": "LS",
    "model_dsc": "LS",
    "make_cd": "LINC"
  },
  {
    "model_cd": "LS6",
    "model_dsc": "LS6",
    "make_cd": "LINC"
  },
  {
    "model_cd": "LS8",
    "model_dsc": "LS8",
    "make_cd": "LINC"
  },
  {
    "model_cd": "MARK",
    "model_dsc": "MARK SERIES",
    "make_cd": "LINC"
  },
  {
    "model_cd": "MII",
    "model_dsc": "MARK II",
    "make_cd": "LINC"
  },
  {
    "model_cd": "MIII",
    "model_dsc": "MARK III",
    "make_cd": "LINC"
  },
  {
    "model_cd": "MIV",
    "model_dsc": "MARK IV",
    "make_cd": "LINC"
  },
  {
    "model_cd": "MKC",
    "model_dsc": "MKC",
    "make_cd": "LINC"
  },
  {
    "model_cd": "MV",
    "model_dsc": "MARK V",
    "make_cd": "LINC"
  },
  {
    "model_cd": "MVI",
    "model_dsc": "MARK VI",
    "make_cd": "LINC"
  },
  {
    "model_cd": "MVII",
    "model_dsc": "MARK VII",
    "make_cd": "LINC"
  },
  {
    "model_cd": "NAVI",
    "model_dsc": "NAVIGATOR",
    "make_cd": "LINC"
  },
  {
    "model_cd": "PRE",
    "model_dsc": "PREMIERE",
    "make_cd": "LINC"
  },
  {
    "model_cd": "STAN",
    "model_dsc": "STANDARD",
    "make_cd": "LINC"
  },
  {
    "model_cd": "TOWN",
    "model_dsc": "TOWN CAR",
    "make_cd": "LINC"
  },
  {
    "model_cd": "VER",
    "model_dsc": "VERSAILLES",
    "make_cd": "LINC"
  },
  {
    "model_cd": "VIII",
    "model_dsc": "MARK VIII",
    "make_cd": "LINC"
  },
  {
    "model_cd": "ZEP",
    "model_dsc": "ZEPHYR",
    "make_cd": "LINC"
  },
  {
    "model_cd": "MKT",
    "model_dsc": "MKT",
    "make_cd": "LINC"
  },
  {
    "model_cd": "NAUT",
    "model_dsc": "NAUTILUS",
    "make_cd": "LINC"
  },
  {
    "model_cd": "MKZ",
    "model_dsc": "MKZ",
    "make_cd": "LINC"
  },
  {
    "model_cd": "MKX",
    "model_dsc": "MKX",
    "make_cd": "LINC"
  },
  {
    "model_cd": "BER",
    "model_dsc": "BERLINA",
    "make_cd": "LNCI"
  },
  {
    "model_cd": "BET",
    "model_dsc": "BETA SERIES",
    "make_cd": "LNCI"
  },
  {
    "model_cd": "DED",
    "model_dsc": "DEDRA",
    "make_cd": "LNCI"
  },
  {
    "model_cd": "FLA",
    "model_dsc": "FLAVIA",
    "make_cd": "LNCI"
  },
  {
    "model_cd": "FLM",
    "model_dsc": "FLAMINIA",
    "make_cd": "LNCI"
  },
  {
    "model_cd": "FUL",
    "model_dsc": "FULVIA",
    "make_cd": "LNCI"
  },
  {
    "model_cd": "ZAG",
    "model_dsc": "ZAGATO",
    "make_cd": "LNCI"
  },
  {
    "model_cd": "ECL",
    "model_dsc": "ECLAT",
    "make_cd": "LOTU"
  },
  {
    "model_cd": "ELA",
    "model_dsc": "ELAN",
    "make_cd": "LOTU"
  },
  {
    "model_cd": "ELI",
    "model_dsc": "ELITE",
    "make_cd": "LOTU"
  },
  {
    "model_cd": "ESPI",
    "model_dsc": "ESPRIT",
    "make_cd": "LOTU"
  },
  {
    "model_cd": "EUR",
    "model_dsc": "EUROPA",
    "make_cd": "LOTU"
  },
  {
    "model_cd": "PLU",
    "model_dsc": "PLUS TWO",
    "make_cd": "LOTU"
  },
  {
    "model_cd": "SUP",
    "model_dsc": "SUPER 7",
    "make_cd": "LOTU"
  },
  {
    "model_cd": "200",
    "model_dsc": "2000 SERIES",
    "make_cd": "MASE"
  },
  {
    "model_cd": "228",
    "model_dsc": "228",
    "make_cd": "MASE"
  },
  {
    "model_cd": "350",
    "model_dsc": "3500 SERIES",
    "make_cd": "MASE"
  },
  {
    "model_cd": "400",
    "model_dsc": "4000 SERIES",
    "make_cd": "MASE"
  },
  {
    "model_cd": "420",
    "model_dsc": "4200 GT",
    "make_cd": "MASE"
  },
  {
    "model_cd": "425",
    "model_dsc": "425",
    "make_cd": "MASE"
  },
  {
    "model_cd": "430",
    "model_dsc": "430",
    "make_cd": "MASE"
  },
  {
    "model_cd": "500",
    "model_dsc": "5000 SERIES",
    "make_cd": "MASE"
  },
  {
    "model_cd": "BIT",
    "model_dsc": "BITURBO",
    "make_cd": "MASE"
  },
  {
    "model_cd": "BOR",
    "model_dsc": "BORA",
    "make_cd": "MASE"
  },
  {
    "model_cd": "GHI",
    "model_dsc": "GHIBLI",
    "make_cd": "MASE"
  },
  {
    "model_cd": "GTI",
    "model_dsc": "GTI SERIES",
    "make_cd": "MASE"
  },
  {
    "model_cd": "IND",
    "model_dsc": "INDY",
    "make_cd": "MASE"
  },
  {
    "model_cd": "KHA",
    "model_dsc": "KHAMSIN",
    "make_cd": "MASE"
  },
  {
    "model_cd": "MER",
    "model_dsc": "MERAK",
    "make_cd": "MASE"
  },
  {
    "model_cd": "MEX",
    "model_dsc": "MEXICO",
    "make_cd": "MASE"
  },
  {
    "model_cd": "MIS",
    "model_dsc": "MISTRELL",
    "make_cd": "MASE"
  },
  {
    "model_cd": "QUA",
    "model_dsc": "QUATTROPORTE",
    "make_cd": "MASE"
  },
  {
    "model_cd": "SEB",
    "model_dsc": "SEBRING",
    "make_cd": "MASE"
  },
  {
    "model_cd": "SHM",
    "model_dsc": "SHAMAL",
    "make_cd": "MASE"
  },
  {
    "model_cd": "SPY",
    "model_dsc": "SPYDER",
    "make_cd": "MASE"
  },
  {
    "model_cd": "1500",
    "model_dsc": "1500",
    "make_cd": "MASS"
  },
  {
    "model_cd": "3400",
    "model_dsc": "3400",
    "make_cd": "MASS"
  },
  {
    "model_cd": "3600",
    "model_dsc": "3600",
    "make_cd": "MASS"
  },
  {
    "model_cd": "500",
    "model_dsc": "500",
    "make_cd": "MASS"
  },
  {
    "model_cd": "5400",
    "model_dsc": "5400",
    "make_cd": "MASS"
  },
  {
    "model_cd": "6400",
    "model_dsc": "6400",
    "make_cd": "MASS"
  },
  {
    "model_cd": "7400",
    "model_dsc": "7400",
    "make_cd": "MASS"
  },
  {
    "model_cd": "8400",
    "model_dsc": "8400",
    "make_cd": "MASS"
  },
  {
    "model_cd": "GC",
    "model_dsc": "GC",
    "make_cd": "MASS"
  },
  {
    "model_cd": "SUNF",
    "model_dsc": "SUNFLOWER",
    "make_cd": "MASS"
  },
  {
    "model_cd": "2",
    "model_dsc": "2",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "3",
    "model_dsc": "3",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "323",
    "model_dsc": "323",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "5",
    "model_dsc": "5",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "6",
    "model_dsc": "6",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "616",
    "model_dsc": "616",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "618",
    "model_dsc": "618",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "626",
    "model_dsc": "626",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "808",
    "model_dsc": "808 SERIES",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "929",
    "model_dsc": "929",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "B200",
    "model_dsc": "B2000",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "B220",
    "model_dsc": "B2200",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "B230",
    "model_dsc": "B2300",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "B250",
    "model_dsc": "B2500",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "B260",
    "model_dsc": "B2600",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "B300",
    "model_dsc": "B3000",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "B400",
    "model_dsc": "B4000",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "CSM",
    "model_dsc": "COSMO",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "CX5",
    "model_dsc": "CX-5",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "CX7",
    "model_dsc": "CX-7",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "CX9",
    "model_dsc": "CX-9",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "GLC",
    "model_dsc": "GLC",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "M6",
    "model_dsc": "M6",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "MIAT",
    "model_dsc": "MIATA",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "MILE",
    "model_dsc": "MILLENIA",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "MISE",
    "model_dsc": "MISER",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "MPV",
    "model_dsc": "MPV",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "MX3",
    "model_dsc": "MX3",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "MX5",
    "model_dsc": "MX5",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "MX6",
    "model_dsc": "MX6",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "NAVA",
    "model_dsc": "NAVAJO",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "PRO",
    "model_dsc": "FAMILIA",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "PROT",
    "model_dsc": "PROTEGE",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "RX2",
    "model_dsc": "RX2 (ROTARY ENGINE)",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "RX3",
    "model_dsc": "RX3 (ROTARY ENGINE)",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "RX4",
    "model_dsc": "RX4 (ROTARY ENGINE)",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "RX7",
    "model_dsc": "RX7 (ROTARY ENGINE)",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "RX8",
    "model_dsc": "RX8",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "TRIB",
    "model_dsc": "TRIBUTE",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "CX3",
    "model_dsc": "CX-3",
    "make_cd": "MAZD"
  },
  {
    "model_cd": "MP4",
    "model_dsc": "MP4",
    "make_cd": "MCLA"
  },
  {
    "model_cd": "BOBC",
    "model_dsc": "BOBCAT",
    "make_cd": "MERC"
  },
  {
    "model_cd": "BREE",
    "model_dsc": "BREEZEWAY",
    "make_cd": "MERC"
  },
  {
    "model_cd": "BROU",
    "model_dsc": "BROUGHAM",
    "make_cd": "MERC"
  },
  {
    "model_cd": "CAPR",
    "model_dsc": "CAPRI",
    "make_cd": "MERC"
  },
  {
    "model_cd": "CCR",
    "model_dsc": "COUNTRY CRUISER",
    "make_cd": "MERC"
  },
  {
    "model_cd": "CLI",
    "model_dsc": "CALIENTE",
    "make_cd": "MERC"
  },
  {
    "model_cd": "CMM",
    "model_dsc": "COMMUTER",
    "make_cd": "MERC"
  },
  {
    "model_cd": "COL",
    "model_dsc": "COLONY PARK",
    "make_cd": "MERC"
  },
  {
    "model_cd": "COME",
    "model_dsc": "COMET",
    "make_cd": "MERC"
  },
  {
    "model_cd": "COUG",
    "model_dsc": "COUGAR",
    "make_cd": "MERC"
  },
  {
    "model_cd": "CUS",
    "model_dsc": "CUSTOM",
    "make_cd": "MERC"
  },
  {
    "model_cd": "CYC",
    "model_dsc": "CYCLONE",
    "make_cd": "MERC"
  },
  {
    "model_cd": "GRAN",
    "model_dsc": "GRAND MARQUIS",
    "make_cd": "MERC"
  },
  {
    "model_cd": "LN7",
    "model_dsc": "LN7",
    "make_cd": "MERC"
  },
  {
    "model_cd": "LYNX",
    "model_dsc": "LYNX",
    "make_cd": "MERC"
  },
  {
    "model_cd": "MARA",
    "model_dsc": "MARAUDER",
    "make_cd": "MERC"
  },
  {
    "model_cd": "MARI",
    "model_dsc": "MARINER",
    "make_cd": "MERC"
  },
  {
    "model_cd": "MARQ",
    "model_dsc": "MARQUIS",
    "make_cd": "MERC"
  },
  {
    "model_cd": "MED",
    "model_dsc": "MEDALIST",
    "make_cd": "MERC"
  },
  {
    "model_cd": "MONA",
    "model_dsc": "MONARCH",
    "make_cd": "MERC"
  },
  {
    "model_cd": "MONT",
    "model_dsc": "MONTEGO",
    "make_cd": "MERC"
  },
  {
    "model_cd": "MONY",
    "model_dsc": "MONTEREY",
    "make_cd": "MERC"
  },
  {
    "model_cd": "MOT",
    "model_dsc": "MONTCLAIR",
    "make_cd": "MERC"
  },
  {
    "model_cd": "MTN",
    "model_dsc": "MOUNTAINEER",
    "make_cd": "MERC"
  },
  {
    "model_cd": "MYST",
    "model_dsc": "MYSTIQUE",
    "make_cd": "MERC"
  },
  {
    "model_cd": "PARK",
    "model_dsc": "PARKLANE",
    "make_cd": "MERC"
  },
  {
    "model_cd": "S22",
    "model_dsc": "S-22",
    "make_cd": "MERC"
  },
  {
    "model_cd": "S33",
    "model_dsc": "S-33",
    "make_cd": "MERC"
  },
  {
    "model_cd": "S55",
    "model_dsc": "S-55",
    "make_cd": "MERC"
  },
  {
    "model_cd": "SABL",
    "model_dsc": "SABLE",
    "make_cd": "MERC"
  },
  {
    "model_cd": "TOPA",
    "model_dsc": "TOPAZ",
    "make_cd": "MERC"
  },
  {
    "model_cd": "TRAC",
    "model_dsc": "TRACER",
    "make_cd": "MERC"
  },
  {
    "model_cd": "TUR",
    "model_dsc": "TURNPIKE CRUISER",
    "make_cd": "MERC"
  },
  {
    "model_cd": "VILL",
    "model_dsc": "VILLAGER",
    "make_cd": "MERC"
  },
  {
    "model_cd": "VOYA",
    "model_dsc": "VOYAGER",
    "make_cd": "MERC"
  },
  {
    "model_cd": "ZEP",
    "model_dsc": "ZEPHYR",
    "make_cd": "MERC"
  },
  {
    "model_cd": "SCOR",
    "model_dsc": "SCORPIO",
    "make_cd": "MERK"
  },
  {
    "model_cd": "XR4",
    "model_dsc": "XR4Ti",
    "make_cd": "MERK"
  },
  {
    "model_cd": "180",
    "model_dsc": "180 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "190",
    "model_dsc": "190 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "200",
    "model_dsc": "200 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "219",
    "model_dsc": "219 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "220",
    "model_dsc": "220 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "230",
    "model_dsc": "230 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "240",
    "model_dsc": "240 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "250",
    "model_dsc": "250 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "260",
    "model_dsc": "260 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "280",
    "model_dsc": "280 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "300",
    "model_dsc": "300 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "320",
    "model_dsc": "320 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "320W",
    "model_dsc": "E320W",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "350",
    "model_dsc": "350 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "380",
    "model_dsc": "380 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "400",
    "model_dsc": "400 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "420",
    "model_dsc": "420 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "450",
    "model_dsc": "450 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "500",
    "model_dsc": "500 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "560",
    "model_dsc": "560 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "600",
    "model_dsc": "600 SERIES",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "B200",
    "model_dsc": "B200",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "B250",
    "model_dsc": "B250",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "C220",
    "model_dsc": "C220",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "C230",
    "model_dsc": "C230",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "C240",
    "model_dsc": "C240",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "C250",
    "model_dsc": "C250",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "C280",
    "model_dsc": "C280",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "C300",
    "model_dsc": "C300",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "C320",
    "model_dsc": "C320",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "C350",
    "model_dsc": "C350",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "C36",
    "model_dsc": "C36",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "C400",
    "model_dsc": "C400",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "C43",
    "model_dsc": "C43",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "C55",
    "model_dsc": "C55",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "C63",
    "model_dsc": "C63",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "CK32",
    "model_dsc": "CLK32",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "CK35",
    "model_dsc": "CLK35",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "CK50",
    "model_dsc": "CLK50",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "CK55",
    "model_dsc": "CLK55",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "CL4",
    "model_dsc": "CLK430",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "CL45",
    "model_dsc": "CLA45",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "CL50",
    "model_dsc": "CL500",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "CL55",
    "model_dsc": "CL55",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "CL60",
    "model_dsc": "CL600",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "CL65",
    "model_dsc": "CL65",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "CLA2",
    "model_dsc": "CLA250",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "CLK3",
    "model_dsc": "CLK320",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "CLK5",
    "model_dsc": "CLK500",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "CLS5",
    "model_dsc": "CLS500",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "CLS6",
    "model_dsc": "CLS63",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "CS55",
    "model_dsc": "CLS55",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "E300",
    "model_dsc": "E300",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "E320",
    "model_dsc": "E320",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "E350",
    "model_dsc": "E350",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "E400",
    "model_dsc": "E400",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "E420",
    "model_dsc": "E420",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "E43",
    "model_dsc": "E43",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "E430",
    "model_dsc": "E430",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "E500",
    "model_dsc": "E500",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "E55",
    "model_dsc": "E55",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "E63",
    "model_dsc": "E63",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "G35",
    "model_dsc": "GLK35",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "G350",
    "model_dsc": "GLE350",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "G400",
    "model_dsc": "GLE400",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "G450",
    "model_dsc": "GL450",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "G500",
    "model_dsc": "G500",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "G55",
    "model_dsc": "G55",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "G550",
    "model_dsc": "G550",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "G63",
    "model_dsc": "G63",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "GL30",
    "model_dsc": "GLC30",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "GL35",
    "model_dsc": "GL350",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "GL43",
    "model_dsc": "GLC43",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "GLA",
    "model_dsc": "GLA",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "GLE3",
    "model_dsc": "GLE35",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "GLE4",
    "model_dsc": "GLE45",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "GLK2",
    "model_dsc": "GLK250",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "GLK3",
    "model_dsc": "GLK350",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "GLS5",
    "model_dsc": "GLS550",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "METR",
    "model_dsc": "METRIS",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "ML3",
    "model_dsc": "ML320 (SPORT UTILITY)",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "ML35",
    "model_dsc": "ML350",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "ML4",
    "model_dsc": "ML430",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "ML50",
    "model_dsc": "ML500",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "ML63",
    "model_dsc": "ML63",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "R350",
    "model_dsc": "R350",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "S430",
    "model_dsc": "S430",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "S450",
    "model_dsc": "S450",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "S500",
    "model_dsc": "S500",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "S55",
    "model_dsc": "S55",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "S550",
    "model_dsc": "S550V",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "S600",
    "model_dsc": "S600",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "SL",
    "model_dsc": "SL",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "SL5",
    "model_dsc": "SL500",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "SL6",
    "model_dsc": "SL600",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "SL65",
    "model_dsc": "SL65",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "SLK3",
    "model_dsc": "SLK3",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "SLK5",
    "model_dsc": "SLK5",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "SPRI",
    "model_dsc": "SPRINTER",
    "make_cd": "MERZ"
  },
  {
    "model_cd": "KR",
    "model_dsc": "KR200",
    "make_cd": "MESS"
  },
  {
    "model_cd": "KR1",
    "model_dsc": "KR201",
    "make_cd": "MESS"
  },
  {
    "model_cd": "TIG",
    "model_dsc": "TIGER",
    "make_cd": "MESS"
  },
  {
    "model_cd": "COY",
    "model_dsc": "COUNTRY SEDAN",
    "make_cd": "METE"
  },
  {
    "model_cd": "LEM",
    "model_dsc": "LEMOYNE",
    "make_cd": "METE"
  },
  {
    "model_cd": "MGO",
    "model_dsc": "MONTEGO",
    "make_cd": "METE"
  },
  {
    "model_cd": "MON",
    "model_dsc": "MONTCALM",
    "make_cd": "METE"
  },
  {
    "model_cd": "NIA",
    "model_dsc": "NIAGARA",
    "make_cd": "METE"
  },
  {
    "model_cd": "RAW",
    "model_dsc": "RANCH WAGON",
    "make_cd": "METE"
  },
  {
    "model_cd": "RID",
    "model_dsc": "RIDEAU",
    "make_cd": "METE"
  },
  {
    "model_cd": "S33",
    "model_dsc": "S-33",
    "make_cd": "METE"
  },
  {
    "model_cd": "1600",
    "model_dsc": "1600",
    "make_cd": "MG"
  },
  {
    "model_cd": "4R",
    "model_dsc": "PRINCESS 4-R",
    "make_cd": "MG"
  },
  {
    "model_cd": "MAGN",
    "model_dsc": "MAGNETTE",
    "make_cd": "MG"
  },
  {
    "model_cd": "MARI",
    "model_dsc": "MARINA",
    "make_cd": "MG"
  },
  {
    "model_cd": "MARK",
    "model_dsc": "MARK II",
    "make_cd": "MG"
  },
  {
    "model_cd": "MG1",
    "model_dsc": "1100",
    "make_cd": "MG"
  },
  {
    "model_cd": "MGA",
    "model_dsc": "MGA",
    "make_cd": "MG"
  },
  {
    "model_cd": "MGB",
    "model_dsc": "MGB",
    "make_cd": "MG"
  },
  {
    "model_cd": "MGC",
    "model_dsc": "MGC",
    "make_cd": "MG"
  },
  {
    "model_cd": "MGG",
    "model_dsc": "MGB/GT",
    "make_cd": "MG"
  },
  {
    "model_cd": "MGT",
    "model_dsc": "MGC/GT",
    "make_cd": "MG"
  },
  {
    "model_cd": "MIDG",
    "model_dsc": "MIDGET",
    "make_cd": "MG"
  },
  {
    "model_cd": "SPRI",
    "model_dsc": "SPRITE",
    "make_cd": "MG"
  },
  {
    "model_cd": "SPS",
    "model_dsc": "SPORTS SEDAN",
    "make_cd": "MG"
  },
  {
    "model_cd": "TF",
    "model_dsc": "TF SERIES",
    "make_cd": "MG"
  },
  {
    "model_cd": "COOP",
    "model_dsc": "COOPER",
    "make_cd": "MINI"
  },
  {
    "model_cd": "3GT",
    "model_dsc": "3000 GT",
    "make_cd": "MITS"
  },
  {
    "model_cd": "CHAR",
    "model_dsc": "CHARIOT",
    "make_cd": "MITS"
  },
  {
    "model_cd": "CORD",
    "model_dsc": "CORDIA",
    "make_cd": "MITS"
  },
  {
    "model_cd": "DELI",
    "model_dsc": "DELICA",
    "make_cd": "MITS"
  },
  {
    "model_cd": "DIAM",
    "model_dsc": "DIAMANTE",
    "make_cd": "MITS"
  },
  {
    "model_cd": "ECL",
    "model_dsc": "ECLIPSE SPYDER GS-T",
    "make_cd": "MITS"
  },
  {
    "model_cd": "ECLI",
    "model_dsc": "ECLIPSE",
    "make_cd": "MITS"
  },
  {
    "model_cd": "ENDE",
    "model_dsc": "ENDEAVOR",
    "make_cd": "MITS"
  },
  {
    "model_cd": "EXPO",
    "model_dsc": "EXPO",
    "make_cd": "MITS"
  },
  {
    "model_cd": "GALA",
    "model_dsc": "GALANT",
    "make_cd": "MITS"
  },
  {
    "model_cd": "LANC",
    "model_dsc": "LANCER",
    "make_cd": "MITS"
  },
  {
    "model_cd": "MIN",
    "model_dsc": "MINICA",
    "make_cd": "MITS"
  },
  {
    "model_cd": "MIRA",
    "model_dsc": "MIRAGE",
    "make_cd": "MITS"
  },
  {
    "model_cd": "MONT",
    "model_dsc": "MONTERO/MONTERO SPORT",
    "make_cd": "MITS"
  },
  {
    "model_cd": "MTX",
    "model_dsc": "MIGHTY MAX",
    "make_cd": "MITS"
  },
  {
    "model_cd": "OUTL",
    "model_dsc": "OUTLANDER",
    "make_cd": "MITS"
  },
  {
    "model_cd": "PRE",
    "model_dsc": "PRECIS",
    "make_cd": "MITS"
  },
  {
    "model_cd": "RVR",
    "model_dsc": "RVR",
    "make_cd": "MITS"
  },
  {
    "model_cd": "SIG",
    "model_dsc": "SIGMA",
    "make_cd": "MITS"
  },
  {
    "model_cd": "SPYD",
    "model_dsc": "SPYDER 3000 GT",
    "make_cd": "MITS"
  },
  {
    "model_cd": "STA",
    "model_dsc": "STARION",
    "make_cd": "MITS"
  },
  {
    "model_cd": "TRE",
    "model_dsc": "TREDIA",
    "make_cd": "MITS"
  },
  {
    "model_cd": "250",
    "model_dsc": "GT250",
    "make_cd": "MODE"
  },
  {
    "model_cd": "MOD",
    "model_dsc": "MODEL A",
    "make_cd": "MODE"
  },
  {
    "model_cd": "THUN",
    "model_dsc": "THUNDERBIRD",
    "make_cd": "MODE"
  },
  {
    "model_cd": "LUC",
    "model_dsc": "LUCERNE",
    "make_cd": "MONA"
  },
  {
    "model_cd": "RIC",
    "model_dsc": "RICHELIEU",
    "make_cd": "MONA"
  },
  {
    "model_cd": "SCP",
    "model_dsc": "SCEPTRE",
    "make_cd": "MONA"
  },
  {
    "model_cd": "MK5",
    "model_dsc": "4/4 MARK 5",
    "make_cd": "MORG"
  },
  {
    "model_cd": "PL4",
    "model_dsc": "PLUS 4 SERIES",
    "make_cd": "MORG"
  },
  {
    "model_cd": "110",
    "model_dsc": "1100",
    "make_cd": "MORR"
  },
  {
    "model_cd": "850",
    "model_dsc": "850 SERIES",
    "make_cd": "MORR"
  },
  {
    "model_cd": "DEL",
    "model_dsc": "DELUXE",
    "make_cd": "MORR"
  },
  {
    "model_cd": "MII",
    "model_dsc": "MINI SERIES",
    "make_cd": "MORR"
  },
  {
    "model_cd": "MIN",
    "model_dsc": "MINOR",
    "make_cd": "MORR"
  },
  {
    "model_cd": "OXF",
    "model_dsc": "OXFORD",
    "make_cd": "MORR"
  },
  {
    "model_cd": "TRV",
    "model_dsc": "TRAVELLER",
    "make_cd": "MORR"
  },
  {
    "model_cd": "V7",
    "model_dsc": "V7",
    "make_cd": "MOTO"
  },
  {
    "model_cd": "V9",
    "model_dsc": "V9",
    "make_cd": "MOTO"
  },
  {
    "model_cd": "JET",
    "model_dsc": "JET",
    "make_cd": "MUNT"
  },
  {
    "model_cd": "AMB",
    "model_dsc": "AMBASSADOR",
    "make_cd": "NASH"
  },
  {
    "model_cd": "LAF",
    "model_dsc": "LAYFAYETTE",
    "make_cd": "NASH"
  },
  {
    "model_cd": "MET",
    "model_dsc": "METROPOLITAN",
    "make_cd": "NASH"
  },
  {
    "model_cd": "RAM",
    "model_dsc": "RAMBLER",
    "make_cd": "NASH"
  },
  {
    "model_cd": "STA",
    "model_dsc": "STATESMAN",
    "make_cd": "NASH"
  },
  {
    "model_cd": "BUS",
    "model_dsc": "BUS",
    "make_cd": "NEFL"
  },
  {
    "model_cd": "BAYS",
    "model_dsc": "BAY STAR",
    "make_cd": "NEWM"
  },
  {
    "model_cd": "CANY",
    "model_dsc": "CANYON STAR",
    "make_cd": "NEWM"
  },
  {
    "model_cd": "VENT",
    "model_dsc": "VENTANA",
    "make_cd": "NEWM"
  },
  {
    "model_cd": "DUTC",
    "model_dsc": "DUTCH STAR",
    "make_cd": "NEWM"
  },
  {
    "model_cd": "MOUN",
    "model_dsc": "MOUNTAIN AIRE",
    "make_cd": "NEWM"
  },
  {
    "model_cd": "ESSE",
    "model_dsc": "ESSEX",
    "make_cd": "NEWM"
  },
  {
    "model_cd": "KING",
    "model_dsc": "KING AIRE",
    "make_cd": "NEWM"
  },
  {
    "model_cd": "200S",
    "model_dsc": "200SX",
    "make_cd": "NISS"
  },
  {
    "model_cd": "240S",
    "model_dsc": "240SX",
    "make_cd": "NISS"
  },
  {
    "model_cd": "300Z",
    "model_dsc": "300ZX",
    "make_cd": "NISS"
  },
  {
    "model_cd": "350Z",
    "model_dsc": "350Z",
    "make_cd": "NISS"
  },
  {
    "model_cd": "370Z",
    "model_dsc": "370Z",
    "make_cd": "NISS"
  },
  {
    "model_cd": "ALTI",
    "model_dsc": "ALTIMA",
    "make_cd": "NISS"
  },
  {
    "model_cd": "ARMA",
    "model_dsc": "ARMADA",
    "make_cd": "NISS"
  },
  {
    "model_cd": "AXXE",
    "model_dsc": "AXXESS",
    "make_cd": "NISS"
  },
  {
    "model_cd": "CUBE",
    "model_dsc": "CUBE",
    "make_cd": "NISS"
  },
  {
    "model_cd": "FRON",
    "model_dsc": "FRONTIER",
    "make_cd": "NISS"
  },
  {
    "model_cd": "GT-R",
    "model_dsc": "GT-R",
    "make_cd": "NISS"
  },
  {
    "model_cd": "JUKE",
    "model_dsc": "JUKE",
    "make_cd": "NISS"
  },
  {
    "model_cd": "KICK",
    "model_dsc": "KICKS",
    "make_cd": "NISS"
  },
  {
    "model_cd": "LEAF",
    "model_dsc": "LEAF",
    "make_cd": "NISS"
  },
  {
    "model_cd": "MAXI",
    "model_dsc": "MAXIMA",
    "make_cd": "NISS"
  },
  {
    "model_cd": "MICR",
    "model_dsc": "MICRA",
    "make_cd": "NISS"
  },
  {
    "model_cd": "MURA",
    "model_dsc": "MURANO",
    "make_cd": "NISS"
  },
  {
    "model_cd": "NAVA",
    "model_dsc": "NAVARA",
    "make_cd": "NISS"
  },
  {
    "model_cd": "NP30",
    "model_dsc": "NP300",
    "make_cd": "NISS"
  },
  {
    "model_cd": "NV20",
    "model_dsc": "NV200",
    "make_cd": "NISS"
  },
  {
    "model_cd": "NX",
    "model_dsc": "NX",
    "make_cd": "NISS"
  },
  {
    "model_cd": "PATH",
    "model_dsc": "PATHFINDER",
    "make_cd": "NISS"
  },
  {
    "model_cd": "PULS",
    "model_dsc": "PULSAR",
    "make_cd": "NISS"
  },
  {
    "model_cd": "QASH",
    "model_dsc": "QASHQAI",
    "make_cd": "NISS"
  },
  {
    "model_cd": "QUES",
    "model_dsc": "QUEST",
    "make_cd": "NISS"
  },
  {
    "model_cd": "ROGU",
    "model_dsc": "ROGUE",
    "make_cd": "NISS"
  },
  {
    "model_cd": "SE",
    "model_dsc": "SE-V6",
    "make_cd": "NISS"
  },
  {
    "model_cd": "SENT",
    "model_dsc": "SENTRA",
    "make_cd": "NISS"
  },
  {
    "model_cd": "SKYL",
    "model_dsc": "SKYLINE",
    "make_cd": "NISS"
  },
  {
    "model_cd": "STAN",
    "model_dsc": "STANZA",
    "make_cd": "NISS"
  },
  {
    "model_cd": "TERR",
    "model_dsc": "TERRANO II",
    "make_cd": "NISS"
  },
  {
    "model_cd": "TITA",
    "model_dsc": "TITAN",
    "make_cd": "NISS"
  },
  {
    "model_cd": "VERS",
    "model_dsc": "VERSA",
    "make_cd": "NISS"
  },
  {
    "model_cd": "XE",
    "model_dsc": "XE",
    "make_cd": "NISS"
  },
  {
    "model_cd": "XTER",
    "model_dsc": "XTERRA",
    "make_cd": "NISS"
  },
  {
    "model_cd": "XTRA",
    "model_dsc": "XTRAIL",
    "make_cd": "NISS"
  },
  {
    "model_cd": "SPSP",
    "model_dsc": "SP&SP",
    "make_cd": "NISS"
  },
  {
    "model_cd": "ARCT",
    "model_dsc": "ARCTIC FOX",
    "make_cd": "NORT"
  },
  {
    "model_cd": "HEV",
    "model_dsc": "HEV",
    "make_cd": "NOVA"
  },
  {
    "model_cd": "100",
    "model_dsc": "1000",
    "make_cd": "NSU"
  },
  {
    "model_cd": "110",
    "model_dsc": "110 TYPE",
    "make_cd": "NSU"
  },
  {
    "model_cd": "AVA",
    "model_dsc": "AUTO NOVA",
    "make_cd": "NSU"
  },
  {
    "model_cd": "PRIN",
    "model_dsc": "PRINZ",
    "make_cd": "NSU"
  },
  {
    "model_cd": "SPI",
    "model_dsc": "SPIDER (WANKEL)",
    "make_cd": "NSU"
  },
  {
    "model_cd": "442",
    "model_dsc": "442",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "88",
    "model_dsc": "88",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "98",
    "model_dsc": "98",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "ACHI",
    "model_dsc": "ACHIEVA",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "ALER",
    "model_dsc": "ALERO",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "AURO",
    "model_dsc": "AURORA",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "BRAV",
    "model_dsc": "BRAVADA",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "CALA",
    "model_dsc": "CALAIS",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "CARA",
    "model_dsc": "CARAVAN",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "CCR",
    "model_dsc": "CUSTOM CRUISER",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "CUS",
    "model_dsc": "CUSTOM",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "CUTL",
    "model_dsc": "CUTLASS",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "CUTS",
    "model_dsc": "CUTLASS SUPREME",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "DEL",
    "model_dsc": "DELUXE",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "DELT",
    "model_dsc": "DELTA 88",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "DLM",
    "model_dsc": "DELMONT 88",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "DLT",
    "model_dsc": "LSS",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "DYN",
    "model_dsc": "DYNAMIC 88",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "F85",
    "model_dsc": "F-85",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "FIRE",
    "model_dsc": "FIRENZA",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "HOLI",
    "model_dsc": "HOLIDAY",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "INTR",
    "model_dsc": "INTRIGUE",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "JTF",
    "model_dsc": "JETFIRE",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "JTS",
    "model_dsc": "JETSTAR",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "OMEG",
    "model_dsc": "OMEGA",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "REG",
    "model_dsc": "REGENCY (NINETY-EIGHT SERIES)",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "ROYA",
    "model_dsc": "ROYALE",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "SIL",
    "model_dsc": "SILHOUETTE",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "STA",
    "model_dsc": "STARFIRE",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "STD",
    "model_dsc": "STANDARD",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "SUP",
    "model_dsc": "SUPER 88",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "TORO",
    "model_dsc": "TORONADO",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "TRO",
    "model_dsc": "TROFEO",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "VIS",
    "model_dsc": "VISTA CRUISER",
    "make_cd": "OLDS"
  },
  {
    "model_cd": "190",
    "model_dsc": "1900",
    "make_cd": "OPEL"
  },
  {
    "model_cd": "ASTR",
    "model_dsc": "ASTRA",
    "make_cd": "OPEL"
  },
  {
    "model_cd": "CARA",
    "model_dsc": "CARAVAN",
    "make_cd": "OPEL"
  },
  {
    "model_cd": "DIPL",
    "model_dsc": "DIPLOMAT",
    "make_cd": "OPEL"
  },
  {
    "model_cd": "GT",
    "model_dsc": "GT",
    "make_cd": "OPEL"
  },
  {
    "model_cd": "KAD",
    "model_dsc": "KADETTE",
    "make_cd": "OPEL"
  },
  {
    "model_cd": "KAP",
    "model_dsc": "KAPITAN",
    "make_cd": "OPEL"
  },
  {
    "model_cd": "LUX",
    "model_dsc": "LUXUS",
    "make_cd": "OPEL"
  },
  {
    "model_cd": "MAN",
    "model_dsc": "MANTA",
    "make_cd": "OPEL"
  },
  {
    "model_cd": "OLY",
    "model_dsc": "OLYMPIA",
    "make_cd": "OPEL"
  },
  {
    "model_cd": "RAL",
    "model_dsc": "RALLYE",
    "make_cd": "OPEL"
  },
  {
    "model_cd": "REK",
    "model_dsc": "REKORD",
    "make_cd": "OPEL"
  },
  {
    "model_cd": "BAL",
    "model_dsc": "BALBOA",
    "make_cd": "PACK"
  },
  {
    "model_cd": "CAR",
    "model_dsc": "CARIBBEAN",
    "make_cd": "PACK"
  },
  {
    "model_cd": "CAVA",
    "model_dsc": "CAVALIER",
    "make_cd": "PACK"
  },
  {
    "model_cd": "CLI",
    "model_dsc": "CLIPPER",
    "make_cd": "PACK"
  },
  {
    "model_cd": "PAT",
    "model_dsc": "PATRICIAN",
    "make_cd": "PACK"
  },
  {
    "model_cd": "PRD",
    "model_dsc": "PREDICTOR",
    "make_cd": "PACK"
  },
  {
    "model_cd": "REQ",
    "model_dsc": "REQUEST",
    "make_cd": "PACK"
  },
  {
    "model_cd": "DEVI",
    "model_dsc": "DEVILLE",
    "make_cd": "PANE"
  },
  {
    "model_cd": "J72",
    "model_dsc": "J72",
    "make_cd": "PANE"
  },
  {
    "model_cd": "KAL",
    "model_dsc": "KILLETA",
    "make_cd": "PANE"
  },
  {
    "model_cd": "LIM",
    "model_dsc": "LIMA",
    "make_cd": "PANE"
  },
  {
    "model_cd": "ROD",
    "model_dsc": "ROADSTER",
    "make_cd": "PANZ"
  },
  {
    "model_cd": "OPTI",
    "model_dsc": "OPTIMA",
    "make_cd": "PASS"
  },
  {
    "model_cd": "203",
    "model_dsc": "203",
    "make_cd": "PEUG"
  },
  {
    "model_cd": "304",
    "model_dsc": "304",
    "make_cd": "PEUG"
  },
  {
    "model_cd": "403",
    "model_dsc": "403",
    "make_cd": "PEUG"
  },
  {
    "model_cd": "404",
    "model_dsc": "404",
    "make_cd": "PEUG"
  },
  {
    "model_cd": "405",
    "model_dsc": "405",
    "make_cd": "PEUG"
  },
  {
    "model_cd": "504",
    "model_dsc": "504 SERIES",
    "make_cd": "PEUG"
  },
  {
    "model_cd": "505",
    "model_dsc": "505 SERIES",
    "make_cd": "PEUG"
  },
  {
    "model_cd": "604",
    "model_dsc": "604",
    "make_cd": "PEUG"
  },
  {
    "model_cd": "TYPH",
    "model_dsc": "TYPHOON",
    "make_cd": "PIAG"
  },
  {
    "model_cd": "D7",
    "model_dsc": "D7",
    "make_cd": "PJ"
  },
  {
    "model_cd": "ACCL",
    "model_dsc": "ACCLAIM",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "ARRO",
    "model_dsc": "ARROW",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "BARR",
    "model_dsc": "BARRACUDA",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "BELV",
    "model_dsc": "BELVEDERE",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "BREE",
    "model_dsc": "BREEZE",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "CAMB",
    "model_dsc": "CAMBRIDGE",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "CARA",
    "model_dsc": "CARAVELLE",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "CHAM",
    "model_dsc": "CHAMP",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "COLT",
    "model_dsc": "COLT",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "CONQ",
    "model_dsc": "CONQUEST",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "CRA",
    "model_dsc": "CRANBROOK",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "CRIC",
    "model_dsc": "CRICKET (IMPORTED)",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "DUST",
    "model_dsc": "DUSTER",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "FURY",
    "model_dsc": "FURY (ALSO GRAN FURY)",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "GTX",
    "model_dsc": "GTX",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "HORI",
    "model_dsc": "HORIZON (ALSO TC3)",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "LASE",
    "model_dsc": "LASER",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "NEON",
    "model_dsc": "NEON",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "PLAZ",
    "model_dsc": "PLAZA",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "RELI",
    "model_dsc": "RELIANT",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "ROAD",
    "model_dsc": "ROAD RUNNER",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "SAPO",
    "model_dsc": "SAPPORO",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "SATE",
    "model_dsc": "SATELLITE",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "SAVO",
    "model_dsc": "SAVOY",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "SCAM",
    "model_dsc": "SCAMP",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "SIGN",
    "model_dsc": "SIGNET",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "SUBU",
    "model_dsc": "SUBURBAN",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "SUND",
    "model_dsc": "SUNDANCE",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "TURI",
    "model_dsc": "TURISMO",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "VALI",
    "model_dsc": "VALIANT",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "VIP",
    "model_dsc": "VIP",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "VOLA",
    "model_dsc": "VOLARE",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "VOYA",
    "model_dsc": "VOYAGER",
    "make_cd": "PLYM"
  },
  {
    "model_cd": "POL1",
    "model_dsc": "POLESTAR 1",
    "make_cd": "POLE"
  },
  {
    "model_cd": "POL2",
    "model_dsc": "POLESTAR 2",
    "make_cd": "POLE"
  },
  {
    "model_cd": "POL3",
    "model_dsc": "POLESTAR 3",
    "make_cd": "POLE"
  },
  {
    "model_cd": "SUNR",
    "model_dsc": "SUNRUNNER",
    "make_cd": "PONT"
  },
  {
    "model_cd": "2000",
    "model_dsc": "2000",
    "make_cd": "PONT"
  },
  {
    "model_cd": "2P2",
    "model_dsc": "2+2",
    "make_cd": "PONT"
  },
  {
    "model_cd": "6000",
    "model_dsc": "6000",
    "make_cd": "PONT"
  },
  {
    "model_cd": "ASTR",
    "model_dsc": "ASTRE",
    "make_cd": "PONT"
  },
  {
    "model_cd": "AZTE",
    "model_dsc": "AZTEK",
    "make_cd": "PONT"
  },
  {
    "model_cd": "BONN",
    "model_dsc": "BONNEVILLE",
    "make_cd": "PONT"
  },
  {
    "model_cd": "CATA",
    "model_dsc": "CATALINA",
    "make_cd": "PONT"
  },
  {
    "model_cd": "CHIE",
    "model_dsc": "CHIEFTAIN",
    "make_cd": "PONT"
  },
  {
    "model_cd": "CUS",
    "model_dsc": "CUSTOM",
    "make_cd": "PONT"
  },
  {
    "model_cd": "DEL",
    "model_dsc": "DELUXE",
    "make_cd": "PONT"
  },
  {
    "model_cd": "EXE",
    "model_dsc": "EXECUTIVE",
    "make_cd": "PONT"
  },
  {
    "model_cd": "FIER",
    "model_dsc": "FIERO",
    "make_cd": "PONT"
  },
  {
    "model_cd": "FIRE",
    "model_dsc": "FIREBIRD",
    "make_cd": "PONT"
  },
  {
    "model_cd": "FIRF",
    "model_dsc": "FIREFLY",
    "make_cd": "PONT"
  },
  {
    "model_cd": "FIRH",
    "model_dsc": "FIREHAWK",
    "make_cd": "PONT"
  },
  {
    "model_cd": "G3",
    "model_dsc": "G3",
    "make_cd": "PONT"
  },
  {
    "model_cd": "G5",
    "model_dsc": "G5",
    "make_cd": "PONT"
  },
  {
    "model_cd": "G6",
    "model_dsc": "G6",
    "make_cd": "PONT"
  },
  {
    "model_cd": "GRAN",
    "model_dsc": "GRAND AM",
    "make_cd": "PONT"
  },
  {
    "model_cd": "GRAP",
    "model_dsc": "GRAND PRIX",
    "make_cd": "PONT"
  },
  {
    "model_cd": "GRD",
    "model_dsc": "GRAND VILLE",
    "make_cd": "PONT"
  },
  {
    "model_cd": "GT0",
    "model_dsc": "GT0",
    "make_cd": "PONT"
  },
  {
    "model_cd": "J200",
    "model_dsc": "J2000",
    "make_cd": "PONT"
  },
  {
    "model_cd": "LAUR",
    "model_dsc": "LAURENTIAN",
    "make_cd": "PONT"
  },
  {
    "model_cd": "LEMA",
    "model_dsc": "LEMANS",
    "make_cd": "PONT"
  },
  {
    "model_cd": "MONT",
    "model_dsc": "MONTANA",
    "make_cd": "PONT"
  },
  {
    "model_cd": "PARG",
    "model_dsc": "GRAND PARISIENNE",
    "make_cd": "PONT"
  },
  {
    "model_cd": "PARI",
    "model_dsc": "PARISIENNE",
    "make_cd": "PONT"
  },
  {
    "model_cd": "PHOE",
    "model_dsc": "PHOENIX",
    "make_cd": "PONT"
  },
  {
    "model_cd": "PURS",
    "model_dsc": "PURSUIT",
    "make_cd": "PONT"
  },
  {
    "model_cd": "SAFA",
    "model_dsc": "SAFARI",
    "make_cd": "PONT"
  },
  {
    "model_cd": "SKY",
    "model_dsc": "SKY CHIEF",
    "make_cd": "PONT"
  },
  {
    "model_cd": "SOLS",
    "model_dsc": "SOLSTICE",
    "make_cd": "PONT"
  },
  {
    "model_cd": "SSE",
    "model_dsc": "SSE",
    "make_cd": "PONT"
  },
  {
    "model_cd": "STA",
    "model_dsc": "STAR CHIEF",
    "make_cd": "PONT"
  },
  {
    "model_cd": "STR",
    "model_dsc": "STREAMLINER",
    "make_cd": "PONT"
  },
  {
    "model_cd": "STRA",
    "model_dsc": "STRATO CHIEF",
    "make_cd": "PONT"
  },
  {
    "model_cd": "SUNB",
    "model_dsc": "SUNBIRD",
    "make_cd": "PONT"
  },
  {
    "model_cd": "SUNF",
    "model_dsc": "SUNFIRE",
    "make_cd": "PONT"
  },
  {
    "model_cd": "SUP",
    "model_dsc": "SUPER CHIEF",
    "make_cd": "PONT"
  },
  {
    "model_cd": "T10",
    "model_dsc": "T-1000",
    "make_cd": "PONT"
  },
  {
    "model_cd": "TEMG",
    "model_dsc": "TEMPEST GTO",
    "make_cd": "PONT"
  },
  {
    "model_cd": "TEMP",
    "model_dsc": "TEMPEST",
    "make_cd": "PONT"
  },
  {
    "model_cd": "TORR",
    "model_dsc": "TORRENT",
    "make_cd": "PONT"
  },
  {
    "model_cd": "TRAN",
    "model_dsc": "TRANS AM (SEE FIREBIRD)",
    "make_cd": "PONT"
  },
  {
    "model_cd": "TRAS",
    "model_dsc": "TRANS SPORT/TRANSPORT",
    "make_cd": "PONT"
  },
  {
    "model_cd": "VENT",
    "model_dsc": "VENTURA",
    "make_cd": "PONT"
  },
  {
    "model_cd": "VIBE",
    "model_dsc": "VIBE",
    "make_cd": "PONT"
  },
  {
    "model_cd": "WAVE",
    "model_dsc": "WAVE",
    "make_cd": "PONT"
  },
  {
    "model_cd": "150",
    "model_dsc": "1500",
    "make_cd": "PORS"
  },
  {
    "model_cd": "160",
    "model_dsc": "1600",
    "make_cd": "PORS"
  },
  {
    "model_cd": "356",
    "model_dsc": "356",
    "make_cd": "PORS"
  },
  {
    "model_cd": "911",
    "model_dsc": "911",
    "make_cd": "PORS"
  },
  {
    "model_cd": "912",
    "model_dsc": "912",
    "make_cd": "PORS"
  },
  {
    "model_cd": "914",
    "model_dsc": "914",
    "make_cd": "PORS"
  },
  {
    "model_cd": "918",
    "model_dsc": "918 SPYDER",
    "make_cd": "PORS"
  },
  {
    "model_cd": "924",
    "model_dsc": "924",
    "make_cd": "PORS"
  },
  {
    "model_cd": "928",
    "model_dsc": "928",
    "make_cd": "PORS"
  },
  {
    "model_cd": "930",
    "model_dsc": "930",
    "make_cd": "PORS"
  },
  {
    "model_cd": "944",
    "model_dsc": "944",
    "make_cd": "PORS"
  },
  {
    "model_cd": "968",
    "model_dsc": "968",
    "make_cd": "PORS"
  },
  {
    "model_cd": "BOXS",
    "model_dsc": "BOXSTER",
    "make_cd": "PORS"
  },
  {
    "model_cd": "CABR",
    "model_dsc": "CABRIOLET",
    "make_cd": "PORS"
  },
  {
    "model_cd": "CARR",
    "model_dsc": "CARRERA",
    "make_cd": "PORS"
  },
  {
    "model_cd": "CAYE",
    "model_dsc": "CAYENNE",
    "make_cd": "PORS"
  },
  {
    "model_cd": "CAYM",
    "model_dsc": "CAYMAN",
    "make_cd": "PORS"
  },
  {
    "model_cd": "KARM",
    "model_dsc": "KARMAN",
    "make_cd": "PORS"
  },
  {
    "model_cd": "MACA",
    "model_dsc": "MACAN",
    "make_cd": "PORS"
  },
  {
    "model_cd": "PANA",
    "model_dsc": "PANAMERA",
    "make_cd": "PORS"
  },
  {
    "model_cd": "STA",
    "model_dsc": "STANDARD",
    "make_cd": "PORS"
  },
  {
    "model_cd": "SUP",
    "model_dsc": "SUPER",
    "make_cd": "PORS"
  },
  {
    "model_cd": "TARG",
    "model_dsc": "TARGA",
    "make_cd": "PORS"
  },
  {
    "model_cd": "1500",
    "model_dsc": "1500",
    "make_cd": "RAM"
  },
  {
    "model_cd": "PROM",
    "model_dsc": "ProMaster",
    "make_cd": "RAM"
  },
  {
    "model_cd": "3500",
    "model_dsc": "3500",
    "make_cd": "RAM"
  },
  {
    "model_cd": "2500",
    "model_dsc": "2500",
    "make_cd": "RAM"
  },
  {
    "model_cd": "AMBA",
    "model_dsc": "AMBASSADOR",
    "make_cd": "RAMB"
  },
  {
    "model_cd": "AMER",
    "model_dsc": "AMERICAN",
    "make_cd": "RAMB"
  },
  {
    "model_cd": "CLAS",
    "model_dsc": "CLASSIC",
    "make_cd": "RAMB"
  },
  {
    "model_cd": "CUS",
    "model_dsc": "CUSTOM",
    "make_cd": "RAMB"
  },
  {
    "model_cd": "DEL",
    "model_dsc": "DELUXE",
    "make_cd": "RAMB"
  },
  {
    "model_cd": "SUP",
    "model_dsc": "SUPER",
    "make_cd": "RAMB"
  },
  {
    "model_cd": "TYP",
    "model_dsc": "TYPHOON",
    "make_cd": "RAMB"
  },
  {
    "model_cd": "18i",
    "model_dsc": "18i",
    "make_cd": "RENA"
  },
  {
    "model_cd": "750",
    "model_dsc": "750",
    "make_cd": "RENA"
  },
  {
    "model_cd": "CARA",
    "model_dsc": "CARAVELLE",
    "make_cd": "RENA"
  },
  {
    "model_cd": "DAU",
    "model_dsc": "DAUPHINE",
    "make_cd": "RENA"
  },
  {
    "model_cd": "EST",
    "model_dsc": "ESTAFETTE",
    "make_cd": "RENA"
  },
  {
    "model_cd": "EXPO",
    "model_dsc": "EXPORT",
    "make_cd": "RENA"
  },
  {
    "model_cd": "FUEG",
    "model_dsc": "FUEGO",
    "make_cd": "RENA"
  },
  {
    "model_cd": "GON",
    "model_dsc": "GORDINI",
    "make_cd": "RENA"
  },
  {
    "model_cd": "LEC",
    "model_dsc": "LE CAR",
    "make_cd": "RENA"
  },
  {
    "model_cd": "LX",
    "model_dsc": "LUXE",
    "make_cd": "RENA"
  },
  {
    "model_cd": "R10",
    "model_dsc": "R-10",
    "make_cd": "RENA"
  },
  {
    "model_cd": "R12",
    "model_dsc": "R-12",
    "make_cd": "RENA"
  },
  {
    "model_cd": "R15",
    "model_dsc": "R-15",
    "make_cd": "RENA"
  },
  {
    "model_cd": "R16",
    "model_dsc": "R-16",
    "make_cd": "RENA"
  },
  {
    "model_cd": "R17",
    "model_dsc": "R-17",
    "make_cd": "RENA"
  },
  {
    "model_cd": "R4",
    "model_dsc": "R-4",
    "make_cd": "RENA"
  },
  {
    "model_cd": "R5",
    "model_dsc": "R-5",
    "make_cd": "RENA"
  },
  {
    "model_cd": "R8",
    "model_dsc": "R-8",
    "make_cd": "RENA"
  },
  {
    "model_cd": "AERB",
    "model_dsc": "AERBUS",
    "make_cd": "REXH"
  },
  {
    "model_cd": "CONC",
    "model_dsc": "CONCORD",
    "make_cd": "REXH"
  },
  {
    "model_cd": "FLEE",
    "model_dsc": "FLEETWOOD",
    "make_cd": "REXH"
  },
  {
    "model_cd": "REXA",
    "model_dsc": "REXAIR",
    "make_cd": "REXH"
  },
  {
    "model_cd": "ROLL",
    "model_dsc": "ROLLSAIR",
    "make_cd": "REXH"
  },
  {
    "model_cd": "R1S",
    "model_dsc": "R1S",
    "make_cd": "RIVI"
  },
  {
    "model_cd": "R1T",
    "model_dsc": "R1T",
    "make_cd": "RIVI"
  },
  {
    "model_cd": "CAM",
    "model_dsc": "CAMARGUE",
    "make_cd": "ROLL"
  },
  {
    "model_cd": "CORN",
    "model_dsc": "CORNICHE",
    "make_cd": "ROLL"
  },
  {
    "model_cd": "FPR",
    "model_dsc": "FLYING SPUR",
    "make_cd": "ROLL"
  },
  {
    "model_cd": "MUL",
    "model_dsc": "MULSANNE",
    "make_cd": "ROLL"
  },
  {
    "model_cd": "PHAN",
    "model_dsc": "PHANTOM",
    "make_cd": "ROLL"
  },
  {
    "model_cd": "SER",
    "model_dsc": "SILVER SERAPH",
    "make_cd": "ROLL"
  },
  {
    "model_cd": "SID",
    "model_dsc": "SILVER DAWN",
    "make_cd": "ROLL"
  },
  {
    "model_cd": "SILV",
    "model_dsc": "SILVER CLOUD",
    "make_cd": "ROLL"
  },
  {
    "model_cd": "SIS",
    "model_dsc": "SILVER SHADOW",
    "make_cd": "ROLL"
  },
  {
    "model_cd": "SIW",
    "model_dsc": "SILVER WRAITH",
    "make_cd": "ROLL"
  },
  {
    "model_cd": "SPR",
    "model_dsc": "SILVER SPUR",
    "make_cd": "ROLL"
  },
  {
    "model_cd": "SSP",
    "model_dsc": "SILVER SPIRIT",
    "make_cd": "ROLL"
  },
  {
    "model_cd": "ALP",
    "model_dsc": "ALPINE",
    "make_cd": "ROOT"
  },
  {
    "model_cd": "ARR",
    "model_dsc": "ARROW",
    "make_cd": "ROOT"
  },
  {
    "model_cd": "IMP",
    "model_dsc": "IMP",
    "make_cd": "ROOT"
  },
  {
    "model_cd": "TIG",
    "model_dsc": "TIGER",
    "make_cd": "ROOT"
  },
  {
    "model_cd": "200",
    "model_dsc": "2000",
    "make_cd": "ROVE"
  },
  {
    "model_cd": "350",
    "model_dsc": "3500",
    "make_cd": "ROVE"
  },
  {
    "model_cd": "3L",
    "model_dsc": "3 LITRE",
    "make_cd": "ROVE"
  },
  {
    "model_cd": "LAND",
    "model_dsc": "LAND ROVER",
    "make_cd": "ROVE"
  },
  {
    "model_cd": "MK4",
    "model_dsc": "MARK IV",
    "make_cd": "ROVE"
  },
  {
    "model_cd": "900",
    "model_dsc": "900",
    "make_cd": "SAAB"
  },
  {
    "model_cd": "9000",
    "model_dsc": "9000",
    "make_cd": "SAAB"
  },
  {
    "model_cd": "92",
    "model_dsc": "92",
    "make_cd": "SAAB"
  },
  {
    "model_cd": "92X",
    "model_dsc": "92X",
    "make_cd": "SAAB"
  },
  {
    "model_cd": "93",
    "model_dsc": "93 & 93B",
    "make_cd": "SAAB"
  },
  {
    "model_cd": "95",
    "model_dsc": "95",
    "make_cd": "SAAB"
  },
  {
    "model_cd": "96",
    "model_dsc": "96",
    "make_cd": "SAAB"
  },
  {
    "model_cd": "97",
    "model_dsc": "97",
    "make_cd": "SAAB"
  },
  {
    "model_cd": "97X",
    "model_dsc": "97X",
    "make_cd": "SAAB"
  },
  {
    "model_cd": "99",
    "model_dsc": "99",
    "make_cd": "SAAB"
  },
  {
    "model_cd": "GT",
    "model_dsc": "GT 750",
    "make_cd": "SAAB"
  },
  {
    "model_cd": "SON",
    "model_dsc": "SONNET",
    "make_cd": "SAAB"
  },
  {
    "model_cd": "45538",
    "model_dsc": "45538",
    "make_cd": "SAAB"
  },
  {
    "model_cd": "CM60",
    "model_dsc": "CM600S",
    "make_cd": "SANG"
  },
  {
    "model_cd": "JEEP",
    "model_dsc": "JEEP",
    "make_cd": "SANG"
  },
  {
    "model_cd": "ASTR",
    "model_dsc": "ASTRA",
    "make_cd": "SATU"
  },
  {
    "model_cd": "EVI",
    "model_dsc": "EVI",
    "make_cd": "SATU"
  },
  {
    "model_cd": "ION",
    "model_dsc": "ION",
    "make_cd": "SATU"
  },
  {
    "model_cd": "LSER",
    "model_dsc": "LSERIES",
    "make_cd": "SATU"
  },
  {
    "model_cd": "RELA",
    "model_dsc": "RELAY",
    "make_cd": "SATU"
  },
  {
    "model_cd": "SC",
    "model_dsc": "SC",
    "make_cd": "SATU"
  },
  {
    "model_cd": "SKY",
    "model_dsc": "SKY",
    "make_cd": "SATU"
  },
  {
    "model_cd": "SL",
    "model_dsc": "SL",
    "make_cd": "SATU"
  },
  {
    "model_cd": "SW",
    "model_dsc": "SW",
    "make_cd": "SATU"
  },
  {
    "model_cd": "VUE",
    "model_dsc": "VUE",
    "make_cd": "SATU"
  },
  {
    "model_cd": "LW20",
    "model_dsc": "LW200",
    "make_cd": "SATU"
  },
  {
    "model_cd": "LS1",
    "model_dsc": "LS1",
    "make_cd": "SATU"
  },
  {
    "model_cd": "FRS",
    "model_dsc": "FR-S",
    "make_cd": "SCIO"
  },
  {
    "model_cd": "TC",
    "model_dsc": "TC",
    "make_cd": "SCIO"
  },
  {
    "model_cd": "XA",
    "model_dsc": "XA",
    "make_cd": "SCIO"
  },
  {
    "model_cd": "XB",
    "model_dsc": "XB",
    "make_cd": "SCIO"
  },
  {
    "model_cd": "IM",
    "model_dsc": "IM",
    "make_cd": "SCIO"
  },
  {
    "model_cd": "C500",
    "model_dsc": "COBRA GT500",
    "make_cd": "SHEB"
  },
  {
    "model_cd": "COBR",
    "model_dsc": "COBRA",
    "make_cd": "SHEB"
  },
  {
    "model_cd": "CSX",
    "model_dsc": "CSX",
    "make_cd": "SHEB"
  },
  {
    "model_cd": "100",
    "model_dsc": "1000 & 1000GL",
    "make_cd": "SIM"
  },
  {
    "model_cd": "120",
    "model_dsc": "120",
    "make_cd": "SIM"
  },
  {
    "model_cd": "ARO",
    "model_dsc": "ARONDE",
    "make_cd": "SIM"
  },
  {
    "model_cd": "BER",
    "model_dsc": "BERTONE",
    "make_cd": "SIM"
  },
  {
    "model_cd": "ETO",
    "model_dsc": "ETOILE",
    "make_cd": "SIM"
  },
  {
    "model_cd": "GLS",
    "model_dsc": "GLS",
    "make_cd": "SIM"
  },
  {
    "model_cd": "VED",
    "model_dsc": "VEDETTE",
    "make_cd": "SIM"
  },
  {
    "model_cd": "CHA",
    "model_dsc": "CHAMOIS",
    "make_cd": "SIN"
  },
  {
    "model_cd": "VOG",
    "model_dsc": "VOGUE",
    "make_cd": "SIN"
  },
  {
    "model_cd": "FORT",
    "model_dsc": "FORTWO",
    "make_cd": "SMAR"
  },
  {
    "model_cd": "252T",
    "model_dsc": "SL252T",
    "make_cd": "SOUT"
  },
  {
    "model_cd": "825",
    "model_dsc": "825",
    "make_cd": "STLG"
  },
  {
    "model_cd": "827",
    "model_dsc": "827",
    "make_cd": "STLG"
  },
  {
    "model_cd": "TK",
    "model_dsc": "STERLING",
    "make_cd": "STLG"
  },
  {
    "model_cd": "AVAN",
    "model_dsc": "AVANTI",
    "make_cd": "STUD"
  },
  {
    "model_cd": "CHAL",
    "model_dsc": "CHALLENGER",
    "make_cd": "STUD"
  },
  {
    "model_cd": "CHAM",
    "model_dsc": "CHAMPION",
    "make_cd": "STUD"
  },
  {
    "model_cd": "COM",
    "model_dsc": "COMMANDER",
    "make_cd": "STUD"
  },
  {
    "model_cd": "CRU",
    "model_dsc": "CRUISER",
    "make_cd": "STUD"
  },
  {
    "model_cd": "DAYT",
    "model_dsc": "DAYTONA",
    "make_cd": "STUD"
  },
  {
    "model_cd": "HAWK",
    "model_dsc": "HAWK SERIES",
    "make_cd": "STUD"
  },
  {
    "model_cd": "LAN",
    "model_dsc": "LANDALL",
    "make_cd": "STUD"
  },
  {
    "model_cd": "LAR",
    "model_dsc": "LANK SERIES",
    "make_cd": "STUD"
  },
  {
    "model_cd": "PRE",
    "model_dsc": "PRESIDENT",
    "make_cd": "STUD"
  },
  {
    "model_cd": "REGA",
    "model_dsc": "REGAL",
    "make_cd": "STUD"
  },
  {
    "model_cd": "SCO",
    "model_dsc": "SCOTSMAN",
    "make_cd": "STUD"
  },
  {
    "model_cd": "TURI",
    "model_dsc": "GRAND TURISMO",
    "make_cd": "STUD"
  },
  {
    "model_cd": "WAGO",
    "model_dsc": "WAGONAIRE",
    "make_cd": "STUD"
  },
  {
    "model_cd": "100",
    "model_dsc": "100 SERIES",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "110",
    "model_dsc": "1100 SERIES",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "130",
    "model_dsc": "1300 SERIES",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "140",
    "model_dsc": "1400 SERIES",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "160",
    "model_dsc": "1600 SERIES",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "BAJA",
    "model_dsc": "BAJA",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "BRZ",
    "model_dsc": "BRZ",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "CROS",
    "model_dsc": "CROSSTREK",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "DL",
    "model_dsc": "DL",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "FE2",
    "model_dsc": "FE",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "FORR",
    "model_dsc": "FORESTER",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "GL",
    "model_dsc": "GL",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "GLF",
    "model_dsc": "GLF",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "IMPO",
    "model_dsc": "IMPREZA OUTBACK",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "IMPR",
    "model_dsc": "IMPREZA",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "JUST",
    "model_dsc": "JUSTY",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "LEGA",
    "model_dsc": "LEGACY",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "LEGO",
    "model_dsc": "LEGACY OUTBACK",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "LEON",
    "model_dsc": "LEONE GL COUPE",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "LOYA",
    "model_dsc": "LOYALE",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "RX",
    "model_dsc": "RX",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "SPOR",
    "model_dsc": "OUTBACK SPORT (SW)",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "STA",
    "model_dsc": "STANDARD",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "SVX",
    "model_dsc": "SVX",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "TRIB",
    "model_dsc": "TRIBECA",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "WRX",
    "model_dsc": "WRX",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "XT6",
    "model_dsc": "XT6",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "XTC",
    "model_dsc": "XT COUPE",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "ASCE",
    "model_dsc": "ASCENT",
    "make_cd": "SUBA"
  },
  {
    "model_cd": "ALP",
    "model_dsc": "ALPINE",
    "make_cd": "SUNB"
  },
  {
    "model_cd": "ARR",
    "model_dsc": "ARROW",
    "make_cd": "SUNB"
  },
  {
    "model_cd": "DEL",
    "model_dsc": "DELUXE",
    "make_cd": "SUNB"
  },
  {
    "model_cd": "IMP",
    "model_dsc": "IMP",
    "make_cd": "SUNB"
  },
  {
    "model_cd": "MINX",
    "model_dsc": "MINX",
    "make_cd": "SUNB"
  },
  {
    "model_cd": "RAP",
    "model_dsc": "RAPIER",
    "make_cd": "SUNB"
  },
  {
    "model_cd": "TIG",
    "model_dsc": "TIGER",
    "make_cd": "SUNB"
  },
  {
    "model_cd": "AERI",
    "model_dsc": "AERIO",
    "make_cd": "SUZU"
  },
  {
    "model_cd": "ESTE",
    "model_dsc": "ESTEEM",
    "make_cd": "SUZU"
  },
  {
    "model_cd": "FORS",
    "model_dsc": "FORSA",
    "make_cd": "SUZU"
  },
  {
    "model_cd": "GRVI",
    "model_dsc": "GRAND VITARA",
    "make_cd": "SUZU"
  },
  {
    "model_cd": "SAMU",
    "model_dsc": "SAMURAI",
    "make_cd": "SUZU"
  },
  {
    "model_cd": "SIDE",
    "model_dsc": "SIDEKICK",
    "make_cd": "SUZU"
  },
  {
    "model_cd": "SWIF",
    "model_dsc": "SWIFT",
    "make_cd": "SUZU"
  },
  {
    "model_cd": "SX4",
    "model_dsc": "SX4",
    "make_cd": "SUZU"
  },
  {
    "model_cd": "VER",
    "model_dsc": "VERONA",
    "make_cd": "SUZU"
  },
  {
    "model_cd": "VITA",
    "model_dsc": "VITARA",
    "make_cd": "SUZU"
  },
  {
    "model_cd": "X90",
    "model_dsc": "X90",
    "make_cd": "SUZU"
  },
  {
    "model_cd": "XL7",
    "model_dsc": "XL7",
    "make_cd": "SUZU"
  },
  {
    "model_cd": "KIZA",
    "model_dsc": "KIZASHI",
    "make_cd": "SUZU"
  },
  {
    "model_cd": "3",
    "model_dsc": "MODEL 3",
    "make_cd": "TESL"
  },
  {
    "model_cd": "ROAD",
    "model_dsc": "ROADSTER",
    "make_cd": "TESL"
  },
  {
    "model_cd": "S",
    "model_dsc": "MODEL S",
    "make_cd": "TESL"
  },
  {
    "model_cd": "X",
    "model_dsc": "MODEL X",
    "make_cd": "TESL"
  },
  {
    "model_cd": "Y",
    "model_dsc": "MODEL Y",
    "make_cd": "TESL"
  },
  {
    "model_cd": "BUS",
    "model_dsc": "SCHOOL BUS",
    "make_cd": "THOM"
  },
  {
    "model_cd": "WAVE",
    "model_dsc": "WAVE",
    "make_cd": "THOR"
  },
  {
    "model_cd": "ACE",
    "model_dsc": "ACE",
    "make_cd": "THOR"
  },
  {
    "model_cd": "4RUN",
    "model_dsc": "4-RUNNER",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "86",
    "model_dsc": "86",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "ALPH",
    "model_dsc": "ALPHARD",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "ARIS",
    "model_dsc": "ARISTO",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "AVAL",
    "model_dsc": "AVALON",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "AVEN",
    "model_dsc": "AVENSIS",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "CAMR",
    "model_dsc": "CAMRY",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "CARI",
    "model_dsc": "CARINA",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "CAVA",
    "model_dsc": "CAVALIER",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "CELI",
    "model_dsc": "CELICA",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "CHR",
    "model_dsc": "C-HR",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "CORO",
    "model_dsc": "COROLLA",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "CRES",
    "model_dsc": "CRESSIDA",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "CROW",
    "model_dsc": "CROWN",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "ECHO",
    "model_dsc": "ECHO",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "FJ",
    "model_dsc": "FJ CRUISER",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "HIGH",
    "model_dsc": "HIGHLANDER",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "HILU",
    "model_dsc": "HILUX",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "LAND",
    "model_dsc": "LAND CRUISER",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "LEVA",
    "model_dsc": "LE VAN",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "MARK",
    "model_dsc": "MARK II",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "MATR",
    "model_dsc": "MATRIX",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "MR2",
    "model_dsc": "MR2",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "PASE",
    "model_dsc": "PASEO",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "PRE",
    "model_dsc": "PRE RUNNER",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "PREV",
    "model_dsc": "PREVIA",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "PRI",
    "model_dsc": "PRIUS",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "RAV4",
    "model_dsc": "RAV4",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "SCIO",
    "model_dsc": "SCION",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "SEQU",
    "model_dsc": "SEQUOIA",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "SIEN",
    "model_dsc": "SIENNA",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "SOLA",
    "model_dsc": "SOLARA",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "SR5",
    "model_dsc": "SR5",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "STAR",
    "model_dsc": "STARLET",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "SUPR",
    "model_dsc": "SUPRA",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "T100",
    "model_dsc": "T-100",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "TACO",
    "model_dsc": "TACOMA",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "TERC",
    "model_dsc": "TERCEL",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "TUND",
    "model_dsc": "TUNDRA",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "VENZ",
    "model_dsc": "VENZA",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "YARI",
    "model_dsc": "YARIS",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "MIRA",
    "model_dsc": "MIRAI",
    "make_cd": "TOYO"
  },
  {
    "model_cd": "1200",
    "model_dsc": "1200",
    "make_cd": "TRIU"
  },
  {
    "model_cd": "1250",
    "model_dsc": "1250",
    "make_cd": "TRIU"
  },
  {
    "model_cd": "1300",
    "model_dsc": "1300",
    "make_cd": "TRIU"
  },
  {
    "model_cd": "2000",
    "model_dsc": "2000",
    "make_cd": "TRIU"
  },
  {
    "model_cd": "250",
    "model_dsc": "250",
    "make_cd": "TRIU"
  },
  {
    "model_cd": "GT",
    "model_dsc": "GT SERIES",
    "make_cd": "TRIU"
  },
  {
    "model_cd": "HERA",
    "model_dsc": "HERALD",
    "make_cd": "TRIU"
  },
  {
    "model_cd": "SP6",
    "model_dsc": "SPORT 6",
    "make_cd": "TRIU"
  },
  {
    "model_cd": "SPIT",
    "model_dsc": "SPITFIRE",
    "make_cd": "TRIU"
  },
  {
    "model_cd": "STA",
    "model_dsc": "STAG",
    "make_cd": "TRIU"
  },
  {
    "model_cd": "TR3",
    "model_dsc": "TR-3 & TR-3A",
    "make_cd": "TRIU"
  },
  {
    "model_cd": "TR4",
    "model_dsc": "TR-4 & TR-4A",
    "make_cd": "TRIU"
  },
  {
    "model_cd": "TR6",
    "model_dsc": "TR6",
    "make_cd": "TRIU"
  },
  {
    "model_cd": "TR7",
    "model_dsc": "TR7",
    "make_cd": "TRIU"
  },
  {
    "model_cd": "TR8",
    "model_dsc": "TR8",
    "make_cd": "TRIU"
  },
  {
    "model_cd": "VITE",
    "model_dsc": "VITESSE",
    "make_cd": "TRIU"
  },
  {
    "model_cd": "TUS",
    "model_dsc": "TUSCAN",
    "make_cd": "TVR"
  },
  {
    "model_cd": "VIXE",
    "model_dsc": "VIXEN",
    "make_cd": "TVR"
  },
  {
    "model_cd": "TK",
    "model_dsc": "CCMV",
    "make_cd": "UAZ"
  },
  {
    "model_cd": "LTC",
    "model_dsc": "LECTRIC LEOPARD",
    "make_cd": "USEL"
  },
  {
    "model_cd": "M12",
    "model_dsc": "M12 (SPORTS COUPE)",
    "make_cd": "VACR"
  },
  {
    "model_cd": "VECT",
    "model_dsc": "VECTOR",
    "make_cd": "VACR"
  },
  {
    "model_cd": "DEL",
    "model_dsc": "DELUXE",
    "make_cd": "VANG"
  },
  {
    "model_cd": "ENS",
    "model_dsc": "ENSIGN",
    "make_cd": "VANG"
  },
  {
    "model_cd": "LUX",
    "model_dsc": "LUXURY",
    "make_cd": "VANG"
  },
  {
    "model_cd": "MK3",
    "model_dsc": "MARK III",
    "make_cd": "VANG"
  },
  {
    "model_cd": "CRE",
    "model_dsc": "CRESTA",
    "make_cd": "VAUX"
  },
  {
    "model_cd": "ENVO",
    "model_dsc": "ENVOY",
    "make_cd": "VAUX"
  },
  {
    "model_cd": "EPIC",
    "model_dsc": "EPIC",
    "make_cd": "VAUX"
  },
  {
    "model_cd": "FIRE",
    "model_dsc": "FIRENZA",
    "make_cd": "VAUX"
  },
  {
    "model_cd": "VEL",
    "model_dsc": "VELOX",
    "make_cd": "VAUX"
  },
  {
    "model_cd": "VICT",
    "model_dsc": "VICTOR",
    "make_cd": "VAUX"
  },
  {
    "model_cd": "VIVA",
    "model_dsc": "VIVA",
    "make_cd": "VAUX"
  },
  {
    "model_cd": "113",
    "model_dsc": "113",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "1200",
    "model_dsc": "1200",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "1300",
    "model_dsc": "1300",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "1500",
    "model_dsc": "1500",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "412",
    "model_dsc": "411/412",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "BEET",
    "model_dsc": "BEETLE",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "CABR",
    "model_dsc": "CABRIOLET",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "CORR",
    "model_dsc": "CORRADO",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "DAS",
    "model_dsc": "DASHER",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "EOS",
    "model_dsc": "EOS",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "EURO",
    "model_dsc": "EUROVAN",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "FAST",
    "model_dsc": "FASTBACK",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "FOX",
    "model_dsc": "FOX",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "GOLF",
    "model_dsc": "GOLF",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "GTI",
    "model_dsc": "GTI",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "JETT",
    "model_dsc": "JETTA",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "KARM",
    "model_dsc": "KARMANN GHIA",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "PASS",
    "model_dsc": "PASSAT",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "PHAE",
    "model_dsc": "PHAETON",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "POLO",
    "model_dsc": "POLO",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "QUAN",
    "model_dsc": "QUANTUM",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "RABB",
    "model_dsc": "RABBIT",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "ROUT",
    "model_dsc": "ROUTAN",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "SB",
    "model_dsc": "SQUAREBACK",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "SCIR",
    "model_dsc": "SCIROCCO",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "SUR",
    "model_dsc": "SUNROOF",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "THIN",
    "model_dsc": "THE THING",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "TIGU",
    "model_dsc": "TIGUAN",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "TOUA",
    "model_dsc": "TOUAREG",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "VANA",
    "model_dsc": "VANAGON",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "VAR",
    "model_dsc": "VARIANT",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "WEST",
    "model_dsc": "WESTFALIA",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "ATLA",
    "model_dsc": "ATLAS",
    "make_cd": "VOLK"
  },
  {
    "model_cd": "122",
    "model_dsc": "122 SERIES",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "140",
    "model_dsc": "140 SERIES",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "164",
    "model_dsc": "164 SERIES",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "180",
    "model_dsc": "1800 SERIES",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "190",
    "model_dsc": "P1900",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "200",
    "model_dsc": "200 SERIES",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "240",
    "model_dsc": "240 SERIES",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "245",
    "model_dsc": "245 SERIES",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "260",
    "model_dsc": "260 SERIES",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "444",
    "model_dsc": "PV444",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "544",
    "model_dsc": "PV544",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "740",
    "model_dsc": "740 SERIES",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "745",
    "model_dsc": "745 SERIES",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "760",
    "model_dsc": "760",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "765",
    "model_dsc": "765 SERIES",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "780",
    "model_dsc": "780 SERIES",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "850",
    "model_dsc": "850 SERIES",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "940",
    "model_dsc": "940",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "960",
    "model_dsc": "960",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "C30",
    "model_dsc": "C30",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "C70",
    "model_dsc": "C70",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "COB",
    "model_dsc": "COMBI",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "DL",
    "model_dsc": "DL",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "GL",
    "model_dsc": "GL",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "GLE",
    "model_dsc": "GLE",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "GLT",
    "model_dsc": "GLT",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "R4",
    "model_dsc": "R4",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "S40",
    "model_dsc": "S40",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "S60",
    "model_dsc": "S60",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "S70",
    "model_dsc": "S70",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "S80",
    "model_dsc": "S80",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "S90",
    "model_dsc": "S90",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "SPO",
    "model_dsc": "SPORT",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "V40",
    "model_dsc": "V40",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "V50",
    "model_dsc": "V50",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "V70",
    "model_dsc": "V70",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "V90",
    "model_dsc": "V90",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "XC70",
    "model_dsc": "XC70",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "XC90",
    "model_dsc": "XC90",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "XC60",
    "model_dsc": "XC60",
    "make_cd": "VOLV"
  },
  {
    "model_cd": "YUG",
    "model_dsc": "YUGO (SERIES)",
    "make_cd": "ZCZY"
  }
]

def upgrade():
    op.drop_table('vehicle_model')
    op.drop_table('vehicle_make')
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicle_make',
    sa.Column('make_cd', sa.String(), nullable=False, unique=False),
    sa.Column('make_dsc', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('make_cd')
    )
    op.create_table('vehicle_model',
    sa.Column('model_cd', sa.String(), nullable=False),
    sa.Column('model_dsc', sa.String(), nullable=False),
    sa.Column('make_cd', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['make_cd'], ['vehicle_make.make_cd'], ),
    )
    op.create_primary_key('vehicle_model_pkey', 'vehicle_model', ['make_cd', 'model_cd'])
    
    # Seed vehicle makes
    with op.get_context().autocommit_block():
        bind = op.get_bind()
        meta = sa.MetaData()
        meta.bind = bind
        meta.reflect(bind=bind, only=('vehicle_make',))
        vehicle_make = sa.Table('vehicle_make', meta)
        op.bulk_insert(vehicle_make, vehicle_makes)
        
    # Seed vehicle models
    with op.get_context().autocommit_block():
        bind = op.get_bind()
        meta = sa.MetaData()
        meta.bind = bind
        meta.reflect(bind=bind, only=('vehicle_model',))
        vehicle_model = sa.Table('vehicle_model', meta)
        op.bulk_insert(vehicle_model, vehicle_models)
    
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicle_model')
    op.drop_table('vehicle_make')
    # ### end Alembic commands ###
