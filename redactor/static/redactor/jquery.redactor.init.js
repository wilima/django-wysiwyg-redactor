if (typeof jQuery === 'undefined' && django && django.jQuery) {
    jQuery = django.jQuery;
}

/**
This makes sure that we initialise the redactor on the text area once its displayed
so it can be used as part of an inline formset.

Credit to the approach taken in:
https://github.com/yourlabs/django-autocomplete-light
**/
(function($) {
    $(document).ready(function() {
        $('textarea.redactor-box').on('initialize', function() {
            redactor_options = $(this).data('redactor-options');
            redactor_options.imageUploadErrorCallback = function (json) {
                // TODO: Needs better error messages
                alert(json.error);
            }
            $(this).redactor(redactor_options);
        });
        $(document).trigger('redactorWidgetReady');

        $('textarea.redactor-box:not([id*="__prefix__"])').each(function() {
            $(this).trigger('initialize');
        });

        $(document).bind('DOMNodeInserted', function(e) {
            var widget = $(e.target).find('.redactor-box');

            if (!widget.length) return;

            widget.trigger('initialize');
        });
    });
})(jQuery);
