# import data_generation as dg
import user_interface as ui
import logger as lg
import crud


# dg.start() # генерация базы контактов
lg.logging.info('Start')
crud.init_data_base('emploees.csv')
ui.ls_menu()