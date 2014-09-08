/**
 * Created by leosamu on 05/09/14.
 */
function showStuff(id) {

        tabnames = $("a[name='tab\\[\\]']").map(function(){return $(this).context.text;}).get();

        tabnames.forEach(function(tab) {
             document.getElementById(tab).style.display = 'none';
        });

   	    document.getElementById(id).style.display = 'block';
       return true;
   }