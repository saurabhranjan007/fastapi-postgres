"""init

Revision ID: f6df06a9c30e
Revises: 
Create Date: 2023-05-30 11:54:45.183943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6df06a9c30e'
down_revision = None
branch_labels = None
depends_on = None


# def upgrade() -> None:
#     pass

def upgrade():
    op.create_table(
        'Events',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('desc',sa.String, nullable=False)

        # sa.Column('event_id', sa.Integer, primary_key=True),
        # sa.Column('event_name', sa.String, nullable=False),
        # sa.Column('event_location', sa.String, nullable=False),
        # sa.Column('event_desc', sa.String, nullable=False)
    )

# def downgrade() -> None:
#     pass

def downgrade():
    op.drop_table('Events')
