# Taller de Investigación: Interfaces Gráficas con PySide6
**Asignatura:** Programación Orientada a Objetos  
**Tema:** Interfaces gráficas y programación orientada a eventos  
**Biblioteca seleccionada:** PySide6 (Qt 6 for Python)

---

## Tabla de Contenido
1. [Investigación Teórica](#1-investigación-teórica)
   - [¿Qué es PySide6 y su propósito principal?](#11-qué-es-pyside6-y-su-propósito-principal)
   - [¿Qué tipo de aplicaciones permite desarrollar?](#12-qué-tipo-de-aplicaciones-permite-desarrollar)
   - [Instalación y Requisitos](#13-instalación-y-requisitos)
   - [Principales Componentes Gráficos](#14-principales-componentes-gráficos)
   - [Manejo de Eventos del Usuario](#15-manejo-de-eventos-del-usuario)
   - [Ventajas y Limitaciones frente a Tkinter](#16-ventajas-y-limitaciones-frente-a-tkinter)
2. [Explicación del Funcionamiento](#2-explicación-del-funcionamiento)
   - [Creación de la Ventana Principal](#21-creación-de-la-ventana-principal)
   - [Creación y Visualización de Componentes](#22-creación-y-visualización-de-componentes)
   - [Eventos Implementados y Detección](#23-eventos-implementados-y-detección)
   - [Método de Respuesta al Evento](#24-método-de-respuesta-al-evento)
   - [Modificación de la Interfaz tras la Interacción](#25-modificación-de-la-interfaz-tras-la-interacción)
3. [Código Fuente del Proyecto](#3-código-fuente-del-proyecto)
4. [Instrucciones de Ejecución](#4-instrucciones-de-ejecución)
5. [Evidencia Visual](#5-evidencia-visual)
6. [Fuentes Consultadas](#6-fuentes-consultadas)

---

## 1. Investigación Teórica

### 1.1. ¿Qué es PySide6 y su propósito principal?
**PySide6** es el conjunto oficial de enlaces (*bindings*) en Python para el framework **Qt 6**, desarrollado y mantenido por **The Qt Company**. Su propósito primordial es facilitar la construcción de aplicaciones de escritorio multiplataforma (Windows, Linux, macOS) con interfaces gráficas modernas, alto rendimiento y una arquitectura fuertemente orientada a objetos sustentada en el motor nativo de C++.

### 1.2. ¿Qué tipo de aplicaciones permite desarrollar?
* **Software empresarial y de gestión:** Paneles administrativos, herramientas de conexión a bases de datos (CRUD), puntos de venta y sistemas ERP.
* **Herramientas de ingeniería y visualización científica:** Interfaces de telemetría en tiempo real, integración con bibliotecas como Matplotlib, visores 3D y simuladores.
* **Software multimedia y herramientas de diseño:** Paneles de control para producción audiovisual y plugins para suites avanzadas como Blender, Maya y Houdini.

### 1.3. Instalación y Requisitos
* **Requisitos:**
  * Python 3.8 o superior.
  * Gestor de paquetes `pip`.
* **Instalación:**
  ```bash
  pip install PySide6
  ```

### 1.4. Principales Componentes Gráficos
Todos los componentes visuales en PySide6 heredan de la clase base `QWidget`. Los más utilizados del módulo `PySide6.QtWidgets` son:
* `QMainWindow`: Ventana principal que provee la estructura base (barra de menús, barra de estado y widget central).
* `QDialog`: Ventana secundaria o cuadro de diálogo emergente utilizado para confirmaciones o avisos.
* `QFrame`: Contenedor visual rectangular utilizado para agrupar elementos y aplicar estilos/bordes.
* `QLabel`: Despliegue de texto estático, imágenes o animaciones.
* `QLineEdit`: Campo de entrada de texto de una sola línea para formularios.
* `QPushButton`: Botón interactivo de comando para ejecutar acciones.

### 1.5. Manejo de Eventos del Usuario
PySide6 implementa el paradigma desacoplado de **Signals & Slots (Señales y Ranuras)**:
* **Signal (Señal):** Notificación emitida automáticamente por un widget cuando ocurre una acción del usuario (por ejemplo, el clic de un ratón con `QPushButton.clicked` o la pulsación de la tecla Enter con `QLineEdit.returnPressed`).
* **Slot (Ranura):** Método o función receptora encargada de procesar la lógica de negocio.
* **Conexión:** Se asocian limpiamente mediante el método `.connect()`, sin necesidad de manejar cadenas de texto arbitrarias ni alterar el paso de argumentos.

### 1.6. Ventajas y Limitaciones frente a Tkinter

| Criterio | PySide6 | Tkinter |
| :--- | :--- | :--- |
| **Estética y Personalización** | Interfaz moderna, renderizado nativo del sistema y soporte avanzado de hojas de estilo (*Qt Style Sheets* tipo CSS). | Apariencia básica y anticuada por defecto; `ttk` mejora el aspecto pero mantiene limitaciones de personalización. |
| **Arquitectura de Eventos** | *Signals & Slots* fuertemente tipados y desacoplados. | Sistema basado en cadenas de texto mágicas (`"<Return>"`, `"<Button-1>"`) con dependencia estricta del foco activo. |
| **Escalabilidad** | Robusto para proyectos grandes, soporte multinúcleo con `QThread` y herramientas avanzadas de diseño. | Adecuado para scripts sencillos; se vuelve engorroso en proyectos con múltiples vistas o hilos. |
| **Instalación** | Requiere descarga externa vía `pip` (~100 MB). | Viene preinstalado con la biblioteca estándar de Python. |
| **Curva de Aprendizaje** | Requiere comprender orientación a objetos estricta y jerarquías padre-hijo. | Curva baja para scripts procedimentales rápidos. |

---

## 2. Explicación del Funcionamiento

### 2.1. Creación de la Ventana Principal
La aplicación se encapsula en la clase `Ventana`, la cual hereda directamente de `QMainWindow`.
* [Ver bloque de inicialización en el código](#linea-clase-ventana)
* Al instanciar `super().__init__()`, se configuran las dimensiones fijas (`500x330 px`) con `setFixedSize`, el título con `setWindowTitle` y el color de fondo mediante `setStyleSheet`.
* La ventana se expone al sistema operativo mediante el bucle principal administrado por `QApplication(sys.argv)` y `app.exec()`.

### 2.2. Creación y Visualización de Componentes
A diferencia de Tkinter (donde se requiere instanciar y luego invocar `.pack()` o `.grid()`), en PySide6 la pertenencia visual se define pasando el contenedor padre en el constructor:
* [Ver creación del formulario en el código](#linea-componentes-ui)
* `self.frame_titulo = QFrame(self)` establece que el frame pertenece a la ventana principal.
* `self.titulo = QLabel(self.frame_titulo)` hace que la etiqueta resida dentro de ese frame.
* El posicionamiento y dimensionamiento exacto se determina con `setGeometry(x, y, ancho, alto)`, asegurando un diseño fijo y ordenado sin conflicto entre celdas.

### 2.3. Eventos Implementados y Detección
Se implementaron dos mecanismos complementarios de interacción orientada a eventos:
1. **Evento de ratón:** Señal `.clicked` proveniente del widget `QPushButton`.
2. **Evento de teclado:** Señal `.returnPressed` proveniente del widget `QLineEdit`.
* [Ver conexión de señales en el código](#linea-conexion-eventos)
* Ambos eventos detectan la interacción y dirigen el flujo hacia el mismo manejador, garantizando que el usuario pueda enviar el formulario haciendo clic o pulsando la tecla `Enter`.

### 2.4. Método de Respuesta al Evento
* [Ver método obtiene_texto en el código](#linea-metodo-slot)
* El método `obtiene_texto(self)` actúa como el **Slot** receptor.
* Extrae el contenido ingresado en la caja de texto mediante `self.entrada.text()` y aplica la lógica necesaria para actualizar el estado.

### 2.5. Modificación de la Interfaz tras la Interacción
* [Ver apertura de diálogo en el código](#linea-modificacion-interfaz)
* Cuando se dispara `obtiene_texto(self)`, el método altera dinámicamente el texto del cuadro emergente invocando `self.titulo_dialogo.setText(...)`.
* Posteriormente, hace visible el cuadro de diálogo modal invocando `self.dialogo.show()`, mostrando el saludo personalizado junto con la imagen de bienvenida cargada mediante estilos visuales.

---

## 3. Código Fuente del Proyecto

Guarda este archivo bajo el nombre `main.py`:

```python
import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFrame, QLabel, 
    QLineEdit, QPushButton, QDialog
)
from PySide6.QtCore import Qt

# <a id="linea-clase-ventana"></a>
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Primera ventana con PySide6")
        self.setFixedSize(500, 330)
        self.setStyleSheet("background: #242526;")

        # Construcción de la interfaz gráfica
        self.inicializar_UI()

    # <a id="linea-componentes-ui"></a>
    def inicializar_UI(self):
        # Frame 1: Cabecera
        self.frame_titulo = QFrame(self)
        self.frame_titulo.setGeometry(10, 10, 480, 100)
        self.frame_titulo.setStyleSheet("background: #1d2f44;")

        # Título
        self.titulo = QLabel(self.frame_titulo)
        self.titulo.setText("Hola!")
        self.titulo.setGeometry(0, 20, 480, 40)
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo.setStyleSheet("""
            color: white;
            font-size: 25px;
            font-weight: bold;
        """)

        # Frame 2: Formulario interactivo
        self.frame2 = QFrame(self)
        self.frame2.setGeometry(10, 120, 480, 200)
        self.frame2.setStyleSheet("background: #1d2f44;")

        # Enunciado
        self.enunciado = QLabel(self.frame2)
        self.enunciado.setText("Ingresa Tu nombre!")
        self.enunciado.setGeometry(0, 20, 480, 40)
        self.enunciado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.enunciado.setStyleSheet("""
            color: white;
            font-size: 25px;
            font-weight: bold;
        """)

        # Campo de entrada (QLineEdit)
        self.entrada = QLineEdit(self.frame2)
        self.entrada.setGeometry(10, 70, 460, 45)
        self.entrada.setStyleSheet("background: white; color: black; font-size: 16px;")

        # Botón de acción (QPushButton)
        self.boton = QPushButton(self.frame2)
        self.boton.setText("Click me")
        self.boton.setGeometry(10, 130, 460, 40)
        self.boton.setStyleSheet("""
            background: #314F72;
            color: white;
            font-size: 20px;
            font-weight: bold;
        """)

        # <a id="linea-conexion-eventos"></a>
        # Conexión de Eventos: Clic de ratón y Tecla Enter
        self.boton.clicked.connect(self.obtiene_texto)
        self.entrada.returnPressed.connect(self.obtiene_texto)

        # Diálogo emergente de respuesta
        self.dialogo = QDialog(self)
        self.dialogo.setFixedSize(300, 300)
        self.dialogo.setStyleSheet("background: #242526;")

        self.frame_titulo_dialogo = QFrame(self.dialogo)
        self.frame_titulo_dialogo.setGeometry(10, 10, 280, 100)
        self.frame_titulo_dialogo.setStyleSheet("background: #1d2f44;")

        self.titulo_dialogo = QLabel(self.frame_titulo_dialogo)
        self.titulo_dialogo.setGeometry(0, 30, 280, 40)
        self.titulo_dialogo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo_dialogo.setStyleSheet("""
            color: white;
            font-size: 18px;
            font-weight: bold;
        """)

        self.frame_imagen = QFrame(self.dialogo)
        self.frame_imagen.setGeometry(10, 120, 280, 170)
        
        # Ruta dinámica para la imagen
        ruta_script = os.path.dirname(os.path.abspath(__file__))
        ruta_imagen = os.path.join(ruta_script, "images.jpg").replace("\\", "/")
        self.frame_imagen.setStyleSheet(f"border-image: url('{ruta_imagen}') 0 0 0 0 stretch stretch;")

    # <a id="linea-metodo-slot"></a>
    def obtiene_texto(self):
        """Slot encargado de procesar la entrada y modificar la interfaz."""
        nombre = self.entrada.text().strip()
        if not nombre:
            nombre = "Usuario"

        # <a id="linea-modificacion-interfaz"></a>
        self.titulo_dialogo.setText(f"¡Bienvenido {nombre}!")
        self.dialogo.show()
        print(f"Formulario enviado con el nombre: {nombre}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
```

---

## 4. Instrucciones de Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. **Instalar dependencias requeridas:**
   ```bash
   pip install PySide6
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python main.py
   ```

---

## 5. Evidencia Visual

Asegúrate de tener un archivo llamado `captura.png` y tu recurso `images.jpg` en la raíz del proyecto.

### Vista de la Aplicación en Ejecución
<a id="evidencia-captura"></a>
![Captura de la Aplicación en Ejecución](./captura.png)

> **Nota:** Puedes hacer clic directamente en el enlace a la [Captura de la ventana principal y cuadro de diálogo emergente](#evidencia-captura) para inspeccionar la interfaz activa.

---

## 6. Fuentes Consultadas
* The Qt Company. (s.f.). *Qt for Python Documentation (PySide6)*. Recuperado de: [https://doc.qt.io/qtforpython-6/](https://doc.qt.io/qtforpython-6/)
* The Qt Company. (s.f.). *Signals and Slots in PySide6*. Recuperado de: [https://doc.qt.io/qtforpython-6/tutorials/basictutorial/signals_and_slots.html](https://doc.qt.io/qtforpython-6/tutorials/basictutorial/signals_and_slots.html)
* The Qt Company. (s.f.). *Qt Style Sheets Reference*. Recuperado de: [https://doc.qt.io/qt-6/stylesheet-reference.html](https://doc.qt.io/qt-6/stylesheet-reference.html)