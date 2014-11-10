/**
 * Created by leosamu on 05/09/14.
 */
/* Javascript for MultiTabXBlock. */

    function showStuff(id,element) {

            tabnames = $("a[name='tab\\[\\]']",element.parentNode).map(function(){return $(this).context.text;}).get();

            tabnames.forEach(function(tab) {
                 $("#"+tab,element.parentNode).css({"display":'none'});
            });

            $("#"+id,element.parentNode).css({"display":'block'});
           return false;
       }


