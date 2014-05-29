var info_window = null;
var last_polygon = null;

function new_polygon(map, path, color, content, editable, draggable){

  var polygonOptions = {
    path: path, 
    strokeColor: color,
    strokeWeight: 2,
    fillColor: color, 
    fillOpacity: 0.1,
    editable: editable, 
    draggable: draggable
  };
  var polygon = new google.maps.Polygon( polygonOptions );
  polygon.setMap(map);
  
  google.maps.event.addListener(polygon, 'click', function(e){
    if (info_window){
      info_window.setMap(null);
    }
    info_window = new google.maps.InfoWindow();
    info_window.setContent(content);
    info_window.setPosition(e.latLng);
    info_window.open(map);

    mark_polygon(polygon);
  });
  return polygon;
}

function mark_polygon(polygon){
    if(last_polygon){
      last_polygon.setOptions({fillOpacity:0.1});
    }
    last_polygon = polygon;
    polygon.setOptions({fillOpacity:0.3});
}

function create_marker(name, icon, latitude, longitude, content){
  var quarry_marker = null;
 
  quarry_marker = new google.maps.Marker({
    position: new google.maps.LatLng(parseFloat(latitude), parseFloat(longitude)),
    map: map,
    title: name,
    icon: icon
  });

  google.maps.event.addListener(quarry_marker, 'click', function () {
    quarry_window = new google.maps.InfoWindow({
      content: content
    })
    quarry_window.open(map, quarry_marker);
  });
} 