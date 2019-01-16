// Creating map object
var myMap = L.map("map", {
  center: [38.9072, -77.0369],
  zoom: 11
});

// Adding tile layer to the map
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

// Query URL
var geoJSONdata = "https://raw.githubusercontent.com/dbikindu/Project_MovingViolations/master/map/mv_2018.geojson"

// Grab the data with d3
d3.json(geoJSONdata, function(response) {

  // Create a new marker cluster group
  var markers = L.markerClusterGroup({
    animateAddingMarkers: true
  });
  var features = response.features;
  // Loop through data
  for (var i = 0; i < features.length; i++) {
    var coords = features[i].geometry;
    // Set the data location property to a variable


    // Check for location property
    if (coords) {

      // Add a new marker to the cluster group and bind a pop-up
      markers.addLayer(L.marker([coords.coordinates[1], coords.coordinates[0]])
        .bindPopup());
    }

  }

  // Add our marker cluster layer to the map
  myMap.addLayer(markers);

});
