"""empty message

Revision ID: 2b0bb8892bc7
Revises: db4b7266b1cb
Create Date: 2023-10-21 11:03:36.567101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b0bb8892bc7'
down_revision = 'db4b7266b1cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('twenty_four_hour_form', schema=None) as batch_op:
        batch_op.alter_column('requested_prescribed_test',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('twenty_four_hour_form', schema=None) as batch_op:
        batch_op.alter_column('requested_prescribed_test',
               existing_type=sa.String(),
               type_=sa.BOOLEAN(),
               existing_nullable=True)

    # ### end Alembic commands ###
