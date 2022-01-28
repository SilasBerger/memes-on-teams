./zagreus-server &>/dev/null &

# TODO: Poll localhost:58179/api/version untill status 200 instead
sleep 3

cd template && ../zagreus-generator build -u && cd ..
