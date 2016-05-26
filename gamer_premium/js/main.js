	

	//Main instructions javascript and jquery


		// galería de fotos y videos 

		$(document).ready(function() {

			//Modal video

			$('.venobox').venobox({
				framewidth: '640px', 
				frameheight: '480px',
			}); 

			//Modal galería imágenes
			$('.venobox_gallery').venobox({
				framewidth: '700px', 
				frameheight: '423px',
			});
			
			//toogle function open menu
			$('#list-menu').hide();

			$('.expander').on('click', function() {
				$('#list-menu').toggle('slow');
			});
		});
		

		// Validación aplicación de libraría fullpage para resoluciones mayores a 768px (Tabletas) 

		// Se realiza esta validación por Legibilidad de información en Phones 
		
		

		if (screen && screen.width > 768) {

			document.write('<script type="text/javascript" src="lib/bower_components/fullpage.js/dist/jquery.fullpage.js"><\/script>');

			$(document).ready(function() {

				var $AnimatedSecond = $('.s2 .mett__cont-base-flex .mett__animated');
				var $AnimatedThird = $('.s3 .mett__cont-base-flex .mett__animated');

				 $('#fullpage').fullpage({
					menu: '#mainMenu',
					anchors: ['firstPage', 'secondPage', 'thirdPage', 'fourthPage', 'fifthPage', 'sixthPage'],
					navigationTooltips: ['Generalidades', 'Descripción', 'Especificaciones', 'Cambios y devoluciones'],
					navigation: true,
					onLeave: function(index, nextIndex, direction){
							
					// first animation
					if( index == 1 && nextIndex == 2 ) { 

						$AnimatedSecond.addClass('animated fadeInUp fadeIn');
						$AnimatedSecond.eq(0).css('animation-delay', '.1s');
						$AnimatedSecond.eq(1).css('animation-delay', '.2s');
						$AnimatedSecond.eq(2).css('animation-delay', '.3s');
						$AnimatedSecond.eq(3).css('animation-delay', '.4s');
						$AnimatedSecond.eq(4).css('animation-delay', '.5s');
						$AnimatedSecond.eq(5).css('animation-delay', '.6s');
						// $isAnimatedSecondSingle.addClass('animated rollIn').css('animation-delay', '1.7s');


						} else if ( ( index == 1 || index == 2) && nextIndex == 3 ) {
							$AnimatedThird.addClass('animated fadeInRight fadeIn');
							
						}
					}
				});
			});
		}
		