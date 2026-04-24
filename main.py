import pytest
import pytest
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



#Aplicação da mutação
#    setattr → escreve no __dict__ do objeto/módulo.
#    setitem → usa mapping[key] = value.
#    setenv → escreve em os.environ.
#    syspath_prepend → insere em sys.path.
#    chdir → altera os.getcwd() via os.chdir.

#func()	executa a função
# PYTEST
#    monkeypatch.setattr()
#               .delattr()
#               .setitem()
#               .delitem()
#               .setenv()
#               .delenv()
#               .syspath_prepend(path)
#               .chdir(path)
#               .context()
#
# DEFINA:
#     monkeypatch.setattr()             ----- sobrescreve atributo no objeto
#     monkeypatch.delattr()             ----- remove atributo do objeto
#     monkeypatch.setitem()             ----- define chave em dict-like
#     monkeypatch.delitem()             ----- remove chave de dict-like
#     monkeypatch.setenv()              ----- cria/atualiza variável de ambiente
#     monkeypatch.delenv()              ----- remove variável de ambiente
#     monkeypatch.syspath_prepend(path) ----- adiciona caminho no início de sys.path
#     monkeypatch.chdir(path)           ----- muda diretório de trabalho atual
#     monkeypatch.context()             ----- cria escopo isolado; reverte patches ao sair
#
#
#monkeypatch:
#    atributo ----- setattr,delattr
#    dict     ----- setitem, delitem
#    env      ----- setenv, setenv
#    import   ----- syspath_prepend
#    cwd      ----- chdir
#--------------------------------------------------------------------------------------------------
# pytest-mock é uma wrapper do                             ----- unittest.mock
# qual desses dois é nativo do pytest mock ou monkeypatch  ----- monkeypatch
# para teste de estado eu uso                              ----- monkeypatch
# para teste de comportamento eu uso                       ----- pytest-mock
# o que eu uso para checar apenas o retorno de uma função  ----- monkeypatch
# o que eu uso para checar o comportamento de uma função   ----- pytest-mock
# o que são hooks no pytest                                ----- funções nomeadas com prefixo pytest_





