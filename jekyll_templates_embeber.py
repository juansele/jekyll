#!/usr/bin/python
#coding: utf-8

from string import Template

templates = {}

templates['inicio'] = '''
		<!-- ESTILOS DE LA FICHA -->
		<style type="text/css">
		
			iframe.mett__iframe{width:100%;max-width:755px;height:425px}a.mett__link{text-decoration:none;color:#444}@font-face{font-family:HelveticaNeueLT-Light;src:url(fonts/HelveticaNeueLT-Light_gdi.eot);src:url(fonts/HelveticaNeueLT-Light_gdi.eot?#iefix) format('embedded-opentype'),url(fonts/HelveticaNeueLT-Light_gdi.woff) format('woff'),url(fonts/HelveticaNeueLT-Light_gdi.ttf) format('truetype'),url(fonts/HelveticaNeueLT-Light_gdi.svg#HelveticaNeueLT-Light) format('svg');font-weight:3;font-style:normal;font-stretch:normal;unicode-range:U+0-10FFFF}@font-face{font-family:HelveticaNeue-Thin;src:url(fonts/HelveticaNeue-Thin_gdi.eot);src:url(fonts/HelveticaNeue-Thin_gdi.eot?#iefix) format('embedded-opentype'),url(fonts/HelveticaNeue-Thin_gdi.woff) format('woff'),url(fonts/HelveticaNeue-Thin_gdi.ttf) format('truetype'),url(fonts/HelveticaNeue-Thin_gdi.svg#HelveticaNeue-Thin) format('svg');font-weight:100;font-style:normal;font-stretch:normal;unicode-range:U+0020-2212}@font-face{font-family:icomoon;src:url(fonts/icomoon.eot?44l93u);src:url(fonts/icomoon.eot?44l93u#iefix) format('embedded-opentype'),url(fonts/icomoon.ttf?44l93u) format('truetype'),url(fonts/icomoon.woff?44l93u) format('woff'),url(fonts/icomoon.svg?44l93u#icomoon) format('svg');font-weight:400;font-style:normal}[class^=icon-],[class*=mett__icon-]{font-family:icomoon!important;speak:none;font-style:normal;font-weight:400;font-variant:normal;text-transform:none;line-height:1;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.mett__icon-facebook2:before{content:"\e900"}.mett__icon-instagram:before{content:"\e901"}.mett__icon-twitter:before{content:"\e902"}.mett__container-main{min-width:304px!important}.mett__layout,.mett__layout-column,.mett__layout-row{box-sizing:border-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-display:flex}.mett__layout-wrap{-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap}.mett__layout-row{flex-direction:row;-webkit-flex-direction:row;-ms-direction:row}.mett__justify-center{justify-content:center;-webkit-justify-content:center}.mett__justify-start{justify-content:flex-start;-webkit-justify-content:flex-start}.mett__justify-end{justify-content:flex-end;-webkit-justify-content:flex-end}.mett__justify-space-between{justify-content:space-between;-webkit-justify-content:space-between}.mett__justify-space-around{justify-content:space-around;-webkit-justify-content:space-around}.mett__align-start{align-items:flex-start;-webkit-align-items:flex-start}.mett__align-end{align-items:flex-end;-webkit-align-items:flex-end}.mett__align-center{align-items:center;-webkit-align-items:center}.mett__align-stretch{align-items:stretch;-webkit-align-items:stretch}.mett__align-baseline{align-items:baseline;-webkit-align-items:baseline}.mett__align-all-center{align-content:center;-webkit-align-content:center}.mett__align-all-start{align-content:flex-start;-webkit-align-content:flex-start}.mett__align-all-end{align-content:flex-end;-webkit-align-content:flex-end}.mett__align-all-space-between{align-content:space-between;-webkit-align-content:space-between}.mett__align-all-space-around{align-content:space-around;-webkit-align-content:space-around}@media screen and (max-width:319px){.mett__container-main{border:1px solid orange;display:none}.mett__msj-not-resolution{display:block;font-family:HelveticaNeueLT-Light;color:#28cad6;text-align:center;font-size:20px;margin:6em 0}}@media (min-width:320px){.mett__msj-not-resolution{display:none}.mett__text-align-gt{text-align:center}.mett__order-gt-1{order:1;-webkit-order:1}.mett__order-gt-2{order:2;-webkit-order:2}.mett__order-gt-3{order:3;-webkit-order:3}.mett__order-gt-4{order:4;-webkit-order:4}.mett__main-text1{font-size:10vw}.mett__second-text1{font-size:3.5vw;padding:.1em 0 .6em;opacity:.9}.mett__flex-gt-hide{display:none}.mett__flex-gt-5{-webkit-flex:1 1 5%;-ms-flex:1 1 5%;flex:1 1 5%;max-width:5%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-10{-webkit-flex:1 1 10%;-ms-flex:1 1 10%;flex:1 1 10%;max-width:10%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-15{-webkit-flex:1 1 15%;-ms-flex:1 1 15%;flex:1 1 15%;max-width:15%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-20{-webkit-flex:1 1 20%;-ms-flex:1 1 20%;flex:1 1 20%;max-width:20%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-25{-webkit-flex:1 1 25%;-ms-flex:1 1 25%;flex:1 1 25%;max-width:25%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-30{-webkit-flex:1 1 30%;-ms-flex:1 1 30%;flex:1 1 30%;max-width:30%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-35{-webkit-flex:1 1 35%;-ms-flex:1 1 35%;flex:1 1 35%;max-width:35%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-40{-webkit-flex:1 1 40%;-ms-flex:1 1 40%;flex:1 1 40%;max-width:40%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-45{-webkit-flex:1 1 45%;-ms-flex:1 1 45%;flex:1 1 45%;max-width:45%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-50{-webkit-flex:1 1 50%;-ms-flex:1 1 50%;flex:1 1 50%;max-width:50%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-55{-webkit-flex:1 1 55%;-ms-flex:1 1 55%;flex:1 1 55%;max-width:55%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-60{-webkit-flex:1 1 60%;-ms-flex:1 1 60%;flex:1 1 60%;max-width:60%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-65{-webkit-flex:1 1 65%;-ms-flex:1 1 65%;flex:1 1 65%;max-width:65%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-70{-webkit-flex:1 1 70%;-ms-flex:1 1 70%;flex:1 1 70%;max-width:70%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-75{-webkit-flex:1 1 75%;-ms-flex:1 1 75%;flex:1 1 75%;max-width:75%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-80{-webkit-flex:1 1 80%;-ms-flex:1 1 80%;flex:1 1 80%;max-width:80%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-85{-webkit-flex:1 1 85%;-ms-flex:1 1 85%;flex:1 1 85%;max-width:85%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-90{-webkit-flex:1 1 90%;-ms-flex:1 1 90%;flex:1 1 90%;max-width:90%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-95{-webkit-flex:1 1 95%;-ms-flex:1 1 95%;flex:1 1 95%;max-width:95%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-gt-100{-webkit-flex:1 1 100%;-ms-flex:1 1 100%;flex:1 1 100%;max-width:100%;max-height:100%;box-sizing:border-box;word-wrap:break-word}}@media (min-width:600px){.mett__msj-not-resolution{display:none}.mett__text-align-xs{text-align:center}.mett__order-xs-1{order:1;-webkit-order:1}.mett__order-xs-2{order:2;-webkit-order:2}.mett__order-xs-3{order:3;-webkit-order:3}.mett__order-xs-4{order:4;-webkit-order:4}.mett__main-text1{font-size:37px}.mett__second-text1{font-size:20px;padding:.1em 0 .6em;opacity:.9}.mett__flex-xs-hide{display:none}.mett__flex-xs-5{-webkit-flex:1 1 5%;-ms-flex:1 1 5%;flex:1 1 5%;max-width:5%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-10{-webkit-flex:1 1 10%;-ms-flex:1 1 10%;flex:1 1 10%;max-width:10%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-15{-webkit-flex:1 1 15%;-ms-flex:1 1 15%;flex:1 1 15%;max-width:15%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-20{-webkit-flex:1 1 20%;-ms-flex:1 1 20%;flex:1 1 20%;max-width:20%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-25{-webkit-flex:1 1 25%;-ms-flex:1 1 25%;flex:1 1 25%;max-width:25%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-30{-webkit-flex:1 1 30%;-ms-flex:1 1 30%;flex:1 1 30%;max-width:30%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-35{-webkit-flex:1 1 35%;-ms-flex:1 1 35%;flex:1 1 35%;max-width:35%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-40{-webkit-flex:1 1 40%;-ms-flex:1 1 40%;flex:1 1 40%;max-width:40%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-45{-webkit-flex:1 1 45%;-ms-flex:1 1 45%;flex:1 1 45%;max-width:45%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-50{-webkit-flex:1 1 50%;-ms-flex:1 1 50%;flex:1 1 50%;max-width:50%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-55{-webkit-flex:1 1 55%;-ms-flex:1 1 55%;flex:1 1 55%;max-width:55%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-60{-webkit-flex:1 1 60%;-ms-flex:1 1 60%;flex:1 1 60%;max-width:60%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-65{-webkit-flex:1 1 65%;-ms-flex:1 1 65%;flex:1 1 65%;max-width:65%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-70{-webkit-flex:1 1 70%;-ms-flex:1 1 70%;flex:1 1 70%;max-width:70%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-75{-webkit-flex:1 1 75%;-ms-flex:1 1 75%;flex:1 1 75%;max-width:75%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-80{-webkit-flex:1 1 80%;-ms-flex:1 1 80%;flex:1 1 80%;max-width:80%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-85{-webkit-flex:1 1 85%;-ms-flex:1 1 85%;flex:1 1 85%;max-width:85%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-90{-webkit-flex:1 1 90%;-ms-flex:1 1 90%;flex:1 1 90%;max-width:90%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-95{-webkit-flex:1 1 95%;-ms-flex:1 1 95%;flex:1 1 95%;max-width:95%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-xs-100{-webkit-flex:1 1 100%;-ms-flex:1 1 100%;flex:1 1 100%;max-width:100%;max-height:100%;box-sizing:border-box;word-wrap:break-word}}@media (min-width:768px){.mett__msj-not-resolution{display:none}.mett__text-align-sm{text-align:center}.mett__order-sm-1{order:1;-webkit-order:1}.mett__order-sm-2{order:2;-webkit-order:2}.mett__order-sm-3{order:3;-webkit-order:3}.mett__order-sm-4{order:4;-webkit-order:4}.mett__main-text3{font-size:48px}.mett__second-text3{font-size:20px;padding:.1em 0 .6em;opacity:.9}.mett__logo{width:70px}.mett__flex-sm-5{-webkit-flex:1 1 5%;-ms-flex:1 1 5%;flex:1 1 5%;max-width:5%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-10{-webkit-flex:1 1 10%;-ms-flex:1 1 10%;flex:1 1 10%;max-width:10%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-15{-webkit-flex:1 1 15%;-ms-flex:1 1 15%;flex:1 1 15%;max-width:15%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-20{-webkit-flex:1 1 20%;-ms-flex:1 1 20%;flex:1 1 20%;max-width:20%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-25{-webkit-flex:1 1 25%;-ms-flex:1 1 25%;flex:1 1 25%;max-width:25%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-30{-webkit-flex:1 1 30%;-ms-flex:1 1 30%;flex:1 1 30%;max-width:30%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-35{-webkit-flex:1 1 35%;-ms-flex:1 1 35%;flex:1 1 35%;max-width:35%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-40{-webkit-flex:1 1 40%;-ms-flex:1 1 40%;flex:1 1 40%;max-width:40%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-45{-webkit-flex:1 1 45%;-ms-flex:1 1 45%;flex:1 1 45%;max-width:45%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-50{-webkit-flex:1 1 50%;-ms-flex:1 1 50%;flex:1 1 50%;max-width:50%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-55{-webkit-flex:1 1 55%;-ms-flex:1 1 55%;flex:1 1 55%;max-width:55%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-60{-webkit-flex:1 1 60%;-ms-flex:1 1 60%;flex:1 1 60%;max-width:60%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-65{-webkit-flex:1 1 65%;-ms-flex:1 1 65%;flex:1 1 65%;max-width:65%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-70{-webkit-flex:1 1 70%;-ms-flex:1 1 70%;flex:1 1 70%;max-width:70%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-75{-webkit-flex:1 1 75%;-ms-flex:1 1 75%;flex:1 1 75%;max-width:75%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-80{-webkit-flex:1 1 80%;-ms-flex:1 1 80%;flex:1 1 80%;max-width:80%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-85{-webkit-flex:1 1 85%;-ms-flex:1 1 85%;flex:1 1 85%;max-width:85%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-90{-webkit-flex:1 1 90%;-ms-flex:1 1 90%;flex:1 1 90%;max-width:90%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-95{-webkit-flex:1 1 95%;-ms-flex:1 1 95%;flex:1 1 95%;max-width:95%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-100{-webkit-flex:1 1 100%;-ms-flex:1 1 100%;flex:1 1 100%;max-width:100%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-sm-hide{display:none}}@media (min-width:992px){.mett__msj-not-resolution{display:none}.mett__flex-md-show{display:block}.mett__text-align-md{text-align:left}.mett__order-md-1{order:1;-webkit-order:1}.mett__order-md-2{order:2;-webkit-order:2}.mett__order-md-3{order:3;-webkit-order:3}.mett__order-md-4{order:4;-webkit-order:4}.mett__main-text2{font-size:52px}.mett__second-text2{font-size:23px;padding:.1em 0 .6em;opacity:.9}.mett__flex-md-100{-webkit-flex:1 1 100%;-ms-flex:1 1 100%;flex:1 1 100%;max-width:100%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-5{-webkit-flex:1 1 5%;-ms-flex:1 1 5%;flex:1 1 5%;max-width:5%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-10{-webkit-flex:1 1 10%;-ms-flex:1 1 10%;flex:1 1 10%;max-width:10%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-15{-webkit-flex:1 1 15%;-ms-flex:1 1 15%;flex:1 1 15%;max-width:15%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-20{-webkit-flex:1 1 20%;-ms-flex:1 1 20%;flex:1 1 20%;max-width:20%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-25{-webkit-flex:1 1 25%;-ms-flex:1 1 25%;flex:1 1 25%;max-width:25%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-30{-webkit-flex:1 1 30%;-ms-flex:1 1 30%;flex:1 1 30%;max-width:30%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-35{-webkit-flex:1 1 35%;-ms-flex:1 1 35%;flex:1 1 35%;max-width:35%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-40{-webkit-flex:1 1 40%;-ms-flex:1 1 40%;flex:1 1 40%;max-width:40%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-45{-webkit-flex:1 1 45%;-ms-flex:1 1 45%;flex:1 1 45%;max-width:45%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-50{-webkit-flex:1 1 50%;-ms-flex:1 1 50%;flex:1 1 50%;max-width:50%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-55{-webkit-flex:1 1 55%;-ms-flex:1 1 55%;flex:1 1 55%;max-width:55%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-60{-webkit-flex:1 1 60%;-ms-flex:1 1 60%;flex:1 1 60%;max-width:60%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-65{-webkit-flex:1 1 65%;-ms-flex:1 1 65%;flex:1 1 65%;max-width:65%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-70{-webkit-flex:1 1 70%;-ms-flex:1 1 70%;flex:1 1 70%;max-width:70%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-75{-webkit-flex:1 1 75%;-ms-flex:1 1 75%;flex:1 1 75%;max-width:75%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-80{-webkit-flex:1 1 80%;-ms-flex:1 1 80%;flex:1 1 80%;max-width:80%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-85{-webkit-flex:1 1 85%;-ms-flex:1 1 85%;flex:1 1 85%;max-width:85%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-90{-webkit-flex:1 1 90%;-ms-flex:1 1 90%;flex:1 1 90%;max-width:90%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-md-95{-webkit-flex:1 1 95%;-ms-flex:1 1 95%;flex:1 1 95%;max-width:95%;max-height:100%;box-sizing:border-box;word-wrap:break-word}}@media (min-width:1200px){.mett__msj-not-resolution{display:none}.mett__flex-lg-show{display:block}.mett__text-align-lg{text-align:left}.mett__order-lg-1{order:1;-webkit-order:1}.mett__order-lg-2{order:2;-webkit-order:2}.mett__order-lg-3{order:3;-webkit-order:3}.mett__order-lg-4{order:4;-webkit-order:4}.mett__main-text1{font-size:55px}.mett__second-text1{font-size:26px;padding:.1em 0 .6em;opacity:.9}.mett__flex-lg-5{-webkit-flex:1 1 5%;-ms-flex:1 1 5%;flex:1 1 5%;max-width:5%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-10{-webkit-flex:1 1 10%;-ms-flex:1 1 10%;flex:1 1 10%;max-width:10%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-15{-webkit-flex:1 1 15%;-ms-flex:1 1 15%;flex:1 1 15%;max-width:15%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-20{-webkit-flex:1 1 20%;-ms-flex:1 1 20%;flex:1 1 20%;max-width:20%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-25{-webkit-flex:1 1 25%;-ms-flex:1 1 25%;flex:1 1 25%;max-width:25%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-30{-webkit-flex:1 1 30%;-ms-flex:1 1 30%;flex:1 1 30%;max-width:30%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-35{-webkit-flex:1 1 35%;-ms-flex:1 1 35%;flex:1 1 35%;max-width:35%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-40{-webkit-flex:1 1 40%;-ms-flex:1 1 40%;flex:1 1 40%;max-width:40%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-45{-webkit-flex:1 1 45%;-ms-flex:1 1 45%;flex:1 1 45%;max-width:45%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-50{-webkit-flex:1 1 50%;-ms-flex:1 1 50%;flex:1 1 50%;max-width:50%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-55{-webkit-flex:1 1 55%;-ms-flex:1 1 55%;flex:1 1 55%;max-width:55%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-60{-webkit-flex:1 1 60%;-ms-flex:1 1 60%;flex:1 1 60%;max-width:60%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-65{-webkit-flex:1 1 65%;-ms-flex:1 1 65%;flex:1 1 65%;max-width:65%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-70{-webkit-flex:1 1 70%;-ms-flex:1 1 70%;flex:1 1 70%;max-width:70%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-75{-webkit-flex:1 1 75%;-ms-flex:1 1 75%;flex:1 1 75%;max-width:75%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-80{-webkit-flex:1 1 80%;-ms-flex:1 1 80%;flex:1 1 80%;max-width:80%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-85{-webkit-flex:1 1 85%;-ms-flex:1 1 85%;flex:1 1 85%;max-width:85%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-90{-webkit-flex:1 1 90%;-ms-flex:1 1 90%;flex:1 1 90%;max-width:90%;max-height:100%;box-sizing:border-box;word-wrap:break-word}.mett__flex-lg-95{-webkit-flex:1 1 95%;-ms-flex:1 1 95%;flex:1 1 95%;max-width:95%;max-height:100%;box-sizing:border-box;word-wrap:break-word}}.mett__titulo-ficha span{text-align:center;font-size:16px;margin:0 auto;display:block}.mett__mod-inline{display:inline-block;vertical-align:middle;text-align:center}.mett__mod-section{padding:1em 0;background:-moz-radial-gradient(center,ellipse cover,#fff 0,#fff 44%,rgba(255,255,255,0) 100%);background:-webkit-radial-gradient(center,ellipse cover,#fff 0,#fff 44%,rgba(255,255,255,0) 100%);background:radial-gradient(ellipse at center,#fff 0,#fff 44%,rgba(255,255,255,0) 100%);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffff', endColorstr='#00ffffff', GradientType=1)}.mett__mod-section.mett__inner-section{margin:1em 0}.mett__borde{border:1px solid red}.mett__mod-texto{margin:1.5em 0}.mett__content-img-big{overflow:hidden;text-align:center}.mett__content-img-big img{width:90%}.mett__content-img-small{overflow:hidden;border-radius:16px;-webkit-border-radius:16px}.mett__shadow-box{-webkit-box-shadow:7px 7px 1px 0 rgba(50,50,50,.15);-moz-box-shadow:7px 7px 1px 0 rgba(50,50,50,.15);box-shadow:7px 7px 1px 0 rgba(50,50,50,.15);-webkit-border-radius:16px;-moz-border-radius:16px;-ms-border-radius:16px;-o-border-radius:16px}.mett__content-img-small img{width:100%}img.mett__image-ficha{width:100%}.mett__uppercase{text-transform:uppercase}

			/* STYLES WITH VARIABLES */
			.mett__contenedor-ficha{background: url(img/OTROS/lenovo_pattern-02.png) no-repeat center center fixed; -webkit-background-size: cover; -moz-background-size: cover; -o-background-size: cover; background-size: cover; border: 1px solid #eee; border-radius: 4px; padding:0; font-family: "Helvetica Neue",Helvetica,Arial,sans-serif; color: rgba(0,0,0,0.6) !important; font-size: initial !important; line-height: initial !important; }
			p.mett__parrafo{margin: 0; font-size: 22px; width: 100%; text-align: center; margin-top:.5em !important}
			.mett__cont-circle-number{background-color:${color_secundario}; width: 56px; height: 56px; margin: 0.5em 0em; color: white; font-family: Arial; font-weight: bold; font-size: 30px; text-align: center; border-radius: 10em; -webkit-border-radius: 10em; -moz-border-radius: 10em; -ms-border-radius: 10em; -o-border-radius: 10em; }
			.mett__cont-t-cabecera, .mett__titulo-descripcion-main, .mett__titulo-caracteristica{font-family: 'HelveticaNeue-Thin', Helvetica, arial, sans-serif; text-align: center;}
			.mett__cont-t-cabecera{background-color: ${color_primario}; color: white; border-radius: 10px; }
			.mett__separador-info-t-cabecera{background:${color_secundario}; height:3px; }
			.mett__titulo-descripcion-main{color: ${color_secundario}; font-size: 45px !important; text-transform: uppercase; line-height: 51px; }
			.mett__titulo-caracteristica{color: ${color_caracteristica}; font-size: 30px !important; }
			.mett__cont-icon-footer{padding:0em 0.5em; font-size:1.8em; text-decoration: none; -webkit-transition: all 0.28s ease-in-out; -moz-transition: all 0.28s ease-in-out; -o-transition: all 0.28s ease-in-out; transition: all 0.28s ease-in-out; }

		</style>
'''


