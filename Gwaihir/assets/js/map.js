
let map;

function initMap() {
    map = new google.maps.Map(
        document.getElementById('map'),
        {center: new google.maps.LatLng(-33.91722, 151.23064), zoom: 16});

    let iconBase =
        'https://developers.google.com/maps/documentation/javascript/examples/full/images/';

    let icons = {
        parking: {
        icon: iconBase + 'parking_lot_maps.png'
        },
        library: {
        icon: iconBase + 'library_maps.png'
        },
        info: {
        icon: iconBase + 'info-i_maps.png'
        }
    };

    let features = [
        {
        position: new google.maps.LatLng(-33.91721, 151.22630),
        type: 'info'
        }, {
        position: new google.maps.LatLng(-33.91662347903106, 151.22879464019775),
        type: 'parking'
        }, {
        position: new google.maps.LatLng(-33.91727341958453, 151.23348314155578),
        type: 'library'
        }
    ];

    // Create markers.
    for (let i = 0; i < features.length; i++) {
        let marker = new google.maps.Marker({
        position: features[i].position,
        //icon: icons[features[i].type].icon,
        map: map
        });
    };
}