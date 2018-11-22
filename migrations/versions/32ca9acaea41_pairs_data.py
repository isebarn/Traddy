"""Pairs data

Revision ID: 32ca9acaea41
Revises: 65e5a1db4b17
Create Date: 2018-11-22 19:24:29.671400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32ca9acaea41'
down_revision = '65e5a1db4b17'
branch_labels = None
depends_on = None


def seed_data():
    pairs_table = sa.sql.table(
        'pairs',
        sa.sql.column('pair', sa.String),
        sa.sql.column('std_lot_profit_per_pip', sa.Integer),
        sa.sql.column('comission', sa.Numeric),
    )

    # Insert new roles
    op.bulk_insert(
        pairs_table,
        [
            {'pair': 'EURUSD', 'std_lot_profit_per_pip': 10.00, 'comission': 2.7},
            {'pair': 'GBPUSD', 'std_lot_profit_per_pip': 10.00, 'comission': 2.7},
            {'pair': 'USDJPY', 'std_lot_profit_per_pip': 8.91, 'comission': 2.7},
            {'pair': 'USDCAD', 'std_lot_profit_per_pip': 7.63, 'comission': 2.7},
        ]
    ) 	


def upgrade():
    seed_data()

def downgrade():
    pass
