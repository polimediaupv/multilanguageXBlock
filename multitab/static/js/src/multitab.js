/* Javascript for MultiTabXBlock. */
function MultiTabXBlock(runtime, element) {



   $(element).find('.cancel-button').bind('click', function() {
        runtime.notify('cancel', {});
    });

   $(element).find('.save-button').bind('click', function() {
        var data = {
            'display_name': $(edit_display_name).context.value,
            'tabnames': $("input[name='tabname\\[\\]']").map(function(){return $(this).context.value;}).get(),
            'tabcontent': $("textarea[name='tabcontent\\[\\]']").map(function(){return $(this).context.value;}).get()
        };

        $('.xblock-editor-error-message', element).html();
        $('.xblock-editor-error-message', element).css('display', 'none');
        var handlerUrl = runtime.handlerUrl(element, 'save_tabs');
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            if (response.result === 'success') {
                window.location.reload(false);
            } else {
                $('.xblock-editor-error-message', element).html('Error: '+response.message);
                $('.xblock-editor-error-message', element).css('display', 'block');
            }
        });
   });

   $(element).find('.add-button').on('click', function () {

        newtab="";
        orderbutons="";
        if ($(this).parent().parent().next().size()==0 && $(this).parent().parent().prev().size()==0)
        {
            orderbutons = '<a href="#" class="up-button  roundbuttons">^</a>';
        }
        else if ($(this).parent().parent().next().size()==0 && $(this).parent().parent().prev().size()!=0)
        {
            /*when we add an element at the end of the array we need to add a down button to the element that creates this */
            $(this).next().after('<a href="#" class="down-button roundbuttons">v</a>');
            orderbutons = '<a href="#" class="up-button  roundbuttons">^</a>';
        }
        else
        {
            orderbutons = '<a href="#" class="down-button roundbuttons">v</a><a href="#" class="up-button roundbuttons">^</a>';
        }


        newtab = newtab + '<div>';
        newtab = newtab + '<div class="wrapper-videolist-url videolist-settings-item" >';
        newtab = newtab + '<label class="label setting-label">Tab name</label>';
        newtab = newtab + '<input class="input setting-input edit-display-name" id="tab0" value="" name="tabname[]">';
        newtab = newtab + '<a href="#" class="add-button roundbuttons" >+</a><a href="#" class="del-button roundbuttons">-</a>';
        newtab = newtab + orderbutons;
        newtab = newtab + '</div>';
        newtab = newtab + '<div class="wrapper-videolist-url videolist-settings-item">';
        newtab = newtab + '<label class="label setting-label">Tab content</label>';
        newtab = newtab + '<textarea class="input setting-input edit-display-name" id="tabcontent0" type="text" style="margin: 2px; width: 372px; height: 135px;" name="tabcontent[]">';
        newtab = newtab + '</textarea>';
        newtab = newtab + ' </div></div>';

       $(this).parent().parent().after(newtab);
    }
   );



    $(element).find('.del-button').on('click', function() {
        if ($(this).parent().parent().next().size()==0 && $(this).parent().parent().prev().size()==0)
        {
            /*only one tab we clear text*/
            $(this).parent().next().children('[type="text"]').val("");
            $(this).prev().prev().val("");
        }
        else if ($(this).parent().parent().next().size()==0 && $(this).parent().parent().prev().prev().size()==1)
        {
            /*last tab we delete the tab and remove the downbutton from the previous*/
            $(this).parent().parent().prev().children().children("[class='down-button roundbuttons']").remove();
            $(this).parent().parent().remove();
        }
        else if ($(this).parent().parent().next().size()==1 && $(this).parent().parent().prev().size()==0)
        {

            if($(this).parent().parent().next().children().children("[class='down-button roundbuttons']").size()==0)
            {
                $(this).parent().parent().next().children().children("[class='up-button roundbuttons']").after('<a href="#" class="down-button roundbuttons">v</a>');
            }
            $(this).parent().parent().next().children().children("[class='up-button roundbuttons']").remove();
            $(this).parent().parent().remove();
        }
        else
        {
            $(this).parent().parent().remove();
        }

    });

    $(element).find('.up-button').on('click', function() {
        tabname =    $(this).parent().parent().children().children("input[name='tabname\\[\\]']").val();
        tabcontent = $(this).parent().parent().children().children("textarea[name='tabcontent\\[\\]']").val();
        $(this).parent().parent().children().children("input[name='tabname\\[\\]']").val($(this).parent().parent().prev().children().children("input[name='tabname\\[\\]']").val());
        $(this).parent().parent().children().children("textarea[name='tabcontent\\[\\]']").val($(this).parent().parent().prev().children().children("textarea[name='tabcontent\\[\\]']").val());
        $(this).parent().parent().prev().children().children("input[name='tabname\\[\\]']").val(tabname);
        $(this).parent().parent().prev().children().children("textarea[name='tabcontent\\[\\]']").val(tabcontent);
    });


    $(element).find('.down-button').on('click', function() {
        tabname =    $(this).parent().parent().children().children("input[name='tabname\\[\\]']").val();
        tabcontent = $(this).parent().parent().children().children("textarea[name='tabcontent\\[\\]']").val();
        $(this).parent().parent().children().children("input[name='tabname\\[\\]']").val($(this).parent().parent().next().children().children("input[name='tabname\\[\\]']").val());
        $(this).parent().parent().children().children("textarea[name='tabcontent\\[\\]']").val($(this).parent().parent().next().children().children("textarea[name='tabcontent\\[\\]']").val());
        $(this).parent().parent().next().children().children("input[name='tabname\\[\\]']").val(tabname);
        $(this).parent().parent().next().children().children("textarea[name='tabcontent\\[\\]']").val(tabcontent);
    });

   $(function ($) {
        /* Here's where you'd do things on page load. */

   });
}


