from subprocess import call

call("pip3 install virtualenv", shell=True)
call("virtualenv env", shell=True)
call("source ./env/bin/activate", shell=True)
call("pip3 install Flask", shell=True)
call("pip3 install requests", shell=True)
call("pip3 install pandas", shell=True)
call("pip3 install nltk", shell=True)
call("pip3 install musicbrainzngs", shell=True)
call("pip3 install scikit-learn", shell=True)
call("pip3 install pyLDAvis", shell=True)
call("pip3 install redis", shell=True)
call("python3 webapp/client.py", shell=True)
