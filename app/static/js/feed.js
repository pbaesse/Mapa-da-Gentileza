var initialCoord = [-22.91, -43.20];
var initialZoom = 13;

// coordenadas do local que o usuário selecionou para o post.
var latitude;
var longitude;

// inicializa o mapa.
var map = L.map('map').setView(initialCoord, initialZoom);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	attribution: '&copy; Contribuidores do <a href="http://osm.org/copyright">OpenStreetMap</a>'
}).addTo(map);


// responsável por pegar 
function mapClick(local){
	latitude = parseFloat(local.latlng.lat.toString());
	longitude = parseFloat(local.latlng.lng.toString());
}

map.on('click', mapClick);


$(document).ready(function(){
	getKindness();
	createKindness();
	
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
		if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", "{{ form.csrf_token._value() }}")
			}
		}
	});

	$("#uploadedImage").change(function(){
		var reader = new FileReader();
		reader.readAsDataURL($("#uploadedImage")[0].files[0]);

		reader.onload = function(event){
			$("#uploadedPreview").attr('src', event.target.result);
		};
	});
	
});

function addMarker(lat, lon, content){
	var newMarker = createMarker(lat, lon);

	newMarker.addTo(map);
	newMarker.bindPopup(content);
	newMarker.openPopup();

  	return newMarker;
}

function createMarker(lat, lon){
	var coord = [lat, lon];
	var newMarker;

	var iconProp = {
		iconUrl: "../static/img/marker-icon.png",
		iconSize: [44, 59],
		iconAnchor: [22, 59],
	    popupAnchor: [0, -50]
	};

	var iconM = L.icon(iconProp);
	newMarker = L.marker(coord, {icon: iconM});

	return newMarker;
}

function getKindness(){

	$.ajax({
	    type: 'GET',
	    url: "../feed/list_kindness",
	    dataType: 'json',
	    contentType: 'application/json; charset=utf-8',
	    success: function(callback){
	    	console.log(callback);

	    	callback.forEach(function(kindness){
	    		var lat = kindness.latitude;
	    		var lon = kindness.longitude;
	    		var body = kindness.body;
	    		addMarker(lat, lon, body);
	    	});

	    },
	    error: function(){
	    	$(this).html("error!");
	    }    
	});
}

function createKindness(){

	$('#form-new-post').submit(function (e) {
		
		var data = {};
		var Form = this;
		$.each(this.elements, function(i, v) {
			var input = $(v);
		    data[input.attr("name")] = input.val();
			delete data["undefined"];

		});
		
		data["latitude"] = latitude;
		data["longitude"] = longitude;

	    var url = "../feed/";

	    $.ajax({
	        type: "POST",
	        url: url,
	        dataType: 'json',
	        contentType: 'application/json; charset=utf-8',
	        data: JSON.stringify(data), 
	        success: function (data) {
	            console.log(data) 
	            $('#respostas').html("salvo");
	            getKindness();
	        }
	    });
	    e.preventDefault();
	});
}