#!/usr/bin/python
#coding: utf-8

from string import Template

templates = {}

templates['inicio'] = '''
	<!DOCTYPE html>
	<html LANG="ES">
		<head>
			<meta charset="UTF-8">
			<title>${titulo}</title>
			<link rel="shortcut icon" type="image/x-icon" href="../favicon.ico">
			<meta name="viewport" content="width=device-width, height=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
		</head>
		<body>
		
		<style type="text/css">

 
	html{background: url('../img/OTROS/lenovo_pattern-02.png') no-repeat center center fixed; -webkit-background-size: cover; -moz-background-size: cover; -o-background-size: cover; background-size: cover; } @font-face {font-family:'HelveticaNeueLT-Light'; src: url('../fonts/HelveticaNeueLT-Light_gdi.eot'); src: url('../fonts/HelveticaNeueLT-Light_gdi.eot?#iefix') format('embedded-opentype'), url('../fonts/HelveticaNeueLT-Light_gdi.woff') format('woff'), url('../fonts/HelveticaNeueLT-Light_gdi.ttf') format('truetype'), url('../fonts/HelveticaNeueLT-Light_gdi.svg#HelveticaNeueLT-Light') format('svg'); font-weight: 3; font-style: normal; font-stretch: normal; unicode-range: U+0-10FFFF; } @font-face {font-family:'HelveticaNeue-Thin'; src: url('../fonts/HelveticaNeue-Thin_gdi.eot'); src: url('../fonts/HelveticaNeue-Thin_gdi.eot?#iefix') format('embedded-opentype'), url('../fonts/HelveticaNeue-Thin_gdi.woff') format('woff'), url('../fonts/HelveticaNeue-Thin_gdi.ttf') format('truetype'), url('../fonts/HelveticaNeue-Thin_gdi.svg#HelveticaNeue-Thin') format('svg'); font-weight: 100; font-style: normal; font-stretch: normal; unicode-range: U+0020-2212; } /* Archivo base sistema de grids flex */ .container-main{min-width: 304px !important; } .layout, .layout-column, .layout-row {box-sizing: border-box; display: -webkit-flex; display: -ms-flexbox; display: flex; flex-wrap: wrap; -webkit-display:flex; } .layout-row{flex-direction: row; -webkit-flex-direction: row; -ms-direction: row; } .layout-column{flex-direction: column; -webkit-flex-direction: column; -ms-direction: column; } /* JUSTIFY ELEMENTS */ .justify-center{justify-content:center; -webkit-justify-content:center; } .justify-start{justify-content:flex-start; -webkit-justify-content:flex-start; } .justify-end{justify-content:flex-end; -webkit-justify-content:flex-end; } .justify-space-between{justify-content:space-between; -webkit-justify-content:space-between; } .justify-space-around{justify-content:space-around; -webkit-justify-content:space-around; } /* ALINGMENT ELEMENTS */ .align-start{align-items: flex-start; -webkit-align-items: flex-start; } .align-end{align-items:flex-end; -webkit-align-items:flex-end; } .align-center{align-items:center; -webkit-align-items:center; } .align-stretch{align-items:stretch; -webkit-align-items:stretch; } .align-baseline{align-items:baseline; -webkit-align-items:baseline; } /* ALINGMENT ALL CONTENT */ .align-all-center{align-content:center; -webkit-align-content:center; } .align-all-start{align-content:flex-start; -webkit-align-content:flex-start; } .align-all-end{align-content:flex-end; -webkit-align-content:flex-end; } .align-all-space-between{align-content:space-between; -webkit-align-content:space-between; } .align-all-space-around{align-content:space-around; -webkit-align-content:space-around; } /**/ .flex{-webkit-flex: 1 1 100%; -ms-flex: 1 1 100%; flex: 1 1 1; max-width: 100%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-5{-webkit-flex: 1 1 5%; -ms-flex: 1 1 5%; flex: 1 1 5%; max-width: 5%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-10{-webkit-flex: 1 1 10%; -ms-flex: 1 1 10%; flex: 1 1 10%; max-width: 10%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-15{-webkit-flex: 1 1 15%; -ms-flex: 1 1 15%; flex: 1 1 15%; max-width: 15%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-20{-webkit-flex: 1 1 20%; -ms-flex: 1 1 20%; flex: 1 1 20%; max-width: 20%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-25{-webkit-flex: 1 1 25%; -ms-flex: 1 1 25%; flex: 1 1 25%; max-width: 25%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-30{-webkit-flex: 1 1 30%; -ms-flex: 1 1 30%; flex: 1 1 30%; max-width: 30%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-35{-webkit-flex: 1 1 35%; -ms-flex: 1 1 35%; flex: 1 1 35%; max-width: 35%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-40{-webkit-flex: 1 1 40%; -ms-flex: 1 1 40%; flex: 1 1 40%; max-width: 40%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-45{-webkit-flex: 1 1 45%; -ms-flex: 1 1 45%; flex: 1 1 45%; max-width: 45%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-50{-webkit-flex: 1 1 50%; -ms-flex: 1 1 50%; flex: 1 1 50%; max-width: 50%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-55{-webkit-flex: 1 1 55%; -ms-flex: 1 1 55%; flex: 1 1 55%; max-width: 55%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-60{-webkit-flex: 1 1 60%; -ms-flex: 1 1 60%; flex: 1 1 60%; max-width: 60%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-65{-webkit-flex: 1 1 65%; -ms-flex: 1 1 65%; flex: 1 1 65%; max-width: 65%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-70{-webkit-flex: 1 1 70%; -ms-flex: 1 1 70%; flex: 1 1 70%; max-width: 70%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-75{-webkit-flex: 1 1 75%; -ms-flex: 1 1 75%; flex: 1 1 75%; max-width: 75%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-80{-webkit-flex: 1 1 80%; -ms-flex: 1 1 80%; flex: 1 1 80%; max-width: 80%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-85{-webkit-flex: 1 1 85%; -ms-flex: 1 1 85%; flex: 1 1 85%; max-width: 85%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-90{-webkit-flex: 1 1 90%; -ms-flex: 1 1 90%; flex: 1 1 90%; max-width: 90%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-95{-webkit-flex: 1 1 95%; -ms-flex: 1 1 95%; flex: 1 1 95%; max-width: 95%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } @media screen and (max-width: 319px){.container-main{border:1px solid orange; display: none; } .msj-not-resolution{display: block; font-family: HelveticaNeueLT-Light; color: #28cad6; text-align: center; font-size: 20px; margin: 6em 0em; } } /* Small devices (smartphones, 320px and up) */ @media (min-width: 320px){.msj-not-resolution{display: none;} .text-align-gt{text-align: center; } .order-gt-1{order:1; -webkit-order:1; } .order-gt-2{order:2; -webkit-order:2; } .order-gt-3{order:3; -webkit-order:3; } .order-gt-4{order:4; -webkit-order:4; } .main-text1{font-size:10vw; } .second-text1{font-size: 3.5vw;padding: 0.1em 0em 0.6em;opacity: 0.9; } .flex-gt-hide{display: none; } .flex-gt-5{-webkit-flex: 1 1 5%; -ms-flex: 1 1 5%; flex: 1 1 5%; max-width: 5%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-10{-webkit-flex: 1 1 10%; -ms-flex: 1 1 10%; flex: 1 1 10%; max-width: 10%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-15{-webkit-flex: 1 1 15%; -ms-flex: 1 1 15%; flex: 1 1 15%; max-width: 15%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-20{-webkit-flex: 1 1 20%; -ms-flex: 1 1 20%; flex: 1 1 20%; max-width: 20%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-25{-webkit-flex: 1 1 25%; -ms-flex: 1 1 25%; flex: 1 1 25%; max-width: 25%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-30{-webkit-flex: 1 1 30%; -ms-flex: 1 1 30%; flex: 1 1 30%; max-width: 30%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-35{-webkit-flex: 1 1 35%; -ms-flex: 1 1 35%; flex: 1 1 35%; max-width: 35%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-40{-webkit-flex: 1 1 40%; -ms-flex: 1 1 40%; flex: 1 1 40%; max-width: 40%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-45{-webkit-flex: 1 1 45%; -ms-flex: 1 1 45%; flex: 1 1 45%; max-width: 45%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-50{-webkit-flex: 1 1 50%; -ms-flex: 1 1 50%; flex: 1 1 50%; max-width: 50%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-55{-webkit-flex: 1 1 55%; -ms-flex: 1 1 55%; flex: 1 1 55%; max-width: 55%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-60{-webkit-flex: 1 1 60%; -ms-flex: 1 1 60%; flex: 1 1 60%; max-width: 60%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-65{-webkit-flex: 1 1 65%; -ms-flex: 1 1 65%; flex: 1 1 65%; max-width: 65%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-70{-webkit-flex: 1 1 70%; -ms-flex: 1 1 70%; flex: 1 1 70%; max-width: 70%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-75{-webkit-flex: 1 1 75%; -ms-flex: 1 1 75%; flex: 1 1 75%; max-width: 75%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-80{-webkit-flex: 1 1 80%; -ms-flex: 1 1 80%; flex: 1 1 80%; max-width: 80%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-85{-webkit-flex: 1 1 85%; -ms-flex: 1 1 85%; flex: 1 1 85%; max-width: 85%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-90{-webkit-flex: 1 1 90%; -ms-flex: 1 1 90%; flex: 1 1 90%; max-width: 90%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-95{-webkit-flex: 1 1 95%; -ms-flex: 1 1 95%; flex: 1 1 95%; max-width: 95%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-gt-100{-webkit-flex: 1 1 100%; -ms-flex: 1 1 100%; flex: 1 1 100%; max-width: 100%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } } /* Small devices (tablets, 600px and up) */ @media (min-width: 600px){.msj-not-resolution{display: none;} .text-align-xs{text-align: center; } .order-xs-1{order:1; -webkit-order:1; } .order-xs-2{order:2; -webkit-order:2; } .order-xs-3{order:3; -webkit-order:3; } .order-xs-4{order:4; -webkit-order:4; } .main-text1{font-size:58px; } .second-text1{font-size: 20px;padding: 0.1em 0em 0.6em;opacity: 0.9; } .flex-xs-hide{display: none; } .flex-xs-5{-webkit-flex: 1 1 5%; -ms-flex: 1 1 5%; flex: 1 1 5%; max-width: 5%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-10{-webkit-flex: 1 1 10%; -ms-flex: 1 1 10%; flex: 1 1 10%; max-width: 10%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-15{-webkit-flex: 1 1 15%; -ms-flex: 1 1 15%; flex: 1 1 15%; max-width: 15%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-20{-webkit-flex: 1 1 20%; -ms-flex: 1 1 20%; flex: 1 1 20%; max-width: 20%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-25{-webkit-flex: 1 1 25%; -ms-flex: 1 1 25%; flex: 1 1 25%; max-width: 25%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-30{-webkit-flex: 1 1 30%; -ms-flex: 1 1 30%; flex: 1 1 30%; max-width: 30%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-35{-webkit-flex: 1 1 35%; -ms-flex: 1 1 35%; flex: 1 1 35%; max-width: 35%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-40{-webkit-flex: 1 1 40%; -ms-flex: 1 1 40%; flex: 1 1 40%; max-width: 40%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-45{-webkit-flex: 1 1 45%; -ms-flex: 1 1 45%; flex: 1 1 45%; max-width: 45%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-50{-webkit-flex: 1 1 50%; -ms-flex: 1 1 50%; flex: 1 1 50%; max-width: 50%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-55{-webkit-flex: 1 1 55%; -ms-flex: 1 1 55%; flex: 1 1 55%; max-width: 55%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-60{-webkit-flex: 1 1 60%; -ms-flex: 1 1 60%; flex: 1 1 60%; max-width: 60%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-65{-webkit-flex: 1 1 65%; -ms-flex: 1 1 65%; flex: 1 1 65%; max-width: 65%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-70{-webkit-flex: 1 1 70%; -ms-flex: 1 1 70%; flex: 1 1 70%; max-width: 70%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-75{-webkit-flex: 1 1 75%; -ms-flex: 1 1 75%; flex: 1 1 75%; max-width: 75%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-80{-webkit-flex: 1 1 80%; -ms-flex: 1 1 80%; flex: 1 1 80%; max-width: 80%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-85{-webkit-flex: 1 1 85%; -ms-flex: 1 1 85%; flex: 1 1 85%; max-width: 85%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-90{-webkit-flex: 1 1 90%; -ms-flex: 1 1 90%; flex: 1 1 90%; max-width: 90%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-95{-webkit-flex: 1 1 95%; -ms-flex: 1 1 95%; flex: 1 1 95%; max-width: 95%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-xs-100{-webkit-flex: 1 1 100%; -ms-flex: 1 1 100%; flex: 1 1 100%; max-width: 100%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } } /* Small devices (tablets, 768px and up) */ @media (min-width: 768px) {.msj-not-resolution{display: none;} .text-align-sm{text-align: center; } /* Clases order */ .order-sm-1{order:1; -webkit-order:1; } .order-sm-2{order:2; -webkit-order:2; } .order-sm-3{order:3; -webkit-order:3; } .order-sm-4{order:4; -webkit-order:4; } .main-text3{font-size:70px; } .second-text3{font-size: 23px; padding: 0.1em 0em 0.6em; opacity: 0.9; } .logo{width: 70px; } .flex-sm-5{-webkit-flex: 1 1 5%; -ms-flex: 1 1 5%; flex: 1 1 5%; max-width: 5%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-10{-webkit-flex: 1 1 10%; -ms-flex: 1 1 10%; flex: 1 1 10%; max-width: 10%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-15{-webkit-flex: 1 1 15%; -ms-flex: 1 1 15%; flex: 1 1 15%; max-width: 15%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-20{-webkit-flex: 1 1 20%; -ms-flex: 1 1 20%; flex: 1 1 20%; max-width: 20%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-25{-webkit-flex: 1 1 25%; -ms-flex: 1 1 25%; flex: 1 1 25%; max-width: 25%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-30{-webkit-flex: 1 1 30%; -ms-flex: 1 1 30%; flex: 1 1 30%; max-width: 30%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-35{-webkit-flex: 1 1 35%; -ms-flex: 1 1 35%; flex: 1 1 35%; max-width: 35%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-40{-webkit-flex: 1 1 40%; -ms-flex: 1 1 40%; flex: 1 1 40%; max-width: 40%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-45{-webkit-flex: 1 1 45%; -ms-flex: 1 1 45%; flex: 1 1 45%; max-width: 45%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-50{-webkit-flex: 1 1 50%; -ms-flex: 1 1 50%; flex: 1 1 50%; max-width: 50%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-55{-webkit-flex: 1 1 55%; -ms-flex: 1 1 55%; flex: 1 1 55%; max-width: 55%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-60{-webkit-flex: 1 1 60%; -ms-flex: 1 1 60%; flex: 1 1 60%; max-width: 60%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-65{-webkit-flex: 1 1 65%; -ms-flex: 1 1 65%; flex: 1 1 65%; max-width: 65%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-70{-webkit-flex: 1 1 70%; -ms-flex: 1 1 70%; flex: 1 1 70%; max-width: 70%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-75{-webkit-flex: 1 1 75%; -ms-flex: 1 1 75%; flex: 1 1 75%; max-width: 75%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-80{-webkit-flex: 1 1 80%; -ms-flex: 1 1 80%; flex: 1 1 80%; max-width: 80%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-85{-webkit-flex: 1 1 85%; -ms-flex: 1 1 85%; flex: 1 1 85%; max-width: 85%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-90{-webkit-flex: 1 1 90%; -ms-flex: 1 1 90%; flex: 1 1 90%; max-width: 90%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-95{-webkit-flex: 1 1 95%; -ms-flex: 1 1 95%; flex: 1 1 95%; max-width: 95%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-100{-webkit-flex: 1 1 100%; -ms-flex: 1 1 100%; flex: 1 1 100%; max-width: 100%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-sm-hide{display: none; } } /* Medium devices (desktops, 992px and up) */ @media (min-width: 992px) {.msj-not-resolution{display: none;} .flex-md-show{display:block;} .text-align-md{text-align: left; } .order-md-1{order:1; -webkit-order:1; } .order-md-2{order:2; -webkit-order:2; } .order-md-3{order:3; -webkit-order:3; } .order-md-4{order:4; -webkit-order:4; } .main-text2{font-size:75px; } .second-text2{font-size: 23px; padding: 0.1em 0em 0.6em; opacity: 0.9; } .flex-md-100{-webkit-flex: 1 1 100%; -ms-flex: 1 1 100%; flex: 1 1 100%; max-width: 100%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-5{-webkit-flex: 1 1 5%; -ms-flex: 1 1 5%; flex: 1 1 5%; max-width: 5%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-10{-webkit-flex: 1 1 10%; -ms-flex: 1 1 10%; flex: 1 1 10%; max-width: 10%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-15{-webkit-flex: 1 1 15%; -ms-flex: 1 1 15%; flex: 1 1 15%; max-width: 15%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-20{-webkit-flex: 1 1 20%; -ms-flex: 1 1 20%; flex: 1 1 20%; max-width: 20%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-25{-webkit-flex: 1 1 25%; -ms-flex: 1 1 25%; flex: 1 1 25%; max-width: 25%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-30{-webkit-flex: 1 1 30%; -ms-flex: 1 1 30%; flex: 1 1 30%; max-width: 30%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-35{-webkit-flex: 1 1 35%; -ms-flex: 1 1 35%; flex: 1 1 35%; max-width: 35%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-40{-webkit-flex: 1 1 40%; -ms-flex: 1 1 40%; flex: 1 1 40%; max-width: 40%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-45{-webkit-flex: 1 1 45%; -ms-flex: 1 1 45%; flex: 1 1 45%; max-width: 45%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-50{-webkit-flex: 1 1 50%; -ms-flex: 1 1 50%; flex: 1 1 50%; max-width: 50%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-55{-webkit-flex: 1 1 55%; -ms-flex: 1 1 55%; flex: 1 1 55%; max-width: 55%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-60{-webkit-flex: 1 1 60%; -ms-flex: 1 1 60%; flex: 1 1 60%; max-width: 60%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-65{border:1px solid blue; -webkit-flex: 1 1 65%; -ms-flex: 1 1 65%; flex: 1 1 65%; max-width: 65%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-70{-webkit-flex: 1 1 70%; -ms-flex: 1 1 70%; flex: 1 1 70%; max-width: 70%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-75{-webkit-flex: 1 1 75%; -ms-flex: 1 1 75%; flex: 1 1 75%; max-width: 75%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-80{-webkit-flex: 1 1 80%; -ms-flex: 1 1 80%; flex: 1 1 80%; max-width: 80%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-85{-webkit-flex: 1 1 85%; -ms-flex: 1 1 85%; flex: 1 1 85%; max-width: 85%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-90{-webkit-flex: 1 1 90%; -ms-flex: 1 1 90%; flex: 1 1 90%; max-width: 90%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-md-95{-webkit-flex: 1 1 95%; -ms-flex: 1 1 95%; flex: 1 1 95%; max-width: 95%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } } /* Large devices (large desktops, 1200px and up) */ @media (min-width: 1200px) {.msj-not-resolution{display: none;} .flex-lg-show{display:block;} .text-align-lg{text-align: left; } .order-lg-1{order:1; -webkit-order:1; } .order-lg-2{order:2; -webkit-order:2; } .order-lg-3{order:3; -webkit-order:3; } .order-lg-4{order:4; -webkit-order:4; } .main-text1{font-size:85px; } .second-text1{font-size: 26px;padding: 0.1em 0em 0.6em;opacity: 0.9; } .flex-lg-5{-webkit-flex: 1 1 5%; -ms-flex: 1 1 5%; flex: 1 1 5%; max-width: 5%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-10{-webkit-flex: 1 1 10%; -ms-flex: 1 1 10%; flex: 1 1 10%; max-width: 10%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-15{-webkit-flex: 1 1 15%; -ms-flex: 1 1 15%; flex: 1 1 15%; max-width: 15%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-20{-webkit-flex: 1 1 20%; -ms-flex: 1 1 20%; flex: 1 1 20%; max-width: 20%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-25{-webkit-flex: 1 1 25%; -ms-flex: 1 1 25%; flex: 1 1 25%; max-width: 25%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-30{-webkit-flex: 1 1 30%; -ms-flex: 1 1 30%; flex: 1 1 30%; max-width: 30%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-35{-webkit-flex: 1 1 35%; -ms-flex: 1 1 35%; flex: 1 1 35%; max-width: 35%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-40{-webkit-flex: 1 1 40%; -ms-flex: 1 1 40%; flex: 1 1 40%; max-width: 40%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-45{-webkit-flex: 1 1 45%; -ms-flex: 1 1 45%; flex: 1 1 45%; max-width: 45%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-50{-webkit-flex: 1 1 50%; -ms-flex: 1 1 50%; flex: 1 1 50%; max-width: 50%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-55{-webkit-flex: 1 1 55%; -ms-flex: 1 1 55%; flex: 1 1 55%; max-width: 55%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-60{-webkit-flex: 1 1 60%; -ms-flex: 1 1 60%; flex: 1 1 60%; max-width: 60%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-65{-webkit-flex: 1 1 65%; -ms-flex: 1 1 65%; flex: 1 1 65%; max-width: 65%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-70{-webkit-flex: 1 1 70%; -ms-flex: 1 1 70%; flex: 1 1 70%; max-width: 70%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-75{-webkit-flex: 1 1 75%; -ms-flex: 1 1 75%; flex: 1 1 75%; max-width: 75%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-80{-webkit-flex: 1 1 80%; -ms-flex: 1 1 80%; flex: 1 1 80%; max-width: 80%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-85{-webkit-flex: 1 1 85%; -ms-flex: 1 1 85%; flex: 1 1 85%; max-width: 85%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-90{-webkit-flex: 1 1 90%; -ms-flex: 1 1 90%; flex: 1 1 90%; max-width: 90%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } .flex-lg-95{-webkit-flex: 1 1 95%; -ms-flex: 1 1 95%; flex: 1 1 95%; max-width: 95%; max-height: 100%; box-sizing: border-box; word-wrap:break-word; } } body{padding:0; margin: 0; font-family: Helvetica, Arial, sans-serif; color: rgba(0,0,0,0.8); } p, span{margin: 0; font-size: 19px; width: 100%; text-align: center; } p{margin-top: 0.5em; } div span{text-align: center; font-size: 16px; margin: 0 auto; display: block; } .mod-inline{display: inline-block; vertical-align: middle; text-align: center; } .mod-section{padding: 1em 0em; /* Permalink - use to edit and share this gradient: http://colorzilla.com/gradient-editor/#ffffff+0,ffffff+100&1+44,0+100 */background: -moz-radial-gradient(center, ellipse cover,  rgba(255,255,255,1) 0%, rgba(255,255,255,1) 44%, rgba(255,255,255,0) 100%); /* FF3.6-15 */background: -webkit-radial-gradient(center, ellipse cover,  rgba(255,255,255,1) 0%,rgba(255,255,255,1) 44%,rgba(255,255,255,0) 100%); /* Chrome10-25,Safari5.1-6 */background: radial-gradient(ellipse at center,  rgba(255,255,255,1) 0%,rgba(255,255,255,1) 44%,rgba(255,255,255,0) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffffff', endColorstr='#00ffffff',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */} .mod-section .inner-section{margin: 1em 0em; } /**/ .cont-circle-number > div {padding:7px 0px; } .borde{border: 1px solid red; } .mod-texto{margin: 1.5em 0em; } /* p i i */ .content-img-big{overflow: hidden; /*max-height: 400px;*/ text-align: center; } .content-img-big img{width: 90%; } .content-img-small{overflow: hidden; border-radius: 16px; -webkit-border-radius: 16px; } .shadow-box{-webkit-box-shadow: 7px 7px 1px 0px rgba(50, 50, 50, 0.15); -moz-box-shadow:    7px 7px 1px 0px rgba(50, 50, 50, 0.15); box-shadow:         7px 7px 1px 0px rgba(50, 50, 50, 0.15); -webkit-border-radius: 16px; -moz-border-radius: 16px; -ms-border-radius: 16px; -o-border-radius: 16px; } .content-img-small img{width: 100%; } img{width: 100%; } .uppercase{text-transform: uppercase; }
	/* CLASES VARIABILIDAD DE COLORES */

	.cont-circle-number{
		background-color:${color_secundario};
		width: 50px;
		height:50px;
		padding: 0.1em;
		margin: 0.5em 0em;
		color: white;
		font-family: Arial;
		font-weight: bold;
		font-size: 33px;
		text-align: center;
		border-radius: 10em;
		-webkit-border-radius: 10em;
		-moz-border-radius: 10em;
		-ms-border-radius: 10em;
		-o-border-radius: 10em;
	}

	.cont-t-cabecera, .titulo-descripcion-main, .titulo-caracteristica{
		font-family: 'HelveticaNeue-Thin', Helvetica, arial, sans-serif;
	}

	.cont-t-cabecera{
		background-color: ${color_primario};
		color: white;
		border-radius: 10px;
	}

	.separador-info-t-cabecera{
		background:${color_secundario};
		height:3px;
	}

	.titulo-descripcion-main{
		color: ${color_secundario};
		font-size: 30px;
		text-transform: uppercase;
	}

	.titulo-caracteristica{
		color: ${color_caracteristica};
		font-size: 30px;
	}

	a{text-transform: uppercase;}

	/* unvisited link */
	a:link {
	    color: #4e8cca;
	}

	/* visited link */
	a:visited {
	    color:#4e8cca;
	}

	/* mouse over link */
	a:hover {
	    color: #4e8cca;
	}

	/* selected link */
	a:active {
	    color: b#4e8cca;
	}

	</style>
'''


