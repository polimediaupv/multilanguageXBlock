/**
 * Created by leosamu on 17/12/15.
 */
/* Javascript for MultiLanguageXBlock. */


    function showNavigatorLanguage(id,element)
    {
        console.log(element);
        tabs =  $(".multilanguage_block>div",element.parentNode);
        tabs = tabs.toArray();
        allNone = true;
        tabs.forEach(function(tab){ if(tab.id===$(".lang_code",element.parentNode)[0].innerHTML|navigator.languages[0]||navigator.userLanguage){$(tab).css({"display":'block'});allNone=false;}else{$(tab).css({"display":'none'});} })
        if (allNone)
        {
           $($(".multilanguage_block>div:not(.lang_code)",element.parentNode)[0]).css({"display":'block'});
        }
    }
