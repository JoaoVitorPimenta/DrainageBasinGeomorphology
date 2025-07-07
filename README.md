# Drainage Basin Geomorphology
This plugin provides tools to help geomorphological analysis, especially in drainage basins.

Author = João Vitor Pimenta   
Email = jvpjoaopimenta@gmail.com   

## Technologies
The following technologies were used in processing the algorithms of this plugin:  
- QGIS  
- GeoPandas  
- Numpy  
- Plotly  
- GDAL  
- OGR

## Installation
With QGIS open, follow these steps: plugins -> manage and install plugins -> install from ZIP
Then select the ZIP containing this plugin -> install plugin or place this plugin in the folder corresponding to plugins installed in QGIS.

# Tools
This plugin offers tools for studying the geomorphology of drainage basins, are they:

## Calculate all morphometric parameters
This tool calculates all morphometric parameters of the watershed as shown in the table below. If any known parameter is not being calculated, feel free to message me.

**Inputs:**  
**Drainage basins** - Vector layer containing drainage basin features.

**Channel network** - Vector layer containing the drainage network of the drainage basins.

**Distance limit for connecting channels** - This is the maximum distance to join channels that are not fully connected to correct possible faults in the drainage network.


**DEM** - Digital Elevation Model in the area of the drainage basins.

**Output:**  
**All morphometric parameters** - All morphometric parameters calculated, for each basin, in .csv.

## Calculate elevation area volume above
This tool calculates the elevation area volume curves (above) for all features provided in the drainage basin layer as input.

**Inputs:**  
**Drainage basins** - Vector layer containing drainage basin features.

**DEM** - Digital Elevation Model in the area of the drainage basins.

**Distance between contour lines** - The spacing between contour lines, between the first and last contour lines.

**Base level** - The reference elevation to calculate the area and volume above.

**Output:**  
**Elevation area volume data** - Elevation Area Volume data, for each basin, in .csv.

**Graphs** - Graphs with elevation-area and elevation-volume curves, for each basin, stored in .HTML format in a folder.

## Calculate elevation area volume below
This tool calculates the elevation area volume curves (below) for all features provided in the drainage basin layer as input.

**Inputs:**  
**Drainage basins** - Vector layer containing drainage basin features.

**DEM** - Digital Elevation Model in the area of the drainage basins.

**Distance between contour lines** - The spacing between contour lines, between the first and last contour lines.

**Base level** - The reference elevation to calculate the area and volume below.

**Output:**  
**Elevation area volume data** - Elevation Area Volume data, for each basin, in .csv.

**Graphs** - Graphs with elevation-area and elevation-volume curves, for each basin, stored in .HTML format in a folder.

## Calculate elevation area volume above and below
This tool calculates the elevation area volume curves (above and below) for all features provided in the drainage basin layer as input.

**Inputs:**  
**Drainage basins** - Vector layer containing drainage basin features.

**DEM** - Digital Elevation Model in the area of the drainage basins.

**Distance between contour lines** - The spacing between contour lines, between the first and last contour lines.

**Minimum level** - The minimum elevation of the elevation area volume curve.

**Maximum level** - The maximum elevation of the elevation area volume curve.

**Output:**  
**Elevation area volume data** - Elevation Area Volume data, for each basin, in .csv.

**Graphs** - Graphs with elevation-area and elevation-volume curves, for each basin, stored in .HTML format in a folder.

## Calculate hypsometric curves
This tool calculates and plots the hypsometric curves, with absolute or relative values ​​(from 0 to 1). The hypsometric curves represents the area above a certain elevation.

**Inputs:**  
**Drainage basins** - Vector layer containing drainage basin features.

**DEM** - Digital Elevation Model in the area of the drainage basins.

**Distance between contour lines** - The spacing between contour lines, between the first and last contour lines.

**Output:**  
**Hypsometric curves** - The data used to create the hypsometric curves, for each basin, in .csv.

**Graph** - The graph with the hypsometric curves, for each basin, in .html.

## Calculate linear parameters
This tool calculates linear parameters of the watershed as shown in the table below. If any known parameter is not being calculated, feel free to message me.

**Inputs:**  
**Drainage basins** - Vector layer containing drainage basin features.

**Channel network** - Vector layer containing the drainage network of the drainage basins.

**Distance limit for connecting channels** - This is the maximum distance to join channels that are not fully connected to correct possible faults in the drainage network.

**DEM** - Digital Elevation Model in the area of the drainage basins.

**Output:**  
**All morphometric parameters** - Linear parameters calculated, for each basin in .csv.