templates['cabecera'] = '''
		<!-- CONTENEDOR DE LA FICHA -->
		<div class="mett__contenedor-ficha">
			<section class="mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-center">
				<div class="mett__container-main mett__flex-lg-90 mett__flex-md-85 mett__flex-sm-95 mett__flex-xs-95 mett__flex-gt-95" style="padding: 2vh 0vh;">
					


					<!-- CABECERA -->
					<section class="mett__layout-row mett__layout-wrap mett__align-start">
						
						<div class="mett__flex-lg-100 mett__flex-md-100 mett__flex-sm-100 mett__flex-xs-100 mett__flex-gt-100 mett__layout-row mett__layout-wrap mett__justify-space-between">
							<div class="mett__flex-lg-80 mett__flex-md-80 mett__flex-sm-85 mett__flex-xs-85 mett__flex-gt-90 mett__layout-row mett__layout-wrap mett__justify-start mett__align-start">
								<div class="mett__flex-lg-100 mett__flex-md-100 mett__flex-sm-100 mett__flex-xs-100 mett__flex-gt-100 mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-center mett__cont-t-cabecera">
									<!-- Contenedor titulo principal -->
									<div class="mett__flex-lg-95 mett__flex-md-95 mett__flex-xs-95 mett__flex-xs-95 mett__flex-gt-95 mett__uppercase mett__main-text1 mett__main-text2 mett__main-text3" style="text-align:center;">		
										${nombre_producto}
									</div>
									<div class="mett__flex-lg-95 mett__flex-md-95 mett__flex-xs-95 mett__flex-xs-95 mett__flex-gt-95 mett__separador-info-t-cabecera"></div>
									<div class="mett__flex-lg-95 mett__flex-md-95 mett__flex-xs-95 mett__flex-xs-95 mett__flex-gt-95 mett__uppercase mett__second-text1 mett__second-text2 mett__second-text3" style="text-align:center;">
										${subtitulo_cabecera}
									</div>
								</div>
							</div>
							<!-- Logo Lenovo -->
							<div class="mett__flex-lg-10 mett__flex-md-15 mett__flex-sm-15 mett__flex-xs-10 mett__flex-gt-10 mett__layout-row mett__layout-wrap mett__justify-end">
								<div><img class="mett__image-ficha mett__logo" src="${logo_lenovo}"></div>
							</div>
						</div>
					</section>
'''

