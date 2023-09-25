"""empty message

Revision ID: c021e4dd831c
Revises: e1a757ee4348
Create Date: 2023-09-20 12:21:37.139942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c021e4dd831c'
down_revision = 'e1a757ee4348'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('icbc_retry_count', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('vi_retry_count', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.drop_column('vi_retry_count')
        batch_op.drop_column('icbc_retry_count')

    # ### end Alembic commands ###