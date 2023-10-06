if uname -a | grep -q 'Ubuntu'; then
    sudo apt-get install pkg-config libmysqlclient-dev
else
    echo 'Not Ubuntu!!'
fi