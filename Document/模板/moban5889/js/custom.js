function toIndex(){
    window.location.href="index.html";
}
function toXBIO(){
    window.location.href="xbio-demo.html";
}
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