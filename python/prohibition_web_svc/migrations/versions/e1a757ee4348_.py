"""empty message

Revision ID: e1a757ee4348
Revises: 4ae0d0dc8ae4
Create Date: 2023-09-20 10:20:21.805108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1a757ee4348'
down_revision = '4ae0d0dc8ae4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vi_sent_status', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.drop_column('vi_sent_status')

    # ### end Alembic commands ###
