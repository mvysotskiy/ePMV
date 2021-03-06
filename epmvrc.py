# Resource file used to customize PMV.
#
# Visit http://mgltools.scripps.edu/documentation/how-to/changing-default-parameters
# to learn how to change default parameters using _pmvrc.
#
# $Header: /opt/cvs/python/packages/share1.5/Pmv/_pmvrc,v 1.78 2010/11/01 17:44:28 sanner Exp $
#
# $Id: _pmvrc,v 1.78 2010/11/01 17:44:28 sanner Exp $

import pickle
import sys

numOfSelectedVerticesToSelectTriangle = 1 # 1 , 2 or 3

# import the python debugger pdb
#import pdb

# load a set of standard commands 

self.browseCommands('fileCommands', package="Pmv", topCommand=0)
self.browseCommands('bondsCommands',package='Pmv', topCommand=0)

self.browseCommands('deleteCommands',package='Pmv', topCommand=0)
if sys.version_info <= (2, 7):
    self.browseCommands('displayCommands',
                        commands=['displaySticksAndBalls','undisplaySticksAndBalls',
                                  'displayCPK', 'undisplayCPK',
                                  'displayLines','undisplayLines',
                                  'displayBackboneTrace','undisplayBackboneTrace',
                                  ],
                        package='Pmv', topCommand=0)
    
    self.browseCommands('displayCommands',
                        commands=['showMolecules'],
                        package='Pmv', topCommand=0)
                        
    self.browseCommands('displayCommands', commands=['DisplayBoundGeom'],package='ePMV.pmv_dev', topCommand=0)    
else :
    self.browseCommands('displayCommands',
                        commands=['displaySticksAndBalls','undisplaySticksAndBalls',
                                  'displayCPK', 'undisplayCPK',
                                  'displayLines','undisplayLines',
                                  'displayBackboneTrace','undisplayBackboneTrace',
                                  ],
                        package='Pmv', topCommand=0)
    
    self.browseCommands('displayCommands',
                        commands=['showMolecules'],
                        package='Pmv', topCommand=0)
                        
    self.browseCommands('displayCommands_3x', commands=['DisplayBoundGeom'],package='ePMV.pmv_dev', topCommand=0)    
                   
self.browseCommands('editCommands',package='Pmv', topCommand=0)
if self.hasGui:
   self.browseCommands("interactiveCommands", package="Pmv", topCommand=0)
   
#self.browseCommands("secondaryStructureCommands", package="Pmv", topCommand=0)
if sys.version_info <= (2, 7): 
    self.browseCommands('secondaryStructureCommands', package='ePMV.pmv_dev', topCommand=0)
else : 
    self.browseCommands("secondaryStructureCommands", package="Pmv", topCommand=0)

self.browseCommands('beadedRibbonsCommands', package="ePMV.pmv_dev", topCommand=0)


self.browseCommands("splineCommands", package="Pmv", topCommand=0)

#self.browseCommands("coarseMolSurfaceCommands", package="Pmv", topCommand=0)

mslib_import = False
try:#msms is not distributed with commercial version, so we need this to avoid the Traceback
    import mslib
    mslib_import = True
except ImportError:
    mslib_import = False
if mslib_import:
    self.browseCommands('msmsCommands',
	                    commands=['computeMSMS',
	                              'displayMSMS', 'undisplayMSMS',
	                              'readMSMS', 'saveMSMS',
	                              'computeSESAndSASArea',
	                              ],
	                    package='Pmv', topCommand=0)

self.browseCommands('selectionCommands', commands=['select', 'deselect',
                                                   'clearSelection', 'saveSet',
                                                   'invertSelection',
                                                   'selectSet',
                                                   'selectFromString',
                                                   'directSelect',
						   'selectHeteroAtoms'],
                    package='Pmv', topCommand=0)
if self.hasGui:
    self.browseCommands('APBSCommands', package='Pmv', topCommand=0)
else :
    if sys.version_info <= (2, 7):
        self.browseCommands('APBSCommands_2x', package='ePMV.pmv_dev', topCommand=0)
        self.browseCommands('colorCommands',package='ePMV.pmv_dev', topCommand=0)
    else :
        self.browseCommands('APBSCommands', package='ePMV.pmv_dev', topCommand=0)
        self.browseCommands('colorCommands_3x',package='ePMV.pmv_dev', topCommand=0)

self.browseCommands('buildDNACommands',package='ePMV.pmv_dev', topCommand=0)#commands=['buildDNA']
#self.browseCommands('strutsCommands', package='ePMV.pmv_dev',commands=['buildStruts'], topCommand=0)

