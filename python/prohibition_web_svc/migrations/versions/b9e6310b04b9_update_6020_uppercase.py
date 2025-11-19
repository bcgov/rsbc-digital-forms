"""update-6020-uppercase

Revision ID: b9e6310b04b9
Revises: 8fd77cf66929
Create Date: 2025-11-18 16:28:51.537056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9e6310b04b9'
down_revision = '8fd77cf66929'
branch_labels = None
depends_on = None


def upgrade():
    # add missing 98 pedestrian vehicle type
    op.execute('''
            INSERT INTO "TAR"."vehicle_type" (code, description)
            SELECT '98', 'PEDESTRIAN'
               WHERE NOT EXISTS (SELECT 1 FROM "TAR"."vehicle_type" WHERE code = '98');
    ''')
    op.execute('''
        UPDATE "TAR"."injury_classification" SET description = 'Apparently Deceased or Deceased' 
               WHERE code = '98';
    ''')

    # road_class
    op.execute('''
        UPDATE "TAR"."road_class" SET description = UPPER(description);
    ''')

    # traffic_flow
    op.execute('''
        UPDATE "TAR"."traffic_flow" SET description = UPPER(description);
    ''')

    # collision_location
    op.execute('''
        UPDATE "TAR"."collision_location" SET description = UPPER(description);
    ''')

    # speed_zone
    op.execute('''
        UPDATE "TAR"."speed_zone" SET description = UPPER(description);
        ''')

    # traffic_flow
    op.execute('''
        UPDATE "TAR"."traffic_flow" SET description = UPPER(description);
    ''')

    # collision_location
    op.execute('''
        UPDATE "TAR"."collision_location" SET description = UPPER(description);
    ''')

    # speed_zone
    op.execute('''
        UPDATE "TAR"."speed_zone" SET description = UPPER(description);
    ''')

    # traffic_flow
    op.execute('''
        UPDATE "TAR"."traffic_flow" SET description = UPPER(description);
    ''')

    # land_usage
    op.execute('''
        UPDATE "TAR"."land_usage" SET description = UPPER(description);
    ''')

    # road_type
    op.execute('''
        UPDATE "TAR"."road_type" SET description = UPPER(description);
    ''')

    # traffic_control
    op.execute('''
        UPDATE "TAR"."traffic_control" SET description = UPPER(description);
    ''')

    # roadway_character
    op.execute('''
        UPDATE "TAR"."roadway_character" SET description = UPPER(description);
    ''')

    # roadway_condition
    op.execute('''
        UPDATE "TAR"."roadway_condition" SET description = UPPER(description);
    ''')

    # weather_condition
    op.execute('''
        UPDATE "TAR"."weather_condition" SET description = UPPER(description);
    ''')

    # lighting_condition
    op.execute('''
        UPDATE "TAR"."lighting_condition" SET description = UPPER(description);
    ''')

    # type_of_collision
    op.execute('''
        UPDATE "TAR"."type_of_collision" SET description = UPPER(description);
    ''')

    # location_of_first_contact
    op.execute('''
        UPDATE "TAR"."location_of_first_contact" SET description = UPPER(description);
    ''')

    # primary_collision_occurrence
    op.execute('''
        UPDATE "TAR"."primary_collision_occurrence" SET description = UPPER(description);
    ''')

    # pedestrian_location
    op.execute('''
        UPDATE "TAR"."pedestrian_location" SET description = UPPER(description);
    ''')

    # pedestrian_action
    op.execute('''
        UPDATE "TAR"."pedestrian_action" SET description = UPPER(description);
    ''')

    # entity_type
    op.execute('''
        UPDATE "TAR"."entity_type" SET description = UPPER(description);
    ''')

    # contributing_factors
    op.execute('''
        UPDATE "TAR"."contributing_factors" SET description = UPPER(description), type = UPPER(type);
    ''')

    # damage_location
    op.execute('''
        UPDATE "TAR"."damage_location" SET description = UPPER(description);
    ''')

    # damage_severity
    op.execute('''
        UPDATE "TAR"."damage_severity" SET description = UPPER(description);
    ''')

    # pre_collision_action
    op.execute('''
        UPDATE "TAR"."pre_collision_action" SET description = UPPER(description);
    ''')

    # vehicle_type
    op.execute('''
        UPDATE "TAR"."vehicle_type" SET description = UPPER(description);
    ''')

    # vehicle_use
    op.execute('''
        UPDATE "TAR"."vehicle_use" SET description = UPPER(description);
    ''')

    # position
    op.execute('''
        UPDATE "TAR"."position" SET description = UPPER(description);
    ''')

    # safety_equipment
    op.execute('''
        UPDATE "TAR"."safety_equipment" SET description = UPPER(description);
    ''')

    # ejection
    op.execute('''
        UPDATE "TAR"."ejection" SET description = UPPER(description);
    ''')

    # injury_location
    op.execute('''
        UPDATE "TAR"."injury_location" SET description = UPPER(description);
    ''')

    # injury_type
    op.execute('''
        UPDATE "TAR"."injury_type" SET description = UPPER(description);
    ''')

    # victim_status
    op.execute('''
        UPDATE "TAR"."victim_status" SET description = UPPER(description);
    ''')

    # taken_to
    op.execute('''
        UPDATE "TAR"."taken_to" SET description = UPPER(description);
    ''')

    # taken_by
    op.execute('''
        UPDATE "TAR"."taken_by" SET description = UPPER(description);
    ''')

    # taken_by
    op.execute('''
        UPDATE "TAR"."taken_by" SET description = UPPER(description);
    ''')

    # injury_classification
    op.execute('''
        UPDATE "TAR"."injury_classification" SET description = UPPER(description);
    ''')

    op.execute('''
        UPDATE "TAR"."collision_scenario" SET description = UPPER(description);
    ''')

    op.execute('''
        UPDATE "TAR"."police_agency" SET agency_name = UPPER(agency_name);
    ''')


def downgrade():
    pass
