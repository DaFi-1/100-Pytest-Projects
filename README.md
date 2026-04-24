# 🧪 TDD com Pytest — 100 Projetos Práticos 



 
<p align="center">
  <img src="res/LogoEbook.png" width="300" style="display:inline-block;"/>
  <img src="https://docs.pytest.org/en/stable/_static/pytest1.png" width="400" style="display:inline-block;"/>
</p>

### nao foi usado ia neste reposiitorio, este repositorio dedicado ao estudo de pytest ee aplicacos do TDD

Este repositório foi criado com base no estudo do livro  **Test-Driven Development: By Example**, de Kent Beck, com o objetivo de aplicar na prática os conceitos de **Desenvolvimento Guiado por Testes (TDD)** utilizando pytest.

A proposta consiste em **100 projetos/exercícios**, cada um explorando diferentes cenários e mecânicas de teste, sempre seguindo o ciclo fundamental do TDD:

> Red → Green → Refactor

Ao longo dos projetos, são abordados:

- Criação de testes antes da implementação  
- Escrita de código orientada a testes  
- Refatoração contínua  
- Uso de mocks e isolamento de dependências  
- Parametrização e organização de testes  
- Boas práticas de design para código testável  

Mais do que aprender uma ferramenta como o pytest, este repositório tem como foco desenvolver uma mentalidade de engenharia de software baseada em **testabilidade, simplicidade e feedback rápido**.

Este projeto funciona tanto como laboratório de aprendizado quanto como portfólio, demonstrando a aplicação prática de TDD em Python.
<hr>


> ⚠️ **Disclaimer**  
> This repository is a TDD study project using pytest.  
> AI tools were used exclusively to generate the functions under test in order to speed up scenario creation.  
> All test cases and development following the Red-Green-Refactor cycle were written manually.
## 1 - test unitario de uma funcao  de soma


```python
import pytest

def sum(x: int, y: int) -> int:
    return x + y

def test_sum_succes() -> None:
    assert sun(10,10) == 20 
```

veja que eu fiz um test unitario, todo test unitario eee unicamente unico nao depende de nada para fuciona apenas a propria funcao. 

## 2 - testando varios parametros em um unico test unitariio

```python
import pytest

def sum(x: int, y: int) -> int:
    return x + y

@pytest.mark.parametrize('x , y, output',[
    (1,1,2),
    (2,2,4),
    (10,10,20),
])
def test_sum_succes(x, y, output) -> None:
    assert sun(x, y) == output 

-------------- pytest  output --------------
main.py::test_sum_succes[1-1-2] PASSED
main.py::test_sum_succes[2-2-4] PASSED
main.py::test_sum_succes[10-10-20] PASSED
```

com o decorador **@pytest.mark.parametrize()** podemos simular varias chamadas de um mesmo test com varios argumentos diferentes

## 3 - testando a existencia de docstring na funcao sum

```python
import pytest

def sum(x: int, y: int) -> int:
    """function for sum two numbers inter"""
    return x + y

def test_docstring_exist() -> None:
    assert sum.__doc__ is not None
```

para pegar aaa docstring de uma funccao usamos **func.__doc__** , se nao tiver docstring retorna **None**

## 4 - Organizando varios test em uma unica classe

```python
import pytest

def sum(x: int, y: int) -> int:
    """function for sum two numbers inter"""
    return x + y

class TestSum:

    def test_sum_succes(self) -> None:
        assert sum(10,10) == 20

    @pytest.mark.parametrize('x , y, output',[
        (1,1,2),
        (2,2,4),
        (10,10,20),
    ])
    def test_sum_succes(self, x, y, output) -> None:
        assert sum(x, y) == output 

    def test_docstring_exist(self, ) -> None:
        assert sum.__doc__ is not None

-------------- pytest  output --------------
main.py::TestSum::test_sum_succes[1-1-2] PASSED
main.py::TestSum::test_sum_succes[2-2-4] PASSED
main.py::TestSum::test_sum_succes[10-10-20] PASSED
main.py::TestSum::test_docstring_exist PASSED
```
toda classe de test do pytest comeca ccom **Test...** ee todos os methhodos dessa clase tem aaa propria instaccia da ccalsse como argumento **self**, ao criar uma clase de o nommme Test--- seguido do nome da funcao, para ajudar na legibilidade de outras pessoas ao ler os test

veja que eu coloquei todos os test ateriores em uma unica cclasse que faz mencao aaa uma unica fuccao par a ser testada

## 6 - Refatorando aaa funcao para aceitar entradas diferentes

```python
import pytest

def sum(x: int, y: int) -> int | None:
    """
        function for sum two numbers inter
        return None, funciont faling
    """
    if isinstance(x, int) and  isinstance(y, int):
        return x + y

    return None

class TestSumError:
    def test_sum_error(self) -> None:
        assert sum('',10) == None 

-------------- pytest  output --------------
main.py::TestSumError::test_sum_error PASSED
```
Devemos fazer uma cobertura de uma funcao , testando todos os aspectos dela para garantir que essa funcao nao vai subir um erro em futuras implementaacoes seija la quais sejanm.vamos fazer test para que aaa funcao falhe eee podemos implementar melhorias refatorando aaa funcao original que estar sendo tesssstada., vamos da como argumentot uma string , logo erro vai subir , podemos refatorar aaa funcao para um situacao mais geral de uso real ou de falhas no nosso software.

## 7 - fortificando  o test de validadcao de varias entradas

```python
def sum(x: int, y: int) -> int | None:
    """
        function for sum two numbers inter
        return None, funciont faling
    """
    if isinstance(x, int) and  isinstance(y, int):
        return x + y

    return None

class TestSumError:

    @pytest.mark.parametrize('x, y, output',[
        ([],     '', None),
        ([1],   '0', None),
        ((),     "", None),
        ({},     [], None),
        (int,   int, None),
        (bool, bool, None),

    ])
    def test_sum_error(self, x, y, output) -> None:
        assert sum(x, y) == output 

-------------- pytest  output --------------
main.py::TestSumError::test_sum_error[x0--None] PASSED
main.py::TestSumError::test_sum_error[x1-0-None] PASSED
main.py::TestSumError::test_sum_error[x2--None] PASSED
main.py::TestSumError::test_sum_error[x3-y3-None] PASSED
main.py::TestSumError::test_sum_error[int-int-None] PASSED
main.py::TestSumError::test_sum_error[bool-bool-None] PASSED
```

Vamos aogra fazer aaa Parametrizaçãon para garantir que nao vai da erro com diferentes entrasas

## 8 - funcao de emviar uma messagem

```python
import pytest

def send_message(phone: str) -> bool:
    """phone: 99 9999 9999"""
    print('send OK')
    return True

class TestSendMessage:

    def test_strin_phone(self) -> None:
        assert send_message('99 9999 9999') 

-------------- pytest  output --------------
main.py::TestSendMessage::test_strin_phone send OK
PASSED
```

agora vamos fazer uma funcao que envia uma messagem para um string coom um simples test se aaa funcao enviou uma message, veja que nossa funcao retorna sempre treue pos nao aaa test que induza o erro ee por conseguenica aaa refatoracao para melhorar o codigo

## 9 - Refatorando a funcao de messagem

```python
import pytest

def send_message(phone: str) -> bool:
    """phone: 99 9999 9999"""
    if isinstance(phone, str):
        print('send OK')
    return False 

class TestSendMessage:
    @pytest.mark.parametrize('x',[
        (10),
        (''),
        ('1'),
        ([]),
        ('99 9999 9999'),
    ])
    def test_strin_phone(self, x) -> None:
        assert not send_message(x) 

-------------- pytest  output --------------
collected 5 items                                                                                                                                             
main.py .send OK
.send OK
..send OK
.
```

percepa que eu regatorei aa funcao conforme aa necessidade dos test, por isso chamamos de Desenvolvimento orientado por test, isso minnimizar vizitar o codig omais targe ee melhora  aaa confiabilidade eee legibilidade para outras pessoas

## 10 - Refatorando a funcao de messagem

```python
import os
import pytest

def create_dir(pathdir: str) -> None:
    os.makedirs(pathdir,exist_ok=True)

class TestCreateDir:

    def test_strin_phone(self) -> None:
        # criar o dir 
        create_dir("./testDir") 
        # verifica se o dir existe
        if os.path.isdir("./testDir"):
            # caso o dir exista, sera apagado logo em seguida
            os.rmdir("./testDir")

-------------- pytest  output --------------
main.py::TestCreateDir::test_strin_phone PASSED                                                                                                         [100%]
```

Agora como testar uma fucao que depende de outar funcao ?, podemos simplismete usar fazer um test normal, criando u[] pasta eee logo em seguida testar se o dir foi criado  eee apagalo logo em seguida como o cogigo aaa cima 

## 11 - como usar mock 

```python
import os
import pytest

def create_dir(pathdir: str) -> None:
    os.makedirs(pathdir,exist_ok=True)

class TestCreateDir:

    def test_strin_phone(self, mocker) -> None:
        # objeto fake da funcao sobrescrita
        fake = mocker.patch('main.os.makedirs')
        create_dir('./FakeDir')
        #verifica se create_dir chamou os.makedirs corretamente
        fake.assert_called_once_with('./FakeDir', exist_ok=True)

-------------- pytest  output --------------
main.py::TestCreateDir::test_strin_phone PASSED                                                                                                         [100%]
```

podemos usar o conceito de mock para trocar aa funcao dee dentor poooooooor um retorno conheciddo eee simular oo conportamento desejado ou conhecido.
vou usar o plugin do pytest **pytest-mock**

## 12 - plugin pytest-mock 

```python
import os

class UnixFS:

    @staticmethod
    def rm(filename):
        os.remove(filename)

def test_unix_fs(mocker):
    mocker.patch('os.remove')
    UnixFS.rm('file')
    os.remove.assert_called_once_with('file')
```

Veja o exemplo que o pytest-mock da na sua documentacao, o pytest-mock tambem tem coiasas como  **spy**, **stub**. em uma vennv do pythonn voce poode iiiinstalar o pytest-moc com pip install pytest-mock

