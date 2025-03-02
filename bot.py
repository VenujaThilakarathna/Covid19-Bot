from telethon import TelegramClient, events
import json
import requests

APP_ID=7395896
API_HASH='cd3998ddf318dad74d7c506731bc0abc'
BOTT='2100560638:AAHdnGU2Sfmu_iyuLCK1u_icDUFtV67xCgM'


bot = TelegramClient('bot', APP_ID, API_HASH).start(bot_token=BOTT)



def staat(qq):
  url = "https://api.telegram.org/bot"+BOTT+"/sendphoto"
  data = {
    "chat_id": str(qq),
    "photo": "https://telegra.ph/file/ece9c5aedd5d44a04c184.jpg",
    "caption": "ශ්‍රී ලංකාවේ කොරෝනා තතු එසැනින් දැනගන්න. @TheVndCovidbot Group එකට Add කරගත් පසු ස්වයංක්‍රියව නවතම කොරෝනා තතු ලබාගත හැක.  වැඩි විස්තර සදහා /help භාවිතා කරන්න.  Powered by @Venuja_Sadew 🇱🇰",
    "parse_mode": "HTML",
    "reply_markup": {
        "inline_keyboard": [
            [
                {
                    "text": "➕ Add me to your Group",
                    "url": "https://t.me/TheVndCovidbot?startgroup=new"
                }, 
                {
                    "text": "🔊 Channel",
                    "url": "https://t.me/VndBotSupport"
                }
            ]
        ]
    }
}
  headers = {'Content-type': 'application/json'}
  r = requests.post(url, data=json.dumps(data), headers=headers)

def staa():
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
                    '<b>🇱🇰 ලංකාවේ තත්ත්වය</b>' + '\n' + '\n'  +
                    '🤒 තහවුරු කරනලද රෝගීන් සංඛ්‍යාව(සමුච්චිත) = ' + '<code>' +
                    local_total_cases + '</code>' + '\n' +
                    '🤕 ප්‍රතිකාර ලබන රෝගීන් සංඛ්‍යාව = ' + '<code>' + local_active_cases + '</code>' +
                    '\n' + '😷 නව රෝගීන් සංඛ්‍යාව = ' + '<code>' + local_new_cases + '</code>' +
                    '\n' +
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
                    '~Powered by @Venuja_Sadew 🇱🇰 ~')
    return textt




@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    staat(event.original_update.message.peer_id.user_id)
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/corona'))
async def corona(event):
    await event.respond(staa(),parse_mode='html')
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/help'))
async def help(event):
    await event.respond('නවතම කොරෝනා ප්‍රවෘත්ති බැලීමට /corona command භාවිතා කරන්න')
    raise events.StopPropagation

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
