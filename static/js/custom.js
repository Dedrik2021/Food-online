let autocomplete;
const address = document.getElementById('id_address')
const geocoder = new google.maps.Geocoder()

function initAutoComplete(){
autocomplete = new google.maps.places.Autocomplete(
    address,
    {
        types: ['geocode', 'establishment'],
        //default in this app is "IN" - add your country code
        componentRestrictions: {'country': ['in', 'us', 'uk', 'ua', 'cz']},
    })
// function to specify what should happen when the prediction is clicked
autocomplete.addListener('place_changed', onPlaceChanged);
}

function onPlaceChanged (){
    const place = autocomplete.getPlace();

    // User did not select the prediction. Reset the input field or alert()
    if (!place.geometry){
        address.placeholder = "Start typing...";
    }
    else{
        console.log('place name=>', place.name)
    }
    // get the address components and assign them to the fields

    
    geocoder.geocode({'address': address.value}, function(results, status) {
        if (status === google.maps.GeocoderStatus.OK) {
            const latitude = results[0].geometry.location.lat()
            const longitude = results[0].geometry.location.lng()

            $('#id_latitude').val(latitude)
            $('#id_longitude').val(longitude)

            $('#id_address').val(address.value)
        }
    })

    //Loop through the address components and assign other address data

    for (let i = 0; i < place.address_components.length; i++) {
        for (let j = 0; j < place.address_components[i].types.length; j++) {
            //get country
            if (place.address_components[i].types[j] === 'country') {
                $('#id_country').val(place.address_components[i].long_name)
            }

            //get state
            if (place.address_components[i].types[j] === 'administrative_area_level_1') {
                $('#id_state').val(place.address_components[i].long_name)
            }

            //get city
            if (place.address_components[i].types[j] === 'locality') {
                $('#id_city').val(place.address_components[i].long_name)
            }

            //get pincode
            if (place.address_components[i].types[j] === 'postal_code') {
                $('#id_pin_code').val(place.address_components[i].long_name)
            } else {
                $('#id_pin_code').val('')
            }
        }
    }
}