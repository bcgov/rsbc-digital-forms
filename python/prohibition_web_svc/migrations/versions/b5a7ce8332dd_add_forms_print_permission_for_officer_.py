"""Add forms-print permission for officer role

Revision ID: b5a7ce8332dd
Revises: 56d7192bb891
Create Date: 2025-08-26 16:27:45.310846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5a7ce8332dd'
down_revision = '56d7192bb891'
branch_labels = None
depends_on = None


def upgrade():
    # Insert forms-print permission for officer role if it doesn't exist
    op.execute("""
        INSERT INTO permission (role, permission) 
        SELECT 'officer', 'forms-print'
        WHERE NOT EXISTS (
            SELECT 1 FROM permission 
            WHERE role = 'officer' AND permission = 'forms-print'
        );
    """)


def downgrade():
    # Remove forms-print permission for officer role
    op.execute("""
        DELETE FROM permission 
        WHERE role = 'officer' AND permission = 'forms-print';
    """)
