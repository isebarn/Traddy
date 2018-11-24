"""create pair data

Revision ID: d6cabf03fd0b
Revises: 7793c43ebd58
Create Date: 2018-11-22 20:47:36.825226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6cabf03fd0b'
down_revision = '7793c43ebd58'
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
