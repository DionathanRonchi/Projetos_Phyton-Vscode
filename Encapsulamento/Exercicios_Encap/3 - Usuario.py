class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.__senha = None

    # SETTER
    def set_senha(self, nova_senha):
        if len(nova_senha) >= 6:
            self.__senha = nova_senha
        else:
            print("Senha inválida. Deve ter pelo menos 6 caracteres.")

    # MÉTODOS
    def verificar_senha(self, senha_digitada):
        return senha_digitada == self.__senha

    def exibir_perfil(self):
        print("=" * 30)
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print("Senha: ******")
        print("=" * 30)


if __name__ == "__main__":
    u1 = Usuario(nome="Carlos Silva", email="carlos@email.com")
    u1.set_senha("123")
    u1.set_senha("senha123")
    u1.exibir_perfil()
    print("Acesso correto:", u1.verificar_senha("senha123"))
    print("Acesso errado:", u1.verificar_senha("errada123"))