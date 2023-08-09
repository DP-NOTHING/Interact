echo " BUILD START "
py -m pip install -r requirnments.txt
py manage.py collectstatic --noinput --clear
echo " BUILD END"