"""empty message

Revision ID: 6c4aa4e1039d
Revises: 0fab578072b7
Create Date: 2024-09-12 16:18:16.174245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c4aa4e1039d'
down_revision = '0fab578072b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('df_errors',
    sa.Column('error_id', sa.Integer(), nullable=False),
    sa.Column('error_cd', sa.Enum('G00', 'E01', 'E02', name='errorcode'), nullable=False),
    sa.Column('error_cd_desc', sa.String(length=200), nullable=False),
    sa.Column('error_category_cd', sa.Enum('VALIDATION', 'SYSTEM', 'CONNECTION', 'DATA', 'OTHER', name='errorcategory'), nullable=False),
    sa.Column('error_severity_level_cd', sa.Enum('LOW', 'MEDIUM', 'HIGH', 'CRITICAL', name='errorseverity'), nullable=False),
    sa.Column('error_details', sa.Text(), nullable=True),
    sa.Column('error_path', sa.String(length=200), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('event_type', sa.Enum('TWELVE_HOUR', 'TWENTY_FOUR_HOUR', 'IRP', 'VI', name='eventtype'), nullable=True),
    sa.Column('ticket_no', sa.String(length=50), nullable=True),
    sa.Column('received_dt', sa.DateTime(), nullable=True),
    sa.Column('error_status_cd', sa.Enum('NEW', 'VIEWED', 'IN_PROGRESS', 'ASSIGNED', 'RESOLVED', 'CANCELLED', 'CLOSED', name='errorstatus'), nullable=True),
    sa.Column('req_payload', sa.Text(), nullable=True),
    sa.Column('created_by', sa.String(length=150), nullable=True),
    sa.Column('created_dt', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=150), nullable=True),
    sa.Column('updated_dt', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.event_id'], ),
    sa.PrimaryKeyConstraint('error_id')
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('df_errors')
    # ### end Alembic commands ###