## 13 - pytest-cov 

```python
import os

def is_valid_user(user: str) -> bool:
    return user == "admin"

def log_access(user: str) -> None:
    with open("log.txt", "a") as f:
        f.write(f"{user} accessed\n")

def access_system(user: str) -> str:
    if not is_valid_user(user):
        log_access(user)
        return "DENIED"

    if os.path.exists("maintenance.flag"):
        return "SYSTEM OFFLINE"

    return "ACCESS GRANTED"

class TestIsValidUser:

    def test_is_admin(self) -> None:
        assert is_valid_user('admin')

    def test_is_not_admin(self) -> None:
        assert is_valid_user('user') == False

class TestLogAcess:

    def test_acess(self, mocker) -> None:
        fake = mocker.patch('builtins.open', mocker.mock_open())
        log_access('user')
        fake.assert_called_once_with('log.txt', 'a')
        fake().write.assert_called_once_with('user accessed\n')


---------------- pytest  output ----------------
main.py::TestIsValidUser::test_is_admin PASSED
main.py::TestIsValidUser::test_is_not_admin PASSED
main.py::TestLogAcess::test_acess PASSED

-------------- pytest-cov  output --------------

Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      24      6    75%   11-18
---------------------------------------
TOTAL        24      6    75%

```

podemos usar o pytest-cov para ver  aaa corbertura de test da nossa aplicacao para melhor legibilidade
veja que falta testar aaa linha 10 aa 18 , essa linha ou esse trecho de codig ainda nnao foi feito uma tesssssst aaa respeito

## 14 - pytest-cov pesistente 

```python
import os

def is_valid_user(user: str) -> bool:
    return user == "admin"

def log_access(user: str) -> None:
    with open("log.txt", "a") as f:
        f.write(f"{user} accessed\n")

def access_system(user: str) -> str:
    if not is_valid_user(user):
        log_access(user)
        return "DENIED"

    if os.path.exists("maintenance.flag"):
        return "SYSTEM OFFLINE"

    return "ACCESS GRANTED"

class TestIsValidUser:

    def test_is_admin(self) -> None:
        assert is_valid_user('admin')

    def test_is_not_admin(self) -> None:
        assert is_valid_user('user') == False

class TestLogAcess:

    def test_acess(self, mocker) -> None:
        fake = mocker.patch('builtins.open', mocker.mock_open())
        log_access('user')
        fake.assert_called_once_with('log.txt', 'a')
        fake().write.assert_called_once_with('user accessed\n')

class TestAcessSystem:

    def test_access_is_valid_user(self, mocker) -> None:
        fake1 = mocker.patch('main.is_valid_user', return_value=True)
        fake2 = mocker.patch('main.log_access')
        access_system('user')
        fake1.assert_called_once_with('user')


---------------- pytest  output ----------------
main.py::TestIsValidUser::test_is_admin PASSED
main.py::TestIsValidUser::test_is_not_admin PASSED
main.py::TestLogAcess::test_acess PASSED
main.py::TestAcessSystem::test_access_is_valid_user PASSED


-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      31      3    90%   12-13, 16
---------------------------------------
TOTAL        31      3    90%
```

perceba que o cov cobriu so aass linhas que eu testei eee ainda falta aa continuacao de um if ee um return 
linhas 12-13, 16 , perceba que aaa linha 12 eee 13 nao foram testada mesmo fazend um if validar

## 15 - Dois mock em um mesmo test 

```python
import os

def is_valid_user(user: str) -> bool:
    return user == "admin"

def log_access(user: str) -> None:
    with open("log.txt", "a") as f:
        f.write(f"{user} accessed\n")

def access_system(user: str) -> str:
    if is_valid_user(user):
        log_access(user)
        return "DENIED"

    if os.path.exists("maintenance.flag"):
        return "SYSTEM OFFLINE"

    return "ACCESS GRANTED"

class TestIsValidUser:

    def test_is_admin(self) -> None:
        assert is_valid_user('admin')

    def test_is_not_admin(self) -> None:
        assert is_valid_user('user') == False

class TestLogAcess:

    def test_acess(self, mocker) -> None:
        fake = mocker.patch('builtins.open', mocker.mock_open())
        log_access('user')
        fake.assert_called_once_with('log.txt', 'a')
        fake().write.assert_called_once_with('user accessed\n')

class TestAcessSystem:

    def test_access_is_valid_user(self, mocker) -> None:
        fake1 = mocker.patch('main.is_valid_user', return_value=True)
        fake2 = mocker.patch('main.log_access')
        access_system('admin')
        # mock 'main.is_valid_user'
        fake1.assert_called_once_with('admin')
        # mock main.log_access
        fake2.assert_called_once_with('admin')

---------------- pytest  output ----------------
main.py::TestIsValidUser::test_is_admin PASSED
main.py::TestIsValidUser::test_is_not_admin PASSED
main.py::TestLogAcess::test_acess PASSED
main.py::TestAcessSystem::test_access_is_valid_user PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      31      3    90%   15-18
---------------------------------------
TOTAL        31      3    90%
```

perceba que eu fiz dois mocks em um unico test para validar o test unitraio sem dependências externas ou de IO
veja que aa linha do return 'DENIED' passa sem nem mosmo testala no codigo ou eu testar esse retorno, vou fazer isso logo em seguida

## 16 -  

```python
import os

def is_valid_user(user: str) -> bool:
    return user == "admin"

def log_access(user: str) -> None:
    with open("log.txt", "a") as f:
        f.write(f"{user} accessed\n")

def access_system(user: str) -> str:
    if is_valid_user(user):
        log_access(user)
        return "DENIED"

    if os.path.exists("maintenance.flag"):
        return "SYSTEM OFFLINE"

    return "ACCESS GRANTED"

class TestIsValidUser:

    def test_is_admin(self) -> None:
        assert is_valid_user('admin')

    def test_is_not_admin(self) -> None:
        assert is_valid_user('user') == False

class TestLogAcess:

    def test_acess(self, mocker) -> None:
        fake = mocker.patch('builtins.open', mocker.mock_open())
        log_access('user')
        fake.assert_called_once_with('log.txt', 'a')
        fake().write.assert_called_once_with('user accessed\n')

class TestAcessSystem:

    def test_access_is_valid_user(self, mocker) -> None:
        fake1 = mocker.patch('main.is_valid_user', return_value=True)
        fake2 = mocker.patch('main.log_access')
        assert access_system('admin') == 'DENIED'
        # mock 'main.is_valid_user'
        fake1.assert_called_once_with('admin')
        # mock main.log_access
        fake2.assert_called_once_with('admin')

    def test_file_exist(self,  mocker) -> None:
        fake = mocker.patch('main.os.path.exists', return_value=True)
        assert access_system('maintenance.flag') == 'SYSTEM OFFLINE'
        # mock main.os.path.exists
        fake.assert_called_once_with("maintenance.flag")

---------------- pytest  output ----------------
main.py::TestIsValidUser::test_is_admin PASSED
main.py::TestIsValidUser::test_is_not_admin PASSED
main.py::TestLogAcess::test_acess PASSED
main.py::TestAcessSystem::test_access_is_valid_user PASSED
main.py::TestAcessSystem::test_file_exist PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      35      1    97%   18
---------------------------------------
TOTAL        35      1    97%
```

veja que para irmos para o segundo if precisamoos que o primeiro if venha aaa falhar 

## 17 -  falta apenas Uma unica linha

```python
import os

def is_valid_user(user: str) -> bool:
    return user == "admin"

def log_access(user: str) -> None:
    with open("log.txt", "a") as f:
        f.write(f"{user} accessed\n")

def access_system(user: str) -> str:
    if is_valid_user(user):
        log_access(user)
        return "DENIED"

    if os.path.exists("maintenance.flag"):
        return "SYSTEM OFFLINE"

    return "ACCESS GRANTED"

class TestIsValidUser:

    def test_is_admin(self) -> None:
        assert is_valid_user('admin')

    def test_is_not_admin(self) -> None:
        assert is_valid_user('user') == False

class TestLogAcess:

    def test_acess(self, mocker) -> None:
        fake = mocker.patch('builtins.open', mocker.mock_open())
        log_access('user')
        fake.assert_called_once_with('log.txt', 'a')
        fake().write.assert_called_once_with('user accessed\n')

class TestAcessSystem:

    def test_access_is_valid_user(self, mocker) -> None:
        fake1 = mocker.patch('main.is_valid_user', return_value=True)
        fake2 = mocker.patch('main.log_access')
        assert access_system('admin') == 'DENIED'
        # mock 'main.is_valid_user'
        fake1.assert_called_once_with('admin')
        # mock main.log_access
        fake2.assert_called_once_with('admin')

    def test_file_exist(self,  mocker) -> None:
        fake = mocker.patch('main.os.path.exists', return_value=True)
        assert access_system('user') == 'SYSTEM OFFLINE'
        # mock main.os.path.exists
        fake.assert_called_once_with("maintenance.flag")

    def test_finally_return(self,  mocker) -> None:
        fake1 = mocker.patch('main.is_valid_user', return_value=False)
        fake2 = mocker.patch('main.os.path.exists', return_value=False)
        assert access_system('user') == 'ACCESS GRANTED'
        fake1.assert_called_once_with("user")

---------------- pytest  output ----------------
main.py::TestIsValidUser::test_is_admin PASSED
main.py::TestIsValidUser::test_is_not_admin PASSED
main.py::TestLogAcess::test_acess PASSED
main.py::TestAcessSystem::test_access_is_valid_user PASSED
main.py::TestAcessSystem::test_file_exist PASSED
main.py::TestAcessSystem::test_finally_return PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      40      0   100%
---------------------------------------
TOTAL        40      0   100%
```

para validar essa unica linha precisamoos que os dois primeiros if venha aa falhar  

## 18 -  

