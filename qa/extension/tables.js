const city_values = [
    "100 MILE HOUSE", "103 MILE HOUSE", "105 MILE HOUSE", "108 MILE HOUSE", "108 MILE RANCH", "141 MILE HOUSE", "150 MILE HOUSE", "70 MILE HOUSE", "93 MILE HOUSE", "ABBOTSFORD", "ADAMS LAKE", "AGASSIZ", "AGATE", "AHOUSAHT", "AINSWORTH HOT SPRINGS", "ALBREDA", "ALERT BAY", "ALEXANDRIA", "ALEXIS CREEK", "ALEZA LAKE", "ALICE ARM", "ALKALI LAKE", "ALLISON LAKE", "ALTONA", "ANACONDA", "ANAHIM LAKE", "ANAHIMS FLAT IR", "ANAHIMS MEADOW IR", "ANGLEMONT", "ANMORE", "ANSTEY ARM", "ANVIL ISLAND", "ANYOX", "APEX", "APPLEDALE", "ARGENTA", "ARISTAZABAL ISLAND", "ARMSTRONG", "ARRAS", "ARROW PARK", "ASHCROFT", "ASHCROFT RURAL", "ASHTON CREEK", "ASPEN GROVE", "ATHALMER", "ATHLONE ISLAND", "ATKINSON ISLAND", "ATLIN", "ATTACHIE", "AUSTRALIAN", "AVOLA", "BAKER CREEK", "BAKER ISLAND", "BALAKLAVA ISLAND", "BALDONNEL", "BALFOUR", "BAMFIELD", "BANKEIR", "BANKS ISLAND", "BARKERVILLE", "BARNHARTVALE", "BARON ISLAND", "BARRIERE", "BARRIERE RIVER", "BAYNES LAKE", "BEAR FLAT", "BEAR LAKE", "BEASLEY", "BEATON", "BEATTON RIVER", "BEAVER COVE", "BEAVER FALLS", "BEAVERDELL", "BEAVERLEY", "BEDNESTI NORMAN", "BELCARRA", "BELLA BELLA", "BELLA COOLA", "BELL-IRVING", "BENNETT", "BERRY ISLAND", "BESSBOROUGH", "BIG BAR", "BIG BAR LAKE", "BIG CREEK", "BIG LAKE", "BIG LAKE RANCH", "BIG WHITE", "BIRCH ISLAND", "BIRKEN", "BLACK CREEK", "BLACK PINES", "BLACKPOOL", "BLACKWATER", "BLACKWATER NORTH", "BLAEBERRY", "BLEWETT", "BLIGH ISLAND", "BLIND BAY", "BLIND CHANNEL", "BLUBBER BAY", "BLUCHER HALL", "BLUE RIVER", "BLUEBERRY CREEK", "BLUEBERRY RIVER IR", "BOB QUINN", "BOB QUINN LAKE", "BONAPARTE IR", "BONWICK ISLAND", "BOSTON BAR", "BOSTON FLAT", "BOSWELL", "BOUCHIE LAKE", "BOUDREAU LAKE", "BOULDER CITY", "BOWEN ISLAND", "BOWRON LAKES PROVINCIAL PARK", "BOWSER", "BOWSER LAKE", "BOYA LAKE", "BRALORNE", "BRENNAN CREEK", "BRIAR", "BRILLIANT", "BRISCO", "BRITANNIA BEACH", "BROOKMERE", "BROUGHTON ISLAND", "BUCKHORN", "BUCKINGHORSE RIVER", "BUFFALO CREEK", "BUICK", "BULL RIVER", "BURNABY", "BURNABY ISLAND", "BURNS LAKE", "BURTON", "BUTE INLET", "CACHE CREEK", "CACHE CREEK RURAL", "CAHILTY", "CALVERT ISLAND", "CAMPANIA ISLAND", "CAMPBELL ISLAND", "CAMPBELL RIVER", "CANAL FLATS", "CANIM LAKE", "CANOE", "CANOE CREEK", "CANYON ALPINE", "CANYON HOT SPRINGS", "CAPE SCOTT PARK", "CARIBOO RIVER", "CARMI", "CARP LAKE", "CARPENTER LAKE", "CASCADE", "CASTLEDALE", "CASTLEGAR", "CATALA ISLAND", "CAWSTON", "CAYCUSE", "CECIL LAKE", "CEDAR ISLAND", "CEDARVALE", "CELISTA", "CENTRAL SAANICH", "CHAATL ISLAND", "CHAPPERON LAKE", "CHARLIE LAKE", "CHASE", "CHASE CREEK", "CHASE RURAL", "CHASM", "CHATHAM ISLAND", "CHEAM IR", "CHEHALIS", "CHEMAINUS", "CHERRY CREEK", "CHERRYVILLE", "CHESLATTA", "CHETWYND", "CHEZACUT", "CHIEF LAKE", "CHILANKO FORKS", "CHILLIWACK", "CHILLIWACK RIVER VALLEY", "CHIMNEY LAKE", "CHINOOK COVE", "CHRISTIAN VALLEY", "CHRISTINA LAKE", "CHU CHUA", "CINEMA", "CLAPPERTON", "CLAYHURST", "CLEARWATER", "CLEARWATER RURAL", "CLEMRETTA", "CLINTON", "CLINTON RURAL", "CLINTON SOUTH", "CLUCULZ LAKE", "COAL HARBOUR", "COAL ISLAND", "COAL RIVER", "COALMONT", "COBBLE HILL", "COFFIN ISLAND IR", "COLDSTREAM", "COLDSTREAM CREEK", "COLDWATER", "COLLEYMOUNT", "COLUMBIA GARDENS", "COLUMBIA VALLEY", "COLWOOD", "COMOX", "COMPTON ISLAND IR", "CONE ISLAND", "COOMBS", "COOPER CREEK", "COPPER CREEK", "COQUIHALLA", "COQUITLAM", "CORBIN", "CORTES ISLAND", "COTTONWOOD", "COURTENAY", "COUTLEE", "COWICHAN BAY", "COX ISLAND", "CRAIGELLACHIE", "CRANBERRY JUNCTION", "CRANBROOK", "CRAWFORD BAY", "CREASE ISLAND", "CRESCENT SPUR", "CRESCENT VALLEY", "CRESTON", "CROFTON", "CROSS RIVER", "CULTUS LAKE", "CUMBERLAND", "DANSKIN", "D'ARCY", "DARFIELD", "DAVIES ISLAND", "DAWSON CREEK", "DEADMANS CREEK", "DEASE LAKE", "DECKER LAKE", "DECOURCY ISLAND", "DEEP CREEK", "DEEP CREEK IR", "DEHORSEY ISLAND", "DEKA LAKE", "DELTA", "DENMAN ISLAND", "DENNY ISLAND", "DEROCHE", "DEVINE", "DEWDNEY", "DEWDNEY ISLAND", "DIANA ISLAND", "DIGBY ISLAND", "DISCOVERY ISLAND", "DOE RIVER", "DOG CREEK", "DOG CREEK TNRD", "DOGWOOD VALLEY", "DOIG", "DOLPHIN ISLAND", "DOME CREEK", "DONALD", "DONALD LANDING", "DOUGLAS LAKE", "DOVE ISLAND IR", "DRIFTWOOD RIVER", "DUNCAN", "DUNCAN LAKE", "DUNDAS ISLAND", "DUNKLEY", "DUNN LAKE", "DUNSTER", "EAGLE BAY", "EAGLE CREEK", "EAST BARRIERE LAKE", "EAST BLACKPOOL", "EAST PINE", "EAST SALMON ARM", "EAST SOOKE", "EDEN ISLAND", "EDGEWATER", "EDGEWOOD", "EDWARD KING ISLAND", "EGMONT", "ELK VALLEY", "ELKFORD", "ELKHART", "ELKO", "ELSWORTH CAMP", "ENDAKO", "ENDERBY", "ENGEN", "ERICKSON", "ERIE", "ERRINGTON", "ESQUIMALT", "FAIRMONT HOT SPRINGS", "FALKLAND", "FANNY BAY", "FARADAY ISLAND", "FARMINGTON", "FARRANT ISLAND", "FARRELL CREEK", "FAUQUIER", "FELLERS HEIGHTS", "FERNDALE-TABOR", "FERNIE", "FIELD", "FIN ISLAND", "FIRVALE", "FLATHEAD", "FLATROCK", "FLEMING ISLAND", "FLORES ISLAND", "FLY ISLAND IR", "FONTAS", "FOREMAN FLATS", "FOREST GROVE", "FORGETMENOT CREEK", "FORT BABINE", "FORT FRASER", "FORT GEORGE NO 2", "FORT LIARD", "FORT NELSON", "FORT NELSON IR", "FORT ST JAMES", "FORT ST JOHN", "FORT STEELE", "FORT WARE", "FRANCOIS LAKE", "FRASER", "FRASER LAKE", "FRASER VALLEY", "FREDERICK", "FRUITVALE", "FURRY CREEK", "GABRIOLA ISLAND", "GALENA BAY", "GALIANO ISLAND", "GALLOWAY", "GAMBIER ISLAND", "GANG RANCH", "GARDEN BAY", "GARIBALDI PARK", "GENELLE", "GERMANSEN LANDING", "GIBSON ISLAND", "GIBSONS", "GIL ISLAND", "GILFORD ISLAND", "GILLIES BAY", "GINGOLX", "GISCOME", "GITANMAAX", "GITANYOW", "GITAUS", "GITSEGUKLA", "GITWANGAK", "GITWINKSIHLKW", "GLADE", "GLEN VOWELL", "GLENORA", "GLIMPSE LAKE", "GOLD RIVER", "GOLDEN", "GOLDEN EARS PARK", "GOOD HOPE LAKE", "GOODLOW", "GOOSE ISLAND", "GOSCHEN ISLAND", "GOSSIP ISLAND", "GRAND FORKS", "GRANDVIEW BENCH", "GRANISLE", "GRASMERE", "GRASSLANDS IR", "GRASSY ISLAND IR", "GRASSY PLAINS", "GRAY CREEK", "GREAT BEAVER LAKE", "GREEN LAKE", "GREENVILLE", "GREENWOOD", "GREGORY ISLAND", "GRIBBELL ISLAND", "GRINDROD", "GROUNDBIRCH", "GUNDY", "GURD ISLAND", "GUTAH", "HAGENSBORG", "HAGWILGET", "HALFMOON BAY", "HALFWAY RIVER", "HALFWAY RIVER IR", "HAMBER PROVINCIAL PARK", "HANCEVILLE", "HANSON ISLAND", "HARBLEDOWN ISLAND", "HARDWICKE ISLAND", "HARDY ISLAND", "HARRISON HOT SPRINGS", "HARRISON ISLAND", "HARRISON LAKE", "HARRISON MILLS", "HARROP", "HARTLEY BAY", "HARWOOD ISLAND", "HASLER FLATS", "HAT CREEK", "HAT CREEK IR", "HATZIC", "HAWKESBURY ISLAND", "HAZELTON", "HAZELTON RURAL", "HECATE ISLAND", "HEDLEY", "HEFFLEY CREEK", "HEFFLEY CREEK", "HELBY ISLAND", "HELMUT", "HEMLOCK VALLEY", "HENDRIX LAKE", "HENRY ISLAND", "HERNANDO ISLAND", "HIBBEN ISLAND", "HIGHLANDS", "HILLS", "HIXON", "HIXON SOUTH", "HOLBERG", "HONEYMOON BAY", "HOODOO LAKE", "HOPE", "HOPE ISLAND", "HOPKINS LANDING", "HORNBY ISLAND", "HORSEFLY", "HOSMER", "HOT SPRINGS COVE", "HOUSTON", "HOWSER", "HUDSON'S HOPE", "HULL ISLAND", "HUNTER ISLAND", "HUPEL", "HURST ISLAND", "HUTCHISON LAKE", "HUXLEY ISLAND", "HYAS LAKE", "INDIAN ARM", "INSECT ISLAND", "INTEGRATED GANG TASK FORCE", "INVERMERE", "IRVINES LANDING", "ISKUT", "ISLE PIERRE", "JACKFISH LAKE", "JADE CITY", "JAFFRAY", "JAMES ISLAND", "JERVIS INLET", "JESMOND", "JORDAN RIVER", "JUSKATLA", "KADIS IR", "KALEDEN", "KAMLOOPS", "KANAKA BAR", "KASLO", "KEATS ISLAND", "KELLY LAKE", "KELLY LAKE TNRD", "KELOWNA", "KEMANO", "KENNEDY ISLAND", "KENNEDY LAKE", "KEREMEOS", "KERSLEY", "KILDONAN", "KILKERRAN", "KIMBERLEY", "KINASKAN", "KINCOLITH", "KINGCOME INLET", "KINGSGATE", "KINGSVALE", "KISPIOX", "KISPIOX VALLEY", "KITAMAAT VILLAGE", "KITCHENER", "KITIMAT", "KITKATLA", "KITSAULT", "KITWANGA", "KLAOITISIS ISLAND", "KLAPPAN", "KLEENA KLEENE", "KLEMTU", "KNIGHT INLET", "KNUTSFORD", "KOKSILAH", "KOOTENAY BAY", "KOOTENAY PARK", "KOOTENAY PASS", "KOTCHO LAKE", "KRESTOVA", "KSUI LA DAS IR", "KTSUMKAYLUM IR", "KULDEKDUMA IR", "KULDO", "KUNGA ISLAND", "KUNGHIT ISLAND", "KUPER ISLAND", "KWADACHA", "KWINAMSS RIVER", "KYE YAA LA IR", "KYUQUOT", "LAC DU BOIS", "LAC LA HACHE", "LAC LE JEUNE", "LADYSMITH", "LAKE COUNTRY", "LAKE COWICHAN", "LAKE ERROCK", "LAKELSE LAKE", "LANGARA ISLAND", "LANGDALE", "LANGFORD", "LANGLEY", "LANTZVILLE", "LANZ ISLAND", "LARDEAU", "LASQUETI ISLAND", "LAVINGTON", "LAX KW' ALAAMS", "LAXGALTS AP", "LEANCHOIL", "LEE CREEK", "LEWIS ISLAND", "LIARD RIVER", "LIKELY", "LILLOOET", "LILLOOET RURAL", "LILY LAKE", "LINA ISLAND", "LINDELL BEACH", "LIONS BAY", "LISTER", "LITTLE FORT", "LODGEPOLE", "LOGAN LAKE", "LONE BUTTE", "LONE PRAIRIE", "LONG BEACH", "LONGWORTH", "LOON LAKE", "LORETTA ISLAND", "LOUIS CREEK", "LOWER ARROW", "LOWER NICOLA", "LOWER POST", "LUMBY", "LUND", "LYELL ISLAND", "LYTTON", "LYTTON RURAL", "MACKENZIE", "MACKENZIE RURAL", "MADEIRA PARK", "MAGNA BAY", "MAHATTA RIVER", "MAHOOD FALLS", "MAITLAND ISLAND", "MALAHAT", "MALAKWA", "MAMIT LAKE", "MANNING PARK", "MANSON CREEK", "MANSONS LANDING", "MARA", "MARBLE CANYON", "MARGUERITE", "MARINA ISLAND", "MARS ISLAND", "MASSET", "MAUD ISLAND", "MAUDE ISLAND", "MAURELLE ISLAND", "MAXHAMISH", "MAYNE ISLAND", "MAYOOK", "MCCAULEY ISLAND", "MCGILLIVRAY LAKE", "MCGREGOR", "MCKAY ISLAND", "MCLEESE LAKE", "MCLEOD LAKE", "MCLEOD LAKE RESERVE", "MCLURE", "MEADOW CREEK", "MEADOW LAKE", "MEARES ISLAND", "MEGIN LAKE", "MELVILLE ISLAND", "MERRITT", "MERVILLE", "MESACHIE LAKE", "METCHOSIN", "METLAKATLA", "MEZIADIN", "MEZIADIN LAKE", "MICA CREEK", "MILL BAY", "MINNIE LAKE", "MINSTREL ISLAND", "MIOCENE", "MIRROR LAKE", "MISSEZULA LAKE", "MISSEZULA LAKE TNRD", "MISSION", "MIWORTH", "MOBERLY LAKE", "MOKETAS ISLAND", "MOMICH LAKE", "MONKMAN", "MONTE CREEK", "MONTE LAKE", "MONTNEY", "MONTROSE", "MOOSE HEIGHTS", "MORESBY ISLAND", "MORICETOWN-WITSET FN", "MOSSVALE", "MOUNT CURRIE", "MOUNT ROBSON", "MOYIE", "MT LE MORAY", "MT ROBSON PROVINCIAL PARK", "MT TERRY FOX PROVINCIAL PARK", "MT WASHINGTON", "MUD RIVER", "MUDGE ISLAND", "MUNCHO LAKE", "MURCHISON ISLAND", "MURDALE", "MUSKWA", "NAKUSP", "NAMU", "NANAIMO", "NANOOSE BAY", "NARAMATA", "NARCOSLI CREEK", "NASS CAMP", "NAZKO", "NECHAKO", "NEEDLES", "NELSON", "NELSON ISLAND", "NELWAY", "NEMAIAH VALLEY", "NESS LAKE", "NEW AIYANSH", "NEW DENVER", "NEW HAZELTON", "NEW WESTMINSTER", "NEWGATE", "NICOLA LAKE", "NIGEI ISLAND", "NIMPKISH", "NIMPO LAKE", "NISKONLITH LAKE", "NOOAITCH", "NOOTKA ISLAND", "NOOTKA SOUND", "NORALEE", "NORTH BARRIERE LAKE", "NORTH BEND", "NORTH BONAPARTE", "NORTH BROUGHTON ISLAND", "NORTH FALKLAND", "NORTH GABLES", "NORTH ISLAND", "NORTH KELLY", "NORTH KINBASKET LAKE", "NORTH MARA", "NORTH PENDER ISLAND", "NORTH PINE", "NORTH SAANICH", "NORTH SHORE", "NORTH THOMPSON IR", "NORTH VANCOUVER", "NOTCH HILL", "NUKKO LAKE", "OAK BAY", "OASIS", "OBSTRUCTION ISLAND", "OCEAN FALLS", "OKANAGAN FALLS", "OKANAGAN IR NORTH", "OKANAGAN IR SOUTH", "OLALLA", "OLIVER", "ONE ISLAND LAKE", "OONA RIVER", "OOTISCHENIA", "OOTSA LAKE", "OSBORN", "OSOYOOS", "OTTER POINT", "OWEEKENO", "OWL ISLAND", "PACIFIC RIM PARK NORTH", "PACIFIC RIM PARK SOUTH", "PALLING", "PANORAMA", "PARKER ISLAND", "PARKSVILLE", "PARSNIP", "PARSON", "PARSON ISLAND", "PASKA LAKE", "PASS CREEK", "PASSMORE", "PAUL LAKE", "PAVILION", "PEACHLAND", "PEARSE ISLAND", "PEEJAY", "PEMBERTON", "PEMBERTON MEADOWS", "PENASK SUMMIT", "PEND DOREILLE", "PENDER HARBOUR", "PENDER ISLAND", "PENELAKUT ISLAND", "PENNY", "PENTICTON", "PETER HOPE LAKE", "PIERS ISLAND", "PINANTAN LAKE", "PINCHI", "PINCHI LAKE", "PINE PASS", "PINE PASS EAST", "PINE PASS WEST", "PINE VALLEY", "PINEVIEW", "PINEVIEW FFG", "PINK MOUNTAIN", "PITT ISLAND", "PITT MEADOWS", "POOLEY ISLAND", "POPKUM", "PORCHER ISLAND", "PORT ALBERNI", "PORT ALBION", "PORT ALICE", "PORT CLEMENTS", "PORT COQUITLAM", "PORT EDWARD", "PORT ESSINGTON", "PORT HARDY", "PORT MANN", "PORT MCNEILL", "PORT MELLON", "PORT MOODY", "PORT NEVILLE", "PORT RENFREW", "PORTLAND ISLAND", "POUCE COUPE", "POWDER KING", "POWELL RIVER", "PRESCOTT ISLAND", "PRESPATOU", "PRESSY LAKE", "PRICE ISLAND", "PRIESTLY", "PRINCE GEORGE", "PRINCE RUPERT", "PRINCESS ROYAL ISLAND", "PRINCETON", "PRITCHARD", "PROCTER", "PROGRESS", "PROPHET RIVER", "PURDEN", "QUADRA ISLAND", "QUALICUM BEACH", "QUATHIASKI COVE", "QUATSINO", "QUEEN CHARLOTTE", "QUEEN CHARLOTTE ISLANDS", "QUEENS BAY", "QUESNEL", "QUESNEL LAKE", "QUILCHENA", "RADIUM HOT SPRINGS", "RAMSAY ISLAND", "RANDALL ISLAND", "RASPBERRY", "READ ISLAND", "RED LAKE", "RED ROCK", "REDSTONE", "REEF ISLAND", "REES ISLAND", "REFUGE COVE", "RENNELL SOUND", "RENNISON ISLAND", "REVELSTOKE", "RICHARDSON ISLAND", "RICHMOND", "RIONDEL", "RISKE CREEK", "ROBERTS CREEK", "ROBERTSON CREEK", "ROBSON", "ROCK CREEK", "RODERICK ISLAND", "ROE LAKE", "ROGERS PASS", "ROLLA", "ROOSVILLE", "ROSE LAKE", "ROSE PRAIRIE", "ROSEBERY", "ROSSLAND", "ROSSWOOD", "ROYSTON", "RUBY LAKE", "RUXTON ISLAND", "SAANICH", "SALMO", "SALMON ARM", "SALMON RIVER", "SALMON RIVER IR", "SALMON VALLEY", "SALT SPRING ISLAND", "SALTERY BAY", "SAN JOSEF", "SANCA", "SANDILANDS ISLAND", "SANDSPIT", "SARAH ISLAND", "SARITA", "SATURNA ISLAND", "SAVARY ISLAND", "SAVONA", "SAYWARD", "SCOTCH CREEK", "SECHELT", "SETON PORTAGE", "SEWALL", "SEWELL INLET", "SEYMOUR ARM", "SEYMOUR INLET", "SHALALTH", "SHAWNIGAN LAKE", "SHEARWATER", "SHELLEY", "SHELL-GLEN", "SHIRLEY", "SHOREACRES", "SHUTTY BENCH", "SICAMOUS", "SIERRA", "SIKANNI", "SILVER SANDS", "SILVERTON", "SINCLAIR MILLS", "SIRDAR", "SKEENA", "SKEETCHESTN IR", "SKOOKUMCHUCK", "SLOCAN", "SLOCAN PARK", "SMITH ISLAND", "SMITHERS", "SNYDER", "SOAMES POINT", "SODA CREEK", "SOINTULA", "SOLSQUA", "SOMERVILLE ISLAND", "SONORA ISLAND", "SOOKE", "SORRENTO", "SOUTH DAWSON", "SOUTH HAZELTON", "SOUTH ISLAND", "SOUTH KINBASKET LAKE", "SOUTH PENDER ISLAND", "SOUTH SLOCAN", "SOUTH STRATHCONA PARK", "SOUTH TAYLOR", "SOUTHBANK", "SOUTHEAST DISTRICT", "SPALLUMCHEEN", "SPARWOOD", "SPATSIZI", "SPATSUM", "SPICER ISLAND", "SPILLIMACHEEN", "SPOKIN LAKE", "SPRINGHOUSE", "SPUZZUM", "SQUAMISH", "ST IVES", "STACKHOUSE ISLAND", "STEIN MOUNTAIN", "STELLAKO", "STEPHENS ISLAND", "STEWART", "STIKINE", "STONE IR 1A", "STONE MOUNTAIN PARK", "STONER", "STONY CREEK SAIK'UZ IR", "STRANGE ISLAND", "STRATHCONA PARK", "STRATHNAVER", "STUART ISLAND", "STUIE", "STUMP LAKE", "SUKUNKA VALLEY", "SULLIVAN BAY", "SUMMERLAND", "SUMMIT LAKE", "SUN PEAKS", "SUNDANCE LAKES", "SUNRISE VALLEY", "SUNSET PRAIRIE", "SUNSHINE COAST", "SUNSHINE VALLEY", "SUNSHINE VALLEY TNRD", "SURREY", "SUSAN ISLAND", "SUSKWA", "SWANSON ISLAND", "SWIFT RIVER", "SWINDLE ISLAND", "TA TA CREEK", "TACHIE", "TAGHUM", "TAHLTAN", "TAHSIS", "TAHSISH RIVER", "TAKLA LANDING", "TAKU", "TAKYSIE LAKE", "TALUNKWAN ISLAND", "TANU ISLAND", "TAPPEN", "TARRYS", "TATALROSE", "TATLA LAKE", "TATLATUI LAKE", "TATLAYOKO LAKE", "TATSHENSHINI", "TAYLOR", "TCHESINKUT LAKE", "TELEGRAPH COVE", "TELEGRAPH CREEK", "TELKWA", "TERRACE", "TESLIN", "TETE JAUNE CACHE", "TETSA RIVER", "TEXADA ISLAND", "THETIS ISLAND", "THORNHILL", "THREE VALLEY", "THRUMS", "THURLOW ISLANDS", "TINTAGEL", "TLELL", "TOAD RIVER", "TOBA INLET", "TOBIANO", "TOFINO", "TOMSLAKE", "TOPLEY", "TOPLEY LANDING", "TRACEY ISLAND", "TRAIL", "TRAPP LAKE", "TROUT LAKE", "TRUTCH", "TRUTCH ISLAND", "TSAY KEH DENE", "TUGWELL ISLAND IR", "TULAMEEN", "TUNKWA LAKE", "TUPPER", "TURNOUR ISLAND", "TURTLE VALLEY", "TWEEDSMUIR PARK SOUTH", "TWEEDSMUIR PROVINCIAL PARK", "TWO MILE", "TWO RIVERS", "TYE", "TZARTUS ISLAND", "VANCOUVER (UBC)", "UCLUELET", "UNION BAY", "UNION ISLAND", "UPPER CUTBANK", "UPPER FRASER", "UPPER SKEENA", "VALDES ISLAND", "VALEMOUNT", "VALEMOUNT RURAL", "VALLICAN", "VAN ANDA", "VANCOUVER", "VANDERHOOF", "VARGAS ISLAND", "VAVENBY", "VENABLES VALLEY", "VERNON", "VICTORIA", "VIEW ROYAL", "VILLAVERDE ISLANDS", "VINSULLA", "VISCOUNT ISLAND", "WALES ISLAND", "WALHACHIN", "WAPITI RIVER", "WARDNER", "WARFIELD", "WASA", "WATCH LAKE", "WATHUS ISLAND", "WATSON LAKE", "WELLS", "WELLS GRAY PARK", "WEST CRACROFT ISLAND", "WEST FERNIE", "WEST KELOWNA", "WEST LAKE", "WEST VANCOUVER", "WESTBANK", "WESTHOLME", "WESTWOLD", "WHALETOWN", "WHISTLER", "WHITE LAKE", "WHITE RIVER", "WHITE ROCK", "WHITELEY ISLAND", "WICKANINNISH ISLAND", "WILLIAM ISLAND", "WILLIAMS LAKE", "WILLIS POINT", "WILLISTON LAKE", "WILLOW FLATS", "WILLOW RIVER", "WILLOW RIVER VALLEY", "WILLOW VALLEY", "WILMER", "WILSON CREEK", "WINDERMERE", "WINLAW", "WINTER HARBOUR", "WISTARIA", "WITSET", "WONOWON", "WOODPECKER", "WOSS", "WYCLIFFE", "WYNNDEL", "WYNNDEL", "YAHK", "YALE", "YMIR", "YOUBOU", "YOYO", "ZAYAS ISLAND", "ZEBALLOS"
  ];

