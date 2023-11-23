"""empty message

Revision ID: f76bbde02978
Revises: 0134c884845f
Create Date: 2023-11-22 20:03:25.778970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f76bbde02978'
down_revision = '0134c884845f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agency_cross_refs',
    sa.Column('agency_name', sa.String(), nullable=False),
    sa.Column('agency_id', sa.String(), nullable=True),
    sa.Column('agency_city', sa.String(), nullable=True),
    sa.Column('prime_vjur', sa.String(), nullable=True),
    sa.Column('icbc_detachment_name', sa.String(), nullable=True),
    sa.Column('icbc_city_name', sa.String(), nullable=True),
    sa.Column('vips_policedetachments_agency_id', sa.String(), nullable=True),
    sa.Column('vips_policedetachments_agency_nm', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('agency_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('agency_cross_refs')
    # ### end Alembic commands ###