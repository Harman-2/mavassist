"""Initial application tables and PostgreSQL vector extension."""
from alembic import op
from sqlalchemy import text
from app.db import Base
revision='001'
down_revision=None
branch_labels=None
depends_on=None
def upgrade():
    connection=op.get_bind()
    if connection.dialect.name=='postgresql': connection.execute(text('CREATE EXTENSION IF NOT EXISTS vector'))
    Base.metadata.create_all(connection)
    if connection.dialect.name=='postgresql':
        connection.execute(text('CREATE INDEX services_embedding_hnsw ON services USING hnsw (embedding vector_cosine_ops)'))
def downgrade(): Base.metadata.drop_all(op.get_bind())
