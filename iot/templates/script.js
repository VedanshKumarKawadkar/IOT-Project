function toggle(e){
    var element=e.target
    var on=element.classList.contains("on")
    if(on){
        element.classList.remove("on")
    }
    else{
        element.classList.add("on")
    }
}

[...document.querySelectorAll('.toggle')].forEach(elem=>elem.addEventListener("click",toggle));