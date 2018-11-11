"""Pairs data GBP EUR

Revision ID: 7f88b86d4c69
Revises: bfbd244e193d
Create Date: 2018-11-11 10:42:32.763962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f88b86d4c69'
down_revision = 'bfbd244e193d'
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