```python

def start_server():
    global server,HOST,PORT
    server = HTTPServer((HOST, PORT), SimpleCORSHandler)
    dpg.set_value("logserverstatus",f"http://{HOST}:{PORT}")
    server.serve_forever()


class TestStartServer:

    def test_cehck_start_server(self, mocker) -> None:
        fake_server = mocker.Mock()
        fake1 = mocker.patch(
            'toolbox.tools.addnumber.HTTPServer',
            return_value=fake_server,
        )
        fake2 = mocker.patch('toolbox.tools.addnumber.dpg.set_value')

        addnumber.start_server()

        fake1.assert_called_once()
        fake_server.serve_forever.assert_called_once()
        fake2.assert_called_once()
```

## 19 -  toggle_server 

```python
def toggle_server(sender, app_data, user_data):
    global server_thread, server, phones_list

    if sender == "serverON":
        if server_thread is None or not server_thread.is_alive():
            server_thread = threading.Thread(target=start_server, daemon=True)
            server_thread.start()
            dpg.configure_item("logserverstatus", color=(0, 255, 0, 255))  

    else:  # checkbox desmarcado
        if server:
            server.shutdown()
            server = None
            dpg.set_value("logserverstatus","STOP")
            dpg.configure_item("logserverstatus", color=(255, 0, 0, 255))  

class TestToggleServer:

    def test_toggle_server_on(self, mocker):
        # fake thread
        fake_thread = mocker.Mock()
        fake_thread.is_alive.return_value = False

        thread_cls = mocker.patch(
            'toolbox.tools.addnumber.threading.Thread',
            return_value=fake_thread
        )

        config = mocker.patch(
            'toolbox.tools.addnumber.dpg.configure_item'
        )

        # estado inicial
        import toolbox.tools.addnumber as mod
        mod.server_thread = None

        # call
        mod.toggle_server("serverON", None, None)

        # asserts
        thread_cls.assert_called_once()
        fake_thread.start.assert_called_once()
        config.assert_called_once()

    def test_toggle_server_on_already_running(self, mocker):
        fake_thread = mocker.Mock()
        fake_thread.is_alive.return_value = True

        mocker.patch('toolbox.tools.addnumber.threading.Thread')
        mocker.patch('toolbox.tools.addnumber.dpg.configure_item')

        import toolbox.tools.addnumber as mod
        mod.server_thread = fake_thread

        mod.toggle_server("serverON", None, None)

        fake_thread.start.assert_not_called()

    def test_toggle_server_off(self, mocker):
        shutdown = mocker.Mock()

        fake_server = mocker.Mock()
        fake_server.shutdown = shutdown

        set_value = mocker.patch(
            'toolbox.tools.addnumber.dpg.set_value'
        )

        config = mocker.patch(
            'toolbox.tools.addnumber.dpg.configure_item'
        )

        import toolbox.tools.addnumber as mod
        mod.server = fake_server

        mod.toggle_server("serverOFF", None, None)

        shutdown.assert_called_once()
        set_value.assert_called_once_with("logserverstatus", "STOP")
        config.assert_called_once()
        assert mod.server is None

    def test_toggle_server_off_no_server(self, mocker):
        mocker.patch('toolbox.tools.addnumber.dpg.set_value')
        mocker.patch('toolbox.tools.addnumber.dpg.configure_item')

        import toolbox.tools.addnumber as mod
        mod.server = None

        mod.toggle_server("serverOFF", None, None)

```

achei bem confuso testarr isso nao identi muit bem o pq do import toolbox.tools.addnumber as mod, sendo que foi recomendaacao do LLM
sera que eu poderai usar um mocker.Mock() ee atribuir esses method eee esse testt passsaria? fica essa duvida que posteriomente eu voou tirar


## 20 - tratando erros  

```python
import pytest 

def add(x: int, y: int) -> int:
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    raise Exception ('Esta funcao so aceita valores inteiros..')

class TestAdd:

    def test_true_add(self) -> None:
        assert add(10,10) == 20

    def test_add_error_msg(self) -> None:
        with pytest.raises(Exception) as error:
            add(1.0,1.0)
        assert str(error.value) == 'Esta funcao so aceita valores inteiros..'

---------------- pytest  output ----------------
main.py::TestAdd::test_true_add PASSED
main.py::TestAdd::test_add_error_msg PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover
-----------------------------
main.py      12      0   100%
-----------------------------
TOTAL        12      0   100%
```

vemos nesse test que temos dois test apra validar todos os casos da funcao eee suas unicas possiveis solucoes ou saidas, entao um erro tambem ee uma saida
sim, o erro tabem &uma saida valida ele nos dis como aaa funcao se comporta caso nao for passao os argumentos desejados um  erro
vai saltar na tela do Desenvolvedor eee ajudalo aaa progredir no godigo 

## 21 - proposto pelo livro Tdd de estudo 

```python
import pytest 

def add(x: int, y: int) -> int:
    if isinstance(x, int) and isinstance(y, int):
        return x - y
    raise Exception ('Esta funcao so aceita valores inteiros..')

class TestAdd:

    def test_true_sub(self) -> None:
        assert sub(10,10) == 20

    def test_sub_error_msg(self) -> None:
        with pytest.raises(Exception) as error:
            sub(1.0,1.0)
        assert str(error.value) == 'Esta funcao so aceita valores inteiros..'

---------------- pytest  output ----------------
main.py::TestSub::test_true_sub PASSED
main.py::TestSub::test_sub_error_msg PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover
-----------------------------
main.py      12      0   100%
-----------------------------
TOTAL        12      0   100%
```

este segue aa mesma ideia do de cima, foi proprosto pelo livro tambem como exerciio.

## 22 - mais um proposto pelo livro 

```python
import pytest 

def mult(x: int, y: int) -> int:
    if isinstance(x, int) and isinstance(y, int):
        return x * y
    raise Exception ('not mult..')

class Testmult:

    def test_true_mult(self) -> None:
        assert mult(10,10) == 20

    def test_mult_error_msg(self) -> None:
        with pytest.raises(Exception) as error:
            mult(1.0,1.0)
        assert str(error.value) == 'not mult..'


---------------- pytest  output ----------------
main.py::Testmult::test_true_mult PASSED
main.py::Testmult::test_mult_error_msg PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover
-----------------------------
main.py      12      0   100%
-----------------------------
TOTAL        12      0   100%
```

so mais um proproto no capilo 26 do livro que eu setou usando como basse nos estudos de pytest

## 23 - Testando uma api 

```python
import requests
import pytest

def get_user_name(user_id: int) -> str:
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{user_id}")

    if response.status_code != 200:
        raise Exception("Erro ao buscar usuário")

    data = response.json()
    return data['title']


class TestGetUserName:

    def test_reponse_error(self, mocker) -> None:
        fake_response = mocker.Mock()
        fake_response.status_code = 400
        fake = mocker.patch('main.requests.get', side_effect=fake_response)

        with pytest.raises(Exception) as error:
            get_user_name('1')
        assert str(error.value) == "Erro ao buscar usuário"

        fake.assert_called_once_with('https://jsonplaceholder.typicode.com/todos/1')

    def test_reponse_200(self, mocker) -> None:
        fake_response = mocker.Mock()
        fake_response.status_code = 200
        fake_response.json.return_value = {
            'userId': 1, 
            'id': 1, 
            'title': 'delectus aut autem', 
            'completed': False
        }
        fake = mocker.patch('main.requests.get', side_effect=[fake_response])
        assert get_user_name('1') == 'delectus aut autem'
        fake.assert_called_once_with('https://jsonplaceholder.typicode.com/todos/1')

---------------- pytest  output ----------------
main.py::TestGetUserName::test_reponse_error PASSED
main.py::TestGetUserName::test_reponse_200 PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      24      0   100%
---------------------------------------
TOTAL        24      0   100%
```

vamos mocar uma funcao que faz uma chamda aaa API gratuira https://jsonplaceholder.typicode.com/ 
estar api nos devolve dados vamos comparar o retorno no final

## 24 -  testando outras possibilidadas

```python
import pytest
import requests

def get_user_posts_titles(user_id: int) -> list[str]:
    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Erro ao buscar posts")

    data = response.json()

    if not data:
        return []

    return [post["title"] for post in data]
get_user_posts_titles(1)
class TestGetUserPostsTitles:

    def test_error(self, mocker) -> None:
        fake_response = mocker.Mock()
        fake_response.status_code = 400
        fake = mocker.patch('main.requests.get', side_effect=[fake_response])
        with pytest.raises(Exception) as error:
            get_user_posts_titles(1)
        fake.assert_called_once_with('https://jsonplaceholder.typicode.com/posts?userId=1')

    def test_not_data(self, mocker) -> None:
        fake_response = mocker.Mock()
        fake_response.status_code = 200
        fake_response.json.return_value = []
        fake = mocker.patch('main.requests.get', side_effect=[fake_response])
        assert get_user_posts_titles(1) == []
        fake.assert_called_once_with('https://jsonplaceholder.typicode.com/posts?userId=1')

---------------- pytest  output ----------------
main.py::TestGetUserPostsTitles::test_error PASSED
main.py::TestGetUserPostsTitles::test_not_data PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      26      1    96%   17
---------------------------------------
TOTAL        26      1    96%
```

mesmo test do outro, posrem fique atendo aa ao cov do pytest ele mostra aaa linha 17 como uma linha que nao foi testada
uma bom plugin do pytest para termos uma corbertura geral do nosso projeto 

## 25 - testando uma fake API

```python
import pytest
import requests

def enviar_mensagem(usuario: str, mensagem: str) -> bool:
    if not usuario or not mensagem:
        return False
    response = requests.post(
        "https://api.exemplo.com/send",
        json={"user": usuario, "message": mensagem},
        timeout=2
    )
    return response.status_code == 200

class TestEviarMesagem:

    def test_not_user(self) -> None:
        assert enviar_mensagem('', '') == False

    def test_user_check(self, mocker) -> None:
        fake_response = mocker.Mock()
        fake_response.status_code = 200
        fake = mocker.patch('main.requests.post', side_effect=[fake_response])
        assert enviar_mensagem('user', 'HEELO') == True 
        fake.assert_called == 1
        fake.assert_called_once()

---------------- pytest  output ----------------
main.py::TestEviarMesagem::test_not_user PASSED
main.py::TestEviarMesagem::test_user_check PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      17      0   100%
---------------------------------------
TOTAL        17      0   100%
```
nada de novo aqui