templates['cabecera'] = '''
			<section class="layout-row justify-space-around align-center">
				<div class="container-main flex-lg-75 flex-md-85 flex-sm-95 flex-xs-95 flex-gt-95" style="padding: 2vh 0vh;">


					<!-- CABECERA -->
					<section class="layout-row align-start">
						
						<div class="flex-lg-100 flex-md-100 flex-sm-100 flex-xs-100 flex-gt-100 layout-row justify-space-between">
							<div class="flex-lg-80 flex-md-80 flex-sm-85 flex-xs-85 flex-gt-90 layout-row justify-start align-start">
								<div class="flex-lg-100 flex-md-100 flex-sm-100 flex-xs-100 flex-gt-100 layout-row justify-space-around align-center cont-t-cabecera">
									<!-- Contenedor titulo principal -->
									<div class="flex-lg-95 flex-md-95 flex-xs-sm flex-xs-95 flex-gt-95 uppercase main-text1 main-text2 main-text3" style="text-align:center;">${nombre_producto}</div>
									<div class="flex-lg-95 flex-md-95 flex-xs-sm flex-xs-95 flex-gt-95 separador-info-t-cabecera"></div>
									<div class="flex-lg-95 flex-md-95 flex-xs-sm flex-xs-95 flex-gt-95 uppercase second-text1 second-text2 second-text3" style="text-align:center;">${subtitulo_cabecera}</div>
								</div>
							</div>
							<!-- Logo Lenovo -->
							<div class="flex-lg-10 flex-md-15 flex-sm-15 flex-xs-10 flex-gt-10 layout-row justify-end">
								<div><img class="logo" src="${logo_lenovo}"></div>
							</div>
						</div>
					</section>

'''

