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
   
         const pumpSlider = $('#pumpSlider');
     
         pumpSlider.owlCarousel({
             loop: true,
             dots: false,
             margin: 1,
             smartSpeed: 500,
             responsive: {
                 // breakpoint from 0 up
                 0: {
                     items: 1,
                 },

      /*           // breakpoint from 2 up
                 859: {
                    items: 1,
                },
    
                 // breakpoint from 3 up
                 1254: {
                     items: 1,
                 } */
             }
     
         });
     
         $('#pumpSliderLeft').click(function() {
             console.log('Left');
             pumpSlider.trigger('prev.owl.carousel');
         });
     
         $('#pumpSliderRight').click(function() {
             console.log('Right');
             pumpSlider.trigger('next.owl.carousel');
         });
     
     });


/*----------------------------------------------
|           INDEX PUMP SLIDER                   |
-----------------------------------------------*/
      
$(document).ready(function() {
   
      const pufferSlider = $('#pufferSlider');
  
      pufferSlider.owlCarousel({
          loop: true,
          dots: false,
          margin: 1,
          smartSpeed: 500,
          responsive: {
            // breakpoint from 0 up
            0: {
                items: 1,
            },

           // breakpoint from 2 up
            859: {
               items: 1,
           },

            // breakpoint from 3 up
            1254: {
                items: 1,
            }
          }
  
      });
  
      $('#pufferSliderLeft').click(function() {
          console.log('Left');
          pufferSlider.trigger('prev.owl.carousel');
      });
  
      $('#pufferSliderRight').click(function() {
          console.log('Right');
          pufferSlider.trigger('next.owl.carousel');
      });
  
  });






 /*----------------------------------------------
|           TYPED JS - NAVBAR                   |
-----------------------------------------------*/ 
  var typed = new Typed('#element', {
     strings: [
     'LES MEILLEURS PRIX DE TOUTE LA ',
     'NOS SERVICES DE QUALITÉ ',
     'LES POMPES À CHALEUR POUR LES ',
     'ON EST FIERS DE NOTRE',
     ],
     typeSpeed: 8,
     backSpeed: 15,
     backDelay: 3000,
     loop: true
  });
