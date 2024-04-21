echo " BUILD SRART"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --input --clear
echo " BUILD END"