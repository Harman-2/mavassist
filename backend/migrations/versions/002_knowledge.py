"""Add cited knowledge passages for retrieval-augmented answers."""
from alembic import op
from sqlalchemy import text
from app.db import KnowledgeChunk
revision='002'
down_revision='001'
branch_labels=None
depends_on=None
def upgrade():
    connection=op.get_bind()
    KnowledgeChunk.__table__.create(connection,checkfirst=True)
    if connection.dialect.name=='postgresql':
        connection.execute(text('CREATE INDEX IF NOT EXISTS knowledge_embedding_hnsw ON knowledge_chunks USING hnsw (embedding vector_cosine_ops)'))
def downgrade(): KnowledgeChunk.__table__.drop(op.get_bind())
