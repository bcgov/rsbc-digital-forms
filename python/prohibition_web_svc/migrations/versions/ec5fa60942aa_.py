"""empty message

Revision ID: ec5fa60942aa
Revises: 1920269671bc
Create Date: 2023-11-02 11:43:21.933443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec5fa60942aa'
down_revision = '1920269671bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('twelve_hour_form', schema=None) as batch_op:
        batch_op.add_column(sa.Column('twelve_hour_number', sa.String(), nullable=True))

    with op.batch_alter_table('twenty_four_hour_form', schema=None) as batch_op:
        batch_op.add_column(sa.Column('twenty_four_hour_number', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('twenty_four_hour_form', schema=None) as batch_op:
        batch_op.drop_column('twenty_four_hour_number')

    with op.batch_alter_table('twelve_hour_form', schema=None) as batch_op:
        batch_op.drop_column('twelve_hour_number')

    # ### end Alembic commands ###
