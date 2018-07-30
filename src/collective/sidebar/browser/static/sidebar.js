(function($) {
  'use strict'; // Start of use strict

  $(document).ready(function() {

    // Menu Lock

    $('.menu-lock span').click(function() {
      $(this).toggleClass('jam-padlock-open jam-padlock');
      $('#sidebar-cover').toggleClass('hidden');
      if ($.cookie('sidebar-locked')) {
        $.removeCookie('sidebar-locked');
      } else {
        $.cookie('sidebar-locked', 1);
      }
    });

    // Collapse

    $('.userrole-authenticated .menu .menu-section-title').click(function() {
      var parent = $(this).parent();
      $(this).toggleClass('collapsed');
      parent.find('a').toggle();
    });

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
      $('body').attr('data-with-sidebar', 'true');
    });

    // Navigation Slideovers

    $('.menu-sitemap-hook').click(function(e) {
      e.preventDefault();
      $('.menu-sitemap').toggleClass('opened');
    });

    // Sidebar Cover

    $('#sidebar-cover').click(function(e) {
      e.preventDefault();
      $('body').attr('data-with-sidebar', '');
    });

  });

})(jQuery); // End of use strict
