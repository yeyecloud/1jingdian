"""Update piece comment.

Revision ID: 21617647835f
Revises: 35c0d4e5f47
Create Date: 2015-04-02 14:38:52.622864

"""

# revision identifiers, used by Alembic.
revision = '21617647835f'
down_revision = '35c0d4e5f47'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('piece_comment', sa.Column('root_comment_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'piece_comment', 'piece_comment', ['root_comment_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'piece_comment', type_='foreignkey')
    op.drop_column('piece_comment', 'root_comment_id')
    ### end Alembic commands ###