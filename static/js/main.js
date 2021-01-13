$(document).ready(function(){
    // SmartWizard initialize
    $('#smartwizard').smartWizard({
        theme: 'arrows',
        justified: false,
        toolbarSettings: {
            toolbarPosition: 'bottom', // none, top, bottom, both
            toolbarButtonPosition: 'right', // left, right, center
            showNextButton: true, // show/hide a Next button
            showPreviousButton: true, // show/hide a Previous button
        }
    });




    // Darg And Drop image

    $('.dropify').dropify({
        messages: {
            'default': 'Drag here images or <span>browse</span>',
            'replace': 'Drag and drop or <span>click to replace</span>',
            'remove':  '',
            'error':   'Ooops, something wrong happended.'
        },
        tpl: {
            wrap:            '<div class="dropify-wrapper"></div>',
            loader:          '<div class="dropify-loader"></div>',
            message:         '<div class="dropify-message"><p class="note">{{ default }}</p></div>',
            preview:         '<div class="dropify-preview"><span class="dropify-render"></span><div class="dropify-infos"><div class="dropify-infos-inner"><p class="dropify-infos-message">{{ replace }}</p></div></div></div>',
            filename:        '',
            clearButton:     '<button type="button" class="dropify-clear">{{ remove }}</button>',
            errorLine:       '<p class="dropify-error">{{ error }}</p>',
            errorsContainer: '<div class="dropify-errors-container"><ul></ul></div>'
        }
    });

});
