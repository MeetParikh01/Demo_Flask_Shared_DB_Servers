from alembic import op
from sqlalchemy import inspect
from custom_package.db_handler import handler


def table_has_column(table, column):
    insp = inspect(handler.engine)
    has_column = False
    for col in insp.get_columns(table):
        if column not in col['name']:
            continue
        has_column = True
    return has_column