templates['P'] = '''

					<!-- ESTRUCTURA DE INFORMACIÓN P -->

					<section class="mett__flex-lg-100 mett__flex-md-100 mett__flex-sm-100 mett__flex-xs-100 mett__flex-gt-100 mett__layout-row mett__justify-center mett__mod-section" style="margin:3em 0em;">
						<div class="mett__inner-section mett__flex-lg-70 mett__flex-sm-80 mett__flex-xs-80 mett__flex-gt-90">
							<div class="mett__layout-row mett__justify-center mett__align-center">
								<span class="mett__titulo-descripcion-main">${t_descripcion_principal}</span>
							</div>
							<p class="mett__parrafo" style="margin-top:1em;">
								${p_descripcion_principal}
							</p>
						</div>
					</section>


'''

templates['I-P'] = '''
					<!-- ESTRUCTURA DE INFORMACIÓN I | P-->

					<section class="mett__mod-section mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-center">
						<div class="mett__flex-lg-45 mett__flex-md-45 mett__flex-45 mett__flex-sm-55 mett__flex-xs-70 mett__flex-gt-70  mett__content-img-small mett__shadow-box mett__order-lg-1 mett__order-md-1 mett__order-sm-2 mett__order-xs-2 mett__order-gt-2">
							<img class="mett__image-ficha" src="${img_apoyo}">
						</div>
						<div class="mett__flex-lg-45 mett__flex-md-45 mett__flex-45 mett__flex-sm-80 mett__flex-xs-80 mett__flex-gt-90 mett__mod-texto mett__order-lg-2 mett__order-md-2 mett__order-sm-1 mett__order-xs-1 mett__order-gt-1">
							<!-- MOD. P -->
							<div class="mett__mod-p">
								<div class="mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-start mod__mod-texto">
									<div class="mett__flex-lg-75 mett__flex-md-80 mett__order-lg-1 mett__order-md-1 mett__order-sm-2 mett__order-xs-2 mett__order-gt-2">
										<div class="mett__titulo-caracteristica  mett__layout-row mett__justify-center mett__align-center">
											<span>${t_caracteristica}</span>
										</div>
										<p class="mett__parrafo">${p_caracteristica}</p>
									</div>
									<div class="mett__flex-lg-15 mett__flex-md-20 mett__flex-sm-100  mett__layout-row mett__justify-center mett__align-center mett__order-lg-2 mett__order-md-2 mett__order-sm-1  mett__order-xs-1 mett__order-gt-1 ">
										<div class="mett__cont-circle-number mett__layout-row mett__justify-center mett__align-center">
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

					<section class="mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-center mett__mod-section" style="margin-top:2em;">
						<div class=" mett__inner-section mett__flex-lg-40 mett__flex-md-45 mett__flex-sm-60 mett__flex-xs-70 mett__flex-gt-70 mett__content-img-small" style="text-align:center;">
							<img class="mett__image-ficha" src="${img_apoyo}">
						</div>
					</section>
'''


