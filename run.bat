set root=D:\Khoa\Anaconda3
call %root%\Scripts\activate.bat D:\KHOA\anaconda3\envs\overangel
::C:\Users\nguye\.conda\envs\overangel
set PYTHONDONTWRITEBYTECODE=1.
set FLASK_APP=index.py
set FLASK_ENV=development
start msedge http://127.0.0.1:5000/
flask run
pause