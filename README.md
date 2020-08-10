# Django_forecast_web
This project attempts to forecast your next sale, this project uses djongo module
to handle mongoDb as an usual ORM

how to run:

Backend:
	navigate to forecast_web
	run the command 
		-pip install -r requirements.txt
	run 
		-python manage.py runserver
		
FrontEnd:
	navigate to folder angular9-forecast-web
	run the command
		-npm start

Note:

if you want to use anoter ports (deafults are django=8000, angular=4200)
please modify target on file file in angular9-forecast-web to solve CORS error