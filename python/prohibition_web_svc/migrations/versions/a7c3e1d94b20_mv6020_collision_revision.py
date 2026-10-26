"""mv6020_collision_revision

Change reports are new revisions of the same collision case number. The
collision primary key becomes (collision_case_num, revision) and every table
that references a collision carries the revision. Existing rows become
revision 0, the original submission.

Revision ID: a7c3e1d94b20
Revises: f28f7c94e9ee
Create Date: 2026-10-26 09:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7c3e1d94b20'
down_revision = 'f28f7c94e9ee'
branch_labels = None
depends_on = None

SCHEMA = 'TAR'
CHILD_TABLES = ['entity', 'location', 'witness_info', 'additional_collision_details']


def upgrade():
    for table in CHILD_TABLES:
        op.drop_constraint(f'{table}_collision_case_num_fkey', table, schema=SCHEMA, type_='foreignkey')

    for table in ['collision'] + CHILD_TABLES:
        op.add_column(table, sa.Column('revision', sa.Integer(), nullable=False, server_default='0'), schema=SCHEMA)

    op.drop_constraint('collision_pkey', 'collision', schema=SCHEMA, type_='primary')
    op.create_primary_key('collision_pkey', 'collision', ['collision_case_num', 'revision'], schema=SCHEMA)

    op.drop_constraint('additional_collision_details_pkey', 'additional_collision_details', schema=SCHEMA, type_='primary')
    op.create_primary_key('additional_collision_details_pkey', 'additional_collision_details',
                          ['collision_case_num', 'revision'], schema=SCHEMA)

    for table in CHILD_TABLES:
        op.create_foreign_key(f'{table}_collision_revision_fkey', table, 'collision',
                              ['collision_case_num', 'revision'], ['collision_case_num', 'revision'],
                              source_schema=SCHEMA, referent_schema=SCHEMA)


def downgrade():
    # Fails if any case number has more than one revision; remove change
    # report revisions first.
    for table in CHILD_TABLES:
        op.drop_constraint(f'{table}_collision_revision_fkey', table, schema=SCHEMA, type_='foreignkey')

    op.drop_constraint('additional_collision_details_pkey', 'additional_collision_details', schema=SCHEMA, type_='primary')
    op.create_primary_key('additional_collision_details_pkey', 'additional_collision_details',
                          ['collision_case_num'], schema=SCHEMA)

    op.drop_constraint('collision_pkey', 'collision', schema=SCHEMA, type_='primary')
    op.create_primary_key('collision_pkey', 'collision', ['collision_case_num'], schema=SCHEMA)

    for table in ['collision'] + CHILD_TABLES:
        op.drop_column(table, 'revision', schema=SCHEMA)

    for table in CHILD_TABLES:
        op.create_foreign_key(f'{table}_collision_case_num_fkey', table, 'collision',
                              ['collision_case_num'], ['collision_case_num'],
                              source_schema=SCHEMA, referent_schema=SCHEMA)
