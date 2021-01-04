# sendwhatsappmsg
This is module which sends Whatsapp Message to any given Mobile no.



Functions:-

	1. sendmsg(message_text)

		Open whatsapp share page to send any given message to any contact.

                

    2. sendmsgafter(message_text, seconds)

		Open whatsapp share page after the seconds given to send given message to any contact.

                

    3. sendmsgat(message_text, hour, minutes, seconds='00')

		Open whatsapp share page at a given time to send given message to any contact.

                

	4. sendmsgtoafter(send_msg_to_mobile_no, message_text, seconds)

		Open whatsapp share page after the seconds given to send given message to any mobile no.

                

	5. sendmsgtoat(send_msg_to_mobile_no, message_text, hour, minutes, seconds='00')

		Open whatsapp share page at a given time to send given message to any mobile no.

                

	6. sendmsgto(send_msg_to_mobile_no, message_text)

		Open whatsapp share page to send any given message to any mobile no.

		

EXAMPLE:-

CODE:-

import sendwhatsappmsg

sendwhatsappmsg.sendmsgat("Hii Do you Know there is a awesome module named sendwhatsappmsg by which you can ssnd message to any mobile no.",20,25)

OUTPUT:-

MESSAGE WIILL BE SENT AT 20:25:00

DON'T CLOSE THIS PROGRAM ELSE MESSAGE WILL NOT BE SENT!!

MESSAGE SENT
