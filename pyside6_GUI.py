from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Primera ventana con PySide6")
        self.setFixedSize(500,330)
        self.setStyleSheet("background:#242526;")

        self.inicializar_UI()

    def inicializar_UI(self):
        #creacion del frame1
        self.frame_titulo = QFrame(self)
        self.frame_titulo.setGeometry(10,10,480,100)
        #aplicamos estilo
        self.frame_titulo.setStyleSheet("background: #1d2f44;")

        #creamos el label del titulo
        self.titulo =QLabel(self.frame_titulo)
        self.titulo.setText("Hola!")
        self.titulo.setGeometry(0,20,480,40)
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo.setStyleSheet("""
        color: white;
        font-size: 25px;
        font-weight: bold;""")

        #creacion del frame2
        self.frame2 = QFrame(self)
        self.frame2.setGeometry(10,120,480,200)
        self.frame2.setStyleSheet("background: #1d2f44;")

        #creamos leable texto
        self.enunciado = QLabel(self.frame2)
        self.enunciado.setText("Ingresa Tu nombre!")
        self.enunciado.setGeometry(0,20,480,40)
        self.enunciado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #estilos
        self.enunciado.setStyleSheet("""
        color: white;
        font-size: 25px;
        font-weight: bold;""")

        #input
        self.entrada = QLineEdit(self.frame2)
        self.entrada.setGeometry(10,70,460,45)
        self.entrada.setStyleSheet("""
        background: white;""")
        self.entrada.returnPressed.connect(self.obtiene_texto)

        #boton
        self.boton = QPushButton(self.frame2)
        self.boton.setText("Click me")
        self.boton.clicked.connect(self.obtiene_texto)
        self.boton.setGeometry(10,130,460,40)
        self.boton.setStyleSheet("""
        background: #314F72;
        font-size: 25px;
        font-weight: bold;""")

        #cuadro de dialogo
        self.dialogo = QDialog()
        self.dialogo.setFixedSize(300,300)
        self.dialogo.setStyleSheet("background: #242526;")

        #configuramos el frame1 del dialogo
        self.frame_titulo_dialogo = QFrame(self.dialogo)
        self.frame_titulo_dialogo.setGeometry(10,10,280,100)
        self.frame_titulo_dialogo.setStyleSheet("""
        background: #1d2f44;
        font-size: 25px;
        font-weight: bold;""")

        #titulo del dialogo
        self.titulo_dialogo = QLabel(self.frame_titulo_dialogo)

        self.titulo_dialogo.setGeometry(0,0,280,40)
        self.titulo_dialogo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo_dialogo.setStyleSheet("""
        color: white;
        font-size: 25px;
        font-weight: bold;""")

        # frame2 del dialogo
        self.frame_imagen = QFrame(self.dialogo)
        self.frame_imagen.setGeometry(10,120,280,170)
        #reescalamos imagen
        self.frame_imagen.setStyleSheet("border-image: url(./images.jpg) 0 0 0 0 stretch stretch;")


    def obtiene_texto(self):
        self.titulo_dialogo.setText(f"Bienvenido {self.entrada.text()}!")
        self.dialogo.show()
        print(self.entrada.text())


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())