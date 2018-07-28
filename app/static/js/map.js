var initialCoord = [-22.91, -43.20];
var initialZoom = 13;

var markerCoord = [-22.903719, -43.1760605];
var markerMsg = "Olá mundo, <br> Olá LeafletJs";

// inicializa o mapa.
var map = L.map('map').setView(initialCoord, initialZoom);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	attribution: '&copy; Contribuidores do <a href="http://osm.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var iconProp = {
	iconUrl: "../static/img/marker-icon.png"
,   iconSize: [44, 59]
, 	iconAnchor: [22, 59]
,   popupAnchor: [0, -50]
};

var iconM = L.icon(iconProp);

L.marker(markerCoord, {icon: iconM})
	.addTo(map)
	.bindPopup(markerMsg)
	.openPopup();


// teste para pegar latitude e longitude de lugar clicado no mapa.
function mapClick(local){
	alert(local.latlng.lat.toString()+" :: "+local.latlng.lng.toString());
}

map.on('click', mapClick);