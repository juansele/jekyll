	

	//Main instructions javascript and jquery


		// galería de fotos y videos 

		$(document).ready(function() {

			//Modal video

			$('.venobox').venobox({

				framewidth: '100%', 

				frameheight: '400px',

			}); 

			//Modal galería imágenes
			$('.venobox_gallery').venobox({
				
				framewidth: '100%',
				 
				frameheight: '50%',
				
			});
			
		});
		

		// Validación aplicación de libraría fullpage para resoluciones mayores a 768px (Tabletas) 

		// Se realiza esta validación por Legibilidad de información en Phones 
		
		 

		if (screen && screen.width > 768) {

			document.write('<link rel="stylesheet" type="text/css" href="lib/bower_components/fullpage.js/dist/jquery.fullpage.min.css">')
			 
			document.write('<script type="text/javascript" src="lib/bower_components/fullpage.js/dist/jquery.fullpage.js"><\/script>');

			 $(document).ready(function() {

			 	var $AnimatedSecond = $('.s2 .mett__cont-base-flex .mett__animated');

			 	var $AnimatedThird = $('.s3 .mett__cont-base-flex .mett__animated');

			 	var $AnimatedFourth = $('.s4 .mett__cont-base-flex .mett__animated');

			 	var $AnimatedFifth = $('.s5 .mett__cont-base-flex .mett__animated');

				var $AnimatedSixth = $('.s6 .mett__cont-base-flex .mett__animated');

				var $AnimatedSeventh = $('.s7 .mett__cont-base-flex .mett__animated');

				var $AnimatedEight = $('.s8 .mett__cont-base-flex .mett__animated');

				var $AnimatedNineht = $('.s9 .mett__cont-base-flex .mett__animated');

				var $AnimatedTenth = $('.s10 .mett__cont-base-flex .mett__animated');

				var $AnimatedEleventh = $('.s11 .mett__cont-base-flex .mett__animated');


			 	 $('#fullpage').fullpage({

					menu: '#mainMenu',

					anchors: ['firstPage', 'secondPage', 'thirdPage', 'fourthPage', 'fifthPage', 'sixthPage', 'seventhPage', 'eightPage', 'ninePage', 'tenthPage', 'eleventhPage'],

					navigationTooltips: ['Generalidades', 'Descripción', 'Especificaciones', 'Cambios y devoluciones'],

					navigation: true,


					onLeave: function(index, nextIndex, direction){

							

					if( index == 1 && nextIndex == 2 ) { 

						$AnimatedSecond.addClass('animated fadeInUp fadeIn');
			 			// $isAnimatedSecondSingle.addClass('animated rollIn').css('animation-delay', '1.7s');


						} else if ( ( index == 1 || index == 2) && nextIndex == 3 ) {
							
							$AnimatedThird.eq(0).addClass('animated fadeInLeft fadeIn');

							$AnimatedThird.eq(1).addClass('animated fadeInRight fadeIn');

			 			} else if ( ( index == 1 || index == 2 || index == 3) && nextIndex == 4 ) {

							$AnimatedFourth.eq(0).addClass('animated fadeInRight fadeIn');

							$AnimatedFourth.eq(1).addClass('animated fadeInRight fadeIn');

						} else if ( ( index == 1 || index == 2 || index == 3 || index == 4) && nextIndex == 5 ) {

							$AnimatedFifth.eq(0).addClass('animated fadeInUp fadeIn');

							$AnimatedFifth.eq(1).addClass('animated fadeInLeft fadeIn');

			 				$AnimatedFifth.eq(1).css('animation-delay', '.3s');

							$AnimatedFifth.eq(2).addClass('animated fadeInRight fadeIn');

							$AnimatedFifth.eq(2).css('animation-delay', '.6s');

						} else if ( ( index == 1 || index == 2 || index == 3 || index == 4 || index == 5) && nextIndex == 6 ) {

			 				$AnimatedSixth.addClass('animated fadeInLeft fadeIn');

			 			} else if ( ( index == 1 || index == 2 || index == 3 || index == 4 || index == 5 || index == 6 ) && nextIndex == 7 ) {

			 				$AnimatedSeventh.addClass('animated fadeInUp fadeIn');

			 			} else if ( ( index == 1 || index == 2 || index == 3 || index == 4 || index == 5 || index == 6 || index == 7 ) && nextIndex == 8 ) {
			 			
			 				$AnimatedEight.addClass('animated fadeInRight fadeIn');

			 			} else if ( ( index == 1 || index == 2 || index == 3 || index == 4 || index == 5 || index == 6 || index == 7  || index == 8) && nextIndex == 9 ) {
			 				
			 				$AnimatedNineht.addClass('animated fadeInLeft fadeIn');
			 			
			 			} else if ( ( index == 1 || index == 2 || index == 3 || index == 4 || index == 5 || index == 6 || index == 7  || index == 8 || index == 9) && nextIndex == 10 ) {
			 				
			 				$AnimatedTenth.addClass('animated fadeInRight fadeIn');

			 			} else if ( ( index == 1 || index == 2 || index == 3 || index == 4 || index == 5 || index == 6 || index == 7  || index == 8 || index == 9 || index == 10) && nextIndex == 11 ) {
			 				
			 				$AnimatedEleventh.addClass('animated fadeInLeft fadeIn');
			 			}


			 		}
				});
			  });
		} else if (screen && screen.width < 768){

			document.write('<link rel="stylesheet" type="text/css" href="css/style-nofullpage.css">');

		}
		