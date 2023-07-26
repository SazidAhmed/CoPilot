"""Add label to Agent Metadata

Revision ID: 7b25ec454c0a
Revises: 09189f03c3ee
Create Date: 2023-07-27 09:37:01.189629

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "7b25ec454c0a"
down_revision = "09189f03c3ee"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("agent_metadata", schema=None) as batch_op:
        batch_op.add_column(sa.Column("label", sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("agent_metadata", schema=None) as batch_op:
        batch_op.drop_column("label")

    # ### end Alembic commands ###
