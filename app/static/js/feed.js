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
	/*
	$("#search").change(function(){
		getUsersBySearch();
	});
	*/
	$("#uploadedImage").change(function(){
		var reader = new FileReader();
		reader.readAsDataURL($("#uploadedImage")[0].files[0]);

		reader.onload = function(event){
			$("#uploadedPreview").attr('src', event.target.result);
		};
	});

});

function addMarker(lat, lon, content, title, postDate){
	var newMarker = createMarker(lat, lon);
	var date = moment(postDate).fromNow();
	var customPopup = '<div class="ui card"> <div class="content">'+
		'<div class="meta"> <span class="right floated time">'+date+'</span> </div>'+
    '<div class="header">'+title+'</div>'+
    '<div class="description">'+
      '<p>'+content+'</p></div></div>'+
  '<div class="extra content">'+
    '<span class="left floated like">'+
      '<i class="like icon"></i>Like</span>'+
    '<span class="right floated star">'+
      '<i class="star icon"></i>Favorite'+
    '</span></div></div>';

	newMarker.addTo(map);
	newMarker.bindPopup(customPopup);
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
				var data = callback.posts;
				console.log(data);



	    	$.forEach(data, function(key, kindness){
	    		var lat = kindness.latitude;
					var title = kindness.title;
					var datePost = kindness.postDate;
	    		var lon = kindness.longitude;
	    		var body = kindness.body;
	    		addMarker(lat, lon, body, title, datePost);
	    	});

	    },
	    error: function(){
	    	$(this).html("error!");
	    }
	});
}
/*
function getUsersBySearch(){

	//$('#form-search-user').submit(function (e){
		let data = {};

		var url = "../users/search";
		data['search'] = $('#search').val();

		console.log(data);
		$.ajax({
				type: "POST",
				url: url,
				dataType: 'json',
	      contentType: 'application/json; charset=utf-8',
	      data: JSON.stringify(data),
				success: function(response){
					console.log(response);
					let obj = JSON.parse(response);

	        console.log(obj);
	      },
		});

		//e.preventDefault();
	//});
}
*/
function createKindness(){

	$('#form-new-post').submit(function (e) {

		$("#latitude").val(latitude);
		$("#longitude").val(longitude);

		var formData = new FormData($(this)[0]);
		var url = "../feed/";
		console.log(formData);
	    $.ajax({
	        type: "POST",
	        url: url,
	        data: formData,
					async: true,
	        success: function (data) {
	            console.log(data)
	            $('#respostas').html(data.message);
	            getKindness();
	        },
					cache: false,
          contentType: false,
          processData: false
	    });
	    e.preventDefault();
	});
}
