"""empty message

Revision ID: 4ae0d0dc8ae4
Revises: 1dff388c19fd
Create Date: 2023-09-20 10:14:04.313857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ae0d0dc8ae4'
down_revision = '1dff388c19fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('form_storage_refs',
    sa.Column('form_id_24h', sa.Integer(), nullable=True),
    sa.Column('form_id_irp', sa.Integer(), nullable=True),
    sa.Column('form_id_vi', sa.Integer(), nullable=True),
    sa.Column('form_id_12h', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('form_type', sa.String(), nullable=True),
    sa.Column('storage_key', sa.String(), nullable=False),
    sa.Column('created_dt', sa.DateTime(), nullable=True),
    sa.Column('updated_dt', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.event_id'], ),
    sa.ForeignKeyConstraint(['form_id_12h'], ['twelve_hour_form.form_id'], ),
    sa.ForeignKeyConstraint(['form_id_24h'], ['twenty_four_hour_form.form_id'], ),
    sa.ForeignKeyConstraint(['form_id_irp'], ['irp_form.form_id'], ),
    sa.ForeignKeyConstraint(['form_id_vi'], ['vi_form.form_id'], ),
    sa.PrimaryKeyConstraint('storage_key')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('form_storage_refs')
    # ### end Alembic commands ###
