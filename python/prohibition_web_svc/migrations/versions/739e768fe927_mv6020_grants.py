"""mv6020-grants

Revision ID: 739e768fe927
Revises: 8745789679db
Create Date: 2025-07-31 10:22:58.673564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '739e768fe927'
down_revision = '8745789679db'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".collision_location TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".collision_scenario TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".contributing_factors TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".damage_location TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".damage_severity TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".ejection TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".entity_type TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".injury_classification TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".injury_location TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".injury_type TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".land_usage TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".lighting_condition TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".location_of_first_contact TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".pedestrian_action TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".pedestrian_location TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".position TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".pre_collision_action TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".primary_collision_occurrence TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".road_class TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".road_type TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".roadway_character TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".roadway_condition TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".safety_equipment TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".speed_zone TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".taken_by TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".taken_to TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".traffic_control TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".traffic_flow TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".type_of_collision TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".vehicle_type TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".vehicle_use TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".victim_status TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".weather_condition TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE submission TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".police_district TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".police_agency TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".collision TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".additional_collision_details TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".entity TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".location TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".witness_info TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".charges TO df_db_app_user;
        GRANT SELECT, UPDATE, DELETE, INSERT, REFERENCES ON TABLE "TAR".involved_person TO df_db_app_user;
        GRANT USAGE ON SCHEMA "TAR" TO df_db_app_user;
        GRANT SELECT, UPDATE, USAGE ON SEQUENCE "TAR".charges_charge_id_seq TO df_db_app_user;
        GRANT SELECT, UPDATE, USAGE ON SEQUENCE "TAR".entity_entity_id_seq TO df_db_app_user;
        GRANT SELECT, UPDATE, USAGE ON SEQUENCE "TAR".involved_person_person_id_seq TO df_db_app_user;
        GRANT SELECT, UPDATE, USAGE ON SEQUENCE "TAR".location_location_id_seq TO df_db_app_user;
        GRANT SELECT, UPDATE, USAGE ON SEQUENCE "TAR".police_agency_code_seq TO df_db_app_user;
        GRANT SELECT, UPDATE, USAGE ON SEQUENCE "TAR".police_district_id_seq TO df_db_app_user;
        GRANT SELECT, UPDATE, USAGE ON SEQUENCE "TAR".witness_info_id_seq TO df_db_app_user;
    """)


def downgrade():
    pass
