🧊 Projeto Geladeira Inteligente

Sistema desenvolvido em Django para simular o funcionamento de uma geladeira inteligente em um condomínio.
Permite o cadastro de produtos, login de moradores via QR Code, adição de itens ao carrinho e envio de relatórios de compra por e-mail.

🚀 Funcionalidades

🔑 Login com QR Code para moradores.

🛒 Carrinho de compras com seleção de produtos.

📦 Cadastro de produtos (nome, quantidade, valor e categoria).

📧 Envio automático de relatório de compras por e-mail ao morador.

📊 Administração via Django Admin para gerenciamento de estoque.

🛠️ Tecnologias Utilizadas

Python 3.x

Django

SQLite (banco de dados padrão do Django)

Git & GitHub (controle de versão)

⚙️ Como rodar o projeto localmente

Clone o repositório:

git clone https://github.com/danilofreitas77/projeto-geladreira-inteligente.git
cd projeto-geladreira-inteligente


Crie e ative o ambiente virtual:

python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac


Instale as dependências:

pip install -r requirements.txt


Rode as migrações:

python manage.py migrate


Crie um superusuário para acessar o Django Admin:

python manage.py createsuperuser


Inicie o servidor:

python manage.py runserver


Acesse no navegador:

http://127.0.0.1:8000/

📌 Próximos Passos

 Criar interface para escolha de categorias no menu.

 Melhorar design do frontend (templates).

 Adicionar suporte a pagamento simulado.

 Implementar histórico de compras.

👨‍💻 Autor

Projeto desenvolvido por Danilo Freitas
 — estudante de ADS, explorando Django na prática 🚀.