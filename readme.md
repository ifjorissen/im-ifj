##im-ifj 

_____

####Setup (for local development)
##### Make a Python3 Virtual Environment (Pyvenv)

  * `mkdir ~/Envs/im-ifj`
  * `pyvenv ~/Envs/im-ifj`
  * and once you're in the directory where this project is, activate the virtual environment with: `source ~/Envs/im-ifj/bin/activate`

#####Start the Database / Create a Table

  * `pg_ctl start -D /usr/local/var/postgres`
  * `psql -l`  //lists databases
  * `createuser im-ifj_usr` 
  * `createdb -O im-ifj_usr im-ifj_db`

#####Installation

  * `git clone https://github.com/ifjorissen/im-ifj.git`
  * activate the pyvenv (`source ~/Envs/im-ifj/bin/activate`)
  * `pip install -r requirements.txt`
  * `npm install`
  * `bower install`
  * add `bower_components` to the staticfiles_dirs in settings.py




#####To Do:
  * use flatpages application for about, find me, and other pages
  * gallery for photography
  * tag system for blog (and photography) posts
  * migrate from aws to digital ocean