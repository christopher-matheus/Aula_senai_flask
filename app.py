from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Estrutura para armazenar alunos: lista de dicionários
alunos = []
next_id = 1


@app.route('/adicionar_aluno', methods=['POST'])
def adicionar_aluno():
    global next_id
    data = request.get_json()
    if not data:
        return jsonify({'error': 'JSON inválido ou não fornecido'}), 400

    nome = data.get('nome')
    idade = data.get('idade')

    if not nome or idade is None:
        return jsonify({'error': 'Campos obrigatórios: nome, idade'}), 400

    aluno = {'id': next_id, 'nome': nome, 'idade': idade}
    alunos.append(aluno)
    next_id += 1
    return jsonify(aluno), 201


@app.route('/buscar_aluno', methods=['GET'])
def buscar_aluno():
    aluno_id = request.args.get('id')
    nome = request.args.get('nome')

    if aluno_id:
        try:
            aluno_id = int(aluno_id)
        except ValueError:
            return jsonify({'error': 'id deve ser inteiro'}), 400
        for a in alunos:
            if a['id'] == aluno_id:
                return jsonify(a)
        return jsonify({'error': 'Aluno não encontrado'}), 404

    if nome:
        resultado = [a for a in alunos if a['nome'].lower() == nome.lower()]
        if resultado:
            return jsonify(resultado)
        return jsonify({'error': 'Aluno não encontrado'}), 404

    return jsonify({'error': 'Forneça id ou nome como parâmetro de consulta'}), 400


@app.route('/listar_aluno', methods=['GET'])
def listar_aluno():
    return jsonify(alunos)


if __name__ == '__main__':
    app.run(debug=True)