templates['P'] = '''

					<!-- ESTRUCTURA DE INFORMACIÓN P -->

					<section class="flex-lg-100 flex-md-100 flex-sm-100 flex-xs-100 flex-gt-100 layout-row justify-center mod-section" style="margin:3em 0em;">
						<div class="inner-section flex-lg-70 flex-sm-80 flex-xs-80 flex-gt-90">
							<div>
								<span class="titulo-descripcion-main">${t_descripcion_principal}</span>
							</div>
							<p style="margin-top:1em;">${p_descripcion_principal}</p>
						</div>
					</section>


'''

templates['I-P'] = '''

					<!-- ESTRUCTURA DE INFORMACIÓN I | P-->

					<section class="mod-section layout-row justify-space-around align-center">
						<div class="flex-lg-45 flex-md-45 flex-45 flex-sm-55 flex-xs-70 flex-gt-70  content-img-small shadow-box order-lg-1 order-md-1 order-sm-2 order-xs-2 order-gt-2">
							<img src="${img_apoyo}">
						</div>
						<div class="flex-lg-45 flex-md-45 flex-45 flex-sm-80 flex-xs-80 flex-gt-90  mod-texto order-lg-2 order-md-2 order-sm-1 order-xs-1 order-gt-1">
							<!-- MOD. P -->
							<div class="mod-p">
								<div class="layout-row justify-space-around align-start mod-texto">
									<div class="flex-lg-75 flex-md-80 order-lg-1 order-md-1 order-sm-2 order-xs-2 order-gt-2">
										<div>
											<span class="titulo-caracteristica">${t_caracteristica}</span>
										</div>
										<p>${p_caracteristica}</p>
									</div>
									<div class="flex-lg-15 flex-md-20 flex-sm-100  layout-row justify-center align-center order-lg-2 order-md-2 order-sm-1  order-xs-1 order-gt-1 ">
										<div class="mod-inline cont-circle-number">
											<div>${numero_caracteristica}</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</section>

'''

