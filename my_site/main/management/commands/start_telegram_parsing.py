from django.core.management.base import BaseCommand
import logging

from .parsing_functions import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                            level=logging.WARNING)

        api_data = open('secured_data.txt', 'r')
        api_id = int(api_data.readline().splitlines()[0])
        api_hash = api_data.readline().splitlines()[0]
        session_name = api_data.readline().splitlines()[0]
        api_data.close()

        print('api_id= {0} api_hash= {1}  session_name= {2}'.format(api_id, api_hash, session_name))
        client = TelegramClient(session_name, api_id, api_hash)

        input_ch = 'viewrussia'  # viewrussia
        output_ch = 'me'

        print("Waiting for new posts on", input_ch, "channel...")

        @client.on(events.NewMessage(chats=input_ch))
        async def normal_handler(event):
            await client.send_message(output_ch, event.message)

            message_to_base(event.message)
            path = 'media/photos/{0}/{1}'.format(AlbumElem.objects.last().pk, AlbumElem.objects.last().title)
            await client.download_media(event.message.media, path)

            img_url = path + '.jpg'
            AlbumElem.objects.last().photo = img_url
            AlbumElem.objects.last().save()
            print("Waiting for new posts on", input_ch, "channel...")

        client.start()
        client.run_until_disconnected()

