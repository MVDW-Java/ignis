from gi.repository import Gtk, Adw  # type: ignore
from ignis.base_widget import BaseWidget


class StackSwitcher(Adw.ViewSwitcher, BaseWidget):
    """
    Bases: :class:`Adw.ViewSwitcher`

    The StackSwitcher shows a row of buttons to switch between :class:`~ignis.widgets.Stack` pages.

    Args:
        **kwargs: Properties to set.
    """

    __gtype_name__ = "IgnisStackSwitcher"
    __gproperties__ = {**BaseWidget.gproperties}

    def __init__(self, **kwargs):
        Adw.ViewSwitcher.__init__(self)
        BaseWidget.__init__(self, **kwargs)
