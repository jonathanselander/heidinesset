$(document).ready(function () {
    $('.open-popup-link').magnificPopup({
        type: 'inline',
        midClick: true // Allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source in href.
    });
    $('.open-image-popup').magnificPopup({
		type: 'image',
		closeOnContentClick: true,
		closeBtnInside: false,
		fixedContentPos: true,
		mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
		image: {
			verticalFit: true
		},
		gallery: {
			enabled: true
		},
		zoom: {
			enabled: true,
			duration: 200 // don't forget to change the duration also in CSS
		}
    });

    $('#contact').delegate('input,textarea', 'focus', function () {
        if ($(this).attr('type') !== 'submit' && this.value === this.defaultValue) {
            this.value = '';
        }
    });
    $('#contact').delegate('input,textarea', 'blur', function () {
        if ($(this).attr('type') !== 'submit' && this.value === '') {
            this.value = this.defaultValue;
        }
    });
});

$('#logo-img').click(function () {
    $('html, body').animate({ scrollTop: 0 }, "fast");
});