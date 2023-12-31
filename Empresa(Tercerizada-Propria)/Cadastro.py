import sys
from Funcionario import *
from Error import MensagemErro
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTextBrowser, QCheckBox
from PySide6.QtGui import QColor,QCursor
from PySide6.QtCore import Qt


class JanelaInicial(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registro de Pagamento de Funcionários") #Titulo do programa
        self.setGeometry(300, 300, 700, 700) #tamanho da tela inicial
        

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        

        self.lbl_layout = QVBoxLayout()
        
        
        self.BK_Color = QColor(240,255,255) #cor background
        self.setStyleSheet(f"background-color: {self.BK_Color.name()};")
        

        self.lbl_dados_funcionario = QLabel("Informe os dados do funcionário:") #instrução para o usuário
        self.lbl_layout.addWidget(self.lbl_dados_funcionario)
        

        self.txt_nome = QLineEdit()
        self.txt_nome.setPlaceholderText("Nome") #placeholder para nome
        self.lbl_layout.addWidget(self.txt_nome)
        

        self.txt_hora = QLineEdit()
        self.txt_hora.setPlaceholderText("Horas Trabalhadas") #placeholder para horas trabalhadas
        self.lbl_layout.addWidget(self.txt_hora)
        

        self.txt_valor_da_hora = QLineEdit()
        self.txt_valor_da_hora.setPlaceholderText("Valor da Hora trabalhada") #placeholder para o valor da hora trabalhada
        self.lbl_layout.addWidget(self.txt_valor_da_hora)
        

        self.ck_terceirizado = QCheckBox("Terceirizado") #checkbox para funcionário terceirizado
        self.lbl_layout.addWidget(self.ck_terceirizado)
        

        self.txt_despesa_adicional = QLineEdit()
        self.txt_despesa_adicional.setPlaceholderText("Despesa Adicional (Somente para funcionários terceirizados)")
        self.lbl_layout.addWidget(self.txt_despesa_adicional)
        

        self.btn_adicionar = QPushButton("Registrar dados") #botão que finaliza a adição de funcionário
        self.btn_adicionar.clicked.connect(self.adicionar_funcionario)
        self.BK_Color_2 = QColor(152,251,152)
        self.btn_adicionar.setStyleSheet(f"background-color: {self.BK_Color_2.name()};")
        self.btn_adicionar.setCursor(QCursor(Qt.PointingHandCursor)) #mudança de cursor sobre o botão
        

        self.lbl_layout.addWidget(self.btn_adicionar)
        

        self.txt_exibir_texto = QTextBrowser()
        self.BK_Color_3 = QColor(255,255,255)
        self.txt_exibir_texto.setStyleSheet(f"background-color: {self.BK_Color_3.name()};")

        self.lbl_layout.addWidget(self.txt_exibir_texto)
        

        self.central_widget.setLayout(self.lbl_layout)
        

        self.funcionarios = []
      

    def adicionar_funcionario(self):
        try:
            if self.txt_nome.text().isdigit() == True:
                self.erro_mensagem = MensagemErro()
                self.erro_mensagem.erro_funcionario_pagamento()
                
                
            else:
                terceirizado = self.ck_terceirizado.isChecked()
                despesa_adicional = float(self.txt_despesa_adicional.text()) if terceirizado else 0
                horas_trabalhadas = float(self.txt_hora.text())
                valor_da_hora = float(self.txt_valor_da_hora.text())
                

                if despesa_adicional < 0 or horas_trabalhadas < 0 or valor_da_hora < 0: #parametros para msg de erro
                    self.erro_mensagem = MensagemErro()
                    self.erro_mensagem.erro_funcionario_pagamento()


                else:
                    nome = self.txt_nome.text()
                    
                    
                    funcionario = Funcionario(nome, horas_trabalhadas, valor_da_hora, terceirizado, despesa_adicional)
                    self.funcionarios.append(funcionario)
                    

                    self.txt_exibir_texto.append(f"Funcionário adicionado: {funcionario}")
                    
                    
                    self.txt_nome.clear()
                    self.txt_hora.clear()
                    self.txt_valor_da_hora.clear()
                    self.txt_valor_da_hora.clear()
                    self.ck_terceirizado.setChecked(False)
                    
                
        except:
            self.erro_mensagem = MensagemErro()
            self.erro_mensagem.erro_funcionario_pagamento()


        else:
            if self.txt_nome.text().isdigit() == True or despesa_adicional < 0 or horas_trabalhadas < 0 or valor_da_hora < 0:
                pass


            else:
                self.txt_exibir_texto.append('Registro realizado!') #confirma o recebimento e armazenamento do dado
            
                