templates['I'] = '''
					<!-- ESTRUCTURA DE INFORMACIÓN I -->

					<section class="layout-row justify-space-around align-center mod-section" style="margin-top:2em;">
						<div class=" inner-section flex-lg-40 flex-md-45 flex-sm-80 flex-xs-70 flex-gt-70 content-img-small" style="text-align:center;">
							<img src="${img_apoyo}">
						</div>
					</section>
'''


templates['P-I-I'] = '''

					<!-- ESTRUCTURA DE INFORMACIÓN P | I | I GRANDE  -->
					
					<section class="mod-section layout-row justify-space-around align-center">
						<div class="inner-section flex-lg-50 flex-md-50 flex-sm-85 flex-xs-80 flex-gt-90 justify-center align-stretch">
							<!-- MOD. P -->
							<div class="mod-p">
								<div class="layout-row justify-space-around align-start mod-texto">
									<div class="flex-lg-15 flex-md-20 flex-sm-100 layout-row justify-center align-center">
										<div class="mod-inline cont-circle-number">
											<div>${numero_caracteristica}</div>
										</div>
									</div>
									<div class="flex-lg-75 flex-md-80 flex-sm-100">
										<div>
											<span class="titulo-caracteristica">${t_caracteristica}</span>
										</div>
										<p>${p_caracteristica}</p>
									</div>
								</div>
							</div>
							<div class="layout-row justify-space-around align-center">
								<div class="flex-lg-15 flex-md-15 flex-lg-show flex-md-show flex-sm-hide flex-xs-hide flex-gt-hide"></div>
								<div class="flex-lg-75 flex-md-75 flex-sm-55 flex-xs-70 flex-gt-75 content-img-small">
									<img src="${img_apoyo_1}">
								</div>
							</div>
						</div>
						<div class="inner-section flex-lg-40 flex-md-40 flex-sm-50 flex-xs-55 flex-gt-60 content-img-big">
								<img src="${img_apoyo_2}">
						</div>
					</section>
'''

