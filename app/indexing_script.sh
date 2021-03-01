sleep 30
python3 manage.py rebuild_index --noinput

while [ true ]
do
    python3 manage.py update_index --noinput
    sleep 10
done
