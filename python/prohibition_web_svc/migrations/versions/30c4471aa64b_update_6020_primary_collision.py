"""update-6020-primary_collision

Revision ID: 30c4471aa64b
Revises: 3ef0bb500f08
Create Date: 2025-12-08 15:56:00.549048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30c4471aa64b'
down_revision = '3ef0bb500f08'
branch_labels = None
depends_on = None


def upgrade():
    # primary_collision_occurrence
    op.execute('''
        UPDATE "TAR"."primary_collision_occurrence" SET description = 'LEFT TURN (TRAVELING SAME DIRECTION)' where code = '12';
        UPDATE "TAR"."primary_collision_occurrence" SET description = 'LEFT TURN (TURN IN FRONT OF)' where code = '13';
        UPDATE "TAR"."primary_collision_occurrence" SET description = 'OFF ROAD RIGHT' where code = '14';
        UPDATE "TAR"."primary_collision_occurrence" SET description = 'OFF ROAD LEFT' where code = '15';
        UPDATE "TAR"."primary_collision_occurrence" SET description = 'ONE WAY STREET' where code = '16';
    ''')


def downgrade():
    op.execute('''
        UPDATE "TAR"."primary_collision_occurrence" SET description = 'LEFT TURN (CUTOFF)' where code = '12';
        UPDATE "TAR"."primary_collision_occurrence" SET description = 'LEFT TURN (TRAVELING SAME DIRECTION)' where code = '13';
        UPDATE "TAR"."primary_collision_occurrence" SET description = 'LEFT TURN (TURN IN FRONT OF)' where code = '14';
        UPDATE "TAR"."primary_collision_occurrence" SET description = 'OFF ROAD RIGHT' where code = '15';
        UPDATE "TAR"."primary_collision_occurrence" SET description = 'OFF ROAD LEFT' where code = '16';
    ''')
