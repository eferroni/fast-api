"""create address table

Revision ID: 625e13abb159
Revises: baa5afb16938
Create Date: 2022-10-31 12:05:26.576755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '625e13abb159'
down_revision = 'baa5afb16938'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("address",
                    sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("address1", sa.String(), nullable=False),
                    sa.Column("address2", sa.String(), nullable=False),
                    sa.Column("city", sa.String(), nullable=False),
                    sa.Column("state", sa.String(), nullable=False),
                    sa.Column("country", sa.String(), nullable=False),
                    sa.Column("postal_code", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_table("address")
