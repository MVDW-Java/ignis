from gi.repository import Gtk, Adw  # type: ignore
from ignis.base_widget import BaseWidget
from collections.abc import Callable
from ignis.gobject import IgnisProperty


class ToggleButton(Adw.ToggleButton, BaseWidget):
    """
    Bases: :class:`Adw.ToggleButton`

    A toggle button widget.

    Args:
        **kwargs: Properties to set.

    .. code-block:: python

        widgets.ToggleButton(
            on_toggled=lambda x, active: print(active)
        )
    """

    __gtype_name__ = "IgnisToggleButton"
    __gproperties__ = {**BaseWidget.gproperties}

    def __init__(self, **kwargs) -> None:
        Adw.ToggleButton.__init__(self)
        self._on_toggled: Callable | None = None
        BaseWidget.__init__(self, **kwargs)

        self.connect(
            "toggled",
            lambda x: self.on_toggled(self, self.active) if self.on_toggled else None,
        )

    @IgnisProperty
    def on_toggled(self) -> Callable | None:
        """
        The function to call when the button is toggled by the user.
        """
        return self._on_toggled

    @on_toggled.setter
    def on_toggled(self, value: Callable | None) -> None:
        self._on_toggled = value
