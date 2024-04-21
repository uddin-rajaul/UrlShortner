echo " BUILD SRART"
python3.11 -m pip install -r requirements.txt
python3.11 manage.py collectstatic --input --clear
echo " BUILD END"