## 26 - Exemplo um da doc do pytest

```python
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5

---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```

Um simples test, estou lendo agora aaa documentacao do pytest, eu tava trreinando mock, mais aaa dock acabou,
entao eu vou ler aaa dock do pytest ir ir fazendo os tests da doc do pytest

## 27 - Exemplo dois da doc do pytest

```python
import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()

---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```

veja nesse pequeno exemplo aa doc do pytest me ensina aaa como capturar um erro para testalo, afinal um erro tambem eee um test valido

## 28 - ussndo @pytest.mark.skip

```python

import pytest

def soma(a, b):
    return a + b

@pytest.mark.skip('xxxxxxxxx')
def test_soma_1():
    assert soma(2, 2) == 4

@pytest.mark.skip('yyyyyy')
def test_soma_2():
    assert soma(0, 0) == 0

@pytest.mark.skip()
def test_soma_3():
    assert soma(-1, 1) == 0

@pytest.mark.skip
def test_soma_4():
    assert soma(-5, -5) == -10

@pytest.mark.skip
def test_soma_5():
    assert soma(100, 200) == 300

@pytest.mark.skip
def test_soma_6():
    assert soma(1.5, 2.5) == 4.0

@pytest.mark.skip
def test_soma_7('iiiiiii'):
    assert soma(-10, 5) == -5

@pytest.mark.skip
def test_soma_8():
    assert soma(0, 10) == 10

@pytest.mark.skip('aaaaaaaaaaaaaaaaaaa')
def test_soma_9():
    assert soma(999, 1) == 1000

@pytest.mark.skip('final')
def test_soma_10():
    assert soma(3.3, 3.3) == 6.6

---------------- pytest  output ----------------
main.py::test_soma_1 SKIPPED (xxxxxxxxx)
main.py::test_soma_2 SKIPPED (yyyyyy)
main.py::test_soma_3 SKIPPED (unconditional skip)
main.py::test_soma_4 SKIPPED (unconditional skip)
main.py::test_soma_5 SKIPPED (unconditional skip)
main.py::test_soma_6 SKIPPED (unconditional skip)
main.py::test_soma_7 SKIPPED (unconditional skip)
main.py::test_soma_8 SKIPPED (unconditional skip)
main.py::test_soma_9 SKIPPED (unconditional skip)
main.py::test_soma_10 SKIPPED (unconditional skip)

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      33     11    67%   7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47
---------------------------------------
TOTAL        33     11    67%
```

nessa parte eu aprendi como pular test com @pytest.mark.skip

## 29 - usando @pytest.mark.xfail

```python
import pytest

def soma(a, b):
    return a + b

def test_soma_normal():
    assert soma(2, 2) == 4

@pytest.mark.xfail(reason="bug simulado: soma está quebrada propositalmente")
def test_soma_quebrada():
    assert soma(2, 2) == 5

---------------- pytest  output ----------------
main.py::test_soma_normal PASSED
main.py::test_soma_quebrada XFAIL (bug simulado: soma está quebrada propositalmente)

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py       8      0   100%
---------------------------------------
TOTAL         8      0   100%
```

observanod o comportamento do @pytest.mark.xfail, ele serve para aceitar aaa falha de um test, ta uma tag para esse test
ele empede que aaa execucaos dos test pare em um test com bug ou falha conhecida

## 30 - testando errro parte 1

```python
import pytest

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("não pode dividir por zero")
    return a / b

class TestDividir:

    def test_dividir_error(self) -> None:
        with pytest.raises(ZeroDivisionError) as error:
            dividir(1,0)
        assert str(error.value) == "não pode dividir por zero"  

    @pytest.mark.parametrize('x, y, z',[
        (1,   1,  1/1 ),
        (1,  10,  1/10),
        (10, 10, 10/10),
    ])
    def test_dividir_success(self, x, y, z) -> None:
        assert dividir(x, y) == z

---------------- pytest  output ----------------
main.py::TestDividir::test_dividir_error PASSED
main.py::TestDividir::test_dividir_success[1-1-1.0] PASSED
main.py::TestDividir::test_dividir_success[1-10-0.1] PASSED
main.py::TestDividir::test_dividir_success[10-10-1.0] PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      13      0   100%
---------------------------------------
TOTAL        13      0   100%
```

## 31 - testando errro parte 2

```python
import pytest

def acessar_lista(lista: list, i: int) -> list:
    if i < 0:
        raise ValueError("índice negativo não permitido")
    return lista[i]

class TestAcessarLista:

    @pytest.mark.parametrize('x',[
        (-1),
        (-1.0),
    ])
    def test_error(self, x) -> None:
        with pytest.raises(ValueError) as error:
           acessar_lista(list(), x)
        assert str(error.value) == "índice negativo não permitido"

    @pytest.mark.parametrize('x, y',[
        (0, 1),
        (1, 1),
    ])
    def test_success(self, x, y) -> None:
        assert acessar_lista([1,1], x) == y

---------------- pytest  output ----------------
main.py::TestAcessarLista::test_error[-1] PASSED
main.py::TestAcessarLista::test_error[-1.0] PASSED
main.py::TestAcessarLista::test_success[0-1] PASSED
main.py::TestAcessarLista::test_success[1-1] PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      14      0   100%
---------------------------------------
TOTAL        14      0   100%
```

## 32 - testando errro parte 3

```python
import pytest

def converter_int(valor):
    if not isinstance(valor, str):
        raise TypeError("precisa ser string")
    return int(valor)

class TestAcessarLista:

    @pytest.mark.parametrize('x',[
        (3),
        (1),
    ])
    def test_error(self, x) -> None:
        with pytest.raises(TypeError) as error:
           converter_int(x)
        assert str(error.value) == "precisa ser string"


    @pytest.mark.parametrize('x, y',[
        (1.0, int(1.0)),
        (3.2, int(3.2)),
        (2.0, int(2.0)),
    ])
    def test_success(self, x, y) -> None:
        assert converter_int(x) == y

---------------- pytest  output ----------------
main.py::TestAcessarLista::test_error[-1] PASSED
main.py::TestAcessarLista::test_error[-1.0] PASSED
main.py::TestAcessarLista::test_success[0-1] PASSED
main.py::TestAcessarLista::test_success[1-1] PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      14      0   100%
---------------------------------------
TOTAL        14      0   100%
```

## 33 - testando errro parte 4

```python
import pytest

def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("saldo insuficiente")
    return saldo - valor

class TestSacar:

    @pytest.mark.parametrize('x, y',[
        (1,2),
        (1,3),
        (1,8),
    ])
    def test_error(self, x, y) -> None:
        with pytest.raises(ValueError) as error:
            sacar(x, y)
        assert str(error.value) == "saldo insuficiente"

    @pytest.mark.parametrize('x, y',[
        (2,1),
        (3,2),
        (8,4),
    ])
    def test_success(self, x, y) -> None:
        assert sacar(x, y) == x - y

---------------- pytest  output ----------------
main.py::TestSacar::test_error[1-2] PASSED
main.py::TestSacar::test_error[1-3] PASSED
main.py::TestSacar::test_error[1-8] PASSED
main.py::TestSacar::test_success[2-1] PASSED
main.py::TestSacar::test_success[3-2] PASSED
main.py::TestSacar::test_success[8-4] PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      14      0   100%
---------------------------------------
TOTAL        14      0   100%
```

## 34 - testando errro parte 5

```python
import pytest

def login(usuario, senha):
    if usuario == "" or senha == "":
        raise ValueError("campos vazios")
    if senha != "123":
        raise PermissionError("senha incorreta")
    return True

class TestLogin:

    @pytest.mark.parametrize('x, y',[
        ('',''),
    ])
    def test_string_enpty_error(self, x, y) -> None:
        with pytest.raises(ValueError) as error:
            login(x, y)
        assert str(error.value) == "campos vazios"

    @pytest.mark.parametrize('x, y',[
        ('uva','1233'),
    ])
    def test_pass_invalid_error(self, x, y) -> None:
        with pytest.raises(PermissionError) as error:
            login(x, y)
        assert str(error.value) == "senha incorreta"

    @pytest.mark.parametrize('x, y',[
        ('orange','123'),
    ])
    def test_success(self, x, y) -> None:
        assert login(x, y)

---------------- pytest  output ----------------
main.py::TestLogin::test_string_enpty_error[-] PASSED
main.py::TestLogin::test_pass_invalid_error[uva-1233] PASSED
main.py::TestLogin::test_success[orange-123] PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      21      0   100%
---------------------------------------
TOTAL        21      0   100%
```

## 35 - testando errro parte 6

```python
import pytest

def dividir_lista(lista):
    if len(lista) == 0:
        raise IndexError("lista vazia")
    return lista[0] / lista[1]

class TestDividirLista:

    @pytest.mark.parametrize('x',[
        ([]),
    ])
    def test_empty_list_error(self, x) -> None:
        with pytest.raises(IndexError) as error:
            dividir_lista(x)
        assert str(error.value) == "lista vazia"

    @pytest.mark.parametrize('x, y',[
        ([2,2], 2/2),
    ])
    def test_success(self, x, y) -> None:
        assert dividir_lista(x) == y

---------------- pytest  output ----------------
main.py::TestDividirLista::test_empty_list_error[x0] PASSED
main.py::TestDividirLista::test_success[x0-1.0] PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      14      0   100%
---------------------------------------
TOTAL        14      0   100%
```


## 36 - testando errro parte 7

