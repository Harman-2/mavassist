import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';
export default defineConfig({plugins:[react(),tailwindcss()],server:{watch:{ignored:['**/test-results/**','**/playwright-report/**','**/coverage/**','**/dist/**']},proxy:{'/api':process.env.API_PROXY_URL || 'http://127.0.0.1:8000','/health':process.env.API_PROXY_URL || 'http://127.0.0.1:8000'}}});
