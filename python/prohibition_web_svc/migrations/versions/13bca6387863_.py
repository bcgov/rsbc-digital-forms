"""empty message

Revision ID: 13bca6387863
Revises: dc0599cd958e
Create Date: 2023-11-23 13:00:03.610986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13bca6387863'
down_revision = 'dc0599cd958e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city_cross_ref',
    sa.Column('city_code', sa.String(), nullable=False),
    sa.Column('city_name', sa.String(), nullable=True),
    sa.Column('icbc_city_code', sa.String(), nullable=True),
    sa.Column('icbc_city_name', sa.String(), nullable=True),
    sa.Column('icbc_city_name_legacy', sa.String(), nullable=True),
    sa.Column('vips_city_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('city_code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('city_cross_ref')
    # ### end Alembic commands ###
