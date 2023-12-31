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
|           PUMP CAROUSEL                       |
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
|           PUFFER CAROUSEL                    |
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
/* 
           // breakpoint from 2 up
            859: {
               items: 1,
           },

            // breakpoint from 3 up
            1254: {
                items: 1,
            } */
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
|    FUNCTION TO HIDE/SHOW PASSWORD             |
-----------------------------------------------*/ 
  
    function showPassword() {
      var p = document.getElementById('password_for_login');
      if (p.type === 'password') {
        p.type = 'text';
      } 
      else {
        p.type = 'password';
      }
    }
  


/*------------------------------------------------------------------
|    FUNCTION TO CLOSE OFFCANVAS WHEN BUTTON IS CLICKED             |
-------------------------------------------------------------------*/ 
    jQuery("#mySidenav, .sidenav a").click(function(){
        console.log($(this).attr('href'));
        jQuery('.sidenav').offcanvas('hide');
    })





/*------------------------------------------------------------------
|    SCRIPT TO GET THE TIME AT REAL TIME CONSTANTLY                 |
-------------------------------------------------------------------*/ 
setInterval(function() {
    var date = new Date();
    $('#clock').html(
        (date.getHours()<10?'0':'') + date.getHours() + ":" +
        (date.getMinutes()<10?'0':'') + date.getMinutes() + ":" +
        (date.getSeconds()<10?'0':'') + date.getSeconds()
        );
    
}, 500);

/*------------------------------------------------------------------
|    SCRIPT TO UPDATE THE PAGE ALWAYS AT 00:00                      |
-------------------------------------------------------------------*/ 
function autoRefreshPage(hours, minutes, seconds) {
  var now = new Date(); then = new Date();
  then.setHours(hours, minutes, seconds, 0);
  if (then.getTime() < now.getTime()) {
    then.setDate(now.getDate() + 1);
  } 
  var timeout = (then.getTime() - now.getTime());
  setTimeout(function() { 
    window.location.reload(true); 
  }, timeout);
}
autoRefreshPage(0, 0, 0);