templates['I-IP-I'] = '''

					<!-- ESTRUCTURA DE INFORMACIÓN I | I P | I -->

					<section class="mod-section layout-row justify-space-around align-center">
						<div class="inner-section flex-lg-25 flex-md-25 flex-sm-40 flex-xs-40 flex-gt-40 content-img-small shadow-box order-lg-1 order-md-1 order-sm-2 order-xs-2 order-gt-2">
							<img src="${img_apoyo_1}">
						</div>
						<div class="inner-section layout-row flex-lg-45 flex-md-45 flex-sm-80 flex-xs-80 flex-gt-90 order-lg-2 order-md-2 order-sm-1 order-xs-1 order-gt-1">
							
							<div class="flex-lg-100 flex-md-100 flex-sm-100 flex-xs-100 layout-row justify-space-around align-center order-lg-1 order-md-1 order-sm-2 order-xs-2 order-gt-2">
								<div class="flex-lg-80 flex-md-100 flex-sm-80 flex-xs-80 flex-gt-85" style="text-align:center;">
									<img src="${img_apoyo_2}">
								</div>
							</div>
							<!-- MOD. P -->
							<div class="flex-lg-100 flex-md-100 flex-sm-100 flex-xs-100 flex-gt-100 mod-p order-lg-2 order-md-2 order-sm-1 order-xs-1 order-gt-1">
								<div class="layout-row justify-space-around align-start mod-texto">
									<div class="flex-lg-15 flex-md-20 flex-sm-100 flex-xs-100 flex-gt-100 layout-row justify-center align-center">
										<div class="mod-inline cont-circle-number">
											<div>${numero_caracteristica}</div>
										</div>
									</div>
									<div class="flex-lg-75 flex-md-80 flex-sm-80 flex-xs-80 flex-gt-80">
										<div>
											<span class="titulo-caracteristica" >${t_caracteristica}</span>
										</div>
										<p>${p_caracteristica}</p>
									</div>
								</div>
							</div>
						</div>
						<div class="inner-section flex-lg-20 flex-md-15 flex-sm-30 flex-xs-35 flex-gt-35 content-img-small order-md-3 order-sm-3 order-xs-3 order-gt-3">
							 <img src="${img_apoyo_3}">
						</div>
					</section>

'''

