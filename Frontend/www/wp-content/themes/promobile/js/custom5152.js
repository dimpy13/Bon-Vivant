( function( $ ) {
    "use strict";
    $(window).load(function() { 
    	$("#status").fadeOut();
    	$("#preloader").delay(100).fadeOut("slow");
    });


    $( document ).ready(function() {

        $(function(){
            $('.menu-item').each(function(index, el) {
                if ($(this).hasClass('current-menu-parent')) {
                    $(this).parent().find('.submenu').toggleClass('submenu-active');
                }
            });
        });

        $('.show-submenu').click(function(){
           $(this).parent().find('.submenu').toggleClass('submenu-active'); 
           $(this).toggleClass('submenu-active');       
        });
            
        

        setTimeout(function() {

            function slider_dots(){
                var dots_width = (-($('.owl-dots').width()/2));
                $('.owl-dots').css('position', 'absolute');
                $('.owl-dots').css('left', '50%');
                $('.owl-dots').css('margin-left', dots_width);   
            }      
            slider_dots();

        }, 1);

    	(function(a,b,c){if(c in b&&b[c]){var d,e=a.location,f=/^(a|html)$/i;a.addEventListener("click",function(a){d=a.target;while(!f.test(d.nodeName))d=d.parentNode;"href"in d&&(d.href.indexOf("http")||~d.href.indexOf(e.host))&&(a.preventDefault(),e.href=d.href)},!1)}})(document,window.navigator,"standalone")
        
        $(function() {FastClick.attach(document.body);});
            
        $(function() {
            $(".preload-image").lazyload({
                threshold : 200,
                effect : "fadeIn"
            });
            $("img.lazy").show().lazyload();
        });
        
        //Page Chapters Activation
        $('.show-page-chapters, .hide-chapters').click(function(){
           $('.page-chapters').toggleClass('page-chapters-active'); 
        });
        
        $('.page-chapters a').click(function(){
            $('.page-chapters a').removeClass('active-chapter');
            $(this).addClass('active-chapter');
        });
       
        
        /*Accordion*/
        $('.accordion').find('.accordion-toggle').click(function(){
            $(this).next().slideDown(250);
            $('.accordion').find('i').removeClass('rotate-180');
            $(this).find('i').addClass('rotate-180');

            $(".accordion-content").not($(this).next()).slideUp(200);
        });
            
        /*Classic Toggles*/
        $('.toggle-title').click(function(){
            $(this).parent().find('.toggle-content').slideToggle(200); 
            $(this).find('i').toggleClass('rotate-toggle');
            return false;
        });
        
        /*Notifications*/
        $('.static-notification-close').click(function(){
           $(this).parent().slideUp(200); 
            return false;
        });    
        
        $('.tap-dismiss').click(function(){
           $(this).slideUp(200); 
            return false;
        });
        
        
        /*Sharebox Settings*/
                
            $('.show-share-bottom, .show-share-box').click(function(){
                var url_line = $(this).data('href');
                $('.share-socials-bottom').html('<a href="https://www.facebook.com/sharer/sharer.php?u='+url_line+'/"><i class="fa fa-facebook facebook-color"></i>Facebook</a><a href="https://twitter.com/home?status=Check%20out%20ThemeForest%20'+url_line+'"><i class="fa fa-twitter twitter-color"></i>Twitter</a><a href="https://plus.google.com/share?url='+url_line+'"><i class="fa fa-google-plus google-color"></i>Google</a><a href="https://pinterest.com/pin/create/button/?url='+url_line+'/"><i class="fa fa-pinterest-p pinterest-color"></i>Pinterest</a><a href="whatsapp://send?text='+url_line+'"><i class="fa fa-whatsapp sms-color"></i>Text</a><a href="mailto:?&amp;subject=&amp;body='+url_line+'"><i class="fa fa-envelope-o mail-color"></i>Email</a><div class="clear"></div>')
                $('.share-bottom').toggleClass('active-share-bottom'); 
                $.modal.close()
                return false;
            });    
        
        $('.close-share-bottom').click(function(){
           $('.share-bottom').removeClass('active-share-bottom'); 
            return false;
        });
        
        
        
        /*Switches*/
        
            $('.switch-1').click(function(){
               $(this).toggleClass('switch-1-on'); 
                return false;
            });
            
            $('.switch-2').click(function(){
               $(this).toggleClass('switch-2-on'); 
                return false;
            });
            
            $('.switch-3').click(function(){
               $(this).toggleClass('switch-3-on'); 
                return false;
            });
            
            $('.switch, .switch-icon').click(function(){
                $(this).parent().find('.switch-box-content').slideToggle(200); 
                $(this).parent().find('.switch-box-subtitle').slideToggle(200);
                return false;
            });
        

        
        /*Detecting Mobiles*/
        
        var isMobile = {
            Android: function() {
                return navigator.userAgent.match(/Android/i);
            },
            BlackBerry: function() {
                return navigator.userAgent.match(/BlackBerry/i);
            },
            iOS: function() {
                return navigator.userAgent.match(/iPhone|iPad|iPod/i);
            },
            Opera: function() {
                return navigator.userAgent.match(/Opera Mini/i);
            },
            Windows: function() {
                return navigator.userAgent.match(/IEMobile/i);
            },
            any: function() {
                return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
            }
        };
        
        if(isMobile.any()) {
            //Settings for all mobiles
            $('head').append('<link />');
        } 
        
        if( !isMobile.any() ){
            $('.show-blackberry, .show-ios, .show-windows, .show-android').hide(0);
            $('show-no-detection').show(0);
            
            $('#content').bind('mousewheel', function(event) {
              event.preventDefault();
              var scrollTop = this.scrollTop;
              this.scrollTop = (scrollTop + ((event.deltaY * event.deltaFactor) * -2));
            });
            $("#content").css("overflow-y","hidden");
        }
        
        if(isMobile.Android()) {
            $('.show-android').show(0);
            $('.show-blackberry, .show-ios, .show-windows').hide(0);
        }
            
        if(isMobile.BlackBerry()) {
            $('.show-blackberry').show(0);
            $('.show-android, .show-ios, .show-windows').hide(0);
        }
            
        if(isMobile.iOS()) {
            $('.show-ios').show(0);
            $('.show-blackberry, .show-android, .show-windows').hide(0);
        }
            
        if(isMobile.Windows()) {
            $('.show-windows').show(0);
            $('.show-blackberry, .show-ios, .show-android').hide(0);
        }
        
        $('.back-to-top-badge, .back-to-top').click(function() {
    		$('#content').animate({
    			scrollTop:0
    		}, 500, 'easeInOutQuad');
    		return false;
    	});
        
        //Show Back To Home When Scrolling
            
        $('#content').on('scroll', function () {
            var total_scroll_height = $('#content')[0].scrollHeight
            var inside_header = ($(this).scrollTop() <= 150);
            var passed_header = ($(this).scrollTop() >= 0); //250
            var footer_reached = ($(this).scrollTop() >= (total_scroll_height - ($(window).height() +100 )));
            
            if (inside_header == true) {
                $('.back-to-top-badge').removeClass('back-to-top-badge-visible');
            } else if (passed_header == true)  {
                $('.back-to-top-badge').addClass('back-to-top-badge-visible');
            } 
            if (footer_reached == true){            
                $('.back-to-top-badge').removeClass('back-to-top-badge-visible');
            }
        });
        
        /*Make contianer fullscreen*/    
        function create_paddings(){
            var no_padding = $(window).width();
            function mobile_paddings(){
                $('.content').css('padding-left', '20px');   
                $('.content').css('padding-right', '20px');   
                $('.container-fullscreen, .image-fullscreen').css('margin-left', '-21px');
                $('.container-fullscreen, .image-fullscreen').css('width', no_padding +2);    
            }
            
            function tablet_paddings(){
                $('.content').css('padding-left', '50px');   
                $('.content').css('padding-right', '50px');  
                $('.container-fullscreen, .image-fullscreen').css('margin-left', '-51px');
                $('.container-fullscreen, .image-fullscreen').css('width', no_padding +2);              
            }
            
            if($(window).width() < 766){
                mobile_paddings()
            }        
            if($(window).width() > 766){
                tablet_paddings()
            }
        }

        $(window).resize(function() {  create_paddings();});
        create_paddings();
        
        /*Morph Headings*/
        $(".infinite-text").Morphext({
            animation: "flipInX",
            separator: "|",
            speed: 2000,
            complete: function () {
            }
        });
        
        /*Set inputs to today's date by adding class set-day*/
        var set_input_now = new Date();
        var set_input_month = (set_input_now.getMonth() + 1);               
        var set_input_day = set_input_now.getDate();
        if(set_input_month < 10) 
            set_input_month = "0" + set_input_month;
        if(set_input_day < 10) 
            set_input_day = "0" + set_input_day;
        var set_input_today = set_input_now.getFullYear() + '-' + set_input_month + '-' + set_input_day;
        $('.set-today').val(set_input_today);
            
        
        /*Portfolios and Gallerties*/
        $('.adaptive-one').click(function(){
            $('.portfolio-switch').removeClass('active-adaptive');
            $(this).addClass('active-adaptive');
            $('.portfolio-adaptive').removeClass('portfolio-adaptive-two portfolio-adaptive-three');
            $('.portfolio-adaptive').addClass('portfolio-adaptive-one');
            return false;
        });    
        
        $('.adaptive-two').click(function(){
            $('.portfolio-switch').removeClass('active-adaptive');
            $(this).addClass('active-adaptive');
            $('.portfolio-adaptive').removeClass('portfolio-adaptive-one portfolio-adaptive-three');
            $('.portfolio-adaptive').addClass('portfolio-adaptive-two'); 
            return false;
        });    
        
        $('.adaptive-three').click(function(){
            $('.portfolio-switch').removeClass('active-adaptive');
            $(this).addClass('active-adaptive');
            $('.portfolio-adaptive').removeClass('portfolio-adaptive-two portfolio-adaptive-one');
            $('.portfolio-adaptive').addClass('portfolio-adaptive-three'); 
            return false;
        });
        
        //Wide Portfolio
        $('.show-wide-text').click(function(){
            $(this).parent().find('.wide-text').slideToggle(200); 
            return false;
        });
        
        $('.portfolio-close').click(function(){
           $(this).parent().parent().find('.wide-text').slideToggle(200);
            return false;
        });
        
        $('.show-gallery, .show-gallery-1, .show-gallery-2, .show-gallery-3, .show-gallery-4, .show-gallery-5, .add-gallery a').swipebox();
        
        function apply_gallery_justification(){
            var screen_widths = $(window).width();
            if( screen_widths < 768){ 
                $('.gallery-justified').justifiedGallery({
                    rowHeight : 70,
                    maxRowHeight : 370,
                    margins : 5,
                    fixedHeight:false
                });
            };

            if( screen_widths > 768){
                $('.gallery-justified').justifiedGallery({
                    rowHeight : 150,
                    maxRowHeight : 370,
                    margins : 5,
                    fixedHeight:false
                });
            };
        };
        apply_gallery_justification();
        
        /*Filterable Gallery*/        
            var selectedClass = "";
            $(".filter-category").click(function(){
                $('.portfolio-filter-categories a').removeClass('selected-filter');
                $(this).addClass('selected-filter');
                selectedClass = $(this).attr("data-rel");
                $(".portfolio-filter-wrapper").show(250);
                $(".portfolio-filter-wrapper div").not("."+selectedClass).delay(100).hide(250);
                setTimeout(function() {
                    $("."+selectedClass).show(250);
                    $(".portfolio-filter-wrapper").show(250);
                }, 0);
            });
    
        
        /*-------------------Generate Cover Screen Elements--------------------*/
        /*Global Settings for Fullscreen Pages, PageApps and Coverscreen Slider*/
        
        function align_cover_elements(){
            var cover_width = $(window).width();
            var cover_height = $(window).height();
            var cover_vertical = -($('.cover-center').height())/2;
            var cover_horizontal = -($('.cover-center').width())/2;
            
            $('.cover-screen').css('width', cover_width);
            $('.cover-screen').css('height', cover_height);
            $('.cover-screen .overlay').css('width', cover_width);
            $('.cover-screen .overlay').css('height', cover_height);
            
            $('.cover-center').css('margin-left', cover_horizontal);      
            $('.cover-center').css('margin-top', cover_vertical + 30);     
            $('.cover-left').css('margin-top', cover_vertical);   
            $('.cover-right').css('margin-top', cover_vertical);           
        };
        align_cover_elements();        
        
        //Resize Functions
        $(window).resize(function(){
            apply_gallery_justification();  
            align_cover_elements();
        });
        
        
        /* Swipebox Image Gallery */
        	$(".swipebox").swipebox({
        		useCSS : true, 
        		hideBarsDelay : 3000 // 0 to always show caption and action bar
        	});
        

        /* Sidebar Activation for pages with proper functions */
            if($('body').hasClass('dual-sidebar')){   dual_sidebar();   }
            if($('body').hasClass('left-sidebar')){   left_sidebar();   }
            if($('body').hasClass('right-sidebar')){  right_sidebar();  }
            if($('body').hasClass('no-sidebar')){     no_sidebar();     }
                
            function dual_sidebar(){
                var $div = $('<div />').appendTo('body');
                $div.attr('id', 'footer-fixed');
                $div.attr('class', 'not-active');
                var snapper = new Snap({
                    element: document.getElementById('content'),
                    elementMirror: document.getElementById('header-fixed'),
                    elementMirror2: document.getElementById('footer-fixed'),
                    disable: 'none',
                    tapToClose: true,
                    touchToDrag: true,
                    maxPosition: 266,
                    minPosition: -266
                });
                $('.close-sidebar').click(function(){snapper.close();});
                $('.open-left-sidebar').click(function() {
                    //$(this).toggleClass('remove-sidebar');
                    if( snapper.state().state=="left" ){
                        snapper.close();
                    } else {
                        snapper.open('left');
                    }
                    return false;
                });	
                $('.open-right-sidebar').click(function() {
                    //$(this).toggleClass('remove-sidebar');
                    if( snapper.state().state=="right" ){
                        snapper.close();
                    } else {
                        snapper.open('right');
                    }
                    return false;
                });
                snapper.on('open', function(){$('.back-to-top-badge').removeClass('back-to-top-badge-visible');});
            };    
            
            function left_sidebar(){
                var $div = $('<div />').appendTo('body');
                $div.attr('id', 'footer-fixed');
                $div.attr('class', 'not-active');
                var snapper = new Snap({
                    element: document.getElementById('content'),
                    elementMirror: document.getElementById('header-fixed'),
                    elementMirror2: document.getElementById('footer-fixed'),
                    disable: 'right',
                    tapToClose: true,
                    touchToDrag: true,
                    maxPosition: 266,
                    minPosition: -266
                });  
                $('.close-sidebar').click(function(){snapper.close();});
                $('.open-left-sidebar').click(function() {
                    //$(this).toggleClass('remove-sidebar');
                    if( snapper.state().state=="left" ){
                        snapper.close();
                    } else {
                        snapper.open('left');
                    }
                    return false;
                });	
                snapper.on('open', function(){$('.back-to-top-badge').removeClass('back-to-top-badge-visible');});
            };    
            
            function right_sidebar(){
                var $div = $('<div />').appendTo('body');
                $div.attr('id', 'footer-fixed');
                $div.attr('class', 'not-active');
                var snapper = new Snap({
                    element: document.getElementById('content'),
                    elementMirror: document.getElementById('header-fixed'),
                    elementMirror2: document.getElementById('footer-fixed'),
                    disable: 'left',
                    tapToClose: true,
                    touchToDrag: true,
                    maxPosition: 266,
                    minPosition: -266
                });     
                $('.close-sidebar').click(function(){snapper.close();});
                $('.open-right-sidebar').click(function() {
                    //$(this).toggleClass('remove-sidebar');
                    if( snapper.state().state=="right" ){
                        snapper.close();
                    } else {
                        snapper.open('right');
                    }
                    return false;
                });
                snapper.on('open', function(){$('.back-to-top-badge').removeClass('back-to-top-badge-visible');});
            };     
                
            function no_sidebar(){
                var snapper = new Snap({
                    element: document.getElementById('content'),
                    elementMirror: document.getElementById('header-fixed'),
                    elementMirror2: document.getElementById('footer-fixed'),
                    disable: 'none',
                    tapToClose: false,
                    touchToDrag: false
                });        
            }; 
            
    });
})( jQuery );


















