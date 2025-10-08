import pytest
from app import app, alunos


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # limpar lista antes de cada teste
        alunos.clear()
        yield client


def test_adicionar_listar_e_buscar(client):
    # adicionar aluno
    rv = client.post('/adicionar_aluno', json={'nome': 'Ana', 'idade': 22})
    assert rv.status_code == 201
    data = rv.get_json()
    assert data['nome'] == 'Ana'
    assert data['idade'] == 22

    # listar alunos
    rv = client.get('/listar_aluno')
    assert rv.status_code == 200
    lista = rv.get_json()
    assert isinstance(lista, list)
    assert len(lista) == 1

    # buscar por id
    aluno_id = lista[0]['id']
    rv = client.get(f'/buscar_aluno?id={aluno_id}')
    assert rv.status_code == 200
    a = rv.get_json()
    assert a['id'] == aluno_id

    # buscar por nome
    rv = client.get('/buscar_aluno?nome=Ana')
    assert rv.status_code == 200
    found = rv.get_json()
    assert isinstance(found, list)
    assert found[0]['nome'] == 'Ana'
