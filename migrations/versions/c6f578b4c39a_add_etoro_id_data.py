"""add etoro id data

Revision ID: c6f578b4c39a
Revises: 00d539030577
Create Date: 2018-11-24 16:27:50.389218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6f578b4c39a'
down_revision = '00d539030577'
branch_labels = None
depends_on = None


def seed_data():
	connection = op.get_bind()
	connection.execute("update pairs set etoro_id = 1 where pair = 'EURUSD'")
	connection.execute("update pairs set etoro_id = 2 where pair = 'GBPUSD'")
	connection.execute("update pairs set etoro_id = 5 where pair = 'USDJPY'")
	connection.execute("update pairs set etoro_id = 4 where pair = 'USDCAD'")



def upgrade():
	seed_data()

def downgrade():
	pass
