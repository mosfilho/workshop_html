# workshop_html

Estudo guiado para iniciantes em HTML/CSS

### Estrutura de Pasta
```
Estrutura de pastas do projeto inicial
  html_css
    |__ css
    |__ img
    |__ js
        index.html
  jquery
    |_ js
       index.html
```
### Tips

#### CSS

##### Links úteis
Seletores CSS: https://www.w3schools.com/cssref/css_selectors.asp 

#### JS

##### Conceitos de JS que tem que estar dominado!

1. Global/Local Scopes/Closure
2. this/new/window
3. Async/Sync
4. AJAX
5. promisses vs callbacks
6. JQuery

##### Links úteis

JQuery AJAX: https://www.w3schools.com/jquery/jquery_ajax_get_post.asp


### Django

Agora o bicho vai pegar!

1. Crie um ambiente virtual com python3 dentro da pasta django e ative-o
2. Com o ambiente ativado, rode: 
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt # instala pacotes
    ```
3. Só para conhecimento: se quizesse começar um novo projeto django 'crediario'
    ```bash
    django-admin startproject crediario .
    ```
4. Crie um schema com seu nome no banco de dados (conexão no template abaixo)

5. Instale xclip. O que ele faz? Ele copia para o "Ctrl+V" a saída de um comando (poderia ser um "cat", um "echo"...)
    ```bash
    sudo apt install xclip
    ```

6. Pegar uma nova chave secreta (SECRET_KEY) (ainda não estamos utilizando o shell_plus) (Olha que estou copiando a saída do comando com o xclip, então não copie mais nada, pois perderemos o "Crtl+V")
    ```bash
    curl -s https://gist.githubusercontent.com/henriquebastos/11cf99c1bbc70bacf73a/raw/f3f6e190cdad1b30556916e9149eec6253f610c2/secret_gen.py | python | xclip -selection clipboard
    ```    

7. Crie um arquivo .env dentro da pasta crediario utilizando este template. No lugar de "SEU_NOME" coloque o schema que você criou e no "SUA_SECRET_KEY" cole o resultado do "Ctrl+C" gerado no comando acima
   
   ```conf
   DATABASE_URL=postgres://usr_aplicacao:aplicacao@172.16.2.89:5457/dbaimp?currentSchema=SEU_NOME
   DEBUG=True
   SECRET_KEY=SUA_SECRET_KEY
   ```

8. Com ambiente ativado e dentro da pasta crediario, execute o comando para rodar o servidor do django (olhar os Tips abaixo, hora mais!)

9. Se roudou tudo certinho, aplique as migrações que o django já tem para executar (Tips e mais tips!)


#### Tips
Rodar servidor na porta 8000
```bash
cd django
./manage.py runserver 0.0.0.0:8000
```

Gerar migrações
```bash
cd django
./manage.py makemigrations
```

Aplicar migrações
```bash
cd django
./manage.py migrate
```