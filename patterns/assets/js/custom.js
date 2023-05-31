var THEMEMASCOT = {};

(function ($) {
  'use strict';

  /* ---------------------------------------------------------------------- */
  /* -------------------------- Declare Variables ------------------------- */
  /* ---------------------------------------------------------------------- */
  var $document = $(document);
  var $document_body = $(document.body);
  var $window = $(window);
  var $sections = $('section');

  THEMEMASCOT.isMobile = {
    Android: function () {
      return navigator.userAgent.match(/Android/i);
    },
    BlackBerry: function () {
      return navigator.userAgent.match(/BlackBerry/i);
    },
    iOS: function () {
      return navigator.userAgent.match(/iPhone|iPad|iPod/i);
    },
    Opera: function () {
      return navigator.userAgent.match(/Opera Mini/i);
    },
    Windows: function () {
      return navigator.userAgent.match(/IEMobile/i);
    },
    any: function () {
      return (
        THEMEMASCOT.isMobile.Android() ||
        THEMEMASCOT.isMobile.BlackBerry() ||
        THEMEMASCOT.isMobile.iOS() ||
        THEMEMASCOT.isMobile.Opera() ||
        THEMEMASCOT.isMobile.Windows()
      );
    },
  };

  THEMEMASCOT.initialize = {
    init: function () {
      THEMEMASCOT.initialize.TM_customDataAttributes();
      THEMEMASCOT.initialize.TM_resizeFullscreen();
      THEMEMASCOT.initialize.TM_equalHeightDivs();
    },

    /* ---------------------------------------------------------------------- */
    /* ----------------------- Background image, color ---------------------- */
    /* ---------------------------------------------------------------------- */
    TM_customDataAttributes: function () {
      $('[data-bg-color]').each(function () {
        $(this).css('cssText', 'background: ' + $(this).data('bg-color') + ' !important;');
      });
      $('[data-bg-img]').each(function () {
        $(this).css('background-image', 'url(' + $(this).data('bg-img') + ')');
      });
      $('[data-text-color]').each(function () {
        $(this).css('color', $(this).data('text-color'));
      });
      $('[data-font-size]').each(function () {
        $(this).css('font-size', $(this).data('font-size'));
      });
      $('[data-height]').each(function () {
        $(this).css('height', $(this).data('height'));
      });
      $('[data-border]').each(function () {
        $(this).css('border', $(this).data('border'));
      });
      $('[data-margin-top]').each(function () {
        $(this).css('margin-top', $(this).data('margin-top'));
      });
      $('[data-margin-right]').each(function () {
        $(this).css('margin-right', $(this).data('margin-right'));
      });
      $('[data-margin-bottom]').each(function () {
        $(this).css('margin-bottom', $(this).data('margin-bottom'));
      });
      $('[data-margin-left]').each(function () {
        $(this).css('margin-left', $(this).data('margin-left'));
      });
    },

    /* ---------------------------------------------------------------------- */
    /* --------------------------- Home Resize Fullscreen ------------------- */
    /* ---------------------------------------------------------------------- */
    TM_resizeFullscreen: function () {
      var windowHeight = $window.height();
      $('.fullscreen, .revslider-fullscreen').height(windowHeight);
    },

    /* ---------------------------------------------------------------------- */
    /* ---------------------------- equalHeights ---------------------------- */
    /* ---------------------------------------------------------------------- */
    TM_equalHeightDivs: function () {
      /* equal heigh */
      var $equal_height = $('.equal-height');
      $equal_height.children('div').css('min-height', 'auto');
      $equal_height.equalHeights();

      /* equal heigh inner div */
      var $equal_height_inner = $('.equal-height-inner');
      $equal_height_inner.children('div').css('min-height', 'auto');
      $equal_height_inner.children('div').children('div').css('min-height', 'auto');
      $equal_height_inner.equalHeights();
      $equal_height_inner.children('div').each(function () {
        $(this).children('div').css('min-height', $(this).css('min-height'));
      });
    },
  };

  THEMEMASCOT.header = {
    init: function () {
      var t = setTimeout(function () {
        THEMEMASCOT.header.TM_fullscreenMenu();
        THEMEMASCOT.header.TM_sidePanelReveal();
        THEMEMASCOT.header.TM_scroolToTopOnClick();
        THEMEMASCOT.header.TM_scrollToFixed();
        THEMEMASCOT.header.TM_topnavAnimate();
        THEMEMASCOT.header.TM_scrolltoTarget();
        THEMEMASCOT.header.TM_menuzord();
        THEMEMASCOT.header.TM_navLocalScorll();
        THEMEMASCOT.header.TM_menuCollapseOnClick();
        THEMEMASCOT.header.TM_homeParallaxFadeEffect();
        THEMEMASCOT.header.TM_topsearch_toggle();
      }, 0);
    },

    /* ---------------------------------------------------------------------- */
    /* ------------------------- menufullpage ---------------------------- */
    /* ---------------------------------------------------------------------- */
    TM_fullscreenMenu: function () {
      var $menufullpage = $('.menu-full-page .fullpage-nav-toggle');
      $menufullpage.menufullpage();
    },

    /* ---------------------------------------------------------------------- */
    /* ------------------------- Side Push Panel ---------------------------- */
    /* ---------------------------------------------------------------------- */
    TM_sidePanelReveal: function () {
      $('.side-panel-trigger').on('click', function (e) {
        $body.toggleClass('side-panel-open');
        if (THEMEMASCOT.isMobile.any()) {
          $body.toggleClass('overflow-hidden');
        }
        return false;
      });

      $('.has-side-panel .body-overlay').on('click', function (e) {
        $body.toggleClass('side-panel-open');
        return false;
      });

      //sitebar tree
      $('.side-panel-nav .nav .tree-toggler').on('click', function (e) {
        $(this).parent().children('ul.tree').toggle(300);
      });
    },

    /* ---------------------------------------------------------------------- */
    /* ------------------------------- scrollToTop  ------------------------- */
    /* ---------------------------------------------------------------------- */
    TM_scroolToTop: function () {
      if ($window.scrollTop() > 600) {
        $('.scrollToTop').fadeIn();
      } else {
        $('.scrollToTop').fadeOut();
      }
    },

    TM_scroolToTopOnClick: function () {
      $document_body.on('click', '.scrollToTop', function (e) {
        $('html, body').animate(
          {
            scrollTop: 0,
          },
          800,
        );
        return false;
      });
    },

    /* ---------------------------------------------------------------------------- */
    /* --------------------------- One Page Nav close on click -------------------- */
    /* ---------------------------------------------------------------------------- */
    TM_menuCollapseOnClick: function () {
      $document.on('click', '.onepage-nav a', function (e) {
        $('.showhide').trigger('click');
        return true;
      });
    },

    /* ---------------------------------------------------------------------- */
    /* ----------- Active Menu Item on Reaching Different Sections ---------- */
    /* ---------------------------------------------------------------------- */
    TM_activateMenuItemOnReach: function () {
      var $onepage_nav = $('.onepage-nav');
      var cur_pos = $window.scrollTop() + 2;
      var nav_height = $onepage_nav.outerHeight();
      $sections.each(function () {
        var top = $(this).offset().top - nav_height - 80,
          bottom = top + $(this).outerHeight();

        if (cur_pos >= top && cur_pos <= bottom) {
          // $onepage_nav.find('a').parent().removeClass('current').removeClass('active');
          $sections.removeClass('current').removeClass('active');

          //$(this).addClass('current').addClass('active');
          $onepage_nav
            .find('a[href="#' + $(this).attr('id') + '"]')
            .parent()
            .addClass('current')
            .addClass('active');
        }
      });
    },

    /* ---------------------------------------------------------------------- */
    /* ------------------- on click scrool to target with smoothness -------- */
    /* ---------------------------------------------------------------------- */
    TM_scrolltoTarget: function () {
      //jQuery for page scrolling feature - requires jQuery Easing plugin
      $('.smooth-scroll-to-target, .fullscreen-onepage-nav a').on('click', function (e) {
        e.preventDefault();

        var $anchor = $(this);

        var $hearder_top = $('.header .header-nav');
        var hearder_top_offset = 0;
        if ($hearder_top[0]) {
          hearder_top_offset = $hearder_top.outerHeight(true);
        } else {
          hearder_top_offset = 0;
        }

        //for vertical nav, offset 0
        if ($body.hasClass('vertical-nav')) {
          hearder_top_offset = 0;
        }

        var top = $($anchor.attr('href')).offset().top - hearder_top_offset;
        $('html, body').stop().animate(
          {
            scrollTop: top,
          },
          1500,
          'easeInOutExpo',
        );
      });
    },

    /* ---------------------------------------------------------------------- */
    /* -------------------------- Scroll navigation ------------------------- */
    /* ---------------------------------------------------------------------- */
    TM_navLocalScorll: function () {
      var data_offset = -60;
      $('#menuzord .menuzord-menu, #menuzord-right .menuzord-menu').localScroll({
        target: 'body',
        duration: 800,
        offset: data_offset,
        easing: 'easeInOutExpo',
      });

      $('#menuzord-side-panel .menuzord-menu, #menuzord-verticalnav .menuzord-menu, #fullpage-nav').localScroll({
        target: 'body',
        duration: 800,
        offset: 0,
        easing: 'easeInOutExpo',
      });
    },

    /* ---------------------------------------------------------------------------- */
    /* --------------------------- collapsed menu close on click ------------------ */
    /* ---------------------------------------------------------------------------- */
    TM_scrollToFixed: function () {
      $('.navbar-scrolltofixed').scrollToFixed();
      $('.scrolltofixed').scrollToFixed({
        marginTop: $('.header .header-nav').outerHeight(true) + 10,
        limit: function () {
          var limit = $('#footer').offset().top - $(this).outerHeight(true);
          return limit;
        },
      });
      $('#sidebar').scrollToFixed({
        marginTop: $('.header .header-nav').outerHeight() + 20,
        limit: function () {
          var limit = $('#footer').offset().top - $('#sidebar').outerHeight() - 20;
          return limit;
        },
      });
    },

    /* ----------------------------------------------------------------------------- */
    /* --------------------------- Menuzord - Responsive Megamenu ------------------ */
    /* ----------------------------------------------------------------------------- */
    TM_menuzord: function () {
      $('#menuzord').menuzord({
        align: 'left',
        effect: 'slide',
        animation: 'none',
        indicatorFirstLevel: "<i class='fa fa-angle-down'></i>",
        indicatorSecondLevel: "<i class='fa fa-angle-right'></i>",
      });
      $('#menuzord-right').menuzord({
        align: 'right',
        effect: 'slide',
        animation: 'none',
        indicatorFirstLevel: "<i class='fa fa-angle-down'></i>",
        indicatorSecondLevel: "<i class='fa fa-angle-right'></i>",
      });
      $('#menuzord-side-panel').menuzord({
        align: 'right',
        effect: 'slide',
        animation: 'none',
        indicatorFirstLevel: '',
        indicatorSecondLevel: "<i class='fa fa-angle-right'></i>",
      });

      $('#menuzord-verticalnav').menuzord({
        align: 'right',
        effect: 'slide',
        animation: 'none',
        indicatorFirstLevel: "<i class='fa fa-angle-down'></i>",
        indicatorSecondLevel: "<i class='fa fa-angle-right'></i>",
        /*indicatorFirstLevel: "<i class='fa fa-angle-right'></i>",
            indicatorSecondLevel: "<i class='fa fa-angle-right'></i>"*/
      });
    },

    /* ---------------------------------------------------------------------- */
    /* --------------------------- Waypoint Top Nav Sticky ------------------ */
    /* ---------------------------------------------------------------------- */
    TM_topnavAnimate: function () {
      if ($window.scrollTop() > 50) {
        $('.navbar-sticky-animated').removeClass('animated-active');
      } else {
        $('.navbar-sticky-animated').addClass('animated-active');
      }

      if ($window.scrollTop() > 50) {
        $(
          '.navbar-sticky-animated .header-nav-wrapper .container, .navbar-sticky-animated .header-nav-wrapper .container-fluid',
        ).removeClass('add-padding');
      } else {
        $(
          '.navbar-sticky-animated .header-nav-wrapper .container, .navbar-sticky-animated .header-nav-wrapper .container-fluid',
        ).addClass('add-padding');
      }
    },

    /* ---------------------------------------------------------------------- */
    /* ---------------- home section on scroll parallax & fade -------------- */
    /* ---------------------------------------------------------------------- */
    TM_homeParallaxFadeEffect: function () {
      if ($window.width() >= 1200) {
        var scrolled = $window.scrollTop();
        $('.content-fade-effect .home-content .home-text')
          .css('padding-top', scrolled * 0.061 + '%')
          .css('opacity', 1 - scrolled * 0.0012);
      }
    },

    /* ---------------------------------------------------------------------- */
    /* --------------------------- Top search toggle  ----------------------- */
    /* ---------------------------------------------------------------------- */
    TM_topsearch_toggle: function () {
      $document_body.on('click', '#top-search-toggle', function (e) {
        e.preventDefault();
        $('.search-form-wrapper.toggle').toggleClass('active');
        return false;
      });
    },
  };

  /* ---------------------------------------------------------------------- */
  /* ---------- document ready, window load, scroll and resize ------------ */
  /* ---------------------------------------------------------------------- */
  //document ready
  THEMEMASCOT.documentOnReady = {
    init: function () {
      THEMEMASCOT.initialize.init();
      THEMEMASCOT.header.init();
      THEMEMASCOT.windowOnscroll.init();
    },
  };

  //window on load
  THEMEMASCOT.windowOnLoad = {
    init: function () {
      $window.trigger('scroll');
      $window.trigger('resize');
    },
  };

  //window on scroll
  THEMEMASCOT.windowOnscroll = {
    init: function () {
      $window.on('scroll', function () {
        THEMEMASCOT.header.TM_scroolToTop();
        THEMEMASCOT.header.TM_activateMenuItemOnReach();
        THEMEMASCOT.header.TM_topnavAnimate();
      });
    },
  };

  //window on resize
  THEMEMASCOT.windowOnResize = {
    init: function () {
      var t = setTimeout(function () {
        THEMEMASCOT.initialize.TM_equalHeightDivs();
        THEMEMASCOT.initialize.TM_resizeFullscreen();
      }, 400);
    },
  };

  /* ---------------------------------------------------------------------- */
  /* ---------------------------- Call Functions -------------------------- */
  /* ---------------------------------------------------------------------- */
  $document.ready(THEMEMASCOT.documentOnReady.init);
  $window.on('load', THEMEMASCOT.windowOnLoad.init);
  $window.on('resize', THEMEMASCOT.windowOnResize.init);

  /* === ANCHOR LINKS === */
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const hash = this.getAttribute('href');

      document.querySelector(hash).scrollIntoView({
        behavior: 'smooth',
      });
      setTimeout(() => {
        window.location.hash = hash;
      }, 500);
    });
  });
})(jQuery);
