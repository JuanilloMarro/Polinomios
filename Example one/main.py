import sys
from typing import TypeVar
from doubly_linked_list import DoublyLinkedList
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

T = TypeVar('T')

first_polynomial: DoublyLinkedList[int] = DoublyLinkedList()
second_polynomial: DoublyLinkedList[int] = DoublyLinkedList()
current_polynomial_adicion: DoublyLinkedList[int] = DoublyLinkedList()
current_polynomial_sustraccion: DoublyLinkedList[int] = DoublyLinkedList()

first_polynomial.append(6)
first_polynomial.append(7)

second_polynomial.append(5)
second_polynomial.append(9)
second_polynomial.append(8)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('interface.ui', self)

        self.setWindowTitle('Laboratorio 2 - Polinomios')

        self.btn_hide_menu.hide()
        self.frame_menu.hide()

        self.btn_show_menu.clicked.connect(self.show_menu)
        self.btn_hide_menu.clicked.connect(self.hide_menu)

        self.btn_add.clicked.connect(self.show_page_add)
        self.btn_operations.clicked.connect(self.show_page_operations)
        self.btn_evaluate.clicked.connect(self.show_page_evaluate)
        self.btn_tips.clicked.connect(self.show_page_inicio)

        self.btn_a.clicked.connect(self.add_to_first_polynomial)
        self.btn_b.clicked.connect(self.add_to_second_polynomial)

        self.btn_a_2.clicked.connect(self.evaluate_into_first_polynomial)
        self.btn_b_2.clicked.connect(self.evaluate_into_second_polynomial)

        self.btn_refresh.clicked.connect(self.refresh_data_add)
        self.btn_refresh_2.clicked.connect(self.refresh_data_operations)
        self.btn_refresh_3.clicked.connect(self.refresh_data_evaluate)
        self.btn_refresh_4.clicked.connect(self.refresh_data)

        self.btn_adicion.clicked.connect(self.adicion)
        self.btn_sustraccion.clicked.connect(self.sustraccion)

    def hide_menu(self):
        self.btn_hide_menu.hide()
        self.btn_show_menu.show()
        self.frame_menu.hide()

    def show_menu(self):
        self.btn_hide_menu.show()
        self.btn_show_menu.hide()
        self.frame_menu.show()

    def show_page_add(self):
        self.stackedWidget.setCurrentWidget(self.page_add)

    def show_page_operations(self):
        self.stackedWidget.setCurrentWidget(self.page_operations)

    def show_page_evaluate(self):
        self.stackedWidget.setCurrentWidget(self.page_evaluate)

    def show_page_inicio(self):
        self.stackedWidget.setCurrentWidget(self.page)

    def add_to_first_polynomial(self):
        coeficiente = int(self.coeficiente.text())
        first_polynomial.prepend(coeficiente)
        self.coeficiente.setText('')

    def add_to_second_polynomial(self):
        coeficiente = int(self.coeficiente.text())
        second_polynomial.prepend(coeficiente)
        self.coeficiente.setText('')

    def adicion(self):
        if first_polynomial.size >= second_polynomial.size:

            while second_polynomial.size > 0:
                first_element = first_polynomial.pop()
                second_element = second_polynomial.pop()
                current_polynomial_adicion.prepend(first_element + second_element)

            while first_polynomial.size > 0:
                first_element = first_polynomial.pop()
                current_polynomial_adicion.prepend(first_element)

        else:

            while first_polynomial.size > 0:
                first_element = first_polynomial.pop()
                second_element = second_polynomial.pop()
                current_polynomial_adicion.prepend(first_element + second_element)

            while second_polynomial.size > 0:
                first_element = second_polynomial.pop()
                current_polynomial_adicion.prepend(first_element)

        self.label_c_a.setText(current_polynomial_adicion.transversal())

    def sustraccion(self):
        if first_polynomial.size >= second_polynomial.size:

            while second_polynomial.size > 0:
                first_element = first_polynomial.pop()
                second_element = second_polynomial.pop()
                current_polynomial_sustraccion.prepend(first_element - second_element)

            while first_polynomial.size > 0:
                first_element = first_polynomial.pop()
                current_polynomial_sustraccion.prepend(first_element)
        else:

            while first_polynomial.size > 0:
                first_element = first_polynomial.pop()
                second_element = second_polynomial.pop()
                current_polynomial_sustraccion.prepend(first_element - second_element)

            while second_polynomial.size > 0:
                first_element = second_polynomial.pop()
                current_polynomial_sustraccion.prepend(first_element)

        self.label_c_a.setText(current_polynomial_sustraccion.transversal())

    def evaluate_into_first_polynomial(self):
        number = int(self.evaluate_number.text())
        grade = 0
        total = 0

        self.label_a_evaluate.setText(first_polynomial.evaluate_transversal(number))

        while first_polynomial.size > 0:
            element = first_polynomial.pop()
            total += element * (number ** grade)
            grade += 1

        self.evaluate_number.setText('')
        self.label_total.setText(str(total))

    def evaluate_into_second_polynomial(self):
        number = int(self.evaluate_number.text())
        grade = 0
        total = 0

        self.label_b_evaluate.setText(second_polynomial.evaluate_transversal(number))

        while second_polynomial.size > 0:
            element = second_polynomial.pop()
            total += element * (number ** grade)
            grade += 1

        self.evaluate_number.setText('')
        self.label_total.setText(str(total))

    def refresh_data_add(self):
        self.label_final_a.setText(first_polynomial.transversal())
        self.label_final_b.setText(second_polynomial.transversal())

    def refresh_data_operations(self):
        self.label_inicio_a_2.setText(first_polynomial.transversal())
        self.label_inicio_b_2.setText(second_polynomial.transversal())

    def refresh_data_evaluate(self):
        self.label_inicio_a_3.setText(first_polynomial.transversal())
        self.label_inicio_b_3.setText(second_polynomial.transversal())

    def refresh_data(self):
        self.label_inicio_a.setText(first_polynomial.transversal())
        self.label_inicio_b.setText(second_polynomial.transversal())


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
