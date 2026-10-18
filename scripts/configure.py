"""Generate local environment without fixed credentials. Never overwrite an existing .env."""
from pathlib import Path
import secrets
root=Path(__file__).resolve().parents[1]
target=root/'backend'/'.env'
if target.exists(): print('backend/.env already exists; left unchanged.')
else:
    target.write_text('APP_ENV=development\nDATABASE_URL=sqlite:///./mavassist.db\nJWT_SECRET='+secrets.token_urlsafe(48)+'\nCORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173\nAI_MODE=keyword\nOPENAI_API_KEY=\nOPENAI_MODEL=\nSIMILARITY_THRESHOLD=0.28\nRATE_LIMIT=true\n',encoding='utf-8')
    print('Created backend/.env with a unique JWT secret and offline keyword mode.')
compose=root/'.env'
if not compose.exists():
    compose.write_text('POSTGRES_PASSWORD='+secrets.token_urlsafe(30)+'\nJWT_SECRET='+secrets.token_urlsafe(48)+'\nINSTALL_AI=true\nAI_MODE=rag\nOPENAI_API_KEY=\nOPENAI_MODEL=\n',encoding='utf-8')
    print('Created root .env for Docker Compose. Add your AI key/model or choose keyword mode.')
