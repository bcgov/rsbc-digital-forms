"""empty message

Revision ID: 7925ac186d84
Revises: 4e8b58b8cf7f
Create Date: 2023-10-19 11:32:55.497819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7925ac186d84'
down_revision = '4e8b58b8cf7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location_of_keys', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('type_of_prohibition', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('agency_file_no', sa.String(), nullable=True))

    with op.batch_alter_table('twenty_four_hour_form', schema=None) as batch_op:
        batch_op.drop_column('agency_file_no')
        batch_op.drop_column('location_of_keys')
        batch_op.drop_column('type_of_prohibition')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('twenty_four_hour_form', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type_of_prohibition', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('location_of_keys', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('agency_file_no', sa.VARCHAR(), autoincrement=False, nullable=True))

    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.drop_column('agency_file_no')
        batch_op.drop_column('type_of_prohibition')
        batch_op.drop_column('location_of_keys')

    # ### end Alembic commands ###