templates['P-I-I'] = '''

					<!-- ESTRUCTURA DE INFORMACIÓN P | I | I -->
					
					<section class="mett__mod-section mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-center">
						<div class="mett__inner-section mett__flex-lg-50 mett__flex-md-50 mett__flex-sm-85 mett__flex-xs-80 mett__flex-gt-90 mett__justify-center mett__align-stretch">
							<!-- MOD. P -->
							<div class="mett__mod-p">
								<div class="mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-start mett__mod-texto">
									<div class="mett__flex-lg-15 mett__flex-md-20 mett__flex-sm-100 mett__layout-row mett__justify-center mett__align-center">
										<div class="mett__cont-circle-number mett__layout-row mett__justify-center mett__align-center">
											<div>${numero_caracteristica}</div>
										</div>
									</div>
									<div class="mett__flex-lg-75 mett__flex-md-80 mett__flex-sm-100">
										<div class="mett__titulo-caracteristica  mett__layout-row mett__justify-center mett__align-center">
											<span>${t_caracteristica}</span>
										</div>
										<p class="mett__parrafo">${p_caracteristica}</p>
									</div>
								</div>
							</div>
							<div class="mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-center">
								<div class="mett__flex-lg-15 mett__flex-md-15 mett__flex-lg-show mett__flex-md-show mett__flex-sm-hide mett__flex-xs-hide mett__flex-gt-hide"></div>
								<div class="mett__flex-lg-75 mett__flex-md-75 mett__flex-sm-55 mett__flex-xs-70 mett__flex-gt-75 mett__content-img-small">
									<img class="mett__image-ficha" src="${img_apoyo_1}">
								</div>
							</div>
						</div>
						<div class="mett__inner-section mett__flex-lg-40 mett__flex-md-40 mett__flex-sm-50 mett__flex-xs-55 mett__flex-gt-60 mett__content-img-big">
								<img class="mett__image-ficha" src="${img_apoyo_2}">
						</div>
					</section>
'''

