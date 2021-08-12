import functions.ds_delete as ds_delete
import functions.ds_enable as ds_enable
import functions.ds_help as ds_help
import functions.ds_list as ds_list
import functions.ds_profile as ds_profile
import functions.ds_set as ds_set
#import functions.ds_snake as ds_snake
import conf
async def com(self, message):
    msg = str(message.content)[len(list(conf.cell_char)):].split(" ")
    await getattr(globals()["ds_"+msg[0]], msg[0])(self, message)