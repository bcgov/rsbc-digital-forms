"""lki_hwy_seg_init_data

Revision ID: 0d9df346b27d
Revises: 1d9b5876488f
Create Date: 2025-09-26 13:18:15.273586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d9df346b27d'
down_revision = '1d9b5876488f'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
-- UPSERT statements for lki_highway table
-- Generated from HIGHWAY-Table 1.csv

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0001', 1, '', 'TRANS-CANADA')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('001A', 1, 'A', 'REPLACED TRANS-CANADA SECTIONS')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0002', 2, '', 'ALBERTA - DAWSON CREEK')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0003', 3, '', 'CROWSNEST')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('003A', 3, 'A', 'KEREMEOS - KALEDEN JCT - OSOYOOS - CASTLEGAR - NELSON')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('003B', 3, 'B', 'NANCY GREENE LAKE - ROSSLAND - MEADOWS')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0004', 4, '', 'QUALICUM - TOFINO')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('004A', 4, 'A', 'PARKSVILLE - ROUTE 4, COOMBS')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0005', 5, '', 'COQUIHALLA - KAMLOOPS - YELLOWHEAD SOUTH')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('005A', 5, 'A', 'PRINCETON - ASPEN GROVE - MERRITT - KAMLOOPS')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0006', 6, '', 'NELWAY - NELSON - SLOCAN - NAKUSP - VERNON')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0007', 7, '', 'LOUGHEED')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('007B', 7, 'B', 'MARY HILL BYPASS')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0008', 8, '', 'MERRITT - SPENCES BRIDGE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0009', 9, '', 'ROSEDALE - AGASSIZ - HARRISON HOT SPRINGS')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0010', 10, '', 'LADNER - LANGLEY')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0011', 11, '', 'HUNTINGDON - MISSION')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0012', 12, '', 'LYTTON - LILLOOET - CACHE CREEK')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0013', 13, '', 'ALDERGROVE - BELLINGHAM')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0014', 14, '', 'WEST COAST (SOOKE)')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0015', 15, '', 'PACIFIC')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0016', 16, '', 'YELLOWHEAD TRANS-CANADA')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0017', 17, '', 'PATRICIA BAY -TSAWWASSEN - SOUTH FRASER PERIMETER')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('017A', 17, 'A', 'HWY 17 AT 28 AVE - HWY 99')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0018', 18, '', 'COWICHAN VALLEY')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0019', 19, '', 'INLAND ISLAND')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('019A', 19, 'A', 'OLD ISLAND')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0020', 20, '', 'CHILCOTIN - BELLA COOLA')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0021', 21, '', 'CRESTON - RYKERTS')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0022', 22, '', 'PATERSON - ROSSLAND - CASTLEGAR')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('022A', 22, 'A', 'WANETA')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0023', 23, '', 'NAKUSP - MICA CREEK')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0024', 24, '', '93 MILE - LITTLE FORT')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0026', 26, '', 'BARKERVILLE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0027', 27, '', 'VANDERHOOF - STUART LAKE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0028', 28, '', 'GOLD RIVER')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0029', 29, '', 'HUDSON HOPE - DON PHILLIPS WAY')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0030', 30, '', 'RTE 19 - PORT ALICE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0031', 31, '', 'BALFOUR - KASLO - GALENA BAY')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('031A', 31, 'A', 'KASLO - NEW DENVER')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0033', 33, '', 'ROCK CREEK - KELOWNA')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0035', 35, '', 'NORTH FRANCOIS')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0037', 37, '', 'KITIMAT - CASSIAR')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('037A', 37, 'A', 'GLACIER')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0039', 39, '', 'MACKENZIE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0041', 41, '', 'DANVILLE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0043', 43, '', 'ELK VALLEY')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0049', 49, '', 'DAWSON CREEK - SPIRIT RIVER')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0052', 52, '', 'ARRAS - TUMBLER RIDGE - TUPPER')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0062', 62, '', '(UNOFFICIAL) HIGH LEVEL RD: NEW HAZELTON - HAZELTON')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0077', 77, '', 'LIARD')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0091', 91, '', 'ANNACIS ISLAND ; RICHMOND FREEWAY')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('091A', 91, 'A', 'QUEENSBOROUGH CONNECTOR')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0093', 93, '', 'ROOSVILLE - RADIUM HOT SPRINGS - CASTLE MTN JCT')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0095', 95, '', 'YAHK - KINGSGATE - KOOTENAY - COLUMBIA')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('095A', 95, 'A', 'KIMBERLEY')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0097', 97, '', 'OKANAGAN - CARIBOO - ALASKA')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('097A', 97, 'A', 'VERNON - SICAMOUS')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('097B', 97, 'B', 'GRINDROD - SALMON ARM')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('097C', 97, 'C', 'OKANAGAN CONNECTOR - LOGAN LAKE - CACHE CREEK')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('097D', 97, 'D', 'MEADOW CREEK ROAD')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0099', 99, '', 'VANCOUVER - BLAINE - SEA TO SKY')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('099A', 99, 'A', 'KING GEORGE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0101', 101, '', 'SUNSHINE COAST')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0113', 113, '', 'NISGA''A HIGHWAY')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0118', 118, '', 'BABINE LAKE ROAD')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0395', 395, '', 'CHRISTINA LAKE - LAURIER')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0901', 901, '', 'LOWER MAINLAND UNNUMBERED ROUTE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0902', 902, '', 'VANCOUVER ISLAND UNNUMBERED ROUTE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0903', 903, '', 'ROCKY MOUNTAIN UNNUMBERED ROUTE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0904', 904, '', 'WEST KOOTENAY UNNUMBERED ROUTE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0905', 905, '', 'OKANAGAN SHUSWAP UNNUMBERED ROUTE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0906', 906, '', 'THOMPSON NICOLA UNNUMBERED ROUTE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0907', 907, '', 'CARIBOO UNNUMBERED ROUTE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0908', 908, '', 'PEACE UNNUMBERED ROUTE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0909', 909, '', 'FORT GEORGE UNNUMBERED ROUTE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0910', 910, '', 'BULKLEY STIKINE UNNUMBERED ROUTE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0911', 911, '', 'SKEENA UNNUMBERED ROUTE')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

INSERT INTO "TAR"."lki_highway" ("code", "number", "letter", "description")
VALUES ('0916', 916, '', 'GOLDEN EARS WAY SEGMENTS')
ON CONFLICT ("code")
DO UPDATE SET
    "number" = EXCLUDED."number",
    "letter" = EXCLUDED."letter",
    "description" = EXCLUDED."description";

               
-- UPSERT statements for lki_segment table
-- Generated from SEGMENT-Table 1.csv

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0203', '0916', 'NB EXIT FROM GOLDEN EARS - 113B AVE', 'N', 0.3)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0207', '0916', 'NB EXIT FROM GOLDEN EARS WAY - 200 ST', 'N', 0.47)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0209', '0916', 'S/B EXIT FROM GOLDEN EARS - 113B AVE / AIRPORT WAY', 'S', 0.34)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0212', '0916', 'GOLDEN EARS WAY N/B: 176 ST (HWY 15) - HWY 7', 'N', 9.97)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0213', '0916', 'GOLDEN EARS WAY S/B: HWY 7 - 176 ST (HWY 15)', 'S', 9.97)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0214', '0916', 'GOLDEN EARS WAY:  HWY 7 - 210 ST', 'N', 2.85)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0216', '0916', '201 ST ONRAMP TO GOLDEN EARS WAY N/B', 'N', 0.45)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0217', '0916', 'S/B EXIT FROM GOLDEN EARS WAY - 199A ST', 'S', 0.73)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0313', '0902', 'MCKENZIE AVE: RTE 17 - RTE 1', 'W', 2.51)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0320', '0902', 'WEST SAANICH ROAD: VERDIER AVE - MCTAVISH RD', 'N', 6.83)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0325', '0902', 'MCTAVISH ROAD: WEST SAANICH RD - LOCHSIDE DR', 'E', 3.57)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0326', '0902', 'MCTAVISH RD - ANACORTES FERRY VIA LOCHSIDE', 'N', 2.14)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0348', '0902', 'LAKE COWICHAN RD: SKUTZ FALLS RD - N COWICHAN BNDY', 'E', 14.54)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0356', '019A', 'BRECHIN RD: STEWART AVE (DEPT.BAY) - ISLAND HWY', 'N', 0.99)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0360', '0001', 'CEDAR RD - JCT STEWART AVE/TERMINAL AVE', 'N', 5.92)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0363', '0902', 'TZOUHALEM RD: COWICHAN BAY RD - MAPLE BAY RD', 'N', 5.08)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0365', '0902', 'CROFTON RD: CHEMAINUS RD - SALTSPRING FERRY', 'E', 4.19)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0368', '001A', 'RTE 1 / MT SICKER - CROFTON RD', 'N', 2.3)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0369', '001A', 'CHEMAINUS RD: CROFTON RD - HWY 1 (LADYSMITH)', 'N', 15.14)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0373', '0014', 'VETERANS MEMORIAL PARKWAY: RTE 1 - SOOKE RD', 'S', 3.53)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0374', '0014', 'SOOKE RD: VETERANS MEMORIAL PKWAY - OTTER POINT RD', 'W', 22.06)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0375', '0014', 'WEST COAST RD: SOOKE - PORT RENFREW', 'W', 72.84)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0377', '0902', 'PACIFIC MARINE RD: SOUTH SHORE RD - DEERING RD', 'S', 50.68)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0378', '0902', 'DEERING RD: PACIFIC MARINE RD - HWY 14', 'S', 2.96)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0380', '0017', 'VICTORIA - SWARTZ BAY', 'N', 28.39)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0381', '0017', 'SWARTZ BAY - VICTORIA', 'S', 28.37)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0382', '0902', 'SOUTH SHORE RD: HONEYMOON BAY - MESACHIE LAKE', 'E', 6.87)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0383', '0902', 'SOUTH SHORE RD: MESACHIE LAKE - LAKE COWICHAN', 'E', 8.06)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0384', '0018', 'LAKE COWICHAN - DUNCAN', 'E', 25.76)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0386', '0902', 'YOUBOU RD: YOUBOU - HWY 18 (LAKE COWICHAN)', 'E', 15.08)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0402', '0001', 'TOLMIE AVE (VICTORIA) - MCKENZIE AVE', 'W', 3.04)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0403', '0001', 'MCKENZIE AVE - TOLMIE AVE (VICTORIA)', 'E', 3.03)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0412', '0001', 'MCKENZIE AVE - WESTSHORE PARKWAY', 'W', 10.79)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0413', '0001', 'WESTSHORE PARKWAY - MCKENZIE AVE', 'E', 10.77)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0421', '0001', 'WESTSHORE PARKWAY - RTE 18 / HERD RD', 'N', 48.99)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0432', '0001', 'RTE 18 / HERD RD - RTE 1A (MT SICKER RD)', 'N', 6.85)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0433', '0001', 'RTE 1A (MT SICKER RD) - RTE 18 / HERD RD', 'S', 6.85)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0442', '0001', 'RTE 1A (MT SICKER RD) - RTE 1A (CHEMAINUS RD)', 'N', 14.24)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0443', '0001', 'RTE 1A (CHEMAINUS RD) - RTE 1A (MT SICKER RD)', 'S', 14.23)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0454', '0001', 'RTE 1A (CHEMAINUS RD) - DUKE POINT U/P', 'N', 17.52)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0455', '0001', 'DUKE POINT U/P - RTE 1A (CHEMAINUS RD)', 'S', 17.52)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0460', '0001', 'DUKE POINT U/P - CEDAR RD (N END)', 'N', 1.94)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0461', '0001', 'CEDAR RD (N END) - DUKE POINT U/P', 'S', 1.95)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0467', '0001', 'STEWART AVE: TERMINAL AVE - BRECHIN RD (DEPT.BAY)', 'N', 2.02)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0503', '0001', 'TAYLOR WAY - EAGLE RIDGE I/C', 'W', 10.67)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0504', '0001', 'EAGLE RIDGE I/C - TAYLOR WAY', 'E', 10.94)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0509', '0901', 'MAIN ST: MOUNTAIN HWY - SEYMOUR RIVER BRIDGE', 'E', 0.72)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0511', '0001', 'EAGLE RIDGE I/C - HORSESHOE BAY', 'W', 1.31)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0512', '0001', 'HORSESHOE BAY - EAGLE RIDGE I/C', 'E', 1.82)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0513', '0901', 'RAMP FROM HWY 1 W/B TO HORSESHOE BAY VILLAGE', 'N', 1.43)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0514', '0001', 'TAYLOR WAY - RTE 7 (LOUGHEED HWY)', 'E', 14.41)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0515', '0001', 'RTE 7 (LOUGHEED HWY) - TAYLOR WAY', 'W', 14.47)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0516', '0001', 'LOUGHEED HWY (HWY 7) - 176 ST (HWY 15)', 'E', 25.91)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0517', '0001', '176 ST (HWY 15) - LOUGHEED HWY (HWY 7)', 'W', 25.87)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0518', '0001', '176 ST (HWY 15) - 264 ST (HWY 13)', 'E', 19.84)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0519', '0001', '264 ST (HWY 13) - 176 ST (HWY 15)', 'W', 19.84)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0520', '0001', '264 ST (HWY 13) - SUMAS WAY (HWY 11)', 'E', 18.66)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0521', '0001', 'SUMAS WAY (HWY 11) - 264 ST (HWY 13)', 'W', 18.66)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0522', '0001', 'SUMAS WAY (HWY 11) - BRIDAL FALLS U/P (HWY 9)', 'E', 43.22)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0523', '0001', 'BRIDAL FALLS U/P (HWY 9) - SUMAS WAY (HWY 11)', 'W', 43.2)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0526', '0001', 'BRIDAL FALLS U/P (HWY 9) - RTE 3 (HOPE)', 'E', 35.02)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0527', '0001', 'RTE 3 (HOPE) - BRIDAL FALLS U/P (HWY 9)', 'W', 35.23)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0602', '0901', 'CHANCELLOR BLVD: DRUMMOND DR - NW MARINE DR', 'W', 2.7)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0620', '0901', 'MARINE DR @ UBC: 41 AVE - SPANISH BANKS PARKING', 'W', 9.67)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0640', '0901', '16TH AVE: BLANCA ST - SW MARINE DR', 'W', 2.45)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0660', '0901', 'UNIVERSITY BLVD: BLANCA ST - WESTBROOK MALL', 'W', 2.35)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0670', '0901', 'HORNE ST CONNECTOR: HWY 11 - HWY 7', 'E', 2.1)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0671', '0901', 'HORNE ST CONNECTOR: HWY 7 - HWY 11', 'W', 2.0)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0691', '0901', 'COLUMBIA VALLEY HWY: HENDERSON - CHILLIWACK', 'N', 17.65)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0694', '0901', 'OLD RTE 3: RTE 1 JCT - RTE 3 JCT (EAST HOPE)', 'E', 2.55)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0781', '0013', 'RTE 13 (264 ST): US BORDER - RTE 1A', 'N', 6.56)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0782', '0013', 'RTE 13 (264 ST): RTE 1A - RTE 1 (56 AVE NORTH)', 'N', 4.93)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0785', '001A', 'FRASER HWY: RTE 15 - RTE 10', 'E', 5.24)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0786', '001A', 'FRASER HWY: RTE 10 - 208TH ST', 'E', 2.65)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0787', '001A', 'FRASER HWY: 208TH ST - RTE 13', 'E', 11.98)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0798', '0001', 'RTE 1/3 SPLIT AT EXIT 170 - JCTN OLD RTE 3 (HOPE)', 'N', 0.64)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0799', '0001', 'JCTN OLD RTE 3 (HOPE) - RTE 1/3 MERGE', 'S', 0.38)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0810', '0007', 'RTE 7 E/B THROUGH CAPE HORN INTERCHANGE', 'E', 3.14)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0811', '0007', 'RTE 7 W/B THROUGH CAPE HORN INTERCHANGE', 'W', 3.1)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0901', '0907', 'CORNWALL RD: RTE 1 - RTE 97C ASHCROFT', 'E', 4.85)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0904', '0012', 'LYTTON - LILLOOET', 'N', 61.9)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0907', '0099', 'LILLOOET - CACHE CREEK', 'N', 74.73)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0913', '097C', 'HIGHLAND VALLEY RD: LOGAN LAKE - ASHCROFT', 'N', 57.12)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0914', '097D', 'MEADOW CREEK RD: LOGAN LAKE - LAC LE JEUNE RD', 'E', 27.84)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0919', '097C', 'ASHCROFT - RTE 1 (NORTH)', 'N', 5.99)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0923', '0906', 'LAC LE JEUNE RD: MEADOW CREEK RD - KAMLOOPS', 'N', 16.15)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0926', '0906', 'HWY 1 E/B EXIT 369  - NOTRE DAME DR IN KAMLOOPS', 'N', 0.7)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0927', '0906', 'NOTRE DAME DR IN KAMLOOPS - HWY 1 W/B', 'S', 0.49)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0928', '0906', 'BATTLE ST: COLUMBIA ST - HWY 1 E/B', 'E', 0.93)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0929', '0906', 'BATTLE ST: HWY 1 W/B EXIT 375 - COLUMBIA ST', 'W', 0.86)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0930', '0001', 'JCT OLD ROUTE 3 - ROUTE 12 AT LYTTON', 'E', 108.46)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0932', '0001', 'LYTTON - SPENCES BRIDGE', 'E', 35.6)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0934', '0001', 'SPENCES BRIDGE - JCTN RTE 97C (N ASHCROFT ACCESS)', 'E', 45.06)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0936', '0001', 'JCTN RTE 97C (N ASHCROFT ACCESS) - CACHE CREEK', 'E', 4.18)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0938', '0001', 'CACHE CREEK - JCT RTE 5 (AFTON) KAMLOOPS', 'E', 71.99)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('0944', '0905', 'SQUILAX-ANGLEMONT RD: RTE 1 - SEYMOUR ARM', 'E', 47.28)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1100', '0029', 'TUMBLER RIDGE - CHETWYND', 'N', 93.62)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1101', '0029', 'CHETWYND - HUDSON''S HOPE', 'N', 65.2)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1103', '0052', 'HERITAGE HWY #52: ARRAS - TUMBLER RIDGE', 'S', 98.51)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1104', '0052', 'TUMBLER RIDGE - TUPPER', 'E', 144.4)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1106', '0908', 'ROLLA RD / CLAYHURST RD: DAWSON CREEK - GOODLOW', 'N', 81.57)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1108', '0029', 'HUDSON''S HOPE - ALASKA HWY RTE 97', 'N', 73.05)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1112', '0910', 'KEEFE''S LANDING RD: FRANCOIS LAKE - OOTSA LAKE', 'S', 38.63)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1127', '0905', 'SALMON RIVER ROAD: RTE 97 - SALMON ARM', 'N', 22.5)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1131', '0097', 'CACHE CREEK - 100 MILE HOUSE', 'N', 113.15)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1141', '0097', '100 MILE HOUSE - WILLIAMS LAKE', 'N', 89.71)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1146', '0097', 'WILLIAMS LAKE - QUESNEL', 'N', 124.3)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1151', '0097', 'QUESNEL - PRINCE GEORGE', 'N', 114.11)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1152', '0907', 'CANIM-HENDRIX LAKE RD: 100 MILE - EAGLE CREEK RD', 'E', 42.58)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1153', '0907', 'HORSE LAKE ROAD: 100 MILE HOUSE - RTE 24', 'E', 34.51)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1156', '0909', 'OLD CARIBOO HWY: RTE 97 - PRINCE GEORGE BNDRY', 'N', 6.4)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1157', '0097', 'PRINCE GEORGE - RTE 39 (PARSNIP RIVER)', 'N', 156.38)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1161', '0097', 'JCT RTE 39 (PARSNIP RIVER) - CHETWYND', 'N', 148.12)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1164', '0039', 'PARSNIP RIVER - MACKENZIE', 'N', 36.33)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1172', '0097', 'CHETWYND - DAWSON CREEK', 'N', 99.83)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1173', '0908', 'ROSE PRAIRIE RD: FORT ST JOHN - CECIL LAKE RD', 'N', 2.41)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1174', '0908', 'ROSE PRAIRIE RD: CECIL LAKE RD - 264 RD', 'N', 32.85)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1179', '0908', 'HUDSON''S HOPE - BENNETT DAM', 'W', 19.25)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1187', '0077', 'RTE 77 LIARD HWY: RTE 97 - NWT BORDER', 'N', 137.82)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1188', '0097', 'HWY 97: DIP INTO BC FROM YUKON,  PAST SWAN LAKE', 'W', 64.39)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1189', '0908', 'CECIL LAKE ROAD: ROSE PRAIRIE RD - ALTA BORDER', 'E', 61.32)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1197', '0049', 'DAWSON CREEK - ALBERTA', 'E', 15.24)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1200', '0097', 'DAWSON CREEK - FORT ST JOHN', 'N', 71.64)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1203', '0097', 'ALASKA HWY: FORT ST JOHN 100 ST - RTE 29', 'N', 12.51)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1204', '0097', 'ALASKA HWY: RTE 29 - RTE 77', 'N', 396.53)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1205', '0097', 'ALASKA HWY: RTE 77 - BC/YUKON BOUNDARY', 'N', 473.82)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1210', '0097', 'US BORDER - OSOYOOS', 'N', 4.5)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1212', '0097', 'OSOYOOS - KALEDEN (JCT 3A)', 'N', 47.17)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1214', '0097', 'KALEDEN (JCT 3A) - DROUGHT HILL (JCT 97C)', 'N', 57.34)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1218', '0097', 'JCT #97C (DROUGHT HILL I/C) - JCT #33 (KELOWNA)', 'N', 23.3)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1219', '0097', 'JCT #33 (KELOWNA) - JCT #97C (DROUGHT HILL I/C)', 'S', 23.21)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1221', '0097', 'KELOWNA - VERNON', 'N', 46.66)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1225', '097A', 'SWAN LAKE JCT - RTE 97B (TO SALMON ARM)', 'N', 32.36)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1226', '0097', 'VERNON - SWAN LAKE JCT', 'N', 9.89)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1228', '0097', 'SWAN LAKE JCT - MONTE CREEK', 'N', 80.46)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1229', '097A', 'RTE 97B - SICAMOUS', 'N', 32.87)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1235', '097B', 'RTE 97A - SALMON ARM', 'N', 14.43)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1280', '0905', 'EASTSIDE RD: OKANAGAN FALLS - PENTICTON', 'N', 9.26)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1290', '0905', 'PELMEWASH PARKWAY', 'N', 7.9)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1292', '0905', 'WESTSIDE RD: WEST KELOWNA - SPALLUMCHEEN', 'N', 65.43)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1294', '0905', 'CHASE-FALKLAND RD: FALKLAND TO CHASE', 'N', 43.35)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1303', '0003', 'OTHELLO I/C - NICOLUM PARK ACCESS', 'E', 1.57)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1304', '0003', 'NICOLUM PARK ACCESS - OTHELLO I/C', 'W', 2.07)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1316', '003A', 'KALEDEN SPUR', 'N', 0.15)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1317', '003A', 'KEREMEOS - KALEDEN JCT', 'E', 31.64)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1321', '0904', 'USA BORDER - RTE 3 (MIDWAY)', 'E', 1.94)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1324', '0033', 'ROCK CREEK - RUTLAND', 'N', 128.82)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1343', '0022', 'PATERSON - ROSSLAND', 'N', 10.51)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1376', '0021', 'PORTHILL - CRESTON', 'N', 14.12)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1378', '0901', '1ST AVE I/C: RTE 1 E/B - RUPERT ST & 1ST AVE', 'E', 0.65)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1390', '0901', '1ST AVE I/C RAMP: 1ST AVE - RTE 1 W/B', 'W', 0.33)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1391', '0901', '1ST AVE I/C RAMP: 1ST AVE - RTE 1 E/B', 'E', 0.24)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1392', '0901', '1ST AVE I/C RAMP: RTE 1 W/B - 1ST AVE', 'W', 0.25)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1398', '0043', 'SPARWOOD - ELKFORD', 'N', 34.85)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1399', '0903', 'FORDING MINE RD: HWY 43 - END OF PUBLIC RD', 'N', 24.67)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1401', '0003', 'CASTLEGAR - MEADOWS JCT', 'E', 27.83)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1403', '0003', 'MEADOWS JCT - SALMO', 'E', 10.36)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1411', '0003', 'SALMO - NELWAY JCT', 'E', 14.13)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1418', '0905', 'NIGHTHAWK ROAD: USA BORDER - RTE 3', 'N', 2.91)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1421', '0003', 'NELWAY JCT - CRESTON', 'E', 66.19)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1426', '0041', 'US BORDER (DANVILLE) - GRAND FORKS WEST', 'N', 1.29)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1428', '0395', 'LAURIER - CHRISTINA LAKE', 'N', 4.06)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1435', '003B', 'RTE 3 (NANCY GREENE LAKE) - RTE 22 (ROSSLAND)', 'S', 28.17)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1436', '0022', 'ROSSLAND - JCTN RTE 3B/RTE 22 (WARFIELD)', 'E', 9.71)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1438', '003B', 'JCTN RTE 3B/22 (WARFIELD) - WANETA JCTN (TRAIL)', 'E', 7.31)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1441', '0003', 'CRESTON - RTE 95 CURZON (YAHK)', 'E', 39.96)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1451', '0003', 'RTE 95 CURZON (YAHK) - CRANBROOK', 'E', 72.14)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1455', '0903', 'WARDNER - FORT STEELE RD', 'N', 29.72)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1456', '0003', 'CRANBROOK -  FORT STEELE JCT', 'E', 5.38)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1461', '0003', 'FORT STEELE JCT - ELKO', 'E', 55.63)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1471', '0003', 'ELKO - SPARWOOD', 'E', 61.68)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1476', '0003', 'SPARWOOD - ALBERTA', 'E', 19.4)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1480', '022A', 'US BORDER - WANETA JCT', 'N', 11.14)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1481', '003B', 'WANETA JCTN (TRAIL) - MEADOWS JCT (RTE 3)', 'E', 23.24)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1489', '0022', 'TRAIL - CASTLEGAR', 'N', 26.02)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1500', '0016', 'MASSET - SKIDEGATE', 'S', 101.03)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1506', '0911', 'SKIDEGATE ONE-WAY:FERRY RAMP - HWY 16/ROAD 33 INT', 'W', 0.41)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1507', '0911', 'ALLIFORD BAY ROAD: FERRY TERMINAL - SANDSPIT', 'E', 14.26)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1509', '0911', 'PORT EDWARD ROAD: RTE 16-END OF RD(CASSIAR CANNRY)', 'S', 13.87)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1512', '0911', 'OCEANVIEW DR: SKIDEGATE - QUEEN CHARLOTTE CITY', 'W', 7.95)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1516', '0037', 'KITIMAT - TERRACE', 'N', 57.66)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1519', '0062', 'HIGH LEVEL RD: NEW HAZELTON - HAZELTON', 'W', 7.35)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1531', '0113', 'NISGA''A HIGHWAY: TERRACE - NEW AIYANSH', 'N', 96.16)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1532', '0113', 'VETTER RD: S TO NE CORNERS OF NEW AIYANSH TRIANGLE', 'W', 2.29)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1534', '0113', 'NISGA''A HWY: NASS CAMP - NEW AIYANSH', 'W', 12.38)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1536', '0113', 'NISGA''A HIGHWAY: NEW AIYANSH - GINGOLX', 'W', 72.39)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1544', '0118', 'BABINE LAKE ROAD: RTE 16 (TOPLEY) - GRANISLE', 'N', 48.86)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1549', '0035', 'BURNS LAKE - FRANCOIS LAKE FERRY', 'S', 23.34)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1552', '0907', 'LIKELY RD: RTE 97 - LIKELY', 'N', 82.82)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1553', '0907', 'HORSEFLY ROAD: LIKELY RD - QUESNEL LAKE RD', 'E', 46.96)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1555', '0907', 'CHILCOTIN-MELDRUM RD: HWY 20 - BUCKSKIN RD', 'N', 39.8)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1556', '0907', 'WEST FRASER RD: BUCKSKIN RD - QUESNEL', 'N', 86.52)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1557', '0907', 'BLACKWATER ROAD: QUESNEL - NAZKO RD', 'N', 6.68)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1558', '0907', 'BLACKWATER ROAD: NAZKO RD - HWY 16', 'N', 130.1)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1559', '0907', 'NAZKO ROAD', 'W', 131.84)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1561', '0016', 'VANDERHOOF - PRINCE GEORGE', 'E', 96.63)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1562', '0909', 'BRAESIDE RD: RTE 27 -WESTWOOD RD', 'N', 13.0)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1566', '0027', 'VANDERHOOF - FT ST JAMES', 'N', 61.14)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1573', '0016', 'CITY OF PRINCE GEORGE', 'E', 9.34)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1578', '0909', 'UPPER FRASER ROAD: RTE 16 - NORTH FRASER FSR', 'E', 62.93)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1582', '0016', 'PRINCE GEORGE - DOME CREEK', 'E', 117.03)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1584', '0016', 'DOME CREEK - TETE JAUNE', 'E', 148.71)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1586', '0016', 'TETE JAUNE - ALBERTA', 'E', 76.77)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1640', '0016', 'PRINCE RUPERT - TERRACE', 'E', 145.91)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1642', '0016', 'CITY OF TERRACE', 'E', 4.6)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1644', '0016', 'TERRACE - KITWANGA', 'E', 90.59)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1646', '0016', 'KITWANGA - NEW HAZELTON', 'E', 43.04)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1648', '0016', 'NEW HAZELTON - HOUSTON', 'E', 131.02)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1650', '0016', 'HOUSTON - TOPLEY', 'E', 29.89)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1652', '0016', 'TOPLEY - BURNS LAKE', 'E', 51.3)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1654', '0016', 'BURNS LAKE - VANDERHOOF', 'E', 127.53)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1700', '005A', 'RTE 3 (PRINCETON) - RTE 97C (ASPEN GROVE)', 'N', 62.53)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1712', '0008', 'COLDWATER I/C MERRITT JCT #5 - JCT 8/97C', 'N', 9.01)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1716', '0008', 'JCTN RTE 97C (MAMIT LAKE ROAD) - SPENCES BRIDGE', 'N', 60.31)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1717', '097C', 'MAMIT LAKE ROAD: LOWER NICOLA - LOGAN LAKE', 'N', 41.89)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1721', '005A', 'NICOLA I/C MERRITT -  KAMLOOPS', 'N', 84.15)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1741', '0005', 'JCT RTE 1 KAMLOOPS - LITTLEFORT', 'N', 93.59)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1750', '0024', '93 MILE HOUSE - LITTLEFORT', 'E', 97.5)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1761', '0005', 'LITTLEFORT - AVOLA', 'N', 97.25)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1766', '0906', 'OLD NORTH THOMPSON HWY: BLACKPOOL - CLEARWATER', 'N', 6.7)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1771', '0906', 'HALSTON CONNECTOR: HALSTON BRIDGE - HWY 5', 'E', 2.15)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1776', '0906', 'HEFFLEY LOUIS CREEK RD: KAMLOOPS - SUN PEAKS', 'E', 29.11)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1777', '0906', 'PAUL LAKE ROAD', 'E', 11.89)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1778', '0906', 'PINANTAN - PRITCHARD ROAD', 'E', 33.4)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1781', '0005', 'AVOLA - TETE JAUNE', 'N', 148.2)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1801', '005A', 'RTE 5A/97C (ASPEN GROVE) - COLDWATER I/C (MERRITT)', 'N', 23.47)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1810', '0001', 'SALMON ARM - SICAMOUS', 'E', 26.56)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1812', '0001', 'SICAMOUS - REVELSTOKE', 'E', 70.71)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1814', '0001', 'REVELSTOKE - GLACIER PARK', 'E', 48.02)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1816', '0001', 'WEST GLACIER PARK - EAST GLACIER PARK', 'E', 43.95)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1818', '0001', 'GLACIER PARK - GOLDEN', 'E', 55.83)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1822', '0001', 'GOLDEN - YOHO PARK', 'E', 25.27)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1823', '0001', 'YOHO PARK - GOLDEN', 'W', 25.26)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1829', '0001', 'YOHO PARK - ALBERTA', 'E', 45.62)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1906', '0006', 'NELWAY - NELWAY JCT (HWY 3)', 'N', 10.4)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1921', '0006', 'SALMO - NELSON', 'N', 40.41)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1922', '0006', 'NELSON - SOUTH SLOCAN', 'W', 21.3)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1941', '0006', 'SOUTH SLOCAN - NEW DENVER', 'N', 77.8)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1947', '0006', 'NEW DENVER - NAKUSP', 'N', 47.03)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1949', '031A', 'NEW DENVER - KASLO', 'E', 46.45)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1951', '0006', 'NAKUSP - NEEDLES FERRY', 'W', 58.79)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1953', '0023', 'NAKUSP - GALENA BAY', 'N', 46.74)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1954', '0031', 'BALFOUR - KASLO', 'N', 35.79)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1956', '0031', 'KASLO - GALENA BAY', 'N', 139.58)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1961', '0006', 'NEEDLES FERRY - LUMBY', 'W', 109.19)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1963', '003A', 'NELSON - BALFOUR', 'E', 34.35)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1972', '0006', 'LUMBY - VERNON', 'W', 25.47)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1973', '003A', 'KOOTENAY BAY - CRESTON', 'E', 78.03)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1974', '0023', 'SHELTER BAY - REVELSTOKE', 'N', 48.99)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1977', '0023', 'REVELSTOKE - MICA DAM', 'N', 150.56)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('1985', '003A', 'OOTISCHENIA (CASTLEGAR) - SOUTH SLOCAN', 'E', 19.75)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2026', '0901', 'I/C: KNIGHT ST S/B - ROUTE 91 E/B', 'E', 1.08)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2027', '0901', 'I/C: ROUTE 91 E/B - KNIGHT ST N/B', 'E', 1.09)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2028', '0901', 'I/C: KNIGHT ST S/B - ROUTE 91 W/B', 'S', 0.48)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2029', '0901', 'I/C: ROUTE 91 W/B - KNIGHT ST N/B', 'W', 0.4)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2032', '097C', 'ASPEN GROVE - PEACHLAND', 'E', 82.69)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2033', '097C', 'PEACHLAND - ASPEN GROVE', 'W', 82.33)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2052', '0001', 'E/B: JCT RTE 5 (AFTON) - JCT RTE 5A (ABERDEEN)', 'E', 6.62)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2057', '0001', 'W/B: JCT RTE 5A (ABERDEEN) - JCT RTE 5 (AFTON)', 'W', 6.64)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2062', '0001', 'E/B: JCT RTE 5A(ABERDEEN) - JCT RTE 5(YELLOWHEAD)', 'E', 5.35)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2067', '0001', 'W/B: JCT RTE 5(YELLOWHEAD) - JCT RTE 5A(ABERDEEN)', 'W', 5.37)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2072', '0001', 'JCT RTE 5 (YELLOWHEAD) - JCT RTE 97 (MONTE CREEK)', 'E', 26.07)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2073', '0001', 'JCT RTE 97 (MONTE CREEK) - JCT RTE 5 (YELLOWHEAD)', 'W', 26.01)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2079', '0001', 'MONTE CREEK - SALMON ARM', 'E', 85.16)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2090', '0005', 'OTHELLO I/C HOPE - COLDWATER U/P MERRITT', 'N', 109.32)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2091', '0005', 'COLDWATER U/P MERRITT - OTHELLO I/C HOPE', 'S', 109.94)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2092', '0005', 'COLDWATER U/P MERRITT - NICOLA U/P MERRITT', 'N', 3.97)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2093', '0005', 'NICOLA U/P MERRITT - COLDWATER U/P MERRITT', 'S', 3.99)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2094', '0005', 'NICOLA U/P MERRITT - AFTON U/P KAMLOOPS', 'N', 72.26)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2095', '0005', 'AFTON U/P KAMLOOPS - NICOLA U/P MERRITT', 'S', 72.12)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2106', '0095', 'KINGSGATE - CURZON (YAHK)', 'N', 11.3)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2111', '0093', 'ROOSVILLE - ELKO', 'N', 36.95)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2116', '095A', 'CRANBROOK - WASA', 'N', 55.48)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2136', '0093', 'FORT STEELE JCT - WASA', 'N', 31.79)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2141', '0093', 'WASA - RADIUM', 'N', 102.61)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2143', '0903', 'WESTSIDE RD: RTE 93/95 - INVERMERE', 'N', 22.55)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2150', '0093', 'RADIUM - KOOTENAY PARK', 'N', 1.27)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2156', '0093', 'KOOTENAY PARK - ALBERTA', 'N', 92.86)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2161', '0095', 'RADIUM - GOLDEN', 'N', 105.35)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2201', '0003', 'RTE 1 - OTHELLO I/C', 'E', 6.64)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2202', '0003', 'OTHELLO I/C - RTE 1', 'W', 6.0)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2206', '0003', 'NICOLUM PARK ACCESS - PRINCETON', 'E', 124.79)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2211', '0003', 'PRINCETON - KEREMEOS', 'E', 67.21)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2221', '0003', 'KEREMEOS - OSOYOOS', 'E', 46.13)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2223', '0003', 'OSOYOOS - ROCK CREEK', 'E', 51.68)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2225', '0003', 'ROCK CREEK - CARSON', 'E', 69.01)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2227', '0003', 'CARSON - CHRISTINA LAKE', 'E', 23.55)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2229', '0003', 'CHRISTINA LAKE - NANCY GREENE LAKE', 'E', 49.56)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2231', '0003', 'NANCY GREENE LAKE - CASTLEGAR', 'E', 25.89)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2300', '0004', 'JCT 19 (QUALICUM) - JCT 4A (COOMBS)', 'W', 2.9)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2301', '0019', 'DUKE POINT HWY: HWY 1 O/P - DUKE PT FERRY TERMINAL', 'E', 8.07)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2302', '0019', 'DUKE POINT HWY: DUKE PT FERRY TERMINAL - HWY 1 O/P', 'W', 8.05)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2307', '0902', 'RAMP: HWY 1 S/B - DUKE POINT HWY E/B', 'S', 0.89)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2308', '0902', 'RAMP: DUKE POINT HWY W/B - HWY 1 N/B', 'N', 0.7)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2317', '019A', 'BRECHIN RD - HWY 19/19A JUNCTION (LANTZVILLE)', 'N', 9.79)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2318', '0019', 'JCT 19A (LANTZVILLE) - JCT 19A (CRAIG''S X)', 'N', 17.05)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2319', '0019', 'JCT 19A (CRAIG''S X) - JCT 19A (LANTZVILLE)', 'S', 17.06)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2320', '0028', 'CAMPBELL RIVER - GOLD RIVER', 'W', 88.06)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2322', '0019', 'JCT 19A (CRAIG''S X) - JCT 4A (PARKSVILLE)', 'N', 5.55)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2323', '0019', 'JCT 4A (PARKSVILLE) - JCT 19A (CRAIG''S X)', 'S', 5.55)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2324', '0019', 'JCT 4A ( PARKSVILLE) - JCT 4 (QUALICUM)', 'N', 8.92)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2325', '0019', 'JCT 4 (QUALICUM) - JCT 4A (PARKSVILLE)', 'S', 8.9)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2326', '0019', 'JCT 4 (QUALICUM) - BUCKLEY BAY RD', 'N', 40.24)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2327', '0019', 'BUCKLEY BAY RD - JCT 4 (QUALICUM)', 'S', 40.27)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2328', '0019', 'BUCKLEY BAY RD - COMOX VALLEY PARKWAY', 'N', 16.71)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2329', '0019', 'COMOX VALLEY PARKWAY - BUCKLEY BAY RD', 'S', 16.7)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2331', '0902', 'COMOX VALLEY PARKWAY: HWY 19 - HWY 19A', 'E', 5.72)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2332', '0019', 'COMOX VALLEY PARKWAY - JUBILEE PARKWAY', 'N', 43.41)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2333', '0019', 'JUBILEE PARKWAY - COMOX VALLEY PARKWAY', 'S', 43.42)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2334', '0019', 'JUBILEE PARKWAY NORTH - JCT 19A', 'N', 9.02)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2335', '0019', 'JCT RTE 28/19A - JUBILEE PARKWAY', 'S', 9.01)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2336', '0902', 'ROYSTON RD: ROYSTON - CUMBERLAND', 'W', 4.39)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2358', '004A', 'JCT 19 THROUGH COOMBS - JCT 4', 'W', 9.67)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2364', '0902', 'JUBILEE PARKWAY: HWY 19 - HWY 19A', 'E', 4.62)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2367', '019A', 'JUNCTION 19 N/B - JUNCTION 28/19 S/B', 'N', 0.14)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2375', '0019', 'WOODBURN RD (CAMPBELL R.) - SAYWARD RD', 'N', 63.06)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2376', '0902', 'BUCKLEY BAY CONNECTOR: HWY 19 - HWY 19A', 'E', 1.06)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2377', '0902', 'PORT MCNEILL ACCESS: RTE 19 - PORT MCNEILL FERRY', 'N', 2.94)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2378', '0019', 'JUNCTION 19A - WOODBURN RD', 'N', 0.7)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2379', '0019', 'WOODBURN RD - JUNCTION 28/19A', 'S', 0.69)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2381', '0019', 'SAYWARD RD - BEAVER COVE ROAD', 'N', 121.65)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2382', '0004', 'JCT 4A (COOMBS) - PORT ALBERNI', 'W', 38.24)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2383', '0004', 'PORT ALBERNI - UCLUELET JUNCTION', 'W', 87.8)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2385', '0004', 'UCLUELET JUNCTION - TOFINO', 'W', 32.88)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2387', '0902', 'SAYWARD RD: RTE 19 - KELSEY BAY WHARF', 'N', 12.28)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2388', '0902', 'UCLUELET RD: RTE 4 - UCLUELET GOVT WHARF', 'S', 7.98)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2391', '0902', 'BEAVER COVE ROAD', 'E', 10.52)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2392', '0019', 'BEAVER COVE ROAD - HWY 30', 'N', 26.86)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2393', '0019', 'HWY 30 - DOUGLAS ST', 'N', 16.29)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2394', '0019', 'DOUGLAS ST - BEAR COVE FERRY', 'N', 4.65)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2398', '0902', 'DOUGLAS ST: RTE 19 - HOLBERG RD (PORT HARDY)', 'W', 2.1)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2399', '0030', 'PORT ALICE ROAD:  RTE 19 - PT ALICE', 'S', 36.59)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2401', '0902', 'JCT RTE 1/DELOUME RD - MILL BAY FERRY ACCESS RD', 'S', 5.22)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2402', '0902', 'MILL BAY FERRY ACCESS RD - MILL BAY FERRY TERMINAL', 'W', 0.3)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2515', '099A', '120 M NORTH OF CRESCENT RD - 40TH AVE', 'N', 1.11)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2520', '099A', '8TH AVE - N/B ENTRANCE FROM HWY 99 S/B', 'N', 0.61)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2541', '0901', 'MCGILL ST I/C: MCGILL ST E/B - HWY 1 E/B', 'E', 0.29)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2542', '0901', 'MCGILL ST I/C: MCGILL ST E/B - HWY 1 W/B', 'E', 0.84)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2543', '0901', 'MCGILL ST I/C: HWY 1 E/B - MCGILL ST W/B', 'W', 0.72)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2544', '0901', 'MCGILL ST I/C: HWY 1 W/B - MCGILL ST W/B', 'N', 0.63)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2545', '0901', 'CASSIAR CONN SB: HWY 1 EB - E HASTINGS - HWY 1 EB', 'S', 1.37)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2546', '0901', 'CASSIAR CONN NB: HWY 1 WB - E HASTINGS - HWY 1 WB', 'N', 1.5)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2560', '0901', 'PORT MELLON HWY: PORT MELLON - HWY 101 (LANGDALE)', 'S', 11.61)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2561', '0101', 'LANGDALE FERRY SPUR', 'W', 0.08)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2563', '0901', 'MARINE DRIVE: LANGDALE - GIBSONS TOWN BNDRY', 'S', 3.74)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2567', '0101', 'GIBSONS BYPASS (HWY 101): LANGDALE - GIBSONS', 'W', 4.81)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2568', '0101', 'GIBSONS - EARLS COVE', 'N', 75.51)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2574', '0901', 'MADEIRA PARK SPUR: RTE 101 - MADEIRA PK FED WHARF', 'N', 0.74)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2576', '0901', 'COMOX FERRY SPUR (WHARF ST)', 'W', 0.14)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2581', '0101', 'SALTERY BAY - LUND', 'W', 58.35)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2601', '0026', 'QUESNEL - BARKERVILLE', 'E', 81.09)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2620', '019A', 'JCT 19 (CRAIG''S X) - PARKSVILLE', 'N', 5.42)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2621', '019A', 'PARKSVILLE - BUCKLEY BAY RD', 'N', 50.31)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2622', '019A', 'BUCKLEY BAY - S.CTNY CONNECTOR (29TH ST.)', 'N', 19.71)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2623', '019A', '29TH ST (COURTENAY) - JUBILEE PKWAY(CAMPBELL R.)', 'N', 37.87)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2624', '019A', 'JUBILEE PARKWAY - JUNCTION 19 N/B (TAMARAC)', 'N', 12.45)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2716', '007B', 'UNITED BLVD ONTO MARY HILL BYPASS: COQ - PT COQ', 'E', 8.71)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2717', '007B', 'MARY HILL BYPASS ONTO UNITED BLVD: PT COQ - COQ', 'W', 8.69)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2722', '0007', 'OTTAWA ST - DEWDNEY TRUNK RD', 'E', 7.19)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2723', '0007', 'DEWDNEY TRUNK RD - OTTAWA ST', 'W', 7.19)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2728', '0007', 'DEWDNEY TRUNK RD - HWY 11 (MISSION)', 'E', 28.53)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2736', '0007', 'HWY 11 - MERGE N RAILWAY AVE (MISSION)', 'E', 3.16)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2737', '0007', 'MERGE N RAILWAY AVE (MISSION) - HWY 11', 'W', 3.13)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2738', '0007', 'MISSION - RTE 9 (HOT SPRINGS RD)', 'E', 45.67)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2739', '0007', 'RTE 9 (HOT SPRINGS RD) - RTE 9 (EVERGREEN DR)', 'E', 1.55)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2740', '0011', 'HUNTINGDON CUSTOMS - RTE 1, ABBOTSFORD', 'N', 3.44)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2752', '0901', 'AGASSIZ BYPASS: HWY 9 - HWY 7', 'N', 3.61)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2756', '0007', 'RTE 9 (EVERGREEN DR) - RTE 1 AT HAIG', 'E', 30.42)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2761', '0009', 'BRIDAL FALLS - AGASSIZ', 'N', 7.7)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2765', '0009', 'AGASSIZ - HARRISON HOT SPRINGS', 'N', 6.4)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2772', '0011', 'RTE 1(ABBOTSFORD) - N JCT BYPASS (GLADYS AVE)', 'N', 3.71)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2773', '0011', 'N JCT BYPASS(GLADYS AVE) - RTE 1(ABBOTSFORD)', 'S', 3.7)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2776', '0011', 'N JCT BYPASS (GLADYS AVE) - RTE 7 (MISSION)', 'N', 9.92)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2777', '0011', 'RTE 7 (MISSION) - N JCT BYPASS (GLADYS AVE)', 'S', 9.93)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2822', '091A', 'RTE 91 - QUEENSBOROUGH INTERCHANGE', 'N', 3.53)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2823', '091A', 'QUEENSBOROUGH INTERCHANGE - RTE 91', 'S', 4.13)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2840', '0901', '91A CONNECTOR - CLIVEDEN AVE (ANNACIS ISLAND)', 'S', 1.23)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2900', '0099', 'BLAINE - VANCOUVER', 'N', 40.92)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2901', '0099', 'VANCOUVER - BLAINE', 'S', 40.9)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2923', '0901', 'SEA ISLAND WAY: OAK ST - NO 3 RD', 'W', 0.95)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2924', '0901', 'HORSESHOE BAY DR: HORSESHOE BAY - JCT RTE 99', 'N', 2.68)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2926', '0099', 'STANLEY PARK CAUSEWAY (S END) - TAYLOR WAY - HWY 1', 'N', 6.13)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2929', '0099', 'TUNNEL POINT REST AREA - SQUAMISH', 'N', 29.08)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2935', '0907', 'LILLOOET - GOLD BRIDGE (ROAD 40)', 'W', 106.21)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2942', '0099', 'EAGLE RIDGE I/C - TUNNEL POINT REST AREA', 'N', 15.51)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2943', '0099', 'TUNNEL POINT REST AREA - EAGLE RIDGE I/C', 'S', 15.16)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2945', '0099', 'SQUAMISH - WHISTLER', 'N', 57.77)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2947', '0099', 'WHISTLER - MT CURRIE', 'N', 38.79)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('2948', '0099', 'MT CURRIE - LILLOOET', 'N', 91.81)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3002', '0091', 'ANNACIS:  RTE 99 - NORDEL I/C', 'N', 7.85)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3003', '0091', 'ANNACIS:  NORDEL I/C - RTE 99', 'S', 7.97)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3032', '0091', 'ANNACIS:  NORDEL I/C - JCT 91A', 'N', 3.9)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3033', '0091', 'ANNACIS:  JCT 91A - NORDEL I/C', 'S', 3.88)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3042', '0901', 'CONNECTOR: HWY 91 E/B - HWY 91A N/B', 'E', 2.5)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3046', '0091', 'RICHMOND FREEWAY: RTE 91A - RTE 99', 'W', 11.07)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3047', '0091', 'RICHMOND FREEWAY: RTE 99 - RTE 91A', 'E', 11.04)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3100', '0010', 'RTE 91 - RTE 15 CLOVERDALE', 'E', 12.55)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3101', '0010', 'RTE 15 CLOVERDALE - RTE 91', 'W', 12.55)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3114', '0010', 'RTE 15 CLOVERDALE - RTE 1A LANGLEY', 'E', 4.89)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3119', '0010', 'LANGLEY BYPASS: RTE 1A - GLOVER RD', 'E', 2.23)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3120', '0010', 'GLOVER RD:  LANGLEY BYPASS - SPRINGBROOK RD', 'E', 3.61)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3121', '0010', 'SPRINGBROOK ROAD - 72ND AVE', 'E', 3.31)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3130', '0017', 'TSAWWASSEN - 28 AVE', 'E', 6.86)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3131', '0017', '28 AVE - TSAWWASSEN', 'W', 7.05)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3144', '0901', 'GOLDEN EARS CONNECTOR', 'E', 2.36)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3146', '0901', 'HWY 91 CONNECTOR / NORDEL WAY E/B', 'E', 2.37)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3147', '0901', 'HWY 91 CONNECTOR / NORDEL WAY W/B', 'W', 2.37)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3152', '0017', 'SOUTH FRASER PERIMETER ROAD: 28 AVE - HWY 99', 'E', 6.27)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3153', '0017', 'SOUTH FRASER PERIMETER ROAD: HWY 99 - 28 AVE', 'W', 6.08)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3154', '0017', 'SOUTH FRASER PERIMETER ROAD: HWY 99 - 136 ST', 'E', 21.1)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3155', '0017', 'SOUTH FRASER PERIMETER ROAD: 136 ST - HWY 99', 'W', 21.13)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3156', '0017', 'SOUTH FRASER PERIMETER ROAD: 136 ST - HWY 1', 'E', 9.94)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3157', '0017', 'SOUTH FRASER PERIMETER ROAD: HWY 1 - 136 ST', 'W', 9.95)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3176', '017A', 'HWY 17 AT 28 AVE - HWY 99', 'N', 6.29)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3177', '017A', 'HWY 99 - HWY 17 AT 28 AVE', 'S', 6.09)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3180', '0015', 'DOUGLAS CUSTOMS - RTE 10', 'N', 11.29)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3188', '0901', '8 AVE: RTE 15 (176 ST) - KING GEORGE BLVD (99A)', 'W', 2.01)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3191', '0901', 'DELTAPORT WAY', 'E', 8.08)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3196', '0901', 'RAMP: DELTAPORT WAY E/B TO HWY 17 E/B', 'E', 0.53)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3197', '0901', 'RAMP: HWY 17 W/B TO DELTAPORT WAY W/B', 'W', 0.53)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3198', '0901', 'RAMP: DELTAPORT WAY E/B TO HWY 17A N/B', 'N', 0.64)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3199', '0901', 'RAMP: HWY 17A S/B TO DELTAPORT WAY W/B', 'S', 0.56)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3200', '0015', 'RTE 15 NB (176 ST): RTE 10 - RTE 1A', 'N', 3.87)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3201', '0015', 'RTE 15 SB (176 ST): RTE 1A - RTE 10', 'S', 3.87)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3202', '0015', 'RTE 15 NB (176 ST): RTE 1A - RTE 1', 'N', 4.85)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3203', '0015', 'RTE 15 SB (176 ST): RTE 1 - RTE 1A', 'S', 4.85)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3311', '0020', 'BELLA COOLA - ANAHIM', 'E', 138.33)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3321', '0020', 'ANAHIM - TATLA LAKE', 'E', 95.18)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3331', '0020', 'TATLA LAKE - ALEXIS CREEK', 'E', 109.55)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3341', '0020', 'ALEXIS CREEK - WILLIAMS LAKE', 'E', 111.88)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3600', '0910', 'TELEGRAPH CR RD: TELEGRAPH CR - TUYA RIVER BRIDGE', 'N', 36.74)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3601', '0910', 'TELEGRAPH CR RD: TUYA RIVER BRIDGE - DEASE LAKE', 'N', 75.0)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3613', '0910', 'ATLIN HWY: ATLIN - BC/YUKON BORDER', 'N', 50.99)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3711', '0037', 'KITWANGA - CRANBERRY JCT', 'N', 76.05)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3721', '0037', 'CRANBERRY JCT - MEZIADIN LAKE JCT', 'N', 80.73)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3726', '037A', 'GLACIER HWY: USA BDR - RTE 37 MEZIADIN LAKE', 'E', 65.07)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3731', '0037', 'MEZIADIN LAKE JCT - N BELL IRVING', 'N', 92.94)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3741', '0037', 'N BELL IRVING - BURRAGE RIVER', 'N', 83.24)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3751', '0037', 'BURRAGE RIVER - DEASE LAKE', 'N', 155.7)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3766', '0037', 'DEASE LAKE - CASSIAR RD', 'N', 115.94)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('3771', '0037', 'CASSIAR RD - BC/YUKON BORDER', 'N', 115.91)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('4021', '0002', 'ALBERTA - HWY 52', 'W', 2.07)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('4022', '0002', 'HWY 52 - HWY 49 (DAWSON CREEK)', 'W', 37.47)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('4023', '0002', 'HWY 49 (DAWSON CREEK) - HWY 97 (DAWSON CREEK)', 'W', 2.08)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('5006', '0019', 'NANAIMO PARKWAY NORTHBOUND', 'N', 19.18)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";

INSERT INTO "TAR"."lki_segment" ("code", "hwy_code", "description", "direction", "length_km")
VALUES ('5007', '0019', 'NANAIMO PARKWAY SOUTHBOUND', 'S', 18.88)
ON CONFLICT ("code")
DO UPDATE SET
    "hwy_code" = EXCLUDED."hwy_code",
    "description" = EXCLUDED."description",
    "direction" = EXCLUDED."direction",
    "length_km" = EXCLUDED."length_km";
               
               """)


def downgrade():
    op.execute("""
DELETE FROM "TAR"."lki_segment";
DELETE FROM "TAR"."lki_highway";               
                """)
