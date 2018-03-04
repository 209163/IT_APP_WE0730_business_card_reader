jQuery(window).on("load", function () {

    /* animacje */
    if (!(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent))) {

        /*jQuery(window).scroll(function () {
         if (isInViewport("#o_nas")) {
         jQuery("#i3").removeClass("invisible").addClass("slideInUp animated");
         setTimeout(function () {
         jQuery("#i4").removeClass("invisible").addClass("slideInUp animated");
         }, 200);
         }
         
         });*/

    } else {
        jQuery('.invisible').css('visibility', 'visible');
    }



    $('#file').change(function () {
        $('#results').addClass('active');
        setTimeout(function () {
            jQuery(".visit-card-content").removeClass("invisible").addClass("fadeIn animated");
        }, 400);
        setTimeout(function () {
            jQuery(".card-details").removeClass("invisible").addClass("fadeIn animated");
        }, 800);
        setTimeout(function () {
            jQuery(".infobox").removeClass("invisible").addClass("fadeIn animated");
        }, 1400);

    });

    if (window.innerWidth > 991) {
        sameHeight(".author-box", 0);
    }

});


function isInViewport(elements) {

    var windowHeight = window.innerHeight;
    var positionTop = jQuery(window).scrollTop();
    var positionBottom = positionTop + windowHeight;
    var positionMiddleOne = (positionBottom - positionTop) / 1.5 + positionTop;
    var positionMiddleTwo = (positionBottom - positionTop) / 2.5 + positionTop;
    var output = false;
    if (jQuery(elements).length) {
        var pos = jQuery(elements).offset();
        var posBottom = pos.top + jQuery(elements).outerHeight();

        if ((positionMiddleOne < posBottom) && (positionMiddleOne > pos.top)) {
            output = true;
        }

        if ((positionMiddleTwo < posBottom) && (positionMiddleTwo > pos.top)) {
            output = true;
        }
    }
    return output;
}
function sameHeight(blocks, p) {
    var i = 0;
    var maxVal;
    jQuery(blocks).each(function () {
        if (i === 0) {
            maxVal = jQuery(this).height();
        } else {
            if (jQuery(this).outerHeight() > maxVal) {
                maxVal = jQuery(this).height();
            }
        }
        i++;
    });

    jQuery(blocks).each(function () {
        jQuery(this).height(maxVal + p);
    });
}