templates['I-IP-I'] = '''

					<!-- ESTRUCTURA DE INFORMACIÓN I | I P | I -->

					<section class="mett__mod-section mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-center">
						<div class="mett__inner-section mett__flex-lg-25 mett__flex-md-25 mett__flex-sm-55 mett__flex-xs-55 mett__flex-gt-60 mett__content-img-small mett__shadow-box mett__order-lg-1 mett__order-md-1 mett__order-sm-2 mett__order-xs-2 mett__order-gt-2">
							<img class="mett__image-ficha" src="${img_apoyo_1}">
						</div>
						<div class="mett__inner-section mett__layout-row mett__layout-wrap mett__flex-lg-45 mett__flex-md-45 mett__flex-sm-80 mett__flex-xs-80 mett__flex-gt-90 mett__order-lg-2 mett__order-md-2 mett__order-sm-1 mett__order-xs-1 mett__order-gt-1">
							
							<div class="mett__layout-row mett__layout-wrap mett__flex-lg-100 mett__flex-md-100 mett__flex-sm-100 mett__flex-xs-100 mett__justify-space-around mett__align-center mett__order-lg-1 mett__order-md-1 mett__order-sm-2 mett__order-xs-2 mett__order-gt-2">
								<div class="mett__flex-lg-80 mett__flex-md-100 mett__flex-sm-80 mett__flex-xs-80 mett__flex-gt-85" style="text-align:center;">
									<img class="mett_image-ficha" src="${img_apoyo_2}">
								</div>
							</div>
							<!-- MOD. P -->
							<div class="mett__flex-lg-100 mett__flex-md-100 mett__flex-sm-100 mett__flex-xs-100 mett__flex-gt-100 mett__mod-p mett__order-lg-2 mett__order-md-2 mett__order-sm-1 mett__order-xs-1 mett__order-gt-1">
								<div class="mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-start mett__mod-texto">
									<div class="mett__layout-row mett__layout-wrap mett__flex-lg-15 mett__flex-md-20 mett__flex-sm-100 mett__flex-xs-100 mett__flex-gt-100 mett__justify-center mett__align-center">
										<div class="mett__cont-circle-number mett__layout-row mett__justify-center mett__align-center">
											<div>${numero_caracteristica}</div>
										</div>
									</div>
									<div class="mett__flex-lg-75 mett__flex-md-75 mett__flex-sm-100 mett__flex-xs-80 mett__flex-gt-100">
										<div class="mett__titulo-caracteristica  mett__layout-row mett__justify-center mett__align-center">
											<span>${t_caracteristica}</span>
										</div>
										<p class="mett__parrafo">${p_caracteristica}</p>
									</div>
								</div>
							</div>
						</div>
						<div class="mett__inner-section mett__flex-lg-20 mett__flex-md-15 mett__flex-sm-55 mett__flex-xs-55 mett__flex-gt-60 mett__content-img-small mett__order-md-3 mett__order-sm-3 mett__order-xs-3 mett__order-gt-3">
							 <img class="mett__image-ficha" src="${img_apoyo_3}">
						</div>
					</section>

'''

