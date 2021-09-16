from telethon import TelegramClient, events
import json
import requests

APP_ID =
API_HASH = ''
BOTT = ''

bot = TelegramClient('bot', APP_ID, API_HASH).start(bot_token = BOTT)

def startt (qq):
    url = "https://api.telegram.org/bot" + BOTT = "/sendphoto"
    data = {
        "chat_id" : str (qq)
        "photo" : "http://newscenter.lk/wp-content/uploads/2020/11/UPDATE_a-700x394-2.jpg"
        "caption" : "ශ්‍රී ලංකාවේ කොරෝනා තතු එසැනින් දැනගන්න. @UBCoronaBot Group එකට Add කරගත් පසු ස්වයංක්‍රියව නවතම කොරෝනා තතු ලබාගත හැක. \n වැඩි විස්තර සදහා /help භාවිතා කරන්න."
        "parse_mode" : HTML
        "reply_markup" : {
            "inline_keyboard":[
                {
                    "text" : "Updates Channel"
                    "URL" : "https://t.me/UvinduBro"
                }
            ]
        }
    }

headers = { Content-type : 'application/json'}
r = requests.post(url, data= json.dumps(data), headers=headers)

def stats ():
    r = requests.get('https://hpb.health.gov.lk/api/get-current-statistical')
    jsondata = json.loads(r.text)
    update_date_time    = str(jsondata['data']['update_date_time'])
    local_new_cases     = str(jsondata['data']['local_new_cases'])
    local_active_cases  = str(jsondata['data']['local_active_cases'])
    local_total_cases   = str(jsondata['data']['local_total_cases'])
    local_deaths        = str(jsondata['data']['local_deaths'])
    local_recovered     = str(jsondata['data']['local_recovered'])
    local_total_number_of_individuals_in_hospitals = str(jsondata['data']['local_total_number_of_individuals_in_hospitals'])
    global_new_cases    = str(jsondata['data']['global_new_cases'])
    global_total_cases  = str(jsondata['data']['global_total_cases'])
    global_deaths       = str(jsondata['data']['global_deaths'])
    global_new_deaths   = str(jsondata['data']['global_deaths'])
    global_recovered    = str(jsondata['data']['global_recovered'])

    textt = str(
            '<b>CURRENT SITUATION</b>' + '\n' + '\n' + '<b>' +
            update_date_time + ' වන විට</b>' + '\n' + '\n' +
            '<b>🇱🇰 ශ්‍රී ලංකාවේ තත්ත්වය</b>' + '\n' + '\n'  +
            '🤒 තහවුරු කරනලද රෝගීන් සංඛ්‍යාව(සමුච්චිත) = ' + '<code>' +
            local_total_cases + '</code>' + '\n' +
            '🤕 ප්‍රතිකාර ලබන රෝගීන් සංඛ්‍යාව = ' + '<code>' + local_active_cases + '</code>' +
            '\n' + '😷 නව රෝගීන් සංඛ්‍යාව = ' + '<code>' + local_new_cases + '</code>' + '\n' +
            '🏥 දැනට රෝහල්වල විමර්ශන යටතේ සිටින පුද්ගලයින් = ' + '<code>' +
            local_total_number_of_individuals_in_hospitals +  '</code>' + '\n' +
            '🙂 සුවය ලබා පිටව ගිය සංඛ්‍යාව = ' + '<code>' + local_recovered + '</code>' + 
            '\n' + '⚰ මරණ සංඛ්‍යාව = ' + '<code>'  + local_deaths + '</code>' + '\n' +
            '\n' + '<b>🌎 ලොව පුරා තත්ත්වය</b>' + '\n' +
            '\n' + '🤒 තහවුරු කරනලද රෝගීන් සංඛ්‍යාව (සමුච්චිත) = ' '<code>'  +
            global_total_cases + '</code>' + '\n' + '😷 නව රෝගීන් සංඛ්‍යාව = ' '<code>'  +
            global_new_cases + '</code>' + '\n' + '⚰ මරණ සංඛ්‍යාව = ' '<code>'  +
            global_deaths + '</code>' + '\n' + '🙂 සුවය ලැබූ සංඛ්‍යාව = ' '<code>'  +
            global_recovered + '</code>' + '\n' + '\n' + '\n' +
            '✅ සියලු තොරතුරු රජයේ සහ පිලිගත් මුලාශ්‍ර මගිනි' + '\n' +
            '~ @UvinduBro 🇱🇰 ~')

    return textt




@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    startt (event.original_update.message.peer_id.user_id)
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/covid'))
async def stats(event):
     await event.respond(stats(), parse_mode='HTML')
     raise events.StopPropagation


def main():
    """Started"""
    bot.run_until_disconected()

if __name__ == '__main__':
    main()
