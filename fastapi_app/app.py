import asyncio
from email import message
from random import randint
from fastapi import FastAPI, Form, status
from fastapi.responses import FileResponse, RedirectResponse
from twilio.rest import Client
from pydantic import BaseModel
import config

app = FastAPI()
settings = config.Settings()

class UserNumber(BaseModel):
    _user_number: str

class PinNumber(BaseModel):
    _pin: str

pin = randint(1000000, 9999999)
message_ = "Tu código de verificación es: {}".format(pin)
#message = Message(_message=message_)

app = FastAPI()

@app.post("/users_number/", response_model=PinNumber)
async def send_messege(user_number: UserNumber):
    await asyncio.get_event_loop().run_in_executor(
        None, send_whatsapp, user_number._user_number, message_)
    
    return PinNumber(_pin=pin)

def send_whatsapp(to_number, body):
    client = Client(settings.twilio_account_sid, settings.twilio_auth_token)
    return client.messages.create(from_=settings.twilio_phone_number,
                                  to=to_number, body=body)