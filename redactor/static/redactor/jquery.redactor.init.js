if(typeof django !== "undefined") {
    jQuery = django.jQuery.noConflict(true);
}

var image_upload_error_callback = function (json) {
    // TODO: Needs better error messages
    alert(json.error);
}

redactor_default_options = {
    imageUploadErrorCallback: image_upload_error_callback
};
