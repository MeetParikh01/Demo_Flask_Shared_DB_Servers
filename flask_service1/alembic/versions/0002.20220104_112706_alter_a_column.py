"""alter a column

Revision ID: 0002
Revises: 0001
Create Date: 2022-01-04 11:27:06.113081

"""
from alembic import op
import sqlalchemy as sa
from alembic_helpers import table_has_column

# revision identifiers, used by Alembic.
revision = '0002'
down_revision = '0001'
branch_labels = None
depends_on = None


def upgrade():
    if table_has_column("customers", "description"):
        op.alter_column("customers", "description", new_column_name="description_changedescription_change")


def downgrade():
    pass
