const body = document.querySelector("body"),
      sidebar = body.querySelector(".sidebar"),
      toggle = body.querySelector(".toggle"),
      searchButton = body.querySelector(".search-button"),
      modeSwitch = body.querySelector(".toggle-switch"),
      modeText = body.querySelector(".mode-text");
      searchButton.addEventListener("click", () =>{
          sidebar.classList.toggle("close");
      });
      toggle.addEventListener("click", () =>{
          sidebar.classList.toggle("close");
      });
      modeSwitch.addEventListener("click", () =>{
        body.classList.toggle("dark");

        if(body.classList.contains("dark")){
            modeText.innerText = "Light Mode"
        }else{
            modeText.innerText = "Dark Mode"
        }
      });




function show_ortom(){
    document.getElementById("ortom-overlay").style.display = "block"
}
function hide_ortom(){
    document.getElementById("ortom-overlay").style.display = "none"
}

function show_aisyiyah(){
    document.getElementById("aisyiyah").style.display = "block"
}
function hide_aisyiyah(){
    document.getElementById("aisyiyah").style.display = "none"
}


function show(){
    document.getElementById("overlay").style.display = "block"
}
function hide(){
    document.getElementById("overlay").style.display = "none"
}
function show_hadist(){
    document.getElementById("overlay2").style.display = "block"
}
function hide_hadist(){
    document.getElementById("overlay2").style.display = "none"
}
function show_about(){
    document.getElementById("overlay3").style.display = "block"
}
function hide_about(){
    document.getElementById("overlay3").style.display = "none"
}
function show_news(){
    document.getElementById("overlay4").style.display = "block"
}
function hide_news(){
    document.getElementById("overlay4").style.display = "none"
}

const observer = new IntersectionObserver((entries)=> {
    entries.forEach((entry) => {
        console.log(entry)
        if(entry.isIntersecting){
            entry.target.classList.add('show')
        }else{
            entry.target.classList.remove('show')
        }
    });
});


const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));