templates['P-I-num_centro'] = '''

					<!-- ESTRUCTURA DE INFORMACIÓN P | I NUMERO CENTRO-->
					
					<section class="mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-center mett__mod-section">
						<div class="mett__flex-lg-45 mett__flex-md-45 mett__flex-45 mett__flex-sm-80 mett__flex-xs-80 mett__flex-gt-90  mett__mod-texto">
							<!-- MOD. P -->
							<div class="mett__mod-p">
								<div class="mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-start mod-texto">
									<div class="mett__flex-lg-75 mett__flex-md-80 mett__order-lg-1 mett__order-md-1 mett__order-sm-2  mett__order-xs-2 mett__order-gt-2">
										<div class="mett__titulo-caracteristica  mett__layout-row mett__justify-center mett__align-center">
											<span>${t_caracteristica}</span>
										</div>
										<p class="mett__parrafo">${p_caracteristica}</p>
									</div>
									<div class="mett__flex-lg-15 mett__flex-md-20 mett__flex-sm-100  mett__layout-row mett__layout-wrap mett__justify-center mett__align-center mett__order-lg-2 mett__order-md-2 mett__order-sm-1  mett__order-xs-1 mett__order-gt-1">
										<div class="mett__cont-circle-number mett__layout-row mett__justify-center mett__align-center">
											<div>${numero_caracteristica}</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						<div class="mett__flex-lg-45 mett__flex-md-45 mett__flex-45 mett__flex-sm-55 mett__flex-xs-70 mett__flex-gt-70 mett__content-img-small">
							<img class="mett__image-ficha" src="${img_apoyo}">
						</div>
					</section>

'''
templates['P-I-num_izq'] = '''
					<!-- ESTRUCTURA DE INFORMACIÓN P | I NUMERO IZQ -->
					
					<section class="mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-center mett__mod-section">
						<div class="mett__flex-lg-45 mett__flex-md-45 mett__flex-45 mett__flex-sm-80 mett__flex-xs-80 mett__flex-gt-90  mett__mod-texto">
							<!-- MOD. P -->
							<div class="mett__mod-p">
								<div class="mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-start mett__mod-texto">
									<div class="mett__flex-lg-15 mett__flex-md-20 mett__flex-sm-100  mett__layout-row mett__layout-wrap mett__justify-center mett__align-center">
										<div class="mett__cont-circle-number mett__layout-row mett__justify-center mett__align-center">
											<div>${numero_caracteristica}</div>
										</div>
									</div>
									<div class="mett__flex-lg-75 mett__flex-md-80">
										<div class="mett__titulo-caracteristica  mett__layout-row mett__justify-center mett__align-center">
											<span>${t_caracteristica}</span>
										</div>
										<p class="mett__parrafo">${p_caracteristica}</p>
									</div>
								</div>
							</div>
						</div>
						<div class="mett__flex-lg-45 mett__flex-md-45 mett__flex-45 mett__flex-sm-55 mett__flex-xs-70 mett__flex-gt-70 mett__content-img-small">
							<img class="mett__image-ficha" src="${img_apoyo}">
						</div>
					</section>
'''
templates['I-I'] = '''

					<!-- ESTRUCTURA DE INFORMACIÓN I | I  -->

					<section class="mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-center mett__mod-section" style="margin-top:2em;">
						<div class=" mett__inner-section mett__flex-lg-40 mett__flex-md-45 mett__flex-sm-60 mett__flex-xs-70 mett__flex-gt-70 mett__content-img-small" style="text-align:center;">
							<img class="mett__image-ficha" src="${img_apoyo_1}">
						</div>

						<div class=" mett__inner-section mett__flex-lg-40 mett__flex-md-45 mett__flex-sm-60 mett__flex-xs-70 mett__flex-gt-70 mett__content-img-small" style="text-align:center;">
							<img class="mett__image-ficha" src="${img_apoyo_2}">
						</div>
					</section>
					
'''

