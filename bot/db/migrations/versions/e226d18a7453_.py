"""

Revision ID: e226d18a7453
Revises: 342baa79f745
Create Date: 2022-11-11 17:55:41.920557

"""
#  Copyright (c) 2022.

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'e226d18a7453'
down_revision = '342baa79f745'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'channels', ['id'])
    op.add_column('users', sa.Column('locale', sa.VARCHAR(length=2), nullable=True))
    op.create_unique_constraint(None, 'users', ['user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'locale')
    op.drop_constraint(None, 'channels', type_='unique')
    # ### end Alembic commands ###