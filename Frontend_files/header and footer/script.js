var dropdown1 = document.getElementById('dropdown1');
var down1 = document.getElementById('down1');
var dropdown2 = document.getElementById('dropdown2');
var down2 = document.getElementById('down2');
var dropdown3 = document.getElementById('dropdown3');
var down3 = document.getElementById('down3');
var  menu_icon = document.getElementById("menu-icon");
var sign_up = document.getElementById('sign-up');
var nav = document.getElementById('nav');


window.onclick = function(event){
    if(event.target.matches("#down1")){
        dropdown1.style.display = "block";
        dropdown2.style.display = "none";
        dropdown3.style.display = "none";
    }
    else if(event.target.matches("#down2")){
        dropdown1.style.display = "none";
        dropdown2.style.display = "block";
        dropdown3.style.display = "none";
    }
    else if(event.target.matches("#down3")){
        dropdown1.style.display = "none";
        dropdown2.style.display = "none";
        dropdown3.style.display = "block";
    }
    else if(event.target.matches("#menu-icon")){
        menu_icon.style.border = "2px solid #807f7f";
        sign_up.style.display = "block";
        nav.style.display = "block";
    }
    else if(event.target.matches("#menu-icon") && menu_icon.style.border == "2px solid #807f7f"){
        sign_up.style.display = "none";
        nav.style.display = "none";
        dropdown1.style.display = "none";
        dropdown2.style.display = "none";
        dropdown3.style.display = "none";
    }
    // else{
    //     menu_icon.style.border = "none";
    //     sign_up.style.display = "none";
    //     nav.style.display = "none";
    //     dropdown1.style.display = "none";
    //     dropdown2.style.display = "none";
    //     dropdown3.style.display = "none";
    // }
}
