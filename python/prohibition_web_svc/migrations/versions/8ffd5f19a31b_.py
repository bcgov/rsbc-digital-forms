"""empty message

Revision ID: 8ffd5f19a31b
Revises: 7fbf9737ddc4
Create Date: 2023-10-21 10:19:17.762506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ffd5f19a31b'
down_revision = '7fbf9737ddc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('confirmation_of_service', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('confirmation_of_service_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.drop_column('confirmation_of_service_date')
        batch_op.drop_column('confirmation_of_service')

    # ### end Alembic commands ###
