"""Add a column

Revision ID: 0001
Revises: 
Create Date: 2022-01-03 13:07:19.024903

"""
from alembic import op
import sqlalchemy as sa

from custom_package.models.customers import Customers
# revision identifiers, used by Alembic.
from alembic_helpers import table_has_column

revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    if not table_has_column("customers", "description"):
        op.add_column("customers", sa.Column("description", sa.String))


def downgrade():
    pass
