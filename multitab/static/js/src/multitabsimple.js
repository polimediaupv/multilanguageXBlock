/* Javascript for MultiTabXBlock. */
function MultiTabXBlock(runtime, element) {



   $(element).find('.cancel-button').bind('click', function() {
        runtime.notify('cancel', {});
    });

    $(element).find('.save-button').bind('click', function() {
        var data = {
            'display_name': $(edit_display_name).context.value,
            'youtube_id': $(tab0).context.value,
            'youku_id': $(tab1).context.value,
            'polimedia_id':$(tab2).context.value
        };

        $('.xblock-editor-error-message', element).html();
        $('.xblock-editor-error-message', element).css('display', 'none');
        var handlerUrl = runtime.handlerUrl(element, 'save_simple_tabs');
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            if (response.result === 'success') {
                window.location.reload(false);
            } else {
                $('.xblock-editor-error-message', element).html('Error: '+response.message);
                $('.xblock-editor-error-message', element).css('display', 'block');
            }
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */

    });


   function showStuff(id) {

        tabnames = $("a[name='tab\\[\\]']").map(function(){return $(this).context.text;}).get();

        tabnames.forEach(function(tab) {
             document.getElementById(tab).style.display = 'none';
        });

   	    document.getElementById(id).style.display = 'block';
       return true;
   }
}