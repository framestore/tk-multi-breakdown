"""
Copyright (c) 2012 Shotgun Software, Inc
----------------------------------------------------
"""
import os
import sys

from PySide import QtCore, QtGui 

class ThumbnailLabel(QtGui.QLabel):

    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)

    def setPixmap(self, pixmap):
        
        # scale the pixmap down to fit
        if pixmap.height() > 80 or pixmap.width() > 120:
            # scale it down to 120x80
            pixmap = pixmap.scaled( QtCore.QSize(120,80), 
                                    QtCore.Qt.KeepAspectRatio, 
                                    QtCore.Qt.SmoothTransformation)
        
        # now slap it on top of a 120x80 transparent canvas
        rendered_pixmap = QtGui.QPixmap(120, 80)
        rendered_pixmap.fill(QtCore.Qt.transparent)

        w_offset = (120 - pixmap.width()) / 2
        h_offset = (80 - pixmap.height()) / 2
        
        painter = QtGui.QPainter(rendered_pixmap)
        painter.drawPixmap(w_offset, h_offset, pixmap)
        painter.end()
        
        # and finally assign it
        QtGui.QLabel.setPixmap(self, rendered_pixmap)
