from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random, smtplib
from email.message import EmailMessage

class ActionSendEmailRLNC(Action):
    def name(self):
        return "action_send_email_rlnc"

    def run(self, dispatcher, tracker, domain):
        rlnc_id = f"RLNC-${random.randint(1000,9999)}"
        issue = tracker.latest_message['intent'].get('name')
        mobile = tracker.get_slot('mobile_number')
        citizenship = tracker.get_slot('citizenship')
        email_id = tracker.get_slot('email_id')
        screenshot = tracker.get_slot('screenshot')
        issue_desc = tracker.get_slot('issue_description')

        msg = EmailMessage()
        msg['Subject'] = f"{issue} - {rlnc_id}"
        msg['From'] = "bot@yourdomain.com"
        msg['To'] = "support@yourdomain.com"
        msg.set_content(f"""
        RLNC ID: {rlnc_id}
        Issue: {issue}
        Mobile: {mobile}
        Citizenship: {citizenship}
        Email: {email_id}
        Screenshot: {screenshot}
        Description: {issue_desc}
        """)

        with smtplib.SMTP('smtp.yourdomain.com') as server:
            server.send_message(msg)

        dispatcher.utter_message(text="Thanks for the request. It will take 2–4 working days to complete your request. Once completed, we will notify you via email.")
        return []
