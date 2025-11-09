from gi.repository import Gtk, Adw  # type: ignore
from ignis.base_widget import BaseWidget


class StackSwitcher(Adw.StackSwitcher, BaseWidget):
    """
    Bases: :class:`Adw.StackSwitcher`

    The StackSwitcher shows a row of buttons to switch between :class:`~ignis.widgets.Stack` pages.

    Args:
        **kwargs: Properties to set.
    """

    __gtype_name__ = "IgnisStackSwitcher"
    __gproperties__ = {**BaseWidget.gproperties}

    def __init__(self, **kwargs):
        Adw.StackSwitcher.__init__(self)
        BaseWidget.__init__(self, **kwargs)