templates['I-P-I'] = '''

					<!-- ESTRUCTURA DE INFORMACIÓN I | P | I -->

					<section class="mett__mod-section mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-center">
						<div class="mett__inner-section mett__flex-lg-25 mett__flex-md-25 mett__flex-sm-50 mett__flex-xs-70 mett__flex-gt-70 mett__content-img-small mett__shadow-box mett__order-lg-1 mett__order-md-1 mett__order-sm-2 mett__order-xs-2 mett__order-gt-2">
							<img class="mett__image-ficha" src="${img_apoyo_1}">
						</div>
						<div class="mett__inner-section mett__flex-lg-45 mett__flex-md-45 mett__flex-sm-80 mett__flex-xs-80 mett__flex-gt-90 mett__order-lg-2 mett__order-md-2 mett__order-sm-1 mett__order-xs-1 mett__order-gt-1">
							<!-- MOD. P -->
							<div class="mett__mod-p">
								<div class="mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-start mett__mod-texto">
									<div class="mett__flex-lg-15 mett__flex-md-20 mett__flex-sm-100 mett__flex-xs-100 mett__flex-gt-100 mett__layout-row mett__layout-wrap mett__justify-center mett__align-center">
										<div class="mett__cont-circle-number mett__layout-row mett__justify-center mett__align-center">
											<div>${numero_caracteristica}</div>
										</div>
									</div>
									<div class="mett__flex-lg-75 mett__flex-md-75 mett__flex-sm-100 mett__flex-xs-100 mett__flex-gt-100">
										<div class="mett__titulo-caracteristica  mett__layout-row mett__justify-center mett__align-center">
											<span>${t_caracteristica}</span>
										</div>
										<p class="mett__parrafo">${p_caracteristica}</p>
									</div>
								</div>
							</div>
						</div>
						<div class="mett__inner-section mett__flex-lg-20 mett__flex-md-15 mett__flex-sm-55 mett__flex-xs-55 mett__flex-gt-70 mett__content-img-small mett__order-lg-3 mett__order-md-2 mett__order-sm-3 mett__order-xs-3 mett__order-gt-3">
							 <img class="mett__image-ficha" src="${img_apoyo_2}">
						</div>
					</section>
'''

templates['P-P'] = '''
					<!-- ESTRUCTURA DE INFORMACIÓN P | P -->

					<section class="mett__mod-section mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-start">
						<div class="mett__inner-section mett__flex-lg-45 mett__flex-md-45 mett__flex-sm-80 mett__flex-xs-80 mett__flex-gt-90">
							<div class="mett__mod-list mett__layout-row mett__layout-wrap mett__justify-center mett__align-start">
								<!-- Logo-especificación -->
								<div class="mett__layout-row mett__layout-wrap mett__justify-center mett__align-start mett__flex-lg-30 mett__flex-md-30 mett__flex-sm-90 mett__flex-xs-90 mett__flex-gt-100">
									<img class="mett__image-ficha" style="max-width:110px;max-height:102px;" src="${icono_caracteristica_1}">
								</div>
								<!-- Parrafo-especificación -->
								<div class="mett__flex-lg-70 mett__flex-md-70 mett__flex-sm-100 mett__flex-xs-100 mett__flex-gt-100">
									<p class="mett__parrafo" class="mett__text-align-lg mett__text-align-md mett__text-align-sm mett__text-align-xs mett__text-align-gt">${detalle_caracteristica_1}</p>
								</div>
							</div>
						</div>
						<div class="mett__inner-section mett__flex-lg-45 mett__flex-md-45 mett__flex-sm-80 mett__flex-xs-80 mett__flex-gt-90">
							<div class="mett__mod-list mett__layout-row mett__layout-wrap mett__justify-center mett__align-start">
								<!-- Logo-especificación -->
								<div class="mett__layout-row mett__layout-wrap mett__justify-center mett__align-start mett__flex-lg-30 mett__flex-md-30 mett__flex-sm-90 mett__flex-xs-90 mett__flex-gt-100">
									<img class="mett__image-ficha" style="max-width:110px;max-height:102px;" src="${icono_caracteristica_2}">
								</div>
								<!-- Parrafo-especificación -->
								<div class="mett__flex-lg-70 mett__flex-md-70 mett__flex-sm-100 mett__flex-xs-100 mett__flex-gt-100">
									<p class="mett__parrafo" class="mett__text-align-lg mett__text-align-md mett__text-align-sm mett__text-align-xs mett__text-align-gt">${detalle_caracteristica_2}</p>
								</div>
							</div>
						</div>
					</section>

'''