```python
import pytest

def abrir_arquivo(nome):
    if not nome.endswith(".txt"):
        raise FileNotFoundError("arquivo inválido")
    return True

class TestAbrirArquivo:

    def test_error_invalid_file(self) -> None:
        with pytest.raises(FileNotFoundError) as error:
            abrir_arquivo('file.py')
        assert str(error.value) == 'arquivo inválido'

    def test_successd_file(self) -> None:
        assert abrir_arquivo('file.txt')

---------------- pytest  output ----------------
main.py::TestAbrirArquivo::test_error_invalid_file PASSED
main.py::TestAbrirArquivo::test_successd_file PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      12      0   100%
---------------------------------------
TOTAL        12      0   100%
```


## 37 - testando errro parte 8

```python
import pytest

def calcular_desconto(preco):
    if preco < 0:
        raise ValueError("preço negativo inválido")
    return preco * 0.9

class TestCalcularDesconto:

    def test_error(self) -> None:
        with pytest.raises(ValueError) as error:
            calcular_desconto(-1)
        assert str(error.value) == 'preço negativo inválido'

    def test_success(self) -> None:
        assert calcular_desconto(1) == 1 * 0.9 

---------------- pytest  output ----------------
main.py::TestCalcularDesconto::test_error PASSED
main.py::TestCalcularDesconto::test_success PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      12      0   100%
---------------------------------------
TOTAL        12      0   100%
```


## 38 - testando errro parte 9

```python
import pytest

def processar_id(id_user):
    if id_user is None:
        raise TypeError("id não pode ser None")
    return f"user-{id_user}"

class TestProcessarId:

    def test_error(self) -> None:
        with pytest.raises(TypeError) as error:
            processar_id(None)
        assert str(error.value) == "id não pode ser None"

    def test_success(self) -> None:
        assert processar_id('uva') == 'user-uva'

---------------- pytest  output ----------------
main.py::TestProcessarId::test_error PASSED
main.py::TestProcessarId::test_success PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      12      0   100%
---------------------------------------
TOTAL        12      0   100%
```


## 39 -  Fixture com mock

```python
import os
import requests
import pytest

def get_temperature(city: str) -> float:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API_KEY não definida")

    url = f"https://fake-weather-api.com/{city}?key={api_key}"
    response = requests.get(url)

    if response.status_code != 200:
        raise ConnectionError("Erro na API")

    data = response.json()

    if "temperature" not in data:
        raise KeyError('Resposta inválida')

    return data["temperature"]


class TestGetTemperature:

    @pytest.fixture
    def fake_response_erro(self, mocker) -> fake:
        fake = mocker.Mock()
        fake.status_code = 300
        fake.json.return_value = {} 
        return fake

    def test_error_not_found_api_key(self, mocker) -> None:
        fake = mocker.patch('main.os.getenv', return_value='')
        with pytest.raises(ValueError) as error:
            get_temperature('')
        assert str(error.value) == 'API_KEY não definida'

    def test_error_status_code_error(self, mocker, fake_response_erro) -> None:
        fake1 = mocker.patch('main.os.getenv', return_value='uva')
        fake1 = mocker.patch('main.requests.get', return_value=fake_response_erro)
        with pytest.raises(ConnectionError) as error:
            get_temperature('uva')
        assert str(error.value) == "Erro na API"

    def test_error_resonse_json(self, mocker, fake_response_erro) -> None:
        fake_response_erro.status_code = 200
        fake1 = mocker.patch('main.os.getenv', return_value='uva')
        fake2 = mocker.patch('main.requests.get', return_value=fake_response_erro)
        with pytest.raises(KeyError) as error:
            get_temperature('uva')

    def test_success(self, mocker, fake_response_erro) -> None:
        fake_response_erro.status_code = 200
        fake_response_erro.json.return_value = {"temperature": True} 
        fake1 = mocker.patch('main.os.getenv', return_value='uva')
        fake2 = mocker.patch('main.requests.get', return_value=fake_response_erro)
        assert get_temperature('uva')

---------------- pytest  output ----------------
main.py::TestGetTemperature::test_error_not_found_api_key PASSED
main.py::TestGetTemperature::test_error_status_code_error PASSED
main.py::TestGetTemperature::test_error_resonse_json PASSED
main.py::TestGetTemperature::test_success PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      45      0   100%
---------------------------------------
TOTAL        45      0   100%
```

nesse test ai eu tentei fazer um fixture para diminuir aaaa repeticao de codigo, uma fixture de um mock de response que atribui coiass aaa
ele dependendo do que o test precissa, ate agorra minha compreencao com fixture do pytest ee mais para impedir erpeticao de codigo nos test
gostei , deixa bem verboso parra outras pessoas..

## 40 - assert str(error.value.) == 'Resposta inválida'

```python
import os
import requests
import pytest

def get_temperature(city: str) -> float:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API_KEY não definida")

    url = f"https://fake-weather-api.com/{city}?key={api_key}"
    response = requests.get(url)

    if response.status_code != 200:
        raise ConnectionError("Erro na API")

    data = response.json()

    if "temperature" not in data:
        raise KeyError('Resposta inválida')

    return data["temperature"]

class TestGetTemperature:

    @pytest.fixture
    def fake_response_erro(self, mocker) -> fake:
        fake = mocker.Mock()
        fake.status_code = 300
        fake.json.return_value = {} 
        return fake

    def test_error_not_found_api_key(self, mocker) -> None:
        fake = mocker.patch('main.os.getenv', return_value='')
        with pytest.raises(ValueError) as error:
            get_temperature('')
        assert str(error.value) == 'API_KEY não definida'

    def test_error_status_code_error(self, mocker, fake_response_erro) -> None:
        fake1 = mocker.patch('main.os.getenv', return_value='uva')
        fake1 = mocker.patch('main.requests.get', return_value=fake_response_erro)
        with pytest.raises(ConnectionError) as error:
            get_temperature('uva')
        assert str(error.value) == "Erro na API"

    def test_error_resonse_json(self, mocker, fake_response_erro) -> None:
        fake_response_erro.status_code = 200
        fake1 = mocker.patch('main.os.getenv', return_value='uva')
        fake2 = mocker.patch('main.requests.get', return_value=fake_response_erro)
        with pytest.raises(KeyError) as error:
            get_temperature('uva')
        assert str(error.value.args[0]) == 'Resposta inválida'
        #assert str(error.value.) == 'Resposta inválida'

    def test_success(self, mocker, fake_response_erro) -> None:
        fake_response_erro.status_code = 200
        fake_response_erro.json.return_value = {"temperature": True} 
        fake1 = mocker.patch('main.os.getenv', return_value='uva')
        fake2 = mocker.patch('main.requests.get', return_value=fake_response_erro)
        assert get_temperature('uva')

---------------- pytest  output ----------------
main.py::TestGetTemperature::test_error_not_found_api_key PASSED
main.py::TestGetTemperature::test_error_status_code_error PASSED
main.py::TestGetTemperature::test_error_resonse_json PASSED
main.py::TestGetTemperature::test_success PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      46      0   100%
---------------------------------------
TOTAL        46      0   100%
```

um ponto para resaltaarr assert str(error.value.) == 'Resposta inválida' isso falha pq o python trada essa execao diferernte, 
todas ate agora foram normais pq essa levanta errro

## 41 - poderia ter usado um spy

```python
import os
import pytest

def enviar_dado(api, data):
    key = os.getenv("API_KEY")

    if not key:
        raise ValueError("sem chave")

    if not data:
        raise ValueError("sem dados")

    return 'send True' 

class TestEviarDados:

    def test_empty_key_error(self) -> None:
        with pytest.raises(ValueError) as error:
            enviar_dado('', '')

    def test_empty_data_error(self, mocker) -> None:
        fake = mocker.patch('main.os.getenv', return_value='abcd')
        with pytest.raises(ValueError) as error:
            enviar_dado('', '')

    def test_success(self, mocker) -> None:
        fake = mocker.patch('main.os.getenv', return_value='abcd')
        assert enviar_dado('y', 'y') == 'send True'

---------------- pytest  output ----------------
main.py::TestEviarDados::test_empty_key_error PASSED
main.py::TestEviarDados::test_empty_data_error PASSED
main.py::TestEviarDados::test_success PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      20      0   100%
---------------------------------------
TOTAL        20      0   100%
```
## 42 - Testar soma com números negativos

```python
import os 
import pytest

def soma_negativos(a, b):
    total = 0

    if a < 0:
        total += a
    else:
        total += a

    if b < 0:
        total += b
    else:
        total += b

    temp = total

    for _ in range(10):
        temp = temp + 0

    check = temp
    result = check

    for _ in range(10):
        result = result

    return result

class TestSomaNegativos:

    def test_menor_q_1(self) -> None:
        soma_negativos(-1,-1)

    def test_maior_q_1(self) -> None:
        soma_negativos(1,1)

    def test_forcar_runtime(self, mocker):
        # hack: alterar comportamento interno
        original = soma_negativos

        def fake(a, b):
            raise RuntimeError("erro interno")

        mocker.patch(__name__ + ".soma_negativos", fake)

        import pytest
        with pytest.raises(RuntimeError):
            soma_negativos(1, 2)



---------------- pytest  output ----------------
main.py::TestSomaNegativos::test_menor_q_1 PASSED
main.py::TestSomaNegativos::test_maior_q_1 PASSED
main.py::TestSomaNegativos::test_forcar_runtime PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      31      0   100%
---------------------------------------
TOTAL        31      0   100%
```

## 43 - Testar divisão por zero

```python
import pytest

def div(a, b):
    if b == 0:
        raise ValueError("divisão por zero")

    result = a

    for _ in range(10):
        result = result

    result = result / b

class TestDiv:

    def test_div_error(self,) -> None:
        with pytest.raises(ValueError) as error:
            div(1,0)
        assert str(error.value) == "divisão por zero"

    def test_return_none(self) -> None:
        assert div(1,1) == None

---------------- pytest  output ----------------
main.py::TestDiv::test_div_error PASSED
main.py::TestDiv::test_return_none PASSED


-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      16      0   100%
---------------------------------------
TOTAL        16      0   100%
```

## 44 - Testar função que retorna None

