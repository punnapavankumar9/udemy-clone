var menu_btn = document.querySelector(".hamburger-svg");
var menu_active = false;
// var search_btn = document.querySelector(".search-svg");
// var search_active = false;

menu_btn.addEventListener("click", () => {
  if(!menu_active){
    menu_btn.classList.remove("in-active")
    menu_btn.classList.add("active")
    menu_active = true
  }else{
    menu_btn.classList.remove("active")
    menu_btn.classList.add("in-active")
    menu_active = false
  }
});

var swiper = new Swiper('.swiper-container', {
  spaceBetween: 2,
  centeredSlides: true,
  loop: true,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});

$(document).ready(function(){
  var x = $('#img').css('height');
  console.log(x)
  $('.img1').css('max-height', x);
  var sc1Width = $( window ).width();
  
  var swiper1 = new Swiper('.swiper-container-1', {
    slidesPerView: 1.5,
    spaceBetween: 30,
    slidesPerGroup: 1,
    navigation: {
      nextEl: '.swiper-button-next-1',
      prevEl: '.swiper-button-prev-1',
    },
  });

});


var acc = document.getElementsByClassName("accordion");
        var i;

        for (i = 0; i < acc.length; i++) {
            acc[i].addEventListener("click", function () {
                this.classList.toggle("active");
                var panel = this.nextElementSibling;
                if (panel.style.maxHeight) {
                    panel.style.maxHeight = null;
                } else {
                    panel.style.maxHeight = panel.scrollHeight + "px";
                }
            });
        }
