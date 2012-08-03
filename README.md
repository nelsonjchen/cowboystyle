# Cowboystyle

Cowboystyle is a proposed stylesheet and set of tools for the stylesheet and
sidebar used in [r/UCSantaBarbara](http://www.reddit.com/r/ucsantabarbara).  

Current Maintainer's Demo/Development Reddits:

* [Temporal](http://www.reddit.com/r/crazysimreddittest)
* [Perma-Day](http://www.reddit.com/r/crazysimreddittesttwo)
* [Perma-Night](http://www.reddit.com/r/crazysimreddittest3)

## Concept

Here are the visual and usability goals of the project that a viewer will
notice:

* Storke Tower is prominently on the right.
  * It is drawn isometrically in pixel art to emphasize it's overall shape
    and color.
  * The tower extends all the way to the bottom.
  * The top of the tower peeks up beyond the subreddit's body like scraping
    the sky.
  * It's a great place to hide an easter egg.
* Strong UCSB colors are used in the header.
* The look of the subreddit changes depending on if the sun is above or
  below the horizon.
  * Colors are adjusted to show that it is night on campus.
  * Images that make up storke tower are swapped for night versions.
  * Users with browsers that support APNG will have a blinking Storke Tower
    that is just like the real thing!  
* Header Reddit Logo text is Retina-display browser friendly.
* Sidebar styling is updated to something a bit more modern.
* Content submit links have been modified to be more prominent.
* Reddit Enhancement Suite elements are taken into consideration for users of
  those extensions to ensure their continued functionality.

## Development

Since there isn't a Ruby on Rails analogue to subreddit styling and sidebar
markdown development for deployment on Heroku, adaptation of existing tools and
homegrown scripts were made.  They're definitely not the most polished and will
probably be specific to r/UCSantaBarbara for some time. These scripts will
allow development of the subreddit's style and content on multiple test
subreddits without affecting the production subreddit.  Finally, a large amount
of time was spent to make this project hostable on Heroku for free with very
minimal maintainence.

### QuickStart

This might not work for everyone but it's a rough guide to getting your system
up and going with Ruby and Python from a fresh. Apologies, it isn't much of
a quickstart but it's the fastest way I can come up with.

1. Install Git
2. Clone this repository
3. Install Heroku Tools
4. Ensure GCC or Clang is installed.
5. Install Virtualenv-burrito
6. Install Pythonz
7. Install Python 2.7.2 through Pythonz
8. Create a virtualenv with the python 2.7.2 binary from Pythonz. Yes, the
   binary is going to be inside the .pythonz dotfolder.
9. Install Rbenv
10. Install Ruby-build
11. Install Ruby 1.9.3 through ruby-build
12. Switch to ruby 1.9.3 through rbenv
13. `cd` to the git repository and run `bundle install`
14. `workon` the virtualenv you created earlier
15. `pip install -r requirements.txt`

If you open a new shell, you'll need to repeat step 12 and 14 before running
anything otherwise the dependencies will not resolve.

You must also prepare three subreddits for testing and development : night,
day, and temporal. *You must upload all required images beforehand or otherwise
the CSS uploading will fail.*

### Tools

Ruby tools include:
* Guard for monitoring changes to source files and involing rake tasks
* Rake for task specification
  * Upload to all the test subreddits at once for development and previewing
    purposes.
* Compass is used to compile the SCSS files to CSS files so we can maintain two
  CSS files and their little differences from the same codebase. We also get
  free SCSS goodies like darken, lighten, mixins, inheritance, and other
  freebies.

Python tools include:
* deploy.py to handle deployment upon enviromental variables
  * Jinja2 is used in deploy.py to do variable subsitution in the markdown
    files.

Recommended tools to install for development include:
* Some form of Linux or OS X. Development may work with Cygwin but support
  won't be guaranteed.
* Git for version control. The code and content is versioned so if something
  goes wrong we can rollback. It also allows for use of sites like GitHub or
  Bitbucket where people can do pull requests against the styling or markdown.
* RVM or rbenv/ruby-build, each with bundler, for running Ruby 1.9.3
* Some form of Virtualenv/pythonz to run virtualenv with Python 2.7.2
* Heroku tools for `foreman` which loads up `.env` files with private login
  details for easy configuration. It is highly recommended that Heroku tools be
  installed even if you are not deploying to Heroku just for the `foreman`
  utility.

For more information on each tool, see the next sections.

### Git

This project places the SCSS and Sidebar Markdown under `git`. It uses
`git-flow` to manage releases and such. As such, development generally happens
in the `develop` branch. Whatever is in the `master` branch is what goes on
Heroku for the periodically updating the CSS.

Even if you don't follow `git-flow`, pull requests are much appreciated. If you
pull request against the `develop` branch, that will be even better.

### Heroku/Foreman/Configuration

This toolkit was adapted to be used with [Heroku](http://heroku.com). You
should be prefixing commands with `foreman run` with a valid `.env` in order to
set proper enviromental variables. `.env` files are ignored by git and will not
be shared so private and local information such as passwords or keys can be
placed into there.  A sample `.env` file is below. Put this `.env` file at the
root of the git repository. 

    REDDIT_USER=crazysim
    REDDIT_PASSWORD=notmyrealpassword
    REDDIT_SUBREDDIT=crazysimreddittest
    REDDIT_STYLESHEET_DAY_FILENAME=stylesheets/day.css
    REDDIT_STYLESHEET_NIGHT_FILENAME=stylesheets/night.css
    REDDIT_STYLESHEET_MODE=auto
    REDDIT_STYLESHEET_COMPILE=true
    REDDIT_SIDEBAR_FILENAME=sidebar.mkdn
    REDDIT_SUBREDDIT_DEV_TEMPORAL=crazysimreddittest
    REDDIT_SUBREDDIT_DEV_DAY=crazysimreddittesttwo
    REDDIT_SUBREDDIT_DEV_NIGHT=crazysimreddittest3

Most of these options are self explanatory. The ones that are not are described
as follows:

* `REDDIT_SUBREDDIT` is the target subreddit that deploy.rb will deploy to.
* `REDDIT_STYLESHEET_MODE` has three options
  * `day` will upload the day CSS
  * `night` will upload the night CSS
  * `auto` will calculate the solar elevation of the sun at Storke Tower and
    upload the appropiate CSS
* `REDDIT_STYLESHEET_COMPILE` determines if `deploy.py` will invoke `compass
  compile`
  * This is required for Heroku as CSS files are generated from only files in
    the `git` repository. More work could be done to precompile in the
    deployment stage on Heroku but it is not worth the headaches.
* `REDDIT_SIDEBAR_FILENAME` is the filename of the sidebar file relative to the
  templates folder.
* `REDDIT_SUBREDDIT_DEV_*` are development subreddits. This is mostly used by
  `rake` to change the `REDDIT_SUBREDDIT` that is passed to `deploy.py`.
  * `TEMPORAL` is uploaded depending on solar elevation. It is meant to be used
    by looking out the window if you're on or near campus and then back at the
    screen.
  * `NIGHT` is the subreddit that is to be uploaded the night stylesheet.
  * `DAY` is the subreddit that is to be uploaded the day stylesheet.

*Remember to have images uploaded onto the test subreddits beforehand!*

It is assumed that you have moderator privileges on all subreddits mentioned in
the `.env` file.

On Heroku, this is the git repository that is meant to be uploaded. There will
be no peristantly running dynos. The only addon used is the Scheduler addon
which should run `rake deploy:deploy` every ten minutes.

## SCSS Compass

CSS is is generated by Compass. Files in the `sass` folder are compiled and the
resulting CSS files are put into the `stylesheets` folder.  everytime deploy.rb
is run with `REDDIT_STYLESHEET_COMPILE=true`, `compass compile` or by the
`guard-compass` plugin in `guard`. 

During compilation, `day.css` and `night.css` are generated inside the
stylesheets folder. Most of their common code is in the `_base.scss` file. Use
of SCSS @imports are done to import colors and different image urls from the `colors`
folder for placement in `day.css` and `night.css`.

You may upload these css files into the test subreddits by editing their
stylesheets manually and pasting in the content from the generated files.
Currently, this is the only way to retrieve real error messages for CSS files.
A rudimentary hack to diff the existing CSS file with the new one is provided
if the stylesheet fails to upload for whatever reason. An issue has been filed
upstream with the reddit library used to fix this.

On reddit, the canonical CSS validation and filter source file is in
[cssfilter.py](https://github.com/reddit/reddit/blob/master/r2/r2/lib/cssfilter.py).
The most common CSS keywords are allowed through that whitelist though cutting
edge keywords like animation or uncommon background-position arguments are not.

## Images

Images must be manually uploaded until the python API allows image uploading.
Only finalized versions are to be put in the `images` folder. Development of
these images happen in a [Dropbox
folder](https://www.dropbox.com/sh/i3qo9cgdgen1bcf/oNpFhT8gF0). There is one
requirement for submitting images for use in this subreddit and that is you
must include the source. The source will be placed into that Dropbox folder.

Images that must be uploaded to the subreddit before uploading CSS include:

* Storke Tower
    * Top Night
        * This special image is an APNG with the top light blinking at 40 times
          per minute. Reddit does not allow gifs. It's a minor detail.
    * Top Day
    * Middle Night
    * Middle Day
* Header Background
    * The Alien without the text but the same dimensions as the logo in
      half DPI. This will have seperate night and day versions in the future.
      The framework has been laid out for such already.

_If these images are not uploaded, CSS uploading will fail!_

One more image that should be uploaded but is not required:
    * A 144dpi image of the subreddit text at 280x80. This image will be
      resquashed to the proper dimensions. The reason for the high DPI is to
      ensure that it looks good on Retina-class displays such as the ones on
      newer Macs, iPads, Android Tablets, Windows 8 UI, and other HiDPI
      displays.

Images for this subreddit were created with Pixen for the tower,
Illustrator/Inkscape for the alien.

The APNG version of the tower is compiled with `apng2asm` which is probably not
in your distribution's repositories. You will most likely have to download this
from their sourceforge site.

### Sidebar

`sidebar.md` is the source for the sidebar. Since the styling may rely on
the ordering of certain elements in the sidebar, the sidebar is placed under
version control as well. `sidebar.md` is currently run through Jinja2 and
may incorporate more variables and features in the future.

## Guard

A Guardfile has been provided. Run `foreman run guard` to automatically monitor
and compile compile the SCSS and upload to test subreddits set by enviromental
variables. Currently, it monitors the CSS files for upload to the
`REDDIT_SUBREDDIT_DEV_NIGHT` and `REDDIT_SUBREDDIT_DEV_DAY` subreddits and
`sidebar.markdown` for upload to `REDDIT_SUBREDDIT_DEV_NIGHT`,
`REDDIT_SUBREDDIT_DEV_DAY`, and `REDDIT_SUBREDDIT_DEV_TEMPORAL` subreddits
simultanously.

## To do and future plans

Unfortunately, the Ruby parts are not very clean and the Python parts are
absolutely not Pythonic. It's a start and a good proof of concept though. It
could be put into production at this moment, pending documentation and
approval. However, massive refactoring, particularly in the Python code should
be done before attempts at adding more ambitious features are added.

## Random Notes

Modded Official logo from http://satedproductions.com/tmp/reddit/alien/
UCSB alien logo and variants from u/snifty.
Initial version of toolkit and Tower by u/crazysim

