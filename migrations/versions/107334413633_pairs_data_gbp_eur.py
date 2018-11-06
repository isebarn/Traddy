"""Pairs data GBP EUR

Revision ID: 107334413633
Revises: a353b760a3dc
Create Date: 2018-11-06 21:36:56.524866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '107334413633'
down_revision = 'a353b760a3dc'
branch_labels = None
depends_on = None

def seed_data():
    roles_table = sa.sql.table(
        'pairs',
        sa.sql.column('pair', sa.String),
        sa.sql.column('units_per_pip_usd', sa.Integer),
        sa.sql.column('comission', sa.Numeric),
    )

    # Insert new roles
    op.bulk_insert(
        roles_table,
        [
            {'pair': 'EURUSD', 'units_per_pip_usd': 10000, 'comission': 2.7},
            {'pair': 'GBPUSD', 'units_per_pip_usd': 10000, 'comission': 2.7},
        ]
    ) 	


def upgrade():
    seed_data()


def downgrade():
    pass
