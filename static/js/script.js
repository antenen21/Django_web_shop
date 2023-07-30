/*----------------------------------------------
|           Side Navigation / Offcanvas         |
-----------------------------------------------*/
      function openNav() {
      document.getElementById("mySidenav").style.width = "250px";
      }
      
      function closeNav() {
      document.getElementById("mySidenav").style.width = "0";
      }







/*----------------------------------------------
|           TEST CAROUSEL         |
-----------------------------------------------*/
      
      $(document).ready(function() {
   
         const shopSlider = $('#shopSlider');
     
         shopSlider.owlCarousel({
             loop: true,
             dots: false,
             margin: 2,
             smartSpeed: 500,
             responsive: {
                 // breakpoint from 0 up
                 0: {
                     items: 1,
                 },
                 // breakpoint from 3 up
                 1254: {
                     items: 3,
                 }
             }
     
         });
     
         $('#shopSliderLeft').click(function() {
             console.log('Left');
             shopSlider.trigger('prev.owl.carousel');
         });
     
         $('#shopSliderRight').click(function() {
             console.log('Right');
             shopSlider.trigger('next.owl.carousel');
         });
     
     });


/*----------------------------------------------
|           INDEX PUMP SLIDER                   |
-----------------------------------------------*/
      
$(document).ready(function() {
   
      const shopSlider = $('#main_slider');
  
      shopSlider.owlCarousel({
          loop: true,
          dots: false,
          margin: 2,
          smartSpeed: 500,
          responsive: {
              // breakpoint from 0 up
              0: {
                  items: 1,
              },
              // breakpoint from 3 up
              1254: {
                  items: 3,
              }
          }
  
      });
  
      $('#pumpLeft').click(function() {
          console.log('Left');
          shopSlider.trigger('prev.owl.carousel');
      });
  
      $('#pumpRight').click(function() {
          console.log('Right');
          shopSlider.trigger('next.owl.carousel');
      });
  
  });