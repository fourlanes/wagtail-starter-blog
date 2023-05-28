var THEMEMASCOT = {};

(function ($) {
  'use strict';

  /* ---------------------------------------------------------------------- */
  /* -------------------------- Declare Variables ------------------------- */
  /* ---------------------------------------------------------------------- */
  var $document = $(document);
  var $window = $(window);

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

  /* ---------------------------------------------------------------------- */
  /* ---------- document ready, window load, scroll and resize ------------ */
  /* ---------------------------------------------------------------------- */
  //document ready
  THEMEMASCOT.documentOnReady = {
    init: function () {
      THEMEMASCOT.initialize.init();
    },
  };

  //window on load
  THEMEMASCOT.windowOnLoad = {
    init: function () {
      $window.trigger('scroll');
      $window.trigger('resize');
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
