class ListaContato():

   def __init__(self):
       self.listatelefonica = []

   def Adicionar(self,numero):

       self.listatelefonica.append(numero)

   def Remover(self,numero):

       for x in self.listatelefonica:
           if x.numero == numero:
               self.listatelefonica.remove(x)



   def MostrarNome(self,nomeinput):

       achados = 0

       for x in self.listatelefonica:
           if x.nome == nomeinput:
               achados = achados + 1
               x.SelfPrint()
       print("Foi encontrado ",achados,"contatos com esse nome.")

   def SelfPrint(self):

       for x in self.listatelefonica:
           x.SelfPrint()
       return



class Numero():
   def __init__(self,nome,numero):
       self.nome = nome
       self.numero = numero


   def SelfPrint(self):
       print("Nome: ",self.nome,"------ Telefone: ",self.numero,)
       return



class Menu():

   def __init__(self):
       self.lista = ListaContato()

   def MenuControl(self,x):

       self.lista.SelfPrint()

       while x != "5":
           if x == "1":
               self.lista.Adicionar(self.AddContato())

           elif x == "2":
               self.lista.Remover(self.RemContato())

           elif x == "3":
               self.lista.MostrarNome(self.BuscarContato())
           elif x == "4":
               self.lista.SelfPrint()
           elif x != "5":
               print("Digite uma opção valida.")


           x = self.MenuShow()

   def MenuShow(self):
       return input("1 - Adicionar Contato\n 2- Excluir Contato\n 3- Buscar Contato\n 4- Mostrar Contatos\n 5- Sair\n\n")

   def AddContato(self):
       while True:
           nom = input("Digite o nome do contato: ")
           nume = input("Digite o número de telefone: ")
           elemento = Numero(nom,nume)

           return elemento

   def RemContato(self):
       while True:

           num = input("Digite o numero do contato para remover: ")

           return num

   def BuscarContato(self):

       while True:
           nome = input("Digite o nome da pessoa que deve ser encontrada: ")

           return nome




menu = Menu()
menu.MenuControl(menu.MenuShow())