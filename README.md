# Edx Xblock for Multilanguage Content #
This Xblock allows to generate multi language content into the edX platform, the XBlock takes into account the active languages in the platform when generating the content and the selected user language when it shows it to the student.

Right now it accepts html content, but in the future we could have another type of contents like edx problems, videos, etc.

## Installation instructions ##
In order to install the XBlock into your Edx devstack Server you need to.

## Download the XBlock from github. Place the files inside your server.

##.   Install your block::
You must replace `/path/to/your/block` with the path where you have downloaded the xblock

        $ vagrant ssh
        vagrant@precise64:~$ sudo -u edxapp /edx/bin/pip.edxapp install /path/to/your/block

##.  Enable the block

    #.  In ``edx-platform/lms/envs/common.py``, uncomment::

        # from xmodule.x_module import prefer_xmodules
        # XBLOCK_SELECT_FUNCTION = prefer_xmodules

    #.  In ``edx-platform/cms/envs/common.py``, uncomment::

        # from xmodule.x_module import prefer_xmodules
        # XBLOCK_SELECT_FUNCTION = prefer_xmodules

    #.  In ``edx-platform/cms/envs/common.py``, change::

            'ALLOW_ALL_ADVANCED_COMPONENTS': False,

        to::

            'ALLOW_ALL_ADVANCED_COMPONENTS': True,

##.  Add the block to your courses' advanced settings in Studio

    #. Log in to Studio, and open your course
    #. Settings -> Advanced Settings
    #. Change the value for the key ``"advanced_modules"`` to ``paellavideo``


##.  Add your block into your course

    #. Edit a unit
    #. Advanced -> your-block

##. Deploying your XBlock

To deploy your block to your own hosted version of edx-platform, you need to install it
into the virtualenv that the platform is running out of, and add to the list of ``ADVANCED_COMPONENT_TYPES``
in ``edx-platform/cms/djangoapps/contentstore/views/component.py``.

#. Using the XBlock in the course

.In the Studio go to:

![Settings->Advanced Settings](https://raw.githubusercontent.com/polimediaupv/multilanguagexblock/master/doc/img/1.png)

.Add a multilanguage policy key on the advanced_modules keys

TODO CHANGE IMAGE
![Policy key added](https://raw.githubusercontent.com/polimediaupv/multilanguagexblock/master/doc/img/2.png)

.After that, a new button called Advanced will appear in your unit edit view

![Advanced](https://raw.githubusercontent.com/polimediaupv/multilanguagexblock/master/doc/img/3.png)

.And a new option called Multilanguage. Wich will add the component with the default content in english/spanish.

TODO CHANGE IMAGE
![Adding multilanguage](https://raw.githubusercontent.com/polimediaupv/multilanguagexblock/master/doc/img/4.png)

.You can change the content pressing the edit button.

TODO CHANGE IMAGE
![Editing content](https://raw.githubusercontent.com/polimediaupv/multilanguagexblock/master/doc/img/5.png)

.Right now you can modify the content for each of the languages.

![MultilanguageXblock](https://raw.githubusercontent.com/polimediaupv/multilanguagexblock/master/doc/img/6.png)

.Modify the language of the content.

![Select language](https://raw.githubusercontent.com/polimediaupv/multilanguagexblock/master/doc/img/7.png)

.Delete language content

![Delete language content](https://raw.githubusercontent.com/polimediaupv/multilanguagexblock/master/doc/img/8.png)

.Reorder language priority just by dragging the elements, and the priority of appearance will be the order that you see in the editor.   

![Reordering contents](https://raw.githubusercontent.com/polimediaupv/multilanguagexblock/master/doc/img/9.png)