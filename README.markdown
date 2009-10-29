Pythentic Jobs
=========================================================================================
Pythentic Jobs is a small (pure Python) wrapper around the Authentic Jobs (http://www.authenticjobs.com)
API. I got bored one night, wanted something I could knock out quickly, so... here it is.

Requirements
-----------------------------------------------------------------------------------------------------
Pythentic Jobs requires simpleJSON, because nobody should ever have to willingly see or deal with
XML ever again. Yeah, I'm opinionated like that, deal with it. 

> http://pypi.python.org/pypi/simplejson


Example Use
-----------------------------------------------------------------------------------------------------
> from pythentic_jobs import pythentic
>
> jobs = pythentic(api_key="fajsnfjasdnf...")   
> jobs.getLocations()


Pythentic 3k
-----------------------------------------------------------------------------------------------------
There's a script included that's built for Python 3. It's not guaranteed to work, as I don't actively
maintain it; it's simply there to provide a base to work on. Feel free to contribute back patches on 
this if you so desire.

Questions, Comments, etc?
-----------------------------------------------------------------------------------------------------
Pythentic Jobs should be simple enough that you would hopefully have no questions, but if you do,
feel free to hit me up at the following:

GitHub: (Where you're probably reading this)   
Twitter: ( http://twitter.com/ryanmcgrath )   
Email: (ryan [at] venodesigns dot net)   

Twython is released under an MIT License - see the LICENSE file for more information.
