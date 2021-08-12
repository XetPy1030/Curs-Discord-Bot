def check(*args):
    if str(args[1].id) in args[0].all_db["accounts"].keys():
        pass
    else:
        args[0].all_db["accounts"].update({str(args[1].id): {"married": False, "married_to": 0, "xp": 0, "married_date": "", "married_request": 0, "admin": False, "enable_msg_reply": True}})