"""create apt_num to address

Revision ID: 9d12522171c3
Revises: 80344d738c85
Create Date: 2022-10-31 14:09:04.337494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d12522171c3'
down_revision = '80344d738c85'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("address", sa.Column("apt_num", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("address", "apt_num")
