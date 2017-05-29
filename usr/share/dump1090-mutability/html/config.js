// --------------------------------------------------------
//
// This file is to configure the configurable settings.
// Load this file before script.js file at gmap.html.
//
// --------------------------------------------------------

// -- Output Settings -------------------------------------
// Show metric values
// This controls the units used in the plane table,
// and whether metric or imperial units are shown first
// in the detailed plane info.
Metric = false; // true or false

// -- Map settings ----------------------------------------
// These settings are overridden by any position information
// provided by dump1090 itself. All positions are in decimal
// degrees.

// Default center of the map.
DefaultCenterLat = 45.0;
DefaultCenterLon = 9.0;
// The google maps zoom level, 0 - 16, lower is further out
DefaultZoomLvl   = 7;

SiteShow    = true;           // true to show a center marker
SiteLat     = #;            // position of the marker
SiteLon     = #;
SiteName    = "My Radar Site"; // tooltip of the marker


// -- Marker settings -------------------------------------
// The default marker color
MarkerColor       = "rgb(127, 127, 127)";
SelectedColor = "rgb(225, 225, 225)";
StaleColor = "rgb(190, 190, 190)";


SiteCircles = true; // true to show circles (only shown if the center marker is shown)
// In nautical miles or km (depending settings value 'Metric')
SiteCirclesDistances = new Array(20,40,60,80,100);

// Show the clocks at the top of the righthand pane? You can disable the clocks if you want here
ShowClocks = true;

// Controls page title, righthand pane when nothing is selected
PageName = "CJ's Radar";
