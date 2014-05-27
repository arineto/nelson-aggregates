var drawing = false;

function start_drawing(){
  polygon = new_polygon(map, new google.maps.MVCArray(), document.getElementById("color").value, document.getElementById("title").value, true, true);
  drawing = true;
  document.getElementById("color").disabled = true;
  document.getElementById("start_drawing").disabled = true;
  document.getElementById("title").disabled = true;
  document.getElementById("end_drawing").disabled = false;
}

function end_drawing(){
  // polygon.setDraggable(false);
  // polygon.setEditable(false);
  // drawing = false;
  // document.getElementById("color").disabled = false;
  // document.getElementById("start_drawing").disabled = false;
  // document.getElementById("info_text").disabled = false;
  // document.getElementById("end_drawing").disabled = true;
  save_map();
}

function get_path_points(array){
  var path_points = "";
  for (i=0; i<array.length; i++){
    path_points+=array[i].toString()+", ";
  }
  return path_points;
}

function save_map(){
  document.new_map_form.points.value = get_path_points(polygon.getPath().getArray());
  document.getElementById("id_color").value = document.getElementById("color").value;
  document.new_map_form.title.value = document.getElementById("title").value;
  document.getElementById("title").value="";
  document.new_map_form.submit();
}