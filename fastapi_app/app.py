import asyncio
import uvicorn
from email import message
from fastapi import FastAPI, Form, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse
from twilio.rest import Client
from pydantic import BaseModel
import config
import firebase_admin
from firebase_admin import credentials
from firebase_credentials import admin_credentials
from id_token import IdTokenMiddleware

firebase_credentials = credentials.Certificate(admin_credentials)
firebase_admin.initialize_app(firebase_credentials)

class Body(BaseModel):
    to_number: str
    verification_code: str

app = FastAPI()
settings = config.Settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.add_middleware(IdTokenMiddleware)


app = FastAPI()

@app.post("/send_pin/")
async def send_messege(body: Body):
    message_ = "Tu código de verificación de FIUBER es: {}".format(body.verification_code)
    future = await asyncio.get_event_loop().run_in_executor(
        None, send_whatsapp, body.to_number, message_)
    
    return future.add_done_callback(callback)

def send_whatsapp(to_number, body):
    client = Client(settings.twilio_account_sid, settings.twilio_auth_token)
    return client.messages.create(from_="whatsapp:{}".format(settings.twilio_phone_number),
                                  body=body, to="whatsapp:{}".format(to_number))

def callback(future):
    if future.exception():
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Error al enviar el mensaje")
    
    return future.result()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)