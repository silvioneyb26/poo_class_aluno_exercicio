class aluno:
    #construtor
    def __init__(self, nomeALuno, notaAluno1, pesoAluno2):
        self.nome = nomeALuno
        self.nota1 = notaAluno1
        self.nota2 = pesoAluno2
    #calcular média   
    def calcularMedia(self):
        media = (self.nota1 + self.nota2) / 2    
        return media
    #verificar a frequência
    def setFrequencia(self):
        #criar atributo frequência
        setattr(self, "frequencia", 0)           
        self.frequencia = float(input("Informe a frequência do aluno: "))
        return self.calcularAprovacao()                             
    #verificar aprovação de acordo com nota e frequência do aluno          
    def calcularAprovacao(self):
        if self.frequencia >= 0.75 and int(self.calcularMedia()) >= 6:                 
           return "O aluno {} foi aprovado com media {} e frequência {}".format(self.nome, self.calcularMedia(), self.frequencia)
        if self.frequencia >= 0.75 and int(self.calcularMedia()) < 6:
            return "O aluno {} foi reprovado com media {} e frequência {}".format(self.nome, self.calcularMedia(), self.frequencia)
        if self.frequencia < 0.75 and int(self.calcularMedia()) >=6:
            return "O aluno {} foi reprovado com media {} e frequência {}".format(self.nome, self.calcularMedia(), self.frequencia)