```python
import pytest

def retorna_none(x):
    if x > 0:
        val = x

        for _ in range(10):
            val = val

        return val

    temp = None

    for _ in range(15):
        temp = temp

    check = temp

    if check is None:
        pass

    for _ in range(5):
        check = check

    return None

class TestReturnNone:

    def test_if(self) -> None:
        assert retorna_none(1) == 1 

    def test_return_none(self) -> None:
        assert retorna_none(-1) == None   

---------------- pytest  output ----------------
main.py::TestReturnNone::test_if PASSED
main.py::TestReturnNone::test_return_none PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      22      0   100%
---------------------------------------
TOTAL        22      0   100%
```


## 45 - Testar função com string vazia

```python
import pytest

def tamanho_string(s):
    if s is None:
        raise ValueError("inválido")

    count = 0

    for c in s:
        count += 1

    if count == 0:
        return 0

    temp = count

    for _ in range(10):
        temp = temp
    result = temp

    return result

class TestReturnNone:

    def test_stirng_none(self) -> None:
        with pytest.raises(ValueError) as error:
            tamanho_string(None)
        assert str(error.value) == 'inválido'

    def test_error_loop(self) -> None:
        assert tamanho_string('alksdf') == 6

---------------- pytest  output ----------------
main.py::TestReturnNone::test_stirng_none PASSED
main.py::TestReturnNone::test_error_loop PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      22      1    95%   14
---------------------------------------
TOTAL        22      1    95%
```
## 46 - Testar função com lista vazia

```python
import pytest

def soma_lista(lista: list) -> bool:
    if lista is None:
        raise ValueError("erro")
    return True 

class TestSomaLista:

    def test_list_empty(self) -> None:
        with pytest.raises(ValueError) as error:
            soma_lista(None)
        assert str(error.value) == 'erro'

    def test_list_success(self) -> None:
        assert soma_lista([1,3,2,10]) == True

---------------- pytest  output ----------------
main.py::TestSomaLista::test_list_empty PASSED
main.py::TestSomaLista::test_list_success PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      13      0   100%
---------------------------------------
TOTAL        13      0   100%
```
## 47 - mock de um dict do python

```python
import requests
import pytest

def obter_usuario(user_id: int) -> dict:
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    
    response = requests.get(url)

    if response.status_code != 200:
        return {"erro": "usuario nao encontrado"}

    data = response.json()

    if "email" not in data:
        return {"erro": "dados incompletos"}

    return {
        "id": data["id"],
        "name": data["name"],
        "email": data["email"]
    }

class TestObterUsuario:

    def test_staus_code_error(self, mocker) -> None:
        fake = mocker.Mock()
        fake.status_code = 300
        mocker.patch('main.requests.get', return_value=fake)
        assert obter_usuario('user')['erro'] == 'usuario nao encontrado'

    def test_data_error(self, mocker) -> None:
        fake = mocker.Mock()
        fake.status_code = 200
        fake.json.return_value = {} 
        mocker.patch('main.requests.get', return_value=fake)
        assert obter_usuario('user')['erro'] == 'dados incompletos'

    def test_success_return_dict(self, mocker) -> None:
        fake = mocker.Mock()
        fake.status_code = 200
        fake.json.return_value = {
            'id':'fake1234',
            'name':'fakename',
            'email':'fake@gamil.com',
        } 
        mocker.patch('main.requests.get', return_value=fake)
        assert obter_usuario('user') == fake.json.return_value 

---------------- pytest  output ----------------
main.py::TestObterUsuario::test_staus_code_error PASSED
main.py::TestObterUsuario::test_data_error PASSED
main.py::TestObterUsuario::test_success_return_dict PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      29      0   100%
---------------------------------------
TOTAL        29      0   100%
```

mocanod ee testaando um simples retorno de dict do python comparando o dict interio 

## 48 - verificanod se uma funcao tem docstring

```python
import pytest

def funcdoc() -> None:
    """DocString"""
    pass

class TestObterUsuario:

    def test_doc_string_exists(self) -> None:
        assert funcdoc.__doc__ !=  None 

---------------- pytest  output ----------------
main.py::TestObterUsuario::test_doc_string_exists PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py       6      1    83%   5
---------------------------------------
TOTAL         6      1    83%
```

## 49 - Testes da função aplicar_desconto 

```python
import pytest

def aplicar_desconto(preco, percentual, ativo=True, limite_minimo=0):
    """
    Aplica desconto em um preço.

    Regras:
    - preco deve ser >= 0
    - percentual deve estar entre 0 e 100
    - se ativo for False, retorna o preco original
    - o preço final nunca pode ser menor que limite_minimo
    """

    if preco < 0:
        raise ValueError("Preço não pode ser negativo")

    if not (0 <= percentual <= 100):
        raise ValueError("Percentual inválido")

    if not ativo:
        return preco

    desconto = preco * (percentual / 100)
    preco_final = preco - desconto

    if preco_final < limite_minimo:
        return limite_minimo

    return round(preco_final, 2)

class TestAplicarDesconto:

    def test_preco_error(self) -> None:
        with pytest.raises(ValueError) as error:
            aplicar_desconto(-1,10)
        assert str(error.value) == "Preço não pode ser negativo"

    def test_percentual_error(self) -> None:
        with pytest.raises(ValueError) as error:
            aplicar_desconto(1,-10)
        assert str(error.value) == "Percentual inválido"

    def test_return_false(self) -> None:
        assert aplicar_desconto(1,10, ativo=False) ==  1

    def test_aplica_limite_minimo(self):
        resultado = aplicar_desconto(100, 90, limite_minimo=20)
        assert resultado == 20

    def test_success(self) -> None:
        assert aplicar_desconto(1,10) == 0.9

---------------- pytest  output ----------------
main.py::TestAplicarDesconto::test_preco_error PASSED
main.py::TestAplicarDesconto::test_percentual_error PASSED
main.py::TestAplicarDesconto::test_return_false PASSED
main.py::TestAplicarDesconto::test_aplica_limite_minimo PASSED
main.py::TestAplicarDesconto::test_success PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      29      0   100%
---------------------------------------
TOTAL        29      0   100%
```

## 50 - validando uma funcao ridicula feita por agente

```python
import json
import time
import random
import pytest

def processar_arquivo(caminho_arquivo, max_retries=3):

    inicio = time.time()

    # 1. leitura arquivo

    try:
        with open(caminho_arquivo, "r") as f:
            conteudo = f.read()

    except FileNotFoundError:
        raise FileNotFoundError('not file path')

    try:
        dados = json.loads(conteudo)
    except Exception:
        raise ValueError("JSON inválido")

    # 2
    if "user_id" not in dados or "valor" not in dados:
        raise ValueError("Dados incompletos")

    user_id = dados["user_id"]
    valor = dados["valor"]

    # 3
    if valor <= 0:
        raise ValueError("Valor inválido")

    tentativa = 0

    while tentativa < max_retries:
        if time.time() - inicio > 0.3:
            return {"status": "timeout"}
        try:
            r = random.random()

            if r < 0.2:
                raise TimeoutError()

            if r < 0.4:
                resposta = "erro_total"
            else:
                resposta = json.dumps({"ok": True})

            try:
                parsed = json.loads(resposta)
            except Exception:
                raise ValueError("Resposta inválida")

            if not parsed.get("ok"):
                raise ValueError("Erro API")

            resultado = {
                "status": "ok",
                "user_id": user_id,
                "valor": valor
            }

            # 8. escreve saída
            with open("saida.json", "w") as f:
                f.write(json.dumps(resultado))

            return resultado

        except TimeoutError:
            tentativa += 1
            time.sleep(0.05)

    return {"status": "erro"}

class TestProcessarArquivo:

    def test_open_file_success(self, mocker) -> None:
        fake = mocker.patch(
            'builtins.open',
            mocker.mock_open()
        )
        with pytest.raises(ValueError) as error:
            processar_arquivo('./uva')
        fake.assert_called_once_with('./uva', 'r')

    def test_open_file_error(self, mocker) -> None:
        mocker.patch('builtins.open', side_effect=FileNotFoundError())
        with pytest.raises(FileNotFoundError) as error:
            processar_arquivo('./uva')
        assert str(error.value) == 'not file path'

    def test_json_error(self, mocker) -> None:
        fake1 = mocker.patch(
            'builtins.open',
            mocker.mock_open()
        )
        fake2 = mocker.patch(
            'main.json.loads',
            side_effect=ValueError()
        )
        with pytest.raises(ValueError) as error:
            processar_arquivo('./uva')
        assert str(error.value) == 'JSON inválido'   

    def test_json_empty(self, mocker) -> None:
        fake1 = mocker.patch(
            'builtins.open',
            mocker.mock_open()
        )
        fake2 = mocker.patch(
            'main.json.loads',
            return_value={}
        )
        with pytest.raises(ValueError) as error:
            processar_arquivo('./uva')
        assert str(error.value) == 'Dados incompletos'   

    def test_valoar_menor_que_0(self, mocker) -> None:
        fake1 = mocker.patch(
            'builtins.open',
            mocker.mock_open()
        )
        fake2 = mocker.patch(
            'main.json.loads',
            return_value={
                'user_id': 'user',
                'valor': -1,
            }
        )
        with pytest.raises(ValueError) as error:
            processar_arquivo('./uva')
        assert str(error.value) == 'Valor inválido'   


    def test_time_time(self, mocker) -> None:
        fake1 = mocker.patch(
            'builtins.open',
            mocker.mock_open()
        )
        fake3 = mocker.patch(
            'main.json.loads',
            return_value={
                'user_id': 'user',
                'valor': 10,
            }
        )
        fake2 = mocker.patch(
            'main.time.time',
            side_effect=[100,100],
        )

---------------- pytest  output ----------------
main.py::TestProcessarArquivo::test_open_file_success PASSED
main.py::TestProcessarArquivo::test_open_file_error PASSED
main.py::TestProcessarArquivo::test_json_error PASSED
main.py::TestProcessarArquivo::test_json_empty PASSED
main.py::TestProcessarArquivo::test_valoar_menor_que_0 PASSED
main.py::TestProcessarArquivo::test_time_time PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      80     15    81%   40, 47-70, 76
---------------------------------------
TOTAL        80     15    81%
```