templates['P-I'] = '''

					<!-- ESTRUCTURA DE INFORMACIÓN P | I-->
					
					<section class="layout-row justify-space-around align-center mod-section">
						<div class="flex-lg-45 flex-md-45 flex-45 flex-sm-80 flex-xs-80 flex-gt-90  mod-texto">
							<!-- MOD. P -->
							<div class="mod-p">
								<div class="layout-row justify-space-around align-start mod-texto">
									<div class="flex-lg-75 flex-md-80 order-lg-1 order-md-1 order-sm-2  order-xs-2 order-gt-2 ">
										<div>
											<span class="titulo-caracteristica">${t_caracteristica}</span>
										</div>
										<p>${p_caracteristica}</p>
									</div>
									<div class="flex-lg-15 flex-md-20 flex-sm-100  layout-row justify-center align-center order-lg-2 order-md-2 order-sm-1  order-xs-1 order-gt-1">
										<div class="mod-inline cont-circle-number">
											<div>${numero_caracteristica}</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						<div class="flex-lg-45 flex-md-45 flex-45 flex-sm-55 flex-xs-70 flex-gt-70 content-img-small">
							<img src="${img_apoyo}">
						</div>
					</section>

'''

templates['I-I'] = '''


					<!-- ESTRUCTURA DE INFORMACIÓN I | I  CHECK -->

					<section class="layout-row justify-space-around align-center mod-section" style="margin-top:2em;">
						<div class=" inner-section flex-lg-40 flex-md-45 flex-sm-80 flex-xs-70 flex-gt-70 content-img-small" style="text-align:center;">
							<img src="${img_apoyo_1}">
						</div>

						<div class=" inner-section flex-lg-40 flex-md-45 flex-sm-80 flex-xs-70 flex-gt-70 content-img-small" style="text-align:center;">
							<img src="${img_apoyo_2}">
						</div>
					</section>
					
'''

