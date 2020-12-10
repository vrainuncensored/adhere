import os
from twilio.rest import Client
import sched, time
import schedule


hostPhoneNumber = "+12246287287"
safteyPhoneNumber = "+17038191285"
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC76ba72e79d8e3665d3bd460d944d77d7'
auth_token = '99717eabde4883558063829e8bd27b11'
client = Client(account_sid, auth_token)


def testPhoneNumber(phone_number):
    if len(phone_number) == 10:
        phone_number = "+1" + phone_number
        return True
    else: 
        return False
    
optiInNumbers = ["6188895954", "6188895458"]
print(optiInNumbers)

def confirmationThatMessagesWentOut():
    alertMessage = client.messages \
        .create( 
        body= "The message went out!",
        from_= hostPhoneNumber,
        to= safteyPhoneNumber
        )

def alert_User(phone_number, Name_of_Medication):
    if testPhoneNumber(phone_number):
        alertMessage = client.messages \
        .create( 
        body= "This is a reminder for you to take your " + Name_of_Medication + " medication",
        from_= hostPhoneNumber,
        to= phone_number
        )
        confirmationThatMessagesWentOut()
    else : 
        print("there was an error with the phone number")


def enroll_Patient():
    for number in optiInNumbers:
        if testPhoneNumber(number):
            alertMessage = client.messages \
            .create( 
            body= "This is an alert that you will be receiving text alerts to take you medication",
            from_= hostPhoneNumber,
            to= number
            )
        else: 
            print("there was an error with the phone number")



def settupTime(interval, date , time):
    switch()
#     for number in optiInNumbers:
#         schedule.every(5).seconds.do(alert_User,number,"advil")
        

# operator to run the commands
# enroll_Patient()

schedule.every().day.at("08:00").do(alert_User,"6188895954","Atorvastatin")
schedule.every().day.at("08:00").do(alert_User,"6188895954","Blood Pressure Medication ")
schedule.every().day.at("08:00").do(alert_User,"6188895458","Atorvastatin")
schedule.every().day.at("16:00").do(alert_User,"6182970223","Caffeine + AM Meds")
# need to be added once Pardeep sends me the info 
schedule.every().day.at("16:00").do(alert_User,"618512","Caffeine + AM Meds")
schedule.every().day.at("16:00").do(alert_User,"6182970223","Caffeine + AM Meds")

while True:
   schedule.run_pending()
   time.sleep(1)
