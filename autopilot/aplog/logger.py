logging.basicConfig(filename='autopilot.log', level=logging.DEBUG)
logger = colorlog.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(
    colorlog.ColoredFormatter('%(log_color)s%(levelname)-8s%(reset)s %(white)s%(message)s',
        log_colors={
            'DEBUG':    'fg_bold_cyan',
            'INFO':     'fg_bold_green',
            'WARNING':  'bg_bold_yellow,fg_bold_blue',
            'ERROR':    'bg_bold_red,fg_bold_white',
            'CRITICAL': 'bg_bold_red,fg_bold_yellow',
	},secondary_log_colors={}

    ))
logger.addHandler(handler)

logging.info('\n'+200*'-'+'\n'+'---- AUTOPILOT DATA '+180*'-'+'\n'+200*'-')

logging.info('RELEASE='+str(RELEASE))
logging.info('PATH_LOG_FILES='+str(PATH_LOG_FILES))
logging.info('PATH_KEYBINDINGS='+str(PATH_KEYBINDINGS))
logging.info('KEY_MOD_DELAY='+str(KEY_MOD_DELAY))
logging.info('KEY_DEFAULT_DELAY='+str(KEY_DEFAULT_DELAY))
logging.info('KEY_REPEAT_DELAY='+str(KEY_REPEAT_DELAY))
logging.info('FUNCTION_DEFAULT_DELAY='+str(FUNCTION_DEFAULT_DELAY))
logging.info('SCREEN_WIDTH='+str(SCREEN_WIDTH))
logging.info('SCREEN_HEIGHT='+str(SCREEN_HEIGHT))