"""empty message

Revision ID: 2f823367eff8
Revises: eaed4d2b6dd3
Create Date: 2024-03-12 10:47:24.871211

"""
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = '2f823367eff8'
down_revision = 'eaed4d2b6dd3'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vehicle_make', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('vehicle_model', sa.String(), nullable=True))

        # Retrieve data from the old column using SQLAlchemy's select function
        stmt = sa.select(['event_id', 'vehicle_mk_md']).select_from('event')
        result = op.execute(stmt)
        
        if result is not None:
            old_data = result.fetchall()

            # Print the fetched data for debugging
            print("Fetched data:", old_data)

            # Iterate through the data, split and update the new columns
            for row in old_data:
                event_id, vehicle_mk_md = row
                if vehicle_mk_md:
                    parts = map(str.strip, vehicle_mk_md.split('-'))
                    make = parts[0]
                    model = parts[1] if len(parts) > 1 else None
                    op.execute(
                        "UPDATE event SET vehicle_make = :make, vehicle_model = :model WHERE event_id = :event_id",
                        {'make': make, 'model': model, 'event_id': event_id}
                    )

            # Finally, we can drop the original column
            batch_op.drop_column('vehicle_mk_md')
        else:
            print("No data found for the specified query.")

def downgrade():
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vehicle_mk_md', sa.VARCHAR(), autoincrement=False, nullable=True))

        # Retrieve data from the new columns
        result = op.execute("SELECT event_id, vehicle_make, vehicle_model FROM event")
        
        print("Result: ", result)

        if result is not None:
            new_data = result.fetchall()

            # Iterate through the data, concatenate and update the old column
            for row in new_data:
                event_id, make, model = row
                vehicle_mk_md = f"{make}-{model}" if model else f"{make}-"
                op.execute(
                    "UPDATE event SET vehicle_mk_md = :vehicle_mk_md WHERE event_id = :event_id",
                    {'vehicle_mk_md': vehicle_mk_md, 'event_id': event_id}
                )

            # Finally, drop the new columns
            batch_op.drop_column('vehicle_model')
            batch_op.drop_column('vehicle_make')
        else:
            print("No data found for the specified query.")
