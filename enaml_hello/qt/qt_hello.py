from atom.api import Typed

from enaml_hello.widgets.hello import ProxyHello

from enaml.qt.QtGui import QLabel

from enaml.qt.qt_control import QtControl


class QHello(QLabel):

    def __init__(self, *args, **kwargs):
        super(QHello, self).__init__(*args, **kwargs)
        font = self.font()
        font.setBold(True)
        self.setFont(font)

    def setText(self, text):
        super(QHello, self).setText('Hello {}'.format(text))


class QtHello(QtControl, ProxyHello):
    """ A Qt implementation of an Enaml ProxyHello.

    """
    #: A reference to the widget created by the proxy.
    widget = Typed(QHello)

    #--------------------------------------------------------------------------
    # Initialization API
    #--------------------------------------------------------------------------
    def create_widget(self):
        """ Create the underlying Hello widget.

        """
        self.widget = QHello(self.parent_widget())

    def init_widget(self):
        """ Initialize the underlying widget.

        """
        super(QtHello, self).init_widget()
        d = self.declaration
        self.set_name(d.name)

    #--------------------------------------------------------------------------
    # ProxyHello API
    #--------------------------------------------------------------------------
    def set_name(self, name):
        """ Set the text in the widget.

        """
        with self.geometry_guard():
            self.widget.setText(name)


def hello_factory():
    """ This is the factory method that gets called by the entry point.

    """
    return QtHello