self.browseCommands('repairCommands', package='Pmv', topCommand=0)
self.browseCommands("dejaVuCommands", package="ViewerFramework", topCommand=0)
                    
#self.browseCommands('helpCommands',package ='Pmv', topCommand =0)

# load command: edit - color palettes - Edit Color By Atom Type Palette
if self.hasGui:
    self.browseCommands('colorPaletteCommands',
                        commands=['editColorPaletteByAtomType', 'editColorPaletteByResidueType', 
                                  'editColorPaletteByChain', 'editColorPaletteByMolecule' ],
                        package='Pmv', topCommand=0)
#self.browseCommands('superimposeCommandsNew', package='Pmv', topCommand=0)
self.browseCommands('setangleCommands', package='Pmv', topCommand=0)
if self.hasGui:
    # The following commands will be executed on the molecule when
    # loaded in the viewer.
    self.setOnAddObjectCommands(['buildBondsByDistance','displayLines','colorByAtomType'],
                           topCommand=0)

    # bind several shortcut to commands
    self.bindCmdToKey( 'z', 'Control_L', self.undo, topCommand=0)

	# not needed anymore as theese command are set on modifiers at startup
    #self.bindCmdToKey( 's', 'Control_L', self.setICOM,
    #                   (self.select,), topCommand=0)
    #self.bindCmdToKey( 'd', 'Control_L', self.setICOM,
    #                   (self.deselect,), topCommand=0)
    #self.bindCmdToKey( 'p', 'Control_L', self.setICOM,
    #                   (self.printNodeNames,), topCommand=0)
    


# Set some user preferences
if self.hasGui:
    self.setUserPreference(('Transformation Logging', 'final'), topCommand=0)
    self.setUserPreference(('Show Progress Bar', 'show'), topCommand=0)
    self.setUserPreference(('Sharp Color Boundaries for MSMS', 'blur'), topCommand=0)
#self.GUI.floatCamera()
#self.GUI.addToolBar('large')

if self.hasGui and 'dashboard' in self.commands:
    # adding columns to dashboard
    self.dashboardSuspendRedraw(True)

    #from Pmv.dashboard import visibilityColDescr
    #self.addDashboardCmd(visibilityColDescr, log=0)

    from Pmv.dashboard import selectColDescr
    self.addDashboardCmd(selectColDescr, log=0)

    from Pmv.dashboard import displayLinesColDescr
    self.addDashboardCmd(displayLinesColDescr, log=0)

    from Pmv.dashboard import displaySandBColDescr
    self.addDashboardCmd(displaySandBColDescr, log=0)

    from Pmv.dashboard import displayCPKColDescr
    self.addDashboardCmd(displayCPKColDescr, log=0)

    from Pmv.dashboard import displaySSColDescr
    self.addDashboardCmd(displaySSColDescr, log=0)

    if mslib_import:
        from Pmv.dashboard import displayMSMSColDescr
        self.addDashboardCmd(displayMSMSColDescr, log=0)

    #from Pmv.dashboard import labelColDescr
    #self.addDashboardCmd(labelColDescr, log=0)

    from Pmv.dashboard import labelMenuColDescr
    self.addDashboardCmd(labelMenuColDescr, log=0)

    from Pmv.dashboard import colorMenuColDescr
    self.addDashboardCmd(colorMenuColDescr, log=0)

##     from Pmv.dashboard import colAtColDescr
##     self.addDashboardCmd(colAtColDescr, log=0)

##     from Pmv.dashboard import colMolColDescr
##     self.addDashboardCmd(colMolColDescr, log=0)

##     from Pmv.dashboard import colChainColDescr
##     self.addDashboardCmd(colChainColDescr, log=0)

##     from Pmv.dashboard import colResRASColDescr
##     self.addDashboardCmd(colResRASColDescr, log=0)

##     from Pmv.dashboard import colResSHAColDescr
##     self.addDashboardCmd(colResSHAColDescr, log=0)

##     from Pmv.dashboard import colDGColDescr
##     self.addDashboardCmd(colDGColDescr, log=0)

##     from Pmv.dashboard import colSSColDescr
##     self.addDashboardCmd(colSSColDescr, log=0)

##     from Pmv.dashboard import colInstColDescr
##     self.addDashboardCmd(colInstColDescr, log=0)

    self.dashboardSuspendRedraw(False)

    self.GUI.ROOT.update()
    # set dahboard size
    self.dashboard.setNaturalSize()
   
    self.GUI.ROOT.after_idle(self.fetch.checkCache)

#self.browseCommands('serverCommands', commands=[
#    'startServer', 'connectToServer', 'StartWebControlServer'],
#                    package='ViewerFramework', topCommand=0)
#                    


