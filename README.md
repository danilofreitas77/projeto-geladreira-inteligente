# 🧊 Projeto Geladeira Inteligente

Sistema de gerenciamento e compras de produtos de uma "geladeira inteligente" para condomínio, desenvolvido em **Django**.  

## 🚀 Funcionalidades
- Cadastro e autenticação de moradores (login com QR Code).
- Cadastro de produtos (via Django Admin).
- Organização de produtos por categorias (ex: Bebidas).
- Sistema de carrinho de compras.
- Envio de relatório de compras por e-mail para o morador.

## 🛠️ Tecnologias Utilizadas
- **Python 3.12**
- **Django**
- **SQLite (padrão do Django)**
- **Git/GitHub**
- **Bootstrap (para estilização futura)**

## 📦 Estrutura do Projeto

projeto-geladeira/
│── geladeira/ # Configurações principais do Django
│── produtos/ # App para cadastro e gestão de produtos
│── usuarios/ # App para moradores e login via QR Code
│── templates/ # Templates HTML
│── static/ # Arquivos estáticos (CSS, JS, imagens)
│── db.sqlite3 # Banco de dados padrão
│── manage.py # CLI do Django


## ⚙️ Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/danilofreitas77/projeto-geladreira-inteligente.git
   cd projeto-geladreira-inteligente

2. Crie e ative o ambiente virtual:

python -m venv venv
venv\Scripts\activate  # (Windows)
source venv/bin/activate  # (Linux/Mac)

3. Instale as dependências:

pip install -r requirements.txt

4. Rode as migrações:

python manage.py migrate

5. Crie um superusuário (para acessar o admin):

python manage.py createsuperuser

6. Inicie o servidor:

python manage.py runserver

7. Acesse no navegador:

http://127.0.0.1:8000


## 📧 Envio de Relatórios

Cada morador terá um e-mail cadastrado.

Após a compra, o sistema gera um relatório e envia para o morador.

## 📌 Próximos Passos

Melhorar a interface do usuário.

Adicionar mais categorias de produtos.

Implementar histórico de compras.

Criar painel de administração mais amigável.


💡 Projeto desenvolvido para aprendizado prático de Django e entregue como trabalho acadêmico.

## 👨‍💻 Autor

Projeto desenvolvido por Danilo Freitas
 — estudante de ADS, explorando Django na prática 🚀.