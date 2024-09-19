# Minha API

Esse é meu projeto MVP da disciplina **Desenvolvimento Full Stack Básico**.

A intenção foi criar um ambiente que pudesse receber dois tipos de usuários:
Convidados, para poderem confirmar presença no evento, além de obterem informações sobre o casamento.
E principalmente para a administração do evento poder gerir os convites e os funcionários.

---
## Com front-end
A versão completa do meu projeto depende de APIs para carregar algumas seções da página.
Portanto, fiz uma versão simplificada que pudesse atender a 'Observação nº 3' dos requisitos do MVP.

Vou explicar como acessar ambas as versões:
Basta no início do arquivo app.py, deixar não comentado o diretório desejado.

# Para a versão simplificada: #
    app = Flask(__name__, template_folder='../front_end', static_folder='../front_end')

# Para a versão completa: #
    app = Flask(__name__, template_folder='../front_end/versão-completa/templates', static_folder='../front_end/versão-completa')

---

## Como executar a API

Primeiramente, vá no diretório raiz, pelo terminal, para executar os comandos.

```
> É importante o uso de ambientes virtuais tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
No terminal instale todas as libs necessárias presentes em `requirements.txt`.

Para isso, basta executar o comando:
(env)$ pip install -r requirements.txt

```
Feito isso, pode executar a API:
(env)$ flask run --host 0.0.0.0 --port 5000

```
Executado e tudo dando certo, só colar [http://127.0.0.1:5000] no navegador.
