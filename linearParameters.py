# -*- coding: utf-8 -*-

'''
/***************************************************************************
 DrainageBasinGeomorphology
                                 A QGIS plugin
 This plugin provides tools for geomorphological analysis in drainage basins.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2025-03-22
        copyright            : (C) 2025 by João Vitor Pimenta
        email                : jvpjoaopimenta@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
'''

__author__ = 'João Vitor Pimenta'
__date__ = '2025-03-22'
__copyright__ = '(C) 2025 by João Vitor Pimenta'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.core import (QgsProcessing,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFileDestination,
                       QgsProcessingParameterNumber)
from .algorithms.parametersProcessing import calculateLinearParameters,verifyLibs

class linearParametersCalc(QgsProcessingAlgorithm):
    '''
    This is an example algorithm that takes a vector layer and
    creates a new identical one.

    It is meant to be used as an example of how to create your own
    algorithms and explain methods and variables used to do it. An
    algorithm like this will be available in all elements, and there
    is not need for additional work.

    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    '''

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    LINEAR_PARAMETERS = 'LINEAR_PARAMETERS'
    DRAINAGE_BASINS = 'DRAINAGE_BASINS'
    DEM = 'DEM'
    CHANNEL_NETWORK = 'CHANNEL_NETWORK'
    CHANNEL_COORDINATE_PRECISION = 'CHANNEL_COORDINATE_PRECISION'

    def initAlgorithm(self, config):
        '''
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        '''

        # We add the input vector features source. It can have any kind of
        # geometry.
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.DRAINAGE_BASINS,
                self.tr('Drainage basins'),
                [QgsProcessing.TypeVectorPolygon]
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.CHANNEL_NETWORK,
                self.tr('Channel network'),
                [QgsProcessing.TypeVectorLine]
            )
        )

        self.addParameter(
            QgsProcessingParameterNumber(
                self.CHANNEL_COORDINATE_PRECISION,
                self.tr('Channel coordinate precision'),
                type=QgsProcessingParameterNumber.Double,
                minValue=0,
                defaultValue=0.000001,
                optional=True
            )
        )

        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterFileDestination(
                self.LINEAR_PARAMETERS,
                self.tr('Linear parameters'),
                fileFilter=('CSV files (*.csv)')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        '''
        Here is where the processing itself takes place.
        '''

        # Retrieve the feature source and sink. The 'dest_id' variable is used
        # to uniquely identify the feature sink, and must be included in the
        # dictionary returned by the processAlgorithm function.
        basinSource = self.parameterAsSource(parameters, self.DRAINAGE_BASINS, context)

        channelNetwork = self.parameterAsSource(parameters, self.CHANNEL_NETWORK, context)

        precisionSnapCoordinates = self.parameterAsDouble(parameters, self.CHANNEL_COORDINATE_PRECISION, context)

        path = self.parameterAsFileOutput(parameters, self.LINEAR_PARAMETERS, context)

        verifyLibs()
        calculateLinearParameters(basinSource,channelNetwork,path,feedback,precisionSnapCoordinates)

        # Return the results of the algorithm. In this case our only result is
        # the feature sink which contains the processed features, but some
        # algorithms may return multiple feature sinks, calculated numeric
        # statistics, etc. These should all be included in the returned
        # dictionary, with keys matching the feature corresponding parameter
        # or output names.
        return {self.LINEAR_PARAMETERS: path}

    def name(self):
        '''
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        '''
        return 'Calculate linear parameters'

    def displayName(self):
        '''
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        '''
        return self.tr(self.name())

    def group(self):
        '''
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        '''
        return self.tr(self.groupId())

    def icon(self):
        """
        Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        return QIcon(os.path.join(os.path.dirname(__file__), "icon.png"))

    def shortHelpString(self):
        """
        Returns a localised short help string for the algorithm.
        """
        return self.tr("""
        <html>
            <body>
                <p>       
        This tool calculates all linear parameters of each basin feature individually.               
                </p>
                <p>
        <strong>Drainage basins: </strong>Layer containing drainage basins as features.
        <strong>Channel network: </strong>Layer containing the drainage network of the drainage basins.
        <strong>Channel coordinate precision: </strong>It is the precision of the channel coordinates, for example: for a precision of 0.000001 the coordinate xxxxxx.xxxxxxxxxxxx becomes xxxxxx.xxxxxx. It is recommended to use 0.000001 to correct possible geometry errors when selecting channels that intersect the basin. If it is 0, there will be no rounding.
        <strong>Linear parameters: </strong>File with all linear parameters calculated individually for each basin.
        
        The use of a projected CRS is recommended (the plugin calculation assumes that all input layers are in projected coordinate reference systems).
                       
        If you need more information about how the plugin works, such as the calculations it performs, among other things, access: https://github.com/JoaoVitorPimenta/qgis-plugin-Drainage-Basin-Geomorphology
        If you have found any bugs, errors or have any requests to make, among other things, please acess: https://github.com/JoaoVitorPimenta/qgis-plugin-Drainage-Basin-Geomorphology/issues
        If you need training for the plugin, or want to contact the plugin author for any reason, send an email to: jvpjoaopimentadev@gmail.com                </p>
            </body>
        </html>
                    """)

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return linearParametersCalc()
