"""create address_id to users

Revision ID: 80344d738c85
Revises: 625e13abb159
Create Date: 2022-10-31 13:10:17.717153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80344d738c85'
down_revision = '625e13abb159'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("address_id", sa.Integer(), nullable=True))
    op.create_foreign_key("address_users_fk",
                          source_table="users",
                          referent_table="address",
                          local_cols=["address_id"],
                          remote_cols=["id"],
                          ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("address_users_fk", table_name="users")
    op.drop_column("users", "address_id")
