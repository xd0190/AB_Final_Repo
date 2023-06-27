import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled((environ.get('USE_CAPTION_FILTER', 'True')), True)

PICS = (environ.get('PICS', 'https://graph.org/file/3d9a9939aaebaabd92f25.jpg https://graph.org/file/128e8073ebfbe13efab9d.jpg https://graph.org/file/b491fe40914955aa08282.jpg https://graph.org/file/b181811e9018697199af7.jpg https://graph.org/file/3b5fc303f0ab9b003d5c3.jpg https://graph.org/file/5d1c773a8745ea4154620.jpg https://graph.org/file/860713c3a80b8d93108a0.jpg https://graph.org/file/76bb397d23bf1452d54fa.jpg https://graph.org/file/6bc14fed529370071bf41.jpg https://graph.org/file/9f9809736cb9c00f2712e.jpg https://graph.org/file/be1d591f929dc3f95ca8d.jpg https://graph.org/file/2b02ed42de7f8d318c078.jpg https://graph.org/file/be86d02e9717d188d6243.jpg https://graph.org/file/144580c4743a510eea5b6.jpg https://graph.org/file/656eb5e75f6d2d59192d4.jpg https://graph.org/file/b52bbb217214e8bf9fa6b.jpg https://graph.org/file/e0d95c39df961268abd23.jpg https://graph.org/file/a63d628253dad4c783613.jpg https://graph.org/file/84bd1b71bdbd24fad9051.jpg https://graph.org/file/f1a54bed8321df297e064.jpg https://graph.org/file/14613eda76c784eca8ab5.jpg https://graph.org/file/2df68aa85b0249a1ee4e1.jpg https://graph.org/file/1c7c2a32e12073a4fbd67.jpg https://graph.org/file/27e451ed20cfdd8589fb6.jpg https://graph.org/file/5a327130795b2ec686eb2.jpg https://graph.org/file/af3afc2ffde42b6a83ca1.jpg https://graph.org/file/c59cd8ebc91291edb4ef0.jpg https://graph.org/file/242c7b5658b363f204d91.jpg https://graph.org/file/fad8747da38a6dddfd7da.jpg https://graph.org/file/2c307cba69badb9d05fec.jpg https://graph.org/file/b790d37479d667e044f32.jpg https://graph.org/file/459cf563cd7ef6953e6ff.jpg https://graph.org/file/0a5a01c71e70a6e11f405.jpg https://graph.org/file/fbc38b741674064233ad4.jpg https://graph.org/file/f88f8638c64bc001b326a.jpg https://graph.org/file/439aab4c76746defeb405.jpg https://graph.org/file/665007f23adbe584a3443.jpg https://graph.org/file/6f2a6b9a86d2953db2721.jpg https://graph.org/file/5249c369e6285540baba3.jpg https://graph.org/file/20959e7abeb989c120729.jpg https://graph.org/file/f24777d7a29ad1e285c76.jpg https://graph.org/file/c1f82e948bf7db3d597ef.jpg https://graph.org/file/c757cfe94b6d8aeb77b57.jpg https://graph.org/file/6a94e6c7ba9b527b71967.jpg https://graph.org/file/896889cc4caf97ce71a0a.jpg https://graph.org/file/544d66506934c0a5752f2.jpg https://graph.org/file/90ba7358f4f951cb11a52.jpg https://graph.org/file/8b0ffea2a41978d66757f.jpg https://graph.org/file/c723238af02f064fdca1c.jpg https://graph.org/file/4ba687ae781791f426f4e.jpg https://graph.org/file/f5efbf793a68763077584.jpg https://graph.org/file/2ab1743a88824280f3aef.jpg https://graph.org/file/589b33d74581fd6d23618.jpg https://graph.org/file/ce9c0f12f5b7f220830a7.jpg https://graph.org/file/204f3771dfeece0dfef11.jpg https://graph.org/file/eb65ae973a8bdfca3fb78.jpg https://graph.org/file/3367f7d1ece6307c1d974.jpg https://graph.org/file/8c2a0dd5dce03917f02e3.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/46443096bc6895c74a716.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/451f038b4e7c2ddd10dc0.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/5e2d4418525832bc9a1b9.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = is_enabled((environ.get("NO_RESULTS_MSG", 'False')), False)

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
IS_VERIFY = is_enabled((environ.get('IS_VERIFY', 'True')), True)
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', "https://t.me/howtodownloadmovie1200/56")
VERIFY2_URL = environ.get('VERIFY2_URL', "nestshortener.com")
VERIFY2_API = environ.get('VERIFY2_API', "799f6e6c12bb493a1b1b29bda41f0fded884b5b7")
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'nestshortener.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '799f6e6c12bb493a1b1b29bda41f0fded884b5b7')
IS_SHORTLINK = is_enabled((environ.get('IS_SHORTLINK', 'False')), False)
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "False")), False)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/abmovierequestgroup')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/AB_BotZ_Update')
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ BaBy ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'abmovierequestgroup')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
