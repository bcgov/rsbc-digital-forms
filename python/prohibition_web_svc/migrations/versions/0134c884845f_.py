"""empty message

Revision ID: 0134c884845f
Revises: 529289c8081b
Create Date: 2023-11-08 12:22:10.320063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0134c884845f'
down_revision = '529289c8081b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vi_form', schema=None) as batch_op:
        batch_op.add_column(sa.Column('out_of_province_dl_jurisdiction', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vi_form', schema=None) as batch_op:
        batch_op.drop_column('out_of_province_dl_jurisdiction')

    # ### end Alembic commands ###