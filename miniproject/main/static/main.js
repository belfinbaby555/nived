function searchplace(){
   let place= document.getElementById("place").value;
   let date= document.getElementById("date").value;
   let people= document.getElementById("people").value;
   let type= document.getElementById("type").value;
   let star= document.getElementById("season").value;

   console.log(place, date, type, people, star);

   fetch("http://127.0.0.1:8000/search/None/None/None/None/5/")
   .then((res)=>(res.json()))
   .then((json)=>{
    
    var search=json.data;
    console.log(search)

    for(let i=0;i<=search.length-1;i++){
        document.getElementById("cards").innerHTML+="<div class='card'><h3><img src='/static/images/drop.png'><b>"+search[i].place+"</b></h3><span><h2>Season<p>--</p>: <b>"+search[i].season+"</b></h2><h2>Type<p>..---</p>: <b>"+search[i].type+"</b></h2><h2>Category: <b>"+search[i].category+"</b></h2><div id='stars' class='stars'><h2>Rating<p></p>:</h2></div><button onclick=''>Google Map</button></span></div>"
    }


    
   })
}