templates['I-P-I'] = '''

					<!-- ESTRUCTURA DE INFORMACIÓN I | P | I -->

					<section class="mod-section layout-row justify-space-around align-center">
						<div class="inner-section flex-lg-25 flex-md-25 flex-sm-50 flex-xs-70 flex-gt-70 content-img-small shadow-box order-lg-1 order-md-1 order-sm-2 order-xs-2 order-gt-2">
							<img src="${img_apoyo_1}">
						</div>
						<div class="inner-section flex-lg-45 flex-md-45 flex-sm-80 flex-xs-80 flex-gt-90 order-lg-2 order-md-2 order-sm-1 order-xs-1 order-gt-1">
							<!-- MOD. P -->
							<div class="mod-p">
								<div class="layout-row justify-space-around align-start mod-texto">
									<div class="flex-lg-15 flex-md-20 flex-sm-100 flex-xs-100 flex-gt-100 layout-row justify-center align-center">
										<div class="mod-inline cont-circle-number">
											<div>${numero_caracteristica}</div>
										</div>
									</div>
									<div class="flex-lg-75 flex-md-80 flex-sm-80 flex-xs-80 flex-gt-80 flex-xs-80">
										<div>
											<span class="titulo-caracteristica" >${t_caracteristica}</span>
										</div>
										<p>${p_caracteristica}</p>
									</div>
								</div>
							</div>
						</div>
						<div class="inner-section flex-lg-20 flex-md-15 flex-sm-55 flex-xs-55 flex-gt-70 content-img-small order-lg-3 order-md-2 order-sm-3 order-xs-3 order-gt-3">
							 <img src="${img_apoyo_2}">
						</div>
					</section>
'''

