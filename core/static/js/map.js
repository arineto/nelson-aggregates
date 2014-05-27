function init_map(map){
  var mapOptions = {
    center: new google.maps.LatLng(43.115050, -79.488938),
    zoom: 11
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