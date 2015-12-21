# coding=utf-8
__author__ = u"Leonardo Salom Muñoz"
__credits__ = u"Leonardo Salom Muñoz"
__version__ = u"0.0.5-SNAPSHOT"
__maintainer__ = u"Leonardo Salom Muñoz"
__email__ = u"leosamu@upv.es"
__status__ = u"Development"
import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from user_api.models import UserPreference
from django.utils import translation
from django.conf import settings
from dark_lang.models import DarkLangConfig
import bson.son
from xblock.fragment import Fragment


class MultiLanguageXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    display_name = String(display_name="Display Name",
                          default="Multilanguage",
                          scope=Scope.settings,
                          help="Name of the component in the edxplatform")

    # serialized_tabs could be a json?
    serialized_tabs = String(display_name="tabnames",
                  default=u'es-es^^^texto en español---en^^^english text',
                  scope=Scope.content,
                  help="Serialized tabs")





    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the MultiTabXBlock, shown to students
        when viewing courses.
        """
        tabs=u''
        divs=u''
        #DarkLangConfig.current().released_languages_list

        tabDict=bson.son.SON((k.strip(), v.strip()) for k,v in
              (item.split('^^^') for item in self.serialized_tabs.split('---')))
        for tab, content in tabDict.iteritems():
            tabs= tabs + u'<a onclick="showStuff(\'' + unicode(tab) + u'\',this);" class="classname" name="tab[]">' + unicode(tab) + u'</a>'
            if divs == u'':
                divs = divs + u'<div id="' + unicode(tab) + u'" style="display: block;">' + unicode(content) + u'</div>'
            else:
                divs = divs + u'<div id="' + unicode(tab) + u'" style="display: none;">' + unicode(content) + u'</div>'
        html = self.resource_string("static/html/multilanguage.html")
        frag = Fragment(html.format(self=self,tabs=tabs,divs=divs,current_language_code=translation.get_language()))
        frag.add_css(self.resource_string("static/css/multilanguage.css"))
        frag.add_javascript(self.resource_string("static/js/src/showstuff.js"))
        frag.initialize_js('showNavigatorLanguage')
        return frag


    def studio_view(self, context=None):   #studio_view

        dynamictabs = u'<ul id="sortable">'

        #generate a dictionary with all the tabs that we currently have
        tabDict=bson.son.SON((k.strip(), v.strip()) for k,v in
              (item.split('^^^') for item in self.serialized_tabs.split('---')))
        i=0

        lang_dict =dict(settings.LANGUAGES)
        print lang_dict[u'es-es']
        print DarkLangConfig.current().released_languages_list
        print translation.get_language()

        for tab, content in tabDict.iteritems():
            dynamictabs = dynamictabs + u'<li id="tab' + unicode(i) + u'" order=' + unicode(i) + u'>'
            dynamictabs = dynamictabs + u'<div class="wrapper-videolist-url videolist-settings-item" >'
            dynamictabs = dynamictabs + u'<label class="label setting-label">Language</label>'

            #change this for a language selector from dark_lang languages
            #dynamictabs = dynamictabs + u'<input class="input setting-input edit-display-name" id="tab0" value="' + unicode(tab) + u'" type="text" name="tabname[]">'
            dynamictabs = dynamictabs + u'<select class="input setting-input edit-display-name" id="tab0" name="tabname[]">'
            for lang in DarkLangConfig.current().released_languages_list:
                if lang == unicode(tab):
                    dynamictabs = dynamictabs + u'<option value="' + lang + '" selected>' + lang_dict[lang] + '</option> '
                else:
                    dynamictabs = dynamictabs + u'<option value="' + lang + '">' + lang_dict[lang] + '</option> '
            dynamictabs = dynamictabs + u'</select>'


            dynamictabs = dynamictabs + u'<a href="#" class="add-button roundbuttons" order=' + unicode(i) + u' >+</a><a href="#" class="del-button roundbuttons" order=' + unicode(i) + u' >-</a>'
            #dynamictabs = dynamictabs + orderbutons
            dynamictabs = dynamictabs + u'</div>'
            dynamictabs = dynamictabs + u'<div class="wrapper-videolist-url videolist-settings-item">'
            dynamictabs = dynamictabs + u'<label class="label setting-label">Content</label>'
            dynamictabs = dynamictabs + u'<textarea class="input setting-input edit-display-name" id="tabcontent0" type="text" style="margin: 2px; width: 372px; height: 135px;" name="tabcontent[]">'
            dynamictabs = dynamictabs + unicode(content)
            dynamictabs = dynamictabs + u'</textarea>'
            dynamictabs = dynamictabs + u' </div></li>'
            i=i+1

        dynamictabs = dynamictabs + u'</ul">'

        html = self.resource_string("static/html/multilanguage_edit.html")
        frag = Fragment(html.format(self=self,dynamictabs=dynamictabs))
        frag.add_css(self.resource_string("static/css/multilanguage.css"))
        frag.add_javascript(self.resource_string("static/js/src/multilanguage.js"))
        frag.initialize_js('MultiLanguageXBlock')
        return frag



    @XBlock.json_handler
    def save_tabs(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        tabnames = data['tabnames']
        tabcontent = data['tabcontent']
        #clean previous content
        self.serialized_tabs= u''
        #revisar luego 'if (unicode(tabnames[i])!='' && unicode(tabcontent[i])!=''):
        for i  in range(0, len(tabnames)):
            self.serialized_tabs = self.serialized_tabs + unicode(tabnames[i]) + u'^^^' + unicode(tabcontent[i]) + u'---'

        self.serialized_tabs=self.serialized_tabs[:-3]

        self.display_name = data['display_name']

        return {
            'result' : 'success',
        }

    @XBlock.json_handler
    def del_tabs(self, data, suffix=''):
        # Just to show data coming in...
        #will need to serialize the edition but firstly we will focus on how content is shown
        #assert data['hello'] == 'world'
        tabnames = data['tabnames']
        tabcontent = data['tabcontent']
        tabindex = data['tabindex']
        #clean previous content
        self.serialized_tabs= u''
        for i  in range(0, len(tabnames)):
            if unicode(i) != tabindex:
                self.serialized_tabs = self.serialized_tabs + unicode(tabnames[i]) + u'^^^' + unicode(tabcontent[i]) + u'---'

        #if we delete all we leave a blank item
        if self.serialized_tabs == u'':
            self.serialized_tabs= u' ^^^ ---'

        self.serialized_tabs=self.serialized_tabs[:-3]

        self.display_name = data['display_name']

        return {
            'result': 'success',
        }

    @XBlock.json_handler
    def add_tabs(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        print data['tabindex']
        # Just to show data coming in...
        #will need to serialize the edition but firstly we will focus on how content is shown
        #assert data['hello'] == 'world'
        tabnames = data['tabnames']
        tabcontent = data['tabcontent']
        tabindex = data['tabindex']
        #clean previous content
        self.serialized_tabs= u''
        for i  in range(0, len(tabnames)):
            self.serialized_tabs = self.serialized_tabs + unicode(tabnames[i]) + u'^^^' + unicode(tabcontent[i]) + u'---'
            if unicode(i) == tabindex:
                self.serialized_tabs = self.serialized_tabs + u' ^^^ ---'

        self.serialized_tabs=self.serialized_tabs[:-3]

        self.display_name = data['display_name']

        return {
            'result': 'success',
        }


    @XBlock.json_handler
    def up_tabs(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        #will need to serialize the edition but firstly we will focus on how content is shown
        #assert data['hello'] == 'world'
        tabnames = data['tabnames']
        tabcontent = data['tabcontent']
        tabindex = data['tabindex']

        flipaux=tabnames[int(tabindex)-1]
        tabnames[int(tabindex)-1]=tabnames[int(tabindex)]
        tabnames[int(tabindex)]=flipaux

        flipaux=tabcontent[int(tabindex)-1]
        tabcontent[int(tabindex)-1]=tabcontent[int(tabindex)]
        tabcontent[int(tabindex)]=flipaux

        #clean previous content
        self.serialized_tabs= u''

        for i  in range(0, len(tabnames)):
            self.serialized_tabs = self.serialized_tabs + unicode(tabnames[i]) + u'^^^' + unicode(tabcontent[i]) + u'---'

        self.serialized_tabs=self.serialized_tabs[:-3]

        self.display_name = data['display_name']

        return {
            'result': 'success',
        }

    @XBlock.json_handler
    def down_tabs(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        #will need to serialize the edition but firstly we will focus on how content is shown
        #assert data['hello'] == 'world'
        tabnames = data['tabnames']
        tabcontent = data['tabcontent']
        tabindex = data['tabindex']

        flipaux=tabnames[int(tabindex)+1]
        tabnames[int(tabindex)+1]=tabnames[int(tabindex)]
        tabnames[int(tabindex)]=flipaux

        flipaux=tabcontent[int(tabindex)+1]
        tabcontent[int(tabindex)+1]=tabcontent[int(tabindex)]
        tabcontent[int(tabindex)]=flipaux

        #clean previous content
        self.serialized_tabs= u''

        for i  in range(0, len(tabnames)):
            self.serialized_tabs = self.serialized_tabs + unicode(tabnames[i]) + u'^^^' + unicode(tabcontent[i]) + u'---'

        self.serialized_tabs=self.serialized_tabs[:-3]

        self.display_name = data['display_name']

        return {
            'result': 'success',
        }


    def studio_simple_view(self, context=None):   #studio_view
        tabDict=dict((k.strip(), v.strip()) for k,v in
              (item.split('^^^') for item in self.serialized_tabs.split('---')))

        #remove not ID content
        tabDict[u'YouTube']=tabDict[u'YouTube'][63:-46]
        tabDict[u'优酷']=tabDict[u'优酷'][69:-46]
        tabDict[u'PoliMedia']=tabDict[u'PoliMedia'][71:-46]

        #html = self.resource_string("static/html/multitab_3simple_edit.html")
        frag = Fragment(html.format(self=self,youtubeID=tabDict[u'YouTube'],youkuID=tabDict[u'优酷'],polimediaID=tabDict[u'PoliMedia']))
        #frag.add_javascript(self.resource_string("static/js/src/multitabsimple.js"))
        frag.initialize_js('MultiLanguageXBlock')
        return frag


    def save_simple_tabs(self, data, suffix=''):
        """
            'display_name': $(edit_display_name).context.value,
            'youtube_id': $(tab0).context.value,
            'youku_id': $(tab1).context.value,
            'polimedia_id':$(tab2).context.value
        """
        # Just to show data coming in...
        #will need to serialize the edition but firstly we will focus on how content is shown
        #assert data['hello'] == 'world'

        auxstr = u'YouTube^^^<iframe width="100%" height="600" src="//www.youtube.com/embed/'
        auxstr = auxstr + data['youtube_id']
        auxstr = auxstr + u'" frameborder="0" allowfullscreen=""></iframe>---优酷^^^<iframe height="600" width="100%" src="http://player.youku.com/embed/'
        auxstr = auxstr + data['youku_id']
        auxstr = auxstr + u'" frameborder="0" allowfullscreen=""></iframe>---PoliMedia^^^<iframe height="600" width="100%" src="https://media.upv.es/player/?id='
        auxstr = auxstr + data['polimedia_id']
        auxstr = auxstr + u'" frameborder="0" allowfullscreen=""></iframe>'
        print(auxstr)
        self.serialized_tabs = auxstr

        self.display_name = data['display_name']

        return {
            'result': 'success',
        }

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("MultiLanguageXBlock",
             """<vertical_demo>
                <multilanguage/>
                </vertical_demo>
             """),
        ]