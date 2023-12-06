"""empty message

Revision ID: 237614f969cf
Revises: b4b054d65515
Create Date: 2023-12-02 14:47:40.537260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '237614f969cf'
down_revision = 'b4b054d65515'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ilo_cross_ref',
    sa.Column('ilo_name', sa.String(), nullable=False),
    sa.Column('vips_impound_lot_operator_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('ilo_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ilo_cross_ref')
    # ### end Alembic commands ###