## Calculate relief parameters
This tool calculates relief parameters of the watershed as shown in the table below. If any known parameter is not being calculated, feel free to message me.

**Inputs:**  
**Drainage basins** - Vector layer containing drainage basin features.

**Channel network** - Vector layer containing the drainage network of the drainage basins.

**Distance limit for connecting channels** - This is the maximum distance to join channels that are not fully connected to correct possible faults in the drainage network.

**DEM** - Digital Elevation Model in the area of the drainage basins.

**Output:**  
**Shape parameters** - Shape parameters calculated, for each basin, in .csv.

## Calculate shape parameters
This tool calculates shape parameters of the watershed as shown in the table below. If any known parameter is not being calculated, feel free to message me.

**Inputs:**  
**Drainage basins** - Vector layer containing drainage basin features.

**Channel network** - Vector layer containing the drainage network of the drainage basins.

**Distance limit for connecting channels** - This is the maximum distance to join channels that are not fully connected to correct possible faults in the drainage network.

**Output:**  
**Shape parameters** - Shape parameters calculated, for each basin, in .csv.

## Calculate inundated area
This tool calculates the inundated area from the EAV curve, it uses the elevation associated with a user-given curve parameter, and then plots the area below that elevation.

**Inputs:**  
**Drainage basins** - Vector layer containing drainage basin features.

**DEM** - Digital Elevation Model in the area of the drainage basins.

**Parameter** - The elevation - area - volume graph variable to be used to calculate the elevation of the inundated area.

**Parameter value** - The numerical value of the elevation - area - volume graph variable to be used to calculate the elevation of the inundated area.

**Nodata value for output band** - The NoDataValue value of the output raster layer band.

**Output:**  
**Inundation raster** - The raster of the inundated area, the raster band represents the depth related to the inundated area, that is, the bathymetry.

**Inundation vector** - The vector with the inundated area, in the vector attribute table has the EAV curve variables related to the parameter provided by the user.

## Recommendations 
All inputs must be in a projected coordinate system for consistent results.

## Acknowledgment
Special thanks to the authors of all the technologies used in this plugin and who made it possible,
to my parents, friends and teachers.

" If I have seen farther than others, it is because I have stood on the shoulders of giants. " - Isaac Newton

## Contact
If you have any questions, suggestions, errors or need information/training about the plugin, please contact: jvpjoaopimentadev@gmail.com

