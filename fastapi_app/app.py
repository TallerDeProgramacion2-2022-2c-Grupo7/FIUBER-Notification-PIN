import asyncio
import uvicorn
from email import message
from random import randint
from fastapi import FastAPI, Form, status
from fastapi.responses import FileResponse, RedirectResponse
from twilio.rest import Client
from pydantic import BaseModel
import config

app = FastAPI()
settings = config.Settings()

class PinNumber(BaseModel):
    pin: str
    mensaje: str | None = None


app = FastAPI()

@app.post("/users_number/{user_number}", response_model=PinNumber)
async def send_messege(user_number: str):
    pin_ = str(randint(1000000, 9999999))
    message_ = "Tu código de verificación de FIUBER es: {}".format(pin_)
    await asyncio.get_event_loop().run_in_executor(
        None, send_whatsapp, user_number, message_)
    
    return {"pin":pin_}

def send_whatsapp(to_number, body):
    client = Client(settings.twilio_account_sid, settings.twilio_auth_token)
    return client.messages.create(from_="whatsapp:{}".format(settings.twilio_phone_number),
                                  body=body, to="whatsapp:{}".format(to_number))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)