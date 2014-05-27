var marker;
var geocoder;

function codeAddress() {
  if(marker){
    marker.setMap(null);
  }
  var address = document.getElementById('searchTextField').value;
  geocoder.geocode( { 'address': address}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      map.setCenter(results[0].geometry.location);
      marker = new google.maps.Marker({
          map: map,
          position: results[0].geometry.location
      });
    } else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
  });
}

$( document ).ready(function() {
  $( "#searchTextField" ).keypress(function(event) {
    if ( event.which == 13 ) {
      codeAddress();
    }
  });
});