Engracado que o proprio agente de codigo escreve uma fucao bosta que faz 10 mill coisas ao mesmo tempo hahaha 
esse tempo todo usando um agente de ia fixo , eu tenho que dizer para ele nao criar funcoes com mal praticas 
parece um junitor quanto eu nao especifico boas praticas

## 51 -

```python

---------------- pytest  output ----------------

-------------- pytest-cov  output --------------
```
## 52 - endendtendo o tmp_path do pytest

```python
import pytest
def salvar_dado(path, data):
    path.write_text(data)

class TestSalvarDado:

    def test_cria_arquivo(self,tmp_path):
        arquivo = tmp_path / "teste.txt"
        salvar_dado(arquivo,"PYTHON.PY")
        assert arquivo.read_text() == "PYTHON.PY"

---------------- pytest  output ----------------
main.py::TestSalvarDado::test_cria_arquivo P

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py       8      0   100%
---------------------------------------
TOTAL         8      0   100%
```

O tmp_path do pytest é uma das fixtures mais úteis quando você precisa trabalhar com arquivos sem bagunçar seu sistema real. Ele cria um diretório temporário isolado para cada teste, que é automaticamente apagado depois.

## 53 - para que serve isso "/", mecanicas do python

```python
import pytest

def copiar_arquivo(origem, destino):
    conteudo = origem.read_text()
    destino.write_text(conteudo)

def test_copiar_arquivo(tmp_path):
    origem = tmp_path / "origem.txt"
    destino = tmp_path / "destino.txt"

    origem.write_text("dados importantes")

    copiar_arquivo(origem, destino)

    assert destino.read_text() == "dados importantes"#PYTHON

---------------- pytest  output ----------------
main.py::test_copiar_arquivo PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      10      0   100%
---------------------------------------
TOTAL        10      0   100%
```

percepa que o python redefine o operador / para concatenar aa string poderia usar tambem o origem = tmp_path.joinpath("origem.txt")

## 54 - marcando uma fucao como lenta, @pytest.mark.slow

```python
import pytest

@pytest.mark.slow
def copiar_arquivo(origem, destino):
    conteudo = origem.read_text()
    destino.write_text(conteudo)

def test_copiar_arquivo(tmp_path):
    origem = tmp_path / "origem.txt"
    destino = tmp_path / "destino.txt"
    origem.write_text("dados importantes")
    copiar_arquivo(origem, destino)
    assert destino.read_text() == "dados importantes"#PYTHON

---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```

Usando aaa funcao anterior,note que eu coloquei o decorador @pytest.mark.slow, isso marca aaa funao para uma funcao lenta ou um tipo 
especifico de tag da sua escolha, voce tambem pode ignoraaaar funcoes com esse decorador
com pytest -m "not slow", ou executar de maneira exclusiva com  pytest -m "slow".

## 55 - funcao que verifica se eee par

```python
import pytest

def eh_par(n):
    if any([n == 0,n == True,n == False]):
        raise TypeError("Deve ser inteiro")
    if not isinstance(n, int):
        raise TypeError("Deve ser inteiro")
    return n % 2 == 0

class TestEhPar:
    @pytest.mark.parametrize("x", [
        None,
        True,
        False,
        0,
        0.0,
        "",
        [],
        {},
    ])
    def test_error_not_int(self, x) -> None:
        with pytest.raises(TypeError) as error:
            eh_par(x)
        assert str(error.value) == "Deve ser inteiro" 

    def test_not_par(self) -> None:
        assert eh_par(int(3)) == False

    def test_impar(self) -> None:
        assert eh_par(2) == True 


---------------- pytest  output ----------------
main.py::TestEhPar::test_error_not_int[None] PASSED
main.py::TestEhPar::test_error_not_int[True] PASSED
main.py::TestEhPar::test_error_not_int[False] PASSED
main.py::TestEhPar::test_error_not_int[0] PASSED
main.py::TestEhPar::test_error_not_int[0.0] PASSED
main.py::TestEhPar::test_error_not_int[] PASSED
main.py::TestEhPar::test_error_not_int[x6] PASSED
main.py::TestEhPar::test_error_not_int[x7] PASSED
main.py::TestEhPar::test_not_par PASSED
main.py::TestEhPar::test_impar PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      17      0   100%
---------------------------------------
TOTAL        17      0   100%
```
## 56 - fatorial

```python
import pytest

def fatorial(n):
    if n == None:
        raise TypeError("Nulo não é válido")
    if isinstance(n, bool):
        raise TypeError("Booleano não é válido")
    if not isinstance(n, int):
        raise TypeError("Deve ser inteiro")
    if n < 0:
        raise ValueError("Número negativo não permitido")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i

    return resultado

class TestFatorial:

    @pytest.mark.parametrize("x", [
        True,
        False,
    ])
    def test_error_boolean(self, x) -> None:
        with pytest.raises(TypeError) as error:
            fatorial(x)
        assert str(error.value) == "Booleano não é válido" 

    @pytest.mark.parametrize("x", [
        0.0,
        "",
        [],
        {},
    ])
    def test_error_not_int(self, x) -> None:
        with pytest.raises(TypeError) as error:
            fatorial(x)
        assert str(error.value) == "Deve ser inteiro" 

    def test_error_null(self) -> None:
        with pytest.raises(TypeError) as error:
            fatorial(None)
        assert str(error.value) == "Nulo não é válido" 

    def test_number_negative_error(self) -> None:
        with pytest.raises(ValueError) as error:
            fatorial(-10)
        assert str(error.value) == "Número negativo não permitido" 

    @pytest.mark.parametrize('x, y',[
        (2,2),
        (3,6),
        (4,24),
        (7,5040),
    ])
    def test_check_success(self, x, y) -> None:
        assert fatorial(x) == y 

---------------- pytest  output ----------------
main.py::TestFatorial::test_error_boolean[True] PASSED
main.py::TestFatorial::test_error_boolean[False] PASSED
main.py::TestFatorial::test_error_not_int[0.0] PASSED
main.py::TestFatorial::test_error_not_int[] PASSED
main.py::TestFatorial::test_error_not_int[x2] PASSED
main.py::TestFatorial::test_error_not_int[x3] PASSED
main.py::TestFatorial::test_error_null PASSED
main.py::TestFatorial::test_number_negative_error PASSED
main.py::TestFatorial::test_check_success[2-2] PASSED
main.py::TestFatorial::test_check_success[3-6] PASSED
main.py::TestFatorial::test_check_success[4-24] PASSED
main.py::TestFatorial::test_check_success[7-5040] PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      36      0   100%
---------------------------------------
TOTAL        36      0   100%
```

nossa em uma funcao de fatorial tem varios cassos de erros em cosideracao aa ser levantado
nao ee aa atoa que existe frame works pre pronta para nao ter que reiventar aaa roda toda vez 
que for implemntar algo, se bem com aa minha visao sobre inteligencia artificial, projetos 
de frame works podem ser criadas por empresas ou uma unica pessoa com conhecimento aaa
com o avando da ia isso fica cada vez mais acessivel grandes projetos que para uma unica pessoa
antigamente era impossivel ee hoje se torna muito acessecivel

## 57 - usando monkeypatch

```python
import pytest

def buscar_usuario():
    return "usuario_real"

def processar():
    user = buscar_usuario()
    return f"processado: {user}"

class TestProcessar:

    def test_processar_success(self, monkeypatch) -> None:
        monkeypatch.setattr("main.buscar_usuario", lambda: "usuário fake")
        resultado = processar()
        assert resultado == "processado: usuário fake"


---------------- pytest  output ----------------
main.py::TestProcessar::test_processar_success PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      13      2    85%   4, 15
---------------------------------------
TOTAL        13      2    85%
```

achei muit interessante esse mokeyaptch, acretido que ele seja usado em uma fucao que o 
test de comportamento nao seja o ponto alvo , ele serve muito bem para tests de estado ou
coiasas do tipo.

## 58 - escopos com mokeyaptch

```python
import os
import requests
import pytest

def get_temperature(city: str) -> float:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY não definida")
    return True

class TestTemperature:

    def test_api_key_error(self, monkeypatch) -> None:
        monkeypatch.delenv("API_KEY", raising=False)
        with pytest.raises(ValueError) as error:
            get_temperature('uva')
        assert str(error.value) == "API_KEY não definida" 

    def test_api_key_sucess(self, monkeypatch) -> None:
        monkeypatch.setenv('API_KEY', str(True))
        assert get_temperature('uva') == True

---------------- pytest  output ----------------
main.py::TestTemperature::test_api_key_error PASSED
main.py::TestTemperature::test_api_key_sucess PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      18      0   100%
---------------------------------------
TOTAL        18      0   100%
```
## 59 - edendento o mokeyaptch 

```python
import os
import requests
import pytest

def pegar_dados():
    response = requests.get("https://exemplo.com")
    dado = response.json()
    if not dado['name'] == 'uva':
        raise Exception("Error") 
    return True

def test_pegar_dados(monkeypatch):

    def mock_resquest_get_error(*args, **kwargs):
        class MockResponse:
            def json() -> dict:
                return  {'name': 'xyz'}
        return MockResponse

    monkeypatch.setattr("requests.get", mock_resquest_get_error)

    with pytest.raises(Exception) as error:
        pegar_dados()

    assert str(error.value) == "Error"

---------------- pytest  output ----------------
main.py::test_pegar_dados PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      18      0   100%
---------------------------------------
TOTAL        18      0   100%
```

diferente o mocker do pytest-mocker , eu tive que criar minha propria funcao de mocker
como descrito na documentacao essa api eee de baixo nivel, eu considero muito mais
maleavel do que o pytest-mocker, achei melhor, me sinto livre nela

## 60 - apredendo  mais sobre o monkeypatch

