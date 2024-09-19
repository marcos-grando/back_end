
class Convidado:
    def __init__(self, id, nome, idade, designacao, mesa, contato, situacao):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.designacao = designacao
        self.mesa = mesa
        self.contato = contato
        self.situacao = situacao

    def to_dict(self, user_type):
        if user_type == 'organizador':
            return {
                'id': self.id,
                'nome': self.nome,
                'idade': self.idade,
                'designacao': self.designacao,
                'mesa': self.mesa,
                'contato': self.contato,
                'situacao': self.situacao
            }
        elif user_type == 'convidado':
            return {
                'id': self.id,
                'nome': self.nome,
                'mesa': self.mesa
            }
        elif user_type == 'self_convidado':
            return {
                'id': self.id,
                'nome': self.nome,
                'mesa': self.mesa,
                'situacao': self.situacao
            }
        else:
            return {}
