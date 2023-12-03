"""empty message

Revision ID: cbfbfa70b774
Revises: ec5fa60942aa
Create Date: 2023-11-06 14:17:17.822899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbfbfa70b774'
down_revision = 'ec5fa60942aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    vehicle_type = op.create_table('vehicle_type',
    sa.Column('type_cd', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('type_cd')
    )
    # ### end Alembic commands ###

    op.bulk_insert(
        vehicle_type,
        [
                        {
                        "type_cd": 1,
                        "description": "PASSENGER"
                        },
                        {
                        "type_cd": 2,
                        "description": "COMMERCIAL TRUCK, FARM INDUSTRIAL, OR PASSENGER CARRYING COMMERCIAL"
                        },{
                        "type_cd": 3,
                        "description": "MOTORCYCLE MOPED"
                        },
                        {
                        "type_cd": 4,
                        "description": "UTILITY TRAILER"
                        },
                        {
                        "type_cd": 5,
                        "description": "MOTOR HOME"
                        },
                        {
                        "type_cd": 6,
                        "description": "COMMERCIAL TRAILER"
                        },
                    ]
                )

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicle_type')
    # ### end Alembic commands ###
