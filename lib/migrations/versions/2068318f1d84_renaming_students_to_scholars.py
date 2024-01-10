"""Renaming students to scholars

Revision ID: 2068318f1d84
Revises: 791279dd0760
Create Date: 2024-01-10 13:53:58.326650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2068318f1d84'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
