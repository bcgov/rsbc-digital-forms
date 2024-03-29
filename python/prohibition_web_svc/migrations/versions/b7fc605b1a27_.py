"""empty message

Revision ID: b7fc605b1a27
Revises: 14107a12fd38
Create Date: 2023-12-21 14:35:27.461893

"""
from alembic import op
import sqlalchemy as sa


vehicle_data = [
  {
    "mk": "ABAR",
    "search": "ABARTH",
    "md": ""
  },
  {
    "mk": "AC",
    "search": "A C (GREAT BRITAIN)",
    "md": ""
  },
  {
    "mk": "ACAD",
    "search": "ACADIAN (GM OF CANADA)",
    "md": ""
  },
  {
    "mk": "ACUR",
    "search": "ACURA",
    "md": ""
  },
  {
    "mk": "ADET",
    "search": "ADETTE",
    "md": ""
  },
  {
    "mk": "ADVA",
    "search": "ADVANCED",
    "md": ""
  },
  {
    "mk": "AERO",
    "search": "AEROCAR",
    "md": ""
  },
  {
    "mk": "AETA",
    "search": "AETA",
    "md": ""
  },
  {
    "mk": "ALCI",
    "search": "ALLEN COACHWORKS INC.",
    "md": ""
  },
  {
    "mk": "ALFA",
    "search": "ALFA ROMEO",
    "md": ""
  },
  {
    "mk": "ALLA",
    "search": "ALLARD",
    "md": ""
  },
  {
    "mk": "ALLF",
    "search": "ALLISONS FIBERGLASS MFG.INC.",
    "md": ""
  },
  {
    "mk": "ALLS",
    "search": "ALL STATE",
    "md": ""
  },
  {
    "mk": "ALMA",
    "search": "ALMA",
    "md": ""
  },
  {
    "mk": "ALPI",
    "search": "ALPHINE",
    "md": ""
  },
  {
    "mk": "ALTA",
    "search": "ALTA",
    "md": ""
  },
  {
    "mk": "ALVI",
    "search": "ALVIS",
    "md": ""
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS",
    "md": ""
  },
  {
    "mk": "AMPH",
    "search": "AMPHICAR",
    "md": ""
  },
  {
    "mk": "ANSE",
    "search": "ANSER MANUFACTURING LTD",
    "md": ""
  },
  {
    "mk": "ARGO",
    "search": "ARGONAUT STATE LIMOUSINE",
    "md": ""
  },
  {
    "mk": "ARIS",
    "search": "ARISTA",
    "md": ""
  },
  {
    "mk": "ARMS",
    "search": "ARMSTRONG SIDDELEY",
    "md": ""
  },
  {
    "mk": "ARNO",
    "search": "ARNOLT-BRISTOL",
    "md": ""
  },
  {
    "mk": "ASA",
    "search": "ASA",
    "md": ""
  },
  {
    "mk": "ASCO",
    "search": "ASCORT",
    "md": ""
  },
  {
    "mk": "ASHL",
    "search": "ASHLEY",
    "md": ""
  },
  {
    "mk": "ASTO",
    "search": "ASTON-MARTIN",
    "md": ""
  },
  {
    "mk": "ASUN",
    "search": "ASUNA",
    "md": ""
  },
  {
    "mk": "ASVE",
    "search": "ASSEMBLED VEHICLE",
    "md": ""
  },
  {
    "mk": "AUBU",
    "search": "AUBURN",
    "md": ""
  },
  {
    "mk": "AUDI",
    "search": "AUDI",
    "md": ""
  },
  {
    "mk": "AUKR",
    "search": "AUTOKRAFT",
    "md": ""
  },
  {
    "mk": "AURO",
    "search": "AURORA",
    "md": ""
  },
  {
    "mk": "AUST",
    "search": "AUSTIN-HEALY",
    "md": ""
  },
  {
    "mk": "AUTA",
    "search": "AUTOBIANCHI",
    "md": ""
  },
  {
    "mk": "AUTB",
    "search": "AUTOBIEU",
    "md": ""
  },
  {
    "mk": "AUTO",
    "search": "AUTOCAR",
    "md": ""
  },
  {
    "mk": "AUTR",
    "search": "AUTOCARRIER AND A.C.",
    "md": ""
  },
  {
    "mk": "AUTU",
    "search": "AUTO UNION",
    "md": ""
  },
  {
    "mk": "AVAN",
    "search": "AVANTI",
    "md": ""
  },
  {
    "mk": "AVEN",
    "search": "AVENGER",
    "md": ""
  },
  {
    "mk": "AVIA",
    "search": "AVIA",
    "md": ""
  },
  {
    "mk": "BANT",
    "search": "BANTAM",
    "md": ""
  },
  {
    "mk": "BAY",
    "search": "BAYLINER",
    "md": ""
  },
  {
    "mk": "BEAR",
    "search": "BEARDMORE",
    "md": ""
  },
  {
    "mk": "BEDF",
    "search": "BEDFORD",
    "md": ""
  },
  {
    "mk": "BEJE",
    "search": "BEIJING JEEP",
    "md": ""
  },
  {
    "mk": "BENT",
    "search": "BENTLEY",
    "md": ""
  },
  {
    "mk": "BERG",
    "search": "BERGANTINE",
    "md": ""
  },
  {
    "mk": "BERK",
    "search": "BERKELEY",
    "md": ""
  },
  {
    "mk": "BERO",
    "search": "BERTONE",
    "md": ""
  },
  {
    "mk": "BESA",
    "search": "BESASIE AUTOMOBILE CO. INC.",
    "md": ""
  },
  {
    "mk": "BIGT",
    "search": "BIG TEX",
    "md": ""
  },
  {
    "mk": "BITT",
    "search": "BITTER",
    "md": ""
  },
  {
    "mk": "BIZZ",
    "search": "BIZZARRINI",
    "md": ""
  },
  {
    "mk": "BLUE",
    "search": "BLUEBIRD",
    "md": ""
  },
  {
    "mk": "BMC",
    "search": "B M C",
    "md": ""
  },
  {
    "mk": "BMW",
    "search": "BMW",
    "md": ""
  },
  {
    "mk": "BOBB",
    "search": "BOBBI-KAR",
    "md": ""
  },
  {
    "mk": "BOCA",
    "search": "BOCAR",
    "md": ""
  },
  {
    "mk": "BOM",
    "search": "BOMBARDIER",
    "md": ""
  },
  {
    "mk": "BONA",
    "search": "BONAIR LEISURE PRODUCTS LTD.",
    "md": ""
  },
  {
    "mk": "BOND",
    "search": "BOND",
    "md": ""
  },
  {
    "mk": "BORG",
    "search": "BORGWARD",
    "md": ""
  },
  {
    "mk": "BOS",
    "search": "BOSTON WHALER",
    "md": ""
  },
  {
    "mk": "BRAS",
    "search": "BRASINCA",
    "md": ""
  },
  {
    "mk": "BRDL",
    "search": "BRADLEY GT",
    "md": ""
  },
  {
    "mk": "BREM",
    "search": "BREMEN SPORT EQUIPMENT",
    "md": ""
  },
  {
    "mk": "BRIC",
    "search": "BRICKLIN",
    "md": ""
  },
  {
    "mk": "BRIS",
    "search": "BRISTOL",
    "md": ""
  },
  {
    "mk": "BROD",
    "search": "BRODEX",
    "md": ""
  },
  {
    "mk": "BUEL",
    "search": "BUELL",
    "md": ""
  },
  {
    "mk": "BUGA",
    "search": "BUGATTI",
    "md": ""
  },
  {
    "mk": "BUIC",
    "search": "BUICK",
    "md": ""
  },
  {
    "mk": "BUTT",
    "search": "BUTTERFIELD MUSKETEER",
    "md": ""
  },
  {
    "mk": "BZEL",
    "search": "B & Z ELECTRIC CAR CO.",
    "md": ""
  },
  {
    "mk": "CADI",
    "search": "CADILLAC",
    "md": ""
  },
  {
    "mk": "CAM",
    "search": "CAMPION",
    "md": ""
  },
  {
    "mk": "CAPR",
    "search": "CAPRI",
    "md": ""
  },
  {
    "mk": "CASE",
    "search": "CASE",
    "md": ""
  },
  {
    "mk": "CATE",
    "search": "CATERPILLAR",
    "md": ""
  },
  {
    "mk": "CBTR",
    "search": "C & B TRAILER",
    "md": ""
  },
  {
    "mk": "CHA",
    "search": "CHAMPION",
    "md": ""
  },
  {
    "mk": "CHAI",
    "search": "CHAIKA",
    "md": ""
  },
  {
    "mk": "CHEC",
    "search": "CHECKER",
    "md": ""
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET",
    "md": ""
  },
  {
    "mk": "CHIN",
    "search": "CHING-KAN-SHAN",
    "md": ""
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER",
    "md": ""
  },
  {
    "mk": "CISI",
    "search": "CISITALIA",
    "md": ""
  },
  {
    "mk": "CITI",
    "search": "CITICAR (ELECTRIC CAR)",
    "md": ""
  },
  {
    "mk": "CITR",
    "search": "CITROEN",
    "md": ""
  },
  {
    "mk": "CLAC",
    "search": "CLASSIC ROADSTERS LTD.",
    "md": ""
  },
  {
    "mk": "CLAI",
    "search": "CLASSIC MOTOR CARRIAGES INC.",
    "md": ""
  },
  {
    "mk": "CLEN",
    "search": "CLENET COACH WORKS",
    "md": ""
  },
  {
    "mk": "CLUA",
    "search": "CLUA",
    "md": ""
  },
  {
    "mk": "CNTL",
    "search": "CONTINENTAL",
    "md": ""
  },
  {
    "mk": "COBR",
    "search": "AC COBRA",
    "md": ""
  },
  {
    "mk": "COCP",
    "search": "CONCEPTOR INDUSTRIES INC",
    "md": ""
  },
  {
    "mk": "COMV",
    "search": "COMMUTER VEHICLES INC",
    "md": ""
  },
  {
    "mk": "CONN",
    "search": "CONNAUGHT",
    "md": ""
  },
  {
    "mk": "CONS",
    "search": "CONSULIER",
    "md": ""
  },
  {
    "mk": "CONT",
    "search": "CONTESSA",
    "md": ""
  },
  {
    "mk": "CORD",
    "search": "CORD",
    "md": ""
  },
  {
    "mk": "CRI",
    "search": "CRISCRAFT",
    "md": ""
  },
  {
    "mk": "CROF",
    "search": "CROFTON CUB",
    "md": ""
  },
  {
    "mk": "CROS",
    "search": "CROSLEY",
    "md": ""
  },
  {
    "mk": "CUBS",
    "search": "CUBSTER",
    "md": ""
  },
  {
    "mk": "CUNN",
    "search": "CUNNINGHAM",
    "md": ""
  },
  {
    "mk": "DAEW",
    "search": "DAEWOO",
    "md": ""
  },
  {
    "mk": "DAF",
    "search": "DAF",
    "md": ""
  },
  {
    "mk": "DAIH",
    "search": "DAIHATSU",
    "md": ""
  },
  {
    "mk": "DAIM",
    "search": "DAIMLER",
    "md": ""
  },
  {
    "mk": "DAIN",
    "search": "D & A VEHICLES INC.",
    "md": ""
  },
  {
    "mk": "DATS",
    "search": "DATSUN",
    "md": ""
  },
  {
    "mk": "DAVI",
    "search": "DAVIS",
    "md": ""
  },
  {
    "mk": "DAYT",
    "search": "DAYTONA",
    "md": ""
  },
  {
    "mk": "DB",
    "search": "D.B.",
    "md": ""
  },
  {
    "mk": "DBL",
    "search": "DOUBLE EAGLE",
    "md": ""
  },
  {
    "mk": "DEBO",
    "search": "DEBONAIR",
    "md": ""
  },
  {
    "mk": "DECO",
    "search": "DECOURVILLE",
    "md": ""
  },
  {
    "mk": "DEEP",
    "search": "DEEP SANDERSON",
    "md": ""
  },
  {
    "mk": "DELL",
    "search": "DELLOW",
    "md": ""
  },
  {
    "mk": "DELO",
    "search": "DE LOREAN",
    "md": ""
  },
  {
    "mk": "DENZ",
    "search": "DENZEL",
    "md": ""
  },
  {
    "mk": "DESO",
    "search": "DESOTO",
    "md": ""
  },
  {
    "mk": "DETO",
    "search": "DETOMASO",
    "md": ""
  },
  {
    "mk": "DITE",
    "search": "DI TELLA",
    "md": ""
  },
  {
    "mk": "DIVA",
    "search": "DIVA",
    "md": ""
  },
  {
    "mk": "DKW",
    "search": "DKW",
    "md": ""
  },
  {
    "mk": "DODG",
    "search": "DODGE",
    "md": ""
  },
  {
    "mk": "DONG",
    "search": "DONG FENG  (EAST WIND)",
    "md": ""
  },
  {
    "mk": "DUCA",
    "search": "DUCATI",
    "md": ""
  },
  {
    "mk": "DUEL",
    "search": "DUEL",
    "md": ""
  },
  {
    "mk": "DUES",
    "search": "DUESENBERG",
    "md": ""
  },
  {
    "mk": "DURA",
    "search": "DURANT",
    "md": ""
  },
  {
    "mk": "DUTC",
    "search": "DUTCHMAN MANUFACTURING INC.",
    "md": ""
  },
  {
    "mk": "EAGL",
    "search": "EAGLE",
    "md": ""
  },
  {
    "mk": "EDSE",
    "search": "EDSEL",
    "md": ""
  },
  {
    "mk": "ELVA",
    "search": "ELVA",
    "md": ""
  },
  {
    "mk": "ELVC",
    "search": "ELECTRIC VEHICLE CORP.",
    "md": ""
  },
  {
    "mk": "EMW",
    "search": "EMW",
    "md": ""
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH)",
    "md": ""
  },
  {
    "mk": "ENVO",
    "search": "ENVOY",
    "md": ""
  },
  {
    "mk": "ENZM",
    "search": "ENZMANN",
    "md": ""
  },
  {
    "mk": "ERSK",
    "search": "ERSKINE",
    "md": ""
  },
  {
    "mk": "ESCO",
    "search": "ESCORT BOAT TRAILER MFG.",
    "md": ""
  },
  {
    "mk": "ESHL",
    "search": "ESHELMAN SPORTABOUT",
    "md": ""
  },
  {
    "mk": "ESSE",
    "search": "ESSEX",
    "md": ""
  },
  {
    "mk": "EVRY",
    "search": "EVERYBODYS MOTOR CAR MFG.",
    "md": ""
  },
  {
    "mk": "EXCA",
    "search": "EXCALIBUR",
    "md": ""
  },
  {
    "mk": "EZLO",
    "search": "EZ LOADER BOAT TRAILERS INC.",
    "md": ""
  },
  {
    "mk": "FACE",
    "search": "FACEL VEGA",
    "md": ""
  },
  {
    "mk": "FAIR",
    "search": "FAIRTHORPE",
    "md": ""
  },
  {
    "mk": "FALC",
    "search": "FALCON (BRITISH)",
    "md": ""
  },
  {
    "mk": "FELB",
    "search": "FELBER",
    "md": ""
  },
  {
    "mk": "FERR",
    "search": "FERRARI",
    "md": ""
  },
  {
    "mk": "FIAA",
    "search": "FIAT-ABARTH",
    "md": ""
  },
  {
    "mk": "FIAT",
    "search": "FIAT",
    "md": ""
  },
  {
    "mk": "FIBE",
    "search": "FIBERFAB INC. (MINNEAPOLIS MN)",
    "md": ""
  },
  {
    "mk": "FIES",
    "search": "FIESTA (IMPORTED BY FORD)",
    "md": ""
  },
  {
    "mk": "FISK",
    "search": "FISKER",
    "md": ""
  },
  {
    "mk": "FLEE",
    "search": "FLEETWOOD ENTERPRISES INC",
    "md": ""
  },
  {
    "mk": "FLYE",
    "search": "FLYER",
    "md": ""
  },
  {
    "mk": "FNM",
    "search": "FNM",
    "md": ""
  },
  {
    "mk": "FORD",
    "search": "FORD",
    "md": ""
  },
  {
    "mk": "FOUN",
    "search": "FOUNTAIN",
    "md": ""
  },
  {
    "mk": "FRAN",
    "search": "FRANKLIN",
    "md": ""
  },
  {
    "mk": "FRAZ",
    "search": "FRAZIER",
    "md": ""
  },
  {
    "mk": "FREF",
    "search": "FRENCH FORD",
    "md": ""
  },
  {
    "mk": "FREI",
    "search": "FREIGHTLINER",
    "md": ""
  },
  {
    "mk": "FRIS",
    "search": "FRISKY",
    "md": ""
  },
  {
    "mk": "FRNA",
    "search": "FRAZER-NASH",
    "md": ""
  },
  {
    "mk": "GAZ",
    "search": "GAZ",
    "md": ""
  },
  {
    "mk": "GDNE",
    "search": "GREAT DANE",
    "md": ""
  },
  {
    "mk": "GENE",
    "search": "GENESIS",
    "md": ""
  },
  {
    "mk": "GEO",
    "search": "GEO",
    "md": ""
  },
  {
    "mk": "GIAN",
    "search": "GIANNINI",
    "md": ""
  },
  {
    "mk": "GILB",
    "search": "GILBERN",
    "md": ""
  },
  {
    "mk": "GINE",
    "search": "GINETTA",
    "md": ""
  },
  {
    "mk": "GITA",
    "search": "GITANE",
    "md": ""
  },
  {
    "mk": "GLAS",
    "search": "GLAS",
    "md": ""
  },
  {
    "mk": "GLSC",
    "search": "GLASSIC",
    "md": ""
  },
  {
    "mk": "GM",
    "search": "GENERAL MOTORS",
    "md": ""
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP.",
    "md": ""
  },
  {
    "mk": "GOLI",
    "search": "GOLIATH",
    "md": ""
  },
  {
    "mk": "GORD",
    "search": "GORDON",
    "md": ""
  },
  {
    "mk": "GRAC",
    "search": "GRACIELA",
    "md": ""
  },
  {
    "mk": "GRAH",
    "search": "GRAHAM",
    "md": ""
  },
  {
    "mk": "GRAP",
    "search": "GRAHAM-PAIGE",
    "md": ""
  },
  {
    "mk": "GRIF",
    "search": "GRIFFITH",
    "md": ""
  },
  {
    "mk": "GSM",
    "search": "GSM",
    "md": ""
  },
  {
    "mk": "GZL",
    "search": "GAZELLE",
    "md": ""
  },
  {
    "mk": "HAN",
    "search": "HANS CHRISTIAN",
    "md": ""
  },
  {
    "mk": "HAR",
    "search": "HARBORCRAFT",
    "md": ""
  },
  {
    "mk": "HARL",
    "search": "HARLEY DAVIDSON",
    "md": ""
  },
  {
    "mk": "HARM",
    "search": "HARMON TANK CO. INC.",
    "md": ""
  },
  {
    "mk": "HAUL",
    "search": "HAULMARK",
    "md": ""
  },
  {
    "mk": "HEIN",
    "search": "HEINKEL",
    "md": ""
  },
  {
    "mk": "HENR",
    "search": "HENRY J.",
    "md": ""
  },
  {
    "mk": "HICK",
    "search": "HICKEY TRAIL-BLAZER",
    "md": ""
  },
  {
    "mk": "HIGH",
    "search": "HIGHLINER",
    "md": ""
  },
  {
    "mk": "HILL",
    "search": "HILLMAN",
    "md": ""
  },
  {
    "mk": "HIND",
    "search": "HINDUSTAN",
    "md": ""
  },
  {
    "mk": "HINO",
    "search": "HINO",
    "md": ""
  },
  {
    "mk": "HOB",
    "search": "HOBIE CAT",
    "md": ""
  },
  {
    "mk": "HOLD",
    "search": "HOLDEN",
    "md": ""
  },
  {
    "mk": "HOND",
    "search": "HONDA",
    "md": ""
  },
  {
    "mk": "HONG",
    "search": "HONGKI OR HONG-CHI",
    "md": ""
  },
  {
    "mk": "HORC",
    "search": "HORCH LIMOUSINE",
    "md": ""
  },
  {
    "mk": "HOTC",
    "search": "HOTCHKISS",
    "md": ""
  },
  {
    "mk": "HRG",
    "search": "HRG",
    "md": ""
  },
  {
    "mk": "HUDS",
    "search": "HUDSON",
    "md": ""
  },
  {
    "mk": "HUMB",
    "search": "HUMBER",
    "md": ""
  },
  {
    "mk": "HUME",
    "search": "HUMBEE SURREY",
    "md": ""
  },
  {
    "mk": "HUMM",
    "search": "HUMMER",
    "md": ""
  },
  {
    "mk": "HUPM",
    "search": "HUPMOBILE",
    "md": ""
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI",
    "md": ""
  },
  {
    "mk": "IAME",
    "search": "I.A.M.E.",
    "md": ""
  },
  {
    "mk": "IKA",
    "search": "I.K.A.",
    "md": ""
  },
  {
    "mk": "IMPB",
    "search": "I.M.P. (U.S.)",
    "md": ""
  },
  {
    "mk": "IMPE",
    "search": "IMPERIAL",
    "md": ""
  },
  {
    "mk": "INFI",
    "search": "INFINITI",
    "md": ""
  },
  {
    "mk": "INME",
    "search": "INTERMECCANICA",
    "md": ""
  },
  {
    "mk": "INNO",
    "search": "INNOCENTI",
    "md": ""
  },
  {
    "mk": "INTE",
    "search": "INTERNATIONAL",
    "md": ""
  },
  {
    "mk": "ISET",
    "search": "ISETTA",
    "md": ""
  },
  {
    "mk": "ISO",
    "search": "ISO",
    "md": ""
  },
  {
    "mk": "ISUZ",
    "search": "ISUZU",
    "md": ""
  },
  {
    "mk": "ITAF",
    "search": "ITALIAN FORD",
    "md": ""
  },
  {
    "mk": "ITAI",
    "search": "ITALIA",
    "md": ""
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR",
    "md": ""
  },
  {
    "mk": "JEEP",
    "search": "JEEP",
    "md": ""
  },
  {
    "mk": "JENS",
    "search": "JENSEN",
    "md": ""
  },
  {
    "mk": "JETM",
    "search": "JETMOBILE",
    "md": ""
  },
  {
    "mk": "JOHN",
    "search": "JOHN DEERE",
    "md": ""
  },
  {
    "mk": "JOWE",
    "search": "JOWETT",
    "md": ""
  },
  {
    "mk": "KAIS",
    "search": "KAISER",
    "md": ""
  },
  {
    "mk": "KAWA",
    "search": "KAWASAKI",
    "md": ""
  },
  {
    "mk": "KENW",
    "search": "KENWORTH",
    "md": ""
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION",
    "md": ""
  },
  {
    "mk": "KIMI",
    "search": "KING MIDGET",
    "md": ""
  },
  {
    "mk": "KIOT",
    "search": "KIOTI",
    "md": ""
  },
  {
    "mk": "KLIN",
    "search": "K-LINE",
    "md": ""
  },
  {
    "mk": "KNIG",
    "search": "KNIGHT",
    "md": ""
  },
  {
    "mk": "KUBO",
    "search": "KUBOTA",
    "md": ""
  },
  {
    "mk": "KURT",
    "search": "KURTIS KRAFT",
    "md": ""
  },
  {
    "mk": "LADA",
    "search": "LADA",
    "md": ""
  },
  {
    "mk": "LAGO",
    "search": "LAGONDA",
    "md": ""
  },
  {
    "mk": "LALL",
    "search": "LASALLE",
    "md": ""
  },
  {
    "mk": "LAMB",
    "search": "LAMBRETTA",
    "md": ""
  },
  {
    "mk": "LAMO",
    "search": "LAMBORGHINI",
    "md": ""
  },
  {
    "mk": "LANC",
    "search": "LANCHESTER",
    "md": ""
  },
  {
    "mk": "LAND",
    "search": "LAND ROVER",
    "md": ""
  },
  {
    "mk": "LASE",
    "search": "LASER",
    "md": ""
  },
  {
    "mk": "LDTR",
    "search": "LOAD TRAIL",
    "md": ""
  },
  {
    "mk": "LEAF",
    "search": "LEA-FRANCIS",
    "md": ""
  },
  {
    "mk": "LEXU",
    "search": "LEXUS",
    "md": ""
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL",
    "md": ""
  },
  {
    "mk": "LLOY",
    "search": "LLOYD",
    "md": ""
  },
  {
    "mk": "LNCI",
    "search": "LANCIA",
    "md": ""
  },
  {
    "mk": "LOCO",
    "search": "LOCOMOBILE",
    "md": ""
  },
  {
    "mk": "LOLA",
    "search": "LOLA",
    "md": ""
  },
  {
    "mk": "LOND",
    "search": "LONDON MOTORS",
    "md": ""
  },
  {
    "mk": "LONE",
    "search": "LONESTAR",
    "md": ""
  },
  {
    "mk": "LOOD",
    "search": "LOODCRAFT",
    "md": ""
  },
  {
    "mk": "LOTU",
    "search": "LOTUS",
    "md": ""
  },
  {
    "mk": "MACK",
    "search": "MACK",
    "md": ""
  },
  {
    "mk": "MAL",
    "search": "MALIBU",
    "md": ""
  },
  {
    "mk": "MANA",
    "search": "MANAC",
    "md": ""
  },
  {
    "mk": "MARC",
    "search": "MARCOS",
    "md": ""
  },
  {
    "mk": "MARM",
    "search": "MARMON",
    "md": ""
  },
  {
    "mk": "MAS",
    "search": "MASTERCRAFT",
    "md": ""
  },
  {
    "mk": "MASE",
    "search": "MASERATI",
    "md": ""
  },
  {
    "mk": "MASS",
    "search": "MASSEY FERGUSON",
    "md": ""
  },
  {
    "mk": "MATR",
    "search": "MATRA",
    "md": ""
  },
  {
    "mk": "MAXL",
    "search": "MAXWELL",
    "md": ""
  },
  {
    "mk": "MAZD",
    "search": "MAZDA",
    "md": ""
  },
  {
    "mk": "MBCC",
    "search": "MCBURNIE COACH CRAFT INC.",
    "md": ""
  },
  {
    "mk": "MBM",
    "search": "M.B.M.",
    "md": ""
  },
  {
    "mk": "MCI",
    "search": "MOTOR COACH INDUSTRIES",
    "md": ""
  },
  {
    "mk": "MCLA",
    "search": "MCLAREN",
    "md": ""
  },
  {
    "mk": "MEAN",
    "search": "MEAN",
    "md": ""
  },
  {
    "mk": "MERC",
    "search": "MERCURY",
    "md": ""
  },
  {
    "mk": "MERK",
    "search": "MERKUR",
    "md": ""
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ",
    "md": ""
  },
  {
    "mk": "MESS",
    "search": "MESSERSCHMITT",
    "md": ""
  },
  {
    "mk": "METE",
    "search": "METEOR (CANADIAN MERCURY)",
    "md": ""
  },
  {
    "mk": "METR",
    "search": "METROPOLITAN",
    "md": ""
  },
  {
    "mk": "MG",
    "search": "MG",
    "md": ""
  },
  {
    "mk": "MIKA",
    "search": "MIKASA",
    "md": ""
  },
  {
    "mk": "MIKR",
    "search": "MIKRUS",
    "md": ""
  },
  {
    "mk": "MINI",
    "search": "MINI",
    "md": ""
  },
  {
    "mk": "MIST",
    "search": "MISTRAL",
    "md": ""
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI",
    "md": ""
  },
  {
    "mk": "MODE",
    "search": "MODEL A & MODEL T MOTOR CAR REPRODUCTION CORP.",
    "md": ""
  },
  {
    "mk": "MONA",
    "search": "MONARCH",
    "md": ""
  },
  {
    "mk": "MONK",
    "search": "MONK",
    "md": ""
  },
  {
    "mk": "MORE",
    "search": "MORETTI",
    "md": ""
  },
  {
    "mk": "MORG",
    "search": "MORGAN",
    "md": ""
  },
  {
    "mk": "MORR",
    "search": "MORRIS",
    "md": ""
  },
  {
    "mk": "MOSK",
    "search": "MOSKOVITCH",
    "md": ""
  },
  {
    "mk": "MOTO",
    "search": "MOTO GUZZI",
    "md": ""
  },
  {
    "mk": "MUNT",
    "search": "MUNTZ",
    "md": ""
  },
  {
    "mk": "MURE",
    "search": "MURENA",
    "md": ""
  },
  {
    "mk": "MZMA",
    "search": "MZMA",
    "md": ""
  },
  {
    "mk": "NAHA",
    "search": "NAHANNI MANUFACTURING LTD",
    "md": ""
  },
  {
    "mk": "NAHE",
    "search": "NASH-HEALY",
    "md": ""
  },
  {
    "mk": "NARD",
    "search": "NARDI-DANESE",
    "md": ""
  },
  {
    "mk": "NASH",
    "search": "NASH",
    "md": ""
  },
  {
    "mk": "NECK",
    "search": "NECKAR",
    "md": ""
  },
  {
    "mk": "NEFL",
    "search": "NEW FLYER",
    "md": ""
  },
  {
    "mk": "NEWM",
    "search": "NEWMAR",
    "md": ""
  },
  {
    "mk": "NISS",
    "search": "NISSAN",
    "md": ""
  },
  {
    "mk": "NORT",
    "search": "NORTHWOOD MANUFACTURING",
    "md": ""
  },
  {
    "mk": "NOVA",
    "search": "NOVABUS",
    "md": ""
  },
  {
    "mk": "NSU",
    "search": "NSU PRINZ",
    "md": ""
  },
  {
    "mk": "NSUF",
    "search": "NSU-FIAT",
    "md": ""
  },
  {
    "mk": "OAKL",
    "search": "OAKLAND",
    "md": ""
  },
  {
    "mk": "OGLE",
    "search": "OGLE",
    "md": ""
  },
  {
    "mk": "OHTA",
    "search": "OHTA",
    "md": ""
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE",
    "md": ""
  },
  {
    "mk": "OMEG",
    "search": "OMEGA (ITALIAN)",
    "md": ""
  },
  {
    "mk": "OPEL",
    "search": "OPEL",
    "md": ""
  },
  {
    "mk": "OPER",
    "search": "OPEN ROADSTERS OF TEXAS",
    "md": ""
  },
  {
    "mk": "ORIO",
    "search": "ORION BUS INDUSTRIES",
    "md": ""
  },
  {
    "mk": "OSCA",
    "search": "OSCA",
    "md": ""
  },
  {
    "mk": "OSI",
    "search": "OSI",
    "md": ""
  },
  {
    "mk": "OTOS",
    "search": "OTOSAN",
    "md": ""
  },
  {
    "mk": "OVER",
    "search": "OVERLAND",
    "md": ""
  },
  {
    "mk": "PACK",
    "search": "PACKARD",
    "md": ""
  },
  {
    "mk": "PALL",
    "search": "PALLISER (RACING CAR)",
    "md": ""
  },
  {
    "mk": "PANE",
    "search": "PANTHER WESTWINDS LTD.",
    "md": ""
  },
  {
    "mk": "PANH",
    "search": "PANHARD",
    "md": ""
  },
  {
    "mk": "PANZ",
    "search": "PANOZ AUTO DEVELOPMENT",
    "md": ""
  },
  {
    "mk": "PASS",
    "search": "PASSPORT",
    "md": ""
  },
  {
    "mk": "PEAC",
    "search": "PEACE",
    "md": ""
  },
  {
    "mk": "PEEL",
    "search": "PEEL",
    "md": ""
  },
  {
    "mk": "PEER",
    "search": "PEERLESS",
    "md": ""
  },
  {
    "mk": "PEGA",
    "search": "PEGASO",
    "md": ""
  },
  {
    "mk": "PETE",
    "search": "PETERBILT",
    "md": ""
  },
  {
    "mk": "PEUG",
    "search": "PEUGEOT",
    "md": ""
  },
  {
    "mk": "PHOE",
    "search": "PHOENIX",
    "md": ""
  },
  {
    "mk": "PIAG",
    "search": "PIAGGIO",
    "md": ""
  },
  {
    "mk": "PINI",
    "search": "PINIFARINA",
    "md": ""
  },
  {
    "mk": "PJ",
    "search": "PJ",
    "md": ""
  },
  {
    "mk": "PLAY",
    "search": "PLAYBOY",
    "md": ""
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH",
    "md": ""
  },
  {
    "mk": "POIR",
    "search": "POIRIER",
    "md": ""
  },
  {
    "mk": "POLE",
    "search": "POLESTAR",
    "md": ""
  },
  {
    "mk": "PONT",
    "search": "PONTIAC",
    "md": ""
  },
  {
    "mk": "PORS",
    "search": "PORSCHE",
    "md": ""
  },
  {
    "mk": "PRAI",
    "search": "PRAIRIE SCHOONER",
    "md": ""
  },
  {
    "mk": "PRCA",
    "search": "PIERCE ARROW",
    "md": ""
  },
  {
    "mk": "PRMO",
    "search": "PRINCE MOTORS",
    "md": ""
  },
  {
    "mk": "PROG",
    "search": "PROGRESS",
    "md": ""
  },
  {
    "mk": "PTV",
    "search": "PTV",
    "md": ""
  },
  {
    "mk": "PUCH",
    "search": "PUCH",
    "md": ""
  },
  {
    "mk": "PUMM",
    "search": "PUMA",
    "md": ""
  },
  {
    "mk": "RAM",
    "search": "RAM",
    "md": ""
  },
  {
    "mk": "RAMB",
    "search": "RAMBLER",
    "md": ""
  },
  {
    "mk": "RAMS",
    "search": "RAMSES",
    "md": ""
  },
  {
    "mk": "RAY",
    "search": "SEARAY",
    "md": ""
  },
  {
    "mk": "REI",
    "search": "REINELL",
    "md": ""
  },
  {
    "mk": "RELI",
    "search": "RELIANT",
    "md": ""
  },
  {
    "mk": "RENA",
    "search": "RENAULT",
    "md": ""
  },
  {
    "mk": "REO",
    "search": "REO",
    "md": ""
  },
  {
    "mk": "REXH",
    "search": "REXHALL",
    "md": ""
  },
  {
    "mk": "RILE",
    "search": "RILEY",
    "md": ""
  },
  {
    "mk": "RIND",
    "search": "RICH INDUSTRIES",
    "md": ""
  },
  {
    "mk": "RIVI",
    "search": "RIVIAN",
    "md": ""
  },
  {
    "mk": "ROAD",
    "search": "ROADRUNNER TRAILERS MFG.",
    "md": ""
  },
  {
    "mk": "ROCH",
    "search": "ROCHDALE",
    "md": ""
  },
  {
    "mk": "ROK",
    "search": "ROCKNE",
    "md": ""
  },
  {
    "mk": "ROLL",
    "search": "ROLLS-ROYCE",
    "md": ""
  },
  {
    "mk": "ROOT",
    "search": "ROOTES",
    "md": ""
  },
  {
    "mk": "ROVE",
    "search": "ROVER",
    "md": ""
  },
  {
    "mk": "RYCS",
    "search": "RYCSA",
    "md": ""
  },
  {
    "mk": "SAAB",
    "search": "SAAB",
    "md": ""
  },
  {
    "mk": "SABR",
    "search": "SABRA",
    "md": ""
  },
  {
    "mk": "SANG",
    "search": "SANGYONG",
    "md": ""
  },
  {
    "mk": "SATU",
    "search": "SATURN",
    "md": ""
  },
  {
    "mk": "SCIO",
    "search": "SCION",
    "md": ""
  },
  {
    "mk": "SEA",
    "search": "SEADOO",
    "md": ""
  },
  {
    "mk": "SEAT",
    "search": "SEAT",
    "md": ""
  },
  {
    "mk": "SERA",
    "search": "SERA",
    "md": ""
  },
  {
    "mk": "SHEB",
    "search": "SHELBY AMERICAN",
    "md": ""
  },
  {
    "mk": "SIAT",
    "search": "SIATA",
    "md": ""
  },
  {
    "mk": "SILA",
    "search": "SILA AUTORETTA",
    "md": ""
  },
  {
    "mk": "SIM",
    "search": "SIMCA",
    "md": ""
  },
  {
    "mk": "SIN",
    "search": "SINGER",
    "md": ""
  },
  {
    "mk": "SKI",
    "search": "SKI NAUTIQUE",
    "md": ""
  },
  {
    "mk": "SKOD",
    "search": "SKODA",
    "md": ""
  },
  {
    "mk": "SMAR",
    "search": "SMART",
    "md": ""
  },
  {
    "mk": "SNOW",
    "search": "SNOWBEAR LIMITED",
    "md": ""
  },
  {
    "mk": "SOUT",
    "search": "SOUTHLAND",
    "md": ""
  },
  {
    "mk": "SOVA",
    "search": "SOVAM",
    "md": ""
  },
  {
    "mk": "SPAR",
    "search": "SPARTAN",
    "md": ""
  },
  {
    "mk": "STAN",
    "search": "STANDARD",
    "md": ""
  },
  {
    "mk": "STAR",
    "search": "STAR",
    "md": ""
  },
  {
    "mk": "STEW",
    "search": "STEWART",
    "md": ""
  },
  {
    "mk": "STEY",
    "search": "STEYR-PUCH",
    "md": ""
  },
  {
    "mk": "STLG",
    "search": "STERLING",
    "md": ""
  },
  {
    "mk": "STLY",
    "search": "STANLEY",
    "md": ""
  },
  {
    "mk": "STRA",
    "search": "STRALE",
    "md": ""
  },
  {
    "mk": "STUD",
    "search": "STUDEBAKER",
    "md": ""
  },
  {
    "mk": "STUZ",
    "search": "STUTZ",
    "md": ""
  },
  {
    "mk": "SUBA",
    "search": "SUBARU",
    "md": ""
  },
  {
    "mk": "SUNB",
    "search": "SUNBEAM",
    "md": ""
  },
  {
    "mk": "SUPT",
    "search": "SUPER TWO",
    "md": ""
  },
  {
    "mk": "SUZL",
    "search": "SUZULIGHT SU",
    "md": ""
  },
  {
    "mk": "SUZU",
    "search": "SUZUKI",
    "md": ""
  },
  {
    "mk": "SYRE",
    "search": "SYRENA",
    "md": ""
  },
  {
    "mk": "TAMA",
    "search": "TAMA",
    "md": ""
  },
  {
    "mk": "TATR",
    "search": "TATRA",
    "md": ""
  },
  {
    "mk": "TAUN",
    "search": "TAUNUS (GERMAN FORD)",
    "md": ""
  },
  {
    "mk": "TCHA",
    "search": "TCHAIKA",
    "md": ""
  },
  {
    "mk": "TESL",
    "search": "TESLA MOTORS",
    "md": ""
  },
  {
    "mk": "THOM",
    "search": "THOMAS",
    "md": ""
  },
  {
    "mk": "THOR",
    "search": "THOR INDUSTRIES INC.",
    "md": ""
  },
  {
    "mk": "THUN",
    "search": "THUNDERJET",
    "md": ""
  },
  {
    "mk": "TITA",
    "search": "TITAN MOTORCYCLE CO.",
    "md": ""
  },
  {
    "mk": "TJAA",
    "search": "TJAARDA",
    "md": ""
  },
  {
    "mk": "TORN",
    "search": "TORNADO (BRITISH)",
    "md": ""
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA",
    "md": ""
  },
  {
    "mk": "TOYP",
    "search": "TOYOPET",
    "md": ""
  },
  {
    "mk": "TRAB",
    "search": "TRABANT",
    "md": ""
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH",
    "md": ""
  },
  {
    "mk": "TROJ",
    "search": "TROJAN",
    "md": ""
  },
  {
    "mk": "TRPE",
    "search": "TERRAPLANE",
    "md": ""
  },
  {
    "mk": "TUCK",
    "search": "TUCKER",
    "md": ""
  },
  {
    "mk": "TURN",
    "search": "TURNER",
    "md": ""
  },
  {
    "mk": "TVR",
    "search": "TVR",
    "md": ""
  },
  {
    "mk": "TZ",
    "search": "TZ",
    "md": ""
  },
  {
    "mk": "UAZ",
    "search": "UAZ (ULIANOVSK AUTOMOBILE ZAVOD)",
    "md": ""
  },
  {
    "mk": "UBUI",
    "search": "U-BUILT",
    "md": ""
  },
  {
    "mk": "UNIC",
    "search": "UNICAR",
    "md": ""
  },
  {
    "mk": "UNIP",
    "search": "UNIPOWER",
    "md": ""
  },
  {
    "mk": "USEL",
    "search": "U.S. ELECTRICAR CORP.",
    "md": ""
  },
  {
    "mk": "UTIL",
    "search": "UTILITY",
    "md": ""
  },
  {
    "mk": "VACR",
    "search": "VECTOR AEROMOTIVE CORPORATION",
    "md": ""
  },
  {
    "mk": "VAL",
    "search": "VAL",
    "md": ""
  },
  {
    "mk": "VALK",
    "search": "VALKRIE",
    "md": ""
  },
  {
    "mk": "VANG",
    "search": "VANGUARD (CANADA)",
    "md": ""
  },
  {
    "mk": "VAUX",
    "search": "VAUXHALL",
    "md": ""
  },
  {
    "mk": "VEAM",
    "search": "VEHICULOS AUTOMORES MEXICANO",
    "md": ""
  },
  {
    "mk": "VERI",
    "search": "VERITAS",
    "md": ""
  },
  {
    "mk": "VESP",
    "search": "VESPA",
    "md": ""
  },
  {
    "mk": "VNDN",
    "search": "VANDEN PLAS",
    "md": ""
  },
  {
    "mk": "VOGA",
    "search": "VOLGA",
    "md": ""
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN",
    "md": ""
  },
  {
    "mk": "VOLV",
    "search": "VOLVO",
    "md": ""
  },
  {
    "mk": "WABA",
    "search": "WABASH",
    "md": ""
  },
  {
    "mk": "WARS",
    "search": "WARSZAWA",
    "md": ""
  },
  {
    "mk": "WART",
    "search": "WARTBURG",
    "md": ""
  },
  {
    "mk": "WARW",
    "search": "WARWICK",
    "md": ""
  },
  {
    "mk": "WATF",
    "search": "WATFORD",
    "md": ""
  },
  {
    "mk": "WEND",
    "search": "WENDAX",
    "md": ""
  },
  {
    "mk": "WEST",
    "search": "WESTERN STAR",
    "md": ""
  },
  {
    "mk": "WHIP",
    "search": "WHIPPET",
    "md": ""
  },
  {
    "mk": "WILS",
    "search": "WILSON",
    "md": ""
  },
  {
    "mk": "WINN",
    "search": "WINNEBEGO",
    "md": ""
  },
  {
    "mk": "WLLS",
    "search": "WILLYS",
    "md": ""
  },
  {
    "mk": "WOLS",
    "search": "WOLSELEY",
    "md": ""
  },
  {
    "mk": "WOOD",
    "search": "WOODILL WILDFIRE",
    "md": ""
  },
  {
    "mk": "WORT",
    "search": "WORTHINGTON CHAMP",
    "md": ""
  },
  {
    "mk": "YAMA",
    "search": "YAMAHA",
    "md": ""
  },
  {
    "mk": "YENK",
    "search": "YENKO",
    "md": ""
  },
  {
    "mk": "YLN",
    "search": "YLN (YUE LOONG MOTOR CO.)",
    "md": ""
  },
  {
    "mk": "ZAPO",
    "search": "ZAPOROZHETS",
    "md": ""
  },
  {
    "mk": "ZARC",
    "search": "ZAR CAR",
    "md": ""
  },
  {
    "mk": "ZCZY",
    "search": "ZASTAVIA (ZCZ-YUGOSLAVIA)",
    "md": ""
  },
  {
    "mk": "ZETA",
    "search": "ZETA",
    "md": ""
  },
  {
    "mk": "ZIL",
    "search": "ZIL",
    "md": ""
  },
  {
    "mk": "ZIM",
    "search": "ZIM",
    "md": ""
  },
  {
    "mk": "ZIMR",
    "search": "ZIMMERMAN AUTOMOBILES",
    "md": ""
  },
  {
    "mk": "ZUND",
    "search": "ZUNDAPP",
    "md": ""
  },
  {
    "mk": "ZWIC",
    "search": "ZWICKAU",
    "md": ""
  },
  {
    "mk": "AC",
    "search": "A C (GREAT BRITAIN) - 3000 ME",
    "md": "300"
  },
  {
    "mk": "ACAD",
    "search": "ACADIAN (GM OF CANADA) - BEAUMONT SERIES",
    "md": "BEAU"
  },
  {
    "mk": "ACAD",
    "search": "ACADIAN (GM OF CANADA) - CANSO SERIES",
    "md": "CANS"
  },
  {
    "mk": "ACAD",
    "search": "ACADIAN (GM OF CANADA) - INVADER SERIES",
    "md": "INVA"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - 1.6 EL",
    "md": "1.6E"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - 1.7 EL",
    "md": "1.7E"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - 2.3",
    "md": "2.3"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - 2.5 TL",
    "md": "2.5T"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - 3.2 TL",
    "md": "3.2T"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - 3.5 RL",
    "md": "3.5R"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - TL",
    "md": "ATL"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - CL (SPORTS COUPE)",
    "md": "CL"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - CSX",
    "md": "CSX"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - EL",
    "md": "EL"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - ILX",
    "md": "ILX"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - INTEGRA",
    "md": "INTE"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - LEGEND",
    "md": "LEGE"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - MDX",
    "md": "MDX"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - NSX",
    "md": "NSX"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - RDX",
    "md": "RDX"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - RL",
    "md": "RL"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - RSX",
    "md": "RSX"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - SLX (SPORTS UTILITY)",
    "md": "SLX"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - TLX",
    "md": "TLX"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - TSX",
    "md": "TSX"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - VIGOR",
    "md": "VIGO"
  },
  {
    "mk": "ACUR",
    "search": "ACURA - 3.2CL",
    "md": "3.2C"
  },
  {
    "mk": "ALFA",
    "search": "ALFA ROMEO - 164",
    "md": "164"
  },
  {
    "mk": "ALFA",
    "search": "ALFA ROMEO - ALFETTA GT",
    "md": "AGT"
  },
  {
    "mk": "ALFA",
    "search": "ALFA ROMEO - ARNA",
    "md": "ARN"
  },
  {
    "mk": "ALFA",
    "search": "ALFA ROMEO - BERLINA",
    "md": "BERL"
  },
  {
    "mk": "ALFA",
    "search": "ALFA ROMEO - C4",
    "md": "C4"
  },
  {
    "mk": "ALFA",
    "search": "ALFA ROMEO - DUETTO",
    "md": "DUET"
  },
  {
    "mk": "ALFA",
    "search": "ALFA ROMEO - GTV6 2.5",
    "md": "G25"
  },
  {
    "mk": "ALFA",
    "search": "ALFA ROMEO - GIULIA",
    "md": "GIUL"
  },
  {
    "mk": "ALFA",
    "search": "ALFA ROMEO - ALFA GT6",
    "md": "GT6"
  },
  {
    "mk": "ALFA",
    "search": "ALFA ROMEO - MILANO",
    "md": "MILA"
  },
  {
    "mk": "ALFA",
    "search": "ALFA ROMEO - MONTREAL",
    "md": "MONT"
  },
  {
    "mk": "ALFA",
    "search": "ALFA ROMEO - GIULIA SPRINT",
    "md": "SPRI"
  },
  {
    "mk": "ALFA",
    "search": "ALFA ROMEO - SPIDER SERIES",
    "md": "SPYD"
  },
  {
    "mk": "ALFA",
    "search": "ALFA ROMEO - GT VELOCE",
    "md": "VELO"
  },
  {
    "mk": "ALFA",
    "search": "ALFA ROMEO - ZAGATO",
    "md": "ZAGA"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - ALLIANCE",
    "md": "ALLI"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - AMBASSADOR",
    "md": "AMBA"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - AMERICAN",
    "md": "AMER"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - AMX",
    "md": "AMX"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - CONCORD",
    "md": "CONC"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - EAGLE",
    "md": "EAGL"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - ENCORE",
    "md": "ENCO"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - GREMLIN",
    "md": "GREM"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - HORNET",
    "md": "HORN"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - JAVELIN",
    "md": "JAVE"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - MARLIN",
    "md": "MARL"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - MATADOR",
    "md": "MATA"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - MEDALLION",
    "md": "MEDA"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - PACER",
    "md": "PACE"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - RAMBLER",
    "md": "RAMB"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - REBEL",
    "md": "REBE"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - SPIRIT",
    "md": "SPIR"
  },
  {
    "mk": "AMER",
    "search": "AMERICAN MOTORS - SPORTABOUT",
    "md": "SPOR"
  },
  {
    "mk": "ASTO",
    "search": "ASTON-MARTIN - DB-5",
    "md": "DB5"
  },
  {
    "mk": "ASTO",
    "search": "ASTON-MARTIN - DB-6",
    "md": "DB6"
  },
  {
    "mk": "ASTO",
    "search": "ASTON-MARTIN - DB7(COUPE)",
    "md": "DB7"
  },
  {
    "mk": "ASTO",
    "search": "ASTON-MARTIN - LAGONDA",
    "md": "LAGO"
  },
  {
    "mk": "ASTO",
    "search": "ASTON-MARTIN - VANTAGE",
    "md": "VANT"
  },
  {
    "mk": "ASTO",
    "search": "ASTON-MARTIN - VIRAGE (SALOON)",
    "md": "VIR"
  },
  {
    "mk": "ASUN",
    "search": "ASUNA - GT",
    "md": "GT"
  },
  {
    "mk": "ASUN",
    "search": "ASUNA - SE",
    "md": "SE"
  },
  {
    "mk": "ASUN",
    "search": "ASUNA - SUNFIRE",
    "md": "SUNF"
  },
  {
    "mk": "ASUN",
    "search": "ASUNA - SUNRUNNER",
    "md": "SUNR"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - 100",
    "md": "100"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - 100GL",
    "md": "1GL"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - 100LS",
    "md": "1LS"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - 200LS",
    "md": "200"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - 4000",
    "md": "400"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - 5000",
    "md": "500"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - 850",
    "md": "850"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - A3",
    "md": "A3"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - A5",
    "md": "A5"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - A7",
    "md": "A7"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - 80",
    "md": "A80"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - 90",
    "md": "A90"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - A4",
    "md": "AA4"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - A6",
    "md": "AA6"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - A8",
    "md": "AA8"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - AS4",
    "md": "AS4"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - S6",
    "md": "AS6"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - AVANT",
    "md": "AVA"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - CABRIOLET",
    "md": "CABR"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - E-TRON",
    "md": "ETRO"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - 80 LS (FOX)",
    "md": "FOX"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - Q3",
    "md": "Q3"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - Q5",
    "md": "Q5"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - Q7",
    "md": "Q7"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - Q8",
    "md": "Q8"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - QUATTRO",
    "md": "QUAT"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - R8",
    "md": "R8"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - RS5",
    "md": "RS5"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - RS6",
    "md": "RS6"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - S3",
    "md": "S3"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - S4",
    "md": "S4"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - S5",
    "md": "S5"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - S6",
    "md": "S6"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - SUPER 90",
    "md": "S90"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - SQ5",
    "md": "SQ5"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - TT",
    "md": "TT"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - V-8",
    "md": "V8"
  },
  {
    "mk": "AUDI",
    "search": "AUDI - RS3",
    "md": "RS3"
  },
  {
    "mk": "AUST",
    "search": "AUSTIN-HEALY - 100 SERIES",
    "md": "100"
  },
  {
    "mk": "AUST",
    "search": "AUSTIN-HEALY - 1100",
    "md": "110"
  },
  {
    "mk": "AUST",
    "search": "AUSTIN-HEALY - 1800",
    "md": "180"
  },
  {
    "mk": "AUST",
    "search": "AUSTIN-HEALY - 3000 SERIES",
    "md": "300"
  },
  {
    "mk": "AUST",
    "search": "AUSTIN-HEALY - 850",
    "md": "850"
  },
  {
    "mk": "AUST",
    "search": "AUSTIN-HEALY - A99 & 110",
    "md": "A10"
  },
  {
    "mk": "AUST",
    "search": "AUSTIN-HEALY - A40",
    "md": "A40"
  },
  {
    "mk": "AUST",
    "search": "AUSTIN-HEALY - A55",
    "md": "A55"
  },
  {
    "mk": "AUST",
    "search": "AUSTIN-HEALY - CAMBRIDGE",
    "md": "A60"
  },
  {
    "mk": "AUST",
    "search": "AUSTIN-HEALY - COOPER S",
    "md": "CPS"
  },
  {
    "mk": "AUST",
    "search": "AUSTIN-HEALY - MARINA",
    "md": "MARI"
  },
  {
    "mk": "AUST",
    "search": "AUSTIN-HEALY - MINI",
    "md": "MINI"
  },
  {
    "mk": "AUST",
    "search": "AUSTIN-HEALY - SPRITE",
    "md": "SPRI"
  },
  {
    "mk": "AUST",
    "search": "AUSTIN-HEALY - WESTMINSTER",
    "md": "WEST"
  },
  {
    "mk": "AVAN",
    "search": "AVANTI - SERIES A",
    "md": "AAV"
  },
  {
    "mk": "AVAN",
    "search": "AVANTI - SERIES B",
    "md": "ABV"
  },
  {
    "mk": "BEJE",
    "search": "BEIJING JEEP - GANG STAR",
    "md": "TK"
  },
  {
    "mk": "BENT",
    "search": "BENTLEY - ARNAGE",
    "md": "ARN"
  },
  {
    "mk": "BENT",
    "search": "BENTLEY - AZURE",
    "md": "AZU"
  },
  {
    "mk": "BENT",
    "search": "BENTLEY - BROOKLANDS",
    "md": "BROO"
  },
  {
    "mk": "BENT",
    "search": "BENTLEY - CONTINENTAL CONVERTIBLE",
    "md": "CONT"
  },
  {
    "mk": "BENT",
    "search": "BENTLEY - CORNICHE",
    "md": "CORN"
  },
  {
    "mk": "BENT",
    "search": "BENTLEY - EIGHT",
    "md": "EIGH"
  },
  {
    "mk": "BENT",
    "search": "BENTLEY - MULSANNE",
    "md": "MULS"
  },
  {
    "mk": "BENT",
    "search": "BENTLEY - TURBO R",
    "md": "TBR"
  },
  {
    "mk": "BERO",
    "search": "BERTONE - CABRIO",
    "md": "CABR"
  },
  {
    "mk": "BERO",
    "search": "BERTONE - PALINURO",
    "md": "PALI"
  },
  {
    "mk": "BERO",
    "search": "BERTONE - X19",
    "md": "X19"
  },
  {
    "mk": "BESA",
    "search": "BESASIE AUTOMOBILE CO. INC. - BACI",
    "md": "BAC"
  },
  {
    "mk": "BIGT",
    "search": "BIG TEX - DUMP",
    "md": "DUMP"
  },
  {
    "mk": "BMC",
    "search": "B M C - PRINCESS",
    "md": "PRI"
  },
  {
    "mk": "BMW",
    "search": "BMW - M340i",
    "md": "M340"
  },
  {
    "mk": "BMW",
    "search": "BMW - 128i",
    "md": "128I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 135i",
    "md": "135I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 1600",
    "md": "160"
  },
  {
    "mk": "BMW",
    "search": "BMW - 1800",
    "md": "180"
  },
  {
    "mk": "BMW",
    "search": "BMW - 2.8",
    "md": "2.8"
  },
  {
    "mk": "BMW",
    "search": "BMW - 2000 SERIES",
    "md": "200"
  },
  {
    "mk": "BMW",
    "search": "BMW - 2002 SERIES",
    "md": "202"
  },
  {
    "mk": "BMW",
    "search": "BMW - 230i",
    "md": "230I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 2500 SERIES",
    "md": "250"
  },
  {
    "mk": "BMW",
    "search": "BMW - 2800 SERIES",
    "md": "280"
  },
  {
    "mk": "BMW",
    "search": "BMW - 328i",
    "md": "28I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 3.0 si",
    "md": "3"
  },
  {
    "mk": "BMW",
    "search": "BMW - 318ti",
    "md": "318T"
  },
  {
    "mk": "BMW",
    "search": "BMW - 318i",
    "md": "318i"
  },
  {
    "mk": "BMW",
    "search": "BMW - 320i",
    "md": "320"
  },
  {
    "mk": "BMW",
    "search": "BMW - 323i",
    "md": "323I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 325",
    "md": "325"
  },
  {
    "mk": "BMW",
    "search": "BMW - 328is",
    "md": "328"
  },
  {
    "mk": "BMW",
    "search": "BMW - 328d",
    "md": "328D"
  },
  {
    "mk": "BMW",
    "search": "BMW - 325i",
    "md": "32I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 330 SERIES",
    "md": "330"
  },
  {
    "mk": "BMW",
    "search": "BMW - 330i",
    "md": "330I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 335",
    "md": "335"
  },
  {
    "mk": "BMW",
    "search": "BMW - 335d",
    "md": "335D"
  },
  {
    "mk": "BMW",
    "search": "BMW - 335i",
    "md": "335I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 335Xi",
    "md": "335X"
  },
  {
    "mk": "BMW",
    "search": "BMW - 428i",
    "md": "428I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 430i",
    "md": "430I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 435i",
    "md": "435I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 440i",
    "md": "440I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 520",
    "md": "520"
  },
  {
    "mk": "BMW",
    "search": "BMW - 524 SERIES",
    "md": "524"
  },
  {
    "mk": "BMW",
    "search": "BMW - 525ia",
    "md": "525"
  },
  {
    "mk": "BMW",
    "search": "BMW - 525i",
    "md": "525I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 528i",
    "md": "528i"
  },
  {
    "mk": "BMW",
    "search": "BMW - 530i",
    "md": "530i"
  },
  {
    "mk": "BMW",
    "search": "BMW - 533i",
    "md": "533i"
  },
  {
    "mk": "BMW",
    "search": "BMW - 535 SERIES",
    "md": "535"
  },
  {
    "mk": "BMW",
    "search": "BMW - 540",
    "md": "540"
  },
  {
    "mk": "BMW",
    "search": "BMW - 540i",
    "md": "540I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 545i",
    "md": "545I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 550",
    "md": "550"
  },
  {
    "mk": "BMW",
    "search": "BMW - 600",
    "md": "600"
  },
  {
    "mk": "BMW",
    "search": "BMW - 630csi",
    "md": "630"
  },
  {
    "mk": "BMW",
    "search": "BMW - 633csi",
    "md": "633"
  },
  {
    "mk": "BMW",
    "search": "BMW - 635 SERIES",
    "md": "635"
  },
  {
    "mk": "BMW",
    "search": "BMW - 645ci",
    "md": "645C"
  },
  {
    "mk": "BMW",
    "search": "BMW - 645i",
    "md": "645I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 650 SERIES",
    "md": "650"
  },
  {
    "mk": "BMW",
    "search": "BMW - 733 SERIES",
    "md": "733"
  },
  {
    "mk": "BMW",
    "search": "BMW - 735 SERIES",
    "md": "735"
  },
  {
    "mk": "BMW",
    "search": "BMW - 740",
    "md": "740"
  },
  {
    "mk": "BMW",
    "search": "BMW - 740i",
    "md": "740i"
  },
  {
    "mk": "BMW",
    "search": "BMW - 745i",
    "md": "745i"
  },
  {
    "mk": "BMW",
    "search": "BMW - 750",
    "md": "750"
  },
  {
    "mk": "BMW",
    "search": "BMW - 750il",
    "md": "750I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 750li",
    "md": "750L"
  },
  {
    "mk": "BMW",
    "search": "BMW - 760i",
    "md": "760I"
  },
  {
    "mk": "BMW",
    "search": "BMW - 760li",
    "md": "760L"
  },
  {
    "mk": "BMW",
    "search": "BMW - 840ci",
    "md": "840"
  },
  {
    "mk": "BMW",
    "search": "BMW - 850i",
    "md": "850"
  },
  {
    "mk": "BMW",
    "search": "BMW - 850ci",
    "md": "850C"
  },
  {
    "mk": "BMW",
    "search": "BMW - BAVARIA",
    "md": "BAVA"
  },
  {
    "mk": "BMW",
    "search": "BMW - I3",
    "md": "I3"
  },
  {
    "mk": "BMW",
    "search": "BMW - I8",
    "md": "I8"
  },
  {
    "mk": "BMW",
    "search": "BMW - ISETTA",
    "md": "ISLE"
  },
  {
    "mk": "BMW",
    "search": "BMW - L6",
    "md": "L6"
  },
  {
    "mk": "BMW",
    "search": "BMW - L7",
    "md": "L7"
  },
  {
    "mk": "BMW",
    "search": "BMW - M235i",
    "md": "M235"
  },
  {
    "mk": "BMW",
    "search": "BMW - M3",
    "md": "M3"
  },
  {
    "mk": "BMW",
    "search": "BMW - M4",
    "md": "M4"
  },
  {
    "mk": "BMW",
    "search": "BMW - M5",
    "md": "M5"
  },
  {
    "mk": "BMW",
    "search": "BMW - M6",
    "md": "M6"
  },
  {
    "mk": "BMW",
    "search": "BMW - TI",
    "md": "TI"
  },
  {
    "mk": "BMW",
    "search": "BMW - X1",
    "md": "X1"
  },
  {
    "mk": "BMW",
    "search": "BMW - X2",
    "md": "X2"
  },
  {
    "mk": "BMW",
    "search": "BMW - X3",
    "md": "X3"
  },
  {
    "mk": "BMW",
    "search": "BMW - X4",
    "md": "X4"
  },
  {
    "mk": "BMW",
    "search": "BMW - X5",
    "md": "X5"
  },
  {
    "mk": "BMW",
    "search": "BMW - X6",
    "md": "X6"
  },
  {
    "mk": "BMW",
    "search": "BMW - Z3",
    "md": "Z3"
  },
  {
    "mk": "BMW",
    "search": "BMW - Z4",
    "md": "Z4"
  },
  {
    "mk": "BORG",
    "search": "BORGWARD - BEL AIR",
    "md": "BELA"
  },
  {
    "mk": "BORG",
    "search": "BORGWARD - BERETTA",
    "md": "BERE"
  },
  {
    "mk": "BORG",
    "search": "BORGWARD - BISCAYNE",
    "md": "BISC"
  },
  {
    "mk": "BORG",
    "search": "BORGWARD - HANSA",
    "md": "HANS"
  },
  {
    "mk": "BORG",
    "search": "BORGWARD - ISABELLA",
    "md": "ISAB"
  },
  {
    "mk": "BREM",
    "search": "BREMEN SPORT EQUIPMENT - CREIGHTON",
    "md": "CREI"
  },
  {
    "mk": "BREM",
    "search": "BREMEN SPORT EQUIPMENT - LAUFER",
    "md": "LAUF"
  },
  {
    "mk": "BREM",
    "search": "BREMEN SPORT EQUIPMENT - MAXI-TAXI",
    "md": "MAXI"
  },
  {
    "mk": "BREM",
    "search": "BREMEN SPORT EQUIPMENT - MINI-MARK",
    "md": "MINI"
  },
  {
    "mk": "BREM",
    "search": "BREMEN SPORT EQUIPMENT - SEBRING",
    "md": "SEBR"
  },
  {
    "mk": "BUGA",
    "search": "BUGATTI - EB110",
    "md": "E10"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - LACROSSE",
    "md": "LACR"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - ALLURE",
    "md": "ALLU"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - APOLLO",
    "md": "APOL"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - CALIFORNIA",
    "md": "CALI"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - CENTURY",
    "md": "CENT"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - CENTURION",
    "md": "CENU"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - ELECTRA (PARK AVENUE)",
    "md": "ELEC"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - ENCLAVE",
    "md": "ENCL"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - ENCORE",
    "md": "ENCO"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - ESTATE WAGON",
    "md": "ESTA"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - GS350",
    "md": "G35"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - GS400",
    "md": "G40"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - GS455",
    "md": "G45"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - GRAND SPORTS (G.S.)",
    "md": "GRAN"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - INVICTA",
    "md": "INVI"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - LE SABRE",
    "md": "LESA"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - LIMITED",
    "md": "LIMI"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - PARK AVENUE",
    "md": "PARK"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - RAINIER",
    "md": "RAIN"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - REATTA",
    "md": "REAT"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - REGAL",
    "md": "REGA"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - RENDEZVOUS",
    "md": "REND"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - RIVIERA",
    "md": "RIVI"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - ROADMASTER",
    "md": "ROAD"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - SKYHAWK",
    "md": "SKYH"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - SKYLARK",
    "md": "SKYL"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - SOMERSET",
    "md": "SOME"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - SPECIAL",
    "md": "SPEC"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - SPORTSWAGON",
    "md": "SPOR"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - SUPER",
    "md": "SUPE"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - TERRAZA",
    "md": "TERR"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - VERANO",
    "md": "VERA"
  },
  {
    "mk": "BUIC",
    "search": "BUICK - WILDCAT",
    "md": "WILD"
  },
  {
    "mk": "BZEL",
    "search": "B & Z ELECTRIC CAR CO. - CADILLAC",
    "md": "CADI"
  },
  {
    "mk": "BZEL",
    "search": "B & Z ELECTRIC CAR CO. - ELECTRA-KING",
    "md": "ELEC"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - 60 SERIES",
    "md": "60"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - 61 SERIES",
    "md": "61"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - 62 SERIES",
    "md": "62"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - 75 SERIES",
    "md": "75"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - ALLANTE",
    "md": "ALLA"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - ATS",
    "md": "ATS"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - BROUGHAM",
    "md": "BROU"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - CALAIS",
    "md": "CALA"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - CATERA",
    "md": "CATE"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - CIMARRON",
    "md": "CIMA"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - CONCOURS",
    "md": "CONC"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - CTS",
    "md": "CTS"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - DEVILLE",
    "md": "DEVI"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - ELDORADO",
    "md": "ELDO"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - ESCALADE",
    "md": "ESCA"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - ESV",
    "md": "ESV"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - EXT",
    "md": "EXT"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - FLEETWOOD",
    "md": "FLEE"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - SEVILLE",
    "md": "SEVI"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - SRX",
    "md": "SRX"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - STS",
    "md": "STS"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - TOURING SEDAN",
    "md": "TOUR"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - XLR",
    "md": "XLR"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - XT5",
    "md": "XT5"
  },
  {
    "mk": "CADI",
    "search": "CADILLAC - DTS",
    "md": "DTS"
  },
  {
    "mk": "CBTR",
    "search": "C & B TRAILER - UTILITY TRAILER",
    "md": "UTTR"
  },
  {
    "mk": "CBTR",
    "search": "C & B TRAILER - LANDSCAPE TRAILER",
    "md": "LATR"
  },
  {
    "mk": "CBTR",
    "search": "C & B TRAILER - FLAT TRAILER",
    "md": "FLTR"
  },
  {
    "mk": "CBTR",
    "search": "C & B TRAILER - TILT TRAILER",
    "md": "TILT"
  },
  {
    "mk": "CBTR",
    "search": "C & B TRAILER - PINTLE PULL TRAILER",
    "md": "PITR"
  },
  {
    "mk": "CBTR",
    "search": "C & B TRAILER - GOOSENECK TRAILER",
    "md": "GOTR"
  },
  {
    "mk": "CBTR",
    "search": "C & B TRAILER - DUMP TRAILER",
    "md": "DUTR"
  },
  {
    "mk": "CHEC",
    "search": "CHECKER - AEROBUS",
    "md": "AERO"
  },
  {
    "mk": "CHEC",
    "search": "CHECKER - CUSTOM",
    "md": "CUST"
  },
  {
    "mk": "CHEC",
    "search": "CHECKER - MARATHON",
    "md": "MARA"
  },
  {
    "mk": "CHEC",
    "search": "CHECKER - SUPERBA",
    "md": "SUPE"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - 210 SERIES",
    "md": "210"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - 300 DELUXE",
    "md": "300"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - ASTRO VAN",
    "md": "ASTR"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - AVALANCHE",
    "md": "AVAL"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - AVEO",
    "md": "AVEO"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - BEL AIR",
    "md": "BELA"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - BERETTA",
    "md": "BERE"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - BISCAYNE",
    "md": "BISC"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - BLAZER",
    "md": "BLAZ"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - BOLT",
    "md": "BOLT"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - BROOKWOOD",
    "md": "BROO"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - C10",
    "md": "C10"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - C/K 1500",
    "md": "C15"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - C/K 2500",
    "md": "C25"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - C/K 3500",
    "md": "C35"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - CAMARO",
    "md": "CAMA"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - CAPRICE",
    "md": "CAPR"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - CAPTIVA",
    "md": "CAPT"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - CAVALIER",
    "md": "CAVA"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - CELEBRITY",
    "md": "CELE"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - DELUXE (CHEVELLE)",
    "md": "CHED"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - GREENBRIER (CHEVELLE)",
    "md": "CHEG"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - NOMAD (CHEVELLE)",
    "md": "CHEN"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - CHEVETTE",
    "md": "CHET"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - CHEVELLE",
    "md": "CHEV"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - CHEVY II",
    "md": "CHEY"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - CITATION",
    "md": "CITA"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - CITY EXPRESS",
    "md": "CITY"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - COBALT",
    "md": "COBA"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - COLORADO",
    "md": "COLO"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - CONCOURS",
    "md": "CONC"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - CORVAIR",
    "md": "CORR"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - CORSICA",
    "md": "CORS"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - CORVETTE",
    "md": "CORV"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - CRUZE",
    "md": "CRUZ"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - DEL RAY",
    "md": "DELR"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - EL CAMINO",
    "md": "ELCA"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - EPICA",
    "md": "EPIC"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - EQUINOX",
    "md": "EQUI"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - ESTATE WAGON",
    "md": "EST"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - EXPRESS",
    "md": "EXP"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - FLEETLINE",
    "md": "FLE"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - HHR",
    "md": "HHR"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - IMPALA",
    "md": "IMPA"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - KINGSWOOD",
    "md": "KIN"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - LUMINA APV",
    "md": "LUMA"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - LUMINA",
    "md": "LUMI"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - LUV",
    "md": "LUV"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - MALIBU",
    "md": "MALI"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - METRO",
    "md": "METR"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - MONTE CARLO",
    "md": "MONT"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - MONZA",
    "md": "MONZ"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - NOVA (CHEVY II & CONCOURS)",
    "md": "NOVA"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - OPTRA",
    "md": "OPTR"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - PARKWOOD",
    "md": "PARK"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - PRISM",
    "md": "PRIS"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - S10",
    "md": "S10"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - SILVERADO",
    "md": "SILV"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - SONIC",
    "md": "SONI"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - SPECTRUM",
    "md": "SPEC"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - SPORTVAN",
    "md": "SPOR"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - SPRINT",
    "md": "SPRI"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - SPARK",
    "md": "SPRK"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - SSR",
    "md": "SSR"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - STYLE MASTER",
    "md": "STM"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - STYLE LINE",
    "md": "STY"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - SUBURBAN",
    "md": "SUBU"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - TAHOE",
    "md": "TAHO"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - TOWNSMAN",
    "md": "TOWN"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - TRACKER",
    "md": "TRAC"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - TRAILBLAZER",
    "md": "TRAI"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - TRAVERSE",
    "md": "TRAV"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - TRAX",
    "md": "TRAX"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - UPLANDER",
    "md": "UPLA"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - VEGA",
    "md": "VEGA"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - VENTURE",
    "md": "VENT"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - VOLT",
    "md": "VOLT"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - G30",
    "md": "G30"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - OPTRA5",
    "md": "OPT5"
  },
  {
    "mk": "CHEV",
    "search": "CHEVROLET - ORLANDO",
    "md": "ORLA"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - 200",
    "md": "200"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - 300",
    "md": "300"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - 300C",
    "md": "300C"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - CIRRUS",
    "md": "CIRR"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - COMMANDER",
    "md": "COMM"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - CONCORDE",
    "md": "CONC"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - CONQUEST",
    "md": "CONQ"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - CORDOBA",
    "md": "CORD"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - CROSSFIRE",
    "md": "CROS"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - DAYTONA",
    "md": "DAYT"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - DYNASTY",
    "md": "DYNA"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - E CLASS",
    "md": "ECL"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - EXECUTIVE SEDAN",
    "md": "EXE"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - IMPERIAL",
    "md": "IMPE"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - INTREPID",
    "md": "INTR"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - LASER",
    "md": "LASE"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - LEBARON",
    "md": "LEBA"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - LHS",
    "md": "LHS"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - LIDO",
    "md": "LID"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - LIMOUSINE",
    "md": "LIMO"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - NEON",
    "md": "NEON"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - FIFTH AVENUE",
    "md": "NEW5"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - NEWPORT",
    "md": "NEWP"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - TOWN & COUNTRY",
    "md": "NEWT"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - NEW YORKER",
    "md": "NEWY"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - PACIFICA",
    "md": "PACI"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - PROWLER",
    "md": "PROW"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - PT CRUISER",
    "md": "PTCR"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - ROYAL",
    "md": "ROYA"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - SALON",
    "md": "SAL"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - SARATOGA",
    "md": "SARA"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - SEBRING",
    "md": "SEBR"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - TC",
    "md": "TC"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - TOWN AND COUNTRY MINIVAN",
    "md": "TNC"
  },
  {
    "mk": "CHRY",
    "search": "CHRYSLER - WINDSOR",
    "md": "WIN"
  },
  {
    "mk": "CITR",
    "search": "CITROEN - 2CV",
    "md": "2CV"
  },
  {
    "mk": "CITR",
    "search": "CITROEN - AM16",
    "md": "AM6"
  },
  {
    "mk": "CITR",
    "search": "CITROEN - AX",
    "md": "AX"
  },
  {
    "mk": "CITR",
    "search": "CITROEN - DS-19",
    "md": "D19"
  },
  {
    "mk": "CITR",
    "search": "CITROEN - DS-21 & D21",
    "md": "D21"
  },
  {
    "mk": "CITR",
    "search": "CITROEN - ID-19",
    "md": "ID9"
  },
  {
    "mk": "CITR",
    "search": "CITROEN - SM",
    "md": "SM"
  },
  {
    "mk": "CLEN",
    "search": "CLENET COACH WORKS - ROADSTER",
    "md": "ROA"
  },
  {
    "mk": "COMV",
    "search": "COMMUTER VEHICLES INC - COMUTA-CAR",
    "md": "COM"
  },
  {
    "mk": "COOP",
    "search": "- MINI",
    "md": "MINI"
  },
  {
    "mk": "DAEW",
    "search": "DAEWOO - LANOS",
    "md": "LAN"
  },
  {
    "mk": "DAEW",
    "search": "DAEWOO - LEGANZA",
    "md": "LEG"
  },
  {
    "mk": "DAEW",
    "search": "DAEWOO - NUBIRA",
    "md": "NUB"
  },
  {
    "mk": "DAIH",
    "search": "DAIHATSU - CHARADE",
    "md": "CHA"
  },
  {
    "mk": "DAIH",
    "search": "DAIHATSU - ROCKY",
    "md": "RKY"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - 110",
    "md": "110"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - 1200",
    "md": "120"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - 200SX",
    "md": "200S"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - 210 (or B-210)",
    "md": "210"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - 240Z",
    "md": "240Z"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - 260Z",
    "md": "260Z"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - 280ZX",
    "md": "280X"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - 280Z",
    "md": "280Z"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - 310",
    "md": "310"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - 311",
    "md": "311"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - 510",
    "md": "510"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - 610",
    "md": "610"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - 710",
    "md": "710"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - 810",
    "md": "810"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - B-210 (or 210)",
    "md": "B210"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - F-10",
    "md": "F10"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - HONEY BEE",
    "md": "HON"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - LIL HUSTLER",
    "md": "LIL"
  },
  {
    "mk": "DATS",
    "search": "DATSUN - MAXIMA",
    "md": "MAXI"
  },
  {
    "mk": "DAYT",
    "search": "DAYTONA - MIGI",
    "md": "MIG"
  },
  {
    "mk": "DAYT",
    "search": "DAYTONA - MOYA",
    "md": "MOY"
  },
  {
    "mk": "DECO",
    "search": "DECOURVILLE - ROADSTER",
    "md": "ROA"
  },
  {
    "mk": "DESO",
    "search": "DESOTO - ADVENTURER",
    "md": "ADV"
  },
  {
    "mk": "DESO",
    "search": "DESOTO - CUSTOM",
    "md": "CUS"
  },
  {
    "mk": "DESO",
    "search": "DESOTO - DELUXE",
    "md": "DEL"
  },
  {
    "mk": "DESO",
    "search": "DESOTO - FIREDOM",
    "md": "FRD"
  },
  {
    "mk": "DESO",
    "search": "DESOTO - FIRELITE",
    "md": "FRF"
  },
  {
    "mk": "DESO",
    "search": "DESOTO - FIRESWEEP",
    "md": "FRS"
  },
  {
    "mk": "DESO",
    "search": "DESOTO - POWERMASTER",
    "md": "POW"
  },
  {
    "mk": "DETO",
    "search": "DETOMASO - DEAUVILLE",
    "md": "DEA"
  },
  {
    "mk": "DETO",
    "search": "DETOMASO - LONGCHAMP",
    "md": "LON"
  },
  {
    "mk": "DETO",
    "search": "DETOMASO - MANGUSTA",
    "md": "MNA"
  },
  {
    "mk": "DETO",
    "search": "DETOMASO - PANTERA",
    "md": "PTA"
  },
  {
    "mk": "DKW",
    "search": "DKW - F102",
    "md": "102"
  },
  {
    "mk": "DKW",
    "search": "DKW - AUDI",
    "md": "AUD"
  },
  {
    "mk": "DKW",
    "search": "DKW - VEMAG",
    "md": "VEM"
  },
  {
    "mk": "DODG",
    "search": "DODGE - A 100 COMPACT",
    "md": "100"
  },
  {
    "mk": "DODG",
    "search": "DODGE - 2000",
    "md": "2000"
  },
  {
    "mk": "DODG",
    "search": "DODGE - 330 SERIES",
    "md": "330"
  },
  {
    "mk": "DODG",
    "search": "DODGE - 400 SERIES",
    "md": "400"
  },
  {
    "mk": "DODG",
    "search": "DODGE - 440 SERIES",
    "md": "440"
  },
  {
    "mk": "DODG",
    "search": "DODGE - 600",
    "md": "600"
  },
  {
    "mk": "DODG",
    "search": "DODGE - 880 SERIES",
    "md": "880"
  },
  {
    "mk": "DODG",
    "search": "DODGE - ARIES",
    "md": "ARIE"
  },
  {
    "mk": "DODG",
    "search": "DODGE - ASPEN",
    "md": "ASPE"
  },
  {
    "mk": "DODG",
    "search": "DODGE - AVENGER",
    "md": "AVEN"
  },
  {
    "mk": "DODG",
    "search": "DODGE - CALIBER",
    "md": "CALI"
  },
  {
    "mk": "DODG",
    "search": "DODGE - CARAVAN",
    "md": "CARA"
  },
  {
    "mk": "DODG",
    "search": "DODGE - CHALLENGER",
    "md": "CHAL"
  },
  {
    "mk": "DODG",
    "search": "DODGE - CHARGER",
    "md": "CHAR"
  },
  {
    "mk": "DODG",
    "search": "DODGE - COLT",
    "md": "COLT"
  },
  {
    "mk": "DODG",
    "search": "DODGE - COMPACT SPORTSMAN",
    "md": "COM"
  },
  {
    "mk": "DODG",
    "search": "DODGE - CONQUEST",
    "md": "CONQ"
  },
  {
    "mk": "DODG",
    "search": "DODGE - CORONET",
    "md": "CORO"
  },
  {
    "mk": "DODG",
    "search": "DODGE - RAM 1500 PU",
    "md": "D150"
  },
  {
    "mk": "DODG",
    "search": "DODGE - RAM 2500 PU",
    "md": "D250"
  },
  {
    "mk": "DODG",
    "search": "DODGE - RAM 3500 PU",
    "md": "D350"
  },
  {
    "mk": "DODG",
    "search": "DODGE - DAKOTA",
    "md": "DAKO"
  },
  {
    "mk": "DODG",
    "search": "DODGE - DART",
    "md": "DART"
  },
  {
    "mk": "DODG",
    "search": "DODGE - DAYTONA",
    "md": "DAYT"
  },
  {
    "mk": "DODG",
    "search": "DODGE - DELUXE",
    "md": "DEL"
  },
  {
    "mk": "DODG",
    "search": "DODGE - DEMON",
    "md": "DEM"
  },
  {
    "mk": "DODG",
    "search": "DODGE - DIPLOMAT",
    "md": "DIPL"
  },
  {
    "mk": "DODG",
    "search": "DODGE - DURANGO",
    "md": "DURA"
  },
  {
    "mk": "DODG",
    "search": "DODGE - DYNASTY",
    "md": "DYNA"
  },
  {
    "mk": "DODG",
    "search": "DODGE - FLEET SPECIAL",
    "md": "FLS"
  },
  {
    "mk": "DODG",
    "search": "DODGE - GRAND CARAVAN",
    "md": "GRAN"
  },
  {
    "mk": "DODG",
    "search": "DODGE - INTREPID",
    "md": "INTR"
  },
  {
    "mk": "DODG",
    "search": "DODGE - JOURNEY",
    "md": "JOUR"
  },
  {
    "mk": "DODG",
    "search": "DODGE - LANCER",
    "md": "LANC"
  },
  {
    "mk": "DODG",
    "search": "DODGE - MAGNUM",
    "md": "MAGN"
  },
  {
    "mk": "DODG",
    "search": "DODGE - MEADOWBROOK",
    "md": "MEAD"
  },
  {
    "mk": "DODG",
    "search": "DODGE - MIRADA",
    "md": "MIRA"
  },
  {
    "mk": "DODG",
    "search": "DODGE - MONACO",
    "md": "MONA"
  },
  {
    "mk": "DODG",
    "search": "DODGE - NEON",
    "md": "NEON"
  },
  {
    "mk": "DODG",
    "search": "DODGE - NITRO",
    "md": "NITR"
  },
  {
    "mk": "DODG",
    "search": "DODGE - OMNI (ALSO 024)",
    "md": "OMNI"
  },
  {
    "mk": "DODG",
    "search": "DODGE - PHOENIX",
    "md": "PHOE"
  },
  {
    "mk": "DODG",
    "search": "DODGE - PIONEER",
    "md": "PION"
  },
  {
    "mk": "DODG",
    "search": "DODGE - POLARA",
    "md": "POLA"
  },
  {
    "mk": "DODG",
    "search": "DODGE - POWER RAM",
    "md": "PRM"
  },
  {
    "mk": "DODG",
    "search": "DODGE - RAIDER",
    "md": "RAID"
  },
  {
    "mk": "DODG",
    "search": "DODGE - RAM CHARGER",
    "md": "RCH"
  },
  {
    "mk": "DODG",
    "search": "DODGE - ROYAL",
    "md": "ROYA"
  },
  {
    "mk": "DODG",
    "search": "DODGE - SENECA",
    "md": "SENE"
  },
  {
    "mk": "DODG",
    "search": "DODGE - SHADOW",
    "md": "SHAD"
  },
  {
    "mk": "DODG",
    "search": "DODGE - SPIRIT",
    "md": "SPIR"
  },
  {
    "mk": "DODG",
    "search": "DODGE - SPRINT",
    "md": "SPRI"
  },
  {
    "mk": "DODG",
    "search": "DODGE - SPRINTER",
    "md": "SPRT"
  },
  {
    "mk": "DODG",
    "search": "DODGE - SRT4",
    "md": "SRT4"
  },
  {
    "mk": "DODG",
    "search": "DODGE - STEALTH",
    "md": "STEA"
  },
  {
    "mk": "DODG",
    "search": "DODGE - ST. REGIS",
    "md": "STR"
  },
  {
    "mk": "DODG",
    "search": "DODGE - STRATUS",
    "md": "STRA"
  },
  {
    "mk": "DODG",
    "search": "DODGE - SX",
    "md": "SX"
  },
  {
    "mk": "DODG",
    "search": "DODGE - SX2.0",
    "md": "SX2"
  },
  {
    "mk": "DODG",
    "search": "DODGE - RAM 1500 VAN",
    "md": "V15"
  },
  {
    "mk": "DODG",
    "search": "DODGE - RAM 2500 VAN",
    "md": "V25"
  },
  {
    "mk": "DODG",
    "search": "DODGE - RAM 3500 VAN",
    "md": "V35"
  },
  {
    "mk": "DODG",
    "search": "DODGE - VIPER",
    "md": "VIPE"
  },
  {
    "mk": "DODG",
    "search": "DODGE - WAYFARER",
    "md": "WAY"
  },
  {
    "mk": "DODG",
    "search": "DODGE - W250",
    "md": "W250"
  },
  {
    "mk": "DUTC",
    "search": "DUTCHMAN MANUFACTURING INC. - AEROLITE",
    "md": "AERO"
  },
  {
    "mk": "DUTC",
    "search": "DUTCHMAN MANUFACTURING INC. - ASPEN TRAIL",
    "md": "ASPE"
  },
  {
    "mk": "DUTC",
    "search": "DUTCHMAN MANUFACTURING INC. - BAYRIDGE",
    "md": "BAYR"
  },
  {
    "mk": "DUTC",
    "search": "DUTCHMAN MANUFACTURING INC. - BRECKENRIDGE",
    "md": "BREC"
  },
  {
    "mk": "DUTC",
    "search": "DUTCHMAN MANUFACTURING INC. - COLEMAN",
    "md": "COLE"
  },
  {
    "mk": "DUTC",
    "search": "DUTCHMAN MANUFACTURING INC. - DENALI",
    "md": "DENA"
  },
  {
    "mk": "DUTC",
    "search": "DUTCHMAN MANUFACTURING INC. - DUTCHMAN",
    "md": "DUTC"
  },
  {
    "mk": "DUTC",
    "search": "DUTCHMAN MANUFACTURING INC. - INFINITY",
    "md": "INFI"
  },
  {
    "mk": "DUTC",
    "search": "DUTCHMAN MANUFACTURING INC. - KODIAK",
    "md": "KODI"
  },
  {
    "mk": "DUTC",
    "search": "DUTCHMAN MANUFACTURING INC. - KOMFORT",
    "md": "KOMF"
  },
  {
    "mk": "DUTC",
    "search": "DUTCHMAN MANUFACTURING INC. - RUBICON",
    "md": "RUBI"
  },
  {
    "mk": "DUTC",
    "search": "DUTCHMAN MANUFACTURING INC. - VOLTAGE",
    "md": "VOLT"
  },
  {
    "mk": "EAGL",
    "search": "EAGLE - MEDALLION",
    "md": "MEDA"
  },
  {
    "mk": "EAGL",
    "search": "EAGLE - PREMIER",
    "md": "PRE"
  },
  {
    "mk": "EAGL",
    "search": "EAGLE - SUMMIT",
    "md": "SUM"
  },
  {
    "mk": "EAGL",
    "search": "EAGLE - TALON",
    "md": "TALO"
  },
  {
    "mk": "EAGL",
    "search": "EAGLE - VISION",
    "md": "VISI"
  },
  {
    "mk": "EDSE",
    "search": "EDSEL - CITATION",
    "md": "CITA"
  },
  {
    "mk": "EDSE",
    "search": "EDSEL - CORSAIR",
    "md": "CORS"
  },
  {
    "mk": "EDSE",
    "search": "EDSEL - PACER",
    "md": "PACE"
  },
  {
    "mk": "EDSE",
    "search": "EDSEL - RANGER",
    "md": "RANG"
  },
  {
    "mk": "EDSE",
    "search": "EDSEL - VILLAGER",
    "md": "VILL"
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH) - 100 E SERIES",
    "md": "100"
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH) - 105 E SERIES",
    "md": "105"
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH) - ANGLIA",
    "md": "ANG"
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH) - CAPRI",
    "md": "CAPR"
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH) - CONSUL",
    "md": "CONS"
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH) - CORSAIR",
    "md": "CORS"
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH) - CORTINA",
    "md": "CORT"
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH) - ESCORT",
    "md": "ESCO"
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH) - GT",
    "md": "GT"
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH) - LOTUS",
    "md": "LOTU"
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH) - MARK II",
    "md": "MK2"
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH) - PERFECT",
    "md": "PER"
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH) - SQUIRE",
    "md": "SQU"
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH) - THAMES",
    "md": "THA"
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH) - ZEPHYR",
    "md": "ZEPH"
  },
  {
    "mk": "ENGF",
    "search": "ENGLISH FORD (BRITISH) - ZODIAC",
    "md": "ZODI"
  },
  {
    "mk": "ENVO",
    "search": "ENVOY - EPIC",
    "md": "EPI"
  },
  {
    "mk": "EXCA",
    "search": "EXCALIBUR - COBRA",
    "md": "COBR"
  },
  {
    "mk": "EXCA",
    "search": "EXCALIBUR - JAC 427 COBRA",
    "md": "JAC"
  },
  {
    "mk": "EXCA",
    "search": "EXCALIBUR - SSK",
    "md": "SSK"
  },
  {
    "mk": "EXCA",
    "search": "EXCALIBUR - SS PHAETON",
    "md": "SSP"
  },
  {
    "mk": "EXCA",
    "search": "EXCALIBUR - SS ROADSTER",
    "md": "SSR"
  },
  {
    "mk": "FACE",
    "search": "FACEL VEGA - HK500",
    "md": "500"
  },
  {
    "mk": "FACE",
    "search": "FACEL VEGA - EXCELLENCE",
    "md": "EXE"
  },
  {
    "mk": "FACE",
    "search": "FACEL VEGA - FACELLIA",
    "md": "FACE"
  },
  {
    "mk": "FACE",
    "search": "FACEL VEGA - FACEL II",
    "md": "FII"
  },
  {
    "mk": "FACE",
    "search": "FACEL VEGA - FACEL III",
    "md": "FIII"
  },
  {
    "mk": "FACE",
    "search": "FACEL VEGA - FV",
    "md": "FV"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - 456GT",
    "md": "456"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - 458",
    "md": "458"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - 512",
    "md": "512"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - BARCHETTA (OR F130)",
    "md": "BAR"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - DAYTONA",
    "md": "DAYT"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - F355",
    "md": "F35"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - F40",
    "md": "F40"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - F430",
    "md": "F430"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - F-550 MARANELLO",
    "md": "MAR"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - MONDIAL",
    "md": "MON"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - QUATTROVALVOLVE",
    "md": "QUA"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - TESTAROSSA",
    "md": "TEST"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - TIPO",
    "md": "TIP"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - F12 BERLINETTA",
    "md": "F12B"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - 206",
    "md": "206"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - 208",
    "md": "208"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - 308",
    "md": "308"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - 328",
    "md": "328"
  },
  {
    "mk": "FERR",
    "search": "FERRARI - 348",
    "md": "348"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - 500",
    "md": "500"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - 1100 - D or R",
    "md": "110"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - 1200",
    "md": "120"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - 124 SERIES",
    "md": "124"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - 128 SERIES",
    "md": "128"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - 131 SERIES",
    "md": "131"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - 1500",
    "md": "150"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - 600D",
    "md": "600"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - 750",
    "md": "750"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - 850 FASTBACK",
    "md": "85F"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - BRAVA",
    "md": "BRAV"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - PUNTO",
    "md": "PUNT"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - RIMTO",
    "md": "RIM"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - SPIDER SERIES",
    "md": "SPYD"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - STRADA",
    "md": "STRA"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - UNO",
    "md": "UNO"
  },
  {
    "mk": "FIAT",
    "search": "FIAT - X19",
    "md": "X19"
  },
  {
    "mk": "FISK",
    "search": "FISKER - KARMA",
    "md": "KARM"
  },
  {
    "mk": "FLEE",
    "search": "FLEETWOOD ENTERPRISES INC - TERRY",
    "md": "TERR"
  },
  {
    "mk": "FLYE",
    "search": "FLYER - BUS",
    "md": "BUS"
  },
  {
    "mk": "FORD",
    "search": "FORD - 300 SERIES",
    "md": "300"
  },
  {
    "mk": "FORD",
    "search": "FORD - 7 LITRE",
    "md": "7LR"
  },
  {
    "mk": "FORD",
    "search": "FORD - AEROSTAR",
    "md": "AERO"
  },
  {
    "mk": "FORD",
    "search": "FORD - ASPIRE",
    "md": "ASPI"
  },
  {
    "mk": "FORD",
    "search": "FORD - BRONCO/BRONCO II",
    "md": "BRON"
  },
  {
    "mk": "FORD",
    "search": "FORD - COBRA",
    "md": "COBR"
  },
  {
    "mk": "FORD",
    "search": "FORD - CONTOUR",
    "md": "CONT"
  },
  {
    "mk": "FORD",
    "search": "FORD - COUNTRY SQUIRE",
    "md": "COQ"
  },
  {
    "mk": "FORD",
    "search": "FORD - COUNTRY SEDAN",
    "md": "COY"
  },
  {
    "mk": "FORD",
    "search": "FORD - CRESTLINE",
    "md": "CRE"
  },
  {
    "mk": "FORD",
    "search": "FORD - VICTORIA",
    "md": "CROW"
  },
  {
    "mk": "FORD",
    "search": "FORD - CUSTOMLINE",
    "md": "CST"
  },
  {
    "mk": "FORD",
    "search": "FORD - CUSTOM",
    "md": "CUS"
  },
  {
    "mk": "FORD",
    "search": "FORD - CLUB WAGON E150",
    "md": "CW1"
  },
  {
    "mk": "FORD",
    "search": "FORD - CLUB WAGON E250",
    "md": "CW2"
  },
  {
    "mk": "FORD",
    "search": "FORD - CLUB WAGON E350",
    "md": "CW3"
  },
  {
    "mk": "FORD",
    "search": "FORD - DELUXE",
    "md": "DEL"
  },
  {
    "mk": "FORD",
    "search": "FORD - ECONOLINE 100",
    "md": "E100"
  },
  {
    "mk": "FORD",
    "search": "FORD - ECONOLINE E150",
    "md": "E150"
  },
  {
    "mk": "FORD",
    "search": "FORD - ECONOLINE E250",
    "md": "E250"
  },
  {
    "mk": "FORD",
    "search": "FORD - ECONOLINE E350",
    "md": "E350"
  },
  {
    "mk": "FORD",
    "search": "FORD - ECONOLINE SERIES",
    "md": "ECON"
  },
  {
    "mk": "FORD",
    "search": "FORD - EDGE",
    "md": "EDGE"
  },
  {
    "mk": "FORD",
    "search": "FORD - ELITE",
    "md": "ELIT"
  },
  {
    "mk": "FORD",
    "search": "FORD - ESCAPE",
    "md": "ESCA"
  },
  {
    "mk": "FORD",
    "search": "FORD - ESCORT",
    "md": "ESCO"
  },
  {
    "mk": "FORD",
    "search": "FORD - EXCURSION",
    "md": "EXCU"
  },
  {
    "mk": "FORD",
    "search": "FORD - EXP",
    "md": "EXP"
  },
  {
    "mk": "FORD",
    "search": "FORD - EXPEDITION",
    "md": "EXPE"
  },
  {
    "mk": "FORD",
    "search": "FORD - EXPLORER",
    "md": "EXPL"
  },
  {
    "mk": "FORD",
    "search": "FORD - F100",
    "md": "F100"
  },
  {
    "mk": "FORD",
    "search": "FORD - F-150XLT",
    "md": "F150"
  },
  {
    "mk": "FORD",
    "search": "FORD - F250 SUPERCAB (TRUCK)",
    "md": "F250"
  },
  {
    "mk": "FORD",
    "search": "FORD - F350",
    "md": "F350"
  },
  {
    "mk": "FORD",
    "search": "FORD - F450",
    "md": "F450"
  },
  {
    "mk": "FORD",
    "search": "FORD - F550",
    "md": "F550"
  },
  {
    "mk": "FORD",
    "search": "FORD - FAIRLANE",
    "md": "FAIL"
  },
  {
    "mk": "FORD",
    "search": "FORD - FAIRMONT",
    "md": "FAIR"
  },
  {
    "mk": "FORD",
    "search": "FORD - FALCON",
    "md": "FALC"
  },
  {
    "mk": "FORD",
    "search": "FORD - FESTIVA",
    "md": "FEST"
  },
  {
    "mk": "FORD",
    "search": "FORD - FIESTA",
    "md": "FIES"
  },
  {
    "mk": "FORD",
    "search": "FORD - FIVE HUNDRED",
    "md": "FIVE"
  },
  {
    "mk": "FORD",
    "search": "FORD - FLEX",
    "md": "FLEX"
  },
  {
    "mk": "FORD",
    "search": "FORD - FOCUS",
    "md": "FOCU"
  },
  {
    "mk": "FORD",
    "search": "FORD - FREESTAR",
    "md": "FREE"
  },
  {
    "mk": "FORD",
    "search": "FORD - FREESTYLE",
    "md": "FRES"
  },
  {
    "mk": "FORD",
    "search": "FORD - FRONTENAC",
    "md": "FRO"
  },
  {
    "mk": "FORD",
    "search": "FORD - FUSION",
    "md": "FUSI"
  },
  {
    "mk": "FORD",
    "search": "FORD - FUTURA",
    "md": "FUTU"
  },
  {
    "mk": "FORD",
    "search": "FORD - GALAXIE",
    "md": "GALA"
  },
  {
    "mk": "FORD",
    "search": "FORD - GRAND MARQUIS",
    "md": "GRA"
  },
  {
    "mk": "FORD",
    "search": "FORD - GRANADA",
    "md": "GRAN"
  },
  {
    "mk": "FORD",
    "search": "FORD - KA",
    "md": "KA"
  },
  {
    "mk": "FORD",
    "search": "FORD - LARIAT",
    "md": "LARI"
  },
  {
    "mk": "FORD",
    "search": "FORD - LASER",
    "md": "LASE"
  },
  {
    "mk": "FORD",
    "search": "FORD - LTD",
    "md": "LTD"
  },
  {
    "mk": "FORD",
    "search": "FORD - LTD II",
    "md": "LTII"
  },
  {
    "mk": "FORD",
    "search": "FORD - MAINLINE",
    "md": "MAIN"
  },
  {
    "mk": "FORD",
    "search": "FORD - MAVERICK",
    "md": "MAVE"
  },
  {
    "mk": "FORD",
    "search": "FORD - MODEL A",
    "md": "MOA"
  },
  {
    "mk": "FORD",
    "search": "FORD - MODEL T",
    "md": "MOT"
  },
  {
    "mk": "FORD",
    "search": "FORD - MUSTANG",
    "md": "MUST"
  },
  {
    "mk": "FORD",
    "search": "FORD - NEVADA",
    "md": "NEVA"
  },
  {
    "mk": "FORD",
    "search": "FORD - PINTO",
    "md": "PINT"
  },
  {
    "mk": "FORD",
    "search": "FORD - PROBE",
    "md": "PROB"
  },
  {
    "mk": "FORD",
    "search": "FORD - RANCH",
    "md": "RAH"
  },
  {
    "mk": "FORD",
    "search": "FORD - RANCHERO",
    "md": "RANC"
  },
  {
    "mk": "FORD",
    "search": "FORD - RANGER",
    "md": "RANG"
  },
  {
    "mk": "FORD",
    "search": "FORD - RANCH WAGON",
    "md": "RAW"
  },
  {
    "mk": "FORD",
    "search": "FORD - SPECIAL",
    "md": "SPE"
  },
  {
    "mk": "FORD",
    "search": "FORD - SQUIRE (FALCON OR FAIRLANE)",
    "md": "SQU"
  },
  {
    "mk": "FORD",
    "search": "FORD - STARLINER",
    "md": "STA"
  },
  {
    "mk": "FORD",
    "search": "FORD - SUNLINER",
    "md": "SUN"
  },
  {
    "mk": "FORD",
    "search": "FORD - SUPER",
    "md": "SUP"
  },
  {
    "mk": "FORD",
    "search": "FORD - TAURUS",
    "md": "TAUR"
  },
  {
    "mk": "FORD",
    "search": "FORD - TEMPO",
    "md": "TEMP"
  },
  {
    "mk": "FORD",
    "search": "FORD - THUNDERBIRD",
    "md": "THUN"
  },
  {
    "mk": "FORD",
    "search": "FORD - TORINO (FAIRLANE)",
    "md": "TORI"
  },
  {
    "mk": "FORD",
    "search": "FORD - TRANSIT",
    "md": "TRAN"
  },
  {
    "mk": "FORD",
    "search": "FORD - WINDSTAR",
    "md": "WIND"
  },
  {
    "mk": "FORD",
    "search": "FORD - XL",
    "md": "XL"
  },
  {
    "mk": "FORD",
    "search": "FORD - C-MAX",
    "md": "CMAX"
  },
  {
    "mk": "FREF",
    "search": "FRENCH FORD - COMETE",
    "md": "COM"
  },
  {
    "mk": "FREF",
    "search": "FRENCH FORD - VEDETTE",
    "md": "VED"
  },
  {
    "mk": "FREF",
    "search": "FRENCH FORD - VENDOME",
    "md": "VEN"
  },
  {
    "mk": "GAZ",
    "search": "GAZ - CHAIKA",
    "md": "CHA"
  },
  {
    "mk": "GAZ",
    "search": "GAZ - VOLGA",
    "md": "VOL"
  },
  {
    "mk": "GDNE",
    "search": "GREAT DANE - DRY VAN",
    "md": "DV"
  },
  {
    "mk": "GDNE",
    "search": "GREAT DANE - FLATBED",
    "md": "FLBD"
  },
  {
    "mk": "GDNE",
    "search": "GREAT DANE - REEFER VAN",
    "md": "RFRV"
  },
  {
    "mk": "GENE",
    "search": "GENESIS - G70",
    "md": "G70"
  },
  {
    "mk": "GENE",
    "search": "GENESIS - G80",
    "md": "G80"
  },
  {
    "mk": "GENE",
    "search": "GENESIS - G80 Sport",
    "md": "G80S"
  },
  {
    "mk": "GENE",
    "search": "GENESIS - G90",
    "md": "G90"
  },
  {
    "mk": "GEO",
    "search": "GEO - METRO",
    "md": "METR"
  },
  {
    "mk": "GEO",
    "search": "GEO - PRIZM",
    "md": "PRIZ"
  },
  {
    "mk": "GEO",
    "search": "GEO - STORM",
    "md": "STRO"
  },
  {
    "mk": "GEO",
    "search": "GEO - TRACKER",
    "md": "TRAC"
  },
  {
    "mk": "GLAS",
    "search": "GLAS - GOGGOMOBILE",
    "md": "GOG"
  },
  {
    "mk": "GM",
    "search": "GENERAL MOTORS - EV1",
    "md": "EV1"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - ACADIA",
    "md": "ACAD"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - CABELLERO",
    "md": "CAB"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - CANYON",
    "md": "CANY"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - DENALI",
    "md": "DEN"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - ENVOY",
    "md": "ENVO"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - JIMMY",
    "md": "JIMM"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - RALLY",
    "md": "RALL"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - SAFARI",
    "md": "SAFA"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - SAVANNA",
    "md": "SAVA"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - SIERRA",
    "md": "SIER"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - SONOMA",
    "md": "SONO"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - SPRINT",
    "md": "SPRI"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - SUBURBAN",
    "md": "SUBU"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - TERRAIN",
    "md": "TERR"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - TYPHOON",
    "md": "TYP"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - VANDURA",
    "md": "VAND"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - YUKON",
    "md": "YUKO"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - 3500HD",
    "md": "3500"
  },
  {
    "mk": "GMC",
    "search": "GENERAL MOTORS CORP. - TRACKER",
    "md": "TRAC"
  },
  {
    "mk": "HILL",
    "search": "HILLMAN - 1600 SERIES",
    "md": "160"
  },
  {
    "mk": "HILL",
    "search": "HILLMAN - DELUXE",
    "md": "DEL"
  },
  {
    "mk": "HILL",
    "search": "HILLMAN - HUSKY",
    "md": "HUS"
  },
  {
    "mk": "HILL",
    "search": "HILLMAN - IMP",
    "md": "IMP"
  },
  {
    "mk": "HILL",
    "search": "HILLMAN - MINX",
    "md": "MIN"
  },
  {
    "mk": "HILL",
    "search": "HILLMAN - SCEPTRE",
    "md": "SCP"
  },
  {
    "mk": "HILL",
    "search": "HILLMAN - SNIPE",
    "md": "SNI"
  },
  {
    "mk": "HILL",
    "search": "HILLMAN - SUPER MINX",
    "md": "SUP"
  },
  {
    "mk": "HOND",
    "search": "HONDA - ACCORD",
    "md": "ACCO"
  },
  {
    "mk": "HOND",
    "search": "HONDA - CIVIC (AND CRX)",
    "md": "CIVI"
  },
  {
    "mk": "HOND",
    "search": "HONDA - CR-Z",
    "md": "CR-Z"
  },
  {
    "mk": "HOND",
    "search": "HONDA - CROSSTOUR",
    "md": "CROS"
  },
  {
    "mk": "HOND",
    "search": "HONDA - CRV",
    "md": "CRV"
  },
  {
    "mk": "HOND",
    "search": "HONDA - DEL SOL",
    "md": "DELS"
  },
  {
    "mk": "HOND",
    "search": "HONDA - ELEMENT",
    "md": "ELEM"
  },
  {
    "mk": "HOND",
    "search": "HONDA - EVPLUS",
    "md": "EVP"
  },
  {
    "mk": "HOND",
    "search": "HONDA - FIT",
    "md": "FIT"
  },
  {
    "mk": "HOND",
    "search": "HONDA - HR-V",
    "md": "HRV"
  },
  {
    "mk": "HOND",
    "search": "HONDA - INSIGHT",
    "md": "INSI"
  },
  {
    "mk": "HOND",
    "search": "HONDA - ODYSSEY",
    "md": "ODYS"
  },
  {
    "mk": "HOND",
    "search": "HONDA - PASSPORT",
    "md": "PASS"
  },
  {
    "mk": "HOND",
    "search": "HONDA - PILOT",
    "md": "PILO"
  },
  {
    "mk": "HOND",
    "search": "HONDA - PRELUDE",
    "md": "PREL"
  },
  {
    "mk": "HOND",
    "search": "HONDA - RIDGELINE",
    "md": "RIDG"
  },
  {
    "mk": "HOND",
    "search": "HONDA - S2000",
    "md": "S200"
  },
  {
    "mk": "HOND",
    "search": "HONDA - CLARITY",
    "md": "CLAR"
  },
  {
    "mk": "HUDS",
    "search": "HUDSON - COMMODORE",
    "md": "COM"
  },
  {
    "mk": "HUDS",
    "search": "HUDSON - DELUXE",
    "md": "DEL"
  },
  {
    "mk": "HUDS",
    "search": "HUDSON - HORNET",
    "md": "HOR"
  },
  {
    "mk": "HUDS",
    "search": "HUDSON - ITALIA",
    "md": "ITA"
  },
  {
    "mk": "HUDS",
    "search": "HUDSON - JET",
    "md": "JET"
  },
  {
    "mk": "HUDS",
    "search": "HUDSON - PACEMAKER",
    "md": "PAC"
  },
  {
    "mk": "HUDS",
    "search": "HUDSON - RAMBLER",
    "md": "RAM"
  },
  {
    "mk": "HUDS",
    "search": "HUDSON - SUPER",
    "md": "SUP"
  },
  {
    "mk": "HUDS",
    "search": "HUDSON - WASP",
    "md": "WAS"
  },
  {
    "mk": "HUMB",
    "search": "HUMBER - HAWK",
    "md": "HAW"
  },
  {
    "mk": "HUMB",
    "search": "HUMBER - SNIPE",
    "md": "SNI"
  },
  {
    "mk": "HUMM",
    "search": "HUMMER - H1",
    "md": "H1"
  },
  {
    "mk": "HUMM",
    "search": "HUMMER - H2",
    "md": "H2"
  },
  {
    "mk": "HUMM",
    "search": "HUMMER - H2 SUT",
    "md": "H2SU"
  },
  {
    "mk": "HUMM",
    "search": "HUMMER - H3",
    "md": "H3"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - ELANTRA",
    "md": "ELAN"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - ENTOURAGE",
    "md": "ENTO"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - EXCEL",
    "md": "EXCE"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - GENESIS",
    "md": "GENE"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - IONIQ",
    "md": "ION"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - IONIQ 5",
    "md": "ION5"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - IONIQ 6",
    "md": "ION6"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - KONA",
    "md": "KONA"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - MARCIA",
    "md": "MAR"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - NIRO",
    "md": "NIRO"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - PALISADE",
    "md": "PALI"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - PONY",
    "md": "PONY"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - SANTA FE",
    "md": "SANT"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - SCOUPE",
    "md": "SCOU"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - SONATA",
    "md": "SONA"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - STELLAR",
    "md": "STEL"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - TIBURON",
    "md": "TIBU"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - TUCSON",
    "md": "TUCS"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - VELOSTER",
    "md": "VELO"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - VENUE",
    "md": "VENU"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - XG300",
    "md": "XG30"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - XG350",
    "md": "XG35"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - ACCENT",
    "md": "ACCE"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - AVATAR",
    "md": "AVAT"
  },
  {
    "mk": "HYUN",
    "search": "HYUNDAI - AZERA",
    "md": "AZER"
  },
  {
    "mk": "IMPE",
    "search": "IMPERIAL - CROWN",
    "md": "CROW"
  },
  {
    "mk": "IMPE",
    "search": "IMPERIAL - CUSTOM",
    "md": "CUS"
  },
  {
    "mk": "IMPE",
    "search": "IMPERIAL - LE BARON",
    "md": "LEBA"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - EX35",
    "md": "EX35"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - FX35",
    "md": "FX35"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - FX45",
    "md": "FX45"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - FX50",
    "md": "FX50"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - G20",
    "md": "G20"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - G35",
    "md": "G35"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - G37",
    "md": "G37"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - I30",
    "md": "I30"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - J30",
    "md": "J30"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - M30",
    "md": "M30"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - M35",
    "md": "M35"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - M45",
    "md": "M45"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - Q45",
    "md": "Q45"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - Q50",
    "md": "Q50"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - Q60",
    "md": "Q60"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - Q70L",
    "md": "Q70L"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - QX4",
    "md": "QX4"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - QX50",
    "md": "QX50"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - QX56",
    "md": "QX56"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - QX80",
    "md": "QX80"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - XQ80",
    "md": "XQ80"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - G37X",
    "md": "G37X"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - I35",
    "md": "I35"
  },
  {
    "mk": "INFI",
    "search": "INFINITI - QX60",
    "md": "QX60"
  },
  {
    "mk": "INTE",
    "search": "INTERNATIONAL - 1652sc",
    "md": "1652"
  },
  {
    "mk": "INTE",
    "search": "INTERNATIONAL - 3200",
    "md": "3200"
  },
  {
    "mk": "INTE",
    "search": "INTERNATIONAL - 3800",
    "md": "3800"
  },
  {
    "mk": "INTE",
    "search": "INTERNATIONAL - 4200",
    "md": "4200"
  },
  {
    "mk": "INTE",
    "search": "INTERNATIONAL - 4300",
    "md": "4300"
  },
  {
    "mk": "INTE",
    "search": "INTERNATIONAL - 4400",
    "md": "4400"
  },
  {
    "mk": "INTE",
    "search": "INTERNATIONAL - 7300",
    "md": "7300"
  },
  {
    "mk": "INTE",
    "search": "INTERNATIONAL - 7400",
    "md": "7400"
  },
  {
    "mk": "INTE",
    "search": "INTERNATIONAL - 8500",
    "md": "8500"
  },
  {
    "mk": "INTE",
    "search": "INTERNATIONAL - 8600",
    "md": "8600"
  },
  {
    "mk": "INTE",
    "search": "INTERNATIONAL - 9200i",
    "md": "9200"
  },
  {
    "mk": "INTE",
    "search": "INTERNATIONAL - 9400i",
    "md": "9400"
  },
  {
    "mk": "INTE",
    "search": "INTERNATIONAL - 9900i",
    "md": "9900"
  },
  {
    "mk": "INTE",
    "search": "INTERNATIONAL - 9900ix",
    "md": "9999"
  },
  {
    "mk": "ISUZ",
    "search": "ISUZU - AMIGO",
    "md": "AMG"
  },
  {
    "mk": "ISUZ",
    "search": "ISUZU - HOMBRE",
    "md": "HOM"
  },
  {
    "mk": "ISUZ",
    "search": "ISUZU - I-MARK",
    "md": "IMA"
  },
  {
    "mk": "ISUZ",
    "search": "ISUZU - IMPULSE",
    "md": "IMPU"
  },
  {
    "mk": "ISUZ",
    "search": "ISUZU - OASIS",
    "md": "OAS"
  },
  {
    "mk": "ISUZ",
    "search": "ISUZU - RODEO",
    "md": "RODE"
  },
  {
    "mk": "ISUZ",
    "search": "ISUZU - STYLUS",
    "md": "STYL"
  },
  {
    "mk": "ISUZ",
    "search": "ISUZU - TROOPER",
    "md": "TROO"
  },
  {
    "mk": "ISUZ",
    "search": "ISUZU - VEHICROSS",
    "md": "VCS"
  },
  {
    "mk": "ITAF",
    "search": "ITALIAN FORD - ANGLIA",
    "md": "ANG"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - 2.4 LITRE",
    "md": "24L"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - 340",
    "md": "340"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - 3.4 LITRE",
    "md": "34L"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - 3.8 LITRE",
    "md": "38L"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - 420",
    "md": "420"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - 4.2 LITRE",
    "md": "42L"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - E-TYPE",
    "md": "ETY"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - XJ12",
    "md": "J12"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - MARK V SERIES",
    "md": "MAR"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - MARK TEN SALON",
    "md": "MTS"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - SOVEREIGN",
    "md": "SOV"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - S-TYPE",
    "md": "STYP"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - V12",
    "md": "V12"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - VANDEN PLAS",
    "md": "VAN"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - XF",
    "md": "XF"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - XJ",
    "md": "XJ"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - XJ40",
    "md": "XJ4"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - XJ6",
    "md": "XJ6"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - XJ8",
    "md": "XJ8"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - XJC",
    "md": "XJC"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - XJR",
    "md": "XJR"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - XJS",
    "md": "XJS"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - XK SERIES",
    "md": "XK"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - XK8",
    "md": "XK8"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - XK-E SERIES",
    "md": "XKE"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - XTYPE",
    "md": "XTYP"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - XVLR",
    "md": "XVLR"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - XE",
    "md": "XE"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - I-PACE",
    "md": "IPAC"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - F-PACE",
    "md": "FPAC"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - E-PACE",
    "md": "EPAC"
  },
  {
    "mk": "JAGU",
    "search": "JAGUAR - F-TYPE",
    "md": "FTYP"
  },
  {
    "mk": "JEEP",
    "search": "JEEP - GLADIATOR",
    "md": "GLAD"
  },
  {
    "mk": "JEEP",
    "search": "JEEP - CHEROKEE/GRAND CHEROKEE",
    "md": "CHER"
  },
  {
    "mk": "JEEP",
    "search": "JEEP - CJ",
    "md": "CJ"
  },
  {
    "mk": "JEEP",
    "search": "JEEP - COMANCHE",
    "md": "COMA"
  },
  {
    "mk": "JEEP",
    "search": "JEEP - COMMANDER",
    "md": "COMM"
  },
  {
    "mk": "JEEP",
    "search": "JEEP - COMPASS",
    "md": "COMP"
  },
  {
    "mk": "JEEP",
    "search": "JEEP - DAKAR",
    "md": "DAKA"
  },
  {
    "mk": "JEEP",
    "search": "JEEP - J-10",
    "md": "J10"
  },
  {
    "mk": "JEEP",
    "search": "JEEP - LIBERTY",
    "md": "LIBE"
  },
  {
    "mk": "JEEP",
    "search": "JEEP - PATRIOT",
    "md": "PATR"
  },
  {
    "mk": "JEEP",
    "search": "JEEP - RENEGADE",
    "md": "RENE"
  },
  {
    "mk": "JEEP",
    "search": "JEEP - TJ",
    "md": "TJ"
  },
  {
    "mk": "JEEP",
    "search": "JEEP - WAGONEER",
    "md": "WAGO"
  },
  {
    "mk": "JEEP",
    "search": "JEEP - WRANGLER",
    "md": "WRAN"
  },
  {
    "mk": "JEEP",
    "search": "JEEP - YJ",
    "md": "YJ"
  },
  {
    "mk": "JENS",
    "search": "JENSEN - HEALY",
    "md": "HEAL"
  },
  {
    "mk": "JENS",
    "search": "JENSEN - INTERCEPTOR",
    "md": "INTE"
  },
  {
    "mk": "KAIS",
    "search": "KAISER - CAROLINA",
    "md": "CARO"
  },
  {
    "mk": "KAIS",
    "search": "KAISER - DARRIN",
    "md": "DAR"
  },
  {
    "mk": "KAIS",
    "search": "KAISER - DELUXE",
    "md": "DEL"
  },
  {
    "mk": "KAIS",
    "search": "KAISER - DRAGON",
    "md": "DRA"
  },
  {
    "mk": "KAIS",
    "search": "KAISER - MANHATTAN",
    "md": "MAN"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - SELTOS",
    "md": "SELT"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - AMANTI",
    "md": "AMAN"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - AVELLA",
    "md": "AVE"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - CADENZA",
    "md": "CAD"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - FORTE",
    "md": "FORT"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - K900",
    "md": "K900"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - MAGENTIS",
    "md": "MAGE"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - MATIZ",
    "md": "MATI"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - NIRO",
    "md": "NIRO"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - OPTIMA",
    "md": "OPT"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - RIO",
    "md": "RIO"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - RIO5",
    "md": "RIO5"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - RONDO",
    "md": "ROND"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - SEDONA",
    "md": "SEDO"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - SEPHIA",
    "md": "SEPH"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - SORENTO",
    "md": "SORE"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - SOUL",
    "md": "SOUL"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - SPECTRA",
    "md": "SPEC"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - SPORTAGE",
    "md": "SPOR"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - STINGER",
    "md": "STIN"
  },
  {
    "mk": "KIA",
    "search": "KIA MOTORS CORPORATION - TELLURIDE",
    "md": "TELL"
  },
  {
    "mk": "KIOT",
    "search": "KIOTI - CK",
    "md": "CK"
  },
  {
    "mk": "KIOT",
    "search": "KIOTI - DK",
    "md": "DK"
  },
  {
    "mk": "KUBO",
    "search": "KUBOTA - B",
    "md": "B"
  },
  {
    "mk": "KUBO",
    "search": "KUBOTA - BX",
    "md": "BX"
  },
  {
    "mk": "KUBO",
    "search": "KUBOTA - L",
    "md": "L"
  },
  {
    "mk": "KUBO",
    "search": "KUBOTA - M",
    "md": "M"
  },
  {
    "mk": "KUBO",
    "search": "KUBOTA - RTV",
    "md": "RTV"
  },
  {
    "mk": "KUBO",
    "search": "KUBOTA - TLB",
    "md": "TLB"
  },
  {
    "mk": "LADA",
    "search": "LADA - NIVA",
    "md": "NIV"
  },
  {
    "mk": "LAMO",
    "search": "LAMBORGHINI - LM129",
    "md": "129"
  },
  {
    "mk": "LAMO",
    "search": "LAMBORGHINI - COUNTACH",
    "md": "COUN"
  },
  {
    "mk": "LAMO",
    "search": "LAMBORGHINI - DIABLO",
    "md": "DIAB"
  },
  {
    "mk": "LAMO",
    "search": "LAMBORGHINI - ESPADA",
    "md": "ESP"
  },
  {
    "mk": "LAMO",
    "search": "LAMBORGHINI - GALLARDO",
    "md": "GALL"
  },
  {
    "mk": "LAMO",
    "search": "LAMBORGHINI - JALPA",
    "md": "JAL"
  },
  {
    "mk": "LAMO",
    "search": "LAMBORGHINI - JARMA",
    "md": "JAR"
  },
  {
    "mk": "LAMO",
    "search": "LAMBORGHINI - MIURA SV",
    "md": "MIU"
  },
  {
    "mk": "LAMO",
    "search": "LAMBORGHINI - ROADSTER",
    "md": "ROD"
  },
  {
    "mk": "LAMO",
    "search": "LAMBORGHINI - HURACAN",
    "md": "HURA"
  },
  {
    "mk": "LAND",
    "search": "LAND ROVER - DEFENDER 110",
    "md": "D110"
  },
  {
    "mk": "LAND",
    "search": "LAND ROVER - DEFENDER 90",
    "md": "D90"
  },
  {
    "mk": "LAND",
    "search": "LAND ROVER - DEFENDER SERIES",
    "md": "DEFE"
  },
  {
    "mk": "LAND",
    "search": "LAND ROVER - RANGE ROVER DISCOVERY",
    "md": "DISC"
  },
  {
    "mk": "LAND",
    "search": "LAND ROVER - FREELANDER",
    "md": "FREE"
  },
  {
    "mk": "LAND",
    "search": "LAND ROVER - HSE",
    "md": "HSE"
  },
  {
    "mk": "LAND",
    "search": "LAND ROVER - LR2",
    "md": "LR2"
  },
  {
    "mk": "LAND",
    "search": "LAND ROVER - LR3",
    "md": "LR3"
  },
  {
    "mk": "LAND",
    "search": "LAND ROVER - LR4",
    "md": "LR4"
  },
  {
    "mk": "LAND",
    "search": "LAND ROVER - RANGE ROVER",
    "md": "RANG"
  },
  {
    "mk": "LAND",
    "search": "LAND ROVER - RANGE ROVER DISCOVERY SPORT",
    "md": "DISS"
  },
  {
    "mk": "LAND",
    "search": "LAND ROVER - RANGE ROVER EVOQUE",
    "md": "EVOQ"
  },
  {
    "mk": "LAND",
    "search": "LAND ROVER - RANGE ROVER VELAR",
    "md": "VELR"
  },
  {
    "mk": "LAND",
    "search": "LAND ROVER - RANGE ROVER SPORT",
    "md": "SPOR"
  },
  {
    "mk": "LDTR",
    "search": "LOAD TRAIL - DK",
    "md": "DK"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - ES250",
    "md": "250"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - ES300",
    "md": "300"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - ES350",
    "md": "350"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - LS400",
    "md": "400"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - CT200H",
    "md": "CT20"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - ES330",
    "md": "ES33"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - GS300",
    "md": "GS3"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - GS350",
    "md": "GS35"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - GS400",
    "md": "GS4"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - GS430",
    "md": "GS43"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - GS450",
    "md": "GS45"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - GSF",
    "md": "GSF"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - GX460",
    "md": "GX46"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - GX470",
    "md": "GX47"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - IS200T",
    "md": "IS20"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - IS250",
    "md": "IS25"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - IS300",
    "md": "IS30"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - IS350",
    "md": "IS35"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - ISF",
    "md": "ISF"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - LX450",
    "md": "L45"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - LX470",
    "md": "L47"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - LX570",
    "md": "L57"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - LS430",
    "md": "LS43"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - LS460",
    "md": "LS46"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - LS460L",
    "md": "LS4L"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - LS600HL",
    "md": "LS60"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - NX",
    "md": "NX"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - NX300",
    "md": "NX30"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - RC300",
    "md": "RC30"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - RC350",
    "md": "RC35"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - RCF",
    "md": "RCF"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - RX300",
    "md": "RX3"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - RX330",
    "md": "RX33"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - RX350",
    "md": "RX35"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - RX400H",
    "md": "RX40"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - RX450H",
    "md": "RX45"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - SC300",
    "md": "S30"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - SC400",
    "md": "S40"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - SC430",
    "md": "SC43"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - NX 250",
    "md": "NX25"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - NX 350",
    "md": "NX35"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - NX 350h",
    "md": "NX3H"
  },
  {
    "mk": "LEXU",
    "search": "LEXUS - NX 450h+",
    "md": "NX45"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - AVIATOR",
    "md": "AVIA"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - CONTINENTAL",
    "md": "CONT"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - CUSTOM",
    "md": "CUS"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - LS",
    "md": "LS"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - LS6",
    "md": "LS6"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - LS8",
    "md": "LS8"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - MARK SERIES",
    "md": "MARK"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - MARK II",
    "md": "MII"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - MARK III",
    "md": "MIII"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - MARK IV",
    "md": "MIV"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - MKC",
    "md": "MKC"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - MARK V",
    "md": "MV"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - MARK VI",
    "md": "MVI"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - MARK VII",
    "md": "MVII"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - NAVIGATOR",
    "md": "NAVI"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - PREMIERE",
    "md": "PRE"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - STANDARD",
    "md": "STAN"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - TOWN CAR",
    "md": "TOWN"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - VERSAILLES",
    "md": "VER"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - MARK VIII",
    "md": "VIII"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - ZEPHYR",
    "md": "ZEP"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - MKT",
    "md": "MKT"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - NAUTILUS",
    "md": "NAUT"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - MKZ",
    "md": "MKZ"
  },
  {
    "mk": "LINC",
    "search": "LINCOLN-CONTINENTAL - MKX",
    "md": "MKX"
  },
  {
    "mk": "LNCI",
    "search": "LANCIA - BERLINA",
    "md": "BER"
  },
  {
    "mk": "LNCI",
    "search": "LANCIA - BETA SERIES",
    "md": "BET"
  },
  {
    "mk": "LNCI",
    "search": "LANCIA - DEDRA",
    "md": "DED"
  },
  {
    "mk": "LNCI",
    "search": "LANCIA - FLAVIA",
    "md": "FLA"
  },
  {
    "mk": "LNCI",
    "search": "LANCIA - FLAMINIA",
    "md": "FLM"
  },
  {
    "mk": "LNCI",
    "search": "LANCIA - FULVIA",
    "md": "FUL"
  },
  {
    "mk": "LNCI",
    "search": "LANCIA - ZAGATO",
    "md": "ZAG"
  },
  {
    "mk": "LOTU",
    "search": "LOTUS - ECLAT",
    "md": "ECL"
  },
  {
    "mk": "LOTU",
    "search": "LOTUS - ELAN",
    "md": "ELA"
  },
  {
    "mk": "LOTU",
    "search": "LOTUS - ELITE",
    "md": "ELI"
  },
  {
    "mk": "LOTU",
    "search": "LOTUS - ESPRIT",
    "md": "ESPI"
  },
  {
    "mk": "LOTU",
    "search": "LOTUS - EUROPA",
    "md": "EUR"
  },
  {
    "mk": "LOTU",
    "search": "LOTUS - PLUS TWO",
    "md": "PLU"
  },
  {
    "mk": "LOTU",
    "search": "LOTUS - SUPER 7",
    "md": "SUP"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - 2000 SERIES",
    "md": "200"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - 228",
    "md": "228"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - 3500 SERIES",
    "md": "350"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - 4000 SERIES",
    "md": "400"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - 4200 GT",
    "md": "420"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - 425",
    "md": "425"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - 430",
    "md": "430"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - 5000 SERIES",
    "md": "500"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - BITURBO",
    "md": "BIT"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - BORA",
    "md": "BOR"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - GHIBLI",
    "md": "GHI"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - GTI SERIES",
    "md": "GTI"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - INDY",
    "md": "IND"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - KHAMSIN",
    "md": "KHA"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - MERAK",
    "md": "MER"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - MEXICO",
    "md": "MEX"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - MISTRELL",
    "md": "MIS"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - QUATTROPORTE",
    "md": "QUA"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - SEBRING",
    "md": "SEB"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - SHAMAL",
    "md": "SHM"
  },
  {
    "mk": "MASE",
    "search": "MASERATI - SPYDER",
    "md": "SPY"
  },
  {
    "mk": "MASS",
    "search": "MASSEY FERGUSON - 1500",
    "md": "1500"
  },
  {
    "mk": "MASS",
    "search": "MASSEY FERGUSON - 3400",
    "md": "3400"
  },
  {
    "mk": "MASS",
    "search": "MASSEY FERGUSON - 3600",
    "md": "3600"
  },
  {
    "mk": "MASS",
    "search": "MASSEY FERGUSON - 500",
    "md": "500"
  },
  {
    "mk": "MASS",
    "search": "MASSEY FERGUSON - 5400",
    "md": "5400"
  },
  {
    "mk": "MASS",
    "search": "MASSEY FERGUSON - 6400",
    "md": "6400"
  },
  {
    "mk": "MASS",
    "search": "MASSEY FERGUSON - 7400",
    "md": "7400"
  },
  {
    "mk": "MASS",
    "search": "MASSEY FERGUSON - 8400",
    "md": "8400"
  },
  {
    "mk": "MASS",
    "search": "MASSEY FERGUSON - GC",
    "md": "GC"
  },
  {
    "mk": "MASS",
    "search": "MASSEY FERGUSON - SUNFLOWER",
    "md": "SUNF"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - 2",
    "md": "2"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - 3",
    "md": "3"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - 323",
    "md": "323"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - 5",
    "md": "5"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - 6",
    "md": "6"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - 616",
    "md": "616"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - 618",
    "md": "618"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - 626",
    "md": "626"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - 808 SERIES",
    "md": "808"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - 929",
    "md": "929"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - B2000",
    "md": "B200"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - B2200",
    "md": "B220"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - B2300",
    "md": "B230"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - B2500",
    "md": "B250"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - B2600",
    "md": "B260"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - B3000",
    "md": "B300"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - B4000",
    "md": "B400"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - COSMO",
    "md": "CSM"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - CX-5",
    "md": "CX5"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - CX-7",
    "md": "CX7"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - CX-9",
    "md": "CX9"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - GLC",
    "md": "GLC"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - M6",
    "md": "M6"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - MIATA",
    "md": "MIAT"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - MILLENIA",
    "md": "MILE"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - MISER",
    "md": "MISE"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - MPV",
    "md": "MPV"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - MX3",
    "md": "MX3"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - MX5",
    "md": "MX5"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - MX6",
    "md": "MX6"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - NAVAJO",
    "md": "NAVA"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - FAMILIA",
    "md": "PRO"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - PROTEGE",
    "md": "PROT"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - RX2 (ROTARY ENGINE)",
    "md": "RX2"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - RX3 (ROTARY ENGINE)",
    "md": "RX3"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - RX4 (ROTARY ENGINE)",
    "md": "RX4"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - RX7 (ROTARY ENGINE)",
    "md": "RX7"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - RX8",
    "md": "RX8"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - TRIBUTE",
    "md": "TRIB"
  },
  {
    "mk": "MAZD",
    "search": "MAZDA - CX-3",
    "md": "CX3"
  },
  {
    "mk": "MCLA",
    "search": "MCLAREN - MP4",
    "md": "MP4"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - BOBCAT",
    "md": "BOBC"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - BREEZEWAY",
    "md": "BREE"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - BROUGHAM",
    "md": "BROU"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - CAPRI",
    "md": "CAPR"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - COUNTRY CRUISER",
    "md": "CCR"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - CALIENTE",
    "md": "CLI"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - COMMUTER",
    "md": "CMM"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - COLONY PARK",
    "md": "COL"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - COMET",
    "md": "COME"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - COUGAR",
    "md": "COUG"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - CUSTOM",
    "md": "CUS"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - CYCLONE",
    "md": "CYC"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - GRAND MARQUIS",
    "md": "GRAN"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - LN7",
    "md": "LN7"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - LYNX",
    "md": "LYNX"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - MARAUDER",
    "md": "MARA"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - MARINER",
    "md": "MARI"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - MARQUIS",
    "md": "MARQ"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - MEDALIST",
    "md": "MED"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - MONARCH",
    "md": "MONA"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - MONTEGO",
    "md": "MONT"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - MONTEREY",
    "md": "MONY"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - MONTCLAIR",
    "md": "MOT"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - MOUNTAINEER",
    "md": "MTN"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - MYSTIQUE",
    "md": "MYST"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - PARKLANE",
    "md": "PARK"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - S-22",
    "md": "S22"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - S-33",
    "md": "S33"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - S-55",
    "md": "S55"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - SABLE",
    "md": "SABL"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - TOPAZ",
    "md": "TOPA"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - TRACER",
    "md": "TRAC"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - TURNPIKE CRUISER",
    "md": "TUR"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - VILLAGER",
    "md": "VILL"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - VOYAGER",
    "md": "VOYA"
  },
  {
    "mk": "MERC",
    "search": "MERCURY - ZEPHYR",
    "md": "ZEP"
  },
  {
    "mk": "MERK",
    "search": "MERKUR - SCORPIO",
    "md": "SCOR"
  },
  {
    "mk": "MERK",
    "search": "MERKUR - XR4Ti",
    "md": "XR4"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 180 SERIES",
    "md": "180"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 190 SERIES",
    "md": "190"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 200 SERIES",
    "md": "200"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 219 SERIES",
    "md": "219"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 220 SERIES",
    "md": "220"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 230 SERIES",
    "md": "230"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 240 SERIES",
    "md": "240"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 250 SERIES",
    "md": "250"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 260 SERIES",
    "md": "260"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 280 SERIES",
    "md": "280"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 300 SERIES",
    "md": "300"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 320 SERIES",
    "md": "320"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - E320W",
    "md": "320W"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 350 SERIES",
    "md": "350"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 380 SERIES",
    "md": "380"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 400 SERIES",
    "md": "400"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 420 SERIES",
    "md": "420"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 450 SERIES",
    "md": "450"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 500 SERIES",
    "md": "500"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 560 SERIES",
    "md": "560"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - 600 SERIES",
    "md": "600"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - B200",
    "md": "B200"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - B250",
    "md": "B250"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - C220",
    "md": "C220"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - C230",
    "md": "C230"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - C240",
    "md": "C240"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - C250",
    "md": "C250"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - C280",
    "md": "C280"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - C300",
    "md": "C300"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - C320",
    "md": "C320"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - C350",
    "md": "C350"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - C36",
    "md": "C36"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - C400",
    "md": "C400"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - C43",
    "md": "C43"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - C55",
    "md": "C55"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - C63",
    "md": "C63"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - CLK32",
    "md": "CK32"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - CLK35",
    "md": "CK35"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - CLK50",
    "md": "CK50"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - CLK55",
    "md": "CK55"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - CLK430",
    "md": "CL4"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - CLA45",
    "md": "CL45"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - CL500",
    "md": "CL50"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - CL55",
    "md": "CL55"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - CL600",
    "md": "CL60"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - CL65",
    "md": "CL65"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - CLA250",
    "md": "CLA2"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - CLK320",
    "md": "CLK3"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - CLK500",
    "md": "CLK5"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - CLS500",
    "md": "CLS5"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - CLS63",
    "md": "CLS6"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - CLS55",
    "md": "CS55"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - E300",
    "md": "E300"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - E320",
    "md": "E320"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - E350",
    "md": "E350"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - E400",
    "md": "E400"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - E420",
    "md": "E420"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - E43",
    "md": "E43"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - E430",
    "md": "E430"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - E500",
    "md": "E500"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - E55",
    "md": "E55"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - E63",
    "md": "E63"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - GLK35",
    "md": "G35"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - GLE350",
    "md": "G350"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - GLE400",
    "md": "G400"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - GL450",
    "md": "G450"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - G500",
    "md": "G500"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - G55",
    "md": "G55"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - G550",
    "md": "G550"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - G63",
    "md": "G63"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - GLC30",
    "md": "GL30"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - GL350",
    "md": "GL35"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - GLC43",
    "md": "GL43"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - GLA",
    "md": "GLA"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - GLE35",
    "md": "GLE3"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - GLE45",
    "md": "GLE4"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - GLK250",
    "md": "GLK2"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - GLK350",
    "md": "GLK3"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - GLS550",
    "md": "GLS5"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - METRIS",
    "md": "METR"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - ML320 (SPORT UTILITY)",
    "md": "ML3"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - ML350",
    "md": "ML35"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - ML430",
    "md": "ML4"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - ML500",
    "md": "ML50"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - ML63",
    "md": "ML63"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - R350",
    "md": "R350"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - S430",
    "md": "S430"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - S450",
    "md": "S450"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - S500",
    "md": "S500"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - S55",
    "md": "S55"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - S550V",
    "md": "S550"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - S600",
    "md": "S600"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - SL",
    "md": "SL"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - SL500",
    "md": "SL5"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - SL600",
    "md": "SL6"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - SL65",
    "md": "SL65"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - SLK3",
    "md": "SLK3"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - SLK5",
    "md": "SLK5"
  },
  {
    "mk": "MERZ",
    "search": "MERCEDES-BENZ - SPRINTER",
    "md": "SPRI"
  },
  {
    "mk": "MESS",
    "search": "MESSERSCHMITT - KR200",
    "md": "KR"
  },
  {
    "mk": "MESS",
    "search": "MESSERSCHMITT - KR201",
    "md": "KR1"
  },
  {
    "mk": "MESS",
    "search": "MESSERSCHMITT - TIGER",
    "md": "TIG"
  },
  {
    "mk": "METE",
    "search": "METEOR (CANADIAN MERCURY) - COUNTRY SEDAN",
    "md": "COY"
  },
  {
    "mk": "METE",
    "search": "METEOR (CANADIAN MERCURY) - LEMOYNE",
    "md": "LEM"
  },
  {
    "mk": "METE",
    "search": "METEOR (CANADIAN MERCURY) - MONTEGO",
    "md": "MGO"
  },
  {
    "mk": "METE",
    "search": "METEOR (CANADIAN MERCURY) - MONTCALM",
    "md": "MON"
  },
  {
    "mk": "METE",
    "search": "METEOR (CANADIAN MERCURY) - NIAGARA",
    "md": "NIA"
  },
  {
    "mk": "METE",
    "search": "METEOR (CANADIAN MERCURY) - RANCH WAGON",
    "md": "RAW"
  },
  {
    "mk": "METE",
    "search": "METEOR (CANADIAN MERCURY) - RIDEAU",
    "md": "RID"
  },
  {
    "mk": "METE",
    "search": "METEOR (CANADIAN MERCURY) - S-33",
    "md": "S33"
  },
  {
    "mk": "MG",
    "search": "MG - 1600",
    "md": "1600"
  },
  {
    "mk": "MG",
    "search": "MG - PRINCESS 4-R",
    "md": "4R"
  },
  {
    "mk": "MG",
    "search": "MG - MAGNETTE",
    "md": "MAGN"
  },
  {
    "mk": "MG",
    "search": "MG - MARINA",
    "md": "MARI"
  },
  {
    "mk": "MG",
    "search": "MG - MARK II",
    "md": "MARK"
  },
  {
    "mk": "MG",
    "search": "MG - 1100",
    "md": "MG1"
  },
  {
    "mk": "MG",
    "search": "MG - MGA",
    "md": "MGA"
  },
  {
    "mk": "MG",
    "search": "MG - MGB",
    "md": "MGB"
  },
  {
    "mk": "MG",
    "search": "MG - MGC",
    "md": "MGC"
  },
  {
    "mk": "MG",
    "search": "MG - MGB/GT",
    "md": "MGG"
  },
  {
    "mk": "MG",
    "search": "MG - MGC/GT",
    "md": "MGT"
  },
  {
    "mk": "MG",
    "search": "MG - MIDGET",
    "md": "MIDG"
  },
  {
    "mk": "MG",
    "search": "MG - SPRITE",
    "md": "SPRI"
  },
  {
    "mk": "MG",
    "search": "MG - SPORTS SEDAN",
    "md": "SPS"
  },
  {
    "mk": "MG",
    "search": "MG - TF SERIES",
    "md": "TF"
  },
  {
    "mk": "MINI",
    "search": "MINI - COOPER",
    "md": "COOP"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - 3000 GT",
    "md": "3GT"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - CHARIOT",
    "md": "CHAR"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - CORDIA",
    "md": "CORD"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - DELICA",
    "md": "DELI"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - DIAMANTE",
    "md": "DIAM"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - ECLIPSE SPYDER GS-T",
    "md": "ECL"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - ECLIPSE",
    "md": "ECLI"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - ENDEAVOR",
    "md": "ENDE"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - EXPO",
    "md": "EXPO"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - GALANT",
    "md": "GALA"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - LANCER",
    "md": "LANC"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - MINICA",
    "md": "MIN"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - MIRAGE",
    "md": "MIRA"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - MONTERO/MONTERO SPORT",
    "md": "MONT"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - MIGHTY MAX",
    "md": "MTX"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - OUTLANDER",
    "md": "OUTL"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - PRECIS",
    "md": "PRE"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - RVR",
    "md": "RVR"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - SIGMA",
    "md": "SIG"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - SPYDER 3000 GT",
    "md": "SPYD"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - STARION",
    "md": "STA"
  },
  {
    "mk": "MITS",
    "search": "MITSUBISHI - TREDIA",
    "md": "TRE"
  },
  {
    "mk": "MODE",
    "search": "MODEL A & MODEL T MOTOR CAR REPRODUCTION CORP. - GT250",
    "md": "250"
  },
  {
    "mk": "MODE",
    "search": "MODEL A & MODEL T MOTOR CAR REPRODUCTION CORP. - MODEL A",
    "md": "MOD"
  },
  {
    "mk": "MODE",
    "search": "MODEL A & MODEL T MOTOR CAR REPRODUCTION CORP. - THUNDERBIRD",
    "md": "THUN"
  },
  {
    "mk": "MONA",
    "search": "MONARCH - LUCERNE",
    "md": "LUC"
  },
  {
    "mk": "MONA",
    "search": "MONARCH - RICHELIEU",
    "md": "RIC"
  },
  {
    "mk": "MONA",
    "search": "MONARCH - SCEPTRE",
    "md": "SCP"
  },
  {
    "mk": "MORG",
    "search": "MORGAN - 4/4 MARK 5",
    "md": "MK5"
  },
  {
    "mk": "MORG",
    "search": "MORGAN - PLUS 4 SERIES",
    "md": "PL4"
  },
  {
    "mk": "MORR",
    "search": "MORRIS - 1100",
    "md": "110"
  },
  {
    "mk": "MORR",
    "search": "MORRIS - 850 SERIES",
    "md": "850"
  },
  {
    "mk": "MORR",
    "search": "MORRIS - DELUXE",
    "md": "DEL"
  },
  {
    "mk": "MORR",
    "search": "MORRIS - MINI SERIES",
    "md": "MII"
  },
  {
    "mk": "MORR",
    "search": "MORRIS - MINOR",
    "md": "MIN"
  },
  {
    "mk": "MORR",
    "search": "MORRIS - OXFORD",
    "md": "OXF"
  },
  {
    "mk": "MORR",
    "search": "MORRIS - TRAVELLER",
    "md": "TRV"
  },
  {
    "mk": "MOTO",
    "search": "MOTO GUZZI - V7",
    "md": "V7"
  },
  {
    "mk": "MOTO",
    "search": "MOTO GUZZI - V9",
    "md": "V9"
  },
  {
    "mk": "MUNT",
    "search": "MUNTZ - JET",
    "md": "JET"
  },
  {
    "mk": "NASH",
    "search": "NASH - AMBASSADOR",
    "md": "AMB"
  },
  {
    "mk": "NASH",
    "search": "NASH - LAYFAYETTE",
    "md": "LAF"
  },
  {
    "mk": "NASH",
    "search": "NASH - METROPOLITAN",
    "md": "MET"
  },
  {
    "mk": "NASH",
    "search": "NASH - RAMBLER",
    "md": "RAM"
  },
  {
    "mk": "NASH",
    "search": "NASH - STATESMAN",
    "md": "STA"
  },
  {
    "mk": "NEFL",
    "search": "NEW FLYER - BUS",
    "md": "BUS"
  },
  {
    "mk": "NEWM",
    "search": "NEWMAR - BAY STAR",
    "md": "BAYS"
  },
  {
    "mk": "NEWM",
    "search": "NEWMAR - CANYON STAR",
    "md": "CANY"
  },
  {
    "mk": "NEWM",
    "search": "NEWMAR - VENTANA",
    "md": "VENT"
  },
  {
    "mk": "NEWM",
    "search": "NEWMAR - DUTCH STAR",
    "md": "DUTC"
  },
  {
    "mk": "NEWM",
    "search": "NEWMAR - MOUNTAIN AIRE",
    "md": "MOUN"
  },
  {
    "mk": "NEWM",
    "search": "NEWMAR - ESSEX",
    "md": "ESSE"
  },
  {
    "mk": "NEWM",
    "search": "NEWMAR - KING AIRE",
    "md": "KING"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - 200SX",
    "md": "200S"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - 240SX",
    "md": "240S"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - 300ZX",
    "md": "300Z"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - 350Z",
    "md": "350Z"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - 370Z",
    "md": "370Z"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - ALTIMA",
    "md": "ALTI"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - ARMADA",
    "md": "ARMA"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - AXXESS",
    "md": "AXXE"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - CUBE",
    "md": "CUBE"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - FRONTIER",
    "md": "FRON"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - GT-R",
    "md": "GT-R"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - JUKE",
    "md": "JUKE"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - KICKS",
    "md": "KICK"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - LEAF",
    "md": "LEAF"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - MAXIMA",
    "md": "MAXI"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - MICRA",
    "md": "MICR"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - MURANO",
    "md": "MURA"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - NAVARA",
    "md": "NAVA"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - NP300",
    "md": "NP30"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - NV200",
    "md": "NV20"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - NX",
    "md": "NX"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - PATHFINDER",
    "md": "PATH"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - PULSAR",
    "md": "PULS"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - QASHQAI",
    "md": "QASH"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - QUEST",
    "md": "QUES"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - ROGUE",
    "md": "ROGU"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - SE-V6",
    "md": "SE"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - SENTRA",
    "md": "SENT"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - SKYLINE",
    "md": "SKYL"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - STANZA",
    "md": "STAN"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - TERRANO II",
    "md": "TERR"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - TITAN",
    "md": "TITA"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - VERSA",
    "md": "VERS"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - XE",
    "md": "XE"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - XTERRA",
    "md": "XTER"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - XTRAIL",
    "md": "XTRA"
  },
  {
    "mk": "NISS",
    "search": "NISSAN - SP&SP",
    "md": "SPSP"
  },
  {
    "mk": "NORT",
    "search": "NORTHWOOD MANUFACTURING - ARCTIC FOX",
    "md": "ARCT"
  },
  {
    "mk": "NOVA",
    "search": "NOVABUS - HEV",
    "md": "HEV"
  },
  {
    "mk": "NSU",
    "search": "NSU PRINZ - 1000",
    "md": "100"
  },
  {
    "mk": "NSU",
    "search": "NSU PRINZ - 110 TYPE",
    "md": "110"
  },
  {
    "mk": "NSU",
    "search": "NSU PRINZ - AUTO NOVA",
    "md": "AVA"
  },
  {
    "mk": "NSU",
    "search": "NSU PRINZ - PRINZ",
    "md": "PRIN"
  },
  {
    "mk": "NSU",
    "search": "NSU PRINZ - SPIDER (WANKEL)",
    "md": "SPI"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - 442",
    "md": "442"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - 88",
    "md": "88"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - 98",
    "md": "98"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - ACHIEVA",
    "md": "ACHI"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - ALERO",
    "md": "ALER"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - AURORA",
    "md": "AURO"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - BRAVADA",
    "md": "BRAV"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - CALAIS",
    "md": "CALA"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - CARAVAN",
    "md": "CARA"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - CUSTOM CRUISER",
    "md": "CCR"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - CUSTOM",
    "md": "CUS"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - CUTLASS",
    "md": "CUTL"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - CUTLASS SUPREME",
    "md": "CUTS"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - DELUXE",
    "md": "DEL"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - DELTA 88",
    "md": "DELT"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - DELMONT 88",
    "md": "DLM"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - LSS",
    "md": "DLT"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - DYNAMIC 88",
    "md": "DYN"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - F-85",
    "md": "F85"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - FIRENZA",
    "md": "FIRE"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - HOLIDAY",
    "md": "HOLI"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - INTRIGUE",
    "md": "INTR"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - JETFIRE",
    "md": "JTF"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - JETSTAR",
    "md": "JTS"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - OMEGA",
    "md": "OMEG"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - REGENCY (NINETY-EIGHT SERIES)",
    "md": "REG"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - ROYALE",
    "md": "ROYA"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - SILHOUETTE",
    "md": "SIL"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - STARFIRE",
    "md": "STA"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - STANDARD",
    "md": "STD"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - SUPER 88",
    "md": "SUP"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - TORONADO",
    "md": "TORO"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - TROFEO",
    "md": "TRO"
  },
  {
    "mk": "OLDS",
    "search": "OLDSMOBILE - VISTA CRUISER",
    "md": "VIS"
  },
  {
    "mk": "OPEL",
    "search": "OPEL - 1900",
    "md": "190"
  },
  {
    "mk": "OPEL",
    "search": "OPEL - ASTRA",
    "md": "ASTR"
  },
  {
    "mk": "OPEL",
    "search": "OPEL - CARAVAN",
    "md": "CARA"
  },
  {
    "mk": "OPEL",
    "search": "OPEL - DIPLOMAT",
    "md": "DIPL"
  },
  {
    "mk": "OPEL",
    "search": "OPEL - GT",
    "md": "GT"
  },
  {
    "mk": "OPEL",
    "search": "OPEL - KADETTE",
    "md": "KAD"
  },
  {
    "mk": "OPEL",
    "search": "OPEL - KAPITAN",
    "md": "KAP"
  },
  {
    "mk": "OPEL",
    "search": "OPEL - LUXUS",
    "md": "LUX"
  },
  {
    "mk": "OPEL",
    "search": "OPEL - MANTA",
    "md": "MAN"
  },
  {
    "mk": "OPEL",
    "search": "OPEL - OLYMPIA",
    "md": "OLY"
  },
  {
    "mk": "OPEL",
    "search": "OPEL - RALLYE",
    "md": "RAL"
  },
  {
    "mk": "OPEL",
    "search": "OPEL - REKORD",
    "md": "REK"
  },
  {
    "mk": "PACK",
    "search": "PACKARD - BALBOA",
    "md": "BAL"
  },
  {
    "mk": "PACK",
    "search": "PACKARD - CARIBBEAN",
    "md": "CAR"
  },
  {
    "mk": "PACK",
    "search": "PACKARD - CAVALIER",
    "md": "CAVA"
  },
  {
    "mk": "PACK",
    "search": "PACKARD - CLIPPER",
    "md": "CLI"
  },
  {
    "mk": "PACK",
    "search": "PACKARD - PATRICIAN",
    "md": "PAT"
  },
  {
    "mk": "PACK",
    "search": "PACKARD - PREDICTOR",
    "md": "PRD"
  },
  {
    "mk": "PACK",
    "search": "PACKARD - REQUEST",
    "md": "REQ"
  },
  {
    "mk": "PANE",
    "search": "PANTHER WESTWINDS LTD. - DEVILLE",
    "md": "DEVI"
  },
  {
    "mk": "PANE",
    "search": "PANTHER WESTWINDS LTD. - J72",
    "md": "J72"
  },
  {
    "mk": "PANE",
    "search": "PANTHER WESTWINDS LTD. - KILLETA",
    "md": "KAL"
  },
  {
    "mk": "PANE",
    "search": "PANTHER WESTWINDS LTD. - LIMA",
    "md": "LIM"
  },
  {
    "mk": "PANZ",
    "search": "PANOZ AUTO DEVELOPMENT - ROADSTER",
    "md": "ROD"
  },
  {
    "mk": "PASS",
    "search": "PASSPORT - OPTIMA",
    "md": "OPTI"
  },
  {
    "mk": "PEUG",
    "search": "PEUGEOT - 203",
    "md": "203"
  },
  {
    "mk": "PEUG",
    "search": "PEUGEOT - 304",
    "md": "304"
  },
  {
    "mk": "PEUG",
    "search": "PEUGEOT - 403",
    "md": "403"
  },
  {
    "mk": "PEUG",
    "search": "PEUGEOT - 404",
    "md": "404"
  },
  {
    "mk": "PEUG",
    "search": "PEUGEOT - 405",
    "md": "405"
  },
  {
    "mk": "PEUG",
    "search": "PEUGEOT - 504 SERIES",
    "md": "504"
  },
  {
    "mk": "PEUG",
    "search": "PEUGEOT - 505 SERIES",
    "md": "505"
  },
  {
    "mk": "PEUG",
    "search": "PEUGEOT - 604",
    "md": "604"
  },
  {
    "mk": "PIAG",
    "search": "PIAGGIO - TYPHOON",
    "md": "TYPH"
  },
  {
    "mk": "PJ",
    "search": "PJ - D7",
    "md": "D7"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - ACCLAIM",
    "md": "ACCL"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - ARROW",
    "md": "ARRO"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - BARRACUDA",
    "md": "BARR"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - BELVEDERE",
    "md": "BELV"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - BREEZE",
    "md": "BREE"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - CAMBRIDGE",
    "md": "CAMB"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - CARAVELLE",
    "md": "CARA"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - CHAMP",
    "md": "CHAM"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - COLT",
    "md": "COLT"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - CONQUEST",
    "md": "CONQ"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - CRANBROOK",
    "md": "CRA"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - CRICKET (IMPORTED)",
    "md": "CRIC"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - DUSTER",
    "md": "DUST"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - FURY (ALSO GRAN FURY)",
    "md": "FURY"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - GTX",
    "md": "GTX"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - HORIZON (ALSO TC3)",
    "md": "HORI"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - LASER",
    "md": "LASE"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - NEON",
    "md": "NEON"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - PLAZA",
    "md": "PLAZ"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - RELIANT",
    "md": "RELI"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - ROAD RUNNER",
    "md": "ROAD"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - SAPPORO",
    "md": "SAPO"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - SATELLITE",
    "md": "SATE"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - SAVOY",
    "md": "SAVO"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - SCAMP",
    "md": "SCAM"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - SIGNET",
    "md": "SIGN"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - SUBURBAN",
    "md": "SUBU"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - SUNDANCE",
    "md": "SUND"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - TURISMO",
    "md": "TURI"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - VALIANT",
    "md": "VALI"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - VIP",
    "md": "VIP"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - VOLARE",
    "md": "VOLA"
  },
  {
    "mk": "PLYM",
    "search": "PLYMOUTH - VOYAGER",
    "md": "VOYA"
  },
  {
    "mk": "POLE",
    "search": "POLESTAR - POLESTAR 1",
    "md": "POL1"
  },
  {
    "mk": "POLE",
    "search": "POLESTAR - POLESTAR 2",
    "md": "POL2"
  },
  {
    "mk": "POLE",
    "search": "POLESTAR - POLESTAR 3",
    "md": "POL3"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - SUNRUNNER",
    "md": "SUNR"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - 2000",
    "md": "2000"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - 2+2",
    "md": "2P2"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - 6000",
    "md": "6000"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - ASTRE",
    "md": "ASTR"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - AZTEK",
    "md": "AZTE"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - BONNEVILLE",
    "md": "BONN"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - CATALINA",
    "md": "CATA"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - CHIEFTAIN",
    "md": "CHIE"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - CUSTOM",
    "md": "CUS"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - DELUXE",
    "md": "DEL"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - EXECUTIVE",
    "md": "EXE"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - FIERO",
    "md": "FIER"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - FIREBIRD",
    "md": "FIRE"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - FIREFLY",
    "md": "FIRF"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - FIREHAWK",
    "md": "FIRH"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - G3",
    "md": "G3"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - G5",
    "md": "G5"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - G6",
    "md": "G6"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - GRAND AM",
    "md": "GRAN"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - GRAND PRIX",
    "md": "GRAP"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - GRAND VILLE",
    "md": "GRD"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - GT0",
    "md": "GT0"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - J2000",
    "md": "J200"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - LAURENTIAN",
    "md": "LAUR"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - LEMANS",
    "md": "LEMA"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - MONTANA",
    "md": "MONT"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - GRAND PARISIENNE",
    "md": "PARG"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - PARISIENNE",
    "md": "PARI"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - PHOENIX",
    "md": "PHOE"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - PURSUIT",
    "md": "PURS"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - SAFARI",
    "md": "SAFA"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - SKY CHIEF",
    "md": "SKY"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - SOLSTICE",
    "md": "SOLS"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - SSE",
    "md": "SSE"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - STAR CHIEF",
    "md": "STA"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - STREAMLINER",
    "md": "STR"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - STRATO CHIEF",
    "md": "STRA"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - SUNBIRD",
    "md": "SUNB"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - SUNFIRE",
    "md": "SUNF"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - SUPER CHIEF",
    "md": "SUP"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - T-1000",
    "md": "T10"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - TEMPEST GTO",
    "md": "TEMG"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - TEMPEST",
    "md": "TEMP"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - TORRENT",
    "md": "TORR"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - TRANS AM (SEE FIREBIRD)",
    "md": "TRAN"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - TRANS SPORT/TRANSPORT",
    "md": "TRAS"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - VENTURA",
    "md": "VENT"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - VIBE",
    "md": "VIBE"
  },
  {
    "mk": "PONT",
    "search": "PONTIAC - WAVE",
    "md": "WAVE"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - 1500",
    "md": "150"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - 1600",
    "md": "160"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - 356",
    "md": "356"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - 911",
    "md": "911"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - 912",
    "md": "912"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - 914",
    "md": "914"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - 918 SPYDER",
    "md": "918"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - 924",
    "md": "924"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - 928",
    "md": "928"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - 930",
    "md": "930"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - 944",
    "md": "944"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - 968",
    "md": "968"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - BOXSTER",
    "md": "BOXS"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - CABRIOLET",
    "md": "CABR"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - CARRERA",
    "md": "CARR"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - CAYENNE",
    "md": "CAYE"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - CAYMAN",
    "md": "CAYM"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - KARMAN",
    "md": "KARM"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - MACAN",
    "md": "MACA"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - PANAMERA",
    "md": "PANA"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - STANDARD",
    "md": "STA"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - SUPER",
    "md": "SUP"
  },
  {
    "mk": "PORS",
    "search": "PORSCHE - TARGA",
    "md": "TARG"
  },
  {
    "mk": "RAM",
    "search": "RAM - 1500",
    "md": "1500"
  },
  {
    "mk": "RAM",
    "search": "RAM - ProMaster",
    "md": "PROM"
  },
  {
    "mk": "RAM",
    "search": "RAM - 3500",
    "md": "3500"
  },
  {
    "mk": "RAM",
    "search": "RAM - 2500",
    "md": "2500"
  },
  {
    "mk": "RAMB",
    "search": "RAMBLER - AMBASSADOR",
    "md": "AMBA"
  },
  {
    "mk": "RAMB",
    "search": "RAMBLER - AMERICAN",
    "md": "AMER"
  },
  {
    "mk": "RAMB",
    "search": "RAMBLER - CLASSIC",
    "md": "CLAS"
  },
  {
    "mk": "RAMB",
    "search": "RAMBLER - CUSTOM",
    "md": "CUS"
  },
  {
    "mk": "RAMB",
    "search": "RAMBLER - DELUXE",
    "md": "DEL"
  },
  {
    "mk": "RAMB",
    "search": "RAMBLER - SUPER",
    "md": "SUP"
  },
  {
    "mk": "RAMB",
    "search": "RAMBLER - TYPHOON",
    "md": "TYP"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - 18i",
    "md": "18i"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - 750",
    "md": "750"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - CARAVELLE",
    "md": "CARA"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - DAUPHINE",
    "md": "DAU"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - ESTAFETTE",
    "md": "EST"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - EXPORT",
    "md": "EXPO"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - FUEGO",
    "md": "FUEG"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - GORDINI",
    "md": "GON"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - LE CAR",
    "md": "LEC"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - LUXE",
    "md": "LX"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - R-10",
    "md": "R10"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - R-12",
    "md": "R12"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - R-15",
    "md": "R15"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - R-16",
    "md": "R16"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - R-17",
    "md": "R17"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - R-4",
    "md": "R4"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - R-5",
    "md": "R5"
  },
  {
    "mk": "RENA",
    "search": "RENAULT - R-8",
    "md": "R8"
  },
  {
    "mk": "REXH",
    "search": "REXHALL - AERBUS",
    "md": "AERB"
  },
  {
    "mk": "REXH",
    "search": "REXHALL - CONCORD",
    "md": "CONC"
  },
  {
    "mk": "REXH",
    "search": "REXHALL - FLEETWOOD",
    "md": "FLEE"
  },
  {
    "mk": "REXH",
    "search": "REXHALL - REXAIR",
    "md": "REXA"
  },
  {
    "mk": "REXH",
    "search": "REXHALL - ROLLSAIR",
    "md": "ROLL"
  },
  {
    "mk": "RIVI",
    "search": "RIVIAN - R1S",
    "md": "R1S"
  },
  {
    "mk": "RIVI",
    "search": "RIVIAN - R1T",
    "md": "R1T"
  },
  {
    "mk": "ROLL",
    "search": "ROLLS-ROYCE - CAMARGUE",
    "md": "CAM"
  },
  {
    "mk": "ROLL",
    "search": "ROLLS-ROYCE - CORNICHE",
    "md": "CORN"
  },
  {
    "mk": "ROLL",
    "search": "ROLLS-ROYCE - FLYING SPUR",
    "md": "FPR"
  },
  {
    "mk": "ROLL",
    "search": "ROLLS-ROYCE - MULSANNE",
    "md": "MUL"
  },
  {
    "mk": "ROLL",
    "search": "ROLLS-ROYCE - PHANTOM",
    "md": "PHAN"
  },
  {
    "mk": "ROLL",
    "search": "ROLLS-ROYCE - SILVER SERAPH",
    "md": "SER"
  },
  {
    "mk": "ROLL",
    "search": "ROLLS-ROYCE - SILVER DAWN",
    "md": "SID"
  },
  {
    "mk": "ROLL",
    "search": "ROLLS-ROYCE - SILVER CLOUD",
    "md": "SILV"
  },
  {
    "mk": "ROLL",
    "search": "ROLLS-ROYCE - SILVER SHADOW",
    "md": "SIS"
  },
  {
    "mk": "ROLL",
    "search": "ROLLS-ROYCE - SILVER WRAITH",
    "md": "SIW"
  },
  {
    "mk": "ROLL",
    "search": "ROLLS-ROYCE - SILVER SPUR",
    "md": "SPR"
  },
  {
    "mk": "ROLL",
    "search": "ROLLS-ROYCE - SILVER SPIRIT",
    "md": "SSP"
  },
  {
    "mk": "ROOT",
    "search": "ROOTES - ALPINE",
    "md": "ALP"
  },
  {
    "mk": "ROOT",
    "search": "ROOTES - ARROW",
    "md": "ARR"
  },
  {
    "mk": "ROOT",
    "search": "ROOTES - IMP",
    "md": "IMP"
  },
  {
    "mk": "ROOT",
    "search": "ROOTES - TIGER",
    "md": "TIG"
  },
  {
    "mk": "ROVE",
    "search": "ROVER - 2000",
    "md": "200"
  },
  {
    "mk": "ROVE",
    "search": "ROVER - 3500",
    "md": "350"
  },
  {
    "mk": "ROVE",
    "search": "ROVER - 3 LITRE",
    "md": "3L"
  },
  {
    "mk": "ROVE",
    "search": "ROVER - LAND ROVER",
    "md": "LAND"
  },
  {
    "mk": "ROVE",
    "search": "ROVER - MARK IV",
    "md": "MK4"
  },
  {
    "mk": "SAAB",
    "search": "SAAB - 900",
    "md": "900"
  },
  {
    "mk": "SAAB",
    "search": "SAAB - 9000",
    "md": "9000"
  },
  {
    "mk": "SAAB",
    "search": "SAAB - 92",
    "md": "92"
  },
  {
    "mk": "SAAB",
    "search": "SAAB - 92X",
    "md": "92X"
  },
  {
    "mk": "SAAB",
    "search": "SAAB - 93 & 93B",
    "md": "93"
  },
  {
    "mk": "SAAB",
    "search": "SAAB - 95",
    "md": "95"
  },
  {
    "mk": "SAAB",
    "search": "SAAB - 96",
    "md": "96"
  },
  {
    "mk": "SAAB",
    "search": "SAAB - 97",
    "md": "97"
  },
  {
    "mk": "SAAB",
    "search": "SAAB - 97X",
    "md": "97X"
  },
  {
    "mk": "SAAB",
    "search": "SAAB - 99",
    "md": "99"
  },
  {
    "mk": "SAAB",
    "search": "SAAB - GT 750",
    "md": "GT"
  },
  {
    "mk": "SAAB",
    "search": "SAAB - SONNET",
    "md": "SON"
  },
  {
    "mk": "SAAB",
    "search": "SAAB - 9-3",
    "md": "9-3"
  },
  {
    "mk": "SANG",
    "search": "SANGYONG - CM600S",
    "md": "CM60"
  },
  {
    "mk": "SANG",
    "search": "SANGYONG - JEEP",
    "md": "JEEP"
  },
  {
    "mk": "SATU",
    "search": "SATURN - ASTRA",
    "md": "ASTR"
  },
  {
    "mk": "SATU",
    "search": "SATURN - EVI",
    "md": "EVI"
  },
  {
    "mk": "SATU",
    "search": "SATURN - ION",
    "md": "ION"
  },
  {
    "mk": "SATU",
    "search": "SATURN - LSERIES",
    "md": "LSER"
  },
  {
    "mk": "SATU",
    "search": "SATURN - RELAY",
    "md": "RELA"
  },
  {
    "mk": "SATU",
    "search": "SATURN - SC",
    "md": "SC"
  },
  {
    "mk": "SATU",
    "search": "SATURN - SKY",
    "md": "SKY"
  },
  {
    "mk": "SATU",
    "search": "SATURN - SL",
    "md": "SL"
  },
  {
    "mk": "SATU",
    "search": "SATURN - SW",
    "md": "SW"
  },
  {
    "mk": "SATU",
    "search": "SATURN - VUE",
    "md": "VUE"
  },
  {
    "mk": "SATU",
    "search": "SATURN - LW200",
    "md": "LW20"
  },
  {
    "mk": "SATU",
    "search": "SATURN - LS1",
    "md": "LS1"
  },
  {
    "mk": "SCIO",
    "search": "SCION - FR-S",
    "md": "FRS"
  },
  {
    "mk": "SCIO",
    "search": "SCION - TC",
    "md": "TC"
  },
  {
    "mk": "SCIO",
    "search": "SCION - XA",
    "md": "XA"
  },
  {
    "mk": "SCIO",
    "search": "SCION - XB",
    "md": "XB"
  },
  {
    "mk": "SCIO",
    "search": "SCION - IM",
    "md": "IM"
  },
  {
    "mk": "SHEB",
    "search": "SHELBY AMERICAN - COBRA GT500",
    "md": "C500"
  },
  {
    "mk": "SHEB",
    "search": "SHELBY AMERICAN - COBRA",
    "md": "COBR"
  },
  {
    "mk": "SHEB",
    "search": "SHELBY AMERICAN - CSX",
    "md": "CSX"
  },
  {
    "mk": "SIM",
    "search": "SIMCA - 1000 & 1000GL",
    "md": "100"
  },
  {
    "mk": "SIM",
    "search": "SIMCA - 120",
    "md": "120"
  },
  {
    "mk": "SIM",
    "search": "SIMCA - ARONDE",
    "md": "ARO"
  },
  {
    "mk": "SIM",
    "search": "SIMCA - BERTONE",
    "md": "BER"
  },
  {
    "mk": "SIM",
    "search": "SIMCA - ETOILE",
    "md": "ETO"
  },
  {
    "mk": "SIM",
    "search": "SIMCA - GLS",
    "md": "GLS"
  },
  {
    "mk": "SIM",
    "search": "SIMCA - VEDETTE",
    "md": "VED"
  },
  {
    "mk": "SIN",
    "search": "SINGER - CHAMOIS",
    "md": "CHA"
  },
  {
    "mk": "SIN",
    "search": "SINGER - VOGUE",
    "md": "VOG"
  },
  {
    "mk": "SMAR",
    "search": "SMART - FORTWO",
    "md": "FORT"
  },
  {
    "mk": "SOUT",
    "search": "SOUTHLAND - SL252T",
    "md": "252T"
  },
  {
    "mk": "STLG",
    "search": "STERLING - 825",
    "md": "825"
  },
  {
    "mk": "STLG",
    "search": "STERLING - 827",
    "md": "827"
  },
  {
    "mk": "STLG",
    "search": "STERLING - STERLING",
    "md": "TK"
  },
  {
    "mk": "STUD",
    "search": "STUDEBAKER - AVANTI",
    "md": "AVAN"
  },
  {
    "mk": "STUD",
    "search": "STUDEBAKER - CHALLENGER",
    "md": "CHAL"
  },
  {
    "mk": "STUD",
    "search": "STUDEBAKER - CHAMPION",
    "md": "CHAM"
  },
  {
    "mk": "STUD",
    "search": "STUDEBAKER - COMMANDER",
    "md": "COM"
  },
  {
    "mk": "STUD",
    "search": "STUDEBAKER - CRUISER",
    "md": "CRU"
  },
  {
    "mk": "STUD",
    "search": "STUDEBAKER - DAYTONA",
    "md": "DAYT"
  },
  {
    "mk": "STUD",
    "search": "STUDEBAKER - HAWK SERIES",
    "md": "HAWK"
  },
  {
    "mk": "STUD",
    "search": "STUDEBAKER - LANDALL",
    "md": "LAN"
  },
  {
    "mk": "STUD",
    "search": "STUDEBAKER - LANK SERIES",
    "md": "LAR"
  },
  {
    "mk": "STUD",
    "search": "STUDEBAKER - PRESIDENT",
    "md": "PRE"
  },
  {
    "mk": "STUD",
    "search": "STUDEBAKER - REGAL",
    "md": "REGA"
  },
  {
    "mk": "STUD",
    "search": "STUDEBAKER - SCOTSMAN",
    "md": "SCO"
  },
  {
    "mk": "STUD",
    "search": "STUDEBAKER - GRAND TURISMO",
    "md": "TURI"
  },
  {
    "mk": "STUD",
    "search": "STUDEBAKER - WAGONAIRE",
    "md": "WAGO"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - 100 SERIES",
    "md": "100"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - 1100 SERIES",
    "md": "110"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - 1300 SERIES",
    "md": "130"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - 1400 SERIES",
    "md": "140"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - 1600 SERIES",
    "md": "160"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - BAJA",
    "md": "BAJA"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - BRZ",
    "md": "BRZ"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - CROSSTREK",
    "md": "CROS"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - DL",
    "md": "DL"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - FE",
    "md": "FE2"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - FORESTER",
    "md": "FORR"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - GL",
    "md": "GL"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - GLF",
    "md": "GLF"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - IMPREZA OUTBACK",
    "md": "IMPO"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - IMPREZA",
    "md": "IMPR"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - JUSTY",
    "md": "JUST"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - LEGACY",
    "md": "LEGA"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - LEGACY OUTBACK",
    "md": "LEGO"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - LEONE GL COUPE",
    "md": "LEON"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - LOYALE",
    "md": "LOYA"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - RX",
    "md": "RX"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - OUTBACK SPORT (SW)",
    "md": "SPOR"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - STANDARD",
    "md": "STA"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - SVX",
    "md": "SVX"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - TRIBECA",
    "md": "TRIB"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - WRX",
    "md": "WRX"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - XT6",
    "md": "XT6"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - XT COUPE",
    "md": "XTC"
  },
  {
    "mk": "SUBA",
    "search": "SUBARU - ASCENT",
    "md": "ASCE"
  },
  {
    "mk": "SUNB",
    "search": "SUNBEAM - ALPINE",
    "md": "ALP"
  },
  {
    "mk": "SUNB",
    "search": "SUNBEAM - ARROW",
    "md": "ARR"
  },
  {
    "mk": "SUNB",
    "search": "SUNBEAM - DELUXE",
    "md": "DEL"
  },
  {
    "mk": "SUNB",
    "search": "SUNBEAM - IMP",
    "md": "IMP"
  },
  {
    "mk": "SUNB",
    "search": "SUNBEAM - MINX",
    "md": "MINX"
  },
  {
    "mk": "SUNB",
    "search": "SUNBEAM - RAPIER",
    "md": "RAP"
  },
  {
    "mk": "SUNB",
    "search": "SUNBEAM - TIGER",
    "md": "TIG"
  },
  {
    "mk": "SUZU",
    "search": "SUZUKI - AERIO",
    "md": "AERI"
  },
  {
    "mk": "SUZU",
    "search": "SUZUKI - ESTEEM",
    "md": "ESTE"
  },
  {
    "mk": "SUZU",
    "search": "SUZUKI - FORSA",
    "md": "FORS"
  },
  {
    "mk": "SUZU",
    "search": "SUZUKI - GRAND VITARA",
    "md": "GRVI"
  },
  {
    "mk": "SUZU",
    "search": "SUZUKI - SAMURAI",
    "md": "SAMU"
  },
  {
    "mk": "SUZU",
    "search": "SUZUKI - SIDEKICK",
    "md": "SIDE"
  },
  {
    "mk": "SUZU",
    "search": "SUZUKI - SWIFT",
    "md": "SWIF"
  },
  {
    "mk": "SUZU",
    "search": "SUZUKI - SX4",
    "md": "SX4"
  },
  {
    "mk": "SUZU",
    "search": "SUZUKI - VERONA",
    "md": "VER"
  },
  {
    "mk": "SUZU",
    "search": "SUZUKI - VITARA",
    "md": "VITA"
  },
  {
    "mk": "SUZU",
    "search": "SUZUKI - X90",
    "md": "X90"
  },
  {
    "mk": "SUZU",
    "search": "SUZUKI - XL7",
    "md": "XL7"
  },
  {
    "mk": "SUZU",
    "search": "SUZUKI - KIZASHI",
    "md": "KIZA"
  },
  {
    "mk": "TESL",
    "search": "TESLA MOTORS - MODEL 3",
    "md": "3"
  },
  {
    "mk": "TESL",
    "search": "TESLA MOTORS - ROADSTER",
    "md": "ROAD"
  },
  {
    "mk": "TESL",
    "search": "TESLA MOTORS - MODEL S",
    "md": "S"
  },
  {
    "mk": "TESL",
    "search": "TESLA MOTORS - MODEL X",
    "md": "X"
  },
  {
    "mk": "TESL",
    "search": "TESLA MOTORS - MODEL Y",
    "md": "Y"
  },
  {
    "mk": "THOM",
    "search": "THOMAS - SCHOOL BUS",
    "md": "BUS"
  },
  {
    "mk": "THOR",
    "search": "THOR INDUSTRIES INC. - WAVE",
    "md": "WAVE"
  },
  {
    "mk": "THOR",
    "search": "THOR INDUSTRIES INC. - ACE",
    "md": "ACE"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - 4-RUNNER",
    "md": "4RUN"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - 86",
    "md": "86"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - ALPHARD",
    "md": "ALPH"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - ARISTO",
    "md": "ARIS"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - AVALON",
    "md": "AVAL"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - AVENSIS",
    "md": "AVEN"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - CAMRY",
    "md": "CAMR"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - CARINA",
    "md": "CARI"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - CAVALIER",
    "md": "CAVA"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - CELICA",
    "md": "CELI"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - C-HR",
    "md": "CHR"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - COROLLA",
    "md": "CORO"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - CRESSIDA",
    "md": "CRES"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - CROWN",
    "md": "CROW"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - ECHO",
    "md": "ECHO"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - FJ CRUISER",
    "md": "FJ"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - HIGHLANDER",
    "md": "HIGH"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - HILUX",
    "md": "HILU"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - LAND CRUISER",
    "md": "LAND"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - LE VAN",
    "md": "LEVA"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - MARK II",
    "md": "MARK"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - MATRIX",
    "md": "MATR"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - MR2",
    "md": "MR2"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - PASEO",
    "md": "PASE"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - PRE RUNNER",
    "md": "PRE"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - PREVIA",
    "md": "PREV"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - PRIUS",
    "md": "PRI"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - RAV4",
    "md": "RAV4"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - SCION",
    "md": "SCIO"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - SEQUOIA",
    "md": "SEQU"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - SIENNA",
    "md": "SIEN"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - SOLARA",
    "md": "SOLA"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - SR5",
    "md": "SR5"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - STARLET",
    "md": "STAR"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - SUPRA",
    "md": "SUPR"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - T-100",
    "md": "T100"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - TACOMA",
    "md": "TACO"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - TERCEL",
    "md": "TERC"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - TUNDRA",
    "md": "TUND"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - VENZA",
    "md": "VENZ"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - YARIS",
    "md": "YARI"
  },
  {
    "mk": "TOYO",
    "search": "TOYOTA - MIRAI",
    "md": "MIRA"
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH - 1200",
    "md": "1200"
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH - 1250",
    "md": "1250"
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH - 1300",
    "md": "1300"
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH - 2000",
    "md": "2000"
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH - 250",
    "md": "250"
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH - GT SERIES",
    "md": "GT"
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH - HERALD",
    "md": "HERA"
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH - SPORT 6",
    "md": "SP6"
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH - SPITFIRE",
    "md": "SPIT"
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH - STAG",
    "md": "STA"
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH - TR-3 & TR-3A",
    "md": "TR3"
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH - TR-4 & TR-4A",
    "md": "TR4"
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH - TR6",
    "md": "TR6"
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH - TR7",
    "md": "TR7"
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH - TR8",
    "md": "TR8"
  },
  {
    "mk": "TRIU",
    "search": "TRIUMPH - VITESSE",
    "md": "VITE"
  },
  {
    "mk": "TVR",
    "search": "TVR - TUSCAN",
    "md": "TUS"
  },
  {
    "mk": "TVR",
    "search": "TVR - VIXEN",
    "md": "VIXE"
  },
  {
    "mk": "UAZ",
    "search": "UAZ (ULIANOVSK AUTOMOBILE ZAVOD) - CCMV",
    "md": "TK"
  },
  {
    "mk": "USEL",
    "search": "U.S. ELECTRICAR CORP. - LECTRIC LEOPARD",
    "md": "LTC"
  },
  {
    "mk": "VACR",
    "search": "VECTOR AEROMOTIVE CORPORATION - M12 (SPORTS COUPE)",
    "md": "M12"
  },
  {
    "mk": "VACR",
    "search": "VECTOR AEROMOTIVE CORPORATION - VECTOR",
    "md": "VECT"
  },
  {
    "mk": "VANG",
    "search": "VANGUARD (CANADA) - DELUXE",
    "md": "DEL"
  },
  {
    "mk": "VANG",
    "search": "VANGUARD (CANADA) - ENSIGN",
    "md": "ENS"
  },
  {
    "mk": "VANG",
    "search": "VANGUARD (CANADA) - LUXURY",
    "md": "LUX"
  },
  {
    "mk": "VANG",
    "search": "VANGUARD (CANADA) - MARK III",
    "md": "MK3"
  },
  {
    "mk": "VAUX",
    "search": "VAUXHALL - CRESTA",
    "md": "CRE"
  },
  {
    "mk": "VAUX",
    "search": "VAUXHALL - ENVOY",
    "md": "ENVO"
  },
  {
    "mk": "VAUX",
    "search": "VAUXHALL - EPIC",
    "md": "EPIC"
  },
  {
    "mk": "VAUX",
    "search": "VAUXHALL - FIRENZA",
    "md": "FIRE"
  },
  {
    "mk": "VAUX",
    "search": "VAUXHALL - VELOX",
    "md": "VEL"
  },
  {
    "mk": "VAUX",
    "search": "VAUXHALL - VICTOR",
    "md": "VICT"
  },
  {
    "mk": "VAUX",
    "search": "VAUXHALL - VIVA",
    "md": "VIVA"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - 113",
    "md": "113"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - 1200",
    "md": "1200"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - 1300",
    "md": "1300"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - 1500",
    "md": "1500"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - 411/412",
    "md": "412"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - BEETLE",
    "md": "BEET"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - CABRIOLET",
    "md": "CABR"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - CORRADO",
    "md": "CORR"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - DASHER",
    "md": "DAS"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - EOS",
    "md": "EOS"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - EUROVAN",
    "md": "EURO"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - FASTBACK",
    "md": "FAST"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - FOX",
    "md": "FOX"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - GOLF",
    "md": "GOLF"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - GTI",
    "md": "GTI"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - JETTA",
    "md": "JETT"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - KARMANN GHIA",
    "md": "KARM"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - PASSAT",
    "md": "PASS"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - PHAETON",
    "md": "PHAE"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - POLO",
    "md": "POLO"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - QUANTUM",
    "md": "QUAN"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - RABBIT",
    "md": "RABB"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - ROUTAN",
    "md": "ROUT"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - SQUAREBACK",
    "md": "SB"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - SCIROCCO",
    "md": "SCIR"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - SUNROOF",
    "md": "SUR"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - THE THING",
    "md": "THIN"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - TIGUAN",
    "md": "TIGU"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - TOUAREG",
    "md": "TOUA"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - VANAGON",
    "md": "VANA"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - VARIANT",
    "md": "VAR"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - WESTFALIA",
    "md": "WEST"
  },
  {
    "mk": "VOLK",
    "search": "VOLKSWAGEN - ATLAS",
    "md": "ATLA"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - 122 SERIES",
    "md": "122"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - 140 SERIES",
    "md": "140"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - 164 SERIES",
    "md": "164"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - 1800 SERIES",
    "md": "180"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - P1900",
    "md": "190"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - 200 SERIES",
    "md": "200"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - 240 SERIES",
    "md": "240"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - 245 SERIES",
    "md": "245"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - 260 SERIES",
    "md": "260"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - PV444",
    "md": "444"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - PV544",
    "md": "544"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - 740 SERIES",
    "md": "740"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - 745 SERIES",
    "md": "745"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - 760",
    "md": "760"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - 765 SERIES",
    "md": "765"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - 780 SERIES",
    "md": "780"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - 850 SERIES",
    "md": "850"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - 940",
    "md": "940"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - 960",
    "md": "960"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - C30",
    "md": "C30"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - C70",
    "md": "C70"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - COMBI",
    "md": "COB"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - DL",
    "md": "DL"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - GL",
    "md": "GL"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - GLE",
    "md": "GLE"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - GLT",
    "md": "GLT"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - R4",
    "md": "R4"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - S40",
    "md": "S40"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - S60",
    "md": "S60"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - S70",
    "md": "S70"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - S80",
    "md": "S80"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - S90",
    "md": "S90"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - SPORT",
    "md": "SPO"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - V40",
    "md": "V40"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - V50",
    "md": "V50"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - V70",
    "md": "V70"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - V90",
    "md": "V90"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - XC70",
    "md": "XC70"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - XC90",
    "md": "XC90"
  },
  {
    "mk": "VOLV",
    "search": "VOLVO - XC60",
    "md": "XC60"
  },
  {
    "mk": "ZCZY",
    "search": "ZASTAVIA (ZCZ-YUGOSLAVIA) - YUGO (SERIES)",
    "md": "YUG"
  }
]

old_vehicle_data = [
                        {
                            "mk": "AMGN",
                            "search": " - Hummer",
                            "md": "HUMM"
                        },
                        {
                            "mk": "AC",
                            "search": "A C (GREAT BRITIAN) - 3000 ME",
                            "md": "300"
                        },
                        {
                            "mk": "ABAR",
                            "search": "ABARTH - ",
                            "md": ""
                        },
                        {
                            "mk": "COBR",
                            "search": "AC COBRA - ",
                            "md": ""
                        },
                        {
                            "mk": "ACAD",
                            "search": "ACADIAN (GM OF CANADA) - BEAUMONT SERIES",
                            "md": "BEAU"
                        },
                        {
                            "mk": "ACAD",
                            "search": "ACADIAN (GM OF CANADA) - CANSO SERIES",
                            "md": "CANS"
                        },
                        {
                            "mk": "ACAD",
                            "search": "ACADIAN (GM OF CANADA) - INVADER SERIES",
                            "md": "INVA"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - 1.6 EL",
                            "md": "1.6E"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - 1.7 EL",
                            "md": "1.7E"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - 2.3",
                            "md": "2.3"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - 2.5 TL",
                            "md": "2.5T"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - 3.2 TL",
                            "md": "3.2T"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - 3.2CL",
                            "md": "3.2C"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - 3.5 RL",
                            "md": "3.5R"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - CL (SPORTS COUPE)",
                            "md": "CL"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - CSX",
                            "md": "CSX"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - EL",
                            "md": "EL"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - ILX",
                            "md": "ILX"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - INTEGRA",
                            "md": "INTE"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - LEGEND",
                            "md": "LEGE"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - MDX",
                            "md": "MDX"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - NSX",
                            "md": "NSX"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - RDX",
                            "md": "RDX"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - RL",
                            "md": "RL"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - RSX",
                            "md": "RSX"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - SLX (SPORTS UTILITY)",
                            "md": "SLX"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - TL",
                            "md": "ATL"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - TLX",
                            "md": "TLX"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - TSX",
                            "md": "TSX"
                        },
                        {
                            "mk": "ACUR",
                            "search": "ACURA - VIGOR",
                            "md": "VIGO"
                        },
                        {
                            "mk": "ADET",
                            "search": "ADETTE - ",
                            "md": ""
                        },
                        {
                            "mk": "ADVA",
                            "search": "ADVANCED - ",
                            "md": ""
                        },
                        {
                            "mk": "AERO",
                            "search": "AEROCAR - ",
                            "md": ""
                        },
                        {
                            "mk": "AETA",
                            "search": "AETA - ",
                            "md": ""
                        },
                        {
                            "mk": "ALFA",
                            "search": "ALFA ROMEO - 164",
                            "md": "164"
                        },
                        {
                            "mk": "ALFA",
                            "search": "ALFA ROMEO - ALFA GT6",
                            "md": "GT6"
                        },
                        {
                            "mk": "ALFA",
                            "search": "ALFA ROMEO - ALFETTA GT",
                            "md": "AGT"
                        },
                        {
                            "mk": "ALFA",
                            "search": "ALFA ROMEO - ARNA",
                            "md": "ARN"
                        },
                        {
                            "mk": "ALFA",
                            "search": "ALFA ROMEO - BERLINA",
                            "md": "BERL"
                        },
                        {
                            "mk": "ALFA",
                            "search": "ALFA ROMEO - C4",
                            "md": "C4"
                        },
                        {
                            "mk": "ALFA",
                            "search": "ALFA ROMEO - DUETTO",
                            "md": "DUET"
                        },
                        {
                            "mk": "ALFA",
                            "search": "ALFA ROMEO - GIULIA",
                            "md": "GIUL"
                        },
                        {
                            "mk": "ALFA",
                            "search": "ALFA ROMEO - GIULIA SPRINT",
                            "md": "SPRI"
                        },
                        {
                            "mk": "ALFA",
                            "search": "ALFA ROMEO - GT VELOCE",
                            "md": "VELO"
                        },
                        {
                            "mk": "ALFA",
                            "search": "ALFA ROMEO - GTV6 2.5",
                            "md": "G25"
                        },
                        {
                            "mk": "ALFA",
                            "search": "ALFA ROMEO - MILANO",
                            "md": "MILA"
                        },
                        {
                            "mk": "ALFA",
                            "search": "ALFA ROMEO - MONTREAL",
                            "md": "MONT"
                        },
                        {
                            "mk": "ALFA",
                            "search": "ALFA ROMEO - SPIDER SERIES",
                            "md": "SPYD"
                        },
                        {
                            "mk": "ALFA",
                            "search": "ALFA ROMEO - ZAGATO",
                            "md": "ZAGA"
                        },
                        {
                            "mk": "ALLS",
                            "search": "ALL STATE - ",
                            "md": ""
                        },
                        {
                            "mk": "ALLA",
                            "search": "ALLARD - ",
                            "md": ""
                        },
                        {
                            "mk": "ALCI",
                            "search": "ALLEN COACHWORKS INC. - ",
                            "md": ""
                        },
                        {
                            "mk": "ALLF",
                            "search": "ALLISONS FIBERGLASS MFG.INC. - ",
                            "md": ""
                        },
                        {
                            "mk": "ALMA",
                            "search": "ALMA - ",
                            "md": ""
                        },
                        {
                            "mk": "ALPI",
                            "search": "ALPHINE - ",
                            "md": ""
                        },
                        {
                            "mk": "ALTA",
                            "search": "ALTA - ",
                            "md": ""
                        },
                        {
                            "mk": "ALVI",
                            "search": "ALVIS - ",
                            "md": ""
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - ALLIANCE",
                            "md": "ALLI"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - AMBASSADOR",
                            "md": "AMBA"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - AMERICAN",
                            "md": "AMER"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - AMX",
                            "md": "AMX"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - CONCORD",
                            "md": "CONC"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - EAGLE",
                            "md": "EAGL"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - ENCORE",
                            "md": "ENCO"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - GREMLIN",
                            "md": "GREM"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - HORNET",
                            "md": "HORN"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - JAVELIN",
                            "md": "JAVE"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - MARLIN",
                            "md": "MARL"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - MATADOR",
                            "md": "MATA"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - MEDALLION",
                            "md": "MEDA"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - PACER",
                            "md": "PACE"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - RAMBLER",
                            "md": "RAMB"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - REBEL",
                            "md": "REBE"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - SPIRIT",
                            "md": "SPIR"
                        },
                        {
                            "mk": "AMER",
                            "search": "AMERICAN MOTORS - SPORTABOUT",
                            "md": "SPOR"
                        },
                        {
                            "mk": "AMPH",
                            "search": "AMPHICAR - ",
                            "md": ""
                        },
                        {
                            "mk": "ANSE",
                            "search": "ANSER MANUFACTURING LTD - ",
                            "md": ""
                        },
                        {
                            "mk": "ARGO",
                            "search": "ARGONAUT STATE LIMOUSINE - ",
                            "md": ""
                        },
                        {
                            "mk": "ARIS",
                            "search": "ARISTA - ",
                            "md": ""
                        },
                        {
                            "mk": "ARMS",
                            "search": "ARMSTRONG SIDDELEY - ",
                            "md": ""
                        },
                        {
                            "mk": "ARNO",
                            "search": "ARNOLT-BRISTOL - ",
                            "md": ""
                        },
                        {
                            "mk": "ASA",
                            "search": "ASA - ",
                            "md": ""
                        },
                        {
                            "mk": "ASCO",
                            "search": "ASCORT - ",
                            "md": ""
                        },
                        {
                            "mk": "ASHL",
                            "search": "ASHLEY - ",
                            "md": ""
                        },
                        {
                            "mk": "ASVE",
                            "search": "ASSEMBLED VEHICLE - ",
                            "md": ""
                        },
                        {
                            "mk": "ASTO",
                            "search": "ASTON-MARTIN - DB-5",
                            "md": "DB5"
                        },
                        {
                            "mk": "ASTO",
                            "search": "ASTON-MARTIN - DB-6",
                            "md": "DB6"
                        },
                        {
                            "mk": "ASTO",
                            "search": "ASTON-MARTIN - DB7(COUPE)",
                            "md": "DB7"
                        },
                        {
                            "mk": "ASTO",
                            "search": "ASTON-MARTIN - LAGONDA",
                            "md": "LAGO"
                        },
                        {
                            "mk": "ASTO",
                            "search": "ASTON-MARTIN - VANTAGE",
                            "md": "VANT"
                        },
                        {
                            "mk": "ASTO",
                            "search": "ASTON-MARTIN - VIRAGE (SALOON)",
                            "md": "VIR"
                        },
                        {
                            "mk": "ASUN",
                            "search": "ASUNA - GT",
                            "md": "GT"
                        },
                        {
                            "mk": "ASUN",
                            "search": "ASUNA - SE",
                            "md": "SE"
                        },
                        {
                            "mk": "ASUN",
                            "search": "ASUNA - SUNFIRE",
                            "md": "SUNF"
                        },
                        {
                            "mk": "ASUN",
                            "search": "ASUNA - SUNRUNNER",
                            "md": "SUNR"
                        },
                        {
                            "mk": "AUBU",
                            "search": "AUBURN - ",
                            "md": ""
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - 100",
                            "md": "100"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - 100GL",
                            "md": "1GL"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - 100LS",
                            "md": "1LS"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - 200LS",
                            "md": "200"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - 4000",
                            "md": "400"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - 5000",
                            "md": "500"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - 80",
                            "md": "A80"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - 80 LS (FOX)",
                            "md": "FOX"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - 850",
                            "md": "850"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - 90",
                            "md": "A90"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - A3",
                            "md": "A3"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - A4",
                            "md": "A4"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - A5",
                            "md": "A5"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - A6",
                            "md": "A6"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - A7",
                            "md": "A7"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - A8",
                            "md": "A8"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - AS4",
                            "md": "AS4"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - AVANT",
                            "md": "AVA"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - CABRIOLET",
                            "md": "CABR"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - E-TRON",
                            "md": "ETRO"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - Q3",
                            "md": "Q3"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - Q5",
                            "md": "Q5"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - Q7",
                            "md": "Q7"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - Q8",
                            "md": "Q8"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - QUATTRO",
                            "md": "QUAT"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - R8",
                            "md": "R8"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - RS3",
                            "md": "RS3"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - RS5",
                            "md": "RS5"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - RS6",
                            "md": "RS6"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - S3",
                            "md": "S3"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - S4",
                            "md": "S4"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - S5",
                            "md": "S5"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - S6",
                            "md": "AS6"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - S6",
                            "md": "S6"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - SQ5",
                            "md": "SQ5"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - SUPER 90",
                            "md": "S90"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - TT",
                            "md": "TT"
                        },
                        {
                            "mk": "AUDI",
                            "search": "AUDI - V-8",
                            "md": "V8"
                        },
                        {
                            "mk": "AURO",
                            "search": "AURORA - ",
                            "md": ""
                        },
                        {
                            "mk": "AUST",
                            "search": "AUSTIN-HEALY - 100 SERIES",
                            "md": "100"
                        },
                        {
                            "mk": "AUST",
                            "search": "AUSTIN-HEALY - 1100",
                            "md": "110"
                        },
                        {
                            "mk": "AUST",
                            "search": "AUSTIN-HEALY - 1800",
                            "md": "180"
                        },
                        {
                            "mk": "AUST",
                            "search": "AUSTIN-HEALY - 3000 SERIES",
                            "md": "300"
                        },
                        {
                            "mk": "AUST",
                            "search": "AUSTIN-HEALY - 850",
                            "md": "850"
                        },
                        {
                            "mk": "AUST",
                            "search": "AUSTIN-HEALY - A40",
                            "md": "A40"
                        },
                        {
                            "mk": "AUST",
                            "search": "AUSTIN-HEALY - A55",
                            "md": "A55"
                        },
                        {
                            "mk": "AUST",
                            "search": "AUSTIN-HEALY - A99 & 110",
                            "md": "A10"
                        },
                        {
                            "mk": "AUST",
                            "search": "AUSTIN-HEALY - CAMBRIDGE",
                            "md": "A60"
                        },
                        {
                            "mk": "AUST",
                            "search": "AUSTIN-HEALY - COOPER S",
                            "md": "CPS"
                        },
                        {
                            "mk": "AUST",
                            "search": "AUSTIN-HEALY - MARINA",
                            "md": "MARI"
                        },
                        {
                            "mk": "AUST",
                            "search": "AUSTIN-HEALY - MINI",
                            "md": "MINI"
                        },
                        {
                            "mk": "AUST",
                            "search": "AUSTIN-HEALY - SPRITE",
                            "md": "SPRI"
                        },
                        {
                            "mk": "AUST",
                            "search": "AUSTIN-HEALY - WESTMINSTER",
                            "md": "WEST"
                        },
                        {
                            "mk": "AUTU",
                            "search": "AUTO UNION - ",
                            "md": ""
                        },
                        {
                            "mk": "AUTA",
                            "search": "AUTOBIANCHI - ",
                            "md": ""
                        },
                        {
                            "mk": "AUTB",
                            "search": "AUTOBIEU - ",
                            "md": ""
                        },
                        {
                            "mk": "AUTO",
                            "search": "AUTOCAR - ",
                            "md": ""
                        },
                        {
                            "mk": "AUTR",
                            "search": "AUTOCARRIER AND A.C. - ",
                            "md": ""
                        },
                        {
                            "mk": "AUKR",
                            "search": "AUTOKRAFT - ",
                            "md": ""
                        },
                        {
                            "mk": "AVAN",
                            "search": "AVANTI - SERIES A",
                            "md": "AAV"
                        },
                        {
                            "mk": "AVAN",
                            "search": "AVANTI - SERIES B",
                            "md": "ABV"
                        },
                        {
                            "mk": "AVEN",
                            "search": "AVENGER - ",
                            "md": ""
                        },
                        {
                            "mk": "AVIA",
                            "search": "AVIA - ",
                            "md": ""
                        },
                        {
                            "mk": "BZEL",
                            "search": "B & Z ELECTRIC CAR CO. - CADILLAC",
                            "md": "CADI"
                        },
                        {
                            "mk": "BZEL",
                            "search": "B & Z ELECTRIC CAR CO. - ELECTRA-KING",
                            "md": "ELEC"
                        },
                        {
                            "mk": "BMC",
                            "search": "B M C - PRINCESS",
                            "md": "PRI"
                        },
                        {
                            "mk": "BANT",
                            "search": "BANTAM - ",
                            "md": ""
                        },
                        {
                            "mk": "BAY",
                            "search": "BAYLINER - ",
                            "md": ""
                        },
                        {
                            "mk": "BEAR",
                            "search": "BEARDMORE - ",
                            "md": ""
                        },
                        {
                            "mk": "BEDF",
                            "search": "BEDFORD - ",
                            "md": ""
                        },
                        {
                            "mk": "BEJE",
                            "search": "BEIJING JEEP - GANG STAR",
                            "md": "TK"
                        },
                        {
                            "mk": "BENT",
                            "search": "BENTLEY - ARNAGE",
                            "md": "ARN"
                        },
                        {
                            "mk": "BENT",
                            "search": "BENTLEY - AZURE",
                            "md": "AZU"
                        },
                        {
                            "mk": "BENT",
                            "search": "BENTLEY - BROOKLANDS",
                            "md": "BROO"
                        },
                        {
                            "mk": "BENT",
                            "search": "BENTLEY - CONTINENTAL CONVERTIBLE",
                            "md": "CONT"
                        },
                        {
                            "mk": "BENT",
                            "search": "BENTLEY - CORNICHE",
                            "md": "CORN"
                        },
                        {
                            "mk": "BENT",
                            "search": "BENTLEY - EIGHT",
                            "md": "EIGH"
                        },
                        {
                            "mk": "BENT",
                            "search": "BENTLEY - MULSANNE",
                            "md": "MULS"
                        },
                        {
                            "mk": "BENT",
                            "search": "BENTLEY - TURBO R",
                            "md": "TBR"
                        },
                        {
                            "mk": "BERG",
                            "search": "BERGANTINE - ",
                            "md": ""
                        },
                        {
                            "mk": "BERK",
                            "search": "BERKELEY - ",
                            "md": ""
                        },
                        {
                            "mk": "BERO",
                            "search": "BERTONE - CABRIO",
                            "md": "CABR"
                        },
                        {
                            "mk": "BERO",
                            "search": "BERTONE - PALINURO",
                            "md": "PALI"
                        },
                        {
                            "mk": "BERO",
                            "search": "BERTONE - X19",
                            "md": "X19"
                        },
                        {
                            "mk": "BESA",
                            "search": "BESASIE AUTOMOBILE CO. INC. - BACI",
                            "md": "BAC"
                        },
                        {
                            "mk": "BIGT",
                            "search": "BIG TEX - DUMP",
                            "md": "DUMP"
                        },
                        {
                            "mk": "BITT",
                            "search": "BITTER - ",
                            "md": ""
                        },
                        {
                            "mk": "BIZZ",
                            "search": "BIZZARRINI - ",
                            "md": ""
                        },
                        {
                            "mk": "BLUE",
                            "search": "BLUEBIRD - ",
                            "md": ""
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 128i",
                            "md": "128I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 135i",
                            "md": "135I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 1600",
                            "md": "160"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 1800",
                            "md": "180"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 2.8",
                            "md": "2.8"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 2000 SERIES",
                            "md": "200"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 2002 SERIES",
                            "md": "202"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 230i",
                            "md": "230I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 2500 SERIES",
                            "md": "250"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 2800 SERIES",
                            "md": "280"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 3.0 si",
                            "md": "3"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 318i",
                            "md": "318i"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 318ti",
                            "md": "318T"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 320i",
                            "md": "320"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 323i",
                            "md": "323I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 325",
                            "md": "325"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 325i",
                            "md": "32I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 328d",
                            "md": "328D"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 328i",
                            "md": "28I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 328is",
                            "md": "328"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 330 SERIES",
                            "md": "330"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 330i",
                            "md": "330I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 335",
                            "md": "335"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 335Xi",
                            "md": "335X"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 335d",
                            "md": "335D"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 335i",
                            "md": "335I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 428i",
                            "md": "428I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 430i",
                            "md": "430I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 435i",
                            "md": "435I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 440i",
                            "md": "440I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 520",
                            "md": "520"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 524 SERIES",
                            "md": "524"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 525i",
                            "md": "525I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 525ia",
                            "md": "525"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 528i",
                            "md": "528i"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 530i",
                            "md": "530i"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 533i",
                            "md": "533i"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 535 SERIES",
                            "md": "535"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 540",
                            "md": "540"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 540i",
                            "md": "540I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 545i",
                            "md": "545I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 550",
                            "md": "550"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 600",
                            "md": "600"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 630csi",
                            "md": "630"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 633csi",
                            "md": "633"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 635 SERIES",
                            "md": "635"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 645ci",
                            "md": "645C"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 645i",
                            "md": "645I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 650 SERIES",
                            "md": "650"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 733 SERIES",
                            "md": "733"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 735 SERIES",
                            "md": "735"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 740",
                            "md": "740"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 740i",
                            "md": "740i"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 745i",
                            "md": "745i"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 750",
                            "md": "750"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 750il",
                            "md": "750I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 750li",
                            "md": "750L"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 760i",
                            "md": "760I"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 760li",
                            "md": "760L"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 840ci",
                            "md": "840"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 850ci",
                            "md": "850C"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - 850i",
                            "md": "850"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - BAVARIA",
                            "md": "BAVA"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - I3",
                            "md": "I3"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - ISETTA",
                            "md": "ISLE"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - L6",
                            "md": "L6"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - L7",
                            "md": "L7"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - M235i",
                            "md": "M235"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - M3",
                            "md": "M3"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - M4",
                            "md": "M4"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - M5",
                            "md": "M5"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - M6",
                            "md": "M6"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - TI",
                            "md": "TI"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - X1",
                            "md": "X1"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - X2",
                            "md": "X2"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - X3",
                            "md": "X3"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - X4",
                            "md": "X4"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - X5",
                            "md": "X5"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - X6",
                            "md": "X6"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - Z3",
                            "md": "Z3"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - Z4",
                            "md": "Z4"
                        },
                        {
                            "mk": "BMW",
                            "search": "BMW - i8",
                            "md": "I8"
                        },
                        {
                            "mk": "BOBB",
                            "search": "BOBBI-KAR - ",
                            "md": ""
                        },
                        {
                            "mk": "BOCA",
                            "search": "BOCAR - ",
                            "md": ""
                        },
                        {
                            "mk": "BOM",
                            "search": "BOMBARDIER - ",
                            "md": ""
                        },
                        {
                            "mk": "BONA",
                            "search": "BONAIR LEISURE PRODUCTS LTD. - ",
                            "md": ""
                        },
                        {
                            "mk": "BOND",
                            "search": "BOND - ",
                            "md": ""
                        },
                        {
                            "mk": "BORG",
                            "search": "BORGWARD - BEL AIR",
                            "md": "BELA"
                        },
                        {
                            "mk": "BORG",
                            "search": "BORGWARD - BERETTA",
                            "md": "BERE"
                        },
                        {
                            "mk": "BORG",
                            "search": "BORGWARD - BISCAYNE",
                            "md": "BISC"
                        },
                        {
                            "mk": "BORG",
                            "search": "BORGWARD - HANSA",
                            "md": "HANS"
                        },
                        {
                            "mk": "BORG",
                            "search": "BORGWARD - ISABELLA",
                            "md": "ISAB"
                        },
                        {
                            "mk": "BOS",
                            "search": "BOSTON WHALER - ",
                            "md": ""
                        },
                        {
                            "mk": "BRDL",
                            "search": "BRADLEY GT - ",
                            "md": ""
                        },
                        {
                            "mk": "BRAS",
                            "search": "BRASINCA - ",
                            "md": ""
                        },
                        {
                            "mk": "BREM",
                            "search": "BREMEN SPORT EQUIPMENT - CREIGHTON",
                            "md": "CREI"
                        },
                        {
                            "mk": "BREM",
                            "search": "BREMEN SPORT EQUIPMENT - LAUFER",
                            "md": "LAUF"
                        },
                        {
                            "mk": "BREM",
                            "search": "BREMEN SPORT EQUIPMENT - MAXI-TAXI",
                            "md": "MAXI"
                        },
                        {
                            "mk": "BREM",
                            "search": "BREMEN SPORT EQUIPMENT - MINI-MARK",
                            "md": "MINI"
                        },
                        {
                            "mk": "BREM",
                            "search": "BREMEN SPORT EQUIPMENT - SEBRING",
                            "md": "SEBR"
                        },
                        {
                            "mk": "BRIC",
                            "search": "BRICKLIN - ",
                            "md": ""
                        },
                        {
                            "mk": "BRIS",
                            "search": "BRISTOL - ",
                            "md": ""
                        },
                        {
                            "mk": "BROD",
                            "search": "BRODEX - ",
                            "md": ""
                        },
                        {
                            "mk": "BUEL",
                            "search": "BUELL - ",
                            "md": ""
                        },
                        {
                            "mk": "BUGA",
                            "search": "BUGATTI - EB110",
                            "md": "E10"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - ALLURE",
                            "md": "ALLU"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - APOLLO",
                            "md": "APOL"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - CALIFORNIA",
                            "md": "CALI"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - CENTURION",
                            "md": "CENU"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - CENTURY",
                            "md": "CENT"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - ELECTRA (PARK AVENUE)",
                            "md": "ELEC"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - ENCLAVE",
                            "md": "ENCL"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - ENCORE",
                            "md": "ENCO"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - ESTATE WAGON",
                            "md": "ESTA"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - GRAND SPORTS (G.S.)",
                            "md": "GRAN"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - GS350",
                            "md": "G35"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - GS400",
                            "md": "G40"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - GS455",
                            "md": "G45"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - INVICTA",
                            "md": "INVI"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - LE SABRE",
                            "md": "LESA"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - LIMITED",
                            "md": "LIMI"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - PARK AVENUE",
                            "md": "PARK"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - RAINIER",
                            "md": "RAIN"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - REATTA",
                            "md": "REAT"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - REGAL",
                            "md": "REGA"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - RENDEZVOUS",
                            "md": "REND"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - RIVIERA",
                            "md": "RIVI"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - ROADMASTER",
                            "md": "ROAD"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - SKYHAWK",
                            "md": "SKYH"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - SKYLARK",
                            "md": "SKYL"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - SOMERSET",
                            "md": "SOME"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - SPECIAL",
                            "md": "SPEC"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - SPORTSWAGON",
                            "md": "SPOR"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - SUPER",
                            "md": "SUPE"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - TERRAZA",
                            "md": "TERR"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - VERANO",
                            "md": "VERA"
                        },
                        {
                            "mk": "BUIC",
                            "search": "BUICK - WILDCAT",
                            "md": "WILD"
                        },
                        {
                            "mk": "BUTT",
                            "search": "BUTTERFIELD MUSKETEER - ",
                            "md": ""
                        },
                        {
                            "mk": "CBTR",
                            "search": "C & B TRAILER - DUMP TRAILER",
                            "md": "DUTR"
                        },
                        {
                            "mk": "CBTR",
                            "search": "C & B TRAILER - FLAT TRAILER",
                            "md": "FLTR"
                        },
                        {
                            "mk": "CBTR",
                            "search": "C & B TRAILER - GOOSENECK TRAILER",
                            "md": "GOTR"
                        },
                        {
                            "mk": "CBTR",
                            "search": "C & B TRAILER - LANDSCAPE TRAILER",
                            "md": "LATR"
                        },
                        {
                            "mk": "CBTR",
                            "search": "C & B TRAILER - PINTLE PULL TRAILER",
                            "md": "PITR"
                        },
                        {
                            "mk": "CBTR",
                            "search": "C & B TRAILER - TILT TRAILER",
                            "md": "TILT"
                        },
                        {
                            "mk": "CBTR",
                            "search": "C & B TRAILER - UTILITY TRAILER",
                            "md": "UTTR"
                        },
                        {
                            "mk": "CHR",
                            "search": "C-HR - ",
                            "md": ""
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - 60 SERIES",
                            "md": "60"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - 61 SERIES",
                            "md": "61"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - 62 SERIES",
                            "md": "62"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - 75 SERIES",
                            "md": "75"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - ALLANTE",
                            "md": "ALLA"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - ATS",
                            "md": "ATS"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - BROUGHAM",
                            "md": "BROU"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - CALAIS",
                            "md": "CALA"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - CATERA",
                            "md": "CATE"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - CIMARRON",
                            "md": "CIMA"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - CONCOURS",
                            "md": "CONC"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - CTS",
                            "md": "CTS"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - DEVILLE",
                            "md": "DEVI"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - DTS",
                            "md": "DTS"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - ELDORADO",
                            "md": "ELDO"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - ESCALADE",
                            "md": "ESCA"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - ESV",
                            "md": "ESV"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - EXT",
                            "md": "EXT"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - FLEETWOOD",
                            "md": "FLEE"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - SEVILLE",
                            "md": "SEVI"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - SRX",
                            "md": "SRX"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - STS",
                            "md": "STS"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - TOURING SEDAN",
                            "md": "TOUR"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - XLR",
                            "md": "XLR"
                        },
                        {
                            "mk": "CADI",
                            "search": "CADILLAC - XT5",
                            "md": "XT5"
                        },
                        {
                            "mk": "CAM",
                            "search": "CAMPION - ",
                            "md": ""
                        },
                        {
                            "mk": "CAPR",
                            "search": "CAPRI - ",
                            "md": ""
                        },
                        {
                            "mk": "CASE",
                            "search": "CASE - ",
                            "md": ""
                        },
                        {
                            "mk": "CATE",
                            "search": "CATERPILLAR - ",
                            "md": ""
                        },
                        {
                            "mk": "CHAI",
                            "search": "CHAIKA - ",
                            "md": ""
                        },
                        {
                            "mk": "CHA",
                            "search": "CHAMPION - ",
                            "md": ""
                        },
                        {
                            "mk": "CHEC",
                            "search": "CHECKER - AEROBUS",
                            "md": "AERO"
                        },
                        {
                            "mk": "CHEC",
                            "search": "CHECKER - CUSTOM",
                            "md": "CUST"
                        },
                        {
                            "mk": "CHEC",
                            "search": "CHECKER - MARATHON",
                            "md": "MARA"
                        },
                        {
                            "mk": "CHEC",
                            "search": "CHECKER - SUPERBA",
                            "md": "SUPE"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - 300 DELUXE",
                            "md": "300"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - ASTRO VAN",
                            "md": "ASTR"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - AVALANCHE",
                            "md": "AVAL"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - AVEO",
                            "md": "AVEO"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - BEL AIR",
                            "md": "BELA"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - BERETTA",
                            "md": "BERE"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - BISCAYNE",
                            "md": "BISC"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - BLAZER",
                            "md": "BLAZ"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - BOLT",
                            "md": "BOLT"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - BROOKWOOD",
                            "md": "BROO"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - C/K 1500",
                            "md": "C15"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - C/K 2500",
                            "md": "C25"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - C/K 3500",
                            "md": "C35"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - C10",
                            "md": "C10"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - CAMARO",
                            "md": "CAMA"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - CAPRICE",
                            "md": "CAPR"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - CAPTIVA",
                            "md": "CAPT"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - CAVALIER",
                            "md": "CAVA"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - CELEBRITY",
                            "md": "CELE"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - CHEVELLE",
                            "md": "CHEV"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - CHEVETTE",
                            "md": "CHET"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - CHEVY II",
                            "md": "CHEY"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - CITATION",
                            "md": "CITA"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - CITY EXPRESS",
                            "md": "CITY"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - COBALT",
                            "md": "COBA"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - COLORADO",
                            "md": "COLO"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - CONCOURS",
                            "md": "CONC"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - CORSICA",
                            "md": "CORS"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - CORVAIR",
                            "md": "CORR"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - CORVETTE",
                            "md": "CORV"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - CRUZE",
                            "md": "CRUZ"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - DEL RAY",
                            "md": "DELR"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - DELUXE (CHEVELLE)",
                            "md": "CHED"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - EL CAMINO",
                            "md": "ELCA"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - EPICA",
                            "md": "EPIC"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - EQUINOX",
                            "md": "EQUI"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - ESTATE WAGON",
                            "md": "EST"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - EXPRESS",
                            "md": "EXP"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - FLEETLINE",
                            "md": "FLE"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - G30",
                            "md": "G30"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - GREENBRIER (CHEVELLE)",
                            "md": "CHEG"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - HHR",
                            "md": "HHR"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - IMPALA",
                            "md": "IMPA"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - KINGSWOOD",
                            "md": "KIN"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - LUMINA",
                            "md": "LUMI"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - LUMINA APV",
                            "md": "LUMA"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - LUV",
                            "md": "LUV"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - MALIBU",
                            "md": "MALI"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - METRO",
                            "md": "METR"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - MONTE CARLO",
                            "md": "MONT"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - MONZA",
                            "md": "MONZ"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - NOMAD (CHEVELLE)",
                            "md": "CHEN"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - NOVA (CHEVY II & CONCOURS)",
                            "md": "NOVA"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - OPTRA",
                            "md": "OPTR"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - OPTRA5",
                            "md": "OPT5"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - ORLANDO",
                            "md": "ORLA"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - PARKWOOD",
                            "md": "PARK"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - PRISM",
                            "md": "PRIS"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - S10",
                            "md": "S10"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - SILVERADO",
                            "md": "SILV"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - SONIC",
                            "md": "SONI"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - SPARK",
                            "md": "SPRK"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - SPECTRUM",
                            "md": "SPEC"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - SPORTVAN",
                            "md": "SPOR"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - SPRINT",
                            "md": "SPRI"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - SSR",
                            "md": "SSR"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - STYLE LINE",
                            "md": "STY"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - STYLE MASTER",
                            "md": "STM"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - SUBURBAN",
                            "md": "SUBU"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - TAHOE",
                            "md": "TAHO"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - TOWNSMAN",
                            "md": "TOWN"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - TRACKER",
                            "md": "TRAC"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - TRAILBLAZER",
                            "md": "TRAI"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - TRAVERSE",
                            "md": "TRAV"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - TRAX",
                            "md": "TRAX"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - UPLANDER",
                            "md": "UPLA"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - VEGA",
                            "md": "VEGA"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - VENTURE",
                            "md": "VENT"
                        },
                        {
                            "mk": "CHEV",
                            "search": "CHEVROLET - VOLT",
                            "md": "VOLT"
                        },
                        {
                            "mk": "CHIN",
                            "search": "CHING-KAN-SHAN - ",
                            "md": ""
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - 200",
                            "md": "200"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - 300",
                            "md": "300"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - 300C",
                            "md": "300C"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - CIRRUS",
                            "md": "CIRR"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - COMMANDER",
                            "md": "COMM"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - CONCORDE",
                            "md": "CONC"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - CONQUEST",
                            "md": "CONQ"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - CORDOBA",
                            "md": "CORD"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - CROSSFIRE",
                            "md": "CROS"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - DAYTONA",
                            "md": "DAYT"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - DYNASTY",
                            "md": "DYNA"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - E CLASS",
                            "md": "ECL"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - EXECUTIVE SEDAN",
                            "md": "EXE"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - FIFTH AVENUE",
                            "md": "NEW5"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - IMPERIAL",
                            "md": "IMPE"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - INTREPID",
                            "md": "INTR"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - LASER",
                            "md": "LASE"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - LEBARON",
                            "md": "LEBA"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - LHS",
                            "md": "LHS"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - LIDO",
                            "md": "LID"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - LIMOUSINE",
                            "md": "LIMO"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - NEON",
                            "md": "NEON"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - NEW YORKER",
                            "md": "NEWY"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - NEWPORT",
                            "md": "NEWP"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - PACIFICA",
                            "md": "PACI"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - PROWLER",
                            "md": "PROW"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - PT CRUISER",
                            "md": "PTCR"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - ROYAL",
                            "md": "ROYA"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - SALON",
                            "md": "SAL"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - SARATOGA",
                            "md": "SARA"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - SEBRING",
                            "md": "SEBR"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - TC",
                            "md": "TC"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - TOWN & COUNTRY",
                            "md": "NEWT"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - TOWN AND COUNTRY MINIVAN",
                            "md": "TNC"
                        },
                        {
                            "mk": "CHRY",
                            "search": "CHRYSLER - WINDSOR",
                            "md": "WIN"
                        },
                        {
                            "mk": "CISI",
                            "search": "CISITALIA - ",
                            "md": ""
                        },
                        {
                            "mk": "CITI",
                            "search": "CITICAR (ELECTRIC CAR) - ",
                            "md": ""
                        },
                        {
                            "mk": "CITR",
                            "search": "CITROEN - 2CV",
                            "md": "2CV"
                        },
                        {
                            "mk": "CITR",
                            "search": "CITROEN - AM16",
                            "md": "AM6"
                        },
                        {
                            "mk": "CITR",
                            "search": "CITROEN - AX",
                            "md": "AX"
                        },
                        {
                            "mk": "CITR",
                            "search": "CITROEN - DS-19",
                            "md": "D19"
                        },
                        {
                            "mk": "CITR",
                            "search": "CITROEN - DS-21 & D21",
                            "md": "D21"
                        },
                        {
                            "mk": "CITR",
                            "search": "CITROEN - ID-19",
                            "md": "ID9"
                        },
                        {
                            "mk": "CITR",
                            "search": "CITROEN - SM",
                            "md": "SM"
                        },
                        {
                            "mk": "CITY",
                            "search": "CITY EXPRESS - ",
                            "md": ""
                        },
                        {
                            "mk": "CLAI",
                            "search": "CLASSIC MOTOR CARRIAGES INC. - ",
                            "md": ""
                        },
                        {
                            "mk": "CLAC",
                            "search": "CLASSIC ROADSTERS LTD. - ",
                            "md": ""
                        },
                        {
                            "mk": "CLEN",
                            "search": "CLENET COACH WORKS - ROADSTER",
                            "md": "ROA"
                        },
                        {
                            "mk": "CLUA",
                            "search": "CLUA - ",
                            "md": ""
                        },
                        {
                            "mk": "COMV",
                            "search": "COMMUTER VEHICLES INC - COMUTA-CAR",
                            "md": "COM"
                        },
                        {
                            "mk": "COCP",
                            "search": "CONCEPTOR INDUSTRIES INC - ",
                            "md": ""
                        },
                        {
                            "mk": "CONN",
                            "search": "CONNAUGHT - ",
                            "md": ""
                        },
                        {
                            "mk": "CONS",
                            "search": "CONSULIER - ",
                            "md": ""
                        },
                        {
                            "mk": "CONT",
                            "search": "CONTESSA - ",
                            "md": ""
                        },
                        {
                            "mk": "CNTL",
                            "search": "CONTINENTAL - CARGO",
                            "md": "CARG"
                        },
                        {
                            "mk": "CORD",
                            "search": "CORD - ",
                            "md": ""
                        },
                        {
                            "mk": "CRI",
                            "search": "CRISCRAFT - ",
                            "md": ""
                        },
                        {
                            "mk": "CROF",
                            "search": "CROFTON CUB - ",
                            "md": ""
                        },
                        {
                            "mk": "CROS",
                            "search": "CROSLEY - ",
                            "md": ""
                        },
                        {
                            "mk": "CUBS",
                            "search": "CUBSTER - ",
                            "md": ""
                        },
                        {
                            "mk": "CUNN",
                            "search": "CUNNINGHAM - ",
                            "md": ""
                        },
                        {
                            "mk": "DAIN",
                            "search": "D & A VEHICLES INC. - ",
                            "md": ""
                        },
                        {
                            "mk": "DB",
                            "search": "D.B. - ",
                            "md": ""
                        },
                        {
                            "mk": "DAEW",
                            "search": "DAEWOO - LANOS",
                            "md": "LAN"
                        },
                        {
                            "mk": "DAEW",
                            "search": "DAEWOO - LEGANZA",
                            "md": "LEG"
                        },
                        {
                            "mk": "DAEW",
                            "search": "DAEWOO - NUBIRA",
                            "md": "NUB"
                        },
                        {
                            "mk": "DAF",
                            "search": "DAF - ",
                            "md": ""
                        },
                        {
                            "mk": "DAIH",
                            "search": "DAIHATSU - CHARADE",
                            "md": "CHA"
                        },
                        {
                            "mk": "DAIH",
                            "search": "DAIHATSU - ROCKY",
                            "md": "RKY"
                        },
                        {
                            "mk": "DAIM",
                            "search": "DAIMLER - ",
                            "md": ""
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - 110",
                            "md": "110"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - 1200",
                            "md": "120"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - 200SX",
                            "md": "200S"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - 210 (or B-210)",
                            "md": "210"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - 240Z",
                            "md": "240Z"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - 260Z",
                            "md": "260Z"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - 280Z",
                            "md": "280Z"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - 280ZX",
                            "md": "280X"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - 310",
                            "md": "310"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - 311",
                            "md": "311"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - 510",
                            "md": "510"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - 610",
                            "md": "610"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - 710",
                            "md": "710"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - 810",
                            "md": "810"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - B-210 (or 210)",
                            "md": "B210"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - F-10",
                            "md": "F10"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - HONEY BEE",
                            "md": "HON"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - LIL HUSTLER",
                            "md": "LIL"
                        },
                        {
                            "mk": "DATS",
                            "search": "DATSUN - MAXIMA",
                            "md": "MAXI"
                        },
                        {
                            "mk": "DAVI",
                            "search": "DAVIS - ",
                            "md": ""
                        },
                        {
                            "mk": "DAYT",
                            "search": "DAYTONA - MIGI",
                            "md": "MIG"
                        },
                        {
                            "mk": "DAYT",
                            "search": "DAYTONA - MOYA",
                            "md": "MOY"
                        },
                        {
                            "mk": "DELO",
                            "search": "DE LOREAN - ",
                            "md": ""
                        },
                        {
                            "mk": "DEBO",
                            "search": "DEBONAIR - ",
                            "md": ""
                        },
                        {
                            "mk": "DECO",
                            "search": "DECOURVILLE - ROADSTER",
                            "md": "ROA"
                        },
                        {
                            "mk": "DEEP",
                            "search": "DEEP SANDERSON - ",
                            "md": ""
                        },
                        {
                            "mk": "DELL",
                            "search": "DELLOW - ",
                            "md": ""
                        },
                        {
                            "mk": "DENZ",
                            "search": "DENZEL - ",
                            "md": ""
                        },
                        {
                            "mk": "DESO",
                            "search": "DESOTO - ADVENTURER",
                            "md": "ADV"
                        },
                        {
                            "mk": "DESO",
                            "search": "DESOTO - CUSTOM",
                            "md": "CUS"
                        },
                        {
                            "mk": "DESO",
                            "search": "DESOTO - DELUXE",
                            "md": "DEL"
                        },
                        {
                            "mk": "DESO",
                            "search": "DESOTO - FIREDOM",
                            "md": "FRD"
                        },
                        {
                            "mk": "DESO",
                            "search": "DESOTO - FIRELITE",
                            "md": "FRF"
                        },
                        {
                            "mk": "DESO",
                            "search": "DESOTO - FIRESWEEP",
                            "md": "FRS"
                        },
                        {
                            "mk": "DESO",
                            "search": "DESOTO - POWERMASTER",
                            "md": "POW"
                        },
                        {
                            "mk": "DETO",
                            "search": "DETOMASO - DEAUVILLE",
                            "md": "DEA"
                        },
                        {
                            "mk": "DETO",
                            "search": "DETOMASO - LONGCHAMP",
                            "md": "LON"
                        },
                        {
                            "mk": "DETO",
                            "search": "DETOMASO - MANGUSTA",
                            "md": "MNA"
                        },
                        {
                            "mk": "DETO",
                            "search": "DETOMASO - PANTERA",
                            "md": "PTA"
                        },
                        {
                            "mk": "DITE",
                            "search": "DI TELLA - ",
                            "md": ""
                        },
                        {
                            "mk": "DIVA",
                            "search": "DIVA - ",
                            "md": ""
                        },
                        {
                            "mk": "DKW",
                            "search": "DKW - AUDI",
                            "md": "AUD"
                        },
                        {
                            "mk": "DKW",
                            "search": "DKW - F102",
                            "md": "102"
                        },
                        {
                            "mk": "DKW",
                            "search": "DKW - VEMAG",
                            "md": "VEM"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - 2000",
                            "md": "2000"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - 330 SERIES",
                            "md": "330"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - 400 SERIES",
                            "md": "400"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - 440 SERIES",
                            "md": "440"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - 600",
                            "md": "600"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - 880 SERIES",
                            "md": "880"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - A 100 COMPACT",
                            "md": "100"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - ARIES",
                            "md": "ARIE"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - ASPEN",
                            "md": "ASPE"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - AVENGER",
                            "md": "AVEN"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - CALIBER",
                            "md": "CALI"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - CARAVAN",
                            "md": "CARA"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - CHALLENGER",
                            "md": "CHAL"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - CHARGER",
                            "md": "CHAR"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - COLT",
                            "md": "COLT"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - COMPACT SPORTSMAN",
                            "md": "COM"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - CONQUEST",
                            "md": "CONQ"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - CORONET",
                            "md": "CORO"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - DAKOTA",
                            "md": "DAKO"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - DART",
                            "md": "DART"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - DAYTONA",
                            "md": "DAYT"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - DELUXE",
                            "md": "DEL"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - DEMON",
                            "md": "DEM"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - DIPLOMAT",
                            "md": "DIPL"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - DURANGO",
                            "md": "DURA"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - DYNASTY",
                            "md": "DYNA"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - FLEET SPECIAL",
                            "md": "FLS"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - GRAND CARAVAN",
                            "md": "GRAN"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - INTREPID",
                            "md": "INTR"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - JOURNEY",
                            "md": "JOUR"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - LANCER",
                            "md": "LANC"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - MAGNUM",
                            "md": "MAGN"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - MEADOWBROOK",
                            "md": "MEAD"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - MIRADA",
                            "md": "MIRA"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - MONACO",
                            "md": "MONA"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - NEON",
                            "md": "NEON"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - NITRO",
                            "md": "NITR"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - OMNI (ALSO 024)",
                            "md": "OMNI"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - PHOENIX",
                            "md": "PHOE"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - PIONEER",
                            "md": "PION"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - POLARA",
                            "md": "POLA"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - POWER RAM",
                            "md": "PRM"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - RAIDER",
                            "md": "RAID"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - RAM 1500 PU",
                            "md": "D150"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - RAM 1500 VAN",
                            "md": "V15"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - RAM 2500 PU",
                            "md": "D250"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - RAM 2500 VAN",
                            "md": "V25"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - RAM 3500 PU",
                            "md": "D350"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - RAM 3500 VAN",
                            "md": "V35"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - RAM CHARGER",
                            "md": "RCH"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - ROYAL",
                            "md": "ROYA"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - SENECA",
                            "md": "SENE"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - SHADOW",
                            "md": "SHAD"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - SPIRIT",
                            "md": "SPIR"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - SPRINT",
                            "md": "SPRI"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - SPRINTER",
                            "md": "SPRT"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - SRT4",
                            "md": "SRT4"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - ST. REGIS",
                            "md": "STR"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - STRATUS",
                            "md": "STRA"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - SX",
                            "md": "SX"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - SX2.0",
                            "md": "SX2"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - VIPER",
                            "md": "VIPE"
                        },
                        {
                            "mk": "DODG",
                            "search": "DODGE - WAYFARER",
                            "md": "WAY"
                        },
                        {
                            "mk": "DONG",
                            "search": "DONG FENG  (EAST WIND) - ",
                            "md": ""
                        },
                        {
                            "mk": "DBL",
                            "search": "DOUBLE EAGLE - ",
                            "md": ""
                        },
                        {
                            "mk": "DUCA",
                            "search": "DUCATI - ",
                            "md": ""
                        },
                        {
                            "mk": "DUEL",
                            "search": "DUEL - ",
                            "md": ""
                        },
                        {
                            "mk": "DUES",
                            "search": "DUESENBERG - ",
                            "md": ""
                        },
                        {
                            "mk": "DURA",
                            "search": "DURANT - ",
                            "md": ""
                        },
                        {
                            "mk": "DUTC",
                            "search": "DUTCHMAN MANUFACTURING INC. - AEROLITE",
                            "md": "AERO"
                        },
                        {
                            "mk": "DUTC",
                            "search": "DUTCHMAN MANUFACTURING INC. - ASPEN TRAIL",
                            "md": "ASPE"
                        },
                        {
                            "mk": "DUTC",
                            "search": "DUTCHMAN MANUFACTURING INC. - BAYRIDGE",
                            "md": "BAYR"
                        },
                        {
                            "mk": "DUTC",
                            "search": "DUTCHMAN MANUFACTURING INC. - BRECKENRIDGE",
                            "md": "BREC"
                        },
                        {
                            "mk": "DUTC",
                            "search": "DUTCHMAN MANUFACTURING INC. - COLEMAN",
                            "md": "COLE"
                        },
                        {
                            "mk": "DUTC",
                            "search": "DUTCHMAN MANUFACTURING INC. - DENALI",
                            "md": "DENA"
                        },
                        {
                            "mk": "DUTC",
                            "search": "DUTCHMAN MANUFACTURING INC. - DUTCHMAN",
                            "md": "DUTC"
                        },
                        {
                            "mk": "DUTC",
                            "search": "DUTCHMAN MANUFACTURING INC. - INFINITY",
                            "md": "INFI"
                        },
                        {
                            "mk": "DUTC",
                            "search": "DUTCHMAN MANUFACTURING INC. - KODIAK",
                            "md": "KODI"
                        },
                        {
                            "mk": "DUTC",
                            "search": "DUTCHMAN MANUFACTURING INC. - KOMFORT",
                            "md": "KOMF"
                        },
                        {
                            "mk": "DUTC",
                            "search": "DUTCHMAN MANUFACTURING INC. - RUBICON",
                            "md": "RUBI"
                        },
                        {
                            "mk": "DUTC",
                            "search": "DUTCHMAN MANUFACTURING INC. - VOLTAGE",
                            "md": "VOLT"
                        },
                        {
                            "mk": "EAGL",
                            "search": "EAGLE - MEDALLION",
                            "md": "MEDA"
                        },
                        {
                            "mk": "EAGL",
                            "search": "EAGLE - PREMIER",
                            "md": "PRE"
                        },
                        {
                            "mk": "EAGL",
                            "search": "EAGLE - SUMMIT",
                            "md": "SUM"
                        },
                        {
                            "mk": "EAGL",
                            "search": "EAGLE - TALON",
                            "md": "TALO"
                        },
                        {
                            "mk": "EAGL",
                            "search": "EAGLE - VISION",
                            "md": "VISI"
                        },
                        {
                            "mk": "EDSE",
                            "search": "EDSEL - CITATION",
                            "md": "CITA"
                        },
                        {
                            "mk": "EDSE",
                            "search": "EDSEL - CORSAIR",
                            "md": "CORS"
                        },
                        {
                            "mk": "EDSE",
                            "search": "EDSEL - PACER",
                            "md": "PACE"
                        },
                        {
                            "mk": "EDSE",
                            "search": "EDSEL - RANGER",
                            "md": "RANG"
                        },
                        {
                            "mk": "EDSE",
                            "search": "EDSEL - VILLAGER",
                            "md": "VILL"
                        },
                        {
                            "mk": "ELVC",
                            "search": "ELECTRIC VEHICLE CORP. - ",
                            "md": ""
                        },
                        {
                            "mk": "ELVA",
                            "search": "ELVA - ",
                            "md": ""
                        },
                        {
                            "mk": "EMW",
                            "search": "EMW - ",
                            "md": ""
                        },
                        {
                            "mk": "ENGF",
                            "search": "ENGLISH FORD (BRITISH) - 100 E SERIES",
                            "md": "100"
                        },
                        {
                            "mk": "ENGF",
                            "search": "ENGLISH FORD (BRITISH) - 105 E SERIES",
                            "md": "105"
                        },
                        {
                            "mk": "ENGF",
                            "search": "ENGLISH FORD (BRITISH) - ANGLIA",
                            "md": "ANG"
                        },
                        {
                            "mk": "ENGF",
                            "search": "ENGLISH FORD (BRITISH) - CAPRI",
                            "md": "CAPR"
                        },
                        {
                            "mk": "ENGF",
                            "search": "ENGLISH FORD (BRITISH) - CONSUL",
                            "md": "CONS"
                        },
                        {
                            "mk": "ENGF",
                            "search": "ENGLISH FORD (BRITISH) - CORSAIR",
                            "md": "CORS"
                        },
                        {
                            "mk": "ENGF",
                            "search": "ENGLISH FORD (BRITISH) - CORTINA",
                            "md": "CORT"
                        },
                        {
                            "mk": "ENGF",
                            "search": "ENGLISH FORD (BRITISH) - ESCORT",
                            "md": "ESCO"
                        },
                        {
                            "mk": "ENGF",
                            "search": "ENGLISH FORD (BRITISH) - GT",
                            "md": "GT"
                        },
                        {
                            "mk": "ENGF",
                            "search": "ENGLISH FORD (BRITISH) - LOTUS",
                            "md": "LOTU"
                        },
                        {
                            "mk": "ENGF",
                            "search": "ENGLISH FORD (BRITISH) - MARK II",
                            "md": "MK2"
                        },
                        {
                            "mk": "ENGF",
                            "search": "ENGLISH FORD (BRITISH) - PERFECT",
                            "md": "PER"
                        },
                        {
                            "mk": "ENGF",
                            "search": "ENGLISH FORD (BRITISH) - SQUIRE",
                            "md": "SQU"
                        },
                        {
                            "mk": "ENGF",
                            "search": "ENGLISH FORD (BRITISH) - THAMES",
                            "md": "THA"
                        },
                        {
                            "mk": "ENGF",
                            "search": "ENGLISH FORD (BRITISH) - ZEPHYR",
                            "md": "ZEPH"
                        },
                        {
                            "mk": "ENGF",
                            "search": "ENGLISH FORD (BRITISH) - ZODIAC",
                            "md": "ZODI"
                        },
                        {
                            "mk": "ENVO",
                            "search": "ENVOY - EPIC",
                            "md": "EPI"
                        },
                        {
                            "mk": "ENZM",
                            "search": "ENZMANN - ",
                            "md": ""
                        },
                        {
                            "mk": "ERSK",
                            "search": "ERSKINE - ",
                            "md": ""
                        },
                        {
                            "mk": "ESCO",
                            "search": "ESCORT BOAT TRAILER MFG. - ",
                            "md": ""
                        },
                        {
                            "mk": "ESHL",
                            "search": "ESHELMAN SPORTABOUT - ",
                            "md": ""
                        },
                        {
                            "mk": "ESSE",
                            "search": "ESSEX - ",
                            "md": ""
                        },
                        {
                            "mk": "EVRY",
                            "search": "EVERYBODYS MOTOR CAR MFG. - ",
                            "md": ""
                        },
                        {
                            "mk": "EXCA",
                            "search": "EXCALIBUR - COBRA",
                            "md": "COBR"
                        },
                        {
                            "mk": "EXCA",
                            "search": "EXCALIBUR - JAC 427 COBRA",
                            "md": "JAC"
                        },
                        {
                            "mk": "EXCA",
                            "search": "EXCALIBUR - SS PHAETON",
                            "md": "SSP"
                        },
                        {
                            "mk": "EXCA",
                            "search": "EXCALIBUR - SS ROADSTER",
                            "md": "SSR"
                        },
                        {
                            "mk": "EXCA",
                            "search": "EXCALIBUR - SSK",
                            "md": "SSK"
                        },
                        {
                            "mk": "EZLO",
                            "search": "EZ LOADER BOAT TRAILERS INC. - ",
                            "md": ""
                        },
                        {
                            "mk": "FACE",
                            "search": "FACEL VEGA - EXCELLENCE",
                            "md": "EXE"
                        },
                        {
                            "mk": "FACE",
                            "search": "FACEL VEGA - FACEL II",
                            "md": "FII"
                        },
                        {
                            "mk": "FACE",
                            "search": "FACEL VEGA - FACEL III",
                            "md": "FIII"
                        },
                        {
                            "mk": "FACE",
                            "search": "FACEL VEGA - FACELLIA",
                            "md": "FACE"
                        },
                        {
                            "mk": "FACE",
                            "search": "FACEL VEGA - FV",
                            "md": "FV"
                        },
                        {
                            "mk": "FACE",
                            "search": "FACEL VEGA - HK500",
                            "md": "500"
                        },
                        {
                            "mk": "FAIR",
                            "search": "FAIRTHORPE - ",
                            "md": ""
                        },
                        {
                            "mk": "FALC",
                            "search": "FALCON (BRITISH) - ",
                            "md": ""
                        },
                        {
                            "mk": "FELB",
                            "search": "FELBER - ",
                            "md": ""
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - 206",
                            "md": "206"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - 208",
                            "md": "208"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - 308",
                            "md": "308"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - 328",
                            "md": "328"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - 348",
                            "md": "348"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - 456GT",
                            "md": "456"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - 458",
                            "md": "458"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - 512",
                            "md": "512"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - BARCHETTA (OR F130)",
                            "md": "BAR"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - DAYTONA",
                            "md": "DAYT"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - F-550 MARANELLO",
                            "md": "MAR"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - F12 BERLINETTA",
                            "md": "F12B"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - F355",
                            "md": "F35"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - F40",
                            "md": "F40"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - F430",
                            "md": "F430"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - MONDIAL",
                            "md": "MON"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - QUATTROVALVOLVE",
                            "md": "QUA"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - TESTAROSSA",
                            "md": "TEST"
                        },
                        {
                            "mk": "FERR",
                            "search": "FERRARI - TIPO",
                            "md": "TIP"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - 1100 - D or R",
                            "md": "110"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - 1200",
                            "md": "120"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - 124 SERIES",
                            "md": "124"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - 128 SERIES",
                            "md": "128"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - 131 SERIES",
                            "md": "131"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - 1500",
                            "md": "150"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - 500",
                            "md": "500"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - 600D",
                            "md": "600"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - 750",
                            "md": "750"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - 850 FASTBACK",
                            "md": "85F"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - BRAVA",
                            "md": "BRAV"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - PUNTO",
                            "md": "PUNT"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - RIMTO",
                            "md": "RIM"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - SPIDER SERIES",
                            "md": "SPYD"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - STRADA",
                            "md": "STRA"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - UNO",
                            "md": "UNO"
                        },
                        {
                            "mk": "FIAT",
                            "search": "FIAT - X19",
                            "md": "X19"
                        },
                        {
                            "mk": "FIAA",
                            "search": "FIAT-ABARTH - ",
                            "md": ""
                        },
                        {
                            "mk": "FIBE",
                            "search": "FIBERFAB INC. (MINNEAPOLIS MN) - ",
                            "md": ""
                        },
                        {
                            "mk": "FIES",
                            "search": "FIESTA (IMPORTED BY FORD) - ",
                            "md": ""
                        },
                        {
                            "mk": "FISK",
                            "search": "FISKER - KARMA",
                            "md": "KARM"
                        },
                        {
                            "mk": "FLEE",
                            "search": "FLEETWOOD ENTERPRISES INC - TERRY",
                            "md": "TERR"
                        },
                        {
                            "mk": "FLYE",
                            "search": "FLYER - BUS",
                            "md": "BUS"
                        },
                        {
                            "mk": "FNM",
                            "search": "FNM - ",
                            "md": ""
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - 300 SERIES",
                            "md": "300"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - 7 LITRE",
                            "md": "7LR"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - AEROSTAR",
                            "md": "AERO"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - ASPIRE",
                            "md": "ASPI"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - BRONCO/BRONCO II",
                            "md": "BRON"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - C-MAX",
                            "md": "CMAX"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - CLUB WAGON E150",
                            "md": "CW1"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - CLUB WAGON E250",
                            "md": "CW2"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - CLUB WAGON E350",
                            "md": "CW3"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - COBRA",
                            "md": "COBR"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - CONTOUR",
                            "md": "CONT"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - COUNTRY SEDAN",
                            "md": "COY"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - COUNTRY SQUIRE",
                            "md": "COQ"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - CRESTLINE",
                            "md": "CRE"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - CUSTOM",
                            "md": "CUS"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - CUSTOMLINE",
                            "md": "CST"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - DELUXE",
                            "md": "DEL"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - ECONOLINE 100",
                            "md": "E100"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - ECONOLINE E150",
                            "md": "E150"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - ECONOLINE E250",
                            "md": "E250"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - ECONOLINE E350",
                            "md": "E350"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - ECONOLINE SERIES",
                            "md": "ECON"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - EDGE",
                            "md": "EDGE"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - ELITE",
                            "md": "ELIT"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - ESCAPE",
                            "md": "ESCA"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - ESCORT",
                            "md": "ESCO"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - EXCURSION",
                            "md": "EXCU"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - EXP",
                            "md": "EXP"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - EXPEDITION",
                            "md": "EXPE"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - EXPLORER",
                            "md": "EXPL"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - F-150XLT",
                            "md": "F150"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - F100",
                            "md": "F100"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - F250 SUPERCAB (TRUCK)",
                            "md": "F250"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - F350",
                            "md": "F350"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - F450",
                            "md": "F450"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - F550",
                            "md": "F550"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - FAIRLANE",
                            "md": "FAIL"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - FAIRMONT",
                            "md": "FAIR"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - FALCON",
                            "md": "FALC"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - FESTIVA",
                            "md": "FEST"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - FIESTA",
                            "md": "FIES"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - FIVE HUNDRED",
                            "md": "FIVE"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - FLEX",
                            "md": "FLEX"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - FOCUS",
                            "md": "FOCU"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - FREESTAR",
                            "md": "FREE"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - FREESTYLE",
                            "md": "FRES"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - FRONTENAC",
                            "md": "FRO"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - FUSION",
                            "md": "FUSI"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - FUTURA",
                            "md": "FUTU"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - GALAXIE",
                            "md": "GALA"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - GRANADA",
                            "md": "GRAN"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - GRAND MARQUIS",
                            "md": "GRA"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - KA",
                            "md": "KA"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - LARIAT",
                            "md": "LARI"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - LASER",
                            "md": "LASE"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - LTD",
                            "md": "LTD"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - LTD II",
                            "md": "LTII"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - MAINLINE",
                            "md": "MAIN"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - MAVERICK",
                            "md": "MAVE"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - MODEL A",
                            "md": "MOA"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - MODEL T",
                            "md": "MOT"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - MUSTANG",
                            "md": "MUST"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - NEVADA",
                            "md": "NEVA"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - PINTO",
                            "md": "PINT"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - PROBE",
                            "md": "PROB"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - RANCH",
                            "md": "RAH"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - RANCH WAGON",
                            "md": "RAW"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - RANCHERO",
                            "md": "RANC"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - RANGER",
                            "md": "RANG"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - SPECIAL",
                            "md": "SPE"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - SQUIRE (FALCON OR FAIRLANE)",
                            "md": "SQU"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - STARLINER",
                            "md": "STA"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - SUNLINER",
                            "md": "SUN"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - SUPER",
                            "md": "SUP"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - TAURUS",
                            "md": "TAUR"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - TEMPO",
                            "md": "TEMP"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - THUNDERBIRD",
                            "md": "THUN"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - TORINO (FAIRLANE)",
                            "md": "TORI"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - TRANSIT",
                            "md": "TRAN"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - VICTORIA",
                            "md": "CROW"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - WINDSTAR",
                            "md": "WIND"
                        },
                        {
                            "mk": "FORD",
                            "search": "FORD - XL",
                            "md": "XL"
                        },
                        {
                            "mk": "FOUN",
                            "search": "FOUNTAIN - ",
                            "md": ""
                        },
                        {
                            "mk": "FRAN",
                            "search": "FRANKLIN - ",
                            "md": ""
                        },
                        {
                            "mk": "FRNA",
                            "search": "FRAZER-NASH - ",
                            "md": ""
                        },
                        {
                            "mk": "FRAZ",
                            "search": "FRAZIER - ",
                            "md": ""
                        },
                        {
                            "mk": "FREI",
                            "search": "FREIGHTLINER - ",
                            "md": ""
                        },
                        {
                            "mk": "FREF",
                            "search": "FRENCH FORD - COMETE",
                            "md": "COM"
                        },
                        {
                            "mk": "FREF",
                            "search": "FRENCH FORD - VEDETTE",
                            "md": "VED"
                        },
                        {
                            "mk": "FREF",
                            "search": "FRENCH FORD - VENDOME",
                            "md": "VEN"
                        },
                        {
                            "mk": "FRIS",
                            "search": "FRISKY - ",
                            "md": ""
                        },
                        {
                            "mk": "GAZ",
                            "search": "GAZ - CHAIKA",
                            "md": "CHA"
                        },
                        {
                            "mk": "GAZ",
                            "search": "GAZ - VOLGA",
                            "md": "VOL"
                        },
                        {
                            "mk": "GZL",
                            "search": "GAZELLE - ",
                            "md": ""
                        },
                        {
                            "mk": "GM",
                            "search": "GENERAL MOTORS - EV1",
                            "md": "EV1"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - 3500HD",
                            "md": "3500"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - ACADIA",
                            "md": "ACAD"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - CABELLERO",
                            "md": "CAB"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - CANYON",
                            "md": "CANY"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - DENALI",
                            "md": "DEN"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - ENVOY",
                            "md": "ENVO"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - JIMMY",
                            "md": "JIMM"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - RALLY",
                            "md": "RALL"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - SAFARI",
                            "md": "SAFA"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - SAVANNA",
                            "md": "SAVA"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - SIERRA",
                            "md": "SIER"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - SONOMA",
                            "md": "SONO"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - SPRINT",
                            "md": "SPRI"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - SUBURBAN",
                            "md": "SUBU"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - TERRAIN",
                            "md": "TERR"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - TRACKER",
                            "md": "TRAC"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - TYPHOON",
                            "md": "TYP"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - VANDURA",
                            "md": "VAND"
                        },
                        {
                            "mk": "GMC",
                            "search": "GENERAL MOTORS CORP. - YUKON",
                            "md": "YUKO"
                        },
                        {
                            "mk": "GENE",
                            "search": "GENESIS - G70",
                            "md": "G70"
                        },
                        {
                            "mk": "GENE",
                            "search": "GENESIS - G80",
                            "md": "G80"
                        },
                        {
                            "mk": "GENE",
                            "search": "GENESIS - G80 Sport",
                            "md": "G80S"
                        },
                        {
                            "mk": "GENE",
                            "search": "GENESIS - G90",
                            "md": "G90"
                        },
                        {
                            "mk": "GEO",
                            "search": "GEO - METRO",
                            "md": "METR"
                        },
                        {
                            "mk": "GEO",
                            "search": "GEO - PRIZM",
                            "md": "PRIZ"
                        },
                        {
                            "mk": "GEO",
                            "search": "GEO - STORM",
                            "md": "STRO"
                        },
                        {
                            "mk": "GEO",
                            "search": "GEO - TRACKER",
                            "md": "TRAC"
                        },
                        {
                            "mk": "GIAN",
                            "search": "GIANNINI - ",
                            "md": ""
                        },
                        {
                            "mk": "GILB",
                            "search": "GILBERN - ",
                            "md": ""
                        },
                        {
                            "mk": "GINE",
                            "search": "GINETTA - ",
                            "md": ""
                        },
                        {
                            "mk": "GITA",
                            "search": "GITANE - ",
                            "md": ""
                        },
                        {
                            "mk": "GLAS",
                            "search": "GLAS - GOGGOMOBILE",
                            "md": "GOG"
                        },
                        {
                            "mk": "GLSC",
                            "search": "GLASSIC - ",
                            "md": ""
                        },
                        {
                            "mk": "GOLI",
                            "search": "GOLIATH - ",
                            "md": ""
                        },
                        {
                            "mk": "GORD",
                            "search": "GORDON - ",
                            "md": ""
                        },
                        {
                            "mk": "GRAC",
                            "search": "GRACIELA - ",
                            "md": ""
                        },
                        {
                            "mk": "GRAH",
                            "search": "GRAHAM - ",
                            "md": ""
                        },
                        {
                            "mk": "GRAP",
                            "search": "GRAHAM-PAIGE - ",
                            "md": ""
                        },
                        {
                            "mk": "GDNE",
                            "search": "GREAT DANE - DRY VAN",
                            "md": "DV"
                        },
                        {
                            "mk": "GDNE",
                            "search": "GREAT DANE - FLATBED",
                            "md": "FLBD"
                        },
                        {
                            "mk": "GDNE",
                            "search": "GREAT DANE - REEFER VAN",
                            "md": "RFRV"
                        },
                        {
                            "mk": "GRIF",
                            "search": "GRIFFITH - ",
                            "md": ""
                        },
                        {
                            "mk": "GSM",
                            "search": "GSM - ",
                            "md": ""
                        },
                        {
                            "mk": "HAN",
                            "search": "HANS CHRISTIAN - ",
                            "md": ""
                        },
                        {
                            "mk": "HAR",
                            "search": "HARBORCRAFT - ",
                            "md": ""
                        },
                        {
                            "mk": "HARL",
                            "search": "HARLEY DAVIDSON - ",
                            "md": ""
                        },
                        {
                            "mk": "HARM",
                            "search": "HARMON TANK CO. INC. - ",
                            "md": ""
                        },
                        {
                            "mk": "HAUL",
                            "search": "HAULMARK - ",
                            "md": ""
                        },
                        {
                            "mk": "HEIN",
                            "search": "HEINKEL - ",
                            "md": ""
                        },
                        {
                            "mk": "HENR",
                            "search": "HENRY J. - ",
                            "md": ""
                        },
                        {
                            "mk": "HICK",
                            "search": "HICKEY TRAIL-BLAZER - ",
                            "md": ""
                        },
                        {
                            "mk": "HIGH",
                            "search": "HIGHLINER - ",
                            "md": ""
                        },
                        {
                            "mk": "HILL",
                            "search": "HILLMAN - 1600 SERIES",
                            "md": "160"
                        },
                        {
                            "mk": "HILL",
                            "search": "HILLMAN - DELUXE",
                            "md": "DEL"
                        },
                        {
                            "mk": "HILL",
                            "search": "HILLMAN - HUSKY",
                            "md": "HUS"
                        },
                        {
                            "mk": "HILL",
                            "search": "HILLMAN - IMP",
                            "md": "IMP"
                        },
                        {
                            "mk": "HILL",
                            "search": "HILLMAN - MINX",
                            "md": "MIN"
                        },
                        {
                            "mk": "HILL",
                            "search": "HILLMAN - SCEPTRE",
                            "md": "SCP"
                        },
                        {
                            "mk": "HILL",
                            "search": "HILLMAN - SNIPE",
                            "md": "SNI"
                        },
                        {
                            "mk": "HILL",
                            "search": "HILLMAN - SUPER MINX",
                            "md": "SUP"
                        },
                        {
                            "mk": "HIND",
                            "search": "HINDUSTAN - ",
                            "md": ""
                        },
                        {
                            "mk": "HINO",
                            "search": "HINO - ",
                            "md": ""
                        },
                        {
                            "mk": "HOB",
                            "search": "HOBIE CAT - ",
                            "md": ""
                        },
                        {
                            "mk": "HOLD",
                            "search": "HOLDEN - ",
                            "md": ""
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - ACCORD",
                            "md": "ACCO"
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - CIVIC (AND CRX)",
                            "md": "CIVI"
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - CR-Z",
                            "md": "CR-Z"
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - CROSSTOUR",
                            "md": "CROS"
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - CRV",
                            "md": "CRV"
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - DEL SOL",
                            "md": "DELS"
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - ELEMENT",
                            "md": "ELEM"
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - EVPLUS",
                            "md": "EVP"
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - FIT",
                            "md": "FIT"
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - HR-V",
                            "md": "HRV"
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - INSIGHT",
                            "md": "INSI"
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - ODYSSEY",
                            "md": "ODYS"
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - PASSPORT",
                            "md": "PASS"
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - PILOT",
                            "md": "PILO"
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - PRELUDE",
                            "md": "PREL"
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - RIDGELINE",
                            "md": "RIDG"
                        },
                        {
                            "mk": "HOND",
                            "search": "HONDA - S2000",
                            "md": "S200"
                        },
                        {
                            "mk": "HONG",
                            "search": "HONGKI OR HONG-CHI - ",
                            "md": ""
                        },
                        {
                            "mk": "HORC",
                            "search": "HORCH LIMOUSINE - ",
                            "md": ""
                        },
                        {
                            "mk": "HOTC",
                            "search": "HOTCHKISS - ",
                            "md": ""
                        },
                        {
                            "mk": "HRG",
                            "search": "HRG - ",
                            "md": ""
                        },
                        {
                            "mk": "HUDS",
                            "search": "HUDSON - COMMODORE",
                            "md": "COM"
                        },
                        {
                            "mk": "HUDS",
                            "search": "HUDSON - DELUXE",
                            "md": "DEL"
                        },
                        {
                            "mk": "HUDS",
                            "search": "HUDSON - HORNET",
                            "md": "HOR"
                        },
                        {
                            "mk": "HUDS",
                            "search": "HUDSON - ITALIA",
                            "md": "ITA"
                        },
                        {
                            "mk": "HUDS",
                            "search": "HUDSON - JET",
                            "md": "JET"
                        },
                        {
                            "mk": "HUDS",
                            "search": "HUDSON - PACEMAKER",
                            "md": "PAC"
                        },
                        {
                            "mk": "HUDS",
                            "search": "HUDSON - RAMBLER",
                            "md": "RAM"
                        },
                        {
                            "mk": "HUDS",
                            "search": "HUDSON - SUPER",
                            "md": "SUP"
                        },
                        {
                            "mk": "HUDS",
                            "search": "HUDSON - WASP",
                            "md": "WAS"
                        },
                        {
                            "mk": "HUME",
                            "search": "HUMBEE SURREY - ",
                            "md": ""
                        },
                        {
                            "mk": "HUMB",
                            "search": "HUMBER - HAWK",
                            "md": "HAW"
                        },
                        {
                            "mk": "HUMB",
                            "search": "HUMBER - SNIPE",
                            "md": "SNI"
                        },
                        {
                            "mk": "HUMM",
                            "search": "HUMMER - H1",
                            "md": "H1"
                        },
                        {
                            "mk": "HUMM",
                            "search": "HUMMER - H2",
                            "md": "H2"
                        },
                        {
                            "mk": "HUMM",
                            "search": "HUMMER - H2 SUT",
                            "md": "H2SU"
                        },
                        {
                            "mk": "HUMM",
                            "search": "HUMMER - H3",
                            "md": "H3"
                        },
                        {
                            "mk": "HUPM",
                            "search": "HUPMOBILE - ",
                            "md": ""
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - ACCENT",
                            "md": "ACCE"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - AVATAR",
                            "md": "AVAT"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - AZERA",
                            "md": "AZER"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - ELANTRA",
                            "md": "ELAN"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - ENTOURAGE",
                            "md": "ENTO"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - EXCEL",
                            "md": "EXCE"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - GENESIS",
                            "md": "GENE"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - IONIQ",
                            "md": "ION"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - KONA",
                            "md": "KONA"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - MARCIA",
                            "md": "MAR"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - NIRO",
                            "md": "NIRO"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - PONY",
                            "md": "PONY"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - SANTA FE",
                            "md": "SANT"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - SCOUPE",
                            "md": "SCOU"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - SONATA",
                            "md": "SONA"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - STELLAR",
                            "md": "STEL"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - TIBURON",
                            "md": "TIBU"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - TUCSON",
                            "md": "TUCS"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - VELOSTER",
                            "md": "VELO"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - XG300",
                            "md": "XG30"
                        },
                        {
                            "mk": "HYUN",
                            "search": "HYUNDAI - XG350",
                            "md": "XG35"
                        },
                        {
                            "mk": "IAME",
                            "search": "I.A.M.E. - ",
                            "md": ""
                        },
                        {
                            "mk": "IKA",
                            "search": "I.K.A. - ",
                            "md": ""
                        },
                        {
                            "mk": "IMPB",
                            "search": "I.M.P. (U.S.) - ",
                            "md": ""
                        },
                        {
                            "mk": "IMPE",
                            "search": "IMPERIAL - CROWN",
                            "md": "CROW"
                        },
                        {
                            "mk": "IMPE",
                            "search": "IMPERIAL - CUSTOM",
                            "md": "CUS"
                        },
                        {
                            "mk": "IMPE",
                            "search": "IMPERIAL - LE BARON",
                            "md": "LEBA"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - EX35",
                            "md": "EX35"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - FX35",
                            "md": "FX35"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - FX45",
                            "md": "FX45"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - FX50",
                            "md": "FX50"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - G20",
                            "md": "G20"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - G35",
                            "md": "G35"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - G37",
                            "md": "G37"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - G37X",
                            "md": "G37X"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - I30",
                            "md": "I30"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - I35",
                            "md": "I35"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - J30",
                            "md": "J30"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - M30",
                            "md": "M30"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - M35",
                            "md": "M35"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - M45",
                            "md": "M45"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - Q45",
                            "md": "Q45"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - Q50",
                            "md": "Q50"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - Q60",
                            "md": "Q60"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - Q70L",
                            "md": "Q70L"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - QX4",
                            "md": "QX4"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - QX50",
                            "md": "QX50"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - QX56",
                            "md": "QX56"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - QX60",
                            "md": "QX60"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - QX80",
                            "md": "QX80"
                        },
                        {
                            "mk": "INFI",
                            "search": "INFINITI - XQ80",
                            "md": "XQ80"
                        },
                        {
                            "mk": "INNO",
                            "search": "INNOCENTI - ",
                            "md": ""
                        },
                        {
                            "mk": "INME",
                            "search": "INTERMECCANICA - ",
                            "md": ""
                        },
                        {
                            "mk": "INTE",
                            "search": "INTERNATIONAL - 1652sc",
                            "md": "1652"
                        },
                        {
                            "mk": "INTE",
                            "search": "INTERNATIONAL - 3200",
                            "md": "3200"
                        },
                        {
                            "mk": "INTE",
                            "search": "INTERNATIONAL - 3800",
                            "md": "3800"
                        },
                        {
                            "mk": "INTE",
                            "search": "INTERNATIONAL - 4200",
                            "md": "4200"
                        },
                        {
                            "mk": "INTE",
                            "search": "INTERNATIONAL - 4300",
                            "md": "4300"
                        },
                        {
                            "mk": "INTE",
                            "search": "INTERNATIONAL - 4400",
                            "md": "4400"
                        },
                        {
                            "mk": "INTE",
                            "search": "INTERNATIONAL - 7300",
                            "md": "7300"
                        },
                        {
                            "mk": "INTE",
                            "search": "INTERNATIONAL - 7400",
                            "md": "7400"
                        },
                        {
                            "mk": "INTE",
                            "search": "INTERNATIONAL - 8500",
                            "md": "8500"
                        },
                        {
                            "mk": "INTE",
                            "search": "INTERNATIONAL - 8600",
                            "md": "8600"
                        },
                        {
                            "mk": "INTE",
                            "search": "INTERNATIONAL - 9200i",
                            "md": "9200"
                        },
                        {
                            "mk": "INTE",
                            "search": "INTERNATIONAL - 9400i",
                            "md": "9400"
                        },
                        {
                            "mk": "INTE",
                            "search": "INTERNATIONAL - 9900i",
                            "md": "9900"
                        },
                        {
                            "mk": "INTE",
                            "search": "INTERNATIONAL - 9900ix",
                            "md": "9999"
                        },
                        {
                            "mk": "ISET",
                            "search": "ISETTA - ",
                            "md": ""
                        },
                        {
                            "mk": "ISO",
                            "search": "ISO - ",
                            "md": ""
                        },
                        {
                            "mk": "ISUZ",
                            "search": "ISUZU - AMIGO",
                            "md": "AMG"
                        },
                        {
                            "mk": "ISUZ",
                            "search": "ISUZU - HOMBRE",
                            "md": "HOM"
                        },
                        {
                            "mk": "ISUZ",
                            "search": "ISUZU - I-MARK",
                            "md": "IMA"
                        },
                        {
                            "mk": "ISUZ",
                            "search": "ISUZU - IMPULSE",
                            "md": "IMPU"
                        },
                        {
                            "mk": "ISUZ",
                            "search": "ISUZU - OASIS",
                            "md": "OAS"
                        },
                        {
                            "mk": "ISUZ",
                            "search": "ISUZU - RODEO",
                            "md": "RODE"
                        },
                        {
                            "mk": "ISUZ",
                            "search": "ISUZU - STYLUS",
                            "md": "STYL"
                        },
                        {
                            "mk": "ISUZ",
                            "search": "ISUZU - TROOPER",
                            "md": "TROO"
                        },
                        {
                            "mk": "ISUZ",
                            "search": "ISUZU - VEHICROSS",
                            "md": "VCS"
                        },
                        {
                            "mk": "ITAI",
                            "search": "ITALIA - ",
                            "md": ""
                        },
                        {
                            "mk": "ITAF",
                            "search": "ITALIAN FORD - ANGLIA",
                            "md": "ANG"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - 2.4 LITRE",
                            "md": "24L"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - 3.4 LITRE",
                            "md": "34L"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - 3.8 LITRE",
                            "md": "38L"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - 340",
                            "md": "340"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - 4.2 LITRE",
                            "md": "42L"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - 420",
                            "md": "420"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - E-PAC",
                            "md": "EPAC"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - E-TYPE",
                            "md": "ETY"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - F-PAC",
                            "md": "FPAC"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - F-TYPE",
                            "md": "FTYP"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - I-PAC",
                            "md": "IPAC"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - MARK TEN SALON",
                            "md": "MTS"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - MARK V SERIES",
                            "md": "MAR"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - S-TYPE",
                            "md": "STYP"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - SOVEREIGN",
                            "md": "SOV"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - V12",
                            "md": "V12"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - VANDEN PLAS",
                            "md": "VAN"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - XE",
                            "md": "XE"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - XF",
                            "md": "XF"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - XJ",
                            "md": "XJ"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - XJ12",
                            "md": "J12"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - XJ40",
                            "md": "XJ4"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - XJ6",
                            "md": "XJ6"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - XJ8",
                            "md": "XJ8"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - XJC",
                            "md": "XJC"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - XJR",
                            "md": "XJR"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - XJS",
                            "md": "XJS"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - XK SERIES",
                            "md": "XK"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - XK-E SERIES",
                            "md": "XKE"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - XK8",
                            "md": "XK8"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - XTYPE",
                            "md": "XTYP"
                        },
                        {
                            "mk": "JAGU",
                            "search": "JAGUAR - XVLR",
                            "md": "XVLR"
                        },
                        {
                            "mk": "JEEP",
                            "search": "JEEP - CHEROKEE/GRAND CHEROKEE",
                            "md": "CHER"
                        },
                        {
                            "mk": "JEEP",
                            "search": "JEEP - CJ",
                            "md": "CJ"
                        },
                        {
                            "mk": "JEEP",
                            "search": "JEEP - COMANCHE",
                            "md": "COMA"
                        },
                        {
                            "mk": "JEEP",
                            "search": "JEEP - COMMANDER",
                            "md": "COMM"
                        },
                        {
                            "mk": "JEEP",
                            "search": "JEEP - COMPASS",
                            "md": "COMP"
                        },
                        {
                            "mk": "JEEP",
                            "search": "JEEP - DAKAR",
                            "md": "DAKA"
                        },
                        {
                            "mk": "JEEP",
                            "search": "JEEP - GLADIATOR",
                            "md": "GLAD"
                        },
                        {
                            "mk": "JEEP",
                            "search": "JEEP - J-10",
                            "md": "J10"
                        },
                        {
                            "mk": "JEEP",
                            "search": "JEEP - LIBERTY",
                            "md": "LIBE"
                        },
                        {
                            "mk": "JEEP",
                            "search": "JEEP - PATRIOT",
                            "md": "PATR"
                        },
                        {
                            "mk": "JEEP",
                            "search": "JEEP - RENEGADE",
                            "md": "RENE"
                        },
                        {
                            "mk": "JEEP",
                            "search": "JEEP - TJ",
                            "md": "TJ"
                        },
                        {
                            "mk": "JEEP",
                            "search": "JEEP - WAGONEER",
                            "md": "WAGO"
                        },
                        {
                            "mk": "JEEP",
                            "search": "JEEP - WRANGLER",
                            "md": "WRAN"
                        },
                        {
                            "mk": "JEEP",
                            "search": "JEEP - YJ",
                            "md": "YJ"
                        },
                        {
                            "mk": "JENS",
                            "search": "JENSEN - HEALY",
                            "md": "HEAL"
                        },
                        {
                            "mk": "JENS",
                            "search": "JENSEN - INTERCEPTOR",
                            "md": "INTE"
                        },
                        {
                            "mk": "JETM",
                            "search": "JETMOBILE - ",
                            "md": ""
                        },
                        {
                            "mk": "JOHN",
                            "search": "JOHN DEERE - ",
                            "md": ""
                        },
                        {
                            "mk": "JOWE",
                            "search": "JOWETT - ",
                            "md": ""
                        },
                        {
                            "mk": "KLIN",
                            "search": "K-LINE - ",
                            "md": ""
                        },
                        {
                            "mk": "KAIS",
                            "search": "KAISER - CAROLINA",
                            "md": "CARO"
                        },
                        {
                            "mk": "KAIS",
                            "search": "KAISER - DARRIN",
                            "md": "DAR"
                        },
                        {
                            "mk": "KAIS",
                            "search": "KAISER - DELUXE",
                            "md": "DEL"
                        },
                        {
                            "mk": "KAIS",
                            "search": "KAISER - DRAGON",
                            "md": "DRA"
                        },
                        {
                            "mk": "KAIS",
                            "search": "KAISER - MANHATTAN",
                            "md": "MAN"
                        },
                        {
                            "mk": "KAWA",
                            "search": "KAWASAKI - ",
                            "md": ""
                        },
                        {
                            "mk": "KENW",
                            "search": "KENWORTH - ",
                            "md": ""
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - AMANTI",
                            "md": "AMAN"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - AVELLA",
                            "md": "AVE"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - CADENZA",
                            "md": "CAD"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - FORTE",
                            "md": "FORT"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - K900",
                            "md": "K900"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - MAGENTIS",
                            "md": "MAGE"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - MATIZ",
                            "md": "MATI"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - NIRO",
                            "md": "NIRO"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - OPTIMA",
                            "md": "OPT"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - RIO",
                            "md": "RIO"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - RIO5",
                            "md": "RIO5"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - RONDO",
                            "md": "ROND"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - SEDONA",
                            "md": "SEDO"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - SEPHIA",
                            "md": "SEPH"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - SORENTO",
                            "md": "SORE"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - SOUL",
                            "md": "SOUL"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - SPECTRA",
                            "md": "SPEC"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - SPORTAGE",
                            "md": "SPOR"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - STINGER",
                            "md": "STIN"
                        },
                        {
                            "mk": "KIA",
                            "search": "KIA MOTORS CORPORATION - TELLURIDE",
                            "md": "TELL"
                        },
                        {
                            "mk": "KIMI",
                            "search": "KING MIDGET - ",
                            "md": ""
                        },
                        {
                            "mk": "KIOT",
                            "search": "KIOTI - CK",
                            "md": "CK"
                        },
                        {
                            "mk": "KIOT",
                            "search": "KIOTI - DK",
                            "md": "DK"
                        },
                        {
                            "mk": "KNIG",
                            "search": "KNIGHT - ",
                            "md": ""
                        },
                        {
                            "mk": "KUBO",
                            "search": "KUBOTA - B",
                            "md": "B"
                        },
                        {
                            "mk": "KUBO",
                            "search": "KUBOTA - BX",
                            "md": "BX"
                        },
                        {
                            "mk": "KUBO",
                            "search": "KUBOTA - L",
                            "md": "L"
                        },
                        {
                            "mk": "KUBO",
                            "search": "KUBOTA - M",
                            "md": "M"
                        },
                        {
                            "mk": "KUBO",
                            "search": "KUBOTA - RTV",
                            "md": "RTV"
                        },
                        {
                            "mk": "KUBO",
                            "search": "KUBOTA - TLB",
                            "md": "TLB"
                        },
                        {
                            "mk": "KURT",
                            "search": "KURTIS KRAFT - ",
                            "md": ""
                        },
                        {
                            "mk": "LADA",
                            "search": "LADA - NIVA",
                            "md": "NIV"
                        },
                        {
                            "mk": "LAGO",
                            "search": "LAGONDA - ",
                            "md": ""
                        },
                        {
                            "mk": "LAMO",
                            "search": "LAMBORGHINI - COUNTACH",
                            "md": "COUN"
                        },
                        {
                            "mk": "LAMO",
                            "search": "LAMBORGHINI - DIABLO",
                            "md": "DIAB"
                        },
                        {
                            "mk": "LAMO",
                            "search": "LAMBORGHINI - ESPADA",
                            "md": "ESP"
                        },
                        {
                            "mk": "LAMO",
                            "search": "LAMBORGHINI - GALLARDO",
                            "md": "GALL"
                        },
                        {
                            "mk": "LAMO",
                            "search": "LAMBORGHINI - HURACAN",
                            "md": "HURA"
                        },
                        {
                            "mk": "LAMO",
                            "search": "LAMBORGHINI - JALPA",
                            "md": "JAL"
                        },
                        {
                            "mk": "LAMO",
                            "search": "LAMBORGHINI - JARMA",
                            "md": "JAR"
                        },
                        {
                            "mk": "LAMO",
                            "search": "LAMBORGHINI - LM129",
                            "md": "129"
                        },
                        {
                            "mk": "LAMO",
                            "search": "LAMBORGHINI - MIURA SV",
                            "md": "MIU"
                        },
                        {
                            "mk": "LAMO",
                            "search": "LAMBORGHINI - ROADSTER",
                            "md": "ROD"
                        },
                        {
                            "mk": "LAMB",
                            "search": "LAMBRETTA - ",
                            "md": ""
                        },
                        {
                            "mk": "LANC",
                            "search": "LANCHESTER - ",
                            "md": ""
                        },
                        {
                            "mk": "LNCI",
                            "search": "LANCIA - BERLINA",
                            "md": "BER"
                        },
                        {
                            "mk": "LNCI",
                            "search": "LANCIA - BETA SERIES",
                            "md": "BET"
                        },
                        {
                            "mk": "LNCI",
                            "search": "LANCIA - DEDRA",
                            "md": "DED"
                        },
                        {
                            "mk": "LNCI",
                            "search": "LANCIA - FLAMINIA",
                            "md": "FLM"
                        },
                        {
                            "mk": "LNCI",
                            "search": "LANCIA - FLAVIA",
                            "md": "FLA"
                        },
                        {
                            "mk": "LNCI",
                            "search": "LANCIA - FULVIA",
                            "md": "FUL"
                        },
                        {
                            "mk": "LNCI",
                            "search": "LANCIA - ZAGATO",
                            "md": "ZAG"
                        },
                        {
                            "mk": "LAND",
                            "search": "LAND ROVER - DEFENDER 110",
                            "md": "D110"
                        },
                        {
                            "mk": "LAND",
                            "search": "LAND ROVER - DEFENDER 90",
                            "md": "D90"
                        },
                        {
                            "mk": "LAND",
                            "search": "LAND ROVER - DEFENDER SERIES",
                            "md": "DEFE"
                        },
                        {
                            "mk": "LAND",
                            "search": "LAND ROVER - FREELANDER",
                            "md": "FREE"
                        },
                        {
                            "mk": "LAND",
                            "search": "LAND ROVER - HSE",
                            "md": "HSE"
                        },
                        {
                            "mk": "LAND",
                            "search": "LAND ROVER - LR2",
                            "md": "LR2"
                        },
                        {
                            "mk": "LAND",
                            "search": "LAND ROVER - LR3",
                            "md": "LR3"
                        },
                        {
                            "mk": "LAND",
                            "search": "LAND ROVER - LR4",
                            "md": "LR4"
                        },
                        {
                            "mk": "LAND",
                            "search": "LAND ROVER - RANGE ROVER",
                            "md": "RANG"
                        },
                        {
                            "mk": "LAND",
                            "search": "LAND ROVER - RANGE ROVER DISCOVERY",
                            "md": "DISC"
                        },
                        {
                            "mk": "LAND",
                            "search": "LAND ROVER - RANGE ROVER DISCOVERY SPORT",
                            "md": "DISS"
                        },
                        {
                            "mk": "LAND",
                            "search": "LAND ROVER - RANGE ROVER EVOQUE",
                            "md": "EVOQ"
                        },
                        {
                            "mk": "LAND",
                            "search": "LAND ROVER - RANGE ROVER SPORT",
                            "md": "SPOR"
                        },
                        {
                            "mk": "LAND",
                            "search": "LAND ROVER - RANGE ROVER VELAR",
                            "md": "VELR"
                        },
                        {
                            "mk": "LALL",
                            "search": "LASALLE - ",
                            "md": ""
                        },
                        {
                            "mk": "LASE",
                            "search": "LASER - ",
                            "md": ""
                        },
                        {
                            "mk": "LEAF",
                            "search": "LEA-FRANCIS - ",
                            "md": ""
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - CT200H",
                            "md": "CT20"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - ES250",
                            "md": "250"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - ES300",
                            "md": "300"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - ES330",
                            "md": "ES33"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - ES350",
                            "md": "350"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - GS300",
                            "md": "GS3"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - GS350",
                            "md": "GS35"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - GS400",
                            "md": "GS4"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - GS430",
                            "md": "GS43"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - GS450",
                            "md": "GS45"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - GSF",
                            "md": "GSF"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - GX460",
                            "md": "GX46"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - GX470",
                            "md": "GX47"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - IS200T",
                            "md": "IS20"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - IS250",
                            "md": "IS25"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - IS300",
                            "md": "IS30"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - IS350",
                            "md": "IS35"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - ISF",
                            "md": "ISF"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - LS400",
                            "md": "400"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - LS430",
                            "md": "LS43"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - LS460",
                            "md": "LS46"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - LS460L",
                            "md": "LS4L"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - LS600HL",
                            "md": "LS60"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - LX450",
                            "md": "L45"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - LX470",
                            "md": "L47"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - LX570",
                            "md": "L57"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - NX",
                            "md": "NX"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - NX300",
                            "md": "NX30"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - RC300",
                            "md": "RC30"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - RC350",
                            "md": "RC35"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - RCF",
                            "md": "RCF"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - RX300",
                            "md": "RX3"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - RX330",
                            "md": "RX33"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - RX350",
                            "md": "RX35"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - RX400H",
                            "md": "RX40"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - RX450H",
                            "md": "RX45"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - SC300",
                            "md": "S30"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - SC400",
                            "md": "S40"
                        },
                        {
                            "mk": "LEXU",
                            "search": "LEXUS - SC430",
                            "md": "SC43"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - AVIATOR",
                            "md": "AVIA"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - CONTINENTAL",
                            "md": "CONT"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - CUSTOM",
                            "md": "CUS"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - LS",
                            "md": "LS"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - LS6",
                            "md": "LS6"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - LS8",
                            "md": "LS8"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - MARK II",
                            "md": "MII"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - MARK III",
                            "md": "MIII"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - MARK IV",
                            "md": "MIV"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - MARK SERIES",
                            "md": "MARK"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - MARK V",
                            "md": "MV"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - MARK VI",
                            "md": "MVI"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - MARK VII",
                            "md": "MVII"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - MARK VIII",
                            "md": "VIII"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - MKC",
                            "md": "MKC"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - MKT",
                            "md": "MKT"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - MKX",
                            "md": "MKX"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - MKZ",
                            "md": "MKZ"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - NAUTILUS",
                            "md": "NAUT"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - NAVIGATOR",
                            "md": "NAVI"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - PREMIERE",
                            "md": "PRE"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - STANDARD",
                            "md": "STAN"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - TOWN CAR",
                            "md": "TOWN"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - VERSAILLES",
                            "md": "VER"
                        },
                        {
                            "mk": "LINC",
                            "search": "LINCOLN-CONTINENTAL - ZEPHYR",
                            "md": "ZEP"
                        },
                        {
                            "mk": "LLOY",
                            "search": "LLOYD - ",
                            "md": ""
                        },
                        {
                            "mk": "LDTR",
                            "search": "LOAD TRAIL - DK",
                            "md": "DK"
                        },
                        {
                            "mk": "LOCO",
                            "search": "LOCOMOBILE - ",
                            "md": ""
                        },
                        {
                            "mk": "LOLA",
                            "search": "LOLA - ",
                            "md": ""
                        },
                        {
                            "mk": "LOND",
                            "search": "LONDON MOTORS - ",
                            "md": ""
                        },
                        {
                            "mk": "LONE",
                            "search": "LONESTAR - ",
                            "md": ""
                        },
                        {
                            "mk": "LOOD",
                            "search": "LOODCRAFT - ",
                            "md": ""
                        },
                        {
                            "mk": "LOTU",
                            "search": "LOTUS - ECLAT",
                            "md": "ECL"
                        },
                        {
                            "mk": "LOTU",
                            "search": "LOTUS - ELAN",
                            "md": "ELA"
                        },
                        {
                            "mk": "LOTU",
                            "search": "LOTUS - ELITE",
                            "md": "ELI"
                        },
                        {
                            "mk": "LOTU",
                            "search": "LOTUS - ESPRIT",
                            "md": "ESPI"
                        },
                        {
                            "mk": "LOTU",
                            "search": "LOTUS - EUROPA",
                            "md": "EUR"
                        },
                        {
                            "mk": "LOTU",
                            "search": "LOTUS - PLUS TWO",
                            "md": "PLU"
                        },
                        {
                            "mk": "LOTU",
                            "search": "LOTUS - SUPER 7",
                            "md": "SUP"
                        },
                        {
                            "mk": "MBM",
                            "search": "M.B.M. - ",
                            "md": ""
                        },
                        {
                            "mk": "MACK",
                            "search": "MACK - ",
                            "md": ""
                        },
                        {
                            "mk": "MAL",
                            "search": "MALIBU - ",
                            "md": ""
                        },
                        {
                            "mk": "MANA",
                            "search": "MANAC - ",
                            "md": ""
                        },
                        {
                            "mk": "MARC",
                            "search": "MARCOS - ",
                            "md": ""
                        },
                        {
                            "mk": "MARM",
                            "search": "MARMON - ",
                            "md": ""
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - 2000 SERIES",
                            "md": "200"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - 228",
                            "md": "228"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - 3500 SERIES",
                            "md": "350"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - 4000 SERIES",
                            "md": "400"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - 4200 GT",
                            "md": "420"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - 425",
                            "md": "425"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - 430",
                            "md": "430"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - 5000 SERIES",
                            "md": "500"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - BITURBO",
                            "md": "BIT"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - BORA",
                            "md": "BOR"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - GHIBLI",
                            "md": "GHI"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - GTI SERIES",
                            "md": "GTI"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - INDY",
                            "md": "IND"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - KHAMSIN",
                            "md": "KHA"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - MERAK",
                            "md": "MER"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - MEXICO",
                            "md": "MEX"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - MISTRELL",
                            "md": "MIS"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - QUATTROPORTE",
                            "md": "QUA"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - SEBRING",
                            "md": "SEB"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - SHAMAL",
                            "md": "SHM"
                        },
                        {
                            "mk": "MASE",
                            "search": "MASERATI - SPYDER",
                            "md": "SPY"
                        },
                        {
                            "mk": "MASS",
                            "search": "MASSEY FERGUSON - 1500",
                            "md": "1500"
                        },
                        {
                            "mk": "MASS",
                            "search": "MASSEY FERGUSON - 3400",
                            "md": "3400"
                        },
                        {
                            "mk": "MASS",
                            "search": "MASSEY FERGUSON - 3600",
                            "md": "3600"
                        },
                        {
                            "mk": "MASS",
                            "search": "MASSEY FERGUSON - 500",
                            "md": "500"
                        },
                        {
                            "mk": "MASS",
                            "search": "MASSEY FERGUSON - 5400",
                            "md": "5400"
                        },
                        {
                            "mk": "MASS",
                            "search": "MASSEY FERGUSON - 6400",
                            "md": "6400"
                        },
                        {
                            "mk": "MASS",
                            "search": "MASSEY FERGUSON - 7400",
                            "md": "7400"
                        },
                        {
                            "mk": "MASS",
                            "search": "MASSEY FERGUSON - 8400",
                            "md": "8400"
                        },
                        {
                            "mk": "MASS",
                            "search": "MASSEY FERGUSON - GC",
                            "md": "GC"
                        },
                        {
                            "mk": "MASS",
                            "search": "MASSEY FERGUSON - SUNFLOWER",
                            "md": "SUNF"
                        },
                        {
                            "mk": "MAS",
                            "search": "MASTERCRAFT - ",
                            "md": ""
                        },
                        {
                            "mk": "MATR",
                            "search": "MATRA - ",
                            "md": ""
                        },
                        {
                            "mk": "MAXL",
                            "search": "MAXWELL - ",
                            "md": ""
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - 2",
                            "md": "2"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - 3",
                            "md": "3"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - 323",
                            "md": "323"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - 5",
                            "md": "5"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - 6",
                            "md": "6"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - 616",
                            "md": "616"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - 618",
                            "md": "618"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - 626",
                            "md": "626"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - 808 SERIES",
                            "md": "808"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - 929",
                            "md": "929"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - B2000",
                            "md": "B200"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - B2200",
                            "md": "B220"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - B2300",
                            "md": "B230"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - B2500",
                            "md": "B250"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - B2600",
                            "md": "B260"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - B3000",
                            "md": "B300"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - B4000",
                            "md": "B400"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - COSMO",
                            "md": "CSM"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - CX-3",
                            "md": "CX3"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - CX-5",
                            "md": "CX5"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - CX-7",
                            "md": "CX7"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - CX-9",
                            "md": "CX9"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - FAMILIA",
                            "md": "PRO"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - GLC",
                            "md": "GLC"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - M6",
                            "md": "M6"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - MIATA",
                            "md": "MIAT"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - MILLENIA",
                            "md": "MILE"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - MISER",
                            "md": "MISE"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - MPV",
                            "md": "MPV"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - MX3",
                            "md": "MX3"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - MX5",
                            "md": "MX5"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - MX6",
                            "md": "MX6"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - NAVAJO",
                            "md": "NAVA"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - PROTEGE",
                            "md": "PROT"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - RX2 (ROTARY ENGINE)",
                            "md": "RX2"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - RX3 (ROTARY ENGINE)",
                            "md": "RX3"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - RX4 (ROTARY ENGINE)",
                            "md": "RX4"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - RX7 (ROTARY ENGINE)",
                            "md": "RX7"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - RX8",
                            "md": "RX8"
                        },
                        {
                            "mk": "MAZD",
                            "search": "MAZDA - TRIBUTE",
                            "md": "TRIB"
                        },
                        {
                            "mk": "MBCC",
                            "search": "MCBURNIE COACH CRAFT INC. - ",
                            "md": ""
                        },
                        {
                            "mk": "MCLA",
                            "search": "MCLAREN - MP4",
                            "md": "MP4"
                        },
                        {
                            "mk": "MEAN",
                            "search": "MEAN - ",
                            "md": ""
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 180 SERIES",
                            "md": "180"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 190 SERIES",
                            "md": "190"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 200 SERIES",
                            "md": "200"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 219 SERIES",
                            "md": "219"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 220 SERIES",
                            "md": "220"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 230 SERIES",
                            "md": "230"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 240 SERIES",
                            "md": "240"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 250 SERIES",
                            "md": "250"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 260 SERIES",
                            "md": "260"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 280 SERIES",
                            "md": "280"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 300 SERIES",
                            "md": "300"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 320 SERIES",
                            "md": "320"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 350 SERIES",
                            "md": "350"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 380 SERIES",
                            "md": "380"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 400 SERIES",
                            "md": "400"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 420 SERIES",
                            "md": "420"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 450 SERIES",
                            "md": "450"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 500 SERIES",
                            "md": "500"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 560 SERIES",
                            "md": "560"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - 600 SERIES",
                            "md": "600"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - B200",
                            "md": "B200"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - B250",
                            "md": "B250"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - C220",
                            "md": "C220"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - C230",
                            "md": "C230"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - C240",
                            "md": "C240"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - C250",
                            "md": "C250"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - C280",
                            "md": "C280"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - C300",
                            "md": "C300"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - C320",
                            "md": "C320"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - C350",
                            "md": "C350"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - C36",
                            "md": "C36"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - C400",
                            "md": "C400"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - C55",
                            "md": "C55"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - C63",
                            "md": "C63"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - CL500",
                            "md": "CL50"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - CL55",
                            "md": "CL55"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - CL600",
                            "md": "CL60"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - CL65",
                            "md": "CL65"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - CLA250",
                            "md": "CLA2"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - CLA45",
                            "md": "CLA4"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - CLK32",
                            "md": "CK32"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - CLK320",
                            "md": "CLK3"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - CLK35",
                            "md": "CK35"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - CLK430",
                            "md": "CL4"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - CLK50",
                            "md": "CK50"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - CLK500",
                            "md": "CLK5"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - CLK55",
                            "md": "CK55"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - CLS500",
                            "md": "CLS5"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - CLS55",
                            "md": "CS55"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - CLS63",
                            "md": "CLS6"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - E300",
                            "md": "E300"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - E320",
                            "md": "E320"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - E320W",
                            "md": "320W"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - E350",
                            "md": "E350"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - E400",
                            "md": "E400"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - E420",
                            "md": "E420"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - E43",
                            "md": "E43"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - E430",
                            "md": "E430"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - E500",
                            "md": "E500"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - E55",
                            "md": "E55"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - E63",
                            "md": "E63"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - G500",
                            "md": "G500"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - G55",
                            "md": "G55"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - G550",
                            "md": "G550"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - G63",
                            "md": "G63"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - G65",
                            "md": "G65"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - GL350",
                            "md": "GL35"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - GLA",
                            "md": "GLA"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - GLC30",
                            "md": "GL30"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - GLC43",
                            "md": "GL43"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - GLE35",
                            "md": "GLE3"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - GLE350",
                            "md": "G350"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - GLE400",
                            "md": "G400"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - GLE45",
                            "md": "GLE4"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - GLK250",
                            "md": "GLK2"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - GLK35",
                            "md": "G35"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - GLK350",
                            "md": "GLK3"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - GLK450",
                            "md": "G450"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - GLS550",
                            "md": "GLS5"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - METRIS",
                            "md": "METR"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - ML320 (SPORT UTILITY)",
                            "md": "ML3"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - ML350",
                            "md": "ML35"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - ML430",
                            "md": "ML4"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - ML500",
                            "md": "ML50"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - ML63",
                            "md": "ML63"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - R350",
                            "md": "R350"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - S430",
                            "md": "S430"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - S450",
                            "md": "S450"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - S500",
                            "md": "S500"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - S55",
                            "md": "S55"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - S550V",
                            "md": "S550"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - S600",
                            "md": "S600"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - SL",
                            "md": "SL"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - SL500",
                            "md": "SL5"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - SL600",
                            "md": "SL6"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - SL65",
                            "md": "SL65"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - SLK3",
                            "md": "SLK3"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - SLK5",
                            "md": "SLK5"
                        },
                        {
                            "mk": "MERZ",
                            "search": "MERCEDES-BENZ - SPRINTER",
                            "md": "SPRI"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - BOBCAT",
                            "md": "BOBC"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - BREEZEWAY",
                            "md": "BREE"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - BROUGHAM",
                            "md": "BROU"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - CALIENTE",
                            "md": "CLI"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - CAPRI",
                            "md": "CAPR"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - COLONY PARK",
                            "md": "COL"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - COMET",
                            "md": "COME"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - COMMUTER",
                            "md": "CMM"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - COUGAR",
                            "md": "COUG"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - COUNTRY CRUISER",
                            "md": "CCR"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - CUSTOM",
                            "md": "CUS"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - CYCLONE",
                            "md": "CYC"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - GRAND MARQUIS",
                            "md": "GRAN"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - LN7",
                            "md": "LN7"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - LYNX",
                            "md": "LYNX"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - MARAUDER",
                            "md": "MARA"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - MARINER",
                            "md": "MARI"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - MARQUIS",
                            "md": "MARQ"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - MEDALIST",
                            "md": "MED"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - MONARCH",
                            "md": "MONA"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - MONTCLAIR",
                            "md": "MOT"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - MONTEGO",
                            "md": "MONT"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - MONTEREY",
                            "md": "MONY"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - MOUNTAINEER",
                            "md": "MTN"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - MYSTIQUE",
                            "md": "MYST"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - PARKLANE",
                            "md": "PARK"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - S-22",
                            "md": "S22"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - S-33",
                            "md": "S33"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - S-55",
                            "md": "S55"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - SABLE",
                            "md": "SABL"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - TOPAZ",
                            "md": "TOPA"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - TRACER",
                            "md": "TRAC"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - TURNPIKE CRUISER",
                            "md": "TUR"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - VILLAGER",
                            "md": "VILL"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - VOYAGER",
                            "md": "VOYA"
                        },
                        {
                            "mk": "MERC",
                            "search": "MERCURY - ZEPHYR",
                            "md": "ZEP"
                        },
                        {
                            "mk": "MERK",
                            "search": "MERKUR - SCORPIO",
                            "md": "SCOR"
                        },
                        {
                            "mk": "MERK",
                            "search": "MERKUR - XR4Ti",
                            "md": "XR4"
                        },
                        {
                            "mk": "MESS",
                            "search": "MESSERSCHMITT - KR200",
                            "md": "KR"
                        },
                        {
                            "mk": "MESS",
                            "search": "MESSERSCHMITT - KR201",
                            "md": "KR1"
                        },
                        {
                            "mk": "MESS",
                            "search": "MESSERSCHMITT - TIGER",
                            "md": "TIG"
                        },
                        {
                            "mk": "METE",
                            "search": "METEOR (CANADIAN MERCURY) - COUNTRY SEDAN",
                            "md": "COY"
                        },
                        {
                            "mk": "METE",
                            "search": "METEOR (CANADIAN MERCURY) - LEMOYNE",
                            "md": "LEM"
                        },
                        {
                            "mk": "METE",
                            "search": "METEOR (CANADIAN MERCURY) - MONTCALM",
                            "md": "MON"
                        },
                        {
                            "mk": "METE",
                            "search": "METEOR (CANADIAN MERCURY) - MONTEGO",
                            "md": "MGO"
                        },
                        {
                            "mk": "METE",
                            "search": "METEOR (CANADIAN MERCURY) - NIAGARA",
                            "md": "NIA"
                        },
                        {
                            "mk": "METE",
                            "search": "METEOR (CANADIAN MERCURY) - RANCH WAGON",
                            "md": "RAW"
                        },
                        {
                            "mk": "METE",
                            "search": "METEOR (CANADIAN MERCURY) - RIDEAU",
                            "md": "RID"
                        },
                        {
                            "mk": "METE",
                            "search": "METEOR (CANADIAN MERCURY) - S-33",
                            "md": "S33"
                        },
                        {
                            "mk": "METR",
                            "search": "METROPOLITAN - ",
                            "md": ""
                        },
                        {
                            "mk": "MG",
                            "search": "MG - 1100",
                            "md": "MG1"
                        },
                        {
                            "mk": "MG",
                            "search": "MG - 1600",
                            "md": "1600"
                        },
                        {
                            "mk": "MG",
                            "search": "MG - MAGNETTE",
                            "md": "MAGN"
                        },
                        {
                            "mk": "MG",
                            "search": "MG - MARINA",
                            "md": "MARI"
                        },
                        {
                            "mk": "MG",
                            "search": "MG - MARK II",
                            "md": "MARK"
                        },
                        {
                            "mk": "MG",
                            "search": "MG - MGA",
                            "md": "MGA"
                        },
                        {
                            "mk": "MG",
                            "search": "MG - MGB",
                            "md": "MGB"
                        },
                        {
                            "mk": "MG",
                            "search": "MG - MGB/GT",
                            "md": "MGG"
                        },
                        {
                            "mk": "MG",
                            "search": "MG - MGC",
                            "md": "MGC"
                        },
                        {
                            "mk": "MG",
                            "search": "MG - MGC/GT",
                            "md": "MGT"
                        },
                        {
                            "mk": "MG",
                            "search": "MG - MIDGET",
                            "md": "MIDG"
                        },
                        {
                            "mk": "MG",
                            "search": "MG - PRINCESS 4-R",
                            "md": "4R"
                        },
                        {
                            "mk": "MG",
                            "search": "MG - SPORTS SEDAN",
                            "md": "SPS"
                        },
                        {
                            "mk": "MG",
                            "search": "MG - SPRITE",
                            "md": "SPRI"
                        },
                        {
                            "mk": "MG",
                            "search": "MG - TF SERIES",
                            "md": "TF"
                        },
                        {
                            "mk": "MIKA",
                            "search": "MIKASA - ",
                            "md": ""
                        },
                        {
                            "mk": "MIKR",
                            "search": "MIKRUS - ",
                            "md": ""
                        },
                        {
                            "mk": "MINI",
                            "search": "MINI - COOPER",
                            "md": "COOP"
                        },
                        {
                            "mk": "MIST",
                            "search": "MISTRAL - ",
                            "md": ""
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - 3000 GT",
                            "md": "3GT"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - CHARIOT",
                            "md": "CHAR"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - CORDIA",
                            "md": "CORD"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - DELICA",
                            "md": "DELI"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - DIAMANTE",
                            "md": "DIAM"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - ECLIPSE",
                            "md": "ECLI"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - ECLIPSE SPYDER GS-T",
                            "md": "ECL"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - ENDEAVOR",
                            "md": "ENDE"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - EXPO",
                            "md": "EXPO"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - GALANT",
                            "md": "GALA"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - LANCER",
                            "md": "LANC"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - MIGHTY MAX",
                            "md": "MTX"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - MINICA",
                            "md": "MIN"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - MIRAGE",
                            "md": "MIRA"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - MONTERO/MONTERO SPORT",
                            "md": "MONT"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - OUTLANDER",
                            "md": "OUTL"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - PRECIS",
                            "md": "PRE"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - RVR",
                            "md": "RVR"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - SIGMA",
                            "md": "SIG"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - SPYDER 3000 GT",
                            "md": "SPYD"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - STARION",
                            "md": "STA"
                        },
                        {
                            "mk": "MITS",
                            "search": "MITSUBISHI - TREDIA",
                            "md": "TRE"
                        },
                        {
                            "mk": "MODE",
                            "search": "MODEL A & MODEL T MOTOR CAR REPRODUCTION CORP. - GT250",
                            "md": "250"
                        },
                        {
                            "mk": "MODE",
                            "search": "MODEL A & MODEL T MOTOR CAR REPRODUCTION CORP. - MODEL A",
                            "md": "MOD"
                        },
                        {
                            "mk": "MODE",
                            "search": "MODEL A & MODEL T MOTOR CAR REPRODUCTION CORP. - THUNDERBIRD",
                            "md": "THUN"
                        },
                        {
                            "mk": "MONA",
                            "search": "MONARCH - LUCERNE",
                            "md": "LUC"
                        },
                        {
                            "mk": "MONA",
                            "search": "MONARCH - RICHELIEU",
                            "md": "RIC"
                        },
                        {
                            "mk": "MONA",
                            "search": "MONARCH - SCEPTRE",
                            "md": "SCP"
                        },
                        {
                            "mk": "MONK",
                            "search": "MONK - ",
                            "md": ""
                        },
                        {
                            "mk": "MORE",
                            "search": "MORETTI - ",
                            "md": ""
                        },
                        {
                            "mk": "MORG",
                            "search": "MORGAN - 4/4 MARK 5",
                            "md": "MK5"
                        },
                        {
                            "mk": "MORG",
                            "search": "MORGAN - PLUS 4 SERIES",
                            "md": "PL4"
                        },
                        {
                            "mk": "MORR",
                            "search": "MORRIS - 1100",
                            "md": "110"
                        },
                        {
                            "mk": "MORR",
                            "search": "MORRIS - 850 SERIES",
                            "md": "850"
                        },
                        {
                            "mk": "MORR",
                            "search": "MORRIS - DELUXE",
                            "md": "DEL"
                        },
                        {
                            "mk": "MORR",
                            "search": "MORRIS - MINI SERIES",
                            "md": "MII"
                        },
                        {
                            "mk": "MORR",
                            "search": "MORRIS - MINOR",
                            "md": "MIN"
                        },
                        {
                            "mk": "MORR",
                            "search": "MORRIS - OXFORD",
                            "md": "OXF"
                        },
                        {
                            "mk": "MORR",
                            "search": "MORRIS - TRAVELLER",
                            "md": "TRV"
                        },
                        {
                            "mk": "MOSK",
                            "search": "MOSKOVITCH - ",
                            "md": ""
                        },
                        {
                            "mk": "MOTO",
                            "search": "MOTO GUZZI - V7",
                            "md": "V7"
                        },
                        {
                            "mk": "MOTO",
                            "search": "MOTO GUZZI - V9",
                            "md": "V9"
                        },
                        {
                            "mk": "MCI",
                            "search": "MOTOR COACH INDUSTRIES - ",
                            "md": ""
                        },
                        {
                            "mk": "MUNT",
                            "search": "MUNTZ - JET",
                            "md": "JET"
                        },
                        {
                            "mk": "MURE",
                            "search": "MURENA - ",
                            "md": ""
                        },
                        {
                            "mk": "MZMA",
                            "search": "MZMA - ",
                            "md": ""
                        },
                        {
                            "mk": "NAHA",
                            "search": "NAHANNI MANUFACTURING LTD - ",
                            "md": ""
                        },
                        {
                            "mk": "NARD",
                            "search": "NARDI-DANESE - ",
                            "md": ""
                        },
                        {
                            "mk": "NASH",
                            "search": "NASH - AMBASSADOR",
                            "md": "AMB"
                        },
                        {
                            "mk": "NASH",
                            "search": "NASH - LAYFAYETTE",
                            "md": "LAF"
                        },
                        {
                            "mk": "NASH",
                            "search": "NASH - METROPOLITAN",
                            "md": "MET"
                        },
                        {
                            "mk": "NASH",
                            "search": "NASH - RAMBLER",
                            "md": "RAM"
                        },
                        {
                            "mk": "NASH",
                            "search": "NASH - STATESMAN",
                            "md": "STA"
                        },
                        {
                            "mk": "NAHE",
                            "search": "NASH-HEALY - ",
                            "md": ""
                        },
                        {
                            "mk": "NECK",
                            "search": "NECKAR - ",
                            "md": ""
                        },
                        {
                            "mk": "NEFL",
                            "search": "NEW FLYER - BUS",
                            "md": "BUS"
                        },
                        {
                            "mk": "NEWM",
                            "search": "NEWMAR - BAY STAR",
                            "md": "BAYS"
                        },
                        {
                            "mk": "NEWM",
                            "search": "NEWMAR - CANYON STAR",
                            "md": "CANY"
                        },
                        {
                            "mk": "NEWM",
                            "search": "NEWMAR - DUTCH STAR",
                            "md": "DUTC"
                        },
                        {
                            "mk": "NEWM",
                            "search": "NEWMAR - ESSEX",
                            "md": "ESSE"
                        },
                        {
                            "mk": "NEWM",
                            "search": "NEWMAR - KING AIRE",
                            "md": "KING"
                        },
                        {
                            "mk": "NEWM",
                            "search": "NEWMAR - MOUNTAIN AIRE",
                            "md": "MOUN"
                        },
                        {
                            "mk": "NEWM",
                            "search": "NEWMAR - VENTANA",
                            "md": "VENT"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - 200SX",
                            "md": "200S"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - 240SX",
                            "md": "240S"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - 300ZX",
                            "md": "300Z"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - 350Z",
                            "md": "350Z"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - 370Z",
                            "md": "370Z"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - ALTIMA",
                            "md": "ALTI"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - ARMADA",
                            "md": "ARMA"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - AXXESS",
                            "md": "AXXE"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - CUBE",
                            "md": "CUBE"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - FRONTIER",
                            "md": "FRON"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - GT-R",
                            "md": "GT-R"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - JUKE",
                            "md": "JUKE"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - KICKS",
                            "md": "KICK"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - LEAF",
                            "md": "LEAF"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - MAXIMA",
                            "md": "MAXI"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - MICRA",
                            "md": "MICR"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - MURANO",
                            "md": "MURA"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - NAVARA",
                            "md": "NAVA"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - NP300",
                            "md": "NP30"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - NV200",
                            "md": "NV20"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - NX",
                            "md": "NX"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - PATHFINDER",
                            "md": "PATH"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - PULSAR",
                            "md": "PULS"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - QASHQAI",
                            "md": "QASH"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - QUEST",
                            "md": "QUES"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - ROGUE",
                            "md": "ROGU"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - SE-V6",
                            "md": "SE"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - SENTRA",
                            "md": "SENT"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - SKYLINE",
                            "md": "SKYL"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - SP&SP",
                            "md": "SPSP"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - STANZA",
                            "md": "STAN"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - TERRANO II",
                            "md": "TERR"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - TITAN",
                            "md": "TITA"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - VERSA",
                            "md": "VERS"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - XE",
                            "md": "XE"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - XTERRA",
                            "md": "XTER"
                        },
                        {
                            "mk": "NISS",
                            "search": "NISSAN - XTRAIL",
                            "md": "XTRA"
                        },
                        {
                            "mk": "NORT",
                            "search": "NORTHWOOD MANUFACTURING - ARCTIC FOX",
                            "md": "ARCT"
                        },
                        {
                            "mk": "NOVA",
                            "search": "NOVABUS - HEV",
                            "md": "HEV"
                        },
                        {
                            "mk": "NSU",
                            "search": "NSU PRINZ - 1000",
                            "md": "100"
                        },
                        {
                            "mk": "NSU",
                            "search": "NSU PRINZ - 110 TYPE",
                            "md": "110"
                        },
                        {
                            "mk": "NSU",
                            "search": "NSU PRINZ - AUTO NOVA",
                            "md": "AVA"
                        },
                        {
                            "mk": "NSU",
                            "search": "NSU PRINZ - PRINZ",
                            "md": "PRIN"
                        },
                        {
                            "mk": "NSU",
                            "search": "NSU PRINZ - SPIDER (WANKEL)",
                            "md": "SPI"
                        },
                        {
                            "mk": "NSUF",
                            "search": "NSU-FIAT - ",
                            "md": ""
                        },
                        {
                            "mk": "OAKL",
                            "search": "OAKLAND - ",
                            "md": ""
                        },
                        {
                            "mk": "OGLE",
                            "search": "OGLE - ",
                            "md": ""
                        },
                        {
                            "mk": "OHTA",
                            "search": "OHTA - ",
                            "md": ""
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - 442",
                            "md": "442"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - 88",
                            "md": "88"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - 98",
                            "md": "98"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - ACHIEVA",
                            "md": "ACHI"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - ALERO",
                            "md": "ALER"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - AURORA",
                            "md": "AURO"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - BRAVADA",
                            "md": "BRAV"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - CALAIS",
                            "md": "CALA"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - CARAVAN",
                            "md": "CARA"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - CUSTOM",
                            "md": "CUS"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - CUSTOM CRUISER",
                            "md": "CCR"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - CUTLASS",
                            "md": "CUTL"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - CUTLASS SUPREME",
                            "md": "CUTS"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - DELMONT 88",
                            "md": "DLM"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - DELTA 88",
                            "md": "DELT"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - DELUXE",
                            "md": "DEL"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - DYNAMIC 88",
                            "md": "DYN"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - F-85",
                            "md": "F85"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - FIRENZA",
                            "md": "FIRE"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - HOLIDAY",
                            "md": "HOLI"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - INTRIGUE",
                            "md": "INTR"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - JETFIRE",
                            "md": "JTF"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - JETSTAR",
                            "md": "JTS"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - LSS",
                            "md": "DLT"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - OMEGA",
                            "md": "OMEG"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - REGENCY (NINETY-EIGHT SERIES)",
                            "md": "REG"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - ROYALE",
                            "md": "ROYA"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - SILHOUETTE",
                            "md": "SIL"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - STANDARD",
                            "md": "STD"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - STARFIRE",
                            "md": "STA"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - SUPER 88",
                            "md": "SUP"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - TORONADO",
                            "md": "TORO"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - TROFEO",
                            "md": "TRO"
                        },
                        {
                            "mk": "OLDS",
                            "search": "OLDSMOBILE - VISTA CRUISER",
                            "md": "VIS"
                        },
                        {
                            "mk": "OMEG",
                            "search": "OMEGA (ITALIAN) - ",
                            "md": ""
                        },
                        {
                            "mk": "OPEL",
                            "search": "OPEL - 1900",
                            "md": "190"
                        },
                        {
                            "mk": "OPEL",
                            "search": "OPEL - ASTRA",
                            "md": "ASTR"
                        },
                        {
                            "mk": "OPEL",
                            "search": "OPEL - CARAVAN",
                            "md": "CARA"
                        },
                        {
                            "mk": "OPEL",
                            "search": "OPEL - DIPLOMAT",
                            "md": "DIPL"
                        },
                        {
                            "mk": "OPEL",
                            "search": "OPEL - GT",
                            "md": "GT"
                        },
                        {
                            "mk": "OPEL",
                            "search": "OPEL - KADETTE",
                            "md": "KAD"
                        },
                        {
                            "mk": "OPEL",
                            "search": "OPEL - KAPITAN",
                            "md": "KAP"
                        },
                        {
                            "mk": "OPEL",
                            "search": "OPEL - LUXUS",
                            "md": "LUX"
                        },
                        {
                            "mk": "OPEL",
                            "search": "OPEL - MANTA",
                            "md": "MAN"
                        },
                        {
                            "mk": "OPEL",
                            "search": "OPEL - OLYMPIA",
                            "md": "OLY"
                        },
                        {
                            "mk": "OPEL",
                            "search": "OPEL - RALLYE",
                            "md": "RAL"
                        },
                        {
                            "mk": "OPEL",
                            "search": "OPEL - REKORD",
                            "md": "REK"
                        },
                        {
                            "mk": "OPER",
                            "search": "OPEN ROADSTERS OF TEXAS - ",
                            "md": ""
                        },
                        {
                            "mk": "ORIO",
                            "search": "ORION BUS INDUSTRIES - ",
                            "md": ""
                        },
                        {
                            "mk": "OSCA",
                            "search": "OSCA - ",
                            "md": ""
                        },
                        {
                            "mk": "OSI",
                            "search": "OSI - ",
                            "md": ""
                        },
                        {
                            "mk": "OTOS",
                            "search": "OTOSAN - ",
                            "md": ""
                        },
                        {
                            "mk": "OVER",
                            "search": "OVERLAND - ",
                            "md": ""
                        },
                        {
                            "mk": "PACK",
                            "search": "PACKARD - BALBOA",
                            "md": "BAL"
                        },
                        {
                            "mk": "PACK",
                            "search": "PACKARD - CARIBBEAN",
                            "md": "CAR"
                        },
                        {
                            "mk": "PACK",
                            "search": "PACKARD - CAVALIER",
                            "md": "CAVA"
                        },
                        {
                            "mk": "PACK",
                            "search": "PACKARD - CLIPPER",
                            "md": "CLI"
                        },
                        {
                            "mk": "PACK",
                            "search": "PACKARD - PATRICIAN",
                            "md": "PAT"
                        },
                        {
                            "mk": "PACK",
                            "search": "PACKARD - PREDICTOR",
                            "md": "PRD"
                        },
                        {
                            "mk": "PACK",
                            "search": "PACKARD - REQUEST",
                            "md": "REQ"
                        },
                        {
                            "mk": "PALL",
                            "search": "PALLISER (RACING CAR) - ",
                            "md": ""
                        },
                        {
                            "mk": "PANH",
                            "search": "PANHARD - ",
                            "md": ""
                        },
                        {
                            "mk": "PANZ",
                            "search": "PANOZ AUTO DEVELOPMENT - ROADSTER",
                            "md": "ROD"
                        },
                        {
                            "mk": "PANE",
                            "search": "PANTHER WESTWINDS LTD. - DEVILLE",
                            "md": "DEVI"
                        },
                        {
                            "mk": "PANE",
                            "search": "PANTHER WESTWINDS LTD. - J72",
                            "md": "J72"
                        },
                        {
                            "mk": "PANE",
                            "search": "PANTHER WESTWINDS LTD. - KILLETA",
                            "md": "KAL"
                        },
                        {
                            "mk": "PANE",
                            "search": "PANTHER WESTWINDS LTD. - LIMA",
                            "md": "LIM"
                        },
                        {
                            "mk": "PASS",
                            "search": "PASSPORT - OPTIMA",
                            "md": "OPTI"
                        },
                        {
                            "mk": "PEAC",
                            "search": "PEACE - ",
                            "md": ""
                        },
                        {
                            "mk": "PEEL",
                            "search": "PEEL - ",
                            "md": ""
                        },
                        {
                            "mk": "PEER",
                            "search": "PEERLESS - ",
                            "md": ""
                        },
                        {
                            "mk": "PEGA",
                            "search": "PEGASO - ",
                            "md": ""
                        },
                        {
                            "mk": "PETE",
                            "search": "PETERBILT - ",
                            "md": ""
                        },
                        {
                            "mk": "PEUG",
                            "search": "PEUGEOT - 203",
                            "md": "203"
                        },
                        {
                            "mk": "PEUG",
                            "search": "PEUGEOT - 304",
                            "md": "304"
                        },
                        {
                            "mk": "PEUG",
                            "search": "PEUGEOT - 403",
                            "md": "403"
                        },
                        {
                            "mk": "PEUG",
                            "search": "PEUGEOT - 404",
                            "md": "404"
                        },
                        {
                            "mk": "PEUG",
                            "search": "PEUGEOT - 405",
                            "md": "405"
                        },
                        {
                            "mk": "PEUG",
                            "search": "PEUGEOT - 504 SERIES",
                            "md": "504"
                        },
                        {
                            "mk": "PEUG",
                            "search": "PEUGEOT - 505 SERIES",
                            "md": "505"
                        },
                        {
                            "mk": "PEUG",
                            "search": "PEUGEOT - 604",
                            "md": "604"
                        },
                        {
                            "mk": "PHOE",
                            "search": "PHOENIX - ",
                            "md": ""
                        },
                        {
                            "mk": "PIAG",
                            "search": "PIAGGIO - TYPHOON",
                            "md": "TYPH"
                        },
                        {
                            "mk": "PRCA",
                            "search": "PIERCE ARROW - ",
                            "md": ""
                        },
                        {
                            "mk": "PINI",
                            "search": "PINIFARINA - ",
                            "md": ""
                        },
                        {
                            "mk": "PJ",
                            "search": "PJ - D7",
                            "md": "D7"
                        },
                        {
                            "mk": "PLAY",
                            "search": "PLAYBOY - ",
                            "md": ""
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - ACCLAIM",
                            "md": "ACCL"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - ARROW",
                            "md": "ARRO"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - BARRACUDA",
                            "md": "BARR"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - BELVEDERE",
                            "md": "BELV"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - BREEZE",
                            "md": "BREE"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - CAMBRIDGE",
                            "md": "CAMB"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - CARAVELLE",
                            "md": "CARA"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - CHAMP",
                            "md": "CHAM"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - COLT",
                            "md": "COLT"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - CONQUEST",
                            "md": "CONQ"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - CRANBROOK",
                            "md": "CRA"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - CRICKET (IMPORTED)",
                            "md": "CRIC"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - DUSTER",
                            "md": "DUST"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - FURY (ALSO GRAN FURY)",
                            "md": "FURY"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - GTX",
                            "md": "GTX"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - HORIZON (ALSO TC3)",
                            "md": "HORI"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - LASER",
                            "md": "LASE"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - NEON",
                            "md": "NEON"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - PLAZA",
                            "md": "PLAZ"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - RELIANT",
                            "md": "RELI"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - ROAD RUNNER",
                            "md": "ROAD"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - SAPPORO",
                            "md": "SAPO"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - SATELLITE",
                            "md": "SATE"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - SAVOY",
                            "md": "SAVO"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - SCAMP",
                            "md": "SCAM"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - SIGNET",
                            "md": "SIGN"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - SUBURBAN",
                            "md": "SUBU"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - SUNDANCE",
                            "md": "SUND"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - TURISMO",
                            "md": "TURI"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - VALIANT",
                            "md": "VALI"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - VIP",
                            "md": "VIP"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - VOLARE",
                            "md": "VOLA"
                        },
                        {
                            "mk": "PLYM",
                            "search": "PLYMOUTH - VOYAGER",
                            "md": "VOYA"
                        },
                        {
                            "mk": "POIR",
                            "search": "POIRIER - ",
                            "md": ""
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - 2+2",
                            "md": "2P2"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - 2000",
                            "md": "2000"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - 6000",
                            "md": "6000"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - ASTRE",
                            "md": "ASTR"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - AZTEK",
                            "md": "AZTE"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - BONNEVILLE",
                            "md": "BONN"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - CATALINA",
                            "md": "CATA"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - CHIEFTAIN",
                            "md": "CHIE"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - CUSTOM",
                            "md": "CUS"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - DELUXE",
                            "md": "DEL"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - EXECUTIVE",
                            "md": "EXE"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - FIERO",
                            "md": "FIER"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - FIREBIRD",
                            "md": "FIRE"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - FIREFLY",
                            "md": "FIRF"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - FIREHAWK",
                            "md": "FIRH"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - G3",
                            "md": "G3"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - G5",
                            "md": "G5"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - G6",
                            "md": "G6"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - GRAND AM",
                            "md": "GRAN"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - GRAND PARISIENNE",
                            "md": "PARG"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - GRAND PRIX",
                            "md": "GRAP"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - GRAND VILLE",
                            "md": "GRD"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - GT0",
                            "md": "GT0"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - J2000",
                            "md": "J200"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - LAURENTIAN",
                            "md": "LAUR"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - LEMANS",
                            "md": "LEMA"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - MONTANA",
                            "md": "MONT"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - PARISIENNE",
                            "md": "PARI"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - PHOENIX",
                            "md": "PHOE"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - PURSUIT",
                            "md": "PURS"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - SAFARI",
                            "md": "SAFA"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - SKY CHIEF",
                            "md": "SKY"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - SOLSTICE",
                            "md": "SOLS"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - SSE",
                            "md": "SSE"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - STAR CHIEF",
                            "md": "STA"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - STRATO CHIEF",
                            "md": "STRA"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - STREAMLINER",
                            "md": "STR"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - SUNBIRD",
                            "md": "SUNB"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - SUNFIRE",
                            "md": "SUNF"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - SUNRUNNER",
                            "md": "SUNR"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - SUPER CHIEF",
                            "md": "SUP"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - T-1000",
                            "md": "T10"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - TEMPEST",
                            "md": "TEMP"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - TEMPEST GTO",
                            "md": "TEMG"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - TORRENT",
                            "md": "TORR"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - TRANS AM (SEE FIREBIRD)",
                            "md": "TRAN"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - TRANS SPORT/TRANSPORT",
                            "md": "TRAS"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - VENTURA",
                            "md": "VENT"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - VIBE",
                            "md": "VIBE"
                        },
                        {
                            "mk": "PONT",
                            "search": "PONTIAC - WAVE",
                            "md": "WAVE"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - 1300",
                            "md": "130"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - 1500",
                            "md": "150"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - 1600",
                            "md": "160"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - 356",
                            "md": "356"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - 911",
                            "md": "911"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - 912",
                            "md": "912"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - 914",
                            "md": "914"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - 918 SPYDER",
                            "md": "918"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - 924",
                            "md": "924"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - 928",
                            "md": "928"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - 930",
                            "md": "930"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - 944",
                            "md": "944"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - 968",
                            "md": "968"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - BOXSTER",
                            "md": "BOXS"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - CABRIOLET",
                            "md": "CABR"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - CARRERA",
                            "md": "CARR"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - CAYENNE",
                            "md": "CAYE"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - CAYMAN",
                            "md": "CAYM"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - KARMAN",
                            "md": "KARM"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - MACAN",
                            "md": "MACA"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - PANAMERA",
                            "md": "PANA"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - STANDARD",
                            "md": "STA"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - SUPER",
                            "md": "SUP"
                        },
                        {
                            "mk": "PORS",
                            "search": "PORSCHE - TARGA",
                            "md": "TARG"
                        },
                        {
                            "mk": "PRAI",
                            "search": "PRAIRIE SCHOONER - ",
                            "md": ""
                        },
                        {
                            "mk": "PRMO",
                            "search": "PRINCE MOTORS - ",
                            "md": ""
                        },
                        {
                            "mk": "PROG",
                            "search": "PROGRESS - ",
                            "md": ""
                        },
                        {
                            "mk": "PTV",
                            "search": "PTV - ",
                            "md": ""
                        },
                        {
                            "mk": "PUCH",
                            "search": "PUCH - ",
                            "md": ""
                        },
                        {
                            "mk": "PUMM",
                            "search": "PUMA - ",
                            "md": ""
                        },
                        {
                            "mk": "RAM",
                            "search": "RAM - ProMaster",
                            "md": "PROM"
                        },
                        {
                            "mk": "RAMB",
                            "search": "RAMBLER - AMBASSADOR",
                            "md": "AMBA"
                        },
                        {
                            "mk": "RAMB",
                            "search": "RAMBLER - AMERICAN",
                            "md": "AMER"
                        },
                        {
                            "mk": "RAMB",
                            "search": "RAMBLER - CLASSIC",
                            "md": "CLAS"
                        },
                        {
                            "mk": "RAMB",
                            "search": "RAMBLER - CUSTOM",
                            "md": "CUS"
                        },
                        {
                            "mk": "RAMB",
                            "search": "RAMBLER - DELUXE",
                            "md": "DEL"
                        },
                        {
                            "mk": "RAMB",
                            "search": "RAMBLER - SUPER",
                            "md": "SUP"
                        },
                        {
                            "mk": "RAMB",
                            "search": "RAMBLER - TYPHOON",
                            "md": "TYP"
                        },
                        {
                            "mk": "RAMS",
                            "search": "RAMSES - ",
                            "md": ""
                        },
                        {
                            "mk": "REI",
                            "search": "REINELL - ",
                            "md": ""
                        },
                        {
                            "mk": "RELI",
                            "search": "RELIANT - ",
                            "md": ""
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - 18i",
                            "md": "18i"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - 750",
                            "md": "750"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - CARAVELLE",
                            "md": "CARA"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - DAUPHINE",
                            "md": "DAU"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - ESTAFETTE",
                            "md": "EST"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - EXPORT",
                            "md": "EXPO"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - FUEGO",
                            "md": "FUEG"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - GORDINI",
                            "md": "GON"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - LE CAR",
                            "md": "LEC"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - LUXE",
                            "md": "LX"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - R-10",
                            "md": "R10"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - R-12",
                            "md": "R12"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - R-15",
                            "md": "R15"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - R-16",
                            "md": "R16"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - R-17",
                            "md": "R17"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - R-4",
                            "md": "R4"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - R-5",
                            "md": "R5"
                        },
                        {
                            "mk": "RENA",
                            "search": "RENAULT - R-8",
                            "md": "R8"
                        },
                        {
                            "mk": "REO",
                            "search": "REO - ",
                            "md": ""
                        },
                        {
                            "mk": "REXH",
                            "search": "REXHALL - AERBUS",
                            "md": "AERB"
                        },
                        {
                            "mk": "REXH",
                            "search": "REXHALL - CONCORD",
                            "md": "CONC"
                        },
                        {
                            "mk": "REXH",
                            "search": "REXHALL - FLEETWOOD",
                            "md": "FLEE"
                        },
                        {
                            "mk": "REXH",
                            "search": "REXHALL - REXAIR",
                            "md": "REXA"
                        },
                        {
                            "mk": "REXH",
                            "search": "REXHALL - ROLLSAIR",
                            "md": "ROLL"
                        },
                        {
                            "mk": "RIND",
                            "search": "RICH INDUSTRIES - ",
                            "md": ""
                        },
                        {
                            "mk": "RILE",
                            "search": "RILEY - ",
                            "md": ""
                        },
                        {
                            "mk": "ROAD",
                            "search": "ROADRUNNER TRAILERS MFG. - ",
                            "md": ""
                        },
                        {
                            "mk": "ROCH",
                            "search": "ROCHDALE - ",
                            "md": ""
                        },
                        {
                            "mk": "ROK",
                            "search": "ROCKNE - ",
                            "md": ""
                        },
                        {
                            "mk": "ROLL",
                            "search": "ROLLS-ROYCE - CAMARGUE",
                            "md": "CAM"
                        },
                        {
                            "mk": "ROLL",
                            "search": "ROLLS-ROYCE - CORNICHE",
                            "md": "CORN"
                        },
                        {
                            "mk": "ROLL",
                            "search": "ROLLS-ROYCE - FLYING SPUR",
                            "md": "FPR"
                        },
                        {
                            "mk": "ROLL",
                            "search": "ROLLS-ROYCE - MULSANNE",
                            "md": "MUL"
                        },
                        {
                            "mk": "ROLL",
                            "search": "ROLLS-ROYCE - PHANTOM",
                            "md": "PHAN"
                        },
                        {
                            "mk": "ROLL",
                            "search": "ROLLS-ROYCE - SILVER CLOUD",
                            "md": "SILV"
                        },
                        {
                            "mk": "ROLL",
                            "search": "ROLLS-ROYCE - SILVER DAWN",
                            "md": "SID"
                        },
                        {
                            "mk": "ROLL",
                            "search": "ROLLS-ROYCE - SILVER SERAPH",
                            "md": "SER"
                        },
                        {
                            "mk": "ROLL",
                            "search": "ROLLS-ROYCE - SILVER SHADOW",
                            "md": "SIS"
                        },
                        {
                            "mk": "ROLL",
                            "search": "ROLLS-ROYCE - SILVER SPIRIT",
                            "md": "SSP"
                        },
                        {
                            "mk": "ROLL",
                            "search": "ROLLS-ROYCE - SILVER SPUR",
                            "md": "SPR"
                        },
                        {
                            "mk": "ROLL",
                            "search": "ROLLS-ROYCE - SILVER WRAITH",
                            "md": "SIW"
                        },
                        {
                            "mk": "ROOT",
                            "search": "ROOTES - ALPINE",
                            "md": "ALP"
                        },
                        {
                            "mk": "ROOT",
                            "search": "ROOTES - ARROW",
                            "md": "ARR"
                        },
                        {
                            "mk": "ROOT",
                            "search": "ROOTES - IMP",
                            "md": "IMP"
                        },
                        {
                            "mk": "ROOT",
                            "search": "ROOTES - TIGER",
                            "md": "TIG"
                        },
                        {
                            "mk": "ROVE",
                            "search": "ROVER - 2000",
                            "md": "200"
                        },
                        {
                            "mk": "ROVE",
                            "search": "ROVER - 3 LITRE",
                            "md": "3L"
                        },
                        {
                            "mk": "ROVE",
                            "search": "ROVER - 3500",
                            "md": "350"
                        },
                        {
                            "mk": "ROVE",
                            "search": "ROVER - LAND ROVER",
                            "md": "LAND"
                        },
                        {
                            "mk": "ROVE",
                            "search": "ROVER - MARK IV",
                            "md": "MK4"
                        },
                        {
                            "mk": "RYCS",
                            "search": "RYCSA - ",
                            "md": ""
                        },
                        {
                            "mk": "SAAB",
                            "search": "SAAB - 9-3",
                            "md": "9-3"
                        },
                        {
                            "mk": "SAAB",
                            "search": "SAAB - 900",
                            "md": "900"
                        },
                        {
                            "mk": "SAAB",
                            "search": "SAAB - 9000",
                            "md": "9000"
                        },
                        {
                            "mk": "SAAB",
                            "search": "SAAB - 92",
                            "md": "92"
                        },
                        {
                            "mk": "SAAB",
                            "search": "SAAB - 92X",
                            "md": "92X"
                        },
                        {
                            "mk": "SAAB",
                            "search": "SAAB - 93 & 93B",
                            "md": "93"
                        },
                        {
                            "mk": "SAAB",
                            "search": "SAAB - 95",
                            "md": "95"
                        },
                        {
                            "mk": "SAAB",
                            "search": "SAAB - 96",
                            "md": "96"
                        },
                        {
                            "mk": "SAAB",
                            "search": "SAAB - 97",
                            "md": "97"
                        },
                        {
                            "mk": "SAAB",
                            "search": "SAAB - 97X",
                            "md": "97X"
                        },
                        {
                            "mk": "SAAB",
                            "search": "SAAB - 99",
                            "md": "99"
                        },
                        {
                            "mk": "SAAB",
                            "search": "SAAB - GT 750",
                            "md": "GT"
                        },
                        {
                            "mk": "SAAB",
                            "search": "SAAB - SONNET",
                            "md": "SON"
                        },
                        {
                            "mk": "SABR",
                            "search": "SABRA - ",
                            "md": ""
                        },
                        {
                            "mk": "SANG",
                            "search": "SANGYONG - CM600S",
                            "md": "CM60"
                        },
                        {
                            "mk": "SANG",
                            "search": "SANGYONG - JEEP",
                            "md": "JEEP"
                        },
                        {
                            "mk": "SATU",
                            "search": "SATURN - ASTRA",
                            "md": "ASTR"
                        },
                        {
                            "mk": "SATU",
                            "search": "SATURN - EVI",
                            "md": "EVI"
                        },
                        {
                            "mk": "SATU",
                            "search": "SATURN - ION",
                            "md": "ION"
                        },
                        {
                            "mk": "SATU",
                            "search": "SATURN - LS1",
                            "md": "LS1"
                        },
                        {
                            "mk": "SATU",
                            "search": "SATURN - LSERIES",
                            "md": "LSER"
                        },
                        {
                            "mk": "SATU",
                            "search": "SATURN - LW200",
                            "md": "LW20"
                        },
                        {
                            "mk": "SATU",
                            "search": "SATURN - RELAY",
                            "md": "RELA"
                        },
                        {
                            "mk": "SATU",
                            "search": "SATURN - SC",
                            "md": "SC"
                        },
                        {
                            "mk": "SATU",
                            "search": "SATURN - SKY",
                            "md": "SKY"
                        },
                        {
                            "mk": "SATU",
                            "search": "SATURN - SL",
                            "md": "SL"
                        },
                        {
                            "mk": "SATU",
                            "search": "SATURN - SW",
                            "md": "SW"
                        },
                        {
                            "mk": "SATU",
                            "search": "SATURN - VUE",
                            "md": "VUE"
                        },
                        {
                            "mk": "SCIO",
                            "search": "SCION - FR-S",
                            "md": "FRS"
                        },
                        {
                            "mk": "SCIO",
                            "search": "SCION - IM",
                            "md": "IM"
                        },
                        {
                            "mk": "SCIO",
                            "search": "SCION - TC",
                            "md": "TC"
                        },
                        {
                            "mk": "SCIO",
                            "search": "SCION - XA",
                            "md": "XA"
                        },
                        {
                            "mk": "SCIO",
                            "search": "SCION - XB",
                            "md": "XB"
                        },
                        {
                            "mk": "SEA",
                            "search": "SEADOO - ",
                            "md": ""
                        },
                        {
                            "mk": "RAY",
                            "search": "SEARAY - ",
                            "md": ""
                        },
                        {
                            "mk": "SEAT",
                            "search": "SEAT - ",
                            "md": ""
                        },
                        {
                            "mk": "SERA",
                            "search": "SERA - ",
                            "md": ""
                        },
                        {
                            "mk": "SHEB",
                            "search": "SHELBY AMERICAN - COBRA",
                            "md": "COBR"
                        },
                        {
                            "mk": "SHEB",
                            "search": "SHELBY AMERICAN - COBRA GT500",
                            "md": "C500"
                        },
                        {
                            "mk": "SHEB",
                            "search": "SHELBY AMERICAN - CSX",
                            "md": "CSX"
                        },
                        {
                            "mk": "SIAT",
                            "search": "SIATA - ",
                            "md": ""
                        },
                        {
                            "mk": "SILA",
                            "search": "SILA AUTORETTA - ",
                            "md": ""
                        },
                        {
                            "mk": "SIM",
                            "search": "SIMCA - 1000 & 1000GL",
                            "md": "100"
                        },
                        {
                            "mk": "SIM",
                            "search": "SIMCA - 120",
                            "md": "120"
                        },
                        {
                            "mk": "SIM",
                            "search": "SIMCA - ARONDE",
                            "md": "ARO"
                        },
                        {
                            "mk": "SIM",
                            "search": "SIMCA - BERTONE",
                            "md": "BER"
                        },
                        {
                            "mk": "SIM",
                            "search": "SIMCA - ETOILE",
                            "md": "ETO"
                        },
                        {
                            "mk": "SIM",
                            "search": "SIMCA - GLS",
                            "md": "GLS"
                        },
                        {
                            "mk": "SIM",
                            "search": "SIMCA - VEDETTE",
                            "md": "VED"
                        },
                        {
                            "mk": "SIN",
                            "search": "SINGER - CHAMOIS",
                            "md": "CHA"
                        },
                        {
                            "mk": "SIN",
                            "search": "SINGER - VOGUE",
                            "md": "VOG"
                        },
                        {
                            "mk": "SKI",
                            "search": "SKI NAUTIQUE - ",
                            "md": ""
                        },
                        {
                            "mk": "SKOD",
                            "search": "SKODA - ",
                            "md": ""
                        },
                        {
                            "mk": "SMAR",
                            "search": "SMART - FORTWO",
                            "md": "FORT"
                        },
                        {
                            "mk": "SNOW",
                            "search": "SNOWBEAR LIMITED - ",
                            "md": ""
                        },
                        {
                            "mk": "SOUT",
                            "search": "SOUTHLAND - SL252T",
                            "md": "252T"
                        },
                        {
                            "mk": "SOVA",
                            "search": "SOVAM - ",
                            "md": ""
                        },
                        {
                            "mk": "SPAR",
                            "search": "SPARTAN - ",
                            "md": ""
                        },
                        {
                            "mk": "STAN",
                            "search": "STANDARD - ",
                            "md": ""
                        },
                        {
                            "mk": "STLY",
                            "search": "STANLEY - ",
                            "md": ""
                        },
                        {
                            "mk": "STAR",
                            "search": "STAR - ",
                            "md": ""
                        },
                        {
                            "mk": "STEA",
                            "search": "STEALTH - ",
                            "md": ""
                        },
                        {
                            "mk": "STLG",
                            "search": "STERLING - 825",
                            "md": "825"
                        },
                        {
                            "mk": "STLG",
                            "search": "STERLING - 827",
                            "md": "827"
                        },
                        {
                            "mk": "STLG",
                            "search": "STERLING - STERLING",
                            "md": "TK"
                        },
                        {
                            "mk": "STEW",
                            "search": "STEWART - ",
                            "md": ""
                        },
                        {
                            "mk": "STEY",
                            "search": "STEYR-PUCH - ",
                            "md": ""
                        },
                        {
                            "mk": "STRA",
                            "search": "STRALE - ",
                            "md": ""
                        },
                        {
                            "mk": "STUD",
                            "search": "STUDEBAKER - AVANTI",
                            "md": "AVAN"
                        },
                        {
                            "mk": "STUD",
                            "search": "STUDEBAKER - CHALLENGER",
                            "md": "CHAL"
                        },
                        {
                            "mk": "STUD",
                            "search": "STUDEBAKER - CHAMPION",
                            "md": "CHAM"
                        },
                        {
                            "mk": "STUD",
                            "search": "STUDEBAKER - COMMANDER",
                            "md": "COM"
                        },
                        {
                            "mk": "STUD",
                            "search": "STUDEBAKER - CRUISER",
                            "md": "CRU"
                        },
                        {
                            "mk": "STUD",
                            "search": "STUDEBAKER - DAYTONA",
                            "md": "DAYT"
                        },
                        {
                            "mk": "STUD",
                            "search": "STUDEBAKER - GRAND TURISMO",
                            "md": "TURI"
                        },
                        {
                            "mk": "STUD",
                            "search": "STUDEBAKER - HAWK SERIES",
                            "md": "HAWK"
                        },
                        {
                            "mk": "STUD",
                            "search": "STUDEBAKER - LANDALL",
                            "md": "LAN"
                        },
                        {
                            "mk": "STUD",
                            "search": "STUDEBAKER - LANK SERIES",
                            "md": "LAR"
                        },
                        {
                            "mk": "STUD",
                            "search": "STUDEBAKER - PRESIDENT",
                            "md": "PRE"
                        },
                        {
                            "mk": "STUD",
                            "search": "STUDEBAKER - REGAL",
                            "md": "REGA"
                        },
                        {
                            "mk": "STUD",
                            "search": "STUDEBAKER - SCOTSMAN",
                            "md": "SCO"
                        },
                        {
                            "mk": "STUD",
                            "search": "STUDEBAKER - WAGONAIRE",
                            "md": "WAGO"
                        },
                        {
                            "mk": "STUZ",
                            "search": "STUTZ - ",
                            "md": ""
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - 100 SERIES",
                            "md": "100"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - 1100 SERIES",
                            "md": "110"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - 1300 SERIES",
                            "md": "130"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - 1400 SERIES",
                            "md": "140"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - 1600 SERIES",
                            "md": "160"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - ASCENT",
                            "md": "ASCE"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - BAJA",
                            "md": "BAJA"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - BRZ",
                            "md": "BRZ"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - CROSSTREK",
                            "md": "CROS"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - DL",
                            "md": "DL"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - FE",
                            "md": "FE2"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - FORESTER",
                            "md": "FORR"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - GL",
                            "md": "GL"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - GLF",
                            "md": "GLF"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - IMPREZA",
                            "md": "IMPR"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - IMPREZA OUTBACK",
                            "md": "IMPO"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - JUSTY",
                            "md": "JUST"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - LEGACY",
                            "md": "LEGA"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - LEGACY OUTBACK",
                            "md": "LEGO"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - LEONE GL COUPE",
                            "md": "LEON"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - LOYALE",
                            "md": "LOYA"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - OUTBACK SPORT (SW)",
                            "md": "SPOR"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - RX",
                            "md": "RX"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - STANDARD",
                            "md": "STA"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - SVX",
                            "md": "SVX"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - TRIBECA",
                            "md": "TRIB"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - WRX",
                            "md": "WRX"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - XT COUPE",
                            "md": "XTC"
                        },
                        {
                            "mk": "SUBA",
                            "search": "SUBARU - XT6",
                            "md": "XT6"
                        },
                        {
                            "mk": "SUNB",
                            "search": "SUNBEAM - ALPINE",
                            "md": "ALP"
                        },
                        {
                            "mk": "SUNB",
                            "search": "SUNBEAM - ARROW",
                            "md": "ARR"
                        },
                        {
                            "mk": "SUNB",
                            "search": "SUNBEAM - DELUXE",
                            "md": "DEL"
                        },
                        {
                            "mk": "SUNB",
                            "search": "SUNBEAM - IMP",
                            "md": "IMP"
                        },
                        {
                            "mk": "SUNB",
                            "search": "SUNBEAM - MINX",
                            "md": "MINX"
                        },
                        {
                            "mk": "SUNB",
                            "search": "SUNBEAM - RAPIER",
                            "md": "RAP"
                        },
                        {
                            "mk": "SUNB",
                            "search": "SUNBEAM - TIGER",
                            "md": "TIG"
                        },
                        {
                            "mk": "SUPT",
                            "search": "SUPER TWO - ",
                            "md": ""
                        },
                        {
                            "mk": "SUZU",
                            "search": "SUZUKI - AERIO",
                            "md": "AERI"
                        },
                        {
                            "mk": "SUZU",
                            "search": "SUZUKI - ESTEEM",
                            "md": "ESTE"
                        },
                        {
                            "mk": "SUZU",
                            "search": "SUZUKI - FORSA",
                            "md": "FORS"
                        },
                        {
                            "mk": "SUZU",
                            "search": "SUZUKI - GRAND VITARA",
                            "md": "GRVI"
                        },
                        {
                            "mk": "SUZU",
                            "search": "SUZUKI - KIZASHI",
                            "md": "KIZA"
                        },
                        {
                            "mk": "SUZU",
                            "search": "SUZUKI - SAMURAI",
                            "md": "SAMU"
                        },
                        {
                            "mk": "SUZU",
                            "search": "SUZUKI - SIDEKICK",
                            "md": "SIDE"
                        },
                        {
                            "mk": "SUZU",
                            "search": "SUZUKI - SWIFT",
                            "md": "SWIF"
                        },
                        {
                            "mk": "SUZU",
                            "search": "SUZUKI - SX4",
                            "md": "SX4"
                        },
                        {
                            "mk": "SUZU",
                            "search": "SUZUKI - VERONA",
                            "md": "VER"
                        },
                        {
                            "mk": "SUZU",
                            "search": "SUZUKI - VITARA",
                            "md": "VITA"
                        },
                        {
                            "mk": "SUZU",
                            "search": "SUZUKI - X90",
                            "md": "X90"
                        },
                        {
                            "mk": "SUZU",
                            "search": "SUZUKI - XL7",
                            "md": "XL7"
                        },
                        {
                            "mk": "SUZL",
                            "search": "SUZULIGHT SU - ",
                            "md": ""
                        },
                        {
                            "mk": "SYRE",
                            "search": "SYRENA - ",
                            "md": ""
                        },
                        {
                            "mk": "TAMA",
                            "search": "TAMA - ",
                            "md": ""
                        },
                        {
                            "mk": "TATR",
                            "search": "TATRA - ",
                            "md": ""
                        },
                        {
                            "mk": "TAUN",
                            "search": "TAUNUS (GERMAN FORD) - ",
                            "md": ""
                        },
                        {
                            "mk": "TCHA",
                            "search": "TCHAIKA - ",
                            "md": ""
                        },
                        {
                            "mk": "TRPE",
                            "search": "TERRAPLANE - ",
                            "md": ""
                        },
                        {
                            "mk": "TESL",
                            "search": "TESLA MOTORS - MODEL 3",
                            "md": "3"
                        },
                        {
                            "mk": "TESL",
                            "search": "TESLA MOTORS - MODEL S",
                            "md": "S"
                        },
                        {
                            "mk": "TESL",
                            "search": "TESLA MOTORS - MODEL X",
                            "md": "X"
                        },
                        {
                            "mk": "TESL",
                            "search": "TESLA MOTORS - MODEL Y",
                            "md": "Y"
                        },
                        {
                            "mk": "TESL",
                            "search": "TESLA MOTORS - ROADSTER",
                            "md": "ROAD"
                        },
                        {
                            "mk": "THOM",
                            "search": "THOMAS - SCHOOL BUS",
                            "md": "BUS"
                        },
                        {
                            "mk": "THOR",
                            "search": "THOR INDUSTRIES INC. - ACE",
                            "md": "ACE"
                        },
                        {
                            "mk": "THOR",
                            "search": "THOR INDUSTRIES INC. - WAVE",
                            "md": "WAVE"
                        },
                        {
                            "mk": "THUN",
                            "search": "THUNDERJET - ",
                            "md": ""
                        },
                        {
                            "mk": "TITA",
                            "search": "TITAN MOTORCYCLE CO. - ",
                            "md": ""
                        },
                        {
                            "mk": "TJAA",
                            "search": "TJAARDA - ",
                            "md": ""
                        },
                        {
                            "mk": "TORN",
                            "search": "TORNADO (BRITISH) - ",
                            "md": ""
                        },
                        {
                            "mk": "TOYP",
                            "search": "TOYOPET - ",
                            "md": ""
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - 4-RUNNER",
                            "md": "4RUN"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - 86",
                            "md": "86"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - ARISTO",
                            "md": "ARIS"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - AVALON",
                            "md": "AVAL"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - AVENSIS",
                            "md": "AVEN"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - C-HR",
                            "md": "CHR"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - CAMRY",
                            "md": "CAMR"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - CARINA",
                            "md": "CARI"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - CAVALIER",
                            "md": "CAVA"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - CELICA",
                            "md": "CELI"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - COROLLA",
                            "md": "CORO"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - CRESSIDA",
                            "md": "CRES"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - CROWN",
                            "md": "CROW"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - ECHO",
                            "md": "ECHO"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - FJ CRUISER",
                            "md": "FJ"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - HIGHLANDER",
                            "md": "HIGH"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - HILUX",
                            "md": "HILU"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - LAND CRUISER",
                            "md": "LAND"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - LE VAN",
                            "md": "LEVA"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - MARK II",
                            "md": "MARK"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - MATRIX",
                            "md": "MATR"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - MR2",
                            "md": "MR2"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - PASEO",
                            "md": "PASE"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - PRE RUNNER",
                            "md": "PRE"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - PREVIA",
                            "md": "PREV"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - PRIUS",
                            "md": "PRI"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - RAV4",
                            "md": "RAV4"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - SCION",
                            "md": "SCIO"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - SEQUOIA",
                            "md": "SEQU"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - SIENNA",
                            "md": "SIEN"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - SOLARA",
                            "md": "SOLA"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - SR5",
                            "md": "SR5"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - STARLET",
                            "md": "STAR"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - SUPRA",
                            "md": "SUPR"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - T-100",
                            "md": "T100"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - TACOMA",
                            "md": "TACO"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - TERCEL",
                            "md": "TERC"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - TUNDRA",
                            "md": "TUND"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - VENZA",
                            "md": "VENZ"
                        },
                        {
                            "mk": "TOYO",
                            "search": "TOYOTA - YARIS",
                            "md": "YARI"
                        },
                        {
                            "mk": "TRAB",
                            "search": "TRABANT - ",
                            "md": ""
                        },
                        {
                            "mk": "TRIU",
                            "search": "TRIUMPH - 1200",
                            "md": "1200"
                        },
                        {
                            "mk": "TRIU",
                            "search": "TRIUMPH - 1250",
                            "md": "1250"
                        },
                        {
                            "mk": "TRIU",
                            "search": "TRIUMPH - 1300",
                            "md": "1300"
                        },
                        {
                            "mk": "TRIU",
                            "search": "TRIUMPH - 2000",
                            "md": "2000"
                        },
                        {
                            "mk": "TRIU",
                            "search": "TRIUMPH - 250",
                            "md": "250"
                        },
                        {
                            "mk": "TRIU",
                            "search": "TRIUMPH - GT SERIES",
                            "md": "GT"
                        },
                        {
                            "mk": "TRIU",
                            "search": "TRIUMPH - HERALD",
                            "md": "HERA"
                        },
                        {
                            "mk": "TRIU",
                            "search": "TRIUMPH - SPITFIRE",
                            "md": "SPIT"
                        },
                        {
                            "mk": "TRIU",
                            "search": "TRIUMPH - SPORT 6",
                            "md": "SP6"
                        },
                        {
                            "mk": "TRIU",
                            "search": "TRIUMPH - STAG",
                            "md": "STA"
                        },
                        {
                            "mk": "TRIU",
                            "search": "TRIUMPH - TR-3 & TR-3A",
                            "md": "TR3"
                        },
                        {
                            "mk": "TRIU",
                            "search": "TRIUMPH - TR-4 & TR-4A",
                            "md": "TR4"
                        },
                        {
                            "mk": "TRIU",
                            "search": "TRIUMPH - TR6",
                            "md": "TR6"
                        },
                        {
                            "mk": "TRIU",
                            "search": "TRIUMPH - TR7",
                            "md": "TR7"
                        },
                        {
                            "mk": "TRIU",
                            "search": "TRIUMPH - TR8",
                            "md": "TR8"
                        },
                        {
                            "mk": "TRIU",
                            "search": "TRIUMPH - VITESSE",
                            "md": "VITE"
                        },
                        {
                            "mk": "TROJ",
                            "search": "TROJAN - ",
                            "md": ""
                        },
                        {
                            "mk": "TUCK",
                            "search": "TUCKER - ",
                            "md": ""
                        },
                        {
                            "mk": "TURN",
                            "search": "TURNER - ",
                            "md": ""
                        },
                        {
                            "mk": "TVR",
                            "search": "TVR - TUSCAN",
                            "md": "TUS"
                        },
                        {
                            "mk": "TVR",
                            "search": "TVR - VIXEN",
                            "md": "VIXE"
                        },
                        {
                            "mk": "TZ",
                            "search": "TZ - ",
                            "md": ""
                        },
                        {
                            "mk": "UBUI",
                            "search": "U-BUILT - ",
                            "md": ""
                        },
                        {
                            "mk": "USEL",
                            "search": "U.S. ELECTRICAR CORP. - LECTRIC LEOPARD",
                            "md": "LTC"
                        },
                        {
                            "mk": "UAZ",
                            "search": "UAZ (ULIANOVSK AUTOMOBILE ZAVOD) - CCMV",
                            "md": "TK"
                        },
                        {
                            "mk": "UNIC",
                            "search": "UNICAR - ",
                            "md": ""
                        },
                        {
                            "mk": "UNIP",
                            "search": "UNIPOWER - ",
                            "md": ""
                        },
                        {
                            "mk": "UTIL",
                            "search": "UTILITY - ",
                            "md": ""
                        },
                        {
                            "mk": "VAL",
                            "search": "VAL - ",
                            "md": ""
                        },
                        {
                            "mk": "VALK",
                            "search": "VALKRIE - ",
                            "md": ""
                        },
                        {
                            "mk": "VNDN",
                            "search": "VANDEN PLAS - ",
                            "md": ""
                        },
                        {
                            "mk": "VANG",
                            "search": "VANGUARD (CANADA) - DELUXE",
                            "md": "DEL"
                        },
                        {
                            "mk": "VANG",
                            "search": "VANGUARD (CANADA) - ENSIGN",
                            "md": "ENS"
                        },
                        {
                            "mk": "VANG",
                            "search": "VANGUARD (CANADA) - LUXURY",
                            "md": "LUX"
                        },
                        {
                            "mk": "VANG",
                            "search": "VANGUARD (CANADA) - MARK III",
                            "md": "MK3"
                        },
                        {
                            "mk": "VAUX",
                            "search": "VAUXHALL - CRESTA",
                            "md": "CRE"
                        },
                        {
                            "mk": "VAUX",
                            "search": "VAUXHALL - ENVOY",
                            "md": "ENVO"
                        },
                        {
                            "mk": "VAUX",
                            "search": "VAUXHALL - EPIC",
                            "md": "EPIC"
                        },
                        {
                            "mk": "VAUX",
                            "search": "VAUXHALL - FIRENZA",
                            "md": "FIRE"
                        },
                        {
                            "mk": "VAUX",
                            "search": "VAUXHALL - VELOX",
                            "md": "VEL"
                        },
                        {
                            "mk": "VAUX",
                            "search": "VAUXHALL - VICTOR",
                            "md": "VICT"
                        },
                        {
                            "mk": "VAUX",
                            "search": "VAUXHALL - VIVA",
                            "md": "VIVA"
                        },
                        {
                            "mk": "VACR",
                            "search": "VECTOR AEROMOTIVE CORPORATION - M12 (SPORTS COUPE)",
                            "md": "M12"
                        },
                        {
                            "mk": "VACR",
                            "search": "VECTOR AEROMOTIVE CORPORATION - VECTOR",
                            "md": "VECT"
                        },
                        {
                            "mk": "VEAM",
                            "search": "VEHICULOS AUTOMORES MEXICANO - ",
                            "md": ""
                        },
                        {
                            "mk": "VERI",
                            "search": "VERITAS - ",
                            "md": ""
                        },
                        {
                            "mk": "VESP",
                            "search": "VESPA - ",
                            "md": ""
                        },
                        {
                            "mk": "VOGA",
                            "search": "VOLGA - ",
                            "md": ""
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - 113",
                            "md": "113"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - 1200",
                            "md": "1200"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - 1300",
                            "md": "1300"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - 1500",
                            "md": "1500"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - 411/412",
                            "md": "412"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - ATLAS",
                            "md": "ATLA"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - BEETLE",
                            "md": "BEET"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - CABRIOLET",
                            "md": "CABR"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - CORRADO",
                            "md": "CORR"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - DASHER",
                            "md": "DAS"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - EOS",
                            "md": "EOS"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - EUROVAN",
                            "md": "EURO"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - FASTBACK",
                            "md": "FAST"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - FOX",
                            "md": "FOX"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - GOLF",
                            "md": "GOLF"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - GTI",
                            "md": "GTI"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - JETTA",
                            "md": "JETT"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - KARMANN GHIA",
                            "md": "KARM"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - PASSAT",
                            "md": "PASS"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - PHAETON",
                            "md": "PHAE"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - POLO",
                            "md": "POLO"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - QUANTUM",
                            "md": "QUAN"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - RABBIT",
                            "md": "RABB"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - ROUTAN",
                            "md": "ROUT"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - SCIROCCO",
                            "md": "SCIR"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - SQUAREBACK",
                            "md": "SB"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - SUNROOF",
                            "md": "SUR"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - THE THING",
                            "md": "THIN"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - TIGUAN",
                            "md": "TIGU"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - TOUAREG",
                            "md": "TOUA"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - VANAGON",
                            "md": "VANA"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - VARIANT",
                            "md": "VAR"
                        },
                        {
                            "mk": "VOLK",
                            "search": "VOLKSWAGEN - WESTFALIA",
                            "md": "WEST"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - 122 SERIES",
                            "md": "122"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - 140 SERIES",
                            "md": "140"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - 164 SERIES",
                            "md": "164"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - 1800 SERIES",
                            "md": "180"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - 200 SERIES",
                            "md": "200"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - 240 SERIES",
                            "md": "240"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - 245 SERIES",
                            "md": "245"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - 260 SERIES",
                            "md": "260"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - 740 SERIES",
                            "md": "740"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - 745 SERIES",
                            "md": "745"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - 760",
                            "md": "760"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - 765 SERIES",
                            "md": "765"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - 780 SERIES",
                            "md": "780"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - 850 SERIES",
                            "md": "850"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - 940",
                            "md": "940"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - 960",
                            "md": "960"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - C30",
                            "md": "C30"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - C70",
                            "md": "C70"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - COMBI",
                            "md": "COB"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - DL",
                            "md": "DL"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - GL",
                            "md": "GL"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - GLE",
                            "md": "GLE"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - GLT",
                            "md": "GLT"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - P1900",
                            "md": "190"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - PV444",
                            "md": "444"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - PV544",
                            "md": "544"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - R4",
                            "md": "R4"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - S40",
                            "md": "S40"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - S60",
                            "md": "S60"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - S70",
                            "md": "S70"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - S80",
                            "md": "S80"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - S90",
                            "md": "S90"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - SPORT",
                            "md": "SPO"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - V40",
                            "md": "V40"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - V50",
                            "md": "V50"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - V70",
                            "md": "V70"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - V90",
                            "md": "V90"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - XC60",
                            "md": "XC60"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - XC70",
                            "md": "XC70"
                        },
                        {
                            "mk": "VOLV",
                            "search": "VOLVO - XC90",
                            "md": "XC90"
                        },
                        {
                            "mk": "WABA",
                            "search": "WABASH - ",
                            "md": ""
                        },
                        {
                            "mk": "WARS",
                            "search": "WARSZAWA - ",
                            "md": ""
                        },
                        {
                            "mk": "WART",
                            "search": "WARTBURG - ",
                            "md": ""
                        },
                        {
                            "mk": "WARW",
                            "search": "WARWICK - ",
                            "md": ""
                        },
                        {
                            "mk": "WATF",
                            "search": "WATFORD - ",
                            "md": ""
                        },
                        {
                            "mk": "WEND",
                            "search": "WENDAX - ",
                            "md": ""
                        },
                        {
                            "mk": "WEST",
                            "search": "WESTERN STAR - ",
                            "md": ""
                        },
                        {
                            "mk": "WHIP",
                            "search": "WHIPPET - ",
                            "md": ""
                        },
                        {
                            "mk": "WLLS",
                            "search": "WILLYS - ",
                            "md": ""
                        },
                        {
                            "mk": "WILS",
                            "search": "WILSON - ",
                            "md": ""
                        },
                        {
                            "mk": "WINN",
                            "search": "WINNEBEGO - ",
                            "md": ""
                        },
                        {
                            "mk": "WOLS",
                            "search": "WOLSELEY - ",
                            "md": ""
                        },
                        {
                            "mk": "WOOD",
                            "search": "WOODILL WILDFIRE - ",
                            "md": ""
                        },
                        {
                            "mk": "WORT",
                            "search": "WORTHINGTON CHAMP - ",
                            "md": ""
                        },
                        {
                            "mk": "YAMA",
                            "search": "YAMAHA - ",
                            "md": ""
                        },
                        {
                            "mk": "YENK",
                            "search": "YENKO - ",
                            "md": ""
                        },
                        {
                            "mk": "YLN",
                            "search": "YLN (YUE LOONG MOTOR CO.) - ",
                            "md": ""
                        },
                        {
                            "mk": "ZAPO",
                            "search": "ZAPOROZHETS - ",
                            "md": ""
                        },
                        {
                            "mk": "ZARC",
                            "search": "ZAR CAR - ",
                            "md": ""
                        },
                        {
                            "mk": "ZCZY",
                            "search": "ZASTAVIA (ZCZ-YUGOSLAVIA) - YUGO (SERIES)",
                            "md": "YUG"
                        },
                        {
                            "mk": "ZETA",
                            "search": "ZETA - ",
                            "md": ""
                        },
                        {
                            "mk": "ZIL",
                            "search": "ZIL - ",
                            "md": ""
                        },
                        {
                            "mk": "ZIM",
                            "search": "ZIM - ",
                            "md": ""
                        },
                        {
                            "mk": "ZIMR",
                            "search": "ZIMMERMAN AUTOMOBILES - ",
                            "md": ""
                        },
                        {
                            "mk": "ZUND",
                            "search": "ZUNDAPP - ",
                            "md": ""
                        },
                        {
                            "mk": "ZWIC",
                            "search": "ZWICKAU - ",
                            "md": ""
                        }
                    ]

# revision identifiers, used by Alembic.
revision = 'b7fc605b1a27'
down_revision = '14107a12fd38'
branch_labels = None
depends_on = None


def upgrade():
    with op.get_context().autocommit_block():
        bind = op.get_bind()
        meta = sa.MetaData()
        meta.bind = bind
        meta.reflect(bind=bind, only=('vehicle',))
        vehicle = sa.Table('vehicle', meta)
        op.execute('DELETE FROM vehicle')
        op.execute("ALTER SEQUENCE vehicle_id_seq RESTART WITH 1;")
        op.bulk_insert(vehicle, vehicle_data)


def downgrade():
    with op.get_context().autocommit_block():
        bind = op.get_bind()
        meta = sa.MetaData()
        meta.bind = bind
        meta.reflect(bind=bind, only=('vehicle',))
        vehicle = sa.Table('vehicle', meta)
        op.execute('DELETE FROM vehicle')
        op.execute("ALTER SEQUENCE vehicle_id_seq RESTART WITH 1;")
        op.bulk_insert(vehicle, old_vehicle_data)
