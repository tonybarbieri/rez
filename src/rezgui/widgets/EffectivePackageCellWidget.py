from rezgui.qt import QtCore, QtGui
from rezgui.util import create_pane, get_icon_widget
from rez.resolved_context import PatchLock


class EffectivePackageCellWidget(QtGui.QWidget):
    def __init__(self, request, type_, parent=None):
        super(EffectivePackageCellWidget, self).__init__(parent)

        if type_ == "implicit":
            tooltip = "implicit package"
        else:
            tooltip = PatchLock[type_].description

        icon_widget = get_icon_widget(type_, tooltip)
        label = QtGui.QLabel(str(request))
        font = label.font()
        font.setItalic(True)
        label.setFont(font)

        create_pane([icon_widget, (label, 1)], True, parent_widget=self,
                    compact=True)
        self.setEnabled(False)  # this widget always disabled by design