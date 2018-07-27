(function($) {
  'use strict'; // Start of use strict

  $(document).ready(function() {

    // Nav Logo

    setTimeout(function() {
      $('.nav-logo').addClass('in-view');
    }, 500);

    // Header

    var hs = $('');

    if (hs.length) {
      var mh = $('#header-wrapper');

      $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        var os = hs.offset().top;
        var ht = hs.height();
        if (scroll > os + ht) {
          mh.addClass('active');
        } else {
          mh.removeClass('active');
        }
      });
    }

    // Burger

    $('#nav-icon').click(function(e) {
      e.preventDefault();
      $('body').toggleClass('with-sidebar');
    });

    // Navigation Slideovers

    $('.menu-sitemap-hook').click(function(e) {
      e.preventDefault();
      $('.menu-sitemap').toggleClass('opened');
    });

    // Sidebar Cover

    $('#sidebar-cover').click(function(e) {
      e.preventDefault();
      $('body').removeClass('with-sidebar');
    });

  });

})(jQuery); // End of use strict