templates['P-P'] = '''
					<!-- ESTRUCTURA DE INFORMACIÓN P | P -->

					<section class="mod-section layout-row justify-space-around align-start">
						<div class="inner-section flex-lg-45 flex-md-45 flex-sm-80 flex-xs-80 flex-gt-90">
							<div class="mod-list layout-row justify-center align-start">
								<!-- Logo-especificación -->
								<div class="layout-row justify-center align-start flex-lg-30 flex-md-30 flex-sm-80 flex-xs-90 flex-gt-100">
									<img style="max-width:110px;max-height:102px;" src="${icono_caracteristica_1}">
								</div>
								<!-- Parrafo-especificación -->
								<div class="flex-lg-70 flex-md-70 flex-sm-80 flex-xs-90 flex-gt-100">
									<p class="text-align-lg text-align-md text-align-sm text-align-xs text-align-gt">${detalle_caracteristica_1}</p>
								</div>
							</div>
						</div>
						<div class="inner-section flex-lg-45 flex-md-45 flex-sm-80 flex-xs-80 flex-gt-90">
							<div class="mod-list layout-row justify-center align-start">
								<!-- Logo-especificación -->
								<div class="layout-row justify-center align-start flex-lg-30 flex-md-30 flex-sm-80 flex-xs-90 flex-gt-100">
									<img style="max-width:110px;max-height:102px;" src="${icono_caracteristica_2}">
								</div>
								<!-- Parrafo-especificación -->
								<div class="flex-lg-70 flex-md-70 flex-sm-80 flex-xs-90 flex-gt-100">
									<p class="text-align-lg text-align-md text-align-sm text-align-xs text-align-gt">${detalle_caracteristica_2}</p>
								</div>
							</div>
						</div>
					</section>

'''

templates['I-P-nonumero'] = '''
					<!-- ESTRUCTURA DE INFORMACIÓN I | P SIN NÚMERO-->

					<section class="mod-section layout-row justify-space-around align-center">
						<div class="flex-lg-45 flex-md-45 flex-45 flex-sm-55 flex-xs-70 flex-gt-70  content-img-small shadow-box order-lg-1 order-md-1 order-sm-2 order-xs-2 order-gt-2">
							<img src="${img_apoyo}">
						</div>
						<div class="flex-lg-45 flex-md-45 flex-45 flex-sm-80 flex-xs-80 flex-gt-90  mod-texto order-lg-2 order-md-2 order-sm-1 order-xs-1 order-gt-1">
							<!-- MOD. P -->
							<div class="mod-p">
								<div class="layout-row justify-space-around align-start mod-texto">
									<div class="flex-lg-100 flex-md-90 order-lg-1 order-md-1 order-sm-2 order-xs-2 order-gt-2">
										<p>${p_caracteristica}</p>
									</div>
								</div>
							</div>
						</div>
					</section>
'''

templates['Igrande-P-I'] = '''
					<!-- ESTRUCTURA DE INFORMACIÓN I GRANDE | P | I   -->
					
					<section class="mod-section layout-row justify-space-around align-start">
						<div class="inner-section flex-lg-40 flex-md-40 flex-sm-50 flex-xs-55 flex-gt-60 content-img-big order-lg-1 order-md-1 order-sm-2 order-xs-2 order-gt-2">
								<img src="${img_apoyo_1}">
						</div>
						<div class="inner-section flex-lg-50 flex-md-50 flex-sm-85 flex-xs-80 flex-gt-90 justify-center align-stretch order-lg-2 order-md-2 order-sm-1 order-xs-1 order-gt-1">
							<!-- MOD. P -->
							<div class="mod-p">
								<div class="layout-row justify-space-around align-start mod-texto">
									<div class="flex-lg-100 flex-md-100 flex-sm-100 flex-xs-100 flex-gt-100">
										<div>
											<span class="titulo-caracteristica">${t_caracteristica}</span>
										</div>
										<p>${p_caracteristica}</p>
									</div>
								</div>
							</div>
							<div class="layout-row justify-space-around align-center">
								<div class="flex-lg-100 flex-md-100 flex-sm-100 flex-xs-100 flex-gt-100 flex-xs-60 flex-gt-80 flex-md-80">
									<img src="${img_apoyo_2}">
								</div>
							</div>
						</div>
					</section>
'''

templates['fin'] = '''

				</div>


				<!-- FOOTER -->
				<footer style="margin:2em 0em;" class="layout-row justify-center align-center flex-lg-75 flex-md-85 flex-sm-95 flex-xs-95 flex-gt-95">
					<div class="layout-row justify-center align-center flex-lg-60 flex-md-60 flex-sm-60 flex-xs-60 flex-gt-60">
						<div style="padding:0em 0.2em;">
							<img src="../img/OTROS/logo_red_social_1.png">
						</div>
						<div style="padding:0em 0.2em;">
							<img src="../img/OTROS/logo_red_social_2.png">
						</div>
						<div style="padding:0em 0.5em;"><a href="#"><b>www.lenovo.com</b></a></div>
					</div>
				</footer>

				<!-- Mensaje en caso de resoluciones demasiado bajas <=319px -->
				<div class="msj-not-resolution">
					<h3>LO SENTIMOS</h3> 
					<p>la resolución de tú dispositivo es demasiado baja.</p>
				</div>
			</section>
        </body>
    </html>
'''

def generar_ficha(mapa):
    salida = ''
    for seccion in mapa:
        salida = salida + Template(templates[seccion[0]].decode('utf-8')).substitute(seccion[1])
    return salida
