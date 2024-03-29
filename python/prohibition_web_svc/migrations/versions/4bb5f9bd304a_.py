"""empty message

Revision ID: 4bb5f9bd304a
Revises: a6771d58f8fe
Create Date: 2023-08-16 14:55:03.673662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bb5f9bd304a'
down_revision = 'a6771d58f8fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('twenty_four_hour_form', schema=None) as batch_op:
        batch_op.add_column(sa.Column('requested_prescribed_test', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('requested_test_used', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('time_of_requested_test', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('requested_ASD_expiry_date', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('requested_alcohol_test_result', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('requested_BAC_result', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('requested_approved_instrument_used', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('twenty_four_hour_form', schema=None) as batch_op:
        batch_op.drop_column('requested_approved_instrument_used')
        batch_op.drop_column('requested_BAC_result')
        batch_op.drop_column('requested_alcohol_test_result')
        batch_op.drop_column('requested_ASD_expiry_date')
        batch_op.drop_column('time_of_requested_test')
        batch_op.drop_column('requested_test_used')
        batch_op.drop_column('requested_prescribed_test')

    # ### end Alembic commands ###