## License
[GNU General Public License, version 3](https://www.gnu.org/licenses/gpl-3.0.html)

# Calculations

## Morphometric Parameters

| **Category** | **Parameter** | **Symbol** | **Formula**        | **Description**                                                            | **References** |
|--------------|---------------|------------|--------------------|----------------------------------------------------------------------------|----------------|
| Linear       | Stream Order  | _u_        | Hierarchical       | Order of watercourses (Strahler method).                                   |  Strahler (1957)              |
| Linear       | Stream Number | _Nu_       | Count              | Number of stream segments of order _u_.                                    |   Horton (1945)             |
| Linear       | Stream Length Total | _Lu_  | Sum of lengths     | Sum of lengths of streams of order _u_.                                    |     Horton (1945)           |
| Linear       | Stream Length Mean  | _Lmean_ | _Lu / Nu_          | Average length of streams of the same order.                               |  Horton (1945)              |
| Linear       | Stream Length Ratio | _RL_   | _Lu / Lu-1_        | Ratio between lengths of consecutive orders.                               |    Horton (1945)            |
| Linear       | Mean Stream Length Ratio | _⟨RL⟩_ | Average of _RL_    | Average of length ratios between orders.                                   |    Horton (1945)            |
| Linear       | Bifurcation Ratio | _Rb_     | _Nu / Nu+1_        | Ratio between number of channels of consecutive orders.                    |  Horton (1945)              |
| Linear       | Mean Bifurcation Ratio | _⟨Rb⟩_ | Average of _Rb_    | Average of bifurcation ratios.                                             |  Horton (1945)              |
| Linear       | RHO Coefficient | _ρ_       | _⟨RL⟩ / ⟨Rb⟩_          | Correlation between length ratio and bifurcation.                          |   Horton (1945)             |
| Linear       | Main Channel Sinuosity Index | _SI_ | _Lch / Ls_        | Ratio between main channel length and the length of the main channel if it were a straight line.         |   Leopold & Wolman (1957).             |
| Linear       | Fitness Ratio | _Rf_       | _Lch / P_         | Ratio between main channel length and basin perimeter.                             | Melton (1957)               |
| Linear       | Wandering Ratio | _Rw_      | _Lch / Lg_         | Ratio between main channel length and basin length.                              |  Smart & Surkan(1967)              |
| Linear       | Drainage Density | _Dd_     | _Lt / A_           | Ratio of total channel length to basin area.                               |   Horton (1945)             |
| Linear       | Stream Frequency | _Fs_     | _N / A_            | Ratio of total number of segments to basin area.                           |  Horton (1945)              |
| Linear       | Drainage Texture | _Dt_     | _N / P_            | Ratio of number of channels to basin perimeter.                            |  Smith (1950)         |
| Linear       | Length of Overland Flow | _Lg_ | _1 / (2 × Dd)_     | Average length of surface (overland) flow.                                 |   Horton (1945)             |
| Linear       | Constant of Channel Maintenance | _Ccm_ | _1 / Dd_         | Area required to sustain 1 km of channel.                                  |   Schumm (1956)             |
| Linear       | Drainage Intensity | _Di_   | _Fs / Dd_          | Ratio of stream frequency to drainage density.                             |  Faniran (1968)              |
| Linear       | Infiltration Number | _If_  | _Dd × Fs_          | Product of drainage density and stream frequency.                          |  Faniran (1968)              |
| Shape        | Area          | _A_         | Direct measurement | Basin area.                                                                | Shape data|
| Shape        | Perimeter     | _P_         | Direct measurement | Basin perimeter.                                                           |  Shape data|
| Shape        | Basin Length  | _Lb_        | Direct measurement | Length of a straight line passing through the starting and ending points of the highest-order channel to the boundary of the basin.                                    |   Horton (1932)             |
| Shape        | Circulatory Ratio | _Rc_   | _4πA / P²_         | Measures circularity.                                   |          Miller (1953)     |
| Shape        | Elongation Ratio | _Re_    | _(2 × √(A/π)) / Lb_ | Ratio of diameter of equivalent-area circle to basin length.              |   Schumm (1956)             |
| Shape        | Form Factor   | _Ff_        | _A / Lb²_          | Measures compactness of area relative to length.                           |  Horton, R. E. (1932)              |
| Shape        | Lemniscate Ratio | _K_     | _Lb² / 4A_       | index of adjustment of drainage basin shape to the ideal.                                              |   Chorley et al. (1957)             |
| Shape        | Shape Index   | _Sb_        | _Lb² / A_          | Inverse of Form Factor.                                                    |     Horton (1932)           |
| Shape        | Compactness Coefficient | _Cc_ | _P / 2 × √(πA)_    | Compactness normalized for a circle.                                       |      Horton (1932)          |
| Relief       | Minimum Elevation | _Emin_   | Direct measurement | Minimum elevation within basin.                                            | DEM Data           |
| Relief       | Maximum Elevation | _Emax_   | Direct measurement | Maximum elevation within basin.                                            | DEM Data           |
| Relief       | Mean Elevation | _Emean_     | _(Emax + Emin) / 2_ | Average of highest and lowest elevations.                                 | DEM Data           |
| Relief       | Relief (Bh)    | _Bh_        | _Emax – Emin_      | Total relief (elevation range).                                           | DEM Data           |
| Relief       | Relief Ratio   | _Rh_        | _Bh / Lb_          | Ratio of relief to basin length.                                          | Schumm (1956)    |
| Relief       | Relative Relief | _Rhp_      | _Emax / P_           | Ratio of relief to basin area.                                            |  Melton (1957)  |
| Relief       | Ruggedness Number | _Rn_     | _Bh × Dd_          | Product of relief and drainage density.                                   | Strahler (1954)      |
| Relief       | Dissection Index | _Di_      | _(Emax - Emin) / Emax_           | Ratio of relief to perimeter.                                             | Nir Dov (1957)      |
| Relief       | Gradient Ratio | _Gr_       | _(Relief source - Relief mouth) / Lch_         | Ratio between the difference in altitude of the main channel and its length.                                   |  Sreedevi (2005)  |


## Elevation - area - volume below

| Elevation (m)     | Area (m2) | Volume (m3) |
|-------------|----------------|---------------------|
| Pixel elevation data crescent     | Pixel elevation count × (Pixel width × Pixel height) (cumulative)            | Elevation difference × area mean (trapezoid rule) (cumulative)                 |

Strahler (1952)

If the user inputs contour lines, the values ​​will be calculated taking into account all elevations in the DEM, and then the area and volumes values ​​will be interpolated to the contour lines input by the user.

This tool calculates the empty volume of the DEM by elevation.

## Elevation - area - volume above

| Elevation (m)     | Area (m2) | Volume (m3) |
|-------------|----------------|---------------------|
| Pixel elevation data decrescent     | Pixel elevation count × (Pixel width × Pixel height) (cumulative)            | Absolute elevation difference × area mean (trapezoid rule) (cumulative)                 |

Strahler (1952)

If the user inputs contour lines, the values ​​will be calculated taking into account all elevations in the DEM, and then the area and volumes values ​​will be interpolated to the contour lines input by the user.

This tool calculates the solid volume of the DEM by elevation.

## Elevation - area - volume above and below

This tool has the same logic as the calculation of the volume above and below. The volume and area is the difference between the values ​​above and the values ​​below.

## Hypsometric curve

| Relative height     | Relative area | Hypsometric integral |
|-------------|----------------|---------------------|
| (Elevation - Minimum elevation)/(Maximum elevation - Minimum elevation)     | Pixel elevation count × (Pixel width × Pixel height) (cumulative)   |Integral of the curve formed by elevation and area, using the trapezoidal rule.                 |

| Absolute elevation (m)     | Absolute area (m2) | Hypsometric integral |
|-------------|----------------|---------------------|
| Elevation     | Area (cumulative)   |Integral of the curve formed by elevation and area, using the trapezoidal rule.                 |

Strahler (1952)

If the user inputs contour lines, the values ​​will be calculated taking into account all DEM elevations, and then area values ​​will be interpolated for the contour lines the user input.

## Inundated area

| Elevation (m)     | Area (m2) | Volume (m3) |
|-------------|----------------|---------------------|
| Fist elevation from curve     | First area from curve            | First volume from curve                 |
| ...                           | ...                              | ... |
| Interpolated elevation or elevation provided by the user (if the user has chosen the elevation parameter)   | Interpolated area or area provided by the user (if the user has chosen the area parameter) | Interpolated volume or volume provided by the user (if the user has chosen the volume parameter) |
| ...                           | ...                              | ... |
| Last elevation from curve     | Last area from curve             | Last volume from curve 

The inundated area, in both raster and vector layers, is the area of ​​pixels below the interpolated or given elevation (bathymetry).

The inundated raster layer band is the elevation value of the pixels minus the lowest elevation value within the basin.

The attribute table of the vector layer contains information about all the parameters associated with what was provided by the user. (Example: if the volume of X is provided, the attribute table will have the height, elevation and interpolated area for X)

## References
- Horton, R. E. (1932). Drainage-basin characteristics. Transactions of the American Geophysical Union, 13, 350–361.

- Smith, K. (1950). Standards for Grading Textures of Erosional Topography. American Journal of Science, 248, 655–668.

- Strahler, A. N. (1952). Hypsometric (Area-Altitude) Analysis of Erosional Topography. Geological Society of America Bulletin, 63(11), 1117–1142.

- Miller, V. C. (1953). A quantitative geomorphologic study of drainage basin characteristics in the Clinch mountain area, Virginia and Tennessee (Technical Report No. 3). Columbia University, New York.

- Strahler, A. N. (1954). Quantitative geomorphology of drainage basins and channel networks. In V. T. Chow (Ed.), Handbook of Applied Hydrology (Vol. 4, pp. 39–76). McGraw-Hill.

- Schumm, H. J. (1956). Evolution of drainage systems and slopes in badlands at Perth Amboy, New Jersey. Geological Society of America Bulletin, 67(5), 597–646.

- Melton, M. A. (1957). An analysis of the relations among the elements of climate, surface properties and geomorphology (Technical Report No. 11). Department of Geology, Columbia University, New York.

- Leopold, L. B., & Wolman, M. G. (1957). River channel patterns: Braided, meandering, and straight (U.S. Geological Survey Professional Paper 282–B). U.S. Government Printing Office.

- Strahler, A. N. (1957). Quantitative analysis of watershed geomorphology. Transactions of the American Geophysical Union, 38(6), 913–920.

- Dov, N. (1957). The ratio of relative relief and absolute altitudes of Mt.Carmel. Geographical Review, 47, 565.

- Chorley, R. J., Malm, D. E. G., & Pogorzelski, H. A. (1957). A new standard for estimating drainage basin shape. American Journal of Science, 225, 138–141.

- Smart, J. S., & Surkan, A. J. (1967). The relation between mainstream length and area in drainage basins. Water Resources Research, 3(4), 963–973.

- Faniran, A. (1968). The Index of Drainage Intensity—A Provisional New Drainage Factor. Australian Journal of Science, 31, 328–330.

- Sreedevi, P. D., Subrahmanyam, K., & Ahmed, S. (2005). The Significance of Morphometric Analysis for Obtaining Groundwater Potential Zones in a Structurally Controlled Terrain. Environmental Geology, 47, 412–420.

