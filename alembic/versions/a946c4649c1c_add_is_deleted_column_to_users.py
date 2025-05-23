"""add is deleted column to users

Revision ID: a946c4649c1c
Revises: 61e0f8e582b2
Create Date: 2025-05-07 18:10:18.727819

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a946c4649c1c'
down_revision: Union[str, None] = '61e0f8e582b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic  ###
    op.add_column('users', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    # ### Manual additions: RLS setup ###
    op.execute("ALTER TABLE users ENABLE ROW LEVEL SECURITY;")
    op.execute("""
        CREATE POLICY only_non_deleted_users
        ON users
        FOR SELECT
        USING (is_deleted = FALSE);
    """)


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic ###
    op.drop_column('users', 'is_deleted')
    # ### Manual rollback of policies ###
    op.execute("DROP POLICY IF EXISTS only_non_deleted_users ON users;")
    op.execute("ALTER TABLE users DISABLE ROW LEVEL SECURITY;")