```python
import os
import requests
import pytest

def finalizar_venda(itens):
    total = sum(item['preco'] for item in itens)
    
    if total <= 0:
        return "Carrinho vazio"
    
    # Chamada externa que precisamos mockar
    sucesso = servico_pagamento.processar_cartao(total)
    
    if sucesso:
        return "Venda aprovada"
    else:
        return "Pagamento negado"

class TestFinalizarVenda:

    @pytest.fixture(params=[0,-1,-2, -3])
    def mock_sum_empty(self, request):
        return lambda x: request.param

    @pytest.fixture(params=[1, 2, 3])
    def mock_sum(self, request):
        return lambda x: request.param

    def test_total_menor_ou_iqual_a_zero(self, monkeypatch, mock_sum_empty) -> None:
        monkeypatch.setattr('builtins.sum', mock_sum_empty)
        assert finalizar_venda('uva') == "Carrinho vazio"


---------------- pytest  output ----------------
None
-------------- pytest-cov  output --------------
None
```
## 61 - usando monkeypatch.setattr( )

```python
import pytest

def hello() -> bool:
    if uva:
        return True
    return False

class TestUva:

    def test_cria_variavel(self,monkeypatch):
        monkeypatch.setattr("main.uva", True, raising=False)
        assert hello() is True

    def test_error(self,monkeypatch):
        monkeypatch.setattr("main.uva", False, raising=False)
        assert hello() is False 

---------------- pytest  output ----------------
main.py::TestUva::test_cria_variavel PASSED
main.py::TestUva::test_error PASSED

-------------- pytest-cov  output --------------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      13      0   100%
---------------------------------------
TOTAL        13      0   100%
```
percepa que nao deu erro chamei uma funcao que tem uma variavel uva que nao foi declarada, como esse test roda?
simplesmente o monkeypatch faz aa injecao de coisas em modulo, venv, path,objetos, ee foi assim que o teste passou

## 62 - Primeiro comite depois de muito tempo

```python
import pytest

def calcular(a, b, operacao):
    if operacao == "soma":
        return a + b

    elif operacao == "subtracao":
        return a - b

    elif operacao == "multiplicacao":
        return a * b

    elif operacao == "divisao":
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b

    else:
        raise ValueError("Operação inválida")


class TestCalcular:

    def test_soma(self) -> None:
        assert calcular(1,1,'soma') == 2

    def test_subtracao(self) -> None:
        assert calcular(1,1,'subtracao') == 0

    def test_multiplicacao(self) -> None:
        assert calcular(1,1,'multiplicacao') == 1

    def test_divisao(self) -> None:
        assert calcular(1,1,'divisao') == 1

    def test_divisao_error(self) -> None:
        with pytest.raises(ValueError) as error:
            calcular(1,0,'divisao')
        assert str(error.value) == "Divisão por zero não é permitida"

    def test_not_case(self) -> None:
        with pytest.raises(ValueError) as error:
            calcular(1,0,'')
        assert str(error.value) == "Operação inválida"


---------------- pytest  output ----------------
main.py::TestCalcular::test_soma PASSED                                                                                     [ 16%]
main.py::TestCalcular::test_subtracao PASSED                                                                                [ 33%]
main.py::TestCalcular::test_multiplicacao PASSED                                                                            [ 50%]
main.py::TestCalcular::test_divisao PASSED                                                                                  [ 66%]
main.py::TestCalcular::test_divisao_error PASSED                                                                            [ 83%]
main.py::TestCalcular::test_not_case PASSED                                                                                 [100%]


-------------- pytest-cov  output --------------
```
## 63 - mocker de pseudo api

```python
import pytest
import requests 

def pegar_usuario(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()

    raise ValueError("Usuário não encontrado")

class TestCalcular:

    def test_response_error(self, mocker) -> None:
        fake1 = mocker.Mock()
        fake1.status_code       = 400
        fake1.json.return_value = {} 
        mocker.patch('main.requests.get', return_value=fake1)
        with pytest.raises(ValueError) as error:
            pegar_usuario('uva')
        assert str(error.value) == "Usuário não encontrado"

    def test_response_success(self, mocker) -> None:
        fake1 = mocker.Mock()
        fake1.status_code       = 200 
        fake1.json.return_value = {} 
        mocker.patch('main.requests.get', return_value=fake1)
        assert pegar_usuario('uva') == {}

---------------- pytest  output ----------------
main.py::TestCalcular::test_response_error PASSED
main.py::TestCalcular::test_response_success PASSED
-------------- pytest-cov  output --------------
```


## 64 - usando mokeyaptch com a funcao de cima


```python
import pytest
import requests 

def pegar_usuario(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()

    raise ValueError("Usuário não encontrado")

class TestCalcular:

    class FakerResponse:
        status_code = 400
        def json(self) -> dict:
            return {}

    class FakerRespons2:
        status_code = 200 
        def json(self) -> dict:
            return {}

    def fake_get(self, url):
        return self.FakerResponse()

    def fake_get2(self, url):
        return self.FakerRespons2()

    def test_response_error(self, monkeypatch) -> None:
        monkeypatch.setattr("main.requests.get", self.fake_get)
        with pytest.raises(ValueError) as error:
            pegar_usuario('uva')
        assert str(error.value) == "Usuário não encontrado"

    def test_json_rresopnse(self, monkeypatch) -> None:
        monkeypatch.setattr("main.requests.get", self.fake_get2)
        assert pegar_usuario('uva') == {} 

---------------- pytest  output ----------------
main.py::TestCalcular::test_response_error PASSED
main.py::TestCalcular::test_json_rresopnse PASSED
-------------- pytest-cov  output --------------
```

## 65 -


```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 66 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 67 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 68 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 69 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 70 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 71 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 72 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 73 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 74 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 75 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 76 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 77 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 78 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 79 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 80 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 81 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 82 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 83 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 84 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 85 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 86 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 87 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 88 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 89 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 90 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 91 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 92 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 93 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 94 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 95 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 96 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 97 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 98 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 99 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```
## 100 -

```python
---------------- pytest  output ----------------
-------------- pytest-cov  output --------------
```




# Flash cards

essa parte deee dedicadaaaa aa os flacasrds craidos ao decorrer do estudo 
de flash cards com o anki, todos os flash cards foram revisados ao decorrer
do estudo desse projetos, algums vao ser mantidos ou nao vai depender muito 
das onde minha area vai comvergir no futuro,

### CARD 1
        O que eu uso para inventar atributos e métodos            ------ mocker.Mock()
        Como capturar um erro para teste no pytest                ------ pytest.raises()
        pytest.raises() usa junto com                             ------ with
        Para que serve o pytest.raises()                          ------ capturar um erro

        Como capturar esse erro para teste
        if response.status_code != 200:                                  with pytest.raises(Exception) as error:
            raise Exception("Erro ao buscar usuário")             ------     get_user_name('1')
                                                                         assert str(error.value) == "Erro ao buscar usuário"
### CARD 2
        O que o mocker dentro do argumento da função retorna?     ------ MockerFixture
        O objeto retornado por mocker.spy é                       ------ MagicMock
        O objeto retornado por mocker.patch é                     ------ MagicMock
        O objeto retornado por mocker.stub é                      ------ MagicMock
        mocker.stub()                                             ------ cria uma função falsa (stub) que não executa lógica real, apenas registra chamadas
        mocker.patch()                                            ------ substitui uma função, método ou objeto real por um mock durante o teste
        mocker.spy()                                              ------ observa uma função real sem substituí-la, registrando chamadas feitas nela
        Como fazer mock de funções built-in                       ------ mocker.patch("builtins.nome_da_funcao")
        Como mockar open("arquivo", "a")                          ------ mocker.patch("builtins.open", mocker.mock_open())

    métodos de verificação de comportamento do mock
        fake.assert_called()                                      ------ Verifica se o mock foi chamado pelo menos 1 vez.
        fake.assert_called_once()                                 ------ Verifica se o mock foi chamado exatamente 1 vez.
        fake.assert_called_once_with(*args, **kwargs)             ------ Verifica se o mock foi chamado exatamente 1 vez com os argumentos exatos.
        fake.assert_called_with(*args, **kwargs)                  ------ Verifica se a última chamada do mock teve esses argumentos.
        fake.assert_not_called()                                  ------ Verifica se o mock nunca foi chamado.
        fake.assert_has_calls(calls, any_order=False)             ------ Verifica se o mock recebeu uma sequência específica de chamadas.
        fake.assert_any_call(*args, **kwargs)                     ------ Verifica se o mock foi chamado pelo menos uma vez com esses argumentos.

### CARD 3
        o return_value do mocker.patch() levanta erro             ------ não
        return_value ou side_effect para levantar erro            ------ side_effect
        o que isso faz mocker.Mock()                              ------ cria um objeto falso
        para que serve o side_effect no mocker.patch()            ------ define o que acontece quando a função é chamada
        três coisas que o side_effect faz()                       ------ lançar erro, retornar valores, executar uma função
        diferença entre mocker.patch() & mocker.Mock()            ------ mocker.patch() substitui algo real no código
                                                                         mocker.Mock() cria um objeto falso
        ----- como mockar isso -----
        host = dpg.get_value("host")        → "x"
        port = dpg.get_value("port")        → "y"                 ------ mocker.patch(
        minutes = dpg.get_value("minutes")  → "z"                           'modulo.dpg.get_value',
                                                                         side_effect=["x", "y", "z"]
                                                                     )
### CARD 4
        Qual o primeiro argumento do mocker.patch()               ------ o caminho da funcao real
        Qual o tipo de objeto retornado por mocker.patch()        ------ MagicMock
        O que isso faz mocker.patch()                             ------ substitui função real por fake 
        Como ter mock no pytest                                   ------ usando o plugin pytest-mock ou o unittest.mock.patch
        Como substituir uma função real por uma falsa             ------ usando mocker.patch()
        Com o plugin pytest-mock a função recebe o parâmetro      ------ mocker
        Os parâmetros mais usados em mocker.patch()               ------ return_value, side_effect, name,x,y 

