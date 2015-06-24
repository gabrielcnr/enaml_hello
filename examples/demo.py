import enaml
from enaml.qt.qt_application import QtApplication

if __name__ == '__main__':
    with enaml.imports():
        from demo_window import DemoWindow

    app = QtApplication()

    view = DemoWindow()
    view.show()

    app.start()
