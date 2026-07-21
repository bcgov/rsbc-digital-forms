"""add detachment_change_request

Revision ID: a1b2c3d4e5f6
Revises: fff1bdd7ea3e
Create Date: 2026-06-03 07:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = 'a1b2c3d4e5f6'
down_revision = '3b493c418866'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'detachment_change_request',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('officer_id', sa.String(length=120), nullable=False),
        sa.Column('previous_agency_id', sa.Integer(), nullable=True),
        sa.Column('new_agency_id', sa.Integer(), nullable=False),
        sa.Column('reason', sa.String(length=50), nullable=False),
        sa.Column('comments', sa.Text(), nullable=True),
        sa.Column('created_dt', sa.DateTime(), nullable=False),
        sa.Column('created_by', sa.String(length=120), nullable=True),
        sa.ForeignKeyConstraint(['new_agency_id'], ['agency.id']),
        sa.ForeignKeyConstraint(['officer_id'], ['user.user_guid']),
        sa.ForeignKeyConstraint(['previous_agency_id'], ['agency.id']),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('detachment_change_request')
