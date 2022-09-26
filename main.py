import sys
from bs4 import BeautifulSoup
import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QColorDialog
from PySide6.QtWebEngineWidgets import QWebEngineView
from ui_navegador import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

    #Cargar la página web
        self.loadPage()

    ########################################################
    ## CONEXIONES
    ########################################################
        self.pushButton_instertar.clicked.connect(self.addLine)
        self.pushButton_bold.clicked.connect(self.boldText)
        self.pushButton_italic.clicked.connect(self.italicText)
        self.pushButton_under.clicked.connect(self.subText)
        self.pushButton_color.clicked.connect(self.colorText)
        self.navegador_web.loadFinished.connect(self.scrollDown)


    ########################################################
    ## METODOS
    ########################################################
    
    ##### METODO PARA CARGAR PÁGINA EN QWERBVIEWER
    def loadPage(self):

        with open('page1.html', 'r') as f:

            html = f.read()
            self.navegador_web.setHtml(html)      

    ##### METODO PARA QUE LA SCROLLBAR SE QUEDE ABAJO AUTOMATICAMENTE
    def scrollDown(self):
        self.navegador_web.page().runJavaScript("window.scrollTo(0, document.body.scrollHeight);")    

    ##### METODO PARA INSERTAR LÍNEAS
    def addLine(self):

        # obtener texto de textEdit
        text = self.textEdit.toPlainText()

        #Proseguir si hay texto en textEdit
        if len(text) > 0:

            #Obtener el texto del HTML
            html = "page1.html"
            html_file = open(html, 'r')
            source_code = html_file.read() 

            # Obtener fecha
            date  = datetime.datetime.now()
            # Transformar contenido de la página a Beautiful Soup
            soup = BeautifulSoup(source_code, "html.parser")
            # Transformar contenido del textEdit y fecha a Beautiful Soup
            insert = "<div><b>{}:</b> {}</div>".format(date.strftime("%Y-%m-%d %H:%M:%S"), text)
            b_insert = BeautifulSoup(insert, "html.parser")

            # Crear una nueva etiqueta para insertar divs
            new_div = soup.new_tag("div")

            #Atachar la nueva div a la página
            soup.body.append(b_insert)
            new_html = soup.prettify()

            #Imprimir la nueva línea
            print(new_html)

            #Guardar el nuevo html con esta nueva línea
            output = open("page1.html","w")
            output.write(new_html)
            output.close()

            #Eliminar texto de textEdit
            self.textEdit.clear()
            #Actualizar navegador
            self.loadPage()

        #Si no hay texto mostrará error
        else:
            print("ERROR. Ingresa un texto para insertar")

    ##### METODO PARA TEXTO EN NEGRITA
    def boldText(self):
        cursor = self.textEdit.textCursor()
        QApplication.clipboard().setText("<b>" + cursor.selectedText() + "</b>")
        self.textEdit.paste()

    ##### METODO PARA TEXTO EN CURSIVA
    def italicText(self):
        cursor = self.textEdit.textCursor()
        QApplication.clipboard().setText("<i>" + cursor.selectedText() + "</i>")
        self.textEdit.paste()

    ##### METODO PARA TEXTO EN SUBRAYADO
    def subText(self):
        cursor = self.textEdit.textCursor()
        QApplication.clipboard().setText("<u>" + cursor.selectedText() + "</u>")
        self.textEdit.paste()

    ##### METODO PARA TEXTO EN COLOR
    def colorText(self):
        color = QColorDialog().getColor().name()
        print(color)
        cursor = self.textEdit.textCursor()
        QApplication.clipboard().setText("<font color =\"" + color + "\">" + cursor.selectedText() + "</font>")
        self.textEdit.paste()


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()