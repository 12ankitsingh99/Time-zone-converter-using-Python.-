from datetime import datetime 
import pytz 

UTC = pytz.utc 

timeZ_Kl = pytz.timezone('Asia/Kolkata') 
timeZ_Ny = pytz.timezone('America/New_York') 
timeZ_Ma = pytz.timezone('Africa/Maseru') 
timeZ_Ce = pytz.timezone('US/Central') 
timeZ_At = pytz.timezone('Europe/Athens') 

dt_Kl = datetime.now(timeZ_Kl) 
dt_Ny = datetime.now(timeZ_Ny) 
dt_Ma = datetime.now(timeZ_Ma) 
dt_Ce = datetime.now(timeZ_Ce) 
dt_At = datetime.now(timeZ_At) 

utc_Kl = dt_Kl.astimezone(UTC) 
utc_Ny = dt_Ny.astimezone(UTC) 
utc_Ma = dt_Ma.astimezone(UTC) 
utc_Ce = dt_Ce.astimezone(UTC) 
utc_At = dt_At.astimezone(UTC) 

print("UTC Format \t\t\t IST Format") 

print(utc_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z'), 
	"\t ", 
	dt_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z')) 

print(utc_Ny.strftime('%Y-%m-%d %H:%M:%S %Z %z'), 
	"\t ", 
	dt_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z')) 

print(utc_Ma.strftime('%Y-%m-%d %H:%M:%S %Z %z'), 
	"\t ", 
	dt_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z')) 

print(utc_Ce.strftime('%Y-%m-%d %H:%M:%S %Z %z'), 
	"\t ", 
	dt_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z')) 

print(utc_At.strftime('%Y-%m-%d %H:%M:%S %Z %z'), 
	"\t ", 
	dt_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z')) 
