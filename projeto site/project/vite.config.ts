import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        produtos: resolve(__dirname, 'produtos.html'),
        carrinho: resolve(__dirname, 'carrinho.html'),
        pagamento: resolve(__dirname, 'pagamento.html'),
        reserva: resolve(__dirname, 'reserva.html'),
        contato: resolve(__dirname, 'contato.html'),
        login: resolve(__dirname, 'login.html'),
        cadastro: resolve(__dirname, 'cadastro.html'),
      },
    },
  },
});