templates['I-P-nonumero'] = '''
					<!-- ESTRUCTURA DE INFORMACIÓN I | P SIN NÚMERO-->

					<section class="mett__mod-section mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-center">
						<div class="mett__flex-lg-45 mett__flex-md-45 mett__flex-45 flex-sm-55 mett__flex-xs-70 flex-gt-70  mett__content-img-small mett__shadow-box mett__order-lg-1 mett__order-md-1 mett__order-sm-2 mett__order-xs-2 mett__order-gt-2">
							<img class="mett__image-ficha" src="${img_apoyo}">
						</div>
						<div class="mett__flex-lg-45 mett__flex-md-45 mett__flex-45 mett__flex-sm-80 mett__flex-xs-80 mett__flex-gt-90  mett__mod-texto mett__order-lg-2 mett__order-md-2 mett__order-sm-1 mett__order-xs-1 mett__order-gt-1">
							<!-- MOD. P -->
							<div class="mett__mod-p">
								<div class="mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-start mett__mod-texto">
									<div class="mett__flex-lg-100 mett__flex-md-90 mett__order-lg-1 mett__order-md-1 mett__order-sm-2 mett__order-xs-2 mett__order-gt-2">
										<p class="mett__parrafo">${p_caracteristica}</p>
									</div>
								</div>
							</div>
						</div>
					</section>	
'''

templates['Igrande-P-I'] = '''
					<!-- ESTRUCTURA DE INFORMACIÓN I GRANDE | P | I   -->
					
					<section class="mett__mod-section mett__layout-row mett__layout-wrap mett__justify-space-around mett__align-start">
						<div class="mett__inner-section mett__flex-lg-40 mett__flex-md-40 mett__flex-sm-50 mett__flex-xs-55 mett__flex-gt-60 mett__content-img-big mett__order-lg-1 mett__order-md-1 mett__order-sm-2 mett__order-xs-2 mett__order-gt-2">
								<img class="mett__image-ficha" src="${img_apoyo_1}">
						</div>
						<div class="mett__inner-section mett__flex-lg-50 mett__flex-md-50 mett__flex-sm-85 mett__flex-xs-80 mett__flex-gt-90 mett__justify-center mett__align-stretch mett__order-lg-2 mett__order-md-2 mett__order-sm-1 mett__order-xs-1 mett__order-gt-1">
							<!-- MOD. P -->
							<div class="mett__mod-p">
								<div class="mett__layout-row mett__layout-wrap mett__layout-wrap mett__justify-space-around mett__align-start mett__mod-texto">
									<div class="mett__flex-lg-100 mett__flex-md-100 mett__flex-sm-100 mett__flex-xs-100 mett__flex-gt-100">
										<p class="mett__parrafo">${p_caracteristica}</p>
									</div>
								</div>
							</div>
							<div class="mett__layout-row mett__layout-wrap mett__layout-wrap mett__justify-space-around mett__align-center">
								<div class="mett__flex-lg-100 mett__flex-md-100 mett__flex-sm-100 mett__flex-xs-100 mett__flex-gt-100 mett__flex-xs-60 mett__flex-gt-80 mett__flex-md-80">
									<img class="mett__image-ficha" src="${img_apoyo_2}">
								</div>
							</div>
						</div>
					</section>
'''

templates['fin'] = '''

					<!-- MÓDULO VIDEO PRODUCTO -->
					<!---->
					<!-- Nota: Si la ficha no requiere el módulo de video 
							descomentariar la instrucción del atributo 
							style borrando > '/*' y '*/'.
					-->
					<section class="mett__mod-section mett__layout-row mett__layout-wrap mett__justify-center mett__align-center" style="/*display:none;*/">
						<!-- container video -->
						<div class="mett__layout-row mett__layout-wrap mett__justify-center mett__contenedor-video mett__flex-lg-90 mett__flex-md-90 mett__flex-sm-80 mett__flex-xs-80 mett__flex-gt-100">
							<!-- Video de ejemplo -->
							<iframe class="mett__iframe" src="https://www.youtube.com/embed/n2AXcV4Yswk" frameborder="0" allowfullscreen></iframe>
						</div>
					</section>

				</div>


				<!-- FOOTER -->
				<footer style="margin:2em 0em;" class="mett__layout-row mett__layout-wrap mett__justify-center mett__align-center mett__flex-lg-90 mett__flex-md-85 mett__flex-sm-95 mett__flex-xs-95 mett__flex-gt-95">
					<div class="mett__layout-row mett__layout-wrap mett__justify-center mett__align-center mett__flex-lg-60 mett__flex-md-60 mett__flex-sm-60 mett__flex-xs-60 mett__flex-gt-60">
						<a class="mett__link" href="https://es-es.facebook.com/LenovoCo">
							<div class="mett__cont-icon-footer mett__facebook">
								<i class="mett__icon-facebook2"></i>
							</div>
						</a>
						<a class="mett__link" href="https://twitter.com/lenovocolombia?lang=es">
							<div class="mett__cont-icon-footer mett__twitter">
								<i class="mett__icon-twitter"></i>
							</div>
						</a>
						<a class="mett__link" href="https://www.instagram.com/lenovocolombia/">
							<div class="mett__cont-icon-footer mett__instagram">
								<i class="mett__icon-instagram"></i>
							</div>
						</a>
					</div>
				</footer>

				<!-- Mensaje en caso de resoluciones demasiado bajas <=319px -->
				<div class="mett__msj-not-resolution">
					<h3>LO SENTIMOS</h3> 
					<p class="mett__parrafo">la resolución de tú dispositivo es demasiado baja.</p>
				</div>
			</section>
		</div>
'''

def generar_ficha(mapa):
    salida = ''
    for seccion in mapa:
        salida = salida + Template(templates[seccion[0]].decode('utf-8')).substitute(seccion[1])
    return salida