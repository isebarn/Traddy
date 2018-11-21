"""Pairs data GBP EUR

Revision ID: c69b5c464fc7
Revises: 77d2838d0836
Create Date: 2018-11-12 21:29:00.184032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c69b5c464fc7'
down_revision = '77d2838d0836'
branch_labels = None
depends_on = None


def seed_data():
    pairs_table = sa.sql.table(
        'pairs',
        sa.sql.column('pair', sa.String),
        sa.sql.column('units_per_pip_usd', sa.Integer),
        sa.sql.column('comission', sa.Numeric),
    )

    # Insert new roles
    op.bulk_insert(
        pairs_table,
        [
            {'pair': 'EURUSD', 'units_per_pip_usd': 10000, 'comission': 2.7},
            {'pair': 'GBPUSD', 'units_per_pip_usd': 10000, 'comission': 2.7},
        ]
    ) 	


def upgrade():
    seed_data()

def downgrade():
    pass
