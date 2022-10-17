function getwidth(){
    if(innerWidth >= 980){
        $(".header_section").css("position","fixed");
        $(".container-fluid").css("position","fixed");
        console.log("true");
        return true;
    }else{
        console.log("false");

        return false;
    }
 }
 getwidth();
// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


/** google_map js **/

function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

