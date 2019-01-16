// Creating map object
var map = L.map("map", {
  center: [38.9072, -77.0369],
  zoom: 11
});

// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(map);

// Query URL
var geoJSONdata = "https://raw.githubusercontent.com/dbikindu/Project_MovingViolations/master/map/mv_2018.geojson"


// Grabbing our GeoJSON data..
d3.json(geoJSONdata, function(response) {

  console.log(response);

  var features = response.features;

  var heatArray = [];

  for (var i = 0; i < features.length; i++) {
    var coords = features[i].geometry;

    if (coords) {
      heatArray.push([coords.coordinates[1], coords.coordinates[0]]);
    }
  }

  var heat = L.heatLayer(heatArray, {
    radius: 11,
    blur: 25,
    maxZoom: 17,
  }).addTo(map);

});
