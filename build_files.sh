echo " BUILD START "
python3.11 -m pip install -r requirnment.txt
python3.11 mnage.py collectstatic --noinput --clear
echo " BUILD END"