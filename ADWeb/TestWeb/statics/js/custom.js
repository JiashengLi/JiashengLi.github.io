$(document).ready(function(){
    $("#toXBIO").click(function(){
        window.location.href="xbio-demo";
        $.post("/xbio-demo",{
            fakedata:fakedata,
            fakecount:fakecount,
       })
       
    })
})

function toIndex(){
    window.location.href="index";
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

//伪造的json对象。
//count：整数，数据库中的分子式总数。data：数组，包含每个分子式对象。
var fakeObject = {
    count:122,
    data:[
        {'name':'分子名1','casNo':1,},{'name':'分子名1','casNo':2},{'name':'分子名1','casNo':3},
        {'name':'分子名1','casNo':4},{'name':'分子名1','casNo':45},{'name':'分子名1','casNo':6},
        {'name':'分子名1','casNo':7},{'name':'分子名1','casNo':8},{'name':'分子名1','casNo':9}
    ],
}
var fakecount = fakeObject["count"].toString()
var fakedata = fakeObject["data"].toString()