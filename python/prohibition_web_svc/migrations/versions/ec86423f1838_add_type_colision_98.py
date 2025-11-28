"""add_type_colision_98

Revision ID: ec86423f1838
Revises: 0b9e4209b498
Create Date: 2025-11-24 16:23:04.770504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec86423f1838'
down_revision = '0b9e4209b498'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        Insert into "TAR".type_of_collision (code, description, type) values 
            ('98', 'NON APPLICABLE', 'NON COLLISION');
               
        UPDATE "TAR".type_of_collision SET type = UPPER(type);
    """)

def downgrade():
    op.execute("""
        Delete from "TAR".type_of_collision where code = '98';
    """)