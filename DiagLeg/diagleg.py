# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DiagLeg
                                 A QGIS plugin
 Diagram Legend Plugin
                              -------------------
        begin                : 2013-06-18
        copyright            : (C) 2013 by Joana Simoes/FAO
        email                : info@doublebyte.net
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import sys, os.path

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
import diaglegdialog

sys.path.append('/home/joana/.eclipse/org.eclipse.platform_3.8_155965261/plugins/org.python.pydev_2.8.2.2013090511/pysrc')
from pydevd import *

class DiagLeg:
    
    def __init__(self, iface):
        #Debug VERSION: REMOVE THIS FOR RELEASE!!! /////////////7
        #settrace()

        self.iface = iface
        self.qgsVersion = unicode(QGis.QGIS_VERSION_INT)

        # For i18n support
        userPluginPath = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/DiagLeg"
        systemPluginPath = QgsApplication.prefixPath() + "/python/plugins/DiagLeg"

        overrideLocale = QSettings().value("locale/overrideFlag", False)
        if not overrideLocale:
            localeFullName = QLocale.system().name()
        else:
            localeFullName = QSettings().value("locale/userLocale", "")

        if QFileInfo(userPluginPath).exists():
            translationPath = userPluginPath + "/i18n/DiagLeg" + localeFullName + ".qm"
        else:
            translationPath = systemPluginPath + "/i18n/DiagLeg" + localeFullName + ".qm"

        self.localePath = translationPath
        if QFileInfo(self.localePath).exists():
            self.translator = QTranslator()
            self.translator.load(self.localePath)
            QCoreApplication.installTranslator(self.translator)


    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/diagleg/icon.png"), \
            u"DiagLeg", self.iface.mainWindow())
            
    	self.iface.registerMainWindowAction(self.action, "F7") # action1 is triggered by the F7 key
    	QObject.connect(self.action, SIGNAL("triggered()"),self.keyActionF7)
                        
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&GISforEAF", self.action)	  
                
    def unload(self):
        self.iface.removePluginMenu("&GISforEAF",self.action)
        self.iface.removeToolBarIcon(self.action)        
        self.iface.unregisterMainWindowAction(self.action)
	  
    def keyActionF7(self):
      self.run()
	  	  
    # run method that performs all the real work
    def run(self):            
        dlg = diaglegdialog.DiagLegDialog()
        dlg.exec_()          
            
