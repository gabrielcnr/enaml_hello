from atom.api import (
    Typed, ForwardTyped, Unicode, observe, set_default
)

from enaml.core.declarative import d_

from enaml.widgets.control import Control, ProxyControl



class ProxyHello(ProxyControl):
    """ The abstract definition of a proxy HelloWidget object.

    """
    #: A reference to the Hello declaration.
    declaration = ForwardTyped(lambda: Hello)

    def set_name(self, name):
        raise NotImplementedError



class Hello(Control):
    """ A simple control for displaying Hello <name>!.

    """
    name = d_(Unicode())

    #: Labels hug their width weakly by default.
    hug_width = set_default('weak')

    #: A reference to the ProxyHello object.
    proxy = Typed(ProxyHello)

    #--------------------------------------------------------------------------
    # Observers
    #--------------------------------------------------------------------------
    @observe('name')
    def _update_proxy(self, change):
        """ An observer which sends the state change to the proxy.

        """
        # The superclass implementation is sufficient.
        super(Hello, self)._update_proxy(change)
