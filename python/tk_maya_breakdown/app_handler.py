"""
Copyright (c) 2012 Shotgun Software, Inc
----------------------------------------------------
"""
import tempfile
import os
import platform
import sys
import uuid
import shutil


class AppHandler(object):
    """
    Handles the startup of the UIs, wrapped so that
    it works nicely in batch mode.
    """
    
    def __init__(self, app):
        self._app = app

    def show_dialog(self):
        # do the import just before so that this app can run nicely in nuke
        # command line mode,
        from .dialog import AppDialog
        
        # some QT notes here. Need to keep the dialog object from being GC-ed
        # otherwise pyside will go hara kiri. QT has its own loop to track
        # objects and destroy them and unless we store the dialog as a member
        self._dialog = AppDialog(self._app)
        
        # run modal dialogue
        self._dialog.exec_()
        
        # on the mac, need to delete it - otherwise a "ghost" will remain
        # after closing has happened - on other platforms, however, this
        # double deletion crashes Nuke >.<
        if sys.platform == "darwin":
            self._dialog.deleteLater()