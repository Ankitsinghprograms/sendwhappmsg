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



LICENSE:-

MIT LICENSE

Copyright 2020 Ankit Singh

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
