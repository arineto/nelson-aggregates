function init_map(map){
  var mapOptions = {
    center: new google.maps.LatLng(43.276441, -79.916135),
    zoom: 10
  };
  map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

  google.maps.event.addListener(map, 'click', function (e) {
    if (drawing==true){
      var currentPath = polygon.getPath();
      currentPath.push(e.latLng);
    }
  });
  return map;
}