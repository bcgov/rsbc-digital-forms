"""submission_report

Revision ID: 0060d115e3a8
Revises: e4baa2bf0714
Create Date: 2025-12-23 11:36:05.674378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0060d115e3a8'
down_revision = 'e4baa2bf0714'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    CREATE OR REPLACE VIEW submission_report_view AS
    SELECT 
        b.id,
        b.form_id,
        b.form_name,
        b.application_status,
        coalesce(s.submitted_offline, false) as offline,
        b.created,
        cast((b.created at TIME zone 'UTC' at time zone 'America/Vancouver') as date) as created_dt,
        u.agency_id,
        a.agency_name
    FROM submission s  
    RIGHT JOIN dblink('dbname=formsflow_api', 
        'select  
            a.id,
            fpm.form_id,
            fpm.form_name ,
            a.application_status,
            UPPER(SPLIT_PART(a.created_by, ''@'', 1)) AS user_guid,
            a.created
        from application a 
        inner join form_process_mapper fpm on a.form_process_mapper_id = fpm.id'
        ) 
    AS b(id INT, form_id varchar, form_name varchar, application_status varchar, user_guid varchar, created timestamp)
    ON s.ff_application_id  = b.id
    LEFT JOIN "user" u ON UPPER(u.user_guid) = b.user_guid
    INNER JOIN agency a ON a.id = u.agency_id
    ORDER BY created, b.form_name;
    """)


def downgrade():
    op.execute("DROP VIEW IF EXISTS submission_